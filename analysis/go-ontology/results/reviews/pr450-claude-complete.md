---
ontology: go-ontology
issue_number: 32005
pr_number: 32026
eval_repo_pr: 450
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

claude-sonnet-4.5 under the copilot runtime produced **no obsoletion of GO:0009095**. The eval PR diff (blob `961e08a`) does not touch the GO:0009095 stanza at all — no `obsolete` name, no `is_obsolete`, no `consider`. The entire 317-add / 320-delete diff is exactly the **eval base-state contamination block** (unrelated edits from other issues) that is byte-identical across all 9 low-scoring attempts on this case and predates the agent. Net of contamination, this run made zero in-scope changes.

## Strengths

- None applicable. No correct obsoletion was produced for this attempt.

## Issues

- **No output**: the requested obsoletion of GO:0009095 was not performed. None of the required edits are present in the diff. A genuine task failure for the copilot/claude-sonnet-4.5 configuration — notable because the same model under the `claude` runtime (#491, #487) did produce a correct obsoletion, suggesting a runtime/harness interaction problem for copilot here.
- F1 0.017 / precision 0.19 reflect only accidental overlap between the contamination block and unrelated human edits, not agent work.
- Scored diff dominated by **base-state contamination** (eval data-quality issue, same block as #291/#224/#223/#491/#487/#525/#404/#324). This is a harness problem, but it does not excuse the absence of any obsoletion edit. Recommend treating as `no_output`; see Curation Note in METADATA.md.
