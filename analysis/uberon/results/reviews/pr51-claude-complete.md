---
ontology: uberon
issue_number: 3490
pr_number: 3585
eval_repo_pr: 51
agent: std_opencode_g55
model: gpt-5.5
runtime: opencode
agent_config_tag: v3
case_type: axiom_repair
difficulty: hard
f1: 0.333
precision: 0.333
recall: 0.333
jaccard: 0.200
outcome: success
failure_modes: [scope_creep]
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-16
---

## Summary

A second gpt-5.5/opencode run producing a byte-identical edit to attempt
#68: the UBERON:0005162 def is reworded to allow some whole cells, the
`composed_primarily_of GO:0005575` axiom and `[CARO:0001000]` xref are
preserved, and a `term_tracker_item` for #3490 is added. Correctly resolves
issue #3490; semantically equivalent to gold PR #3585. F1=0.333 is a
tiny-diff metadiff artifact and under-represents quality. True outcome:
success.

## Strengths

- Identical correct def to #68: removes the "(complete) cells as a part"
  restriction while keeping the "primarily multiple cell components / two or
  more cells / not itself a cell" core. Aligns with issue #3490 and FBbt
  #2008 intent.
- Explicitly reasoned about preserving the `composed_primarily_of
  GO:0005575` logical axiom (PR comment), correctly noting the relaxed def
  remains consistent with it — good ontological care.
- Retained `[CARO:0001000]` def xref (provenance preserved).
- Reproducibility across two runs (#68/#51) is a positive consistency signal.

## Issues

- Scope: same extra `property_value: term_tracker_item` as #68. Defensible
  provenance, but not in the gold diff nor requested; mild scope_creep.
- Omission vs gold: no clarifying `comment:`; nuance folded into a wordier
  def rather than gold's crisp def + comment split. Stylistically inferior
  to gold/FBbt canonical form, not an error.
- No correctness or syntax problems.
