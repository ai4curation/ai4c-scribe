---
ontology: mondo
issue_number: 9896
pr_number: 10207
eval_repo_pr: 523
agent: std_copilot_son45
model: claude-sonnet-4.5
runtime: copilot
agent_config_tag: v3
case_type: synonym_update
difficulty: simple
f1: 0.095
precision: 0.25
recall: 0.059
jaccard: 0.05
outcome: failure
failure_modes: [over_editing, scope_creep, wrong_pattern, instruction_violation]
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

## Summary

The curator declined to rename MONDO:0957382 and added the ClinGen label only
as an EXACT synonym, keeping the MMDS7 label and both parents. This
copilot/sonnet attempt renamed the term, added four synonyms, **replaced** the
parent (MONDO:0017338 deleted, MONDO:0011612 added) with an `excluded_subClassOf`
axiom, added an `intersection_of` equivalence definition, a `clingen` subset,
and a `dc:creator` property. It also introduced a citation error: the "MMDS7"
abbreviation synonym is sourced to `[NCBI:2653]`, which is the NCBI Gene ID for
GCSH, not a citation for the disease abbreviation. F1=0.095 fairly reflects
that essentially only the issue tracker aligns with gold.

## Strengths

- Added `property_value: IAO:0000233 ".../issues/9896"` matching gold.
- ClinGen synonym present with correct `{OMO:0002001=.../clingen}` qualifier.
- The clinical-spectrum phrasing in the definition closely mirrors gold's
  description text (neonatal fatal → attenuated developmental/seizure
  phenotype), showing the agent found the right source material.

## Issues

- Instruction violation: removed `is_a: MONDO:0017338` and replaced it with
  MONDO:0011612 plus an `excluded_subClassOf MONDO:0017338` axiom. The config
  forbids removing existing parents unless explicitly instructed; the curator
  kept both parents. The `excluded_subClassOf` axiom asserts the original
  parent is wrong — contradicted by gold retaining it.
- Wrong approach: renamed the primary label, the change the curator rejected.
- Citation error: `synonym: "MMDS7" EXACT ABBREVIATION [NCBI:2653]` — NCBI Gene
  2653 is GCSH (the gene), not a bibliographic/database citation for the
  disease abbreviation. This is an incorrect provenance assertion.
- Scope creep / over-editing: four synonyms, `intersection_of` equivalence
  axiom, `clingen` subset, `dc:creator` — none requested, none in gold.
- ClinGen synonym sources empty `[]`; gold cites the ClinGen affiliation and
  requester ORCID. Def cited `[https://orcid.org/0000-0002-7437-8060,
  PMID:36190515]` vs gold's MMDS genus and curator ORCID 0000-0002-7638-4659.
- Net: failure — destructive reparent against an explicit config rule plus a
  fabricated NCBI gene-ID citation on the abbreviation synonym.
