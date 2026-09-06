"""Owner-local attribution metadata and read-only, Git-bound catalog references."""
from __future__ import annotations

import argparse
from contextlib import contextmanager
from datetime import datetime
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import re
import shutil
import subprocess
import sys
import tempfile
import tarfile

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
from tools import catalog_sync
from tools.validate import mapping_fields, validate_record

ID = re.compile(r"^[PW][0-9]{4}$")
IDENTITY = re.compile(r"^[A-Za-z0-9][A-Za-z0-9_.:-]{0,127}$")
REPOSITORY = re.compile(r"^[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+$")
SHA = re.compile(r"^[0-9a-f]{64}$")
COMMIT = re.compile(r"^[0-9a-f]{40}$")
FIELDS = {"contract_version", "record_id", "revision", "origin_instance_id", "creator_id",
          "source_identity", "content_sha256", "derived_from", "source_plans", "comparison",
          "stage", "stage_evidence", "canonical_revision"}
REF_FIELDS = {"origin_instance_id", "record_id", "revision", "source_repository", "source_commit",
              "source_locator", "content_sha256"}


class LineageError(ValueError):
    pass


def canonical(value):
    return (json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"), allow_nan=False) + "\n").encode()


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def _git(root, *args, required=True):
    result = subprocess.run(["git", "-C", str(root), *args], capture_output=True)
    if result.returncode and required:
        raise LineageError("GIT_SNAPSHOT_UNAVAILABLE")
    return result.stdout


def _object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise LineageError("DUPLICATE_FIELD")
        result[key] = value
    return result


def load_json(path):
    return json.loads(path.read_bytes(), object_pairs_hook=_object,
                      parse_constant=lambda value: (_ for _ in ()).throw(LineageError("NONFINITE_VALUE")))


def safe_path(root, relative):
    if not isinstance(relative, str) or "\\" in relative:
        raise LineageError("UNSAFE_LOCATOR")
    value = PurePosixPath(relative)
    if value.is_absolute() or not value.parts or any(p in {".", ".."} for p in relative.split("/")) or str(value) != relative:
        raise LineageError("UNSAFE_LOCATOR")
    target = root / relative
    if any((root / Path(*value.parts[:i])).is_symlink() for i in range(1, len(value.parts) + 1)):
        raise LineageError("SYMLINK_LOCATOR")
    return target


def records(root):
    if not root.is_absolute() or root.resolve() != root or not root.is_dir():
        raise LineageError("EXPLICIT_CANONICAL_CATALOG_ROOT_REQUIRED")
    result = []
    for kind in ("plans", "works"):
        path = safe_path(root, kind + "/index.yaml")
        for row in catalog_sync._parse_list_records(path, "records"):
            if not ID.fullmatch(row.get("id", "")) or not row["id"].startswith("P" if kind == "plans" else "W"):
                raise LineageError("INVALID_RECORD_ID")
            if row.get("path") != f"{kind}/{row['id']}-{row.get('slug', '')}":
                raise LineageError("INVALID_RECORD_PATH")
            safe_path(root, row["path"])
            result.append((kind, row))
    if len({row["id"] for _, row in result}) != len(result):
        raise LineageError("LOCAL_ID_REUSED")
    migration = safe_path(root, "plans/migration.yaml")
    if migration.exists():
        reserved = {row["id"] for row in catalog_sync._parse_list_records(migration, "records")}
        if reserved & {row["id"] for _, row in result}:
            raise LineageError("RESERVED_ID_REUSED")
    return result


def validate_reference(ref):
    if not isinstance(ref, dict) or set(ref) != REF_FIELDS:
        raise LineageError("REFERENCE_FIELDS")
    if (not ID.fullmatch(str(ref["record_id"])) or not IDENTITY.fullmatch(str(ref["origin_instance_id"]))
            or type(ref["revision"]) is not int or ref["revision"] < 1
            or not REPOSITORY.fullmatch(str(ref["source_repository"]))
            or not COMMIT.fullmatch(str(ref["source_commit"])) or not SHA.fullmatch(str(ref["content_sha256"]))):
        raise LineageError("INVALID_REFERENCE")
    safe_path(Path("/reference-boundary"), ref["source_locator"])


def default_lineage(root, kind, row):
    metadata = mapping_fields(safe_path(root, row["path"] + "/metadata.yaml"))
    return {
        "contract_version": "catalog-lineage/v1", "record_id": row["id"], "revision": 1,
        "origin_instance_id": metadata.get("origin_instance_id", "unknown"),
        "creator_id": metadata.get("creator_id", "unknown"),
        "source_identity": row.get("source_identity", "unknown"),
        "content_sha256": row.get("content_sha256", "unknown"),
        "canonical_revision": int(row["plan_revision"]) if kind == "plans" else None,
        "derived_from": [], "source_plans": [],
        "comparison": {"theme": {"value": row["title"], "source_locator": "metadata.yaml#title"},
                       "mechanism": {"value": None, "source_locator": None}},
        "stage": "PLANNED" if kind == "plans" else "UNKNOWN", "stage_evidence": [],
    }


def read_lineage(root, kind, row):
    path = safe_path(root, row["path"] + "/lineage.json")
    return load_json(path) if path.exists() else default_lineage(root, kind, row)


def validate_lineage(root, kind, row, value):
    if not isinstance(value, dict) or set(value) != FIELDS or value.get("contract_version") != "catalog-lineage/v1":
        raise LineageError("LINEAGE_FIELDS_OR_VERSION")
    if value["record_id"] != row["id"] or type(value["revision"]) is not int or value["revision"] < 1:
        raise LineageError("LINEAGE_ID_OR_REVISION")
    for key in ("origin_instance_id", "creator_id"):
        if not isinstance(value[key], str) or not IDENTITY.fullmatch(value[key]):
            raise LineageError("INVALID_ATTRIBUTION")
    if value["source_identity"] != row.get("source_identity", "unknown") or value["content_sha256"] != row.get("content_sha256", "unknown"):
        raise LineageError("LINEAGE_SOURCE_MISMATCH")
    if (value["canonical_revision"] is not None and type(value["canonical_revision"]) is not int) or value["canonical_revision"] != (int(row["plan_revision"]) if kind == "plans" else None):
        raise LineageError("CANONICAL_REVISION_MISMATCH")
    for key in ("derived_from", "source_plans"):
        if not isinstance(value[key], list):
            raise LineageError("LINEAGE_REFERENCE_ARRAY")
        seen = set()
        for ref in value[key]:
            validate_reference(ref)
            identity = (ref["origin_instance_id"], ref["record_id"], ref["revision"])
            if identity in seen or identity == (value["origin_instance_id"], value["record_id"], value["revision"]):
                raise LineageError("DUPLICATE_OR_CYCLIC_REFERENCE")
            seen.add(identity)
    comparison = value["comparison"]
    if not isinstance(comparison, dict) or set(comparison) != {"theme", "mechanism"}:
        raise LineageError("COMPARISON_FIELDS")
    for item in comparison.values():
        if not isinstance(item, dict) or set(item) != {"value", "source_locator"}:
            raise LineageError("COMPARISON_FIELDS")
        if item["value"] is None and item["source_locator"] is None:
            continue
        if not isinstance(item["value"], str) or not 1 <= len(item["value"]) <= 500:
            raise LineageError("COMPARISON_VALUE")
        if item["source_locator"] == "metadata.yaml#title":
            grounded = item["value"] == row["title"]
        elif item["source_locator"] == ("plan.md" if kind == "plans" else "README.md"):
            grounded = item["value"] in safe_path(root, row["path"] + "/" + item["source_locator"]).read_text()
        else:
            grounded = False
        if not grounded:
            raise LineageError("UNGROUNDED_COMPARISON")
    if value["stage"] not in {"PLANNED", "PRODUCED", "EXHIBITED", "UNKNOWN"} or not isinstance(value["stage_evidence"], list):
        raise LineageError("INVALID_STAGE")
    if kind == "plans" and (value["stage"] != "PLANNED" or value["stage_evidence"]):
        raise LineageError("PLAN_IS_NOT_PRODUCTION_OR_EXHIBITION")
    for evidence in value["stage_evidence"]:
        if (not isinstance(evidence, dict) or set(evidence) != {"source_locator", "content_sha256", "epistemic_status"}
                or evidence["epistemic_status"] not in {"observed", "simulated"}
                or not isinstance(evidence["source_locator"], str) or not evidence["source_locator"].startswith("media/")
                or not SHA.fullmatch(str(evidence["content_sha256"]))):
            raise LineageError("STAGE_EVIDENCE_REQUIRED")
        evidence_path = safe_path(root, row["path"] + "/" + evidence["source_locator"])
        if digest(evidence_path.read_bytes()) != evidence["content_sha256"]:
            raise LineageError("STAGE_EVIDENCE_HASH")
        proof = load_json(evidence_path)
        if (not isinstance(proof, dict) or set(proof) != {"contract_version", "record_id", "origin_instance_id", "creator_id", "stage", "epistemic_status", "observed_at", "evidence_ref"}
                or proof["contract_version"] != "public-work-stage/v1"
                or any(proof[key] != value[key] for key in ("record_id", "origin_instance_id", "creator_id", "stage"))
                or proof["stage"] not in {"PRODUCED", "EXHIBITED"}
                or proof["epistemic_status"] != evidence["epistemic_status"]
                or not isinstance(proof["evidence_ref"], str) or not proof["evidence_ref"].startswith(("https://", "public-work://"))
                or datetime.fromisoformat(proof["observed_at"]).tzinfo is None):
            raise LineageError("STAGE_EVIDENCE_MISMATCH")
    if kind == "works" and value["stage"] in {"PRODUCED", "EXHIBITED"} and not value["stage_evidence"]:
        raise LineageError("STAGE_EVIDENCE_REQUIRED")


def _work_errors(root, row, lineage, git_root=None):
    metadata = mapping_fields(safe_path(root, row["path"] + "/metadata.yaml"))
    if any(row.get(key) != metadata.get(key) for key in ("id", "title", "source_identity", "content_sha256", "status", "rights_status", "visibility", "assets")):
        raise LineageError("WORK_METADATA_MISMATCH")
    if row.get("visibility") != "public" or row.get("rights_status") != "cleared" or row.get("status") != "published":
        raise LineageError("WORK_NOT_REVIEWED")
    if digest(safe_path(root, row["path"] + "/README.md").read_bytes()) != row.get("content_sha256"):
        raise LineageError("WORK_BODY_HASH")
    assets = json.loads(row.get("assets", "null"))
    if not isinstance(assets, list):
        raise LineageError("WORK_ASSET_MANIFEST_REQUIRED")
    allowed = set()
    for asset in assets:
        if (not isinstance(asset, dict) or set(asset) != {"path", "sha256", "rights_status", "rights_ref"}
                or not asset["path"].startswith("media/") or asset["rights_status"] != "PUBLIC_CLEARED" or not asset["rights_ref"]):
            raise LineageError("WORK_ASSET_RIGHTS")
        path = safe_path(root, row["path"] + "/" + asset["path"])
        if asset["path"] in allowed or digest(path.read_bytes()) != asset["sha256"]:
            raise LineageError("WORK_ASSET_HASH")
        allowed.add(asset["path"])
    if any(e["source_locator"] not in allowed for e in lineage["stage_evidence"]):
        raise LineageError("UNREVIEWED_STAGE_EVIDENCE")
    if not lineage["source_plans"]:
        raise LineageError("WORK_SOURCE_PLAN_REQUIRED")
    current = {r["id"]: r for k, r in records(root) if k == "plans"}
    for ref in lineage["source_plans"]:
        plan = current.get(ref["record_id"])
        if plan is None or validate_record(root, plan):
            raise LineageError("SOURCE_PLAN_NOT_CANONICAL")
        source = inspect_record(root, "plans", plan)
        if ("unknown" in (source["origin_instance_id"], source["creator_id"])
                or source["origin_instance_id"] != ref["origin_instance_id"] or source["revision"] != ref["revision"]
                or plan["content_sha256"] != ref["content_sha256"] or ref["source_locator"] != plan["path"] + "/plan.md"
                or digest(_git(git_root or root, "show", ref["source_commit"] + ":" + ref["source_locator"])) != ref["content_sha256"]):
            raise LineageError("SOURCE_PLAN_REFERENCE_MISMATCH")


def inspect_record(root, kind, row, value=None, git_root=None):
    value = read_lineage(root, kind, row) if value is None else value
    validate_lineage(root, kind, row, value)
    if kind == "plans":
        if validate_record(root, row):
            raise LineageError("PLAN_NOT_CANONICAL")
        attestation = load_json(safe_path(root, row["path"] + "/public-plan-attestation.json"))
        media = {asset["path"][8:] for asset in attestation["assets"]}
        allowed = {"README.md", "metadata.yaml", "plan.md", "public-plan-attestation.json", "lineage.json"} | media
    else:
        _work_errors(root, row, value, git_root)
        allowed = {"README.md", "metadata.yaml", "lineage.json"} | {a["path"] for a in json.loads(row["assets"])}
    directory = safe_path(root, row["path"])
    for path in directory.rglob("*"):
        if path.is_symlink() or (path.is_file() and path.relative_to(directory).as_posix() not in allowed):
            raise LineageError("UNLISTED_OR_INTERNAL_ASSET")
    return value


def index_document(root, git_root=None):
    rows = []
    for kind, row in records(root):
        try:
            value = inspect_record(root, kind, row, git_root=git_root)
            status = "UNKNOWN_ATTRIBUTION" if "unknown" in (value["origin_instance_id"], value["creator_id"]) else "VALIDATED"
            rows.append({"collection": kind, "path": row["path"], "status": status, "lineage": value})
        except (ValueError, OSError, KeyError, TypeError) as exc:
            rows.append({"collection": kind, "path": row["path"], "record_id": row["id"], "status": "BLOCKED",
                         "reason": str(exc) if isinstance(exc, LineageError) else "INVALID_PUBLIC_RECORD"})
    return {"contract_version": "catalog-lineage-index/v1", "records": rows}


def migration_preview(root):
    proposals = []
    indexed = index_document(root)["records"]
    for kind, row in records(root):
        value = read_lineage(root, kind, row)
        status = next(r["status"] for r in indexed if r["path"] == row["path"])
        proposals.append({"id": row["id"], "path": row["path"] + "/lineage.json", "lineage": value, "status": status})
    reserved = root / "plans/migration.yaml"
    reservations = catalog_sync._parse_list_records(reserved, "records") if reserved.exists() else []
    return {"status": "REVIEW_REQUIRED", "proposals": proposals, "reserved_ids": [r["id"] for r in reservations], "writes": []}


def annotate(root, record_id, value, *, instance, mode, expected_sha256, apply=False):
    if (instance.get("contract_version") != "instance-profile/v1" or instance.get("mode") not in {"resume", "new-clone", "fork"}
            or not IDENTITY.fullmatch(str(instance.get("instance_id", ""))) or not IDENTITY.fullmatch(str(instance.get("creator_id", "")))
            or "unknown" in (instance.get("instance_id"), instance.get("creator_id"))):
        raise LineageError("EXPLICIT_INSTANCE_REQUIRED")
    permissions = instance.get("permissions", {})
    writable = permissions.get("local_knowledge_write") is True if isinstance(permissions, dict) else False
    writable = writable or instance.get("permissions.local_knowledge_write") == "true"
    if apply and not writable:
        raise LineageError("LOCAL_WRITE_NOT_PERMITTED")
    kind, row = next(((k, r) for k, r in records(root) if r["id"] == record_id), (None, None))
    if row is None:
        raise LineageError("RECORD_NOT_FOUND")
    inspect_record(root, kind, row, value)
    path = safe_path(root, row["path"] + "/lineage.json")
    old = read_lineage(root, kind, row)
    previous = path.read_bytes() if path.exists() else None
    raw = canonical(value)
    if mode == "new":
        if value["origin_instance_id"] != instance["instance_id"] or value["creator_id"] != instance["creator_id"]:
            raise LineageError("NEW_RECORD_INSTANCE_MISMATCH")
        if previous != raw and (_git(root, "rev-parse", "--is-shallow-repository").strip() == b"true"
                or _git(root, "log", "--all", "--format=%H", "--", f"{kind}/{record_id}-*", required=False).strip()):
            raise LineageError("INHERITED_RECORD_IS_NOT_NEW")
    elif mode == "preserve":
        if any(value[key] != old[key] for key in ("origin_instance_id", "creator_id")):
            raise LineageError("INHERITED_ATTRIBUTION_CHANGED")
        if previous is None and _git(root, "show", "HEAD:" + row["path"] + "/metadata.yaml", required=False) != (root / row["path"] / "metadata.yaml").read_bytes():
            raise LineageError("PRESERVE_REQUIRES_COMMITTED_METADATA")
    else:
        raise LineageError("ANNOTATION_MODE_REQUIRED")
    if previous == raw:
        return {"status": "ALREADY_APPLIED", "writes": []}
    if expected_sha256 != (digest(previous) if previous is not None else None):
        raise LineageError("REVISION_CONFLICT")
    if previous is not None and value["revision"] <= old["revision"]:
        raise LineageError("REVISION_CONFLICT")
    if previous is not None:
        if _git(root, "show", "HEAD:" + row["path"] + "/lineage.json", required=False) != previous:
            raise LineageError("PREVIOUS_LINEAGE_NOT_COMMITTED")
        if value["source_identity"] != old["source_identity"]:
            raise LineageError("SOURCE_IDENTITY_CHANGED")
        if kind == "plans" and value["content_sha256"] != old["content_sha256"] and value["canonical_revision"] <= old["canonical_revision"]:
            raise LineageError("REVISION_CONFLICT")
        ancestor = (old["origin_instance_id"], old["record_id"], old["revision"], old["content_sha256"])
        previous_refs = [r for r in value["derived_from"] if (r["origin_instance_id"], r["record_id"], r["revision"], r["content_sha256"]) == ancestor]
        if not any(r["source_locator"] == row["path"] + ("/plan.md" if kind == "plans" else "/README.md")
                   and _git(root, "show", r["source_commit"] + ":" + row["path"] + "/lineage.json", required=False) == previous
                   for r in previous_refs):
            raise LineageError("PREVIOUS_REVISION_REFERENCE_REQUIRED")
    if not apply:
        return {"status": "READY", "record_id": record_id, "lineage_sha256": digest(raw), "writes": []}
    lock = root / ".catalog-lineage.lock"
    descriptor = os.open(lock, os.O_CREAT | os.O_EXCL | os.O_WRONLY, 0o600)
    temporary = None
    try:
        os.close(descriptor)
        if (path.read_bytes() if path.exists() else None) != previous:
            raise LineageError("REVISION_CONFLICT")
        inspect_record(root, kind, row, value)
        with tempfile.NamedTemporaryFile(dir=path.parent, delete=False) as stream:
            temporary = Path(stream.name); stream.write(raw); stream.flush(); os.fsync(stream.fileno())
        os.replace(temporary, path)
    finally:
        if temporary is not None and temporary.exists(): temporary.unlink()
        lock.unlink()
    return {"status": "APPLIED", "record_id": record_id, "lineage_sha256": digest(raw), "writes": [row["path"] + "/lineage.json"]}


@contextmanager
def frozen_catalog(root, head):
    """Read only catalog paths from immutable Git objects, never a mixed worktree."""
    paths = ["plans", "works", "public-project.yaml"]
    if _git(root, "ls-tree", head, "--", "docs/repositories.yaml").strip():
        paths.append("docs/repositories.yaml")
    with tempfile.TemporaryDirectory(prefix="catalog-reference-") as temporary:
        target = Path(temporary).resolve()
        process = subprocess.Popen(["git", "-C", str(root), "archive", head, "--", *paths],
                                   stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
        try:
            with tarfile.open(fileobj=process.stdout, mode="r|") as archive:
                for member in archive:
                    name = member.name.rstrip("/")
                    if not (member.isdir() or member.isfile()) or ".git" in PurePosixPath(name).parts:
                        raise LineageError("UNSAFE_CATALOG_SNAPSHOT")
                    destination = safe_path(target, name)
                    if member.isdir():
                        destination.mkdir(parents=True, exist_ok=True)
                    else:
                        destination.parent.mkdir(parents=True, exist_ok=True)
                        with archive.extractfile(member) as source, destination.open("xb") as output:
                            shutil.copyfileobj(source, output, length=65536)
            if process.wait() != 0:
                raise LineageError("CATALOG_SNAPSHOT_UNAVAILABLE")
            yield target
        finally:
            if process.stdout is not None: process.stdout.close()
            if process.poll() is None: process.kill()
            process.wait()


def export_catalog(root, repository, *, snapshot=None):
    if not REPOSITORY.fullmatch(repository):
        raise LineageError("EXPLICIT_CATALOG_REPOSITORY_REQUIRED")
    head = _git(root, "rev-parse", "HEAD").decode().strip()
    if not COMMIT.fullmatch(head) or (snapshot is not None and snapshot != head) or _git(root, "status", "--porcelain", "--untracked-files=all").strip():
        raise LineageError("CLEAN_FIXED_CATALOG_SNAPSHOT_REQUIRED")
    with frozen_catalog(root, head) as frozen:
        document = index_document(frozen, git_root=root)
    output = []; blocked = []
    for item in document["records"]:
        if item["status"] != "VALIDATED":
            blocked.append({"record_id": item.get("record_id", item.get("lineage", {}).get("record_id")), "status": item["status"]})
            continue
        value = item["lineage"]
        body = item["path"] + ("/plan.md" if item["collection"] == "plans" else "/README.md")
        comparison = {key: {"value": entry["value"], "source_locator": item["path"] + "/" + entry["source_locator"] if entry["source_locator"] else None}
                      for key, entry in value["comparison"].items()}
        stage_evidence = [{**entry, "source_locator": item["path"] + "/" + entry["source_locator"]} for entry in value["stage_evidence"]]
        output.append({"record_id": value["record_id"], "origin_instance_id": value["origin_instance_id"],
                       "creator_id": value["creator_id"], "revision": value["revision"],
                       "source_identity": value["source_identity"], "source_repository": repository,
                       "source_commit": head, "source_locator": body, "content_sha256": value["content_sha256"],
                       "canonical_revision": value["canonical_revision"],
                       "collection": item["collection"], "stage": value["stage"],
                       "epistemic_status": "proposed" if item["collection"] == "plans" else
                           ("simulated" if any(e["epistemic_status"] == "simulated" for e in value["stage_evidence"]) else
                            ("observed" if value["stage_evidence"] else "unknown")),
                       "stage_evidence": stage_evidence, "comparison": comparison,
                       "derived_from": value["derived_from"], "source_plans": value["source_plans"]})
    if _git(root, "rev-parse", "HEAD").decode().strip() != head or _git(root, "status", "--porcelain", "--untracked-files=all").strip():
        raise LineageError("CATALOG_CHANGED_DURING_READ")
    return {"contract_version": "catalog-reference/v1", "status": "BLOCKED" if blocked else ("PASSED" if output else "NO_NEW_EVIDENCE"),
            "code_commit": _git(ROOT, "rev-parse", "HEAD").decode().strip(),
            "code_dirty": bool(_git(ROOT, "status", "--porcelain").strip()),
            "knowledge_commit": head, "catalog_repository": repository, "records": output, "blocked": blocked, "writes": []}


def resolve_catalog_root(root=None, destinations_file=None):
    if root is None and destinations_file is not None:
        profile = mapping_fields(destinations_file)
        if profile.get("contract_version") != "output-destinations/v1":
            raise LineageError("DESTINATIONS_PROFILE_VERSION")
        raw = profile.get("destinations.public_projection_root")
        if not raw: raise LineageError("PUBLIC_CATALOG_ROOT_REQUIRED")
        root = Path(raw)
    selected = root or ROOT
    if not selected.is_absolute() or selected.resolve() != selected or not selected.is_dir():
        raise LineageError("EXPLICIT_CANONICAL_CATALOG_ROOT_REQUIRED")
    return selected


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=["export", "migration", "annotate"])
    parser.add_argument("--root", type=Path)
    parser.add_argument("--destinations-file", type=Path)
    parser.add_argument("--repository")
    parser.add_argument("--snapshot")
    parser.add_argument("--record-id")
    parser.add_argument("--input", type=Path)
    parser.add_argument("--instance-profile", type=Path)
    parser.add_argument("--mode", choices=["new", "preserve"])
    parser.add_argument("--expected-sha256")
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args(argv)
    try:
        root = resolve_catalog_root(args.root, args.destinations_file)
        if args.command == "export":
            if args.apply: raise LineageError("READ_ONLY_EXPORT")
            result = export_catalog(root, args.repository or "", snapshot=args.snapshot)
        elif args.command == "migration":
            if args.apply: raise LineageError("MIGRATION_PREVIEW_ONLY")
            result = migration_preview(root)
        else:
            if not args.input or not args.instance_profile: raise LineageError("ANNOTATION_INPUT_REQUIRED")
            result = annotate(root, args.record_id, load_json(args.input), instance=mapping_fields(args.instance_profile),
                              mode=args.mode, expected_sha256=args.expected_sha256, apply=args.apply)
        print(canonical(result).decode(), end="")
        return 2 if result["status"] == "BLOCKED" else 0
    except LineageError as exc:
        print(json.dumps({"status": "BLOCKED", "reason": str(exc), "writes": []}), file=sys.stderr)
        return 2
    except (ValueError, OSError, KeyError, TypeError, AttributeError):
        print(json.dumps({"status": "BLOCKED", "reason": "CATALOG_CONTRACT_OR_ACCESS_FAILED", "writes": []}), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
