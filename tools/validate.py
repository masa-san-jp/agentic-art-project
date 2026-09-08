#!/usr/bin/env python3
"""Validate the public catalog and reject rewritten Production plans."""

from __future__ import annotations

import argparse
import hashlib
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from tools import catalog_sync  # noqa: E402
from tools.attestation_receiver import check_envelope, configured_producer


HASH64 = re.compile(r"^[0-9a-f]{64}$")
SHA40 = re.compile(r"^[0-9a-f]{40}$")
PLAN_ID = re.compile(r"^P[0-9]{4}$")
CANONICAL_STATUS = "ready-for-publication"
BLOCKED_STATUS = "blocked-missing-canonical"
LAYOUT_CONTRACT = {
    "canonical_plan.source_repository": "agentic-art-production",
    "canonical_plan.source_artifact": "03_plan/production-plan.md",
    "canonical_plan.target_artifact": "plan.md",
    "canonical_plan.projection_contract": "canonical-plan-projection/v2",
    "canonical_plan.body_transform": "none",
    "canonical_plan.receiver_validator": "python3 tools/validate.py --check",
    "canonical_plan.migration_registry": "plans/migration.yaml",
}


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def mapping_fields(path: Path) -> dict[str, str]:
    """Read the closed scalar mapping subset used by metadata/layout files."""
    fields: dict[str, str] = {}
    parents: list[tuple[int, str]] = []
    pattern = re.compile(r'^(?P<indent> *)(?P<key>"?[a-z][a-z0-9_]*"?):(?:\s*(?P<value>.*))?$')
    for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        if not line.strip() or line.lstrip().startswith(("#", "- ")):
            continue
        match = pattern.match(line)
        if match is None:
            continue
        indent = len(match.group("indent"))
        if indent % 2:
            raise ValueError(f"{path}:{number}: mapping indentation must use two spaces")
        while parents and parents[-1][0] >= indent:
            parents.pop()
        key = match.group("key").strip('"')
        value = (match.group("value") or "").strip()
        dotted = ".".join([item[1] for item in parents] + [key])
        if value:
            fields[dotted] = catalog_sync._scalar(value)
        else:
            parents.append((indent, key))
    return fields


def canonical_plan_errors(content: bytes, location: str = "plan.md") -> list[str]:
    """A standalone body never establishes canonical status."""
    return [f"{location}: canonical Production attestation and projection provenance required"]


def validate_layout(root: Path) -> list[str]:
    path = root / "public-project.yaml"
    if not path.is_file():
        return ["public-project.yaml: missing layout contract"]
    try:
        fields = mapping_fields(path)
    except (OSError, UnicodeError, ValueError) as exc:
        return [f"public-project.yaml: unreadable layout contract: {exc}"]
    errors: list[str] = []
    for key, expected in LAYOUT_CONTRACT.items():
        if fields.get(key) != expected:
            errors.append(f"public-project.yaml: {key} must be {expected!r}")
    return errors


def validate_record(root: Path, record: dict[str, str]) -> list[str]:
    public_id = record.get("id", "<unknown>")
    location = record.get("path", public_id)
    errors: list[str] = []
    if PLAN_ID.fullmatch(public_id) is None:
        return [f"{location}: invalid plan ID"]
    slug = record.get("slug", "")
    if location != f"plans/{public_id}-{slug}":
        errors.append(f"{location}: path must match ID and slug")
    directory = root / location
    if not directory.is_dir() or directory.is_symlink():
        return errors + [f"{location}: record directory is missing or unsafe"]
    metadata_path = directory / "metadata.yaml"
    readme_path = directory / "README.md"
    if not metadata_path.is_file() or not readme_path.is_file():
        return errors + [f"{location}: README.md and metadata.yaml are required"]
    try:
        metadata = mapping_fields(metadata_path)
    except (OSError, UnicodeError, ValueError) as exc:
        return errors + [f"{location}/metadata.yaml: invalid: {exc}"]
    for key in ("id", "title", "slug", "status", "visibility", "rights_status", "content_sha256"):
        if metadata.get(key) != record.get(key):
            errors.append(f"{location}: metadata {key} differs from index")
    if record.get("visibility") != "public" or record.get("rights_status") != "cleared":
        errors.append(f"{location}: public visibility and cleared rights are required")
    digest = record.get("content_sha256", "")
    if HASH64.fullmatch(digest) is None or record.get("source_key") != "plan:" + record.get("source_identity", "") or not record.get("source_identity"):
        errors.append(f"{location}: source_key must bind stable source identity; body SHA-256 is separate")
    if record.get("status") != CANONICAL_STATUS:
        return errors + [f"{location}: noncanonical legacy record requires metadata-only migration"]
    plan_path = directory / "plan.md"
    if not plan_path.is_file() or plan_path.is_symlink():
        return errors + [f"{location}: canonical plan.md is missing or unsafe"]
    if sha256_file(plan_path) != digest:
        errors.append(f"{location}/plan.md: body hash differs from index")
    if (directory / "summary.md").exists():
        errors.append(f"{location}: summary must not remain in canonical collection")
    try:
        check_envelope(directory, metadata, record, producer_repository=configured_producer(root))
    except (ValueError, OSError, KeyError, TypeError, AttributeError) as exc:
        errors.append(f"{location}: {exc}")

    return errors


def validate(root: Path = ROOT) -> list[str]:
    errors = validate_layout(root)
    try:
        records = catalog_sync.load_plans(root / "plans/index.yaml")
    except (OSError, UnicodeError, catalog_sync.CatalogError) as exc:
        return errors + [f"plans/index.yaml: {exc}"]
    if len({record.get("source_identity") for record in records}) != len(records):
        errors.append("plans/index.yaml: stable source identity/revision conflict")
    migration_path = root / "plans/migration.yaml"
    if migration_path.exists():
        try:
            migration = catalog_sync._parse_list_records(migration_path, "records")
            reserved = [row["id"] for row in migration]
            if len(set(reserved)) != len(reserved) or set(reserved) & {row["id"] for row in records}:
                errors.append("plans/migration.yaml: reserved P ID reused or duplicated")
            for row in migration:
                if set(row) != {"id", "source_candidate", "blocking_reason", "unblock_condition"} or not PLAN_ID.fullmatch(row["id"]) or any(not v for v in row.values()):
                    errors.append("plans/migration.yaml: closed metadata-only reservation required")
        except (ValueError, OSError, KeyError) as exc:
            errors.append("plans/migration.yaml: " + str(exc))
    indexed_paths = {record["path"] for record in records}
    actual_paths = {
        path.relative_to(root).as_posix()
        for path in (root / "plans").glob("P[0-9][0-9][0-9][0-9]-*")
        if path.is_dir()
    }
    if indexed_paths != actual_paths:
        errors.append("plans/index.yaml: indexed plan directories differ from the filesystem")
    for record in records:
        errors.extend(validate_record(root, record))
    from tools.catalog_lineage import index_document
    try:
        for item in index_document(root)["records"]:
            if item["status"] == "BLOCKED":
                errors.append(f"{item['path']}: {item['reason']}")
    except (ValueError, OSError, KeyError, TypeError):
        errors.append("catalog lineage: invalid metadata or collection")
    try:
        expected = catalog_sync.expected_files(root)
        for path, content in expected.items():
            if not path.exists() or path.read_text(encoding="utf-8") != content:
                errors.append(f"{path.relative_to(root)}: generated catalog block is stale")
    except (OSError, UnicodeError, catalog_sync.CatalogError) as exc:
        errors.append(f"catalog: {exc}")
    return errors


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="validate without writing")
    parser.parse_args(argv)
    errors = validate()
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print("OK: public catalog and canonical plans are valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
