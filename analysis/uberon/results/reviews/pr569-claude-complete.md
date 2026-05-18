---
ontology: uberon
issue_number: 3447
pr_number: 3560
eval_repo_pr: 569
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

The gpt-5.5 / opencode run produced a minimal, byte-perfect single-line diff that exactly matches gold PR #3560: on the `dorsolateral prefrontal cortex` (UBERON:0009834) stanza it changed `relationship: part_of UBERON:0000956 ! cerebral cortex` to `relationship: part_of UBERON:0000451 ! prefrontal cortex`. Blob `2c5b9bc` is byte-identical to the merged gold blob; F1=1.0 is genuine and accurately represents quality — a clean resolution of an unambiguous, tightly-scoped reclassification.

## Strengths

- Correct ontological judgment: DLPFC (UBERON:0009834) is correctly reparented from `part_of` cerebral cortex (UBERON:0000956) to `part_of` prefrontal cortex (UBERON:0000451), exactly as requested by @dosumis in issue #3447 and consistent with the Allen Brain Atlas (structure 10172). The change is transitively consistent since UBERON:0000451 is itself `part_of` UBERON:0000956.
- Exemplary scope discipline: exactly one changed line, no `term_tracker_item`/`dcterms-date` provenance additions, and critically **no `robot convert` reserialization churn** — unlike the sibling gpt-5.4 attempts #604/#662. One of the small set (#626, #283, #181, #109) achieving a clean byte-identical-to-gold result.

## Issues

- None. The diff is byte-identical to the merged human PR after normalization, the reasoning is correct, and scope is perfectly contained. (No PR/issue comment was captured in the attempt record, but the diff itself is conclusive.)
