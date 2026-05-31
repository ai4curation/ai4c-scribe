---
ontology: go-ontology
issue_number: 32005
pr_number: 32026
eval_repo_pr: 525
agent: std_opencode_gem4
model: gemma-4-31b
runtime: opencode
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

This run produced **no obsoletion of GO:0009095 at all**. The eval PR diff (blob `961e08a`) does not touch the GO:0009095 stanza in any way — there is no `obsolete aromatic amino acid...` line, no `is_obsolete`, no `consider`. The entire 317-add / 320-delete diff consists solely of the **eval base-state contamination block** (unrelated edits to GO:0000268, GO:0003400, GO:0005048, GO:0008785/0008873-5, exocyst, etc., from other issues) that is byte-identical across all 9 low-scoring attempts and was present in the harness base before the agent ran. Net of contamination, gemma-4-31b made zero in-scope changes: a genuine no-output for the requested task.

## Strengths

- None applicable to the task. No correct obsoletion edit was produced and no PR/issue write-up with substantive rationale was generated for this attempt.

## Issues

- **No output**: the agent did not obsolete GO:0009095. None of the required edits (name prefix, `OBSOLETE.` def, axiom removal, `is_obsolete: true`, `consider` targets, tracker #32005) are present. This is a genuine task failure for gemma-4-31b.
- The non-zero F1 (0.017) and the precision of 0.19 are entirely an artifact of accidental partial overlap between the contamination block and unrelated human changes — not a measure of any work by this agent.
- The scored diff is dominated by **base-state contamination**, which is an eval-harness data-quality problem (same block in #291/#224/#223/#491/#487/#450/#404/#324), not behavior attributable to gemma-4-31b. The contamination, however, does not excuse the agent here: even with a clean base it produced no obsoletion. Recommend treating this attempt as `no_output`; see Curation Note in METADATA.md for the case-level contamination flag.
