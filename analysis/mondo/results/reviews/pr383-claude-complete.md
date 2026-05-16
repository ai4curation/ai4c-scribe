---
ontology: mondo
issue_number: 9937
pr_number: 10112
eval_repo_pr: 383
agent: std_claude_op47
model: claude-opus-4.7
runtime: claude
agent_config_tag: v3
case_type: new_term
difficulty: medium
f1: 0.571
precision: 0.667
recall: 0.5
jaccard: 0.4
outcome: success
failure_modes: [over_editing]
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

## Summary

Issue #9937 is a fully-specified ClinGen new-term request ("KY-related neuromyopathy" under
`MONDO:0100546`, gene-disease axiom on `KY`/HGNC:26576, four PMIDs, ClinGen URL, three children
to reclassify), resolved by the single human PR #10112 (approved first time) — a sound case.
This opus-4.7 attempt produced an ontologically correct term and correctly reclassified all
three children, with the most thorough provenance of any attempt. Its F1 of 0.571 (precision
0.667 is the highest of the nine, recall 0.5) **substantially under-represents** quality: the
recall hit is driven by the unavoidable new-term-ID mismatch plus the agent adding several
defensible pattern-derived synonyms gold did not include.

## Strengths

- Correct genus-differentia logical definition: `intersection_of: MONDO:0100546` +
  `has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/26576`, matching
  gold and the `disease_series_by_gene` pattern.
- Correct parent `is_a: MONDO:0100546`; correct gene KY = HGNC:26576.
- All three requested children reclassified with `is_a: MONDO:7770012`, existing parents
  preserved. The PR comment explicitly and correctly articulates the Mondo convention ("a more
  specific parent is added without removing existing parents unless explicitly requested") —
  strong methodology and self-explanation.
- Richest correct provenance: ClinGen `subset: clingen {source="MONDO:CLINGEN"}`, the
  OMO-qualified ClinGen synonym `"KY-related neuromyopathy" EXACT {OMO:0002001=...}` that
  exactly matches gold's synonym line, plus all four PMIDs and the ClinGen URL.
- `IAO:0000233` to #9937 and `dc:creator` ORCID present.
- The single attempt that reproduced gold's OMO-qualified ClinGen synonym verbatim — a
  precision win and the reason its precision is the highest in the cohort.

## Issues

- New-term ID `MONDO:7770012` ≠ gold `MONDO:1010194` — unavoidable; principal recall penalty.
- Added two extra pattern-derived synonyms ("hereditary neuromuscular disease caused by
  mutation in KY", "KY hereditary neuromuscular disease" from
  `MONDO:patterns/disease_series_by_gene`) and `subset: disease_grouping` that gold omits.
  These are defensible pattern outputs (the DOSDP pattern does generate such synonyms) but
  exceed the human's minimal stanza and lower recall.
- Definition genus "hereditary neuromuscular disease" vs gold "neuromyopathy" — equivalent.
- `dc:creator` = requester ORCID `0000-0002-2078-7280` rather than gold curator ORCID
  `0000-0002-5002-8648`; defensible, convention mismatch.
- Standalone `relationship: has_material_basis_in_germline_mutation_in` line not in gold
  (conventional, mild recall hit); did not reproduce gold's `excluded_from_qc_check` on
  MONDO:0044647 (an internal QC artifact, unanticipatable, pure recall penalty).

This is arguably the most complete and best-justified attempt; the low F1 reflects metadiff
artifacts and a richer-than-gold stanza, not errors.
