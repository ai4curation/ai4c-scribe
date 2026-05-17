---
ontology: mondo
issue_number: 9854
pr_number: 10116
eval_repo_pr: 228
agent: std_opencode_gem4
model: gemma-4-31b
runtime: opencode
agent_config_tag: ai4curation/mondo-agent-config@v3
case_type: other
difficulty: medium
f1: 0.882
precision: 0.833
recall: 0.938
jaccard: 0.789
outcome: partial_success
failure_modes: [syntax_error, missed_requirement]
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

## Summary

A surprisingly strong attempt from a small (31B) model: it performed the full
subset migration and most of the source-qualifier cleanup, earning F1 0.882
(P 0.833 / R 0.938). However it introduced one concrete defect — an empty
`{}` source-annotation block on `xref: MedDRA:10050183` — and omitted the
issue-tracker (`IAO:0000233`) links the human added to both terms. F1 modestly
over-represents quality because the empty-brace serialization is a likely
ROBOT/ODK validation problem that line-level metadiff scores as a near-match.

## Strengths

- Full subset migration: removed the four `{source="Orphanet:2477"}` subsets
  (`ordo_disorder`, `ordo_malformation_syndrome`, `orphanet`, `orphanet_rare`)
  from MONDO:0016608 and re-added them verbatim to MONDO:0017089 — matches gold.
- Correctly stripped `Orphanet:2477` / `Orphanet:2477/e` from `ICD10CM:Q04.5`
  and `icd11.foundation:368780653` on MONDO:0016608, byte-identical to gold on
  those two lines.
- Removed `xref: Orphanet:2477 {source="MONDO:equivalentTo"}` from 0016608 and
  added it to 0017089 (the literal ask). Did not over-copy ICD/MedDRA onto the
  isolated term (better scope discipline than the sonnet-4.5 attempt).

## Issues

- Syntax/serialization defect: rewrote `xref: MedDRA:10050183 {source="Orphanet:2477", source="Orphanet:2477/e"}`
  to `xref: MedDRA:10050183 {}` — an empty trailing annotation block. Gold
  re-sourced this to `{source="MONDO:equivalentTo"}`. An empty `{}` is at best
  non-idiomatic OBO and likely to be flagged by `make NORM` / ODK QC; a bare
  `xref: MedDRA:10050183` (no braces) or the gold's explicit source would be
  correct. Flagged `syntax_error`.
- Missed requirement: did not add the
  `property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9854"`
  term-tracker link to either MONDO:0016608 or MONDO:0017089. The gold added it
  to both, and the project CLAUDE.md explicitly instructs linking back to the
  issue via `term_tracker_item`. This is the main recall-relevant omission.
- Did not carry `xref: icd11.foundation:368780653 {source="Orphanet:2477"}`
  onto MONDO:0017089 (same defensible gap as the kimi attempt — minor).
