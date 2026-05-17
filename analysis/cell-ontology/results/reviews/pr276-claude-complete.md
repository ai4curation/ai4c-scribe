---
ontology: cell-ontology
issue_number: 3379
pr_number: 3444
eval_repo_pr: 276
agent: std_claude_opus47
model: claude-opus-4.7
runtime: claude
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

The agent made exactly the change the issue asked for: in the `EquivalentClasses`
axiom for CD4-positive CD11b-positive dendritic cell (CL:0000999) it replaced the
genus `obo:CL_0000990` (conventional dendritic cell) with `obo:CL_0002465`
(CD11b-positive dendritic cell), matching the gold PR #3444 byte-for-byte on the
substantive line. In addition it removed the now-redundant asserted
`SubClassOf(obo:CL_0000999 obo:CL_0002465)` line, which the gold PR retained;
this is the only source of the recall penalty. The metadiff F1 of 0.800
(P=1.000, R=0.667) **under-represents** the quality: the core edit is perfect and
the extra deletion is ontologically sound and explicitly sanctioned by the agent
config.

## Strengths

- Correct genus substitution `CL_0000990` → `CL_0002465` in the equivalence
  axiom — identical to the human gold edit (precision 1.000, no spurious edits to
  other terms).
- Recognised that once `CL_0002465` is the equivalence genus, the asserted
  `SubClassOf(obo:CL_0000999 obo:CL_0002465)` becomes redundant (it is now
  entailed by the equivalence axiom). The agent config explicitly states "The
  reasoner can find the most specific `is_a`, so it's OK to leave this off",
  so removing it is a defensible cleanup, not an error.
- Tightly scoped: the diff touches only the CL:0000999 block; no scope creep into
  neighbouring classes.
- Preserved every differentia restriction (the two `CL_4030046` lacks-part
  restrictions, the CD4 `RO_0002104`, and the two `RO_0002215` capable-of
  restrictions), so the logical meaning of the class is unchanged apart from the
  intended genus refinement.

## Issues

- Style/convention only: the gold PR kept the explicit
  `SubClassOf(obo:CL_0000999 obo:CL_0002465)` line (the conservative choice that
  keeps an asserted parent). Removing it changes nothing semantically and is
  config-defensible, but it does diverge from the human's more minimal edit and
  is the entire reason the metadiff is below 1.0. No correctness or completeness
  problem.
- The agent config also recommends linking back to the issue with a
  `term_tracker_item` annotation; this attempt did not add one (the human gold
  also omitted it, so this is not penalised, but it is a missed config nicety).
