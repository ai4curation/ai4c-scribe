---
ontology: mondo
issue_number: 9795
pr_number: 10110
eval_repo_pr: 379
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

Poor evaluation case (multi-PR partial gold). This is the strongest-documented opus run: same committed blob `5706df7` (all four merges, full metadata transfer) but with the clearest, most accurate PR narrative of any attempt in the set. F1=0.402 reflects only the scored Usher sub-step #10110 and severely under-represents a complete, well-reasoned resolution.

## Strengths

- All four merges performed with correct `replaced_by` targets; obsolete stanzas reduced to canonical minimum; survivors cleaned of `obsoletion_candidate` / `IAO:0006012`.
- Accurate, OMIM-grounded justification table mapping each obsoletion to its triggering OMIM merge/move (OMIM:218050→123320, 608088→614575, 302900→302800, 614869→609439).
- Owltools-injected synonym evidence `[MONDO:XXXXXXX]` correctly repaired to cite the obsoleted OMIM ID (OMIM:218050/608088/302900/614869).
- Dropped a redundant transferred `is_a: MONDO:0003847` on MONDO:0010549 with correct reasoning (already a subclass of hereditary disease via CMT).
- **Best curator-facing judgment in the set**: explicitly flags the two genuinely contentious transfers — MONDO:0044720 inheriting HSAN parents and MONDO:0012273 inheriting Usher parents — and recommends a curator review them, precisely the syndromic-vs-nonsyndromic issue that is the stated crux of this "medium" case. This is exactly the human-in-the-loop behaviour we want.
- `robot convert` + six merge QC SPARQL queries clean; self-verify greps for `alt_id`, orphan synonym evidence, and stray references documented.

## Issues

- The Usher-parent transfer onto MONDO:0012273 is the one substantive divergence from gold #10110 (the human did not make nonsyndromic hearing loss a subclass of Usher syndrome). The agent does the transfer but explicitly flags it for curator reversal — the right behaviour given the merge skill's literal instructions, though a bolder agent could have made the narrower call itself.
- Did not reproduce the human's `MONDO:preferredExternal` source additions or the two NARROW deafness-synonym deletions on MONDO:0012273 — minor metadata-precision deltas.
- No correctness, syntax, or scope errors relative to the issue.
