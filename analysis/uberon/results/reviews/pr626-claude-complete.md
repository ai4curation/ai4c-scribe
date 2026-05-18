---
ontology: uberon
issue_number: 3447
pr_number: 3560
eval_repo_pr: 626
agent: std_opencode_g55
model: gpt-5.5
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
reviewed_at: 2026-05-17
---

## Summary

The gpt-5.5 / opencode run produced a minimal, byte-perfect single-line diff that exactly matches gold PR #3560: on the `dorsolateral prefrontal cortex` (UBERON:0009834) stanza it changed `relationship: part_of UBERON:0000956 ! cerebral cortex` to `relationship: part_of UBERON:0000451 ! prefrontal cortex`. Blob `2c5b9bc` is byte-identical to the merged gold blob; F1=1.0 is genuine and accurately represents quality. This is a textbook clean resolution of an unambiguous, tightly-scoped reclassification request.

## Strengths

- Correct ontological judgment: DLPFC (UBERON:0009834) is placed `part_of` prefrontal cortex (UBERON:0000451), exactly as @dosumis requested in issue #3447 and consistent with the Allen Brain Atlas (structure 10172).
- Excellent rationale: the PR comment correctly argues that because `prefrontal cortex` is already `part_of cerebral cortex` (UBERON:0000956), the broader placement is preserved transitively while the asserted parent becomes strictly more informative — no information lost.
- Exemplary scope discipline despite running `robot convert` for validation: the agent narrowed the final diff to the single intended line and produced **no reserialization churn** on unrelated terms — unlike attempts #604/#662/#246/#158/#76/#30. One of only four attempts (with #569, #283/#181 haiku, #109 gemma) achieving a clean byte-identical-to-gold diff.

## Issues

- None. The diff is byte-identical to the merged human PR after normalization, the ontological reasoning is correct, and scope is perfectly contained.
