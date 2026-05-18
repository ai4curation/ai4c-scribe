---
ontology: go-ontology
issue_number: 31873
pr_number: 32022
eval_repo_pr: 665
agent: std_opencode_g54
model: gpt-5.4
runtime: opencode
agent_config_tag: v9
case_type: obsoletion
difficulty: medium
f1: 0.818
precision: 0.818
recall: 0.818
jaccard: 0.692
outcome: partial_success
failure_modes:
- wrong_pattern
- missed_requirement
reviewed_by: claude-opus-4.7
reviewed_at: '2026-05-17'
---

## Summary

The agent completed the mechanical obsoletion of GO:0061817 correctly but used `replaced_by: GO:0160214` where the human PR #32022 and issue #31873 deliberately used `consider`, and it omitted `consider: GO:0051643` entirely. The 0.818 metadiff score reflects two real, substantive pattern mismatches rather than mere wording differences — the replacement semantics are too strong for this BP→MF correction, and the BP localization pointer is missing.

## Strengths

- Correct obsoletion mechanics: name prefixed with `obsolete`, definition prefixed with `OBSOLETE.` with provenance preserved, `is_obsolete: true` added.
- Removed both `is_a` axioms (GO:0051643, GO:0140056) and the EXACT synonym.
- Added `property_value: term_tracker_item` for issue #31873 and preserved `created_by`/`creation_date`.
- Obsoletion `comment` is actually more informative than the gpt-5.5 attempts — it names GO:0160214 as the annotation transfer target.
- Methodology was sound: ran `make travis_build`, checked internal references, and queried `runoak -i amigo: associations GO:0061817` to flag remaining IBA annotations for migration.

## Issues

- Wrong pattern: GO:0160214 should be a `consider` target, not `replaced_by`. GO:0160214 is a `molecular_function`, the obsoleted term is `biological_process`; the issue explicitly says curators "should check that the correct MF term is annotated" (i.e. not a safe blanket replacement), and the human PR avoided `replaced_by` for both targets, consistent with the GO:0000185/0000186/0000187 precedent.
- Missed requirement: the human PR's `consider: GO:0051643` (ER localization, the BP parent retained as a process-level pointer) is entirely absent, so the obsolete stanza loses guidance the gold provides.
- Net effect: the metadiff fairly represents the quality here — this is a correct-but-imperfect obsoletion, not an under-scored success.
