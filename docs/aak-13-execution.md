# AAK-13 — Catalog attribution and read-only references

## Purpose / Big Picture

Implement Issue10 against AAK-SPEC/PLAN commit
`b0e7c7f8d0a1f756fa708deef4fb380a62e45e0d`. Preserve canonical plan bytes and
existing P/W IDs while making origin, creator, revisions and derivation explicit.
The public projection stays output-only; `catalog-reference/v1` is a separate
read-only capability. This document records execution, not new requirements.

## Progress

- [x] Read Issue10, pinned common/AAK13 requirements, owner AGENTS/README/layout/index/tools.
- [x] Qualify Project12 base `8e4c90b701c82bfe14964dbbe6a0aba62342fcef`: native validator/catalog and 20 tests PASS; actual Production-parent-Project boundary PASS.
- [x] Parent records AAK13 claim and isolated parent/child branches; no native Project queue/claim CLI exists.
- [x] Add closed record lineage metadata, generated lineage index, migration dry-run and read-only snapshot export.
- [x] Verify inheritance, new-origin records, revision conflicts, canonical-only references and conservative creation stages.
- [ ] Run all Issue10 checks, commit owner evidence, create a separate draft PR, and publish parent checkpoint before lease release.

## Surprises & Discoveries

The old PR11 migration blocker was superseded during this continuation by
Project12. Its P0004 is canonical; other legacy IDs are reserved. Current P0004
does not declare an artist/origin. Git commit authors or the active user are not
evidence of artwork attribution; the migration dry-run must retain unknown.

## Decision Log

Use per-record closed `lineage.json` metadata beside canonical files, with a
generated index produced by the existing catalog tool. Keep the source P/W ID,
canonical source identity and body hash bound to the record. Reference identity
includes origin and local ID. New records must use the explicit active instance;
inherited records retain their attribution. A committed inherited record cannot
be relabeled as a new record merely because its lineage is absent.

Export metadata and source locators from a clean Git snapshot, never canonical
bodies, internal ledgers or arbitrary files. Run existing plan attestation checks
before emitting a reference. Unknown attribution remains a blocker. Plans are
always classified as planned; actual work/exhibition claims need their own
reviewed, hash-bound public evidence. Resolve target catalog paths through
explicit configuration, without a fixed official output repository name.

## Outcomes & Retrospective

Code verification PASS: 12 focused and 32 full native tests, validator, catalog sync,
three schema/example checks, and actual Production-parent-Project boundary.
Retained Git snapshot evidence and draft PR delivery are the next checkpoint.
Actual P0004 body/assets and unknown attribution remain unchanged. No merge,
real-data migration, public work creation or release is performed.

## Context and Orientation

Owner branch `codex/aak-13-catalog-lineage-20260906`, based on Project12.
Parent branch `codex/aak-13-owner-checkpoint-20260906` owns the task/lease record.
AAK04 dependency: `83f7e9e8d1c6e25b39351aebb6eb15cb12da4685`,
`instance-profile/v1`, parent PR201. All candidates remain unmerged.

## Plan of Work

Closed metadata and validation -> owner annotation/migration preview -> canonical
generated index -> immutable read-only export -> positive/negative real-Git
fixtures -> native checks and evidence -> separate owner and parent PRs.

## Concrete Steps

```sh
python3 -m unittest tests.test_catalog_lineage -v
python3 tools/validate.py --check
python3 tools/catalog_sync.py --check
python3 -m unittest discover -s tests -v
git diff --check
```

## Validation and Acceptance

AC1: preserve legacy IDs/declared creators; missing creator/canonical evidence
stays unknown/blocked. AC2: inherited/new fork records keep different origins and
composite identities. AC3: reject tampered bodies, summaries, private/unreviewed
assets. AC4: repeated export does not write and references resolve to the exact
Git snapshot and canonical revision. AC5: planned is not produced/exhibited;
native receiver/catalog gates still pass.

## Idempotence and Recovery

Use explicit expected metadata state for local annotations; exact replay is a
no-op and conflicting revisions fail. Never modify a canonical body to make a
gate pass. Preserve prior snapshots in Git. Publish the completed owner candidate
and parent execution SSOT before releasing the parent-held lease.

## Interfaces and Dependencies

Project owns metadata/catalog schemas and reference export. Production owns plan
semantics; its attestation is reused, not copied as a heading validator. Parent
stores only references and results. Actual owner data migration and merge remain
outside this task. Tests use synthetic catalogs and local Git only.
