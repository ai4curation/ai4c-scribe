---
ontology: mondo
issue_number: 9909
pr_number: 10208
eval_repo_pr: 727
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

The agent located MONDO:0015912, added the genuinely-missing `MATINS` synonym
(`EXACT ABBREVIATION`, sourced to the ClinGen MONDO:0015912 condition page), repaired the
empty-bracket source on the existing lowercase `synonym: "MYH9-related disease" EXACT []`
(to the same ClinGen URL), and added the `IAO:0000233` term tracker (byte-identical to gold).
However it also **added a brand-new capitalization-duplicate** `synonym: "MYH9-Related
Disease" EXACT [issue URL]` alongside the preserved lowercase form. The MATINS add is the
correct core change, but the duplicate-by-case synonym is a net-negative over-edit. Metadiff
F1=0.190 (recall=0.4); the score under-represents the MATINS work but correctly penalizes the
duplicate. Identical diff to #670 (blob `1cab9b7`).

## Strengths

- Added `synonym: "MATINS" EXACT ABBREVIATION [...]` — the one requester-preferred synonym
  genuinely missing from the term and the core substantive change the gold made.
- Unlike #567, **preserved** the existing lowercase `MYH9-related disease` synonym and only
  repaired its empty `[]` source — closer to the gold's minimal-repair intent.
- Added `property_value: IAO:0000233 ".../issues/9909"` term tracker, byte-identical to gold.
- Retained the historical/former-entity synonyms, explicitly citing the issue-thread curation
  decision — aligned with @MeeSiing's "we will keep the other synonyms" comment.
- Documented validation: `obo-grep.pl`, ClinGen condition-page cross-check, `make NORM`,
  `robot convert`; honest about Docker/ODK unavailability.

## Issues

- Over-editing (the headline problem): introduced a NEW `synonym: "MYH9-Related Disease"
  EXACT [https://github.com/monarch-initiative/mondo/issues/9909]` that differs from the
  existing/repaired `synonym: "MYH9-related disease"` only by capitalization. This creates two
  synonyms with the same normalized surface form — a duplicate that violates synonym hygiene
  and that the gold did not introduce (gold kept a single lowercase synonym). The requester's
  capitalized "MYH9-Related Disease" was a display label, not a request for a second synonym.
- Sourcing a synonym to a bare GitHub issue URL is weak provenance (the issue is not an
  authoritative nomenclature source); gold used the curator ORCID, agents elsewhere used
  OMIM/Orphanet/PMID — any of which is preferable to the issue URL.
- Under-editing: missed the six RELATED→EXACT scope promotions like the whole cohort
  (defensible, not in the issue text, but caps recall).
- Net: the MATINS add and lowercase preservation are good, but the case-duplicate synonym is
  a genuine quality regression, placing this below #396/#258 and roughly on par with #567's
  rename problem (here a duplicate rather than a rename).
