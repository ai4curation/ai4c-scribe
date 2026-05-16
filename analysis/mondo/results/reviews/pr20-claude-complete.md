---
ontology: mondo
issue_number: 9937
pr_number: 10112
eval_repo_pr: 20
agent: std_codex_g54
model: gpt-5.4
runtime: codex
agent_config_tag: v3
case_type: new_term
difficulty: medium
f1: 0.5
precision: 0.583
recall: 0.438
jaccard: 0.333
outcome: partial_success
failure_modes: [over_editing, scope_creep]
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

## Summary

Issue #9937 is a fully-specified ClinGen new-term request ("KY-related neuromyopathy" under
`MONDO:0100546`, gene-disease axiom on `KY`/HGNC:26576, four PMIDs, ClinGen URL, three children
to reclassify), resolved by the single human PR #10112 (approved first time) — a sound case.
This gpt-5.4/codex attempt created an ontologically correct new term and reclassified all three
children, but is the **most over-editing** attempt of the nine: it added extra
`has_material_basis_in_germline_mutation_in` relationships and multiple extra `IAO:0000233`
issue links onto the pre-existing child terms. F1 0.5 reflects both the unavoidable ID mismatch
and these genuine scope-creep edits; metadiff under-represents the core correctness but the
extra edits are real.

## Strengths

- Correct genus-differentia logical definition on the new term (`intersection_of:
  MONDO:0100546` + `has_material_basis_in_germline_mutation_in
  http://identifiers.org/hgnc/26576`), matching gold and the `disease_series_by_gene` pattern.
- Correct parent `is_a: MONDO:0100546`; correct gene KY = HGNC:26576 (verified via NCBI Gene
  per the PR comment, which also lists the correct titles of all four PMIDs — good evidence
  handling).
- All three requested children reclassified with `is_a: MONDO:7770012`, existing parents
  preserved.
- All four PMIDs and the ClinGen URL as sources; `IAO:0000233` to #9937 on the new term.
- Strong, accurate literature-grounding: correctly identifies the myopathy vs spastic-paraplegia
  split across the cited PMIDs and applies per-child source attribution accordingly.

## Issues

- New-term ID `MONDO:7770012` ≠ gold `MONDO:1010194` — unavoidable; a major recall penalty.
- Scope creep: added `IAO:0000233 .../issues/9937` to the three pre-existing child terms
  (MONDO:0014922, MONDO:0044647/0044648 stanzas) and added new
  `relationship: has_material_basis_in_germline_mutation_in HGNC:26576` lines onto MONDO:0044647
  and MONDO:0044648. Gold makes none of these edits to the children beyond the single new
  `is_a:` edge. Adding a germline-mutation relationship asserting KY causation directly on the
  two lateral-tongue-atrophy syndrome terms is an unrequested ontological assertion and is the
  weakest decision in the cohort (those syndromes already have their own genetic axioms; this
  risks redundancy/over-assertion). This depresses precision relative to the cleaner attempts.
- `dc:creator` is `doi:10.1186/s13326-024-00320-3` (the Mondo methods paper DOI) rather than
  an ORCID — gold uses the curator ORCID `0000-0002-5002-8648`. The DOI value is an incorrect
  attribution type for `dc:creator` and is the only attempt to make this particular error.
- Added `subset: clingen` and `subset: rare` plus two pattern synonyms gold omits; the
  OMO-qualified ClinGen synonym is correctly reproduced, a precision win.
- Definition genus "hereditary neuromuscular disease" vs gold "neuromyopathy" — equivalent.
- Did not reproduce gold's `excluded_from_qc_check` on MONDO:0044647 (internal QC artifact,
  pure recall penalty, not a defect).

The new term itself is correct, but the unrequested edits to the pre-existing child stanzas
(extra germline-mutation relationships and issue links) and the malformed `dc:creator` DOI make
this a partial success rather than a clean one.
