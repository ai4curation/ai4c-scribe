---
ontology: mondo
issue_number: 9896
pr_number: 10207
eval_repo_pr: 486
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

Second copilot/sonnet run; the committed diff (`8f01663`) is byte-identical to
attempt #523. It renamed MONDO:0957382, added four synonyms, **replaced** the
parent (MONDO:0017338 deleted, MONDO:0011612 added) with an `excluded_subClassOf`
axiom, added an `intersection_of` equivalence definition, a `clingen` subset,
and a `dc:creator` property, and sourced the "MMDS7" abbreviation synonym to
`[NCBI:2653]` (the GCSH NCBI Gene ID, not a citation). The curator declined to
rename and added the ClinGen label only as an EXACT synonym, keeping both
parents. F1=0.095 fairly reflects that only the issue tracker aligns with gold.

## Strengths

- Added `property_value: IAO:0000233 ".../issues/9896"` matching gold.
- ClinGen synonym present with the correct `{OMO:0002001=.../clingen}`
  preferred-label qualifier.
- Definition's clinical-spectrum text closely tracks gold's wording, indicating
  correct source material was located.

## Issues

- Instruction violation: removed `is_a: MONDO:0017338` and replaced it with
  MONDO:0011612 + `excluded_subClassOf MONDO:0017338`, against the config rule
  and contradicting gold (which kept both parents).
- Wrong approach: renamed the primary label, the change the curator rejected.
- Citation error: `synonym: "MMDS7" EXACT ABBREVIATION [NCBI:2653]` cites the
  GCSH NCBI Gene ID as if it were a source for the disease abbreviation.
- Scope creep / over-editing: four synonyms, `intersection_of` equivalence
  axiom, `clingen` subset, `dc:creator` — none requested, none in gold.
- ClinGen synonym sources empty `[]`; def sources/genus differ from gold
  (gold keeps MMDS genus, curator ORCID 0000-0002-7638-4659).
- Net: failure — identical destructive over-edit and fabricated NCBI citation
  as #523.
