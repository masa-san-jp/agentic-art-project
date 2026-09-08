# Catalog lineage and references

Issue10 / AAK-13 implements the pinned AAK specification, without replacing the
Production-owned canonical-plan contract. The projection remains output-only.
`tools/catalog_lineage.py export` is a separate read-only capability; it does not
enable parent knowledge-write dispatch or create public works.

## Record metadata and identity

`plans/Pxxxx-slug/lineage.json` or `works/Wxxxx-slug/lineage.json` follows
[`catalog-lineage/v1`](../schemas/catalog-lineage.schema.json). Its `record_id`
preserves the existing P/W ID. `origin_instance_id` and `creator_id` are explicit
opaque identities. The reference key is origin + local ID + lineage revision;
`canonical_revision` separately retains the Production plan revision. Content
hashes are integrity checks, never creator or work identities.

`derived_from` and `source_plans` retain scoped IDs, revisions, source repository,
Git commit, relative locator and body hash. Public title and mechanism comparison
values must be grounded in the indexed title or exact canonical public text.
Unknown comparison values stay null. Internal research ledgers are not imported.

An absent lineage file has a conservative migration view: preserve already
declared origin/creator fields or use unknown. Never adopt the active user's
identity for an inherited record or infer the artist from a commit author. The
current P0004 remains canonical but attribution-unknown. Reserved legacy IDs in
`plans/migration.yaml` stay reserved. Local IDs are unique within a catalog; the
same local ID in an independent catalog is distinguished by its origin.

## Annotation and migration preview

```sh
python3 tools/catalog_lineage.py migration --root <absolute-catalog-root>
```

This returns proposals and reserved IDs without writes. It does not migrate real
data or supply missing authors. Review unknown attribution against its owner
source before changing the canonical metadata through an authorized workflow.

For a verified new record that is not already in Git history, prepare a closed
lineage JSON and use the already-validated external `instance-profile/v1`:

```sh
python3 tools/catalog_lineage.py annotate --root <absolute-catalog-root> \
  --record-id P0008 --input <external-lineage.json> \
  --instance-profile <external-instance-profile.yaml> --mode new
```

The preview has no writes. Explicit `--apply` requires the profile's
`permissions.local_knowledge_write`. `new` requires the active instance/creator
and rejects inherited or historically used IDs, including a different slug.
`preserve` retains the existing identities and requires committed legacy metadata
when adding the first supplement. Supported instance modes are resume, new-clone
and fork; the shared parent profile remains the schema authority.

When changing existing lineage, use `--mode preserve --expected-sha256 <old-lineage-hash>`
and a higher lineage revision. Include a `derived_from` reference to the preceding
committed revision. Uncommitted previous lineage, stale expected bytes, source
identity changes and conflicting revisions are rejected. Identical replay returns
ALREADY_APPLIED. A repository-local exclusive lock and atomic replacement protect
the supplement; it never rewrites canonical plan bytes or commits/pushes Git.
After review, commit owner metadata using the normal repository workflow.

## Fixed-snapshot read-only export

```sh
python3 tools/catalog_lineage.py export --root <absolute-catalog-root> \
  --repository <owner/catalog> --snapshot <knowledge-commit>
```

Alternatively select `public_projection_root` from an external
`output-destinations/v1` with `--destinations-file`; an explicit `--root` wins.
Require an absolute canonical path. `--repository` is the caller's explicit
catalog namespace, including clone-only local stores; no official output owner
is hard-coded. The configured Production producer is read from the existing
`docs/repositories.yaml` logical-role entry, retaining explicit producer checks
for official and fork catalogs.

The command requires a clean Git checkout at the requested snapshot. It reads
only catalog paths from immutable Git objects into temporary validation storage,
rejects symlink/hardlink entries, runs the existing receiver checks, and emits
[`catalog-reference/v1`](../schemas/catalog-reference.schema.json). It does not
return bodies, arbitrary assets, absolute paths or runtime/private data. Every
reference has the exact source commit, locator and content hash; comparison and
stage-evidence locators are repository-relative. Repeated export changes nothing.

`knowledge_commit` identifies catalog content independently of `code_commit`.
`code_dirty=true` is development/unqualified code and must not be counted as a
qualified runtime candidate. BLOCKED retains per-record unknown/invalid statuses;
eligible references may be returned alongside blockers without claiming overall
success. Empty catalogs return NO_NEW_EVIDENCE.

## Plan, production and exhibition evidence

A plan is always PLANNED with proposed epistemic status, regardless of completion
labels or the existence of a rendered file. A work must have reviewed public
metadata, a hash-bound README and allowlisted/rights-cleared assets, plus references
to canonical attributed source plans. PRODUCED/EXHIBITED additionally require a
distinct hash-bound public evidence document conforming to
[`public-work-stage/v1`](../schemas/public-work-stage.schema.json). Its record,
origin, creator, stage, timestamp and observed/simulated classification must match.
A production evidence document cannot be reused as exhibition proof by changing
only the lineage label. Simulation stays simulated; the validator verifies the
owner's public evidence declaration, not physical completion by executing effects.
Work publication and real-world effects retain their existing human gates.

## Generated catalog and checks

`python3 tools/catalog_sync.py --write` regenerates README catalogs, repository
relationships and `plans/lineage-index.json` from both collections. Unknown
attribution stays visible and cannot enter a validated history export. Never edit
the generated index manually. `tools/validate.py --check` checks the receiver,
supplement validity and index freshness together.

```sh
python3 -m unittest tests.test_catalog_lineage -v
python3 tools/validate.py --check
python3 tools/catalog_sync.py --check
python3 -m unittest discover -s tests -v
git diff --check
```
