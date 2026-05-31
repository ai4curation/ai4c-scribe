---
ontology: cell-ontology
issue_number: 2967
pr_number: 3309
eval_repo_pr: 74
agent: std_codex_g54
model: gpt-5.4
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

gpt-5.4 (codex) produced the correct biological fix for issue #2967, replacing
obsolete `GO:0051024` with `GO:0002639` in the CL:0002038 (T follicular helper
cell) `EquivalentClasses` axiom — semantically identical to the merged gold PR
#3309. The metadiff F1 of 0.333 (lower than the 0.500 of the claude/opencode
runs) **severely under-represents** quality and is depressed by *two* pure
serialization artifacts: (1) the commutative reordering of the two `RO_0002215`
conjuncts, and (2) an incidental EOF-newline normalization (`\ No newline at
end of file` → final newline added) that produces a second spurious diff hunk
unrelated to the issue.

## Strengths

- Correct, biologically valid replacement of the obsolete GO filler
  (`GO:0051024` → `GO:0002639`) on the single `ObjectSomeValuesFrom(obo:RO_0002215
  ...)` term — exactly the issue's actionable ask.
- Good methodology documented: confirmed the obsolete term occurred only in the
  CL:0002038 axiom, verified `GO:0051024` no longer appears, and ran
  `robot convert -i src/ontology/cl-edit.owl -o /tmp/cl-edit.ofn` to confirm the
  file still parses.
- The substantive issue-relevant hunk is correctly scoped to one line.

## Issues

- None biologically/ontologically substantive. The core edit is correct and
  logically equivalent to gold (conjunct order in a commutative
  `ObjectIntersectionOf` is irrelevant).
- Incidental EOF-newline change: the agent's save normalized the missing
  final newline at the end of `cl-edit.owl`, producing a second no-op diff
  hunk (lines ~34718). This is harmless to the ontology but is gratuitous file
  churn the human PR did not make, and it further deflates the line-based
  metadiff recall. Best practice would be to preserve the original EOF state;
  the claude/opencode runs avoided this. Not scored as `over_editing` because
  it is a tooling side effect with zero semantic impact, but worth noting.
