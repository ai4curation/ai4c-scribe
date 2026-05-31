---
ontology: mondo
issue_number: 9909
pr_number: 10208
eval_repo_pr: 258
agent: std_opencode_kimi
model: kimi-k2.6
runtime: opencode
agent_config_tag: v3
case_type: synonym_update
difficulty: simple
f1: 0.2
precision: 0.125
recall: 0.5
jaccard: 0.111
outcome: partial_success
failure_modes: [under_editing, missed_requirement]
case_quality: poor
case_quality_reason: gold_uses_curator_orcid_source_and_expansive_reinterpretation
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

## Summary

The agent located MONDO:0015912, added the missing `MATINS` synonym, repaired the empty-bracket
citation on `MYH9-related disease`, and added the issue term tracker — the same three line-changes
as the best attempt, and tied for top F1 (0.200). The headline strength is methodology: it
performed real literature research and grounded both new sources in **PMID:31384439**
(Fernandez-Prado et al., 2019, *Clin Kidney J*), quoting the exact sentence listing MATINS among
the historical names. The metadiff score **under-represents** quality; the gap is the six
RELATED→EXACT scope promotions the gold also made (which the issue did not request) plus the
gold's unguessable curator-ORCID source token.

## Strengths

- Strong, verifiable methodology: identified and read the full text of PMID:31384439 and quoted
  the passage ("...different names ... (MATINS, May-Hegglin anomaly, Fechtner, Epstein and
  Sebastian syndromes...)"), then used that PMID as the source for both `MATINS` and the
  previously-uncited `MYH9-related disease` synonym. A real, traceable provenance — arguably
  superior to the gold's bare curator ORCID.
- Added `synonym: "MATINS" EXACT ABBREVIATION [PMID:31384439]` — same synonym the gold added.
- Fixed the policy-violating empty `[]` on `MYH9-related disease`, supplying a peer-reviewed
  citation rather than guessing a database xref.
- Added `property_value: IAO:0000233 ".../issues/9909"` term tracker, byte-identical to gold.
- Correctly retained Epstein/Fechtner/May-Hegglin/Sebastian per the curator comment, with a
  well-reasoned rationale (merged OMIM entries, GARD/NCIT provenance, merged obsolete MONDO terms).
- Claims `make NORM` and `robot convert` ran without errors (more complete than the Opus attempt,
  which could not run ODK).

## Issues

- Under-editing: like every attempt in this cohort, it missed the six RELATED→EXACT scope
  promotions (`Alport syndrome with macrothrombocytopenia`, `FTNS`, `macrothrombocytopenia
  progressive deafness`, `MHA`, `MYH9 related disorders`, `SBS`). Defensible (not requested in
  the issue) but the reason recall caps at 0.5.
- Tagged `MATINS` as `ABBREVIATION`; the gold did not use the ABBREVIATION subtype for MATINS
  (gold: `synonym: "MATINS" EXACT [...]`). MATINS is in fact an acronym, so the agent's choice is
  ontologically reasonable, but it is a small divergence from gold.
- Source divergence vs gold (PMID vs curator ORCID) — agent's choice is sound practice but
  guarantees a metadiff miss on those lines.
