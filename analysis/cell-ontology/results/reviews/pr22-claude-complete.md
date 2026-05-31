---
ontology: cell-ontology
issue_number: 2967
pr_number: 3309
eval_repo_pr: 22
agent: std_codex_g55
model: gpt-5.5
runtime: codex
agent_config_tag: ai4curation/cl-agent-config@v3
case_type: axiom_repair
difficulty: simple
f1: 0.333
precision: 0.500
recall: 0.250
jaccard: 0.200
outcome: success
failure_modes: []
case_quality: poor
case_quality_reason: metadiff_conjunct_reorder_plus_eof_artifact
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-16
---

## Summary

gpt-5.5 (codex) produced the correct biological fix for issue #2967, replacing
obsolete `GO:0051024` with `GO:0002639` in the CL:0002038 (T follicular helper
cell) `EquivalentClasses` axiom — semantically identical to the merged gold PR
#3309 and the strongest-validated run in the cohort (it ran both `robot convert`
and `robot reason --reasoner ELK`). The metadiff F1 of 0.333 **severely
under-represents** quality and, as with the other codex run (pr74), is depressed
by two pure serialization artifacts: commutative `RO_0002215` conjunct
reordering plus an incidental EOF-newline normalization producing a spurious
second diff hunk.

## Strengths

- Correct, minimal biological edit: `GO:0051024` → `GO:0002639` on the single
  `ObjectSomeValuesFrom(obo:RO_0002215 ...)` filler in the CL:0002038
  equivalence axiom, per @addiehl's recommendation and GO's `term replaced by`.
- Best validation discipline of any attempt: confirmed the obsolete term
  occurred once, replaced only that reference, then ran `robot convert` *and*
  `robot reason --input src/ontology/cl-edit.owl --reasoner ELK` to verify the
  ontology still classifies cleanly with the replacement term.
- Issue-relevant hunk correctly scoped to one line.

## Issues

- None biologically/ontologically substantive — the core edit is logically
  equivalent to gold.
- Incidental EOF-newline normalization adds a second no-op diff hunk
  (lines ~34718, `\ No newline at end of file` → newline added). Harmless to
  the ontology but gratuitous file churn the human PR did not make, and it
  further deflates the line-based metadiff. Preserving the original EOF state
  would have avoided it (the claude/opencode runs did). Not classified as
  `over_editing` since it is a save-tooling side effect with zero semantic
  impact.
