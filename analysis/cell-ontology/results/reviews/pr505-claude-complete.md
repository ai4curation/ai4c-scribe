---
ontology: cell-ontology
issue_number: 2967
pr_number: 3309
eval_repo_pr: 505
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
(`CL:0002038`) — semantically identical to merged gold PR #3309 and exactly
the issue's only actionable ask (twice recommended by @addiehl). This run's
diff is byte-for-byte the same substantive change as sibling attempts #567,
#74 and #22. The recorded metadiff F1 of 0.333 **severely
under-represents** quality and is depressed solely by two serialization
artifacts. Per the established `case_quality: poor` finding in METADATA.md
this is a **success**.

## Strengths

- Correct, biologically valid replacement of the obsolete GO filler on the
  single `ObjectSomeValuesFrom(obo:RO_0002215 obo:GO_0051024)` conjunct with
  the active replacement `GO:0002639`, matching gold logically.
- Tight scope: the only issue-relevant edit is the single intended line in
  `src/ontology/cl-edit.owl`; no unrelated terms or axioms were modified, and
  the agent correctly stayed out of the broader release-time
  `deprecated_class_reference` check that the issue thread discussed but that
  gouttegd explicitly scoped out of gold PR #3309.

## Issues

- None biologically or ontologically substantive. The agent's axiom differs
  from gold only in the order of the two commutative `RO_0002215` conjuncts
  (agent: `GO_0045830` then `GO_0002639` from literal in-place substitution;
  gold/ROBOT: sorted `GO_0002639` then `GO_0045830`). `ObjectIntersectionOf`
  is order-independent, so the axioms are logically identical — the metadiff
  conjunct-reorder artifact, not an error.
- Incidental EOF-newline normalization: the agent's save added a trailing
  newline at the end of `cl-edit.owl` (`\ No newline at end of file` → final
  newline), producing a second spurious no-op diff hunk (~line 34718) absent
  from gold. Harmless to the ontology but gratuitous file churn that further
  deflates line-based recall (driving F1 to 0.333 rather than the 0.500 of
  the in-place runs). Not scored as `over_editing` — a pure tooling side
  effect with zero semantic impact; preserving the original EOF state would
  be best practice.
- Note: this attempt file lacks the agent PR/issue comment block present in
  #567, so methodology narrative is unavailable; the diff itself is identical
  and correct.
