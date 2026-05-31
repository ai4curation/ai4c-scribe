---
ontology: mondo
issue_number: 9795
pr_number: 10110
eval_repo_pr: 380
agent: std_claude_op47
model: claude-opus-4.7
runtime: claude
agent_config_tag: v3
case_type: obsoletion
difficulty: medium
f1: 0.402
precision: 0.854
recall: 0.263
jaccard: 0.252
outcome: success
failure_modes: []
case_quality: poor
case_quality_reason: gold_pr_is_partial
companion_prs: [10107, 10108, 10109]
scoring_caveat: "Gold PR #10110 covers only the Usher 1J sub-step of a four-merge issue resolved across #10107/#10108/#10109/#10110. Recall floored for every attempt; F1 ~0.40 under-represents quality."
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

## Summary

Poor evaluation case (multi-PR partial gold). The final committed diff (blob `5706df7`, shared by opus runs #376/#377/#379/#380) performs all four requested merges correctly with thorough survivor-metadata transfer. F1=0.402 reflects only the scored Usher sub-step #10110 and under-represents a complete resolution. Notable wrinkle: the PR narrative claims three of the four terms were "already obsoleted" in the base state and that only MONDO:0011961 was changed — this is a misread of the base ontology (the base has them as `obsoletion_candidate`, not obsoleted), but it did not corrupt the result because the committed diff still contains all four correct merges.

## Strengths

- All four merges present in the diff with correct `replaced_by` targets and canonical minimal obsolete stanzas matching the gold #10110 pattern.
- Comprehensive metadata transfer to survivors (synonyms, xrefs, subsets, parents, MalaCards, issue links), with `obsoletion_candidate` / `IAO:0006012` stripped from survivors and owltools-injected `[MONDO:XXXXXXX]` synonym evidence repaired to cite the obsoleted OMIM ID.
- Correctly identified MONDO:0044720 as the replacement for MONDO:0011961 by reasoning that OMIM:608088 merged into OMIM:614575 and MONDO:0044720 carries `xref: OMIM:614575`.
- `robot verify` merge QC and `robot convert` reported clean (NORM flagged as not runnable in-environment, transparently noted).

## Issues

- Inaccurate situational reasoning in the PR comment: it asserts 3/4 terms were "already obsoleted (likely in a prior PR for this same issue)". They were not — the base file has them as live `obsoletion_candidate` terms. The committed diff nonetheless contains the merge-transfer edits for all four, so the artifact is correct, but the explanation does not match what was actually done. This is a transparency/methodology concern, not an ontological error.
- On the scored Usher portion, transfers Usher `is_a` parents (MONDO:0010168, MONDO:0019501) onto the nonsyndromic survivor — the shared divergence from gold #10110, defensible but not the human's preferred narrower classification.
- Did not reproduce the human's `MONDO:preferredExternal` additions or the two NARROW deafness-synonym deletions on MONDO:0012273.
