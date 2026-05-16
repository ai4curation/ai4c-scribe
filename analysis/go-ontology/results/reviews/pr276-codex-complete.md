---
ontology: go-ontology
issue_number: 31916
pr_number: 32024
eval_repo_pr: 276
agent: std_opencode_kimi
model: kimi-k2.6
runtime: opencode
agent_config_tag: v9
case_type: obsoletion
difficulty: medium
f1: 0.957
precision: 0.965
recall: 0.948
jaccard: 0.917
outcome: success
failure_modes:
- over_editing
reviewed_by: gpt-5.5
reviewed_at: 2026-05-16
---

<!-- Review this eval run following analysis/instructions/review-agent-eval.md

  Source issue: https://github.com/geneontology/go-ontology/issues/31916
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/32024
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/276
  Agent config: ai4curation/go-ontology-agent-config

  Quick reference:
    gh issue view 31916 --repo geneontology/go-ontology
    gh pr diff 32024 --repo geneontology/go-ontology
    gh pr diff 276 --repo ai4curation/eval-ont-agent-go
-->

## Summary

The agent successfully resolved the Entner-Doudoroff cleanup. It obsoleted all five variant terms with the correct replacement targets and updated the parent `GO:0061678` MetaCyc xrefs using the correct `source="skos:narrowMatch"` convention. The remaining issues are minor provenance over-edits on obsolete terms.

## Strengths

- Correctly obsoleted `GO:0009255`, `GO:0061679`, `GO:0061680`, and `GO:0061681` with `replaced_by: GO:0061678`.
- Correctly obsoleted `GO:0061688` with `replaced_by: GO:0006096`.
- Correctly removed active logical axioms and synonyms from the obsolete terms.
- Correctly replaced the parent MetaCyc grouping xref with four `skos:narrowMatch` variant pathway xrefs.

## Issues

- Removed historical `created_by` and `creation_date` metadata from several obsoleted terms; the human PR retained those.
- Dropped a pre-existing tracker item on `GO:0061680`.
- Added a tracker to active parent `GO:0061678`, which is harmless but extra relative to the human PR.
