---
ontology: go-ontology
issue_number: 31948
pr_number: 31994
eval_repo_pr: 654
agent: std_opencode_g54
model: gpt-5.4
runtime: opencode
agent_config_tag: v9
case_type: obsoletion
difficulty: medium
f1: 0.9
precision: 0.9
recall: 0.9
jaccard: 0.818
outcome: success
failure_modes: []
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-17
---

<!-- Review this eval run following analysis/instructions/review-agent-eval.md

  Source issue: https://github.com/geneontology/go-ontology/issues/31948
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/31994
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/654
  Agent config: ai4curation/go-ontology-agent-config

  Quick reference:
    gh issue view 31948 --repo geneontology/go-ontology
    gh pr diff 31994 --repo geneontology/go-ontology
    gh pr diff 654 --repo ai4curation/eval-ont-agent-go
-->

## Summary

The agent correctly obsoleted `GO:7770028 glycoprotein cargo receptor activity` with replacement `GO:0038024 cargo receptor activity`, exactly as the issue and curator (@raymond91125) requested. The diff is structurally identical to the human PR #31994: it removed the active `is_a: GO:0038024`, replaced the stale `term_tracker_item` (#31038 → #31948) with a single tracker, dropped the now-stale `created_by: dragon-ai-agent` line, and added the obsolete name/def prefixes, `is_obsolete: true`, and `replaced_by: GO:0038024`. F1 0.900 slightly under-represents quality — the only deviation from gold is free-text obsoletion-comment wording.

## Strengths

- Correct target (`GO:7770028`) and correct replacement (`GO:0038024`), matching the issue's explicit "Replace by" field and the curator instruction.
- Replaced the obsolete `term_tracker_item` #31038 with the current #31948 as a single value — matching the human exactly (the 0.842 attempts kept both).
- Correctly removed the active `is_a: GO:0038024` assertion before adding `replaced_by`, per the term-obsoletion workflow.
- Dropped the stale `created_by: dragon-ai-agent` line, matching the human's provenance cleanup.
- Documented methodology: ran `make travis_build` pre/post, checked `runoak -i amigo: associations GO:7770028` (no annotations, consistent with the issue), and confirmed no internal references needed rewiring.

## Issues

- The obsoletion `comment` is a condensed single sentence ("term was added in error, and cargo receptors should be organized by transport domain rather than substrate type") versus the human's fuller wording that also notes most vesicle cargo are glycoproteins and that substrates should be captured via `has_input`. Substantively equivalent rationale; this free-text wording difference is the sole cause of F1 < 1.0 and is normal metadiff under-representation, not a real defect.
