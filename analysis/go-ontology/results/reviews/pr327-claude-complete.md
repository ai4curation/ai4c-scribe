---
ontology: go-ontology
issue_number: 31295
pr_number: 32040
eval_repo_pr: 327
agent: std_claude_opus47
model: claude-opus-4.7
runtime: claude
agent_config_tag: v9
case_type: new_term
difficulty: medium
f1: 0.75
precision: 0.75
recall: 0.75
jaccard: 0.6
outcome: success
failure_modes: []
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

# Review: Eval PR #327 (claude-opus-4.7 / claude) — Issue #31295 / Gold PR #32040

## Summary

The agent created `GO:7770070 p24 cargo receptor complex` as a `cellular_component`
child of `GO:0062137 cargo receptor complex` with a `capable_of_part_of GO:0006888`
relationship — structurally identical to the gold PR's axiomatization. This is the
top-scoring attempt in the case (F1 0.750) and is a genuine success: the metadiff
slightly under-represents quality because the residual gap is only definition
wording and synonym-string variation, not any ontological error. The agent's
explicit decision to mirror the sibling `GO:0061852` precedent (`is_a` parent +
`capable_of_part_of` process) rather than over-assert an `intersection_of` exactly
matches the gold author's stated reasoning in the issue thread.

## Strengths

- **Correct core axiomatization, matching gold exactly**: `is_a: GO:0062137` plus
  `relationship: capable_of_part_of GO:0006888 ! endoplasmic reticulum to Golgi
  vesicle-mediated transport`. This is precisely what the human (dragon-ai-agent)
  committed, and it correctly follows the sibling `GO:0061852 retrograde cargo
  receptor complex, Golgi to ER` precedent (which uses `capable_of_part_of
  GO:0006890`).
- **Sound design-pattern judgment**: explicitly declined an `intersection_of`
  logical definition because no "GPI-anchored protein cargo receptor activity" MF
  exists and the parent already supplies the necessary+sufficient activity-based
  frame — the same rationale the gold author gave on the issue ("LMAN/ERGIC-53
  also fits that frame").
- **Correctly left location inherited**: did not assert a fixed `part_of` ER/Golgi
  membrane because the complex genuinely cycles ER↔Golgi, relying on the inherited
  `part_of GO:0016020 membrane` from the parent. This avoids the over-localization
  error several lower-scoring attempts made (`part_of GO:0070971`).
- **Definition is biologically accurate and complete**: captures hetero-oligomeric
  composition, ER–Golgi cycling, COPII cargo selection, GPI-anchored cargo
  preference, and one-member-per-subfamily (α/β/γ/δ) — all five PMIDs from the
  issue used and reference-validated, none fabricated.
- **Good methodology and communication**: confirmed no pre-existing p24/emp24/TMED
  complex, posted a detailed rationale and an issue comment to @ValWood flagging
  the open question of whether to also axiomatize the retrograde COPI role — a
  nuanced and curator-appropriate note.

## Issues

- **Definition wording differs from gold** (style, not error): the gold reused
  ValWood's "def synthesised form" almost verbatim; the agent paraphrased it. Both
  are accurate; the difference costs metadiff points without reflecting a quality
  gap.
- **Synonym set differs** (style): agent used "p24 complex" EXACT, "p24 protein
  complex" EXACT, "TMED complex"/"emp24/erv25 complex" RELATED; gold used "p24
  complex" EXACT and "Emp24-Erv25 complex"/"p24 family complex"/"TMED complex"
  RELATED. The agent's "p24 protein complex" as EXACT is defensible; "emp24/erv25
  complex" lowercased differs cosmetically from gold's "Emp24-Erv25 complex". No
  semantic error.
- No omissions or scope creep. This is the strongest attempt in the cohort.
