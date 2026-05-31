---
ontology: mondo
issue_number: 9909
pr_number: 10208
eval_repo_pr: 555
agent: std_codex_g55
model: gpt-5.5
runtime: codex
agent_config_tag: v3
case_type: synonym_update
difficulty: simple
f1: 0.19
precision: 0.125
recall: 0.4
jaccard: 0.105
outcome: partial_success
failure_modes: [under_editing, missed_requirement, over_editing]
case_quality: poor
case_quality_reason: gold_uses_curator_orcid_source_and_expansive_reinterpretation
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

## Summary

The agent added `MATINS`, added the issue term tracker, and addressed the empty-bracket
`MYH9-related disease` citation — but did so by **introducing a duplicate synonym string**:
it added a new `synonym: "MYH9-Related Disease" EXACT [MEDGEN:1704278]` (capitalized variant)
*alongside* re-sourcing the existing lowercase `synonym: "MYH9-related disease" EXACT
[GARD:0000180]`. F1=0.190 is the lowest of the three "MATINS-added" attempts; the score modestly
under-represents the core correct work but the duplicate-casing synonym is a genuine over-editing
error not present in the gold.

## Strengths

- Identified MONDO:0015912 and added `synonym: "MATINS" EXACT ABBREVIATION [MEDGEN:1704278,
  OMIM:155100]` — the one genuinely missing synonym, with plausible MedGen/OMIM provenance.
- Added `property_value: IAO:0000233 ".../issues/9909"` term tracker, byte-identical to gold.
- Did not delete the historical syndrome synonyms, consistent with the curator's resolution.

## Issues

- Over-editing / duplicate synonym (real error): added `synonym: "MYH9-Related Disease" EXACT
  [MEDGEN:1704278]` as a *new* line while the term already carries `synonym: "MYH9-related
  disease" EXACT [...]`. These differ only by capitalization of "Related"/"related"; Mondo
  treats them as redundant synonym strings and this would likely be flagged by QC. The gold did
  not add a capitalized duplicate — it only re-sourced the existing lowercase synonym.
- Misread the requester's quoted label "MYH9-Related Disease" as a *missing* synonym requiring a
  new entry, rather than recognizing it as a case variant of the existing one (the Opus and Kimi
  attempts correctly identified it was already present).
- Under-editing: missed all six RELATED→EXACT scope promotions the gold made (`Alport syndrome
  with macrothrombocytopenia`, `FTNS`, `macrothrombocytopenia progressive deafness`, `MHA`,
  `MYH9 related disorders`, `SBS`); recall 0.4 is the lowest of the partial-success attempts.
- Source divergence vs gold's curator ORCID (MedGen/GARD vs ORCID) — defensible practice but a
  guaranteed metadiff miss; minor relative to the duplicate-synonym issue.
- No PR comment / methodology narrative was captured (codex attempt), so research depth cannot
  be assessed; the diff alone shows weaker synonym hygiene than the Opus/Kimi attempts.
