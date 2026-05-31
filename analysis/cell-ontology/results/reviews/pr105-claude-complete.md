---
ontology: cell-ontology
issue_number: 2967
pr_number: 3309
eval_repo_pr: 105
agent: std_opencode_gem4
model: togetherai/google/gemma-4-31B-it
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

gemma-4-31b (opencode) produced the exactly correct fix for issue #2967:
`GO:0051024` → `GO:0002639` in the CL:0002038 (T follicular helper cell)
`EquivalentClasses` axiom, semantically identical to the merged gold PR #3309.
Notably, the smallest model in the cohort solved this axiom-repair task as
cleanly as the frontier models. The metadiff F1 of 0.500 **severely
under-represents** quality: the only divergence from gold is the commutative
ordering of the two `RO_0002215` conjuncts, a pure serialization artifact.

## Strengths

- Correct, biologically valid replacement of the obsolete GO filler
  (`GO:0051024` → `GO:0002639`) on the single `ObjectSomeValuesFrom(obo:RO_0002215
  ...)` term in the CL:0002038 equivalence axiom.
- Perfectly scoped single-line change, no collateral edits or EOF noise.
- Concise, accurate PR/issue comments correctly naming the term, the obsolete
  ID, and the replacement.

## Issues

- None substantive. Divergence from gold is solely conjunct order within a
  commutative `ObjectIntersectionOf` (gold: `GO_0002639` before `GO_0045830`;
  agent: `GO_0045830` first). Logically equivalent — a metadiff line-diff
  artifact, not an agent error.
