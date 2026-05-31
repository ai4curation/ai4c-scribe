---
ontology: mondo
issue_number: 9937
pr_number: 10112
eval_repo_pr: 491
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

Issue #9937 is a fully-specified ClinGen new-term request ("KY-related neuromyopathy" under
`MONDO:0100546`, gene-disease axiom on `KY`/HGNC:26576, four PMIDs, ClinGen URL, three children
to reclassify), resolved by the single human PR #10112 (approved first time) — a sound case
with a complete gold. This copilot/sonnet-4.5 attempt is **byte-identical to attempt #532**
(same output blob `e9d3ddd`): a correct, well-formed new term with all three children correctly
reclassified. F1 0.583 **under-represents** quality; the gap is the unavoidable new-term-ID
mismatch plus provenance/wording conventions.

## Strengths

- Correct genus-differentia logical definition (`intersection_of: MONDO:0100546` +
  `has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/26576`), matching
  gold and the `disease_series_by_gene` pattern.
- Correct parent `is_a: MONDO:0100546`; correct gene KY = HGNC:26576.
- All three requested children (MONDO:0014922, MONDO:0044648, MONDO:0044647) reclassified with
  `is_a: MONDO:7770012`, existing parents preserved — matches the issue and the human PR.
- All four cited PMIDs included; child `is_a:` source annotations carry both the ClinGen URL
  and the requester ORCID (richer than gold).
- `IAO:0000233` to #9937 and `dc:creator` ORCID present.
- Tightly scoped diff.

## Issues

- New-term ID `MONDO:7770012` ≠ gold `MONDO:1010194` — unavoidable and the dominant F1 penalty
  (compounded across three child lines).
- Added `subset: rare`, which gold omits; for a gene-grouping class this is questionable and
  is a genuine minor over-edit.
- Definition genus "hereditary neuromuscular disease" vs gold "neuromyopathy" — equivalent in
  substance.
- `dc:creator` = requester ORCID `0000-0002-2078-7280` rather than gold curator ORCID
  `0000-0002-5002-8648`; defensible from the issue, convention mismatch.
- Standalone `relationship: has_material_basis_in_germline_mutation_in` line not in gold
  (conventional, mildly recall-lowering); omits gold's OMO-qualified synonym and the
  `excluded_from_qc_check` QC artifact on MONDO:0044647 (pure recall penalty, not a defect).

Functionally correct and well-scoped except for `subset: rare`; metadiff is a floor on quality.
