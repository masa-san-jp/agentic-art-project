import importlib.util
import shutil
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("public_catalog_validate", ROOT / "tools/validate.py")
assert SPEC is not None and SPEC.loader is not None
validator = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(validator)


class PublicCatalogValidationTests(unittest.TestCase):
    def test_repository_is_valid(self):
        self.assertEqual([], validator.validate(ROOT))

    def test_summary_cannot_pass_as_a_canonical_plan(self):
        summary = "# Public summary\n\nA shortened production idea.\n".encode("utf-8")
        errors = validator.canonical_plan_errors(summary, "fixture/plan.md")
        self.assertTrue(errors)
        self.assertTrue(any("canonical" in error for error in errors))

    def test_parent_quoted_metadata_is_accepted(self):
        content = '''"id": "P0008"
"status": "ready-for-publication"
"projection":
  "contract_version": "canonical-plan-projection/v1"
  "mode": "AUTOMATIC_PLAN"
"provenance":
  "source_repository": "agentic-art-production"
'''
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "metadata.yaml"
            path.write_text(content, encoding="utf-8")
            fields = validator.mapping_fields(path)
        self.assertEqual("P0008", fields["id"])
        self.assertEqual("AUTOMATIC_PLAN", fields["projection.mode"])
        self.assertEqual("agentic-art-production", fields["provenance.source_repository"])

    def test_standalone_heading_imitation_never_establishes_canonical_status(self):
        content = b"# Integrated plan\n## Schedule\n## Budget\n"
        self.assertTrue(validator.canonical_plan_errors(content, "fixture/plan.md"))

    def test_only_canonical_records_are_live_and_legacy_ids_are_reserved(self):
        records = validator.catalog_sync._parse_list_records(ROOT / "plans/index.yaml", "records")
        for record in records:
            self.assertEqual([], validator.validate_record(ROOT, record))
        migration = validator.catalog_sync._parse_list_records(ROOT / "plans/migration.yaml", "records")
        self.assertEqual(
            {"P0001", "P0002", "P0003", "P0005", "P0006", "P0007"},
            {record["id"] for record in migration},
        )
        for record in migration:
            self.assertFalse(any((ROOT / "plans").glob(record["id"] + "-*")))
        self.assertFalse(list((ROOT / "plans").glob("P*/summary.md")))

    def test_tampered_plan_body_is_rejected_by_hash(self):
        record = validator.catalog_sync._parse_list_records(ROOT / "plans/index.yaml", "records")[0]
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            target = root / record["path"]
            target.parent.mkdir(parents=True)
            shutil.copytree(ROOT / record["path"], target)
            (target / "plan.md").write_text("# tampered\n", encoding="utf-8")
            errors = validator.validate_record(root, record)
        self.assertTrue(any("body hash" in error for error in errors))

    def test_missing_provenance_and_manual_projection_are_rejected(self):
        record = validator.catalog_sync._parse_list_records(ROOT / "plans/index.yaml", "records")[0]
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            target = root / record["path"]
            target.parent.mkdir(parents=True)
            shutil.copytree(ROOT / record["path"], target)
            metadata = target / "metadata.yaml"
            changed = metadata.read_text(encoding="utf-8")
            changed = changed.replace('"mode": "AUTOMATIC_PLAN"\n', '"mode": "MANUAL"\n')
            changed = changed.replace('"production_commit": "69567e88131e3f033d010791fb5849e1b2ebff8d"\n', "")
            metadata.write_text(changed, encoding="utf-8")
            errors = validator.validate_record(root, record)
        self.assertTrue(any("mismatch" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
