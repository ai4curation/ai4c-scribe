---
ontology: mondo
issue_number: 9707
pr_number: 9745
eval_repo_pr: 48
agent: std_codex_g55
model: gpt-5.5
runtime: codex
agent_config_tag: v3
case_type: new_term
difficulty: hard
f1: 0.308
precision: 0.25
recall: 0.4
jaccard: 0.182
outcome: partial_success
failure_modes: [under_editing, missed_requirement, over_editing]
case_quality: poor
case_quality_reason: placeholder_vs_canonical_id_artifact
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

## Summary

This attempt (gpt-5.5 / codex) created both new terms with the correct revised definitions, gave the SCN5A term a `disease_series_by_gene` logical definition, parented the new terms under the two correct supers, reparented the requested phenotypes, and correctly excluded atrioventricular block. Its distinguishing feature is heavy **source over-stamping**: it appended `source="https://github.com/monarch-initiative/mondo/issues/9707"` as a second source on essentially every new `is_a` and on the new terms' parent axioms, which the gold did not do — this inflates the diff and depresses precision without changing semantics. Metadiff F1=0.308 under-represents conceptual correctness because of the placeholder-ID artifact (`MONDO:7770003/4` vs gold `MONDO:1010180/1`).

## Strengths

- Both new terms with correct **revised** definitions per @LengUNC's follow-up.
- Correct parents on both new terms: `cardiac rhythm disease` (MONDO:0007263) and `cardiogenetic disease` (MONDO:0100547); SCN5A term also under the grouping term.
- SCN5A term given a `disease_series_by_gene` equivalence (`intersection_of: cardiac rhythm disease and has_material_basis_in_germline_mutation_in HGNC:10593`); SCN5A verified as HGNC:10593 via the HGNC service.
- Singular label "cardiogenetic rhythm disorder" matching gold/MONDO convention; plural retained as a synonym.
- Reparented the five SCN5A-specific phenotypes and the family-level rhythm terms; correctly excluded atrioventricular block per @katiermullen.
- Documented validation (make NORM, robot convert).

## Issues

- **Source over-stamping**: every new `is_a` and the new terms' parent/relationship axioms carry an extra `source="https://github.com/monarch-initiative/mondo/issues/9707"` alongside the ClinGen affiliation URL. The gold uses only the ClinGen affiliation source on is_a lines. This is unrequested provenance noise that lowers precision and is not MONDO convention for is_a source on reparenting.
- Did not reproduce the atrioventricular dissociation reclassification (defensible — out of issue scope — but lowers recall).
- The grouping term MONDO:7770003 has no logical definition (only `is_a` parents), unlike #407/#89 which add the `has_characteristic some inherited` equivalence; weaker modelling than the best attempts.
- Placeholder ID mismatch (`MONDO:7770003/4` vs gold `MONDO:1010180/1`) is an eval-harness artifact and the dominant metadiff penalty.
