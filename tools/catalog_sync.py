#!/usr/bin/env python3
"""Synchronize human-readable catalog blocks from the public indexes.

The public projection writes the collection index and collection README.  This
small standard-library-only command keeps the root README's links and the
repository relationship table derived from explicit source files as well.
It intentionally does not discover or copy arbitrary files from an output
directory.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parents[1]
PLAN_INDEX = ROOT / "plans/index.yaml"
PLAN_README = ROOT / "plans/README.md"
ROOT_README = ROOT / "README.md"
REPOSITORY_INDEX = ROOT / "docs/repositories.yaml"

CATALOG_START = "<!-- agentic-art:catalog:start -->"
CATALOG_END = "<!-- agentic-art:catalog:end -->"
REPOSITORIES_START = "<!-- agentic-art:repositories:start -->"
REPOSITORIES_END = "<!-- agentic-art:repositories:end -->"

_FIELD = re.compile(r"^(?P<indent>\s+)(?P<key>[a-z][a-z0-9_]*):\s*(?P<value>.*)$")


class CatalogError(ValueError):
    """Raised when a source catalog does not follow its small YAML contract."""


def _scalar(value: str) -> str:
    value = value.strip()
    if not value:
        return ""
    if value.startswith('"'):
        try:
            parsed = json.loads(value)
        except json.JSONDecodeError as exc:
            raise CatalogError(f"invalid quoted scalar: {value}") from exc
        if not isinstance(parsed, str):
            raise CatalogError(f"expected a string scalar: {value}")
        return parsed
    if value.startswith("'") and value.endswith("'"):
        return value[1:-1].replace("''", "'")
    return value


def _parse_list_records(path: Path, section: str) -> list[dict[str, str]]:
    """Parse the deliberately narrow list-of-flat-mappings YAML used here."""

    lines = path.read_text(encoding="utf-8").splitlines()
    in_section = False
    records: list[dict[str, str]] = []
    current: dict[str, str] | None = None
    for line_number, line in enumerate(lines, start=1):
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if line == f"{section}:":
            in_section = True
            continue
        if not in_section:
            continue
        if line and not line.startswith(" "):
            break
        if line.startswith("  - "):
            if current is not None:
                records.append(current)
            first = line[4:]
            match = _FIELD.match("    " + first)
            if match is None or match.group("key") != "id":
                raise CatalogError(f"{path}:{line_number}: each entry must start with id")
            current = {"id": _scalar(match.group("value"))}
            continue
        if current is None:
            raise CatalogError(f"{path}:{line_number}: field appears before an entry")
        match = _FIELD.match(line)
        if match is None or len(match.group("indent")) != 4:
            raise CatalogError(f"{path}:{line_number}: expected a four-space field")
        current[match.group("key")] = _scalar(match.group("value"))
    if current is not None:
        records.append(current)
    if not records:
        raise CatalogError(f"{path}: section {section!r} contains no entries")
    return records


def load_plans(path: Path = PLAN_INDEX) -> list[dict[str, str]]:
    records = _parse_list_records(path, "records")
    required = {"id", "title", "path", "status", "visibility", "rights_status", "plan_state"}
    for record in records:
        missing = sorted(required - record.keys())
        if missing:
            raise CatalogError(f"{path}: {record.get('id', '<unknown>')} missing {', '.join(missing)}")
        if record["status"] != "published" or record["visibility"] != "public" or record["rights_status"] != "cleared":
            raise CatalogError(f"{path}: {record['id']} is not an eligible public catalog record")
        if record["plan_state"] not in {"canonical-plan", "blocked-missing-canonical"}:
            raise CatalogError(f"{path}: {record['id']} has an invalid plan_state")
        if not record["path"].startswith("plans/"):
            raise CatalogError(f"{path}: {record['id']} path must be under plans/")
    return sorted(records, key=lambda item: item["id"])


def load_repositories(path: Path = REPOSITORY_INDEX) -> list[dict[str, str]]:
    records = _parse_list_records(path, "repositories")
    required = {"id", "full_name", "url", "role", "relation"}
    for record in records:
        missing = sorted(required - record.keys())
        if missing:
            raise CatalogError(f"{path}: {record.get('id', '<unknown>')} missing {', '.join(missing)}")
        if not re.fullmatch(r"https://github\.com/[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+", record["url"]):
            raise CatalogError(f"{path}: {record['id']} has an invalid GitHub URL")
    return records


def _safe_title(title: str) -> str:
    return title.replace("\r", " ").replace("\n", " ").replace("]", r"\]")


def render_plan_catalog(plans: Iterable[dict[str, str]], *, root: bool) -> str:
    lines: list[str] = []
    for plan in plans:
        title = _safe_title(plan["title"])
        path = Path(plan["path"])
        link = f"{path}/README.md" if root else f"{path.name}/README.md"
        lines.append(f"- [{title}]({link})")
    return "\n".join(lines)


def render_repository_catalog(repositories: Iterable[dict[str, str]]) -> str:
    lines = ["| リポジトリ | 役割 | このプロジェクトとの関係 |", "|---|---|---|"]
    for repository in repositories:
        lines.append(
            f"| [{repository['id']}]({repository['url']}) | {repository['role']} | {repository['relation']} |"
        )
    return "\n".join(lines)


def replace_block(text: str, start: str, end: str, body: str, source: str) -> str:
    start_count = text.count(start)
    end_count = text.count(end)
    start_at = text.find(start)
    end_at = text.find(end)
    if start_count != 1 or end_count != 1 or start_at < 0 or end_at < 0 or start_at >= end_at:
        raise CatalogError(f"{source}: expected exactly one ordered marker pair")
    before = text[: start_at + len(start)]
    after = text[end_at:]
    inner = body.strip("\n")
    return f"{before}\n{inner}\n{after}"


def expected_files() -> dict[Path, str]:
    plans = load_plans()
    repositories = load_repositories()
    root_text = ROOT_README.read_text(encoding="utf-8")
    plans_text = PLAN_README.read_text(encoding="utf-8")
    return {
        ROOT_README: replace_block(
            replace_block(root_text, CATALOG_START, CATALOG_END, render_plan_catalog(plans, root=True), str(ROOT_README)),
            REPOSITORIES_START,
            REPOSITORIES_END,
            render_repository_catalog(repositories),
            str(ROOT_README),
        ),
        PLAN_README: replace_block(
            plans_text,
            CATALOG_START,
            CATALOG_END,
            render_plan_catalog(plans, root=False),
            str(PLAN_README),
        ),
    }


def synchronize(*, write: bool) -> int:
    try:
        expected = expected_files()
    except (OSError, CatalogError) as exc:
        print(f"catalog-sync: {exc}", file=sys.stderr)
        return 2
    stale = [path for path, content in expected.items() if path.read_text(encoding="utf-8") != content]
    if not stale:
        print("catalog-sync: catalog blocks are up to date")
        return 0
    if not write:
        for path in stale:
            print(f"catalog-sync: stale generated block: {path.relative_to(ROOT)}", file=sys.stderr)
        print("catalog-sync: run `python3 tools/catalog_sync.py --write`", file=sys.stderr)
        return 1
    for path in stale:
        path.write_text(expected[path], encoding="utf-8")
        print(f"catalog-sync: updated {path.relative_to(ROOT)}")
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--check", action="store_true", help="fail when generated README blocks are stale")
    mode.add_argument("--write", action="store_true", help="rewrite generated README blocks")
    args = parser.parse_args(argv)
    return synchronize(write=args.write)


if __name__ == "__main__":
    raise SystemExit(main())
