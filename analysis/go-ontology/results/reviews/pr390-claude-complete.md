---
ontology: go-ontology
issue_number: 31948
pr_number: 31994
eval_repo_pr: 390
agent: std_copilot_son45
model: claude-sonnet-4.5
runtime: copilot
agent_config_tag: v9
case_type: obsoletion
difficulty: medium
f1: 0.842
precision: 0.800
recall: 0.889
jaccard: 0.727
outcome: success
failure_modes:
  - over_editing
reviewed_by: claude-opus-4.7
reviewed_at: '2026-05-15'
---

## Summary

The claude-sonnet-4.5/copilot run correctly obsoleted GO:7770028 with `replaced_by: GO:0038024`. The obsoletion is fully correct and the rationale comment is strong; F1 = 0.842 is depressed only because the agent kept the #31038 `term_tracker_item` and added #31948 (two tracker lines) and slightly repositioned `created_by`, rather than performing gold's single in-place tracker replacement.

## Strengths

- Correct, complete obsoletion pattern: name `obsolete`-prefixed, definition `OBSOLETE.`-prefixed, `is_a: GO:0038024` removed, `is_obsolete: true` and `replaced_by: GO:0038024` added — semantically identical to gold.
- The `comment:` is substantive and faithful to the issue: notes the term was added in error, that most vesicle cargo are glycoproteins (so the substrate axis is non-orthogonal), and that terms should be organized by transport domain rather than substrate type. Comparable in quality to the gold comment.
- The issue comment summarizing the obsoletion is accurate and well-reasoned.

## Issues

- **Over-editing / scope (precision −):** preserved `term_tracker_item ".../issues/31038"` and appended a second tracker for #31948, where gold replaced the line in place. This extra line is the primary precision drag (0.800). Defensible as fuller lifecycle provenance but divergent from the gold convention.
- Minor stanza churn: the diff also moves the `created_by: dragon-ai-agent` line and inserts `is_obsolete`/`replaced_by` after it rather than before, producing a slightly different ordering than both gold and the higher-scoring sibling attempt #462 (same model, `claude` runtime). The reordering is cosmetic and OBO-order-insensitive, but contributes to the lower Jaccard (0.727).
- Net: a correct obsoletion; the gap vs the top tier is entirely tracker-handling and line-ordering style, not ontological substance.
