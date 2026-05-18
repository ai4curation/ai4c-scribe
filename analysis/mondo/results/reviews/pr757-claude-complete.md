---
ontology: mondo
issue_number: 9909
pr_number: 10208
eval_repo_pr: 757
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

Deterministic replay of the same gpt-5.4/opencode behavior as #704 (identical diff, blob
`945c0bb`): the only edits are repairing the empty-bracket citation on `synonym:
"MYH9-related disease" EXACT []` → `[Orphanet:182050]` and adding the `IAO:0000233`
term tracker (byte-identical to gold). `MATINS` was **not** added. Metadiff F1=0.211
(recall=0.667) under-represents the safety of the two edits but correctly reflects the
omission of the core requested synonym. Notably, this run's PR comment contains a factual
error that #704's did not surface.

## Strengths

- Correctly repaired the policy-violating empty `[]` on `synonym: "MYH9-related disease"
  EXACT []` using `Orphanet:182050`, chosen by analogy to the sibling `MYH9-related
  disorder`/`MYH9-related syndrome` synonyms — sound provenance reasoning.
- Added `property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9909"`
  term tracker, byte-identical to gold.
- Retained the historical synonyms per @MeeSiing's curator comment rather than executing the
  requester's literal removal ask — the correct curation judgment.
- Scope-disciplined: no capitalization-duplicates or unsourced synonyms (contrast #567/#727).
- Transparent about the environment limitation (Docker/ODK unavailable, `make NORM` not run).

## Issues

- Missed requirement: did **not** add `MATINS`, the only requester-preferred synonym actually
  missing from the term and the central substantive change the gold made.
- Factual error in the PR comment: claims `MATINS` was already present on the term ("Confirmed
  that the requested preferred exact synonyms were already present ... MATINS"). It was not —
  this is a verification failure that produced false confidence and explains the missed add.
- Under-editing: missed the six RELATED→EXACT scope promotions like the rest of the cohort
  (defensible, not in the issue text, but contributes to the recall ceiling).
- Source divergence vs gold on `MYH9-related disease` (Orphanet:182050 vs curator ORCID) —
  better practice than ORCID-as-source but a guaranteed metadiff miss.
- Net: weaker than #396/#258 (which made these same safe edits *and* added MATINS); the
  false "already present" claim makes the underlying reasoning worse than #704's silent miss.
