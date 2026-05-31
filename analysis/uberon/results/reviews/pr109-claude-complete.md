---
ontology: uberon
issue_number: 3447
pr_number: 3560
eval_repo_pr: 109
agent: std_opencode_gem4
model: togetherai/google/gemma-4-31B-it
runtime: opencode
agent_config_tag: ai4curation/uberon-agent-config@v3
case_type: reclassification
difficulty: medium
f1: 1.000
precision: 1.000
recall: 1.000
jaccard: 1.000
outcome: success
failure_modes: []
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-16
---

## Summary

The gemma-4-31b / opencode run produced a byte-perfect single-line diff exactly matching gold PR #3560: on UBERON:0009834 (dorsolateral prefrontal cortex) it changed `relationship: part_of UBERON:0000956 ! cerebral cortex` to `relationship: part_of UBERON:0000451 ! prefrontal cortex`. Blob `2c5b9bc` is identical to the merged gold blob; F1=1.0 is genuine and accurately represents quality. Notably, the smallest model in the set matched the gold exactly.

## Strengths

- Correct ontological judgment despite being the smallest model evaluated: DLPFC is placed `part_of` prefrontal cortex (UBERON:0000451), exactly as @dosumis requested and consistent with the Allen Brain Atlas.
- Strong methodology evidence in the PR comment: it documents verifying both UBERON:0009834 and UBERON:0000451 IDs, using `obo-checkout.pl`/`obo-checkin.pl` for the edit, and verifying with `obo-grep.pl` — the recommended repo workflow.
- Critically, it did **not** run `robot convert` as a reserialization step, avoiding the annotation-qualifier reordering churn that craters recall in attempts #246/#158/#76/#30. Clean, minimal, byte-identical-to-gold diff.

## Issues

- None. The diff matches the merged human PR exactly after normalization, the reasoning is correct, and scope is perfectly contained.
