---
ontology: cell-ontology
issue_number: 3534
pr_number: 3535
eval_repo_pr: 520
agent: std_opencode_g54
model: gpt-5.4
runtime: opencode
agent_config_tag: ai4curation/cl-agent-config@v3:.
case_type: new_term
difficulty: medium
case_quality: ok
case_quality_reason: sound_gold_but_new_term_scores_sensitive_to_taxon_and_provenance
f1: 0.000
precision: 0.000
recall: 0.000
jaccard: 0.000
outcome: partial_success
failure_modes:
  - misattribution
  - wrong_pattern
  - under_editing
  - over_editing
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-17
---

## Summary

This run is byte-identical to eval PR #582 (same agent/model gpt-5.4/opencode, same
output blob `1c26cc082`), so the assessment carries over: a substantively sound NTR
resolution — verbatim issue definition with `PMID:30983567` xref, correct parent
`CL_0007001` (skeletogenic cell), correct periosteum term `UBERON_0002515`, mouse
taxon restriction — but with F1=0.000 driven by a **misattribution** (claimed the
term exists upstream as `CL:0020028` and minted that ID instead of the canonical
placeholder `CL_9900000` the gold used) and use of `RO_0002100` (located in) instead
of the gold's `BFO_0000050` (part of) for the periosteum location. Partial success.

## Strengths

- Verbatim issue definition with the correct `oboInOwl:hasDbXref "PMID:30983567"`
  on `IAO_0000115`, matching the gold definition text.
- Correct parent `CL_0007001` (skeletogenic cell), correctly resolving the issue's
  non-existent requested parent "skeletal cell".
- Correct anatomical term `UBERON_0002515` (periosteum) — same target as the gold.
- Mouse taxon restriction `RO_0002162 some NCBITaxon_10090` present.

## Issues

- Misattribution: claims the term "exists upstream as `CL:0020028`" and mints
  `CL_0020028` rather than the canonical `CL_9900000` placeholder used by the gold
  for this genuinely new term. Incorrect provenance claim and the main F1 driver.
- Wrong pattern: periosteum location via `RO_0002100` (located in) rather than the
  gold's `BFO_0000050` (part of), which is the established CL containment pattern.
- Omission: no `RO_0002175` "present in taxon" annotation (gold has it); minor.
- Scope: extra `IAO_0000233` term-tracker annotation and run-date `terms:date`,
  absent from the tightly-scoped gold (defensible provenance, minor).
