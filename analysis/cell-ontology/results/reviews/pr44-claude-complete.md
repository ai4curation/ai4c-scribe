---
ontology: cell-ontology
issue_number: 3379
pr_number: 3444
eval_repo_pr: 44
agent: std_opencode_gpt55
model: gpt-5.5
runtime: opencode
agent_config_tag: ai4curation/cl-agent-config@v3
case_type: reclassification
difficulty: simple
f1: 0.800
precision: 1.000
recall: 0.667
jaccard: 0.667
outcome: success
failure_modes: []
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-16
---

## Summary

This is a sibling run to eval PR #64 (same model/runtime, same blob `a4d630f`)
and produces the identical diff: the genus in the `EquivalentClasses` axiom for
CL:0000999 is changed from `obo:CL_0000990` to `obo:CL_0002465` (matching gold
PR #3444 on the substantive line) plus an added
`AnnotationAssertion(obo:IAO_0000233 obo:CL_0000999 <.../issues/3379>)`
term-tracker annotation. The metadiff F1 of 0.800 (P=1.000, R=0.667) is lowered
only by the config-mandated term-tracker line, so it **under-represents** the
true quality.

## Strengths

- Correct, precise genus substitution `CL_0000990` → `CL_0002465`; all five
  differentia restrictions preserved unchanged.
- Added the `term_tracker_item` (`IAO_0000233`) issue link as the cl-agent-config
  CLAUDE.md instructs — instruction-following behaviour.
- PR comment shows good reasoning: cites the issue's own precedent `CL_0002454`,
  notes `CL_0002465` is itself a conventional dendritic cell, and ran
  `robot convert` to validate syntax before committing.
- Kept the asserted `SubClassOf(obo:CL_0000999 obo:CL_0002465)` line, matching
  the gold PR's conservative choice.

## Issues

- The PR comment states it "Updated the `CL_0000999` textual definition to mirror
  the revised logical genus", but the committed diff does **not** modify the
  `IAO_0000115` text definition (only the equivalence axiom and the added
  tracker line changed). This is a self-report inaccuracy, not an ontology
  error — and in fact leaving the text definition alone is harmless here since
  the gold PR also did not touch it. Worth noting as a methodology/reporting
  discrepancy.
- The only metadiff divergence from gold is the extra config-mandated
  `IAO_0000233` annotation — correct practice, not a defect.
