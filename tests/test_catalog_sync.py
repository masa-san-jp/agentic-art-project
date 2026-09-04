import importlib.util
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("catalog_sync", ROOT / "tools/catalog_sync.py")
assert SPEC is not None and SPEC.loader is not None
catalog_sync = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(catalog_sync)


class CatalogSyncTests(unittest.TestCase):
    def test_public_plan_index_is_rendered_in_both_catalogs(self):
        plans = catalog_sync.load_plans()
        plan_ids = [plan["id"] for plan in plans]
        self.assertTrue(plan_ids)
        self.assertEqual(plan_ids, sorted(set(plan_ids)))
        expected = catalog_sync.expected_files()
        self.assertEqual(
            catalog_sync.ROOT_README.read_text(encoding="utf-8"),
            expected[catalog_sync.ROOT_README],
        )
        self.assertEqual(
            catalog_sync.PLAN_README.read_text(encoding="utf-8"),
            expected[catalog_sync.PLAN_README],
        )

    def test_repository_registry_contains_links(self):
        repositories = catalog_sync.load_repositories()
        self.assertIn("agentic-art-orchestration", {item["id"] for item in repositories})
        self.assertTrue(all(item["url"].startswith("https://github.com/") for item in repositories))

    def test_marker_pair_must_be_unique_and_ordered(self):
        with self.assertRaises(catalog_sync.CatalogError):
            catalog_sync.replace_block("start end end", "start", "end", "body", "fixture")

    def test_blocked_plan_is_rendered_as_not_producible(self):
        plans = catalog_sync.load_plans()
        blocked = [plan for plan in plans if plan["status"] == "blocked-missing-canonical"]
        self.assertTrue(blocked)
        rendered = catalog_sync.render_plan_catalog(blocked, root=False)
        self.assertIn("正本待ち（制作不可）", rendered)

    def test_parent_quoted_indentless_yaml_is_accepted(self):
        content = '''"version": 1
"records":
- "id": "P0008"
  "slug": "automatic-plan"
  "title": "Automatic plan"
  "path": "plans/P0008-automatic-plan"
  "source_key": "plan:aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
  "content_sha256": "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
  "status": "ready-for-publication"
  "visibility": "public"
  "rights_status": "cleared"
"retired_ids": []
'''
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "index.yaml"
            path.write_text(content, encoding="utf-8")
            records = catalog_sync.load_plans(path)
        self.assertEqual(["P0008"], [record["id"] for record in records])


if __name__ == "__main__":
    unittest.main()
