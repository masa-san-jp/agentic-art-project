import copy
import json
from pathlib import Path
import shutil
import tempfile
import unittest

from tools.attestation_receiver import check_envelope, digest, canonical
from tools.validate import validate_record

ROOT=Path(__file__).resolve().parents[1]


class AttestationReceiverTests(unittest.TestCase):
    def setUp(self):
        t=tempfile.TemporaryDirectory();self.addCleanup(t.cleanup);self.root=Path(t.name)
        self.directory=self.root/'plans/P0099-synthetic'
        shutil.copytree(ROOT/'tests/fixtures/attested-plan',self.directory)
        self.a=json.loads((self.directory/'public-plan-attestation.json').read_text())
        self.metadata={"id":"P0099","slug":"synthetic","title":"Synthetic Production fixture","status":"ready-for-publication","visibility":"public","rights_status":"cleared",
            "content_sha256":digest((self.directory/'plan.md').read_bytes()),"attestation_sha256":digest((self.directory/'public-plan-attestation.json').read_bytes()),
            "source_identity":self.a['project_id']+'#'+self.a['plan_id'],"plan_revision":str(self.a['plan_revision']),
            "production_repository":self.a['producer']['repository'],"production_commit":self.a['producer']['commit'],
            "projection_contract":"canonical-plan-projection/v2","projection_mode":"AUTOMATIC_PLAN","body_transform":"none",
            "plan_state":"canonical","production_state":"PLANNING","external_effects_authorized":"false","source_run_id":"synthetic-receiver"}
        self.metadata['source_key']='plan:'+self.metadata['source_identity']
        self.index=dict(self.metadata,path='plans/P0099-synthetic')
        (self.directory/'metadata.yaml').write_text('\n'.join(k+': '+json.dumps(v) for k,v in self.metadata.items())+'\n')
        (self.directory/'README.md').write_text('[制作プラン本文](plan.md)\n')

    def check(self):return check_envelope(self.directory,self.metadata,self.index)

    def test_actual_production_fixture_bytes_assets_and_provenance_pass(self):
        self.assertEqual(self.a,self.check())
        self.assertEqual([],validate_record(self.root,self.index))
        self.assertEqual((ROOT/'tests/fixtures/attested-plan/plan.md').read_bytes(),(self.directory/'plan.md').read_bytes())

    def test_summary_handwritten_heading_imitation_and_one_byte_tamper_fail(self):
        path=self.directory/'plan.md';original=path.read_bytes()
        for bad in (b'# Summary\n',b'# Integrated plan\n## Scope\n## Budget\n',original+b' '):
            path.write_bytes(bad)
            with self.assertRaisesRegex(ValueError,'body hash'):self.check()

    def test_missing_and_forged_attestation_fail(self):
        path=self.directory/'public-plan-attestation.json'
        changed=copy.deepcopy(self.a);changed['plan_revision']+=1;path.write_bytes(canonical(changed))
        with self.assertRaisesRegex(ValueError,'integrity'):self.check()
        changed['integrity']['content_sha256']='sha256:'+digest(canonical({k:v for k,v in changed.items() if k!='integrity'}));path.write_bytes(canonical(changed))
        with self.assertRaisesRegex(ValueError,'mismatch'):self.check()
        path.unlink()
        with self.assertRaisesRegex(ValueError,'missing'):self.check()

    def test_revision_provenance_and_receipt_fields_fail_closed(self):
        for field in ('source_identity','plan_revision','production_commit','source_run_id','attestation_sha256','body_transform','projection_contract'):
            previous=self.metadata.pop(field)
            with self.subTest(field=field),self.assertRaises(ValueError):self.check()
            self.metadata[field]=previous

    def test_asset_tamper_missing_and_unlisted_files_fail(self):
        p=self.directory/'media/concept-mockup.svg';raw=p.read_bytes();p.write_bytes(raw+b'\n')
        with self.assertRaises(ValueError):self.check()
        p.unlink()
        with self.assertRaises(ValueError):self.check()
        p.write_bytes(raw);(self.directory/'media/extra.svg').write_bytes(raw)
        with self.assertRaisesRegex(ValueError,'unlisted'):self.check()

    def test_unresolved_rights_even_with_rehashed_envelope_fail(self):
        self.a['publication_review']['rights']='UNKNOWN';self.a['integrity']['content_sha256']='sha256:'+digest(canonical({k:v for k,v in self.a.items() if k!='integrity'}))
        path=self.directory/'public-plan-attestation.json';path.write_bytes(canonical(self.a))
        for record in (self.metadata,self.index):record['attestation_sha256']=digest(path.read_bytes())
        with self.assertRaisesRegex(ValueError,'review'):self.check()
