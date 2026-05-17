---
ontology: cell-ontology
issue_number: 2967
pr_number: 3309
eval_repo_pr: 38
agent: std_opencode_g55
model: openai/gpt-5.5
runtime: opencode
agent_config_tag: ai4curation/cl-agent-config@v3
case_type: axiom_repair
difficulty: simple
f1: 0.500
precision: 0.500
recall: 0.500
jaccard: 0.333
outcome: success
failure_modes: []
case_quality: poor
case_quality_reason: metadiff_conjunct_reorder_artifact
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-16
---

## Summary

gpt-5.5 (opencode) produced the exactly correct fix for issue #2967, replacing
obsolete `GO:0051024` with `GO:0002639` in the CL:0002038 (T follicular helper
cell) `EquivalentClasses` axiom — identical in substance to the merged gold PR
#3309. The metadiff F1 of 0.500 **severely under-represents** quality: the
agent's axiom is logically equivalent to gold's, differing only in the
commutative ordering of the two `RO_0002215` conjuncts (a serialization
artifact). This is a second gpt-5.5/opencode run; substance matches pr56.

## Strengths

- Correct, minimal biological edit: `GO:0051024` → `GO:0002639` on the single
  `ObjectSomeValuesFrom(obo:RO_0002215 ...)` filler in the CL:0002038
  equivalence axiom, per @addiehl's recommendation and GO's `term replaced by`.
- Perfectly scoped single-line change, no collateral edits or EOF noise.
- Accurate, concise PR/issue comments correctly attributing the replacement to
  the issue discussion.

## Issues

- None substantive. Divergence from gold is solely conjunct order within a
  commutative `ObjectIntersectionOf` (gold: `GO_0002639` before `GO_0045830`;
  agent: `GO_0045830` first). Logically equivalent — a metadiff line-diff
  artifact, not an agent error.
