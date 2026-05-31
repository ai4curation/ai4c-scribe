---
ontology: cell-ontology
issue_number: 2967
pr_number: 3309
eval_repo_pr: 567
agent: std_opencode_g54
model: gpt-5.4
runtime: opencode
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
reviewed_at: 2026-05-17
---

## Summary

gpt-5.4 (opencode) produced the correct biological fix for issue #2967,
replacing the obsolete GO filler `GO:0051024` with `GO:0002639` in the
`EquivalentClasses(obo:CL_0002038 ...)` axiom for T follicular helper cell
(`CL:0002038`) — semantically identical to the merged gold PR #3309 and exactly
the actionable ask of the issue (twice recommended by @addiehl). The recorded
metadiff F1 of 0.333 (versus 0.500 for the in-place claude/opencode runs)
**severely under-represents** quality: it is depressed entirely by two pure
serialization artifacts, not by any substantive defect. Per the established
`case_quality: poor` finding in METADATA.md this is a **success**.

## Strengths

- Correct, biologically valid replacement of the obsolete GO filler on the
  single `ObjectSomeValuesFrom(obo:RO_0002215 obo:GO_0051024)` conjunct with
  the active replacement `GO:0002639` (`positive regulation of follicular
  helper T cell differentiation`-adjacent biology), matching gold logically.
- Tight scope: the only issue-relevant edit is the single intended line in
  `src/ontology/cl-edit.owl`; no unrelated terms or axioms were touched.
- Well-documented methodology in the PR comment: confirmed the reviewer
  guidance from the imported issue context, verified the `CL_0002038` axiom
  before editing, and confirmed `GO_0051024` no longer appears anywhere in
  `cl-edit.owl` after the change.

## Issues

- None biologically or ontologically substantive. The agent's axiom differs
  from gold only in the order of the two commutative `RO_0002215` conjuncts
  (agent keeps `GO_0045830` then `GO_0002639` from literal in-place
  substitution; gold/ROBOT serializes them sorted as `GO_0002639` then
  `GO_0045830`). `ObjectIntersectionOf` is order-independent, so the axioms
  are logically identical — this is the metadiff conjunct-reorder artifact,
  not an error.
- Incidental EOF-newline normalization: the agent's save added a trailing
  newline (`\ No newline at end of file` → final newline) at the end of
  `cl-edit.owl`, producing a second spurious no-op diff hunk (~line 34718)
  that the gold PR did not make. This is harmless to the ontology but is
  gratuitous file churn and further deflates the line-based recall (the extra
  hunk is why F1 falls to 0.333 rather than the 0.500 of the in-place runs).
  Not scored as `over_editing` because it is a pure tooling side effect with
  zero semantic impact; best practice would preserve the original EOF state.
