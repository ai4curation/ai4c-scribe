---
ontology: cell-ontology
issue_number: 2967
pr_number: 3309
eval_repo_pr: 175
agent: std_claude_op47
model: claude-opus-4-7
runtime: claude
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

claude-opus-4.7 produced the exactly correct fix for issue #2967, replacing
obsolete `GO:0051024` with `GO:0002639` in the CL:0002038 (T follicular helper
cell) `EquivalentClasses` axiom — identical in substance to the merged gold PR
#3309. It additionally delivered the best-reasoned writeup of any attempt,
explicitly citing @addiehl's recommendation, GO's `term replaced by`
annotation, the prior thread (#607), and correctly scoping out the broader
release-time `deprecated_class_reference` check as a separate concern. The
metadiff F1 of 0.500 **severely under-represents** quality: the agent's axiom
is logically identical to gold's, differing only in the commutative ordering of
two `RO_0002215` conjuncts (a serialization-only artifact).

## Strengths

- Correct, minimal edit: `GO:0051024` → `GO:0002639` on the single
  `ObjectSomeValuesFrom(obo:RO_0002215 ...)` filler — biologically correct per
  @addiehl and matching GO's deprecation `term replaced by`.
- Strongest methodology of the cohort: PR body documents reading #2967 and the
  originating #607 thread, verified `GO:0051024` appears nowhere else in
  `cl-edit.owl`, and explicitly deferred the ODK/CI release-time check (matching
  what gouttegd's gold PR #3309 also deferred — the issue's broader ask was
  never converted to a CL PR).
- Tight scope; no whitespace/EOF collateral.

## Issues

- None substantive. Divergence from gold is solely conjunct order within a
  commutative `ObjectIntersectionOf` (gold serialized `GO_0002639` before
  `GO_0045830`; agent left `GO_0045830` first). Semantically equivalent — a
  metadiff line-diff artifact, not an error.
- Cosmetic: the PR-comment body is signed "Signed: GitHub Copilot" despite
  being a claude-opus run — a harmless boilerplate/template leak, no bearing on
  the ontology edit.
