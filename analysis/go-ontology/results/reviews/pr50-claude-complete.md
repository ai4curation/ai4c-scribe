---
ontology: go-ontology
issue_number: 31961
pr_number: 32015
eval_repo_pr: 50
agent: std_opencode_g54
model: gpt-5.4
runtime: opencode
agent_config_tag: v9
case_type: obsoletion
difficulty: simple
f1: 0.762
precision: 0.889
recall: 0.667
jaccard: 0.615
outcome: partial_success
failure_modes:
  - over_editing
reviewed_by: claude-opus-4.7
reviewed_at: "2026-05-15"
---

## Summary

gpt-5.4 / opencode re-run producing the identical diff blob (`e255e07`) to attempt #51. Correct core obsoletion of GO:0008785 plus the two defensible comment cleanups, with the same extra (largely redundant) GO:0102039 synonym + tracker-item edits. F1=0.762; the recall drop vs. the 0.800 cluster is a fair penalty for the GO:0102039 churn. Reviewed in parallel with #51.

## Strengths

- Correct, complete core obsoletion: obsolete name prefix, `OBSOLETE.` def prefix, `is_a: GO:0016668` removed, `is_obsolete: true`, `replaced_by: GO:0102039`, #31961 tracker item, historical tracker items preserved.
- GO:0009321 comment rewired to GO:0102039; GO:0070937 spurious comment correctly *deleted*.
- `make travis_build` reported passing (including ROBOT verification and obsolete-reference checks); checkout/checkin workflow followed.

## Issues

- Over-editing: same redundant `synonym: "alkyl hydroperoxide reductase activity" EXACT []` added to GO:0102039 (which already has the near-identical `alkylhydroperoxide reductase activity` EXACT) plus a non-standard #31961 `term_tracker_item` on the replacement term. Not clearly beneficial; absent from the human PR. Fairly penalized in recall.
- Comment omits the explicit EC 1.11.1.26 citation present in the human comment. Stylistic.
- Reproducibility duplicate of #51; no additional signal.
