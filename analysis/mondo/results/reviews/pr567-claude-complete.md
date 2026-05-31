---
ontology: mondo
issue_number: 9909
pr_number: 10208
eval_repo_pr: 567
agent: std_codex_g54
model: gpt-5.4
runtime: codex
agent_config_tag: v3
case_type: synonym_update
difficulty: simple
f1: 0.2
precision: 0.125
recall: 0.5
jaccard: 0.111
outcome: partial_success
failure_modes: [missed_requirement, wrong_pattern, over_editing]
case_quality: poor
case_quality_reason: gold_uses_curator_orcid_source_and_expansive_reinterpretation
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-17
---

## Summary

The agent located MONDO:0015912, added the genuinely-missing `MATINS` synonym (sourced
`OMIM:155100`), added the `IAO:0000233` term tracker (byte-identical to gold), and **replaced**
the empty-bracket `synonym: "MYH9-related disease" EXACT []` with a capitalization-variant
`synonym: "MYH9-Related Disease" EXACT [OMIM:155100]`. Adding MATINS makes this substantively
stronger than the no-MATINS opencode runs (#704/#757), but the case-changed rename is a wrong
pattern: the gold kept the lowercase `MYH9-related disease` and only fixed its source. Metadiff
F1=0.200 under-represents the MATINS work but correctly penalizes the synonym rename.

## Strengths

- Added `synonym: "MATINS" EXACT ABBREVIATION [OMIM:155100]` — the single synonym from the
  requester's preferred list that was actually missing, and the core substantive change the
  gold made. Source `OMIM:155100` is defensible (the OMIM entry whose title yields the acronym).
- Added `property_value: IAO:0000233 ".../issues/9909"` term tracker, byte-identical to gold.
- Correctly retained the historical/legacy syndrome synonyms, citing the issue-thread curation
  decision — aligned with @MeeSiing's "we will keep the other synonyms" comment.
- Strong, transparent methodology: documented `obo-grep.pl` term location, `robot convert`
  syntax check, and `make NORM` normalization in the PR comment.

## Issues

- Wrong pattern: replaced `synonym: "MYH9-related disease" EXACT []` with the case-changed
  `synonym: "MYH9-Related Disease" EXACT [OMIM:155100]`. The gold instead **kept** the lowercase
  string and only repaired its source bracket. This both (a) loses the existing lowercase
  synonym surface form and (b) introduces a new capitalization variant — net-different from
  the curator's intent (the requester used the capitalized form only as a display label).
- Over-editing (mild): the capitalization swap is an unrequested change to an existing synonym
  string rather than a minimal provenance repair.
- Under-editing: missed the six RELATED→EXACT scope promotions like the whole cohort
  (defensible, not in the issue text, but caps recall at 0.5).
- Source divergence vs gold on MATINS / MYH9-related disease (OMIM vs curator ORCID) —
  better practice than ORCID-as-source but a guaranteed metadiff miss on those lines.
- Net: substantively better than #704/#757 (added MATINS) but worse than #396/#258, which
  added MATINS *and* preserved the lowercase synonym while repairing only its source.
