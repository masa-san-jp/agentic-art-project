#!/usr/bin/env python3
"""Validate the public catalog and reject rewritten Production plans."""

from __future__ import annotations

import argparse
import hashlib
import os
import re
import subprocess
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
LOCAL_WORKSPACE_CONTRACT = {
    "contract_version": "repo-local-project-workspace/v1",
    "root": ".agentic-art",
    "config": ".agentic-art/config.yaml",
    "state": ".agentic-art/state",
    "internal": ".agentic-art/internal",
    "staging": ".agentic-art/staging",
    "tracking": "ignored",
}
LOCAL_WORKSPACE_IGNORE_RULE = "/.agentic-art/"
LOCAL_WORKSPACE_PROBE = ".agentic-art/probe"
LOCAL_WORKSPACE_TOKEN = re.compile(r"\.agentic-art(?:[/\\]|$)")


def _lexists(path: Path) -> bool:
    """Return whether a path exists without following a broken symlink."""
    return os.path.lexists(path)


def _public_files(root: Path) -> list[Path]:
    """Return public paths whose contents can become catalog evidence.

    Documentation is intentionally excluded: docs/local-workspace.md and the
    root README explain the private boundary, while records and catalogs must
    never carry a path into it.
    """
    candidates = [
        root / "README.md",
        root / "plans/index.yaml",
        root / "plans/README.md",
        root / "works/index.yaml",
        root / "works/README.md",
        root / "plans/lineage-index.json",
    ]
    for collection in (root / "plans", root / "works", root / "shared"):
        if collection.is_symlink():
            candidates.append(collection)
        elif collection.is_dir():
            candidates.extend(path for path in collection.rglob("*") if path.is_file() or path.is_symlink())
    unique: dict[str, Path] = {}
    for path in candidates:
        if not (path.is_file() or path.is_symlink()):
            continue
        try:
            key = path.relative_to(root).as_posix()
        except ValueError:
            continue
        unique[key] = path
    return [unique[key] for key in sorted(unique)]


def _markdown_links(text: str) -> list[str]:
    """Extract inline and reference-style Markdown destinations."""
    inline = re.findall(r"!?\[[^\]]*\]\(([^)\s]+)(?:\s+['\"][^)]*['\"])?\)", text)
    references = re.findall(r"^\s*\[[^\]]+\]:\s*(\S+)", text, flags=re.MULTILINE)
    return inline + references


def validate_public_workspace_references(root: Path) -> list[str]:
    """Reject private workspace paths from public records and catalog evidence."""
    errors: list[str] = []
    for path in _public_files(root):
        if path.is_symlink():
            errors.append("PUBLIC_LOCAL_WORKSPACE_SYMLINK: public catalog contains an unsafe symlink")
            continue
        try:
            text = path.read_bytes().decode("utf-8")
        except UnicodeDecodeError:
            # Binary public media has no textual locator to inspect here.
            continue
        except OSError:
            errors.append("PUBLIC_LOCAL_WORKSPACE_READ: public catalog file is unreadable")
            continue
        relative = path.relative_to(root).as_posix()
        if relative == "README.md":
            if any(LOCAL_WORKSPACE_TOKEN.search(link) for link in _markdown_links(text)):
                errors.append("PUBLIC_LOCAL_WORKSPACE_REFERENCE: README link enters the private workspace")
        elif LOCAL_WORKSPACE_TOKEN.search(text):
            errors.append("PUBLIC_LOCAL_WORKSPACE_REFERENCE: public record or catalog enters the private workspace")
    return sorted(set(errors))


def validate_local_workspace(root: Path) -> list[str]:
    """Validate the private repo-local workspace boundary without writing."""
    errors: list[str] = []
    ignore_path = root / ".gitignore"
    try:
        ignore_lines = ignore_path.read_text(encoding="utf-8").splitlines()
    except (OSError, UnicodeError):
        ignore_lines = []
    if LOCAL_WORKSPACE_IGNORE_RULE not in ignore_lines:
        errors.append("LOCAL_WORKSPACE_IGNORE: root-anchored /.agentic-art/ rule is required")

    workspace = root / ".agentic-art"
    fixed_paths = (
        (workspace, True),
        (workspace / "config.yaml", False),
        (workspace / "state", True),
        (workspace / "internal", True),
        (workspace / "staging", True),
    )
    unsafe_workspace = False
    for path, directory_expected in fixed_paths:
        if not _lexists(path):
            continue
        if path.is_symlink():
            unsafe_workspace = True
            continue
        if directory_expected and not path.is_dir():
            errors.append("LOCAL_WORKSPACE_LAYOUT: fixed workspace directory has the wrong type")
        elif not directory_expected and not path.is_file():
            errors.append("LOCAL_WORKSPACE_LAYOUT: fixed workspace config has the wrong type")
    if unsafe_workspace:
        errors.append("LOCAL_WORKSPACE_SYMLINK: workspace or fixed child is a symlink")

    git_metadata = root / ".git"
    if _lexists(git_metadata):
        try:
            ignore_result = subprocess.run(
                ["git", "check-ignore", "-q", "--no-index", LOCAL_WORKSPACE_PROBE],
                cwd=root,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
                check=False,
            )
            tracked_result = subprocess.run(
                ["git", "ls-files", "--", ".agentic-art"],
                cwd=root,
                stdout=subprocess.PIPE,
                stderr=subprocess.DEVNULL,
                check=False,
            )
        except (OSError, subprocess.SubprocessError):
            errors.append("LOCAL_WORKSPACE_GIT: Git boundary could not be verified")
        else:
            if ignore_result.returncode != 0:
                errors.append("LOCAL_WORKSPACE_IGNORE: Git does not ignore /.agentic-art/probe")
            if tracked_result.returncode != 0:
                errors.append("LOCAL_WORKSPACE_GIT: Git tracked-file query failed")
            elif tracked_result.stdout.strip():
                errors.append("LOCAL_WORKSPACE_TRACKED: private workspace contains tracked files")

    errors.extend(validate_public_workspace_references(root))
    return sorted(set(errors))


def local_workspace_git_status(root: Path) -> str:
    """Describe whether Git-boundary checks apply to this tree."""
    return "CHECKED" if _lexists(root / ".git") else "NOT_APPLICABLE"


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
            if dotted in fields:
                raise ValueError(f"{path}:{number}: duplicate mapping field")
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
    local_fields = {
        key.removeprefix("local_workspace."): value
        for key, value in fields.items()
        if key.startswith("local_workspace.")
    }
    if local_fields != LOCAL_WORKSPACE_CONTRACT:
        errors.append("public-project.yaml: local_workspace must match the closed v1 contract")
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
    errors.extend(validate_local_workspace(root))
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
    parser.add_argument("--root", type=Path, default=ROOT, help="catalog root to validate")
    args = parser.parse_args(argv)
    root = args.root.resolve()
    errors = validate(root)
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print(f"OK: public catalog and canonical plans are valid (local workspace Git boundary: {local_workspace_git_status(root)})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
