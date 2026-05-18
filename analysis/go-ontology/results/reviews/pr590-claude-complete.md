---
ontology: go-ontology
issue_number: 31873
pr_number: 32022
eval_repo_pr: 590
agent: std_opencode_g55
model: gpt-5.5
runtime: opencode
agent_config_tag: v9
case_type: obsoletion
difficulty: medium
f1: 0.909
precision: 0.909
recall: 0.909
jaccard: 0.833
outcome: success
failure_modes: []
reviewed_by: claude-opus-4.7
reviewed_at: '2026-05-17'
---

## Summary

The agent correctly obsoleted GO:0061817 "endoplasmic reticulum-plasma membrane tethering". The diff is byte-identical to attempt #640 (same blob `08c8873`) and to the human gold PR #32022 structurally: name→`obsolete`, def→`OBSOLETE.`, axioms and synonym removed, `is_obsolete: true`, term_tracker_item, and `consider: GO:0160214` + `consider: GO:0051643`. F1 = 0.909 is held below 1.0 only by a terser obsoletion `comment`; the metadiff under-represents what is effectively a complete, correct solution.

## Strengths

- Used `consider` (not `replaced_by`) for GO:0160214, correctly handling the cross-namespace BP→MF mapping exactly as the human PR and issue #31873 intend; precedent GO:0000185/0000186/0000187 supports this.
- Retained `consider: GO:0051643` for the BP localization parent, matching the gold's second consider tag.
- Removed both `is_a` axioms (GO:0051643, GO:0140056) and the EXACT synonym; added `is_obsolete: true` and `property_value: term_tracker_item` for issue #31873.
- Preserved `created_by`/`creation_date` in place — no spurious diff churn.

## Issues

- None substantive. The obsoletion `comment` is terser than the human's, which additionally names GO:0160214 as the migration target — this single differing line accounts for the entire 0.091 F1 gap. No PR/issue comment body was captured for this attempt, but the committed ontology change is correct and complete.
