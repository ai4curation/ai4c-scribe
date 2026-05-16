---
ontology: mondo
issue_number: 9795
pr_number: 10110
eval_repo_pr: 377
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

Poor evaluation case (multi-PR partial gold). Same committed blob `5706df7` as the other opus runs — all four requested merges performed correctly with full survivor-metadata transfer. The PR write-up is terser than #379/#376 but the agent issue comment still documents the four pairs and notes the synonym-evidence repair. F1=0.402 reflects only the scored Usher sub-step and under-represents a complete resolution.

## Strengths

- All four merges with correct `replaced_by` targets; canonical minimal obsolete stanzas; survivors cleaned of `obsoletion_candidate` / scheduled-obsoletion date.
- Comprehensive metadata transfer (xrefs, synonyms, subsets, parents, MalaCards, issue links) with stale `[MONDO:XXXXXXX]` synonym evidence rewritten to cite the obsoleted OMIM ID.
- Reports all six targeted merge SPARQL QC checks passing (proxy-merge, misused-replaced-by, obsoletion-reason, deprecated-class-reference, xref-without-precision, duplicate-exact-synonym).

## Issues

- Thinner PR documentation than #379/#376: the body is a one-line header and the curator-review flag for the contentious Usher/HSAN parent transfers (present and valued in #379/#376) is absent here. The edits are identical, but the reduced reviewer guidance is a methodology/communication regression for a case whose difficulty is precisely that judgment call.
- Same single substantive divergence from gold #10110: Usher `is_a` parents transferred onto the nonsyndromic survivor MONDO:0012273.
- Did not reproduce the human's `MONDO:preferredExternal` additions or the two NARROW deafness-synonym deletions on MONDO:0012273.
