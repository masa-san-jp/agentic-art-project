import importlib.util
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


if __name__ == "__main__":
    unittest.main()
