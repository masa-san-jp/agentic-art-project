"""Read-only owner verification of an uncommitted canonical plan delivery."""
from __future__ import annotations
import argparse
import json
from pathlib import Path
import sys
if __package__ in {None, ''}:
    sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from tools.catalog_lineage import canonical, digest, records, inspect_record, safe_path, ID, SHA
from tools.validate import validate


def verify(root, expected):
    root=Path(root).resolve()
    fields={'record_id','content_sha256','creator_id','origin_instance_id','source_identity'}
    if not isinstance(expected,list) or not expected:
        raise ValueError('EXPECTED_DELIVERY_REQUIRED')
    ids=[]
    for item in expected:
        if not isinstance(item,dict) or set(item)!=fields or not all(isinstance(v,str) and v for v in item.values()):
            raise ValueError('EXPECTED_DELIVERY_CONTRACT')
        if not ID.fullmatch(item['record_id']) or not SHA.fullmatch(item['content_sha256']) or 'unknown' in (item['creator_id'],item['origin_instance_id']):
            raise ValueError('EXPECTED_DELIVERY_IDENTITY')
        ids.append(item['record_id'])
    if len(ids)!=len(set(ids)):
        raise ValueError('DUPLICATE_DELIVERY_ID')
    errors=validate(root)
    if errors:
        raise ValueError('CATALOG_INVALID: '+errors[0])
    rows={row['id']:row for kind,row in records(root) if kind=='plans'}
    output=[]
    for item in expected:
        row=rows.get(item['record_id'])
        if row is None:
            raise ValueError('DELIVERY_RECORD_MISSING')
        before={p.relative_to(root).as_posix():digest(p.read_bytes()) for p in safe_path(root,row['path']).rglob('*') if p.is_file() and not p.is_symlink()}
        lineage=inspect_record(root,'plans',row)
        if any(lineage.get(key)!=value for key,value in item.items()):
            raise ValueError('DELIVERY_EXPECTATION_MISMATCH')
        after={p.relative_to(root).as_posix():digest(p.read_bytes()) for p in safe_path(root,row['path']).rglob('*') if p.is_file() and not p.is_symlink()}
        if before!=after:
            raise ValueError('DELIVERY_CHANGED_DURING_VALIDATION')
        output.append({**item,'path':row['path'],'files':after})
    result={'contract_version':'local-plan-delivery-receipt/v1','status':'VERIFIED',
            'scope':'LOCAL_WORKTREE','git_saved':False,'remote_synced':False,'records':output}
    result['receipt_sha256']=digest(canonical(result))
    return result


def main(argv=None):
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root',type=Path,required=True)
    parser.add_argument('--expected',type=Path,required=True)
    args=parser.parse_args(argv)
    try:
        print(json.dumps(verify(args.root,json.loads(args.expected.read_text())),ensure_ascii=False,sort_keys=True));return 0
    except (OSError,ValueError,KeyError,TypeError) as exc:
        print(json.dumps({'contract_version':'local-plan-delivery-receipt/v1','status':'BLOCKED','reason':str(exc)}));return 2

if __name__=='__main__':
    raise SystemExit(main())
