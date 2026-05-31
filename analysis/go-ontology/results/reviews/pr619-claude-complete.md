---
ontology: go-ontology
issue_number: 31873
pr_number: 32022
eval_repo_pr: 619
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

The agent obsoleted GO:0061817 correctly at the mechanical level but used `replaced_by: GO:0160214` instead of the human's `consider`, and omitted `consider: GO:0051643`. The diff is byte-identical to attempt #665 (same blob `40affe3`). The 0.818 metadiff score honestly reflects two substantive pattern mismatches in the replacement semantics — it is not under-scored.

## Strengths

- Correct obsoletion mechanics: name→`obsolete`, definition→`OBSOLETE.` with provenance preserved, `is_obsolete: true`, both `is_a` axioms (GO:0051643, GO:0140056) and the EXACT synonym removed.
- Added `property_value: term_tracker_item` for issue #31873 and preserved `created_by`/`creation_date` without churn.
- Obsoletion `comment` names GO:0160214 as the annotation transfer target, more informative than the gpt-5.5 attempts' comment.

## Issues

- Wrong pattern: GO:0160214 (a `molecular_function`) is expressed as `replaced_by` of a `biological_process` term. Issue #31873 explicitly asks curators to "check that the correct MF term is annotated" rather than treating it as a safe blanket replacement; the human PR used `consider` for both targets, matching the GO:0000185/0000186/0000187 precedent.
- Missed requirement: the human's `consider: GO:0051643` (ER localization, BP parent pointer) is absent.
- This is a correct-but-imperfect obsoletion; the metadiff fairly represents the quality (no PR/issue comment captured for this run, but the committed diff is the basis for assessment).
