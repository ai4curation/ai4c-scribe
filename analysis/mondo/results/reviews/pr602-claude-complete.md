---
ontology: mondo
issue_number: 9937
pr_number: 10112
eval_repo_pr: 602
agent: std_claude_hai45
model: claude-haiku-4.5
runtime: claude
agent_config_tag: v3
case_type: new_term
difficulty: medium
f1: 0.609
precision: 0.583
recall: 0.636
jaccard: 0.438
outcome: success
failure_modes:
  - under_editing
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-17
---

## Summary

Issue #9937 is a fully-specified ClinGen new-term request: add "KY-related neuromyopathy"
under `MONDO:0100546`, a gene-disease axiom on KY (`HGNC:26576`), four PMIDs, the ClinGen
affiliation URL, and reclassify `MONDO:0014922`, `MONDO:0044648`, `MONDO:0044647` as children.
The single human PR #10112 was approved first time — a sound case (`case_quality: ok`). This
claude-haiku-4.5/claude attempt produced the correct term, the correct genus-differentia
axiom, and correctly reclassified all three children with existing parents preserved. The
diff is byte-identical to #469 (blob `06b249e`); F1 0.609 is the best in the case and
**under-represents** quality — the gap is the unavoidable new-term-ID mismatch
(`MONDO:7770012` vs gold `MONDO:1010194`) plus provenance/synonym conventions. This run also
includes a detailed, accurate PR comment documenting the design decisions.

## Strengths

- Correct genus-differentia logical definition (`intersection_of: MONDO:0100546` +
  `has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/26576`), matching
  gold and the `disease_series_by_gene` pattern.
- Correct parent `is_a: MONDO:0100546`; correct gene KY = `HGNC:26576`.
- All three requested children (`MONDO:0014922`, `MONDO:0044648`, `MONDO:0044647`)
  reclassified with `is_a: MONDO:7770012` and existing parents preserved — exactly matching
  the issue and human PR in substance.
- Used the ClinGen affiliation URL as the `source=` on every child `is_a`, matching gold's
  provenance convention (the reason it out-scores the gpt-5.4 attempts #686/#740).
- Definition wording "Any neuromyopathy in which the cause of the disease is a mutation in
  the KY gene" matches the requester's requested format and gold's genus.
- Strong, accurate PR-comment methodology: explicitly verified the unique NTR-range ID, the
  KY HGNC identifier against existing MONDO usage, the parent term, ran `make NORM`, and
  documented the multiple-parent-retention design decision per MONDO guidelines.

## Issues

- New-term ID `MONDO:7770012` ≠ gold `MONDO:1010194` — unavoidable placeholder-ID artifact;
  dominant F1 penalty amplified across the three child `is_a` lines.
- No synonym on the new term — gold includes one OMO-qualified ClinGen EXACT synonym; minor
  omission lowering ClinGen preferred-label fidelity (`under_editing`).
- `dc:creator` = requester ORCID `0000-0002-2078-7280` vs gold curator ORCID
  `0000-0002-5002-8648`; defensible convention mismatch, not an error.
- Standalone `relationship: has_material_basis_in_germline_mutation_in` line on the new term
  not present in gold; conventional, mildly recall-lowering.
- Did not reproduce gold's `excluded_from_qc_check` on `MONDO:0044647` — internal QC artifact,
  pure recall penalty, not a substantive defect.

Correct and well-scoped; only genuine gap is the missing ClinGen synonym. Metadiff is a floor
imposed by the placeholder ID, QC artifact, and provenance-wording conventions.
