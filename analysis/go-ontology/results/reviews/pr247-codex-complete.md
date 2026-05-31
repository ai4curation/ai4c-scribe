---
ontology: go-ontology
issue_number: 31945
pr_number: 32013
eval_repo_pr: 247
agent: std_opencode_gem4
model: gemma-4-31b
runtime: opencode
agent_config_tag: v9
case_type: reclassification
difficulty: medium
f1: 0.833
precision: 0.75
recall: 0.938
jaccard: 0.714
outcome: partial_success
failure_modes:
- under_editing
- missed_requirement
reviewed_by: codex
reviewed_at: "2026-05-16"
---

<!-- Review this eval run following analysis/instructions/review-agent-eval.md

  Source issue: https://github.com/geneontology/go-ontology/issues/31945
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/32013
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/247
  Agent config: ai4curation/go-ontology-agent-config

  Quick reference:
    gh issue view 31945 --repo geneontology/go-ontology
    gh pr diff 32013 --repo geneontology/go-ontology
    gh pr diff 247 --repo ai4curation/eval-ont-agent-go
-->

## Summary

The agent got the high-level targets right but did not preserve the old labels as synonyms after renaming GO:0006901 and GO:0048208. It also missed the inline label-comment cleanup for GO:0006901 children. The 0.833 metadiff score is fair: the obsoletion is broadly correct, but the rename is incomplete because search compatibility is lost.

## Strengths

- Correctly obsoleted GO:0003400 with the obsolete label/definition, removed regulation logical axioms, tracker provenance, `is_obsolete: true`, and `replaced_by: GO:0048208`.
- Correctly renamed GO:0006901 to `vesicle coat assembly`.
- Correctly renamed GO:0048208 to `COPII vesicle coat assembly`.
- Preserved creation metadata on the obsoleted term.

## Issues

- Missed requirement: after renaming GO:0006901, it deleted the old `vesicle coat assembly` BROAD synonym but did not add `vesicle coating` back as an EXACT synonym.
- Missed requirement: after renaming GO:0048208, it removed the old `COPII vesicle coat assembly` synonym but did not add `COPII vesicle coating` back as an EXACT synonym.
- It left `is_a: GO:0006901 ! vesicle coating` stale on GO:0048208 and did not update the accepted incoming label comments for GO:0016183 and GO:0048200.
- The obsoletion comment still refers to GO:0048208 by its old label, making the guidance less clear after the rename.
