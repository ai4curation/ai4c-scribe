---
ontology: mondo
issue_number: 9854
pr_number: 10116
eval_repo_pr: 457
agent: claude_claude-sonnet-4.5
model: claude-sonnet-4.5
runtime: claude
agent_config_tag: ai4curation/mondo-agent-config@v3
case_type: other
difficulty: medium
f1: 0.895
precision: 0.944
recall: 0.850
jaccard: 0.810
outcome: success
failure_modes: [wrong_pattern]
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

## Summary

The agent performed the full provenance migration (subsets + source-qualifier
cleanup) like the gold PR, scoring F1 0.895 (P 0.944 / R 0.850). The high
precision is well-earned: most of its lines match gold byte-for-byte. The recall
gap stems from one genuine modelling error — instead of *deleting* the
Orphanet-sourced ICD/MedDRA xrefs from MONDO:0017089's perspective the way gold
did, it *copied* `ICD10CM:Q04.5`, `icd11.foundation:368780653` and
`MedDRA:10050183` (with their full `Orphanet:2477` provenance still attached)
onto the isolated term. F1 slightly under-represents quality; the core task is
correct but the over-copying re-introduces a provenance smell the curator
deliberately removed.

## Strengths

- Correct literal move plus subset migration: removed the four
  `{source="Orphanet:2477"}` subsets from MONDO:0016608 and added them verbatim
  to MONDO:0017089; moved `xref: Orphanet:2477 {source="MONDO:equivalentTo"}`
  between terms — all matching gold.
- Cleanly stripped `Orphanet:2477` / `Orphanet:2477/e` from `ICD10CM:Q04.5` and
  `icd11.foundation:368780653` on MONDO:0016608, leaving the ORCID and
  `MONDO:equivalentTo` sources — byte-identical to gold on the parent term.
- Re-sourced `xref: MedDRA:10050183` on MONDO:0016608 to
  `{source="MONDO:equivalentTo"}` — this exactly matches the human's 3rd
  commit (the one the curator was unsure about). Best MedDRA handling of any
  attempt.
- Added the `IAO:0000233 .../issues/9854` term-tracker link to both terms,
  matching gold.

## Issues

- Wrong pattern on the migration target: the agent added three full xref lines
  to MONDO:0017089 carrying stale Orphanet provenance —
  `xref: ICD10CM:Q04.5 {source="Orphanet:2477", source="MONDO:equivalentTo", source="Orphanet:2477/e"}`,
  `xref: icd11.foundation:368780653 {source="Orphanet:2477", source="MONDO:equivalentTo"}`,
  and `xref: MedDRA:10050183 {source="Orphanet:2477", source="Orphanet:2477/e"}`.
  Gold added only `xref: icd11.foundation:368780653 {source="Orphanet:2477"}`
  to the isolated term and did NOT add ICD10CM or MedDRA there at all. The
  agent essentially duplicated the parent's mappings onto the child, which is
  the over-migration failure mode — these ICD10CM/MedDRA codes map to the
  *broad* megalencephaly concept and the curator deliberately left them only
  (de-provenanced) on the parent.
- Net effect: the agent did slightly *more* than gold on the target term
  (lowering recall to 0.850 from the human's frame), and the extra xrefs are
  ontologically questionable, not merely stylistic. Still a strong, mostly
  correct outcome — `wrong_pattern` flagged for the target-term over-copy, not
  a task failure.
