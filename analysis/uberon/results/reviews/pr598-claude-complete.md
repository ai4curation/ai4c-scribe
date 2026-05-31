---
ontology: uberon
issue_number: 2911
pr_number: 3508
eval_repo_pr: 598
agent: std_opencode_gpt54
model: gpt-5.4
runtime: opencode
agent_config_tag: ai4curation/uberon-agent-config@v3
case_type: axiom_repair
difficulty: medium
f1: 1.000
precision: 1.000
recall: 1.000
jaccard: 1.000
outcome: success
failure_modes: []
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-17
---

## Summary

gpt-5.4 (opencode) correctly resolved issue #2911 by removing the two erroneous `relationship: part_of UBERON:0003983 ! conus arteriosus` axioms from `UBERON:0007181` (serosa of infundibulum of uterine tube) and `UBERON:0007182` (muscle layer of infundibulum of uterine tube). The fix is substantively identical to gold PR #3508 and follows the maintainer's explicit instruction in the issue comment. F1=1.000 accurately represents the quality — this is a faithful, fully-scoped reproduction of the gold repair.

## Strengths

- Removed exactly the two homonym-confusion axioms the issue flagged (cardiac `conus arteriosus` UBERON:0003983 erroneously asserted as parent of two reproductive uterine-tube layers), matching gold PR #3508 byte-for-byte after normalization (blob `1dec482`).
- Correctly preserved the legitimate `intersection_of: part_of UBERON:0003984 ! uterine tube infundibulum` axioms on both terms, so the genuine uterine-tube hierarchy is untouched.
- Tightly scoped: single file `src/ontology/uberon-edit.obo`, +0/-2 lines, no collateral edits, no robot-convert serializer churn in the committed diff.
- Followed the maintainer's directive verbatim ("remove the incorrect part-ofs on UBERON:0007181 and UBERON:0007182"), demonstrating it correctly read and applied the issue context.

## Issues

- None. No errors, omissions, scope creep, or style deviations from gold. The agent's diff and the gold diff differ only in whitespace/blank-line representation that metadiff normalizes away.
