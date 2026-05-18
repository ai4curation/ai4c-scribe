---
ontology: mondo
issue_number: 9937
pr_number: 10112
eval_repo_pr: 469
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
under `MONDO:0100546` (hereditary neuromuscular disease), a gene-disease axiom on KY
(`HGNC:26576`), four PMIDs, the ClinGen affiliation URL, and reclassify three existing terms
(`MONDO:0014922`, `MONDO:0044648`, `MONDO:0044647`) as children. The single human PR #10112
was approved first time — a sound case (`case_quality: ok`). This claude-haiku-4.5/claude
attempt produced the correct new term, the correct genus-differentia axiom, and correctly
reclassified all three children with existing parents preserved. F1 0.609 (best in the case,
diff byte-identical to #602, blob `06b249e`) **under-represents** quality; the gap is the
unavoidable new-term-ID mismatch (`MONDO:7770012` vs gold `MONDO:1010194`, amplified across
the three child `is_a` lines) plus provenance/synonym-wording conventions.

## Strengths

- Correct genus-differentia logical definition: `intersection_of: MONDO:0100546` +
  `intersection_of: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/26576`,
  matching gold and the `disease_series_by_gene` pattern.
- Correct parent `is_a: MONDO:0100546` and correct gene KY = `HGNC:26576` on the
  `has_material_basis_in_germline_mutation_in` relationship.
- All three requested children (`MONDO:0014922`, `MONDO:0044648`, `MONDO:0044647`)
  reclassified with `is_a: MONDO:7770012`, existing parents preserved — matches the issue and
  the human PR exactly in substance.
- Used the ClinGen affiliation URL (`https://clinicalgenome.org/affiliation/40151/`) as the
  `source=` on every child `is_a`, matching the gold's provenance convention for these lines —
  this is why it scores higher than the gpt-5.4 attempts (#686/#740) that used PMIDs there.
- Definition phrased as "Any neuromyopathy in which the cause of the disease is a mutation in
  the KY gene" — exactly the requester's requested wording and gold's genus ("neuromyopathy").
- All four PMIDs as definition sources; `IAO:0000233` to #9937 and `dc:creator` ORCID present.

## Issues

- New-term ID `MONDO:7770012` ≠ gold `MONDO:1010194` — unavoidable placeholder-ID artifact;
  dominant F1 penalty, amplified across the three child `is_a` lines (pure recall loss).
- No synonym on the new term — gold includes one OMO-qualified ClinGen EXACT synonym
  (`"KY-related neuromyopathy" EXACT ... {OMO:0002001=...}`). Minor omission lowering fidelity
  to the ClinGen preferred-label convention; counts as `under_editing`.
- `dc:creator` = requester ORCID `0000-0002-2078-7280` rather than gold curator ORCID
  `0000-0002-5002-8648`; defensible from the issue, a convention mismatch not an error.
- Standalone `relationship: has_material_basis_in_germline_mutation_in ... {source="PMID:27484770",
  source="https://orcid.org/0000-0002-2078-7280"}` line is present where gold has none on the
  new term (gold's standalone relationship is on the child stanzas); conventional, mildly
  recall-lowering, not wrong.
- Did not reproduce gold's `excluded_from_qc_check` on `MONDO:0044647` — an internal QC
  artifact, pure recall penalty, not a substantive defect.

Correct and well-scoped; the only genuine quality gap is the missing ClinGen synonym. The
metadiff floor (placeholder ID + QC artifact + provenance wording) under-represents this.
