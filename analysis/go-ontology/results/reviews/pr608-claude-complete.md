---
ontology: go-ontology
issue_number: 31948
pr_number: 31994
eval_repo_pr: 608
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
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/608
  Agent config: ai4curation/go-ontology-agent-config

  Quick reference:
    gh issue view 31948 --repo geneontology/go-ontology
    gh pr diff 31994 --repo geneontology/go-ontology
    gh pr diff 608 --repo ai4curation/eval-ont-agent-go
-->

## Summary

The agent correctly obsoleted `GO:7770028 glycoprotein cargo receptor activity` with replacement `GO:0038024 cargo receptor activity`. The agent diff blob (`dbcf4b8`) is byte-identical to attempt #654 (same model/runtime) and structurally identical to the human PR #31994: active `is_a: GO:0038024` removed, stale `term_tracker_item` #31038 replaced with #31948 (single value), stale `created_by: dragon-ai-agent` line dropped, and obsolete markers (`is_obsolete: true`, `replaced_by: GO:0038024`, obsolete name/def prefixes) added. F1 0.900 under-represents quality; the sole deviation is obsoletion-comment wording.

## Strengths

- Correct target term (`GO:7770028`) and correct replacement (`GO:0038024`) per the issue's explicit "Replace by" field.
- Replaced the obsolete tracker #31038 with the current #31948 as a single value — matching the human exactly (a discrimination the 0.842 attempts missed).
- Correctly removed the active `is_a: GO:0038024` before adding `replaced_by`, following the obsoletion workflow.
- Dropped the stale `created_by` line, matching the human's provenance cleanup — the cleanest reproduction of the gold (tied with #654).

## Issues

- Obsoletion `comment` is a condensed single sentence rather than the human's fuller rationale (which also explains that most vesicle cargo are glycoproteins and that substrates should be captured via `has_input`). Substantively equivalent; this free-text wording difference is the only reason F1 is below 1.0 and reflects normal metadiff under-representation, not a defect.
- The attempt file for #608 contains only the diff (no PR/issue comment block captured); methodology cannot be independently inspected, but the diff itself is identical to the well-documented #654 run.
