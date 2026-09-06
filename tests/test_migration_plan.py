import unittest

from tools.migration_plan import ROOT, classify


class MigrationPlanTests(unittest.TestCase):
    def test_report_includes_live_canonical_and_reserved_legacy_ids(self):
        report=classify(ROOT)
        self.assertEqual("MIGRATION_APPLIED",report["status"])
        rows={row["id"]:row for row in report["records"]}
        self.assertEqual("CANONICAL",rows["P0004"]["classification"])
        self.assertFalse(rows["P0004"]["applied"])
        self.assertEqual(
            {"P0001","P0002","P0003","P0005","P0006","P0007"},
            {key for key,row in rows.items() if row["classification"]=="MIGRATION_RESERVED"},
        )
        self.assertTrue(all(row["applied"] for row in rows.values() if row["classification"]=="MIGRATION_RESERVED"))
        self.assertEqual([],report["writes"])


if __name__ == "__main__":
    unittest.main()
