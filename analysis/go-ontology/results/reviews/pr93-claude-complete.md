---
ontology: go-ontology
issue_number: 31295
pr_number: 32040
eval_repo_pr: 93
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
outcome: success
failure_modes: [over_editing]
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

# Review: Eval PR #93 (gpt-5.5 / opencode) — Issue #31295 / Gold PR #32040

## Summary

The agent created `GO:7770070 p24 cargo receptor complex` under `GO:0062137`
with the gold's `capable_of_part_of GO:0006888` relationship, plus three EXACT
synonyms and a four-PMID definition. F1 is 0.696. The PR comment text claims a
`capable_of GO:0097020 COPII receptor activity` relationship, but the actual diff
does **not** include it — only the description was inconsistent; the committed
term is clean. Solid success: the core axiomatization matches gold and the small
metadiff gap is wording/synonym variation.

## Strengths

- **Correct parent + process axiom matching gold**: `is_a: GO:0062137` and
  `relationship: capable_of_part_of GO:0006888 ! endoplasmic reticulum to Golgi
  vesicle-mediated transport` — identical to the gold and consistent with sibling
  `GO:0061852`.
- **No over-localization in the committed diff**: did not assert `part_of
  GO:0070971`; relies on inherited parent membrane localization (correct, matches
  gold rationale).
- **Accurate definition**: p24-family composition, ER↔Golgi cycling, ER exit site
  cargo selection, GPI-anchored cargo, COPII vesicles. Four PMIDs (32456004,
  34647572, 27569046).
- **Careful reference hygiene**: explicitly caught and rejected the
  PMCID-vs-PMID ambiguity (PMC2265561 → not PMID:2265561), a genuinely
  thoughtful validation step that avoided introducing a wrong xref.
- Good methodology: pre/post `make travis_build`, RESEARCH.md excerpt validation.

## Issues

- **Description/diff inconsistency** (communication, not an ontology error): the PR
  summary asserts a `GO:0097020 COPII receptor activity` relationship that is
  absent from the committed diff. The committed term is correct; the prose
  over-claims. Minor but a curator reading the PR comment would be misled.
- **Extra synonym vs. gold** (minor `over_editing`): added "p24 cargo receptor
  protein complex" EXACT, which is redundant with the term label itself; gold did
  not include it. Harmless but unnecessary.
- **Synonym set differs from gold** (style): "p24 complex"/"p24 protein complex"
  EXACT vs. gold's RELATED set; no semantic error.
- Definition wording differs from gold (style). Net result is a correct,
  annotation-ready term equivalent in substance to the gold.
