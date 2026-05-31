---
ontology: mondo
issue_number: 9909
pr_number: 10208
eval_repo_pr: 670
agent: std_opencode_g55
model: gpt-5.5
runtime: opencode
agent_config_tag: v3
case_type: synonym_update
difficulty: simple
f1: 0.19
precision: 0.125
recall: 0.4
jaccard: 0.105
outcome: partial_success
failure_modes: [over_editing, missed_requirement]
case_quality: poor
case_quality_reason: gold_uses_curator_orcid_source_and_expansive_reinterpretation
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-17
---

## Summary

Deterministic replay of the same gpt-5.5/opencode behavior as #727 (identical diff, blob
`1cab9b7`): the agent added the genuinely-missing `MATINS` synonym (`EXACT ABBREVIATION`,
ClinGen-sourced), repaired the empty-bracket source on the existing lowercase `synonym:
"MYH9-related disease" EXACT []` (to the same ClinGen URL), added the `IAO:0000233` term
tracker (byte-identical to gold), and **also added a new capitalization-duplicate** `synonym:
"MYH9-Related Disease" EXACT [issue URL]` alongside the preserved lowercase form. MATINS is
the correct core change; the case-duplicate synonym is a net-negative over-edit. Metadiff
F1=0.190 (recall=0.4) under-represents the MATINS work but correctly penalizes the duplicate.

## Strengths

- Added `synonym: "MATINS" EXACT ABBREVIATION [...]` — the only requester-preferred synonym
  genuinely absent from the term and the core substantive change the gold made.
- Preserved the existing lowercase `MYH9-related disease` synonym and only repaired its empty
  `[]` source, rather than renaming it (better than #567's case-rename).
- Added `property_value: IAO:0000233 ".../issues/9909"` term tracker, byte-identical to gold.
- Retained the historical/former-entity synonyms, consistent with @MeeSiing's curator comment
  that the other synonyms should be kept because OMIM provenance supports them.

## Issues

- Over-editing (the headline problem): introduced a NEW `synonym: "MYH9-Related Disease"
  EXACT [https://github.com/monarch-initiative/mondo/issues/9909]` differing from the
  preserved/repaired lowercase `synonym: "MYH9-related disease"` only by capitalization — a
  duplicate-by-case synonym the gold never introduced and a synonym-hygiene violation.
- Weak provenance: sourcing the new (duplicate) synonym to a bare GitHub issue URL; the issue
  is not an authoritative nomenclature source. OMIM/Orphanet/PMID would be preferable.
- Under-editing: missed the six RELATED→EXACT scope promotions like the whole cohort
  (defensible, not in the issue text, but caps recall).
- No PR/issue comment captured in the attempt record (bare diff), so the agent's reasoning is
  not auditable here; judged on the diff alone, which carries the duplicate-synonym defect.
- Net: the MATINS add is correct and valuable, but the case-duplicate synonym is a genuine
  regression that places this below the best cohort attempts (#396/#258).
