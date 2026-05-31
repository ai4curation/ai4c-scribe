---
ontology: go-ontology
issue_number: 32005
pr_number: 32026
eval_repo_pr: 404
agent: std_copilot_son45
model: claude-sonnet-4.5
runtime: copilot
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

A second copilot/claude-sonnet-4.5 run (PR closed), substantively identical to #450: **no obsoletion of GO:0009095** was produced. The eval PR diff (blob `961e08a`) does not touch the GO:0009095 stanza — the entire 317-add / 320-delete diff is the **eval base-state contamination block** (unrelated edits from other issues), byte-identical across all 9 low-scoring attempts and predating the agent. Net of contamination, zero in-scope changes were made.

## Strengths

- None applicable. No correct obsoletion was produced for this attempt.

## Issues

- **No output**: the requested obsoletion was not performed; none of the required edits are present. Reproduces the #450 failure for the copilot/claude-sonnet-4.5 configuration, contrasting with the same model's successful obsoletions under the `claude` runtime (#491, #487) — consistent with a copilot runtime/harness interaction problem on this case.
- F1 0.017 / precision 0.19 are artifacts of accidental overlap between the contamination block and unrelated human edits, not agent work.
- Scored diff dominated by **base-state contamination** (eval data-quality issue; same block as the other 8 low-scoring attempts). A harness problem that does not excuse the missing obsoletion. Recommend treating as `no_output`; see Curation Note in METADATA.md.
