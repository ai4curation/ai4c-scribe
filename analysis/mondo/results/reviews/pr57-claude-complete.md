---
ontology: mondo
issue_number: 9795
pr_number: 10110
eval_repo_pr: 57
agent: std_opencode_g55
model: gpt-5.5
runtime: opencode
agent_config_tag: v3
case_type: obsoletion
difficulty: medium
f1: 0.414
precision: 0.854
recall: 0.273
jaccard: 0.261
outcome: success
failure_modes: []
case_quality: poor
case_quality_reason: gold_pr_is_partial
companion_prs: [10107, 10108, 10109]
scoring_caveat: "Gold PR #10110 covers only the Usher 1J sub-step of a four-merge issue resolved across #10107/#10108/#10109/#10110. Recall floored for every attempt; F1 ~0.41 under-represents quality."
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

## Summary

Poor evaluation case (multi-PR partial gold). This run produces a diff byte-identical to attempt #72 (same blob `8a12406`, same gpt-5.5/opencode config) — it is a replication. All four OMIM merges from the issue are performed correctly with thorough survivor-metadata transfer. F1=0.414 reflects only the scored Usher sub-step #10110 and under-represents the actual, complete resolution.

## Strengths

- Identical substance to #72: all four merges with correct `replaced_by` targets, canonical minimal obsolete stanzas, full synonym/xref/subset/MalaCards transfer to survivors, and removal of `obsoletion_candidate` / `IAO:0006012` from survivors.
- PR body documents the merge rationale per OMIM record and explicitly justifies declining to transfer misleading historical parentage onto survivors — good methodology evidence.
- Validation reported: `robot convert`, `robot verify` merge QC, and `git diff --check` all clean.

## Issues

- Same single substantive divergence as #72: on the scored Usher portion it transfers Usher `is_a` parents onto the nonsyndromic survivor MONDO:0012273, which the human #10110 deliberately avoided. Defensible (OMIM-equivalence view) but the human's narrower classification is preferable for a term named "nonsyndromic".
- Did not reproduce the human's `MONDO:preferredExternal` source additions or the two NARROW deafness-synonym deletions on MONDO:0012273 — minor metadata deltas.
- Reproducibility note (not a quality issue): #57 and #72 are identical, so they should be treated as one data point, not two independent successes.
