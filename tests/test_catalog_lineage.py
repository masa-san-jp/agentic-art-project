from __future__ import annotations

import copy
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

from tools import catalog_lineage as lineage, catalog_sync
from tools.attestation_receiver import canonical as attestation_bytes, digest
from tools.validate import validate, validate_record

ROOT = Path(__file__).resolve().parents[1]


def git(root, *args):
    return subprocess.check_output(["git", "-C", str(root), *args], stderr=subprocess.PIPE).decode().strip()


def commit(root, message):
    git(root, "add", "-A")
    git(root, "-c", "user.name=Synthetic fixture", "-c", "user.email=fixture@example.invalid", "commit", "-qm", message)
    return git(root, "rev-parse", "HEAD")


def write_rows(path, rows):
    path.parent.mkdir(parents=True, exist_ok=True)
    text = "version: 1\nrecords:" + (" []\n" if not rows else "\n")
    for row in rows:
        text += "- id: " + json.dumps(row["id"]) + "\n"
        text += "".join("  " + key + ": " + json.dumps(value, ensure_ascii=False) + "\n" for key, value in row.items() if key != "id")
    path.write_text(text)


def metadata(root, row):
    (root / row["path"] / "metadata.yaml").write_text("".join(key + ": " + json.dumps(value, ensure_ascii=False) + "\n" for key, value in row.items() if key != "path"))


def actor(name="a", mode="resume"):
    return {"contract_version": "instance-profile/v1", "instance_id": "origin-" + name,
            "creator_id": "creator-" + name, "mode": mode, "permissions": {"local_knowledge_write": True}}


def files(root):
    return {p.relative_to(root).as_posix(): digest(p.read_bytes()) for p in root.rglob("*")
            if p.is_file() and ".git" not in p.relative_to(root).parts}


class CatalogLineageTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory(prefix="aak13-")
        self.addCleanup(temporary.cleanup)
        self.parent = Path(temporary.name).resolve()
        self.root = self.parent / "catalog"
        self.root.mkdir()
        git(self.root, "init", "-q", "-b", "main")
        (self.root / "docs").mkdir()
        shutil.copyfile(ROOT / "docs/repositories.yaml", self.root / "docs/repositories.yaml")
        shutil.copyfile(ROOT / "public-project.yaml", self.root / "public-project.yaml")
        (self.root / "README.md").write_text("# Synthetic catalog\n" + catalog_sync.CATALOG_START + "\n" + catalog_sync.CATALOG_END + "\n" + catalog_sync.REPOSITORIES_START + "\n" + catalog_sync.REPOSITORIES_END + "\n")
        write_rows(self.root / "plans/index.yaml", [])
        write_rows(self.root / "works/index.yaml", [])
        (self.root / "plans/README.md").write_text("# Plans\n" + catalog_sync.CATALOG_START + "\n" + catalog_sync.CATALOG_END + "\n")
        commit(self.root, "empty synthetic catalog")

    def plan(self, identifier="P0001", *, known=False):
        directory = self.root / "plans" / (identifier + "-synthetic")
        shutil.copytree(ROOT / "tests/fixtures/attested-plan", directory)
        attestation = json.loads((directory / "public-plan-attestation.json").read_text())
        attestation["project_id"] = "production/synthetic-" + identifier.lower()
        attestation["integrity"]["content_sha256"] = "sha256:" + digest(attestation_bytes({k: v for k, v in attestation.items() if k != "integrity"}))
        (directory / "public-plan-attestation.json").write_bytes(attestation_bytes(attestation) + b"\n")
        row = {"id": identifier, "slug": "synthetic", "title": "Synthetic plan " + identifier,
               "path": directory.relative_to(self.root).as_posix(), "status": "ready-for-publication",
               "visibility": "public", "rights_status": "cleared", "source_identity": attestation["project_id"] + "#" + attestation["plan_id"],
               "plan_revision": str(attestation["plan_revision"]), "production_repository": attestation["producer"]["repository"],
               "production_commit": attestation["producer"]["commit"], "content_sha256": digest((directory / "plan.md").read_bytes()),
               "attestation_sha256": digest((directory / "public-plan-attestation.json").read_bytes()),
               "projection_contract": "canonical-plan-projection/v2", "projection_mode": "AUTOMATIC_PLAN", "body_transform": "none",
               "plan_state": "canonical", "production_state": "PLANNING", "external_effects_authorized": "false",
               "source_run_id": "synthetic-" + identifier, "contract_version": "canonical-plan-projection/v2", "mode": "AUTOMATIC_PLAN",
               "canonical_artifact": "production-plan.md", "assets": json.dumps(attestation["assets"], sort_keys=True, separators=(",", ":"))}
        row["source_key"] = "plan:" + row["source_identity"]
        if known:
            row.update(origin_instance_id="origin-a", creator_id="creator-a")
        metadata(self.root, row)
        (directory / "README.md").write_text("[Canonical plan](plan.md)\n")
        rows = catalog_sync._parse_list_records(self.root / "plans/index.yaml", "records")
        write_rows(self.root / "plans/index.yaml", rows + [row])
        return row

    def label(self, row, *, who=None, mode="new"):
        who = who or actor()
        value = lineage.default_lineage(self.root, "plans", row)
        if mode == "new":
            value.update(origin_instance_id=who["instance_id"], creator_id=who["creator_id"])
        lineage.annotate(self.root, row["id"], value, instance=who, mode=mode, expected_sha256=None, apply=True)
        return value

    def synchronize(self):
        for path, content in catalog_sync.expected_files(self.root).items():
            path.write_text(content)

    def published(self, *, who=None):
        row = self.plan()
        value = self.label(row, who=who)
        self.synchronize()
        commit(self.root, "synthetic attributed plan")
        report = lineage.export_catalog(self.root, "example/catalog")
        self.assertEqual("PASSED", report["status"])
        return row, value, report

    def test_aak13_ac1_migration_preserves_known_and_unknown_attribution_without_writes(self):
        known = self.plan(known=True)
        unknown = self.plan("P0002")
        commit(self.root, "legacy synthetic records")
        before = files(self.root)
        preview = lineage.migration_preview(self.root)
        self.assertEqual(before, files(self.root))
        by_id = {p["id"]: p for p in preview["proposals"]}
        self.assertEqual("creator-a", by_id[known["id"]]["lineage"]["creator_id"])
        self.assertEqual("unknown", by_id[unknown["id"]]["lineage"]["creator_id"])
        self.assertEqual("UNKNOWN_ATTRIBUTION", by_id[unknown["id"]]["status"])
        value = self.label(known, who=actor("b", "fork"), mode="preserve")
        self.assertEqual("origin-a", value["origin_instance_id"])
        self.assertEqual(before[known["path"] + "/plan.md"], digest((self.root / known["path"] / "plan.md").read_bytes()))
        invented = lineage.default_lineage(self.root, "plans", unknown)
        invented.update(origin_instance_id="origin-b", creator_id="creator-b")
        for mode in ("new", "preserve"):
            with self.subTest(mode=mode), self.assertRaises(lineage.LineageError):
                lineage.annotate(self.root, unknown["id"], invented, instance=actor("b", "fork"), mode=mode, expected_sha256=None, apply=True)

    def test_aak13_ac2_fork_retains_inherited_origin_and_new_record_uses_active_instance(self):
        first, _, _ = self.published()
        fork = self.parent / "fork"
        subprocess.run(["git", "clone", "-q", str(self.root), str(fork)], check=True, capture_output=True)
        self.root = fork
        second = self.plan("P0002")
        self.label(second, who=actor("b", "fork"))
        self.synchronize(); commit(self.root, "new fork plan")
        result = lineage.export_catalog(self.root, "someone/public-fork")
        identities = {(r["origin_instance_id"], r["record_id"], r["creator_id"]) for r in result["records"]}
        self.assertEqual({("origin-a", first["id"], "creator-a"), ("origin-b", second["id"], "creator-b")}, identities)
        self.assertEqual("someone/public-fork", result["catalog_repository"])

    def test_aak13_ac2_composite_references_distinguish_same_local_id_in_independent_catalogs(self):
        _, _, first = self.published()
        original = self.root
        # Independent genesis has no inherited P0001 to relabel or reuse.
        other = self.parent / "independent"
        shutil.copytree(original, other, ignore=shutil.ignore_patterns(".git", "P0001-synthetic", "lineage-index.json"))
        self.root = other
        write_rows(other / "plans/index.yaml", [])
        git(other, "init", "-q", "-b", "main"); commit(other, "independent empty catalog")
        row = self.plan(); self.label(row, who=actor("b", "new-clone")); self.synchronize(); commit(other, "independent plan")
        second = lineage.export_catalog(other, "someone/independent")
        refs = first["records"] + second["records"]
        self.assertEqual(2, len({(r["origin_instance_id"], r["record_id"]) for r in refs}))
        self.assertEqual({"P0001"}, {r["record_id"] for r in refs})

    def test_aak13_ac3_tamper_summary_unreviewed_and_internal_assets_do_not_export(self):
        row, _, _ = self.published()
        original = files(self.root)
        directory = self.root / row["path"]
        cases = {"summary": ("plan.md", b"# Summary\n"), "body": ("plan.md", (directory / "plan.md").read_bytes() + b" "),
                 "asset": ("media/concept-mockup.svg", b"tampered"), "internal": ("internal-handoff.json", b"{}")}
        for name, (relative, raw) in cases.items():
            with self.subTest(case=name):
                target = directory / relative; prior = target.read_bytes() if target.exists() else None
                target.write_bytes(raw); commit(self.root, "synthetic invalid " + name)
                result = lineage.export_catalog(self.root, "example/catalog")
                self.assertEqual("BLOCKED", result["status"]); self.assertEqual([], result["records"])
                if prior is None: target.unlink()
                else: target.write_bytes(prior)
                commit(self.root, "restore synthetic case")
        self.assertEqual(original, files(self.root))
        a_path = directory / "public-plan-attestation.json"; a = json.loads(a_path.read_text())
        a["publication_review"]["rights"] = "UNKNOWN"
        a["integrity"]["content_sha256"] = "sha256:" + digest(attestation_bytes({k:v for k,v in a.items() if k != "integrity"}))
        a_path.write_bytes(attestation_bytes(a) + b"\n")
        row["attestation_sha256"] = digest(a_path.read_bytes()); metadata(self.root, row); write_rows(self.root / "plans/index.yaml", [row]); commit(self.root, "unreviewed rights")
        self.assertEqual([], lineage.export_catalog(self.root, "example/catalog")["records"])

    def test_aak13_ac4_export_is_read_only_and_references_resolve_to_exact_git_bytes(self):
        row, value, first = self.published()
        before = files(self.root); head = git(self.root, "rev-parse", "HEAD")
        second = lineage.export_catalog(self.root, "example/catalog", snapshot=head)
        self.assertEqual(first, second); self.assertEqual(before, files(self.root)); self.assertEqual(head, git(self.root, "rev-parse", "HEAD"))
        ref = first["records"][0]
        raw = subprocess.check_output(["git", "-C", str(self.root), "show", ref["source_commit"] + ":" + ref["source_locator"]])
        self.assertEqual(ref["content_sha256"], digest(raw)); self.assertEqual(1, ref["canonical_revision"])
        self.assertEqual(row["path"] + "/metadata.yaml#title", ref["comparison"]["theme"]["source_locator"])
        changed = copy.deepcopy(value); changed["revision"] = 2
        changed["derived_from"] = [{key: ref[key] for key in lineage.REF_FIELDS}]
        changed["comparison"]["mechanism"] = {"value": raw.decode().splitlines()[0], "source_locator": "plan.md"}
        old_path = self.root / row["path"] / "lineage.json"; old_hash = digest(old_path.read_bytes())
        with self.assertRaisesRegex(lineage.LineageError, "REVISION_CONFLICT"):
            lineage.annotate(self.root, row["id"], changed, instance=actor(), mode="preserve", expected_sha256="0"*64, apply=True)
        lineage.annotate(self.root, row["id"], changed, instance=actor(), mode="preserve", expected_sha256=old_hash, apply=True)
        self.synchronize(); commit(self.root, "lineage revision with grounded comparison")
        third = lineage.export_catalog(self.root, "example/catalog")
        self.assertEqual(2, third["records"][0]["revision"])
        self.assertEqual(ref["source_commit"], third["records"][0]["derived_from"][0]["source_commit"])
        self.assertEqual("ALREADY_APPLIED", lineage.annotate(self.root, row["id"], changed, instance=actor(), mode="preserve", expected_sha256=old_hash, apply=True)["status"])

    def test_aak13_ac5_plans_cannot_claim_production_or_exhibition(self):
        row = self.plan(); value = lineage.default_lineage(self.root, "plans", row)
        for stage in ("PRODUCED", "EXHIBITED"):
            with self.subTest(stage=stage), self.assertRaisesRegex(lineage.LineageError, "PLAN_IS_NOT"):
                lineage.validate_lineage(self.root, "plans", row, dict(value, stage=stage))
        self.label(row); self.synchronize(); commit(self.root, "planned only")
        self.assertEqual([], validate(self.root))
        result = lineage.export_catalog(self.root, "example/catalog")
        self.assertEqual("PLANNED", result["records"][0]["stage"])
        self.assertEqual("proposed", result["records"][0]["epistemic_status"])

    def test_aak13_ac5_work_stages_require_distinct_reviewed_public_evidence(self):
        _, _, first = self.published()
        plan_ref = {key: first["records"][0][key] for key in lineage.REF_FIELDS}
        directory = self.root / "works/W0001-synthetic"; (directory / "media").mkdir(parents=True)
        (directory / "README.md").write_text("# Synthetic work record\nA fixture assembly report.\n")
        proof = {"contract_version": "public-work-stage/v1", "record_id": "W0001", "origin_instance_id": "origin-a",
                 "creator_id": "creator-a", "stage": "PRODUCED", "epistemic_status": "observed",
                 "observed_at": "2026-09-06T00:00:00+00:00", "evidence_ref": "public-work://synthetic/assembly"}
        evidence = directory / "media/stage-proof.txt"; evidence.write_bytes(lineage.canonical(proof))
        assets = [{"path": "media/stage-proof.txt", "sha256": digest(evidence.read_bytes()),
                   "rights_status": "PUBLIC_CLEARED", "rights_ref": "synthetic-public-review"}]
        row = {"id": "W0001", "slug": "synthetic", "title": "Synthetic work", "path": "works/W0001-synthetic",
               "status": "published", "visibility": "public", "rights_status": "cleared", "source_identity": "work/synthetic-assembly",
               "content_sha256": digest((directory / "README.md").read_bytes()), "assets": json.dumps(assets, sort_keys=True)}
        metadata(self.root, row); write_rows(self.root / "works/index.yaml", [row])
        value = lineage.default_lineage(self.root, "works", row)
        value.update(origin_instance_id="origin-a", creator_id="creator-a", source_plans=[plan_ref], stage="PRODUCED",
                     stage_evidence=[{"source_locator": "media/stage-proof.txt", "content_sha256": assets[0]["sha256"], "epistemic_status": "observed"}])
        with self.assertRaisesRegex(lineage.LineageError, "STAGE_EVIDENCE_REQUIRED"):
            lineage.validate_lineage(self.root, "works", row, dict(value, stage_evidence=[]))
        with self.assertRaisesRegex(lineage.LineageError, "STAGE_EVIDENCE_MISMATCH"):
            lineage.validate_lineage(self.root, "works", row, dict(value, stage="EXHIBITED"))
        lineage.annotate(self.root, row["id"], value, instance=actor(), mode="new", expected_sha256=None, apply=True)
        self.synchronize(); commit(self.root, "synthetic reviewed work evidence")
        report = lineage.export_catalog(self.root, "example/catalog")
        self.assertEqual("PASSED", report["status"])
        work = next(r for r in report["records"] if r["record_id"] == "W0001")
        self.assertEqual("PRODUCED", work["stage"]); self.assertEqual("observed", work["epistemic_status"])
        self.assertEqual(plan_ref, work["source_plans"][0]); self.assertEqual([], validate(self.root))
        # A simulated exhibition remains explicitly simulated, never measured evidence.
        proof.update(stage="EXHIBITED", epistemic_status="simulated", evidence_ref="public-work://synthetic/simulated-exhibition")
        evidence.write_bytes(lineage.canonical(proof)); assets[0]["sha256"] = digest(evidence.read_bytes())
        row["assets"] = json.dumps(assets, sort_keys=True); metadata(self.root, row); write_rows(self.root / "works/index.yaml", [row])
        current_path = directory / "lineage.json"; expected = digest(current_path.read_bytes())
        changed = copy.deepcopy(value); changed.update(revision=2, stage="EXHIBITED", derived_from=[{key: work[key] for key in lineage.REF_FIELDS}])
        changed["stage_evidence"] = [{"source_locator": "media/stage-proof.txt", "content_sha256": assets[0]["sha256"], "epistemic_status": "simulated"}]
        lineage.annotate(self.root, row["id"], changed, instance=actor(), mode="preserve", expected_sha256=expected, apply=True)
        self.synchronize(); commit(self.root, "explicit simulated exhibition")
        work = next(r for r in lineage.export_catalog(self.root, "example/catalog")["records"] if r["record_id"] == "W0001")
        self.assertEqual("simulated", work["epistemic_status"])

    def test_configured_production_repository_keeps_fork_validation_explicit(self):
        row = self.plan()
        registry = self.root / "docs/repositories.yaml"
        registry.write_text(registry.read_text().replace("masa-san-jp/agentic-art-production", "another-owner/production-protocol"))
        self.assertTrue(validate_record(self.root, row))
        path = self.root / row["path"] / "public-plan-attestation.json"
        attestation = json.loads(path.read_text()); attestation["producer"]["repository"] = "another-owner/production-protocol"
        attestation["integrity"]["content_sha256"] = "sha256:" + digest(attestation_bytes({k:v for k,v in attestation.items() if k != "integrity"}))
        path.write_bytes(attestation_bytes(attestation) + b"\n")
        row.update(production_repository="another-owner/production-protocol", attestation_sha256=digest(path.read_bytes()))
        metadata(self.root, row); write_rows(self.root / "plans/index.yaml", [row])
        self.assertEqual([], validate_record(self.root, row))
        self.label(row); self.synchronize(); commit(self.root, "explicit configured producer")
        self.assertEqual("PASSED", lineage.export_catalog(self.root, "another-owner/catalog")["status"])

    def test_reserved_ids_and_uncommitted_revision_history_cannot_be_reused(self):
        row = self.plan(); value = self.label(row)
        changed = dict(value, revision=2)
        expected = digest((self.root / row["path"] / "lineage.json").read_bytes())
        with self.assertRaisesRegex(lineage.LineageError, "PREVIOUS_LINEAGE_NOT_COMMITTED"):
            lineage.annotate(self.root, row["id"], changed, instance=actor(), mode="preserve", expected_sha256=expected, apply=True)
        write_rows(self.root / "plans/migration.yaml", [{"id": row["id"], "source_candidate": "unknown", "blocking_reason": "synthetic reservation", "unblock_condition": "explicit verified recovery"}])
        with self.assertRaisesRegex(lineage.LineageError, "RESERVED_ID_REUSED"):
            lineage.records(self.root)

    def test_closed_metadata_permissions_symlinks_and_dirty_snapshot_fail_closed(self):
        row = self.plan(); value = lineage.default_lineage(self.root, "plans", row)
        for change in ({"raw_voice": "not allowed"}, {"canonical_revision": True}, {"revision": True}):
            with self.subTest(change=change), self.assertRaises(lineage.LineageError):
                lineage.validate_lineage(self.root, "plans", row, dict(value, **change))
        value.update(origin_instance_id="origin-a", creator_id="creator-a")
        denied = actor(); denied["permissions"]["local_knowledge_write"] = False
        with self.assertRaisesRegex(lineage.LineageError, "LOCAL_WRITE"):
            lineage.annotate(self.root, row["id"], value, instance=denied, mode="new", expected_sha256=None, apply=True)
        self.label(row); self.synchronize(); commit(self.root, "valid synthetic catalog")
        (self.root / row["path"] / "README.md").write_text("dirty\n")
        with self.assertRaisesRegex(lineage.LineageError, "CLEAN_FIXED"):
            lineage.export_catalog(self.root, "example/catalog")
        commit(self.root, "public introduction update")
        target = self.root / row["path"] / "plan.md"; raw = target.read_bytes(); target.unlink()
        external = self.parent / "outside.md"; external.write_bytes(raw); target.symlink_to(external)
        commit(self.root, "synthetic forbidden link")
        with self.assertRaisesRegex(lineage.LineageError, "UNSAFE_CATALOG_SNAPSHOT"):
            lineage.export_catalog(self.root, "example/catalog")

    def test_cli_uses_external_destination_profile_and_does_not_mutate_catalog(self):
        _, _, report = self.published(); before = files(self.root)
        profile = self.parent / "destinations.yaml"
        profile.write_text("contract_version: output-destinations/v1\ndestinations:\n  public_projection_root: " + str(self.root) + "\n")
        result = subprocess.run([sys.executable, str(ROOT / "tools/catalog_lineage.py"), "export", "--destinations-file", str(profile), "--repository", "other-owner/arbitrary-output", "--snapshot", report["knowledge_commit"]], capture_output=True, text=True)
        self.assertEqual(0, result.returncode, result.stderr)
        self.assertEqual("other-owner/arbitrary-output", json.loads(result.stdout)["catalog_repository"])
        self.assertEqual(before, files(self.root)); self.assertNotIn(str(self.root), result.stdout)

    def test_explicit_empty_catalog_has_no_new_evidence(self):
        result = lineage.export_catalog(self.root, "example/empty")
        self.assertEqual("NO_NEW_EVIDENCE", result["status"])
        self.assertEqual([], result["records"])


if __name__ == "__main__":
    unittest.main()
