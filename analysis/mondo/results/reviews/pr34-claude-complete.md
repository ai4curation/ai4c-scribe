---
ontology: mondo
issue_number: 9795
pr_number: 10110
eval_repo_pr: 34
agent: std_codex_g55
model: gpt-5.5
runtime: codex
agent_config_tag: v3
case_type: obsoletion
difficulty: medium
f1: 0.412
precision: 0.854
recall: 0.271
jaccard: 0.259
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

Poor evaluation case (multi-PR partial gold). gpt-5.5 via codex performed all four requested merges correctly with thorough metadata transfer; the diff is substantively the same as the gpt-5.5/opencode runs plus one extra carried-forward relationship. F1=0.412 reflects only the scored Usher sub-step and under-represents a complete resolution.

## Strengths

- All four merges done with correct `replaced_by` targets matching the issue's suggestions.
- Canonical minimal obsolete stanzas; full synonym/xref/subset/MalaCards/issue-link transfer to survivors; `obsoletion_candidate` and `IAO:0006012` correctly stripped from survivors.
- Used `owltools --obsolete-replace` then `make NORM` then manual cleanup — the documented MONDO merge workflow — and ran `robot convert` + six merge QC queries with 0 violations.
- PR body explicitly reasons about NOT transferring conflicting historical subclass axioms or the obsolete-specific definitions onto survivors — sound editorial judgment for the case's central difficulty.

## Issues

- On the scored Usher portion, in addition to the Usher `is_a` parents (the shared divergence from gold), this run also carried forward `relationship: has_characteristic HP:0000007 ... ! Autosomal recessive inheritance` onto MONDO:0012273 — the human #10110 did not. This is defensible (it is a true property of the merged concept) but is extra relative to gold and slightly increases the diff surface vs the opencode runs.
- Did not reproduce the human's `MONDO:preferredExternal` source additions or the two NARROW deafness-synonym deletions on MONDO:0012273.
- No correctness/syntax/scope errors against the issue; the dominant "issue" is the partial-gold harness.
