---
ontology: go-ontology
issue_number: 31916
pr_number: 32024
eval_repo_pr: 337
agent: std_claude_op47
model: claude-opus-4.7
runtime: claude
agent_config_tag: v9
case_type: obsoletion
difficulty: medium
f1: 0.94
precision: 0.965
recall: 0.917
jaccard: 0.887
outcome: success
failure_modes: []
reviewed_by: gpt-5.5
reviewed_at: 2026-05-16
---

<!-- Review this eval run following analysis/instructions/review-agent-eval.md

  Source issue: https://github.com/geneontology/go-ontology/issues/31916
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/32024
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/337
  Agent config: ai4curation/go-ontology-agent-config

  Quick reference:
    gh issue view 31916 --repo geneontology/go-ontology
    gh pr diff 32024 --repo geneontology/go-ontology
    gh pr diff 337 --repo ai4curation/eval-ont-agent-go
-->

## Summary

The agent successfully completed the Entner-Doudoroff pathway consolidation. It obsoleted all targeted variant terms, used the correct replacement targets, preserved historical metadata, and updated `GO:0061678` with the correct MetaCyc `skos:narrowMatch` xrefs. Differences from the human PR are comment wording and harmless extra traceability.

## Strengths

- Correctly obsoleted all five target terms.
- Correct replacement targets: four to `GO:0061678`, one to `GO:0006096`.
- Correctly removed active logical axioms, xrefs, and synonyms from obsolete terms.
- Correctly used `xref: MetaCyc:... {source="skos:narrowMatch"}`.
- Preserved existing creation metadata and prior tracker provenance.

## Issues

- No substantive issues. The agent added a tracker to active parent `GO:0061678` and used longer comments than the human PR, but those are not ontology defects.
