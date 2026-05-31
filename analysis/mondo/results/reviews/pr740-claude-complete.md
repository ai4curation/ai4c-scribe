---
ontology: mondo
issue_number: 9937
pr_number: 10112
eval_repo_pr: 740
agent: std_opencode_g54
model: gpt-5.4
runtime: opencode
agent_config_tag: v3
case_type: new_term
difficulty: medium
f1: 0.5
precision: 0.5
recall: 0.5
jaccard: 0.333
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
gpt-5.4/opencode attempt produced the correct new term, the correct genus-differentia axiom,
and correctly reclassified all three children with existing parents preserved (diff
byte-identical to #686, blob `ad127a1`), accompanied by a thorough and accurate methodology
narrative. F1 0.500 **under-represents** quality; the gap is the unavoidable new-term-ID
mismatch (`MONDO:7770012` vs gold `MONDO:1010194`) plus the PMID-vs-ClinGen-URL provenance
convention on the three child `is_a` lines.

## Strengths

- Correct genus-differentia logical definition (`intersection_of: MONDO:0100546` +
  `has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/26576`), matching
  gold and the `disease_series_by_gene` pattern.
- Correct parent `is_a: MONDO:0100546`; correct gene KY = `HGNC:26576`.
- All three requested children (`MONDO:0014922`, `MONDO:0044648`, `MONDO:0044647`)
  reclassified with `is_a: MONDO:7770012` and existing parents preserved, exactly per the
  issue and human PR in substance.
- Strong, verifiable methodology in the PR comment: read the imported issue context,
  inspected existing KY-related terms, confirmed the `disease_series_by_gene.yaml` pattern,
  verified all four PMIDs on PubMed, confirmed KY = `HGNC:26576` against existing MONDO usage,
  ran `robot convert` syntax validation and `make NORM` then re-applied normalized output.
- All four PMIDs as sources; reasonable `synonym: "KY neuromyopathy" EXACT` with ClinGen
  source; `IAO:0000233` to #9937 and `dc:creator` ORCID present.

## Issues

- New-term ID `MONDO:7770012` ≠ gold `MONDO:1010194` — unavoidable placeholder-ID artifact;
  dominant F1 penalty, amplified across the three child `is_a` lines.
- Used PMIDs as the `source=` on the child `is_a` and new-term `is_a`, where gold uses the
  ClinGen affiliation URL; defensible but a convention mismatch lowering line-match versus
  gold and explaining the ~0.11 F1 deficit relative to claude-haiku attempts (#469/#602).
- Synonym "KY neuromyopathy" differs from gold's "KY-related neuromyopathy" and lacks the
  `OMO:0002001` ClinGen qualifier — minor fidelity gap (still a partial credit; a synonym
  was supplied, unlike #469/#602).
- `dc:creator` = requester ORCID `0000-0002-2078-7280` vs gold curator
  `0000-0002-5002-8648`; defensible convention mismatch.
- Standalone `relationship: has_material_basis_in_germline_mutation_in` line on the new term
  not in gold (conventional); did not reproduce gold's `excluded_from_qc_check` on
  `MONDO:0044647` — internal QC artifact, pure recall penalty.

Correct and well-scoped with the strongest documented methodology of the four reviewed runs;
no substantive error. The F1 floor is the placeholder ID plus provenance convention, not a
quality defect.
