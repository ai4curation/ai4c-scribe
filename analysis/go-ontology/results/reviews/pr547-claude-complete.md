---
ontology: go-ontology
issue_number: 31948
pr_number: 31994
eval_repo_pr: 547
agent: std_codex_g54
model: gpt-5.4
runtime: codex
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
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/547
  Agent config: ai4curation/go-ontology-agent-config

  Quick reference:
    gh issue view 31948 --repo geneontology/go-ontology
    gh pr diff 31994 --repo geneontology/go-ontology
    gh pr diff 547 --repo ai4curation/eval-ont-agent-go
-->

## Summary

The agent correctly obsoleted `GO:7770028 glycoprotein cargo receptor activity` with the requested replacement `GO:0038024 cargo receptor activity`. The obsoletion itself is complete and correct: active `is_a: GO:0038024` removed, obsolete name/def prefixes applied, `is_obsolete: true` and `replaced_by: GO:0038024` added, plus an appropriate rationale comment and the #31948 tracker. F1 0.842 (vs 0.900 for #654/#608) reflects two minor provenance-handling deviations from the human, not substantive errors.

## Strengths

- Correct target (`GO:7770028`) and correct replacement (`GO:0038024`), matching the issue's explicit "Replace by" field and the curator instruction.
- Correctly removed the active `is_a: GO:0038024` assertion before adding `replaced_by`, per the term-obsoletion workflow.
- Added `is_obsolete: true`, the obsolete name/def `OBSOLETE.` prefixes, the #31948 `term_tracker_item`, and a comment correctly identifying substrate-type as an unhelpful cargo-receptor classification axis.
- Used the `obo-checkout.pl`/`obo-checkin.pl` workflow and verified there were no other GO stanzas referencing `GO:7770028` and no direct annotations.

## Issues

- Retained the stale `term_tracker_item` #31038 (the original creation issue) *and* added #31948, leaving two trackers; the human replaced #31038 with #31948 (single value). Minor provenance over-retention that lowers precision.
- Retained the now-stale `created_by: dragon-ai-agent` line; the human removed it as part of the obsoletion cleanup. Defensible but not matching gold.
- Obsoletion `comment` is a condensed single sentence versus the human's fuller rationale (most vesicle cargo are glycoproteins; substrates captured via `has_input`). Substantively equivalent free-text difference.
- `make travis_build` could not complete locally (missing `amm`/`robot` binaries) so post-edit automated validation was not run; the agent did inspect the final diff. Environmental, not an agent fault.
