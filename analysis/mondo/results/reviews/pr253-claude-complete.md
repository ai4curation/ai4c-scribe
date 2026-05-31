---
ontology: mondo
issue_number: 9795
pr_number: 10110
eval_repo_pr: 253
agent: std_opencode_kimi
model: kimi-k2.6
runtime: opencode
agent_config_tag: v3
case_type: obsoletion
difficulty: medium
f1: 0.398
precision: 0.854
recall: 0.259
jaccard: 0.248
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

Poor evaluation case (multi-PR partial gold). kimi-k2.6 via opencode performed all four requested merges correctly with the most detailed per-term transfer documentation in the set. F1=0.398 reflects only the scored Usher sub-step #10110 and under-represents a complete resolution; precision=0.854 confirms the edits are on-target.

## Strengths

- All four merges with correct `replaced_by` targets; canonical minimal obsolete stanzas; survivors cleaned of `obsoletion_candidate` / `IAO:0006012`.
- Per-merge PR documentation enumerates exactly which synonyms/xrefs/subsets/parents/relationships were transferred to each survivor — strong methodology transparency.
- Repaired owltools synonym evidence (`[MONDO:0011961]`→`[OMIM:608088]`, etc.) and applied the documented merge-skill rule for definitions (transfer the obsoleted def to MONDO:0044720 because the survivor had none; keep MONDO:0012273's existing def).
- Flagged the dual-parentage issue on MONDO:0012273 (Usher parents alongside hearing-loss parent) to @kanems for curator review — good engagement with the case's central judgment.
- All six merge QC queries reported 0 violations; `robot convert` clean.

## Issues

- On the scored Usher portion, transfers Usher `is_a` parents and the `has_characteristic HP:0000007` relationship onto MONDO:0012273 — the shared divergence from gold #10110 (defensible but not the human's narrower choice). Also carried the HSAN1B-specific definition onto MONDO:0044720 by literal application of the merge-skill rule; arguably the CANVAS survivor should get a fresh definition rather than the obsoleted HSAN1B one (the agent flags adjacent concerns but not this specific one).
- Did not reproduce the human's `MONDO:preferredExternal` source additions or the two NARROW deafness-synonym deletions on MONDO:0012273.
- No correctness, syntax, or scope errors relative to the issue.
