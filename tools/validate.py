#!/usr/bin/env python3
"""Validate the public catalog and its plan provenance boundary.

The public catalog is deliberately small.  README files may be written for
people, but a plan body is either the exact Production artifact or it is
explicitly blocked from the executable catalog.  This validator uses only the
standard library so the public repository remains dependency-free.
"""

from __future__ import annotations

import argparse
import hashlib
import re
import sys
from pathlib import Path

try:
    from . import catalog_sync
except ImportError:  # pragma: no cover - direct CLI execution
    import catalog_sync


ROOT = Path(__file__).resolve().parents[1]
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
HEX64 = re.compile(r"^[0-9a-f]{64}$")


class CatalogValidationError(ValueError):
    """Raised for malformed public catalog input."""


def _scalar(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] == '"':
        return value[1:-1].replace('\\"', '"')
    if len(value) >= 2 and value[0] == value[-1] == "'":
        return value[1:-1].replace("''", "'")
    return value


def _top_level(text: str, key: str) -> str | None:
    pattern = re.compile(rf"^{re.escape(key)}:\s*(.*?)\s*$", re.MULTILINE)
    match = pattern.search(text)
    return _scalar(match.group(1)) if match else None


def _nested(text: str, section: str, key: str) -> str | None:
    section_match = re.search(rf"^{re.escape(section)}:\s*$", text, re.MULTILINE)
    if not section_match:
        return None
    remainder = text[section_match.end():]
    next_section = re.search(r"^\S[^:]*:\s*$", remainder, re.MULTILINE)
    block = remainder[: next_section.start()] if next_section else remainder
    match = re.search(rf"^  {re.escape(key)}:\s*(.*?)\s*$", block, re.MULTILINE)
    return _scalar(match.group(1)) if match else None


def canonical_plan_findings(content: bytes, location: str = "plan.md") -> list[str]:
    """Return findings for a Production `production-plan.md` body."""

    try:
        text = content.decode("utf-8")
    except UnicodeDecodeError:
        return [f"{location}: plan body must be UTF-8"]
    lines = text.splitlines()
    if not lines or lines[0] != CANONICAL_HEADINGS[0]:
        return [f"{location}: first line must be {CANONICAL_HEADINGS[0]!r}"]
    positions: list[int] = []
    findings: list[str] = []
    for heading in CANONICAL_HEADINGS:
        matches = [index for index, line in enumerate(lines) if line == heading]
        if len(matches) != 1:
            findings.append(f"{location}: required heading missing or duplicated: {heading}")
        else:
            positions.append(matches[0])
    if len(positions) == len(CANONICAL_HEADINGS) and positions != sorted(positions):
        findings.append(f"{location}: canonical headings are out of order")
    metadata_end = positions[2] if len(positions) >= 3 else 0
    metadata = lines[:metadata_end]
    for row in METADATA_ROWS:
        if not any(line.startswith(row) for line in metadata):
            findings.append(f"{location}: metadata row is missing: {row}")
    if "sanitized-public-plan" in text or "限定して整理した公開版" in text:
        findings.append(f"{location}: summarized public-plan marker is not canonical")
    return findings


def _validate_metadata(plan_id: str, metadata_path: Path, plan_bytes: bytes, plan_findings: list[str]) -> list[str]:
    text = metadata_path.read_text(encoding="utf-8")
    findings: list[str] = []
    if _top_level(text, "id") != plan_id:
        findings.append(f"{metadata_path}: id does not match {plan_id}")
    digest = hashlib.sha256(plan_bytes).hexdigest()
    if _top_level(text, "content_sha256") != digest:
        findings.append(f"{metadata_path}: content_sha256 does not match plan.md")
    state = _top_level(text, "plan_state")
    if state not in {"canonical-plan", "blocked-missing-canonical"}:
        findings.append(f"{metadata_path}: plan_state must be canonical-plan or blocked-missing-canonical")
    if state == "blocked-missing-canonical":
        for key, expected in (("classification", "blocked-missing-canonical"), ("execution_status", "blocked")):
            if _top_level(text, key) != expected:
                findings.append(f"{metadata_path}: blocked record must set {key}: {expected}")
        return findings
    if plan_findings:
        findings.extend(plan_findings)
    projection = _nested(text, "projection", "mode")
    transform = _nested(text, "projection", "body_transform")
    if _nested(text, "projection", "contract_version") != "canonical-plan-projection/v1":
        findings.append(f"{metadata_path}: canonical projection contract is missing")
    if projection != "AUTOMATIC_PLAN" or transform != "none":
        findings.append(f"{metadata_path}: canonical plan must declare AUTOMATIC_PLAN and body_transform: none")
    provenance_hash = _nested(text, "provenance", "canonical_sha256")
    if provenance_hash not in {digest, f"sha256:{digest}"}:
        findings.append(f"{metadata_path}: provenance canonical_sha256 does not match plan.md")
    if _nested(text, "provenance", "source_repository") != "agentic-art-production":
        findings.append(f"{metadata_path}: provenance source_repository must be agentic-art-production")
    if not HEX64.fullmatch((_nested(text, "provenance", "source_commit") or "")):
        findings.append(f"{metadata_path}: provenance source_commit must be a 40-character SHA")
    if not _nested(text, "provenance", "source_run_id"):
        findings.append(f"{metadata_path}: provenance source_run_id is required")
    return findings


def validate_catalog(root: Path = ROOT) -> list[str]:
    findings: list[str] = []
    try:
        plans = catalog_sync.load_plans(root / "plans/index.yaml")
    except (OSError, catalog_sync.CatalogError) as exc:
        return [f"catalog: {exc}"]
    for record in plans:
        record_root = root / record["path"]
        plan_path = record_root / "plan.md"
        metadata_path = record_root / "metadata.yaml"
        if not plan_path.is_file() or not metadata_path.is_file():
            findings.append(f"{record['id']}: plan.md and metadata.yaml are required")
            continue
        try:
            plan_bytes = plan_path.read_bytes()
            body_findings = canonical_plan_findings(plan_bytes, str(plan_path))
            findings.extend(_validate_metadata(record["id"], metadata_path, plan_bytes, body_findings))
        except (OSError, UnicodeDecodeError) as exc:
            findings.append(f"{record['id']}: cannot read public record: {exc}")
    return findings


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="validate the public catalog")
    args = parser.parse_args(argv)
    if not args.check:
        parser.error("use --check")
    findings = validate_catalog()
    if findings:
        for finding in findings:
            print(f"public-catalog: {finding}", file=sys.stderr)
        return 1
    print("public-catalog: canonical plan and blocked-record checks passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
