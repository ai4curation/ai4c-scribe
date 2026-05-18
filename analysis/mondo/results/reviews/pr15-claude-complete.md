---
ontology: mondo
issue_number: 9956
pr_number: 10214
eval_repo_pr: 15
agent: std_codex_g54
model: gpt-5.4
runtime: codex
agent_config_tag: v2-noskills
case_type: new_term
difficulty: medium
f1: 0.462
precision: 0.500
recall: 0.429
jaccard: 0.300
outcome: partial_success
failure_modes: [missed_requirement, wrong_pattern, scope_creep]
case_quality: poor
case_quality_reason: new_term_canonical_id_artifact
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-17
---

## Summary

gpt-5.4/codex (running the `v2-noskills` config) created a structurally valid new term with placeholder `MONDO:7770736`, correct gene grounding (`HGNC:28422`) and asserted gene relationship. However it diverged from gold in three substantive ways: the logical-definition genus is `MONDO:0100500` (Mendelian neurodevelopmental disorder) rather than gold's `MONDO:0700092`; the definition cites only 6 PMIDs (dropping issue PMIDs and adding a non-issue one); and it introduced a likely-fabricated TRACK-expansion synonym. F1=0.462 reflects both the new_term artifact and real content/pattern divergence — a genuine partial outcome.

## Strengths

- Correct asserted `has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/28422`; verified TSEN2=HGNC:28422.
- Kept the requested parent `MONDO:0700092` as an asserted `is_a` and used the requested broad label as the primary name.
- Reasonable narrative distinguishing the broad TSEN2 spectrum from the narrower pre-existing `MONDO:0012890` (PCH2B) and declining to rename/replace it.
- Ran `robot convert` syntax validation.

## Issues

- **Wrong logical-definition genus**: `intersection_of: MONDO:0100500` (Mendelian neurodevelopmental disorder) differs from gold's `intersection_of: MONDO:0700092` (neurodevelopmental disorder). The asserted parent and the equivalence-axiom genus are inconsistent (asserts both `MONDO:0700092` and `MONDO:0100500` but only `MONDO:0100500` enters the intersection_of) — a pattern error.
- **Definition divergence (omission)**: cites only `PMID:34964109, 18711368, 20952379, 23562994, 38347586, 38622473` — drops issue PMIDs `32404165` and `38438125` and adds non-issue `34964109`. The issue explicitly listed the definition source PMIDs.
- **Likely fabricated synonym**: `"TSEN2 related atypical hemolytic uremic syndrome, craniofacial malformations, kidney failure" NARROW [PMID:34964109]` — a constructed TRACK acronym expansion not verified against the source; same fabrication-risk pattern flagged for pr551 in the METADATA note.
- **Scope creep**: extra parent `is_a: MONDO:0100500` not requested or in gold.
- **Missing ClinGen synonym**: gold's `OMO:0002001`-qualified ClinGen EXACT synonym is absent.
- **Case quality note**: part of the F1 gap is the new_term canonical-ID artifact — see METADATA Curation Note.
