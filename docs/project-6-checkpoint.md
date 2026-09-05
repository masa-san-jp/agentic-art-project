# Project #6 receiver checkpoint

IN_PROGRESS. Branch agent/project-6-attestation-receiver starts at the isolated
existing PR9 candidate 55615f985d3376cafd5c9c08ecdc579be1c8641d, tree
647af8065845f5aa522c62eb13daa286a0df54a9. This is not current main and is not a
qualified implementation of the revised Issue #6. No existing branch is reset.

Current Issue #6 requires Production attestation/v1 and projection/v2; PR9 has
heading checks and v1, and retains summaries in the public catalog. Implement the
receiver contract in code with synthetic fixture evidence. Actual P0001..P0007
migration/deletion is explicitly not authorized by the AAK start instruction;
do not alter existing record bodies or generated public catalogs to hide this
remaining gate. A read-only migration manifest will make that final action
reviewable. AAK-13 cannot claim dependency acceptance before it is resolved.

Required checks: python3 tools/validate.py --check, python3 tools/catalog_sync.py
--check, python3 -m unittest discover -s tests -v, git diff --check. Existing-data
failures must remain visible, separately from synthetic receiver code checks.

No private/raw, real viewer response, profile, internal handoff or conversation is
added. Publication, merge, release and actual data migration remain human-gated.
