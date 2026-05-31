---
ontology: go-ontology
issue_number: 31295
pr_number: 32040
eval_repo_pr: 87
agent: std_opencode_g55
model: gpt-5.5
runtime: opencode
agent_config_tag: v9
case_type: new_term
difficulty: medium
f1: 0.696
precision: 0.667
recall: 0.727
jaccard: 0.533
outcome: partial_success
failure_modes: [over_editing, wrong_pattern]
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

# Review: Eval PR #87 (gpt-5.5 / opencode) — Issue #31295 / Gold PR #32040

## Summary

The agent created `GO:7770070 p24 cargo receptor complex` under `GO:0062137` with
two EXACT synonyms and a four-PMID definition. F1 is 0.696. Unlike its sibling
run #93, this attempt's committed diff includes **two** relationships: `capable_of
GO:0097020 ! COPII receptor activity` and `capable_of_part_of GO:0006888`. The
`capable_of_part_of` matches gold, but the extra `capable_of GO:0097020` is a
redundant/over-asserted axiom (the parent already supplies `capable_of GO:0038024
cargo receptor activity` via its logical def). A partial success: correct and
usable, but over-axiomatized relative to gold and the sibling precedent.

## Strengths

- **Correct parent and the gold's process axiom**: `is_a: GO:0062137` and
  `relationship: capable_of_part_of GO:0006888 ! endoplasmic reticulum to Golgi
  vesicle-mediated transport`.
- **No fixed-location over-assertion**: did not add `part_of GO:0070971`,
  correctly leaving membrane localization inherited (matches gold rationale).
- **Accurate definition**: p24-family complex, early secretory pathway membranes,
  ER↔Golgi cycling, selective COPII cargo export. Four PMIDs.
- Good validation methodology (pre/post `make travis_build`, reference caching;
  honestly reported a PMID:32456004 HTTP 429 and the manual fallback check).

## Issues

- **Over-asserted `capable_of GO:0097020 COPII receptor activity`** (`over_editing`
  / `wrong_pattern`): the parent `GO:0062137` already carries `capable_of
  GO:0038024 cargo receptor activity` in its logical definition; adding a
  narrower `capable_of` activity axiom on the child is the kind of
  over-specification the gold author explicitly avoided ("the parent's logical
  def already gives necessary+sufficient framing"). The sibling `GO:0061852` does
  not assert an activity relationship. This is a defensible-but-not-ideal extra
  axiom that diverges from the established pattern.
- **Synonym set differs from gold** (style): "p24 complex"/"p24 protein complex"
  EXACT vs. gold's "p24 complex" EXACT + 3 RELATED.
- Definition wording differs from gold (style, not error). The term is biologically
  correct and annotation-ready; the only substantive deviation is the extra
  activity axiom.
