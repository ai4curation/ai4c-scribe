---
ontology: mondo
issue_number: 9937
pr_number: 10112
eval_repo_pr: 686
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
byte-identical to #740, blob `ad127a1`). F1 0.500 **under-represents** quality; the gap is
the unavoidable new-term-ID mismatch (`MONDO:7770012` vs gold `MONDO:1010194`) plus the
use of PMIDs rather than the ClinGen URL as the child-line `source=` (a provenance-wording
convention difference that costs the line-match versus gold on the three child lines).

## Strengths

- Correct genus-differentia logical definition: `intersection_of: MONDO:0100546` +
  `intersection_of: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/26576`,
  matching gold and the `disease_series_by_gene` pattern.
- Correct parent `is_a: MONDO:0100546` and correct gene KY = `HGNC:26576` on the
  `has_material_basis_in_germline_mutation_in` relationship.
- All three requested children (`MONDO:0014922`, `MONDO:0044648`, `MONDO:0044647`)
  reclassified with `is_a: MONDO:7770012`, existing parents preserved — matches the issue and
  the human PR in substance.
- Definition "Any hereditary neuromuscular disease in which the cause of the disease is a
  mutation in the KY gene" — genus equivalent to gold's "neuromyopathy" (gold's genus is the
  more specific synonym; both correctly point at `MONDO:0100546`).
- All four PMIDs as definition sources; added a reasonable `synonym: "KY neuromyopathy" EXACT`
  with the ClinGen source; `IAO:0000233` to #9937 and `dc:creator` ORCID present.

## Issues

- New-term ID `MONDO:7770012` ≠ gold `MONDO:1010194` — unavoidable placeholder-ID artifact;
  dominant F1 penalty, amplified across the three child `is_a` lines.
- Used PMIDs (`source="PMID:27484770", ...`) as the `source=` on the child `is_a` and the
  new-term `is_a`, where gold uses the ClinGen affiliation URL. Defensible (the PMIDs are
  valid evidence) but a convention mismatch that lowers line-match versus gold and explains
  the ~0.11 F1 deficit relative to the claude-haiku attempts (#469/#602).
- Synonym text "KY neuromyopathy" differs from gold's "KY-related neuromyopathy" and lacks
  the `OMO:0002001` qualifier — minor fidelity gap, but a synonym was supplied (unlike
  #469/#602), which is a partial credit.
- `dc:creator` = requester ORCID `0000-0002-2078-7280` vs gold curator
  `0000-0002-5002-8648`; defensible convention mismatch.
- Standalone `relationship: has_material_basis_in_germline_mutation_in` line on the new term
  not in gold (conventional); did not reproduce gold's `excluded_from_qc_check` on
  `MONDO:0044647` — internal QC artifact, pure recall penalty.

Correct and well-scoped; no substantive error. The F1 floor is the placeholder ID plus the
PMID-vs-ClinGen-URL provenance convention on the child lines, not a quality defect.
