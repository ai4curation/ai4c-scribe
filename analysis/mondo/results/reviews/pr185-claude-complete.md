---
ontology: mondo
issue_number: 9795
pr_number: 10110
eval_repo_pr: 185
agent: std_claude_hai45
model: claude-haiku-4.5
runtime: claude
agent_config_tag: v3
case_type: obsoletion
difficulty: medium
f1: 0.392
precision: 0.488
recall: 0.328
jaccard: 0.244
outcome: partial_success
failure_modes: [wrong_pattern, missed_requirement]
case_quality: poor
case_quality_reason: gold_pr_is_partial
companion_prs: [10107, 10108, 10109]
scoring_caveat: "Gold PR #10110 covers only the Usher 1J sub-step of a four-merge issue resolved across #10107/#10108/#10109/#10110. Recall floored for every attempt; but this attempt's low precision reflects real pattern errors, not just the harness."
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

## Summary

Poor evaluation case (multi-PR partial gold). This run is byte-identical to attempt #296 (same blob `f26acad`, same haiku-4.5/claude config) — a replication. Same outcome: all four terms obsoleted with correct `replaced_by` targets, but the merge is incomplete because no metadata is transferred to the surviving terms and synonyms/xrefs are left on the obsolete stanzas. F1=0.392 partly reflects the harness; precision=0.488 reflects a genuine wrong-pattern defect.

## Strengths

- All four merge pairs correctly identified with `is_obsolete: true`, `replaced_by:`, `IAO:0000231 MONDO:TermsMerged`, issue link, and `obsolete ...` name prefix.
- Logical axioms and `obsoletion_candidate` / scheduled date removed from the obsoleted stanzas.

## Issues

- **Same wrong merge pattern as #296**: synonyms/xrefs retained on the obsolete stanzas, nothing transferred to MONDO:0007402 / MONDO:0044720 / MONDO:0010549 / MONDO:0012273. The merges therefore lose the external mappings the human PRs (#10107–#10110) explicitly moved onto the survivors.
- Over-broad rewrite of xref sources to `MONDO:equivalentObsolete` across DOID/MEDGEN/MESH/Orphanet/SCTID/UMLS.
- None of the human's MONDO:0012273 edits reproduced; no engagement with the syndromic-vs-nonsyndromic judgment.
- Reproducibility note (not a quality issue): #185 and #296 are identical and should count as one data point.
