---
ontology: mondo
issue_number: 9937
pr_number: 10112
eval_repo_pr: 36
agent: std_codex_g55
model: gpt-5.5
runtime: codex
agent_config_tag: v3
case_type: new_term
difficulty: medium
f1: 0.5
precision: 0.5
recall: 0.5
jaccard: 0.333
outcome: success
failure_modes: [over_editing]
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

## Summary

Issue #9937 is a fully-specified ClinGen new-term request ("KY-related neuromyopathy" under
`MONDO:0100546`, gene-disease axiom on `KY`/HGNC:26576, four PMIDs, ClinGen URL, three children
to reclassify), resolved by the single human PR #10112 (approved first time) — a sound case.
This gpt-5.5/codex attempt produced a correct term and correctly reclassified all three
children. F1 0.5 **under-represents** quality; the gap is the unavoidable new-term-ID mismatch
plus `subset: rare` and a notable per-child source-attribution choice.

## Strengths

- Correct genus-differentia logical definition (`intersection_of: MONDO:0100546` +
  `has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/26576`), matching
  gold and the `disease_series_by_gene` pattern.
- Correct parent `is_a: MONDO:0100546`; correct gene KY = HGNC:26576 (verified via HGNC REST
  per the PR comment).
- All three requested children reclassified with `is_a: MONDO:7770012`, existing parents
  preserved — matches issue and human PR.
- All four PMIDs and the ClinGen URL as sources on the new term; `IAO:0000233` to #9937 and
  `dc:creator` ORCID present.
- Methodology narrative documents NORM normalization, `robot convert` syntax validation, and
  `git diff --check`.

## Issues

- New-term ID `MONDO:7770012` ≠ gold `MONDO:1010194` — unavoidable; dominant F1 penalty,
  amplified across the three child lines.
- Per-child source attribution is split by phenotype (MONDO:0014922 sourced to
  PMID:27484770/27485408; MONDO:0044648 to PMID:28488683/32818658). This is a thoughtful,
  evidence-aware choice (matching myopathy vs spastic-paraplegia literature to the right
  children) but diverges from gold's uniform ClinGen-URL source on every child edge, lowering
  line-match recall while arguably being more precise scientifically.
- Added `subset: rare`, which gold omits; questionable for a gene-grouping class, a minor
  over-edit.
- Definition genus "hereditary neuromuscular disease" vs gold "neuromyopathy" — equivalent.
- `dc:creator` = requester ORCID `0000-0002-2078-7280` vs gold curator ORCID
  `0000-0002-5002-8648`; defensible, convention mismatch.
- No synonym on the new term (gold has one OMO-qualified ClinGen synonym) — minor omission.
- Standalone `relationship: has_material_basis_in_germline_mutation_in` line not in gold
  (conventional); did not reproduce gold's `excluded_from_qc_check` on MONDO:0044647 (internal
  QC artifact, pure recall penalty).

Correct and ontologically sound; the divergent (but defensible) per-child sourcing and
`subset: rare` are the only real concerns. Metadiff is a floor on quality.
