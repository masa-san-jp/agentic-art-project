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


HASH64 = re.compile(r"^[0-9a-f]{64}$")
SHA40 = re.compile(r"^[0-9a-f]{40}$")
PLAN_ID = re.compile(r"^P[0-9]{4}$")
CANONICAL_STATUS = "ready-for-publication"
BLOCKED_STATUS = "blocked-missing-canonical"
CANONICAL_HEADINGS = (
    "# 統合制作計画書",
    "### 計画メタデータ",
    "## 1. 完成像",
    "## 2. テーマ",
    "## 3. メッセージ",
    "## 4. コンセプト",
    "## 5. 調査の要約",
    "### 採択内容と根拠",
    "### 制作リファレンス",
    "### 要件と受入の目的",
    "## 6. できている物",
    "## 7. 制作範囲と成果物",
    "## 8. 技術仕様・材料・資源",
    "## 9. 工程と作業手順",
    "## 10. 試作・受入評価",
    "## 11. 日程と予算",
    "## 12. リスクと未解決事項",
    "## 13. 承認・安全境界",
    "## 14. 人間向け実行前チェックリスト",
    "## 15. 証跡と再現性",
    "### 受け渡し時の注意",
)
METADATA_ROWS = (
    "| 計画 |",
    "| 計画状態 |",
    "| 制作着手可否 |",
    "| handoff |",
    "| 要件カバレッジ |",
    "| クリティカルパス |",
)
LAYOUT_CONTRACT = {
    "canonical_plan.source_repository": "agentic-art-production",
    "canonical_plan.source_artifact": "03_plan/production-plan.md",
    "canonical_plan.target_artifact": "plan.md",
    "canonical_plan.projection_contract": "canonical-plan-projection/v1",
    "canonical_plan.body_transform": "none",
    "canonical_plan.receiver_validator": "python3 tools/validate.py --check",
    "canonical_plan.blocked_summary_artifact": "summary.md",
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
    try:
        text = content.decode("utf-8")
    except UnicodeDecodeError:
        return [f"{location}: canonical plan must be UTF-8"]
    lines = text.splitlines()
    errors: list[str] = []
    positions: list[int] = []
    for heading in CANONICAL_HEADINGS:
        matches = [index for index, line in enumerate(lines) if line == heading]
        if len(matches) != 1:
            errors.append(f"{location}: missing or duplicate canonical heading {heading!r}")
        else:
            positions.append(matches[0])
    if len(positions) == len(CANONICAL_HEADINGS) and positions != sorted(positions):
        errors.append(f"{location}: canonical headings are out of order")
    metadata_end = positions[2] if len(positions) > 2 else 0
    metadata_lines = lines[:metadata_end]
    for prefix in METADATA_ROWS:
        if not any(line.startswith(prefix) for line in metadata_lines):
            errors.append(f"{location}: missing canonical metadata row {prefix!r}")
    if not lines or lines[0] != CANONICAL_HEADINGS[0]:
        errors.append(f"{location}: canonical Production title is missing")
    if "sanitized-public-plan" in text or "限定して整理した公開版" in text:
        errors.append(f"{location}: summarized public plan marker is forbidden")
    return errors


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
    if HASH64.fullmatch(digest) is None or record.get("source_key") != f"plan:{digest}":
        errors.append(f"{location}: source_key/content_sha256 must identify one SHA-256 body")
    status = record.get("status")
    plan_path = directory / "plan.md"
    summary_path = directory / "summary.md"
    readme = readme_path.read_text(encoding="utf-8")
    if status == CANONICAL_STATUS:
        if not plan_path.is_file() or plan_path.is_symlink():
            errors.append(f"{location}: canonical plan.md is missing or unsafe")
            return errors
        if summary_path.exists():
            errors.append(f"{location}: canonical record must not retain summary.md")
        actual = sha256_file(plan_path)
        if actual != digest:
            errors.append(f"{location}/plan.md: body hash differs from index")
        expected_projection = {
            "projection.contract_version": "canonical-plan-projection/v1",
            "projection.mode": "AUTOMATIC_PLAN",
            "projection.canonical_artifact": "production-plan.md",
            "projection.body_transform": "none",
        }
        for key, expected in expected_projection.items():
            if metadata.get(key) != expected:
                errors.append(f"{location}: {key} must be {expected!r}")
        if metadata.get("projection.producer") not in {"tools/run.py", "tools/batch_run.py"}:
            errors.append(f"{location}: projection.producer is not canonical")
        if metadata.get("provenance.source_repository") != "agentic-art-production":
            errors.append(f"{location}: Production source repository is required")
        if SHA40.fullmatch(metadata.get("provenance.source_commit", "")) is None:
            errors.append(f"{location}: Production source commit must be 40 hex")
        if not metadata.get("provenance.source_run_id"):
            errors.append(f"{location}: source run ID is required")
        if metadata.get("provenance.canonical_sha256") != digest:
            errors.append(f"{location}: canonical SHA-256 differs from plan.md")
        if metadata.get("provenance.source_ref") != f"sha256:{digest}":
            errors.append(f"{location}: source_ref differs from plan.md")
        if "[制作プラン本文](plan.md)" not in readme and "[plan.md](plan.md)" not in readme:
            errors.append(f"{location}/README.md: canonical plan link is missing")
        errors.extend(canonical_plan_errors(plan_path.read_bytes(), f"{location}/plan.md"))
    elif status == BLOCKED_STATUS:
        if plan_path.exists():
            errors.append(f"{location}: blocked summary must not be named plan.md")
        if not summary_path.is_file() or summary_path.is_symlink():
            errors.append(f"{location}: blocked summary.md is missing or unsafe")
            return errors
        if sha256_file(summary_path) != digest:
            errors.append(f"{location}/summary.md: body hash differs from index")
        if metadata.get("canonical_plan_available") != "false":
            errors.append(f"{location}: canonical_plan_available must be false")
        if metadata.get("blocking_reason") != "canonical-production-plan-unavailable":
            errors.append(f"{location}: blocking reason is missing")
        if "[旧要約（制作不可）](summary.md)" not in readme or "正本待ち" not in readme:
            errors.append(f"{location}/README.md: blocked status and summary link are required")
    else:
        errors.append(f"{location}: unsupported status {status!r}")
    return errors


def validate(root: Path = ROOT) -> list[str]:
    errors = validate_layout(root)
    try:
        records = catalog_sync.load_plans(root / "plans/index.yaml")
    except (OSError, UnicodeError, catalog_sync.CatalogError) as exc:
        return errors + [f"plans/index.yaml: {exc}"]
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
    try:
        expected = catalog_sync.expected_files()
        for path, content in expected.items():
            if path.read_text(encoding="utf-8") != content:
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
