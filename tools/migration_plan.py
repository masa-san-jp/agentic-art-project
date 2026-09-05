"""Read-only classification of old plan records; never move or delete public data."""
import argparse
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path: sys.path.insert(0, str(ROOT))
from tools import catalog_sync
from tools.validate import validate_record, mapping_fields


def classify(root):
    result = []
    for record in catalog_sync._parse_list_records(root / "plans/index.yaml", "records"):
        errors = validate_record(root,record)
        metadata = mapping_fields(root / record["path"] / "metadata.yaml")
        result.append({"id": record["id"], "classification": "CANONICAL" if not errors else "MIGRATION_REQUIRED",
            "source_candidate": metadata.get("source_identity") or metadata.get("provenance.source_ref") or "UNKNOWN",
            "blocking_reason": errors, "unblock_condition": "Recover owner-verified attestation and exact body/assets with stable identity, or approve metadata-only reservation and remove this legacy record from the current public collection.",
            "existing_path": record["path"], "proposed_registry": "plans/migration.yaml", "applied": False})
    return {"status": "REVIEW_REQUIRED", "records": result, "writes": [], "human_gate": "ACTUAL_PUBLIC_RECORD_MIGRATION"}


if __name__ == "__main__":
    parser=argparse.ArgumentParser(description=__doc__); parser.add_argument("--root",type=Path,default=ROOT)
    args=parser.parse_args(); print(json.dumps(classify(args.root),ensure_ascii=False,indent=2))
