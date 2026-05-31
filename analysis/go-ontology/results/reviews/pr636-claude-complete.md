---
ontology: go-ontology
issue_number: 31948
pr_number: 31994
eval_repo_pr: 636
agent: std_opencode_g55
model: gpt-5.5
runtime: opencode
agent_config_tag: v9
case_type: obsoletion
difficulty: medium
f1: 0.842
precision: 0.8
recall: 0.889
jaccard: 0.727
outcome: success
failure_modes: []
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-17
---

<!-- Review this eval run following analysis/instructions/review-agent-eval.md

  Source issue: https://github.com/geneontology/go-ontology/issues/31948
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/31994
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/636
  Agent config: ai4curation/go-ontology-agent-config

  Quick reference:
    gh issue view 31948 --repo geneontology/go-ontology
    gh pr diff 31994 --repo geneontology/go-ontology
    gh pr diff 636 --repo ai4curation/eval-ont-agent-go
-->

## Summary

The agent correctly obsoleted `GO:7770028 glycoprotein cargo receptor activity` with the requested replacement `GO:0038024 cargo receptor activity`. The obsoletion is complete and correct: active `is_a: GO:0038024` removed, obsolete name/def `OBSOLETE.` prefixes applied, `is_obsolete: true` and `replaced_by: GO:0038024` added, with an accurate rationale comment and the #31948 tracker. F1 0.842 (blob `9226d70`, identical to #587) reflects provenance over-retention relative to the human, not a substantive error. This run is the best-documented of the 0.842 cohort, with full pre/post `travis_build` validation reported.

## Strengths

- Correct target (`GO:7770028`) and correct replacement (`GO:0038024`) per the issue's explicit "Replace by" field and the curator instruction.
- Correctly removed the active `is_a: GO:0038024` assertion before adding `replaced_by`, per the obsoletion workflow.
- Added `is_obsolete: true`, the obsolete name/def prefixes, the #31948 `term_tracker_item`, and a comment correctly identifying substrate-type as an unhelpful cargo-receptor classification axis.
- Strong documented methodology: `make -C src/ontology travis_build` passed both pre- and post-edit (all SPARQL rules 0 violations), confirmed `GO:0038024` exists as the appropriate broader replacement, checked internal references and `runoak` annotations (none), and confirmed no subset/mapping usage — consistent with the issue report.

## Issues

- Retained the stale `term_tracker_item` #31038 *and* added #31948 (two trackers); the human replaced #31038 with the single #31948. Minor provenance over-retention lowering precision.
- Retained the now-stale `created_by: dragon-ai-agent` line, which the human removed during obsoletion cleanup. Defensible but not matching gold.
- Obsoletion `comment` is a condensed single sentence versus the human's fuller rationale (most vesicle cargo are glycoproteins; substrates captured via `has_input`). Substantively equivalent free-text difference, accounting for the remaining gap below F1 1.0.
