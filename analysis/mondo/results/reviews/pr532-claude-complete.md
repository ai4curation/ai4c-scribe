---
ontology: mondo
issue_number: 9937
pr_number: 10112
eval_repo_pr: 532
agent: std_copilot_son45
model: claude-sonnet-4.5
runtime: copilot
agent_config_tag: v3
case_type: new_term
difficulty: medium
f1: 0.583
precision: 0.583
recall: 0.583
jaccard: 0.412
outcome: success
failure_modes: [over_editing]
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

## Summary

Issue #9937 is a fully-specified ClinGen new-term request for "KY-related neuromyopathy" under
`MONDO:0100546`, with a `KY`/HGNC:26576 gene-disease axiom, four PMIDs, the ClinGen affiliation
URL, and three children (MONDO:0014922, MONDO:0044648, MONDO:0044647) to reclassify; it was
resolved by the single human PR #10112 (approved first time), so the gold is complete and the
case is sound. This copilot/sonnet-4.5 attempt produced a correct, well-formed new term and
correctly reclassified all three children. Its F1 of 0.583 **under-represents** quality: the
diff is byte-identical to attempt #491 (same blob `e9d3ddd`) and the score gap is almost
entirely the unavoidable new-term-ID mismatch plus provenance/wording conventions.

## Strengths

- Correct logical definition: `intersection_of: MONDO:0100546` + `intersection_of:
  has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/26576`, matching gold
  and the `disease_series_by_gene` pattern.
- Correct asserted parent `is_a: MONDO:0100546` and correct gene (KY = HGNC:26576).
- All three requested children reclassified with `is_a: MONDO:7770012`, existing parents
  preserved — exactly the human's and the issue's intent.
- Sources include all four PMIDs; `is_a:` source annotations on the children include both the
  ClinGen affiliation URL and the requester ORCID, a richer (and defensible) provenance than
  gold's URL-only annotation.
- `IAO:0000233` link to #9937 and a `dc:creator` ORCID present, both in gold.
- Scope discipline good: only the new term and three child edges touched.

## Issues

- New-term ID `MONDO:7770012` ≠ gold `MONDO:1010194` (unavoidable; the dominant F1 penalty,
  amplified across the three child lines).
- Added `subset: rare` to the new term, which gold does not include. The gold term is a
  gene-grouping class, not a rare-disease leaf, so `subset: rare` is questionable and is a
  genuine (if minor) over-edit/scope creep.
- Definition genus is "hereditary neuromuscular disease" vs gold's "neuromyopathy" —
  substantively equivalent; gold tracks the issue's literal "Any neuromyopathy ..." wording.
- `dc:creator` uses requester ORCID `0000-0002-2078-7280` rather than gold's curator ORCID
  `0000-0002-5002-8648`; defensible from the issue text but a convention mismatch.
- Added a standalone `relationship: has_material_basis_in_germline_mutation_in` line absent
  from gold (conventional in Mondo, mildly recall-lowering).
- Omitted gold's explicit OMO-qualified ClinGen synonym and the `excluded_from_qc_check` line
  on MONDO:0044647 (an internal QC artifact, pure recall penalty, not a defect).

Correct and well-scoped apart from the `subset: rare` over-edit; metadiff is a quality floor
here, not a ceiling.
