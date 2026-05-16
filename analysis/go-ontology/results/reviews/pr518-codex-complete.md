---
ontology: go-ontology
issue_number: 31962
pr_number: 31970
eval_repo_pr: 518
agent: std_opencode_gem4
model: gemma-4-31b
runtime: opencode
agent_config_tag: v9
case_type: axiom_repair
difficulty: medium
f1: 0.842
precision: 0.8
recall: 0.889
jaccard: 0.727
outcome: partial_success
failure_modes:
- under_editing
- missed_requirement
- wrong_pattern
reviewed_by: gpt-5.5
reviewed_at: 2026-05-16
---

<!-- Review this eval run following analysis/instructions/review-agent-eval.md

  Source issue: https://github.com/geneontology/go-ontology/issues/31962
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/31970
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/518
  Agent config: ai4curation/go-ontology-agent-config

  Quick reference:
    gh issue view 31962 --repo geneontology/go-ontology
    gh pr diff 31970 --repo geneontology/go-ontology
    gh pr diff 518 --repo ai4curation/eval-ont-agent-go
-->

## Summary

The agent partially addressed issue #31962. It made most of the requested EC/RHEA mapping repairs and updated the vitamin D primary label, but it missed the old-label synonym, omitted all issue tracker properties, and added one EC xref without the required `skos:exactMatch` source qualifier. The result is useful but not a complete match to the human ontology repair.

## Strengths

- Correctly downgraded `GO:0004855` `EC:1.17.3.2` from `skos:exactMatch` to `skos:broadMatch`.
- Correctly renamed `GO:0030343` to `vitamin D 25-hydroxylase activity`.
- Correctly added `EC:1.1.1.358 {source="skos:exactMatch"}` to `GO:0036441`.
- Correctly changed the `GO:0070675` definition xref to `RHEA:68012`.
- Correctly added `EC:1.17.3.2 {source="skos:broadMatch"}` and `RHEA:68012 {source="skos:exactMatch"}` to `GO:0070675`.

## Issues

- Added `xref: EC:1.14.14.24` to `GO:0030343` without `{source="skos:exactMatch"}`. The human PR uses the explicit exact-match qualifier, which is important for these enzyme mapping repairs.
- Missed the `synonym: "vitamin D3 25-hydroxylase activity" EXACT []` preservation when renaming `GO:0030343`.
- Did not add the issue #31962 `term_tracker_item` property to any of the changed terms.
