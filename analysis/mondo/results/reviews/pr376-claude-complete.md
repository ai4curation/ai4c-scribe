---
ontology: mondo
issue_number: 9795
pr_number: 10110
eval_repo_pr: 376
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

Poor evaluation case (multi-PR partial gold). Same committed blob `5706df7` as the other opus runs: all four requested merges performed correctly with thorough metadata transfer, plus the most detailed curator-facing notes section of any attempt. F1=0.402 reflects only the scored Usher sub-step #10110 and severely under-represents a complete, carefully-reasoned resolution.

## Strengths

- All four merges with correct `replaced_by` targets; obsolete stanzas reduced to the canonical 6-line skeleton; survivors stripped of `obsoletion_candidate` subset and `IAO:0006012` scheduled date.
- Documents the exact procedure (`owltools --obsolete-replace` → `make NORM` → manual cleanup → `obo-checkin.pl` → QC) and lists all six merge QC queries passing with 0 violations.
- Repaired owltools synonym evidence to the appropriate source (OMIM IDs, and `[Orphanet:139564]` for the HSAN1B synonym on MONDO:0044720).
- **Exemplary "open questions for the reviewer" section**: flags (1) MONDO:0044720 inheriting HSAN parents, (2) MONDO:0012273 inheriting Usher parents with explicit framing of the syndromic-vs-nonsyndromic tension, and (3) that MONDO:0044720 now lacks a definition for the CANVAS phenotype. This directly engages the core difficulty of the case and gives the curator precisely the right follow-up checklist.

## Issues

- Same single substantive divergence from gold #10110: Usher `is_a` parents transferred onto MONDO:0012273 (the human deliberately did not). The agent does the literal merge-skill transfer but transparently flags it as a genuine conceptual tension for curator resolution — appropriate behaviour.
- Did not reproduce the human's `MONDO:preferredExternal` source additions or the two NARROW deafness-synonym deletions on MONDO:0012273.
- No correctness, syntax, or scope errors relative to the issue's actual ask.
