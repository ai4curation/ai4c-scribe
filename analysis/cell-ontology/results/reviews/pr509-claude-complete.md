---
ontology: cell-ontology
issue_number: 3379
pr_number: 3444
eval_repo_pr: 509
agent: std_opencode_gpt54
model: gpt-5.4
runtime: opencode
agent_config_tag: ai4curation/cl-agent-config@v3
case_type: reclassification
difficulty: simple
f1: 0.500
precision: 1.000
recall: 0.333
jaccard: 0.333
outcome: partial_success
failure_modes:
  - over_editing
  - scope_creep
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-17
---

## Summary

The agent made the exact substantive change the issue asked for: in the
`EquivalentClasses` axiom for CD4-positive CD11b-positive dendritic cell
(CL:0000999) it replaced the genus `obo:CL_0000990` (conventional dendritic
cell) with `obo:CL_0002465` (CD11b-positive dendritic cell), byte-for-byte
identical to gold PR #3444 on that line. It then went beyond the
tightly-scoped gold by also rewriting the `IAO_0000115` textual definition and
adding a trailing newline at EOF. The metadiff F1=0.500 (P=1.000, R=0.333)
**under-represents** core correctness (the one essential edit is perfect) but
the low recall is genuinely caused by the agent doing *more* than gold, not by
omission — so this is over-editing relative to a single-line gold, not
under-editing.

## Strengths

- Correct genus substitution `CL_0000990` → `CL_0002465` in the equivalence
  axiom for CL:0000999 — identical to the human gold edit, with precision
  1.000 and no spurious edits to other terms.
- All five differentia restrictions preserved exactly (the two `CL_4030046`
  lacks-plasma-membrane-part restrictions on PR:000001026/PR:000001084, the
  CD4 `RO_0002104` has-plasma-membrane-part, and the two `RO_0002215`
  capable-of `GO_0001816`/`GO_0050728`); the logical meaning is unchanged
  apart from the intended genus refinement.
- Tightly scoped to one file (`src/ontology/cl-edit.owl`) and to the
  CL:0000999 block; no scope creep into neighbouring classes.
- The textual-definition update is directionally good curation hygiene:
  keeping the free-text definition consistent with the revised logical genus
  follows the issue's spirit, and matches the `CL_0002454` precedent the
  issue cites.

## Issues

- Scope/over-editing vs the tightly-scoped gold: the gold PR changed exactly
  one line (the genus only) and deliberately left both the text definition and
  the EOF newline untouched. This attempt additionally rewrote the
  `IAO_0000115` definition and the def rewrite here is the more aggressive
  variant — it discards the original sentence frame ("CD8-alpha-negative
  CD11b-positive dendritic cell is a conventional dendritic cell that is
  CD11b-positive, CD4-positive...") and replaces it with a fully restructured
  "A CD11b-positive dendritic cell that is CD4-positive and is CD205-negative
  and CD8-alpha-negative." This drops the explicit CD11b-positive assertion
  from the prose and is a heavier edit than the minimal genus-phrase swap; a
  curator could reasonably want the original wording preserved.
- Serialization churn: the diff adds a newline at end of `cl-edit.owl`
  (`\ No newline at end of file` removed) far from the issue locus. This is a
  robot/serializer artifact rather than an intentional edit, but it is a real
  diff line and contributes to the recall penalty.
- These two extras are the entire reason F1 is 0.500 rather than ~0.8–1.0;
  none of them is an ontological error, but they diverge from the human's
  minimal, single-line approach.
