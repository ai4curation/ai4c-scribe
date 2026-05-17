---
ontology: go-ontology
issue_number: 25870
pr_number: 32008
eval_repo_pr: 550
agent: std_codex_g54
model: gpt-5.4
runtime: codex
agent_config_tag: v9
case_type: obsoletion
difficulty: medium
f1: 0.667
precision: 0.519
recall: 0.933
jaccard: 0.5
outcome: partial_success
failure_modes:
  - under_editing
  - missed_requirement
reviewed_by: codex
reviewed_at: "2026-05-16"
---

<!-- Review this eval run following analysis/instructions/review-agent-eval.md

  Source issue: https://github.com/geneontology/go-ontology/issues/25870
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/32008
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/550
  Agent config: ai4curation/go-ontology-agent-config

  Quick reference:
    gh issue view 25870 --repo geneontology/go-ontology
    gh pr diff 32008 --repo geneontology/go-ontology
    gh pr diff 550 --repo ai4curation/eval-ont-agent-go
-->

## Summary

The agent correctly handled the main `go-edit.obo` work: it obsoleted `GO:0018581`, used `replaced_by: GO:0047074`, renamed `GO:0047074` to `hydroxyquinol 1,2-dioxygenase activity`, and preserved the old `GO:0047074` label as an EXACT synonym. This is only a partial success because the human PR also removed the participant axioms for the obsolete term from `go-catalytic-activities-participants.owl`, and the agent missed that second-file cleanup entirely.

## Strengths

- Correctly obsoleted the sub-reaction term `GO:0018581`.
- Correct replacement target and correct survivor-term rename.
- Removed active xrefs and parentage from the obsolete stanza.
- Added the expected old-label EXACT synonym to `GO:0047074`.

## Issues

- Missed the import cleanup in `src/ontology/imports/go-catalytic-activities-participants.owl`. Leaving participant restrictions for an obsolete catalytic activity would preserve stale axioms outside the edit file.
- The obsoletion comment is much shorter than the human comment and does not explain the two-step reaction/non-enzymatic second-step rationale, though the replacement target is still correct.
