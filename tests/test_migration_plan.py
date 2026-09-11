import unittest

from tools.migration_plan import ROOT, classify


class MigrationPlanTests(unittest.TestCase):
    def test_report_marks_all_published_plans_complete(self):
        report=classify(ROOT)
        self.assertEqual("COMPLETE",report["status"])
        rows={row["id"]:row for row in report["records"]}
        self.assertEqual({f"P{i:04d}" for i in range(1, 9)}, set(rows))
        self.assertTrue(all(row["classification"] == "CANONICAL" for row in rows.values()))
        self.assertTrue(all(not row["applied"] for row in rows.values()))
        self.assertEqual([],report["writes"])


if __name__ == "__main__":
    unittest.main()
