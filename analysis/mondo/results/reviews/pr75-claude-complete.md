---
ontology: mondo
issue_number: 9937
pr_number: 10112
eval_repo_pr: 75
agent: std_opencode_g55
model: gpt-5.5
runtime: opencode
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
This gpt-5.5/opencode attempt produced a correct term and correctly reclassified all three
children. F1 0.5 (the diff is byte-identical to attempt #56, blob `df272e4`) **under-represents**
quality; the gap is the unavoidable new-term-ID mismatch plus `subset: rare` and
provenance/wording conventions.

## Strengths

- Correct genus-differentia logical definition (`intersection_of: MONDO:0100546` +
  `has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/26576`), matching
  gold and the `disease_series_by_gene` pattern.
- Correct parent `is_a: MONDO:0100546`; correct gene KY = HGNC:26576 (explicitly verified via
  HGNC REST per the PR comment).
- All three requested children reclassified with `is_a: MONDO:7770012`, existing parents
  preserved — matches issue and human PR.
- All four PMIDs and the ClinGen URL as sources; `IAO:0000233` to #9937 and `dc:creator`
  ORCID present.
- Sound methodology narrative: checked parent/children, verified the gene, attempted full-text
  retrieval, ran `make NORM`, and validated with `robot convert`.

## Issues

- New-term ID `MONDO:7770012` ≠ gold `MONDO:1010194` — unavoidable; dominant F1 penalty,
  amplified across the three child lines.
- Added `subset: rare`, which gold omits; for a gene-grouping class this is questionable and a
  genuine minor over-edit.
- Definition genus "hereditary neuromuscular disease" vs gold "neuromyopathy" — equivalent.
- `dc:creator` = requester ORCID `0000-0002-2078-7280` rather than gold curator ORCID
  `0000-0002-5002-8648`; defensible from the issue, convention mismatch.
- No synonym at all on the new term — gold includes one OMO-qualified ClinGen synonym; this is
  a minor omission that lowers fidelity to the ClinGen-preferred label convention.
- Standalone `relationship: has_material_basis_in_germline_mutation_in` line not in gold
  (conventional, mildly recall-lowering); did not reproduce gold's `excluded_from_qc_check` on
  MONDO:0044647 (internal QC artifact, pure recall penalty).

Correct and well-scoped apart from `subset: rare` and the missing synonym; metadiff is a floor.
