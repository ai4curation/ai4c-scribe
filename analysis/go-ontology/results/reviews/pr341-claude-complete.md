---
ontology: go-ontology
issue_number: 31948
pr_number: 31994
eval_repo_pr: 341
agent: std_claude_op47
model: claude-opus-4.7
runtime: claude
agent_config_tag: v9
case_type: obsoletion
difficulty: medium
f1: 0.900
precision: 0.900
recall: 0.900
jaccard: 0.818
outcome: success
failure_modes: []
reviewed_by: claude-opus-4.7
reviewed_at: '2026-05-15'
---

## Summary

The claude-opus-4.7/claude run correctly obsoleted GO:7770028 with `replaced_by: GO:0038024`, reproducing every functionally significant element of human gold PR #31994. F1 = 0.900 slightly under-represents quality: the lone deviation is retention of the trailing `created_by: dragon-ai-agent` line that gold dropped during stanza reordering — cosmetic, with no ontological effect.

## Strengths

- Complete, correct obsoletion: name `obsolete`-prefixed, definition `OBSOLETE.`-prefixed, `is_a: GO:0038024` removed, `is_obsolete: true` and `replaced_by: GO:0038024` added. Exactly the gold transformation.
- Correctly **replaced** (rather than appended) the `term_tracker_item`, pointing it at #31948 and leaving a single tracker line — the structure that matches gold and yields higher precision than the two-tracker attempts (#542/#390/#270).
- The `comment:` is the richest of all seven attempts: it states the term was added in error, explains the non-orthogonal substrate axis, points to organizing by transport domain with `has_input`, and even suggests concrete alternatives ("GO:0038024 or a more specific child such as COPII receptor activity"). This is more actionable than the gold comment while remaining faithful to the issue.
- Excellent scope discipline and self-awareness: the issue comment explicitly distinguishes the ontology edit from the downstream curator checklist (annotation review ticket, obsoletion announcement, go-friends notification) and correctly states those are out of scope for the edit — matching how the human workflow actually partitions the work.
- Verified no internal references, no taxon constraints, no subset membership, and (per issue) no experimental annotations before obsoleting.

## Issues

- Same minor style deviation as the other top-tier attempts: kept `created_by: dragon-ai-agent` where gold removed it. Sole cause of the 0.1 F1 gap; no ontological significance and arguably the more conservative choice (provenance retention).
- No other issues. This is the strongest attempt of the seven on rationale quality and scope reasoning.
