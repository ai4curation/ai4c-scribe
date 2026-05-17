---
ontology: uberon
issue_number: 3447
pr_number: 3560
eval_repo_pr: 181
agent: std_claude_haiku45
model: claude-haiku-4-5-20251001
runtime: claude
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

A second claude-haiku-4.5 run that, like attempt #283, produced a byte-perfect single-line diff exactly matching gold PR #3560: `relationship: part_of UBERON:0000956 ! cerebral cortex` → `relationship: part_of UBERON:0000451 ! prefrontal cortex` on the DLPFC (UBERON:0009834) stanza. Blob `2c5b9bc` is identical to the merged gold blob, so F1=1.0 is genuine and accurately represents quality.

## Strengths

- Correct ontological reclassification: DLPFC placed `part_of` prefrontal cortex (UBERON:0000451), the exact change requested by @dosumis and consistent with the Allen Brain Atlas. Since prefrontal cortex is `part_of` cerebral cortex (UBERON:0000956), the broader placement is retained transitively.
- Perfect scope discipline: a single changed line, no provenance/tracker additions, and no `robot convert` reserialization noise. Reproducibility is demonstrated — two independent haiku runs (#283, #181) converged on the identical minimal diff.

## Issues

- None. Byte-identical to the merged human PR after normalization with correct reasoning and contained scope. (This attempt's case file has no PR/issue comment captured, but the diff alone fully resolves the issue.)
