"""Verify public envelope integrity and layout, without owning Production semantics."""
from __future__ import annotations
import hashlib
import json
from pathlib import Path, PurePosixPath
import re
import xml.etree.ElementTree as ET


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def canonical(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"), allow_nan=False).encode()


def safe_asset(path):
    if not isinstance(path, str) or not re.fullmatch(r"media/[A-Za-z0-9._/-]+", path) or any(p in {".", ".."} for p in path.split("/")) or str(PurePosixPath(path)) != path:
        raise ValueError("unsafe public asset path")
    return path


def configured_producer(root=None):
    from tools.catalog_sync import load_repositories
    code_root = Path(__file__).resolve().parents[1]
    registry = (Path(root) if root is not None else code_root) / "docs/repositories.yaml"
    if not registry.is_file():
        registry = code_root / "docs/repositories.yaml"
    matches = [row["full_name"] for row in load_repositories(registry) if row["id"] == "agentic-art-production"]
    if len(matches) != 1 or not re.fullmatch(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+", matches[0]):
        raise ValueError("configured Production repository required")
    return matches[0]


def check_envelope(directory, metadata, index, *, producer_repository=None):
    directory = Path(directory)
    if directory.is_symlink() or not directory.is_dir():
        raise ValueError("public record directory is missing or unsafe")
    # macOS exposes temporary roots through aliases such as /tmp -> /private/tmp.
    # Resolve the trusted record root once, then reject only links below it.
    directory = directory.resolve(strict=True)
    path = directory / "public-plan-attestation.json"
    if not path.is_file() or path.is_symlink():
        raise ValueError("Production attestation is missing or unsafe")
    raw = path.read_bytes(); a = json.loads(raw)
    if raw != canonical(a) + b"\n":
        raise ValueError("Production attestation bytes are not canonical")
    if a.get("contract_version") != "production-public-plan-attestation/v1":
        raise ValueError("Production attestation contract required")
    integrity = a["integrity"]
    if integrity != {"canonicalization": "json-sort-keys-compact-utf8-v1", "content_sha256": "sha256:" + digest(canonical({k:v for k,v in a.items() if k != "integrity"}))}:
        raise ValueError("attestation integrity mismatch")
    if a["body_transform"] != "none" or a["external_effects_authorized"] is not False or a["validator"]["status"] != "PASSED":
        raise ValueError("validated no-transform attestation required")
    if a["producer"]["repository"] != (producer_repository or configured_producer()) or not re.fullmatch(r"[0-9a-f]{40}", a["producer"]["commit"]) or not a["producer"]["generator"] or not a["producer"]["renderer_contract_version"]:
        raise ValueError("Production producer provenance missing")
    if not a["coverage"] or any(row.get("status") != "VALIDATED" for row in a["coverage"]):
        raise ValueError("Production semantic validation evidence missing")
    # Names/number of domains and renderer headings remain exclusively Production-owned.
    body = (directory / "plan.md").read_bytes()
    human = a["human_plan"]
    if human["path"] != "03_plan/production-plan.md" or human["media_type"] != "text/markdown" or human["sha256"] != "sha256:" + digest(body) or human["byte_length"] != len(body):
        raise ValueError("attested body hash/length mismatch")
    if type(a["plan_revision"]) is not int or a["plan_revision"] < 1:
        raise ValueError("positive plan revision required")
    identity = a["project_id"] + "#" + a["plan_id"]
    expected = {"source_identity": identity, "plan_revision": str(a["plan_revision"]), "production_repository": a["producer"]["repository"], "production_commit": a["producer"]["commit"], "content_sha256": digest(body), "attestation_sha256": digest(raw), "projection_contract": "canonical-plan-projection/v2", "projection_mode": "AUTOMATIC_PLAN", "body_transform": "none", "plan_state": "canonical", "visibility": "public", "external_effects_authorized": "false"}
    for field, value in expected.items():
        if metadata.get(field) != value or index.get(field) != value:
            raise ValueError("metadata/index attestation mismatch: " + field)
    for field, value in {'contract_version':'canonical-plan-projection/v2','mode':'AUTOMATIC_PLAN','canonical_artifact':'production-plan.md'}.items():
        if metadata.get(field)!=value or index.get(field)!=value:
            raise ValueError('projection metadata contract mismatch: '+field)
    if json.loads(metadata.get('assets','null'))!=a['assets'] or metadata.get('assets')!=index.get('assets'):
        raise ValueError('projection metadata asset manifest mismatch')
    if not metadata.get("source_run_id") or metadata.get("source_run_id") != index.get("source_run_id") or not metadata.get("production_state") or metadata.get("production_state") != index.get("production_state"):
        raise ValueError("source run and separate production state required")
    review = a["publication_review"]
    if any(review.get(field) != "PASSED" for field in ("content_safety", "rights", "consent")) or not review.get("consent_ref") or not review.get("policy_version") or review.get("body_sha256") != human["sha256"] or review.get("aggregate_sha256") != a["aggregate"]["sha256"]:
        raise ValueError("hash-bound publication review required")
    if sorted(review["assets"], key=lambda row:row["path"]) != a["assets"]:
        raise ValueError("asset rights review mismatch")
    paths = set()
    for asset in a["assets"]:
        if not asset["path"].startswith("03_plan/"):
            raise ValueError("asset source path required")
        relative = safe_asset(asset["path"][8:]); target = directory / relative
        if relative in paths or target.resolve() != target or not target.is_file():
            raise ValueError("duplicate, missing or unsafe asset")
        paths.add(relative); data = target.read_bytes()
        if asset["rights_status"] != "PUBLIC_CLEARED" or not asset["rights_ref"] or asset["sha256"] != "sha256:" + digest(data) or asset["byte_length"] != len(data):
            raise ValueError("asset hash/rights mismatch")
        mime = asset["media_type"]
        if mime == "image/svg+xml":
            try:
                xml = ET.fromstring(data)
            except ET.ParseError as exc:
                raise ValueError("invalid SVG asset") from exc
            if xml.tag.split("}")[-1] != "svg": raise ValueError("asset MIME mismatch")
        elif mime == "image/png":
            if not data.startswith(b"\x89PNG\r\n\x1a\n"): raise ValueError("asset MIME mismatch")
        elif mime == "image/jpeg":
            if not data.startswith(b"\xff\xd8") or not data.endswith(b"\xff\xd9"): raise ValueError("asset MIME mismatch")
        else: raise ValueError("unsupported public asset MIME")
    linked = set()
    for link in re.findall(r"!?\[[^\]]*\]\(([^)]+)\)", body.decode()):
        if not link.startswith(("https://", "http://", "#")): linked.add(safe_asset(link))
    if linked != paths:
        raise ValueError("unlisted or unlinked asset")
    actual = {p.relative_to(directory).as_posix() for p in (directory / "media").rglob("*") if p.is_file()}
    if actual != paths: raise ValueError("unlisted public media file")
    return a
