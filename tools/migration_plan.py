"""Report canonical records and metadata-only legacy reservations without writes."""
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
    migration = root / "plans/migration.yaml"
    if migration.exists():
        for record in catalog_sync._parse_list_records(migration, "records"):
            result.append({"id": record["id"], "classification": "MIGRATION_RESERVED",
                "source_candidate": record["source_candidate"], "blocking_reason": [record["blocking_reason"]],
                "unblock_condition": record["unblock_condition"], "existing_path": None,
                "proposed_registry": "plans/migration.yaml", "applied": True})
    if any(row["applied"] for row in result):
        status = "MIGRATION_APPLIED"
    elif result and all(row["classification"] == "CANONICAL" for row in result):
        status = "COMPLETE"
    else:
        status = "REVIEW_REQUIRED"
    return {"status": status,
        "records": sorted(result,key=lambda row:row["id"]), "writes": [], "human_gate": "NONE"}


if __name__ == "__main__":
    parser=argparse.ArgumentParser(description=__doc__); parser.add_argument("--root",type=Path,default=ROOT)
    args=parser.parse_args(); print(json.dumps(classify(args.root),ensure_ascii=False,indent=2))
