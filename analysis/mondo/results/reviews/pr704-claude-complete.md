---
ontology: mondo
issue_number: 9909
pr_number: 10208
eval_repo_pr: 704
agent: std_opencode_g54
model: gpt-5.4
runtime: opencode
agent_config_tag: v3
case_type: synonym_update
difficulty: simple
f1: 0.211
precision: 0.125
recall: 0.667
jaccard: 0.118
outcome: partial_success
failure_modes: [under_editing, missed_requirement]
case_quality: poor
case_quality_reason: gold_uses_curator_orcid_source_and_expansive_reinterpretation
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-17
---

## Summary

The agent located MONDO:0015912 and made only two edits: it repaired the policy-violating
empty-bracket citation on `synonym: "MYH9-related disease" EXACT []` by supplying
`[Orphanet:182050]`, and it added the `property_value: IAO:0000233 .../issues/9909` term
tracker (byte-identical to gold). It did **not** add `MATINS`, the one synonym from the
requester's preferred list that was genuinely missing from the term. Metadiff F1=0.211 with
recall=0.667 modestly **under-represents** the safety of the two edits made but correctly
reflects a real omission: this is the most conservative of the cohort and misses the core
substantive add the issue called for.

## Strengths

- Correctly fixed the empty `[]` on `synonym: "MYH9-related disease" EXACT []`, choosing
  `Orphanet:182050` by analogy to the sibling `MYH9-related disorder`/`MYH9-related syndrome`
  synonyms — a sound provenance heuristic (gold instead used the unguessable curator ORCID).
- Added `property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9909"`
  term tracker, byte-identical to gold.
- Correctly retained the historical synonyms (Epstein/Fechtner/May-Hegglin/Sebastian) per
  @MeeSiing's curator comment ("we will keep the other synonyms since OMIM still lists them"),
  declining the requester's literal removal ask — the right judgment call.
- Scope-disciplined: no spurious edits, no capitalization-duplicate synonyms (unlike #567/#727).

## Issues

- Missed requirement (the dominant gap): did **not** add `MATINS`. Of the requester's six
  preferred exact synonyms, MATINS was the only one absent from the term; the gold added it.
  This is the single most important substantive change the issue called for, and it was skipped.
- Under-editing: like every attempt in this cohort, it missed the six RELATED→EXACT scope
  promotions (`Alport syndrome with macrothrombocytopenia`, `FTNS`, `macrothrombocytopenia
  progressive deafness`, `MHA`, `MYH9 related disorders`, `SBS`). Defensible (not requested in
  the issue text) but contributes to the recall ceiling.
- Source divergence vs gold on `MYH9-related disease` (Orphanet:182050 vs curator ORCID) —
  the agent's choice is better practice but guarantees a metadiff miss on that line.
- Net assessment: this is weaker than the best cohort attempts (#396/#258), which made the
  identical safe edits *and* added MATINS. Doing less than those caps this at partial_success.
