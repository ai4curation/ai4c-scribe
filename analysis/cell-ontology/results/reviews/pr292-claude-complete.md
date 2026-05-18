---
ontology: cell-ontology
issue_number: 3379
pr_number: 3444
eval_repo_pr: 292
agent: std_codex_gpt54
model: gpt-5.4
runtime: codex
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
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-17
---

## Summary

The agent made exactly the substantive change the issue asked for: in the
`EquivalentClasses` axiom for CD4-positive CD11b-positive dendritic cell
(CL:0000999) it replaced the genus `obo:CL_0000990` (conventional dendritic
cell) with `obo:CL_0002465` (CD11b-positive dendritic cell), byte-for-byte
identical to gold PR #3444 on that line. It additionally made a *minimal*
consistency edit to the `IAO_0000115` textual definition (swapping only the
genus phrase) and added a trailing EOF newline. The metadiff F1=0.500
(P=1.000, R=0.333) **under-represents** the actual quality: the one essential
edit is perfect, and of the three new attempts on this case this is the
best-judged — its text-def change is the conservative variant rather than a
full rewrite. The recall penalty reflects doing slightly more than the
single-line gold, not an omission.

## Strengths

- Correct genus substitution `CL_0000990` → `CL_0002465` in the equivalence
  axiom for CL:0000999 — identical to the human gold edit, precision 1.000,
  no edits to any other term.
- All five differentia restrictions preserved exactly (the two `CL_4030046`
  lacks-plasma-membrane-part restrictions on PR:000001026/PR:000001084, the
  CD4 `RO_0002104`, and the two `RO_0002215` capable-of
  `GO_0001816`/`GO_0050728`); logical meaning unchanged apart from the
  intended genus refinement.
- The text-definition edit is the *minimal* one: it changes only
  "...is a conventional dendritic cell that is CD11b-positive, CD4-positive..."
  → "...is a CD11b-positive dendritic cell that is CD4-positive..." preserving
  the original sentence frame. This is a defensible, low-risk consistency fix
  aligning the prose with the revised logical genus, and is less invasive than
  the rewrites in sibling attempts #509/#570.
- Strong methodology evidenced in the PR comment: it verified the existing
  axioms for CL:0000999, CL:0002465 and CL:0002454, explicitly cited the
  `CL_0002454` precedent named in the issue, noted the pre-existing asserted
  `SubClassOf(CL_0000999 CL_0002465)`, and attempted a `robot convert` syntax
  check (correctly reporting robot was unavailable rather than fabricating a
  pass).

## Issues

- Scope/over-editing vs the tightly-scoped gold: the gold PR changed exactly
  one line and intentionally left the text definition and EOF newline alone.
  This attempt also edits `IAO_0000115` and adds an end-of-file newline. The
  text-def change is defensible curation hygiene (and arguably an improvement),
  but it diverges from the human's minimal single-line edit and is the main
  driver of the 0.500 F1.
- Serialization churn: a newline was added at end of `cl-edit.owl`
  (`\ No newline at end of file` removed), a robot/serializer artifact far
  from the issue locus rather than an intentional change. Minor, but it is a
  real diff line lowering recall.
- No ontological errors; the divergences are scope/style only.
