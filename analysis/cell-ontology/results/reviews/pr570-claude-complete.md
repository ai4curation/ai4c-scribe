---
ontology: cell-ontology
issue_number: 3379
pr_number: 3444
eval_repo_pr: 570
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

The agent made exactly the substantive change the issue asked for: in the
`EquivalentClasses` axiom for CD4-positive CD11b-positive dendritic cell
(CL:0000999) it replaced the genus `obo:CL_0000990` (conventional dendritic
cell) with `obo:CL_0002465` (CD11b-positive dendritic cell), byte-for-byte
identical to gold PR #3444 on that line. It then went beyond the
tightly-scoped gold by rewriting the `IAO_0000115` textual definition and
adding a trailing EOF newline. The agent diff is identical to sibling attempt
#509 (same blob `bfeea74`). The metadiff F1=0.500 (P=1.000, R=0.333)
**under-represents** core correctness — the one essential edit is perfect —
but the low recall genuinely reflects doing *more* than the single-line gold,
i.e. over-editing, not omission.

## Strengths

- Correct genus substitution `CL_0000990` → `CL_0002465` in the equivalence
  axiom for CL:0000999 — identical to the human gold edit, precision 1.000,
  no edits to any other term.
- All five differentia restrictions preserved exactly (the two `CL_4030046`
  lacks-plasma-membrane-part restrictions on PR:000001026/PR:000001084, the
  CD4 `RO_0002104`, and the two `RO_0002215` capable-of
  `GO_0001816`/`GO_0050728`); logical meaning unchanged apart from the
  intended genus refinement.
- Tightly scoped to one file and the CL:0000999 block; no cross-term leakage.
- Good methodology in the PR comment: inspected CL:0000999, CL:0002465 and
  CL:0002454, explicitly grounded the change in the `CL_0002454` precedent the
  issue cites, and noted the pre-existing asserted
  `SubClassOf(CL_0000999 CL_0002465)`.

## Issues

- Scope/over-editing vs the tightly-scoped gold: gold changed exactly one line
  and left the text definition and EOF newline untouched. This attempt also
  rewrites `IAO_0000115` using the more aggressive variant — discarding the
  original "CD8-alpha-negative CD11b-positive dendritic cell is a conventional
  dendritic cell that is CD11b-positive, CD4-positive..." frame and replacing
  it with "A CD11b-positive dendritic cell that is CD4-positive and is
  CD205-negative and CD8-alpha-negative." This drops the explicit prose
  CD11b-positive assertion and is a heavier edit than a minimal genus-phrase
  swap; a curator could reasonably prefer the original wording preserved
  (contrast with the conservative variant in attempt #292).
- Serialization churn: a newline added at end of `cl-edit.owl`
  (`\ No newline at end of file` removed) — a robot/serializer artifact far
  from the issue locus, not an intentional edit, but a real diff line that
  lowers recall.
- These extras (def rewrite + EOF newline) are the sole reason F1 is 0.500;
  none is an ontological error, but they diverge from the human's minimal,
  single-line approach.
