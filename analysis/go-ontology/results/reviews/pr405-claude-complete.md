---
ontology: go-ontology
issue_number: 31948
pr_number: 31994
eval_repo_pr: 405
agent: std_claude_hai45
model: claude-haiku-4.5
runtime: claude
agent_config_tag: v9
case_type: obsoletion
difficulty: medium
f1: 0.800
precision: 0.800
recall: 0.800
jaccard: 0.667
outcome: success
failure_modes: []
reviewed_by: claude-opus-4.7
reviewed_at: '2026-05-15'
---

## Summary

The claude-haiku-4.5/claude run correctly obsoleted GO:7770028 with `replaced_by: GO:0038024`, capturing every functionally significant element of human gold PR #31994. F1 = 0.800 is the lowest of the seven but under-represents the quality: the obsoletion is fully correct; the gap comes from two cosmetic deviations — removing `created_by` (which gold also did) combined with adding a `! cargo receptor activity` label suffix on the `replaced_by` line and a terse comment.

## Strengths

- Complete, correct obsoletion pattern: name `obsolete`-prefixed, definition `OBSOLETE.`-prefixed, `is_a: GO:0038024` removed, `is_obsolete: true` and `replaced_by: GO:0038024` added.
- **Replaced** the `term_tracker_item` in place (single #31948 line), matching the gold structure and avoiding the two-tracker precision drag seen in #542/#390/#270.
- Removed the trailing `created_by: dragon-ai-agent` line, matching the human's stanza reorganization (same as gold and gemma attempt #237).
- Clear, accurate rationale in the PR narrative: correctly identifies both the unnecessary-substrate-specificity problem and the organize-by-transport-domain principle, and confirms 0 annotations / no mappings / no subset / no references before obsoleting.
- Replacement target GO:0038024 matches the issue's explicit "Replace by" instruction.

## Issues

- Style deviation on `replaced_by`: the agent wrote `replaced_by: GO:0038024 ! cargo receptor activity` (with a trailing label comment), whereas gold used the bare `replaced_by: GO:0038024`. Both are valid OBO — the `! label` form is human-readable and common in `is_a` lines — but it differs from the gold token and contributes to the lower Jaccard (0.667).
- The persisted `comment:` is minimal ("The reason for obsoletion is that this term was added in error"), omitting the substantive ontological rationale (non-orthogonal substrate axis; organize by transport domain; substrate via `has_input`) that the issue states and gold records in full. The richer reasoning is present in the PR description but not in the term comment.
- Net: a correct, complete obsoletion. The lowest F1 of the cohort is driven entirely by formatting/comment-verbosity differences, not by any ontological error — F1 materially under-represents quality here.
