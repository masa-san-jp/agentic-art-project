import unittest

from tools.migration_plan import ROOT, classify


class MigrationPlanTests(unittest.TestCase):
    def test_report_marks_all_published_plans_complete(self):
        report=classify(ROOT)
        self.assertEqual("MIGRATION_APPLIED",report["status"])
        rows={row["id"]:row for row in report["records"] if not row["applied"]}
        expected_ids = {f"P{i:04d}" for i in range(1, 10)} | {"P0015", "P0017"}
        self.assertEqual(expected_ids, set(rows))
        self.assertTrue(all(row["classification"] == "CANONICAL" for row in rows.values()))
        reserved={row["id"]:row for row in report["records"] if row["applied"]}
        self.assertEqual({"P0016"}, set(reserved))
        self.assertTrue(all(row["classification"] == "MIGRATION_RESERVED" for row in reserved.values()))
        self.assertEqual([],report["writes"])


if __name__ == "__main__":
    unittest.main()
