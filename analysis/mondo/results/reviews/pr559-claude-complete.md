---
ontology: mondo
issue_number: 9854
pr_number: 10116
eval_repo_pr: 559
agent: std_codex_g55
model: gpt-5.5
runtime: codex
agent_config_tag: ai4curation/mondo-agent-config@v3
case_type: other
difficulty: medium
f1: 0.759
precision: 0.611
recall: 1.000
jaccard: 0.611
outcome: partial_success
failure_modes: [missed_requirement, under_editing]
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

## Summary

A clean but partial resolution: the agent did the literal xref move, the full
subset migration, and the issue-tracker links, but performed *none* of the
source-qualifier provenance cleanup on MONDO:0016608. F1 0.759 (P 0.611 /
R 1.000) is a fair representation — recall is perfect because everything it did
matches gold, but precision drops because it left several `Orphanet:2477`
provenance references behind that the curator deliberately removed. The work is
correct as far as it goes; it is incomplete, not wrong.

## Strengths

- Correct literal move: removed `xref: Orphanet:2477 {source="MONDO:equivalentTo"}`
  from MONDO:0016608 and added it to MONDO:0017089.
- Full subset migration: removed all four `{source="Orphanet:2477"}` subsets
  from 0016608 and re-added them verbatim to 0017089 — matches gold.
- Added the `IAO:0000233 .../issues/9854` term-tracker link to *both* terms,
  exactly as the human did and as the project instructions require.
- No spurious edits: everything the agent changed is also in the gold diff
  (recall 1.000), so precision loss is purely from omissions, not errors.

## Issues

- Missed the provenance cleanup on MONDO:0016608. The agent left intact:
  `xref: ICD10CM:Q04.5 {... source="Orphanet:2477" ... source="Orphanet:2477/e"}`,
  `xref: icd11.foundation:368780653 {source="Orphanet:2477", source="MONDO:equivalentTo"}`,
  and `xref: MedDRA:10050183 {source="Orphanet:2477", source="Orphanet:2477/e"}`.
  Gold stripped the Orphanet sources from the first two and re-sourced the
  MedDRA xref. Because `Orphanet:2477` is being reassigned from megalencephaly
  to isolated megalencephaly, leaving these stale Orphanet provenance pointers
  on the parent term is the chief substantive gap. `under_editing` /
  `missed_requirement`.
- Did not carry `xref: icd11.foundation:368780653 {source="Orphanet:2477"}`
  onto MONDO:0017089 (consistent with not having cleaned the parent — minor).
- Did not touch the `MedDRA:10050183` xref at all, so the line still claims
  Orphanet:2477 as its provenance for a term no longer mapped to Orphanet:2477.
