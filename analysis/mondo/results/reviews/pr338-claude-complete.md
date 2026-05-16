---
ontology: mondo
issue_number: 9795
pr_number: 10110
eval_repo_pr: 338
agent: std_copilot_son45
model: claude-sonnet-4.5
runtime: copilot
agent_config_tag: v3
case_type: obsoletion
difficulty: medium
f1: 0.352
precision: 0.463
recall: 0.284
jaccard: 0.213
outcome: partial_success
failure_modes: [wrong_pattern, missed_requirement, wrong_term]
case_quality: poor
case_quality_reason: gold_pr_is_partial
companion_prs: [10107, 10108, 10109]
scoring_caveat: "Gold PR #10110 covers only the Usher 1J sub-step of a four-merge issue resolved across #10107/#10108/#10109/#10110. Recall floored for every attempt; this attempt's low precision also reflects real obsoletion-reason and source-qualifier errors."
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

## Summary

Poor evaluation case (multi-PR partial gold). Byte-identical to attempt #347 (same blob `3e2c892`, same sonnet-4.5/copilot config) — a replication. Same outcome: all four terms obsoleted with correct `replaced_by` targets, but with the wrong obsoletion reason (`OMO:0001000` rather than `MONDO:TermsMerged`), a fabricated curator ORCID, the invalid `MONDO:obsoleteEquivalent` qualifier, and no metadata transfer to survivors. F1=0.352 reflects both the partial-gold harness and these genuine defects.

## Strengths

- All four merge pairs correctly identified with `is_obsolete: true`, `replaced_by:`, issue link, `obsolete ...` name prefix.
- Logical axioms and `obsoletion_candidate` / scheduled date removed from obsoleted stanzas.
- PR body documents the OMIM justification per term.

## Issues

- Same defects as #347: `IAO:0000231 OMO:0001000` instead of `MONDO:TermsMerged`; fabricated `dcterms:creator https://orcid.org/0009-0000-1074-3026`; invalid `MONDO:obsoleteEquivalent` source qualifier applied broadly; no metadata transferred to surviving terms (incomplete merge that loses external mappings).
- No engagement with the syndromic-vs-nonsyndromic judgment that defines the case difficulty.
- Reproducibility note (not a quality issue): #338 and #347 are identical and should count as one data point.
