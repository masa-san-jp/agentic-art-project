import unittest
from tools.local_delivery import verify
from tools.catalog_lineage import export_catalog
from tests import test_catalog_lineage as fixture

class LocalDeliveryTests(unittest.TestCase):
    setUp=fixture.CatalogLineageTests.setUp
    plan=fixture.CatalogLineageTests.plan
    label=fixture.CatalogLineageTests.label
    synchronize=fixture.CatalogLineageTests.synchronize

    def prepare(self):
        row=self.plan(); value=self.label(row); self.synchronize()
        return row,[{k:value[k] for k in ('record_id','content_sha256','creator_id','origin_instance_id','source_identity')}]

    def test_uncommitted_delivery_is_verified_without_git_writes(self):
        row,expected=self.prepare()
        head=fixture.git(self.root,'rev-parse','HEAD'); status=fixture.git(self.root,'status','--porcelain')
        before=fixture.files(self.root)
        result=verify(self.root,expected)
        self.assertEqual('VERIFIED',result['status']);self.assertFalse(result['git_saved'])
        self.assertEqual(result,verify(self.root,expected))
        self.assertEqual(head,fixture.git(self.root,'rev-parse','HEAD'))
        self.assertEqual(status,fixture.git(self.root,'status','--porcelain'))
        self.assertEqual(before,fixture.files(self.root))
        with self.assertRaises(ValueError): export_catalog(self.root,'example/catalog')

    def test_missing_and_wrong_identity_fail(self):
        row,expected=self.prepare()
        for key,value in [('record_id','P9999'),('creator_id','wrong'),('origin_instance_id','wrong'),('source_identity','wrong'),('content_sha256','0'*64)]:
            with self.subTest(key=key),self.assertRaises(ValueError):verify(self.root,[{**expected[0],key:value}])

    def test_body_tampering_fails(self):
        row,expected=self.prepare()
        (self.root/row['path']/'plan.md').write_text('invented replacement')
        with self.assertRaises(ValueError):verify(self.root,expected)

    def test_owner_initializes_new_lineage_from_explicit_profile(self):
        import contextlib,io,json
        from tools.catalog_lineage import main
        row=self.plan()
        profile=self.parent/'profile.json';profile.write_text(json.dumps(fixture.actor()))
        with contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(0,main(['annotate','--root',str(self.root),'--record-id',row['id'],'--instance-profile',str(profile),'--mode','new','--initialize-new','--apply']))
        self.synchronize()
        value=fixture.lineage.read_lineage(self.root,'plans',row)
        expected=[{k:value[k] for k in ('record_id','content_sha256','creator_id','origin_instance_id','source_identity')}]
        self.assertEqual('VERIFIED',verify(self.root,expected)['status'])
