---
ontology: go-ontology
issue_number: 32005
pr_number: 32026
eval_repo_pr: 324
agent: std_claude_op47
model: claude-opus-4.7
runtime: claude
agent_config_tag: v9
case_type: obsoletion
difficulty: medium
f1: 0.017
precision: 0.19
recall: 0.009
jaccard: 0.008
outcome: no_output
failure_modes:
  - no_changes
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
case_quality: poor
case_quality_reason: eval_base_state_contamination
---

## Summary

claude-opus-4.7/claude produced **no obsoletion of GO:0009095**. The eval PR diff (blob `961e08a`, PR open and labelled DO NOT MERGE) does not touch the GO:0009095 stanza at all — no `obsolete` name, no `is_obsolete`, no `consider`. The entire 317-add / 320-delete diff is exactly the **eval base-state contamination block** (unrelated edits to GO:0000268/0003400/0005048/0008785/0008873-5 etc. from other issues), byte-identical across all 9 low-scoring attempts on this case and present in the harness base before the agent ran. Net of contamination, zero in-scope changes were made. Note: the merged human PR #32026 was itself authored by `dragon-ai-agent` running claude-opus-4-7 via claude-code in production — so the same model family resolves this issue correctly in the production harness; this eval run did not.

## Strengths

- None applicable to the task in this eval run. No correct obsoletion edit and no substantive PR/issue write-up were produced for attempt #324.

## Issues

- **No output**: the requested obsoletion of GO:0009095 was not performed; none of the required edits (name/def prefix, axiom removal, `is_obsolete: true`, `consider` targets, tracker #32005) are present in the diff. A genuine task failure for this eval run.
- F1 0.017 / precision 0.19 reflect only incidental overlap between the contamination block and unrelated human edits — not work by this agent.
- The scored diff is dominated by **eval base-state contamination**, an eval-harness data-quality defect (same block in #291/#224/#223/#491/#487/#525/#450/#404), not behavior attributable to claude-opus-4.7. However, contamination does not explain the absence of any obsoletion edit — even on a clean base this run produced nothing in scope. Recommend treating as `no_output`; see the case-level Curation Note in METADATA.md.
