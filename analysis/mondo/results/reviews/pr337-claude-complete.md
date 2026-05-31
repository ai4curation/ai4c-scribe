---
ontology: mondo
issue_number: 9795
pr_number: 10110
eval_repo_pr: 337
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
failure_modes: [wrong_pattern, missed_requirement]
case_quality: poor
case_quality_reason: gold_pr_is_partial
companion_prs: [10107, 10108, 10109]
scoring_caveat: "Gold PR #10110 covers only the Usher 1J sub-step of a four-merge issue resolved across #10107/#10108/#10109/#10110. Recall floored for every attempt; this attempt's low precision also reflects a fabricated ORCID, invalid source qualifiers, and no metadata transfer."
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

## Summary

Poor evaluation case (multi-PR partial gold). This run shares the committed blob `3e2c892` with #347/#338, so the on-disk artifact is the same; however, the PR comment for this run states the obsoletion reason was set to `IAO:0000231 MONDO:TermsMerged` (correct), unlike the #347/#338 narratives that describe `OMO:0001000`. All four requested terms are obsoleted with correct `replaced_by` targets, but the merge pattern is still incomplete and carries provenance/qualifier defects. F1=0.352 reflects both the partial-gold harness and these issues.

## Strengths

- All four merge pairs correctly identified with `is_obsolete: true`, `replaced_by:`, `IAO:0000231 MONDO:TermsMerged` (per the PR narrative), issue link, and `obsolete ...` name prefix.
- Logical axioms and the `obsoletion_candidate` subset / scheduled-obsoletion date removed from obsoleted stanzas.
- PR body gives a clear per-term OMIM justification and lists the workflow steps (obo-checkout/checkin, robot convert).

## Issues

- **Fabricated provenance**: injects `property_value: http://purl.org/dc/terms/creator https://orcid.org/0009-0000-1074-3026` on every obsoleted term — an unsupported ORCID.
- **Invalid source qualifier**: uses `MONDO:obsoleteEquivalent` (correct MONDO convention is `MONDO:equivalentObsolete`) across the transferred xref sources.
- **Wrong/incomplete merge pattern**: synonyms and xrefs are left on the obsolete stanzas and nothing is transferred to the surviving terms, so the merges do not preserve the external mappings the human PRs moved onto MONDO:0007402/0044720/0010549/0012273.
- PR narrative also mentions prefixing definitions with "OBSOLETE." where definitions exist — for merged terms the def should be removed (as in gold #10110), not retained with a prefix.
- No engagement with the syndromic-vs-nonsyndromic judgment central to the case.
