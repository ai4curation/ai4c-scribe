---
ontology: go-ontology
issue_number: 31601
pr_number: 32007
eval_repo_pr: 524
agent: std_opencode_gemma
model: gemma-4-31b
runtime: opencode
agent_config_tag: v9
case_type: synonym_update
difficulty: simple
f1: 0.0
precision: 0.0
recall: 0.0
jaccard: 0.0
outcome: failure
failure_modes:
- no_changes
- missed_requirement
case_quality: poor
case_quality_reason: base_contamination_GO_0102067
reviewed_by: claude-opus-4.7
reviewed_at: '2026-05-15'
---

## Summary

The agent made no useful change. Its diff contains only the `GO:0102067`
geranylgeranyl diphosphate reductase activity definition line, which is base/
scaffold contamination from unrelated source PR #32006 present in all 12 eval
PRs for this issue — there is no `GO:0140597` edit at all. The core ask of
issue #31601 (revise the protein carrier activity definition to the
parent-aligned wording) was not performed. F1=0.000 correctly reflects a
genuine failure here.

## Strengths

- None of substance. The agent did not produce the requested ontology edit.

## Issues

- Missed requirement / no changes: the issue (round 2, per @hattrill's reopen
  comment and @raymond91125's instruction) asks for `GO:0140597` to be revised
  to `"Directly binding to a protein and delivering it either to an acceptor
  molecule or to a specific location."`. The agent's branch leaves
  `GO:0140597` at the pre-#32007 wording — i.e. it did nothing.
- The only line in the diff (`GO:0102067`) is a base/scaffold contamination
  artifact (identical wording across every one of the 12 attempts, including
  other no-op runs), not an intentional agent edit; it cannot be credited or
  penalized as agent work, but it confirms the agent contributed zero useful
  change.
- No PR/issue narrative is available in the attempt record, so there is no
  evidence of research, term search, or validation; consistent with a failed
  run for this small open model.
