---
ontology: go-ontology
issue_number: 31670
pr_number: 31676
eval_repo_pr: 328
agent: std_claude_op47
model: claude-opus-4.7
runtime: claude
agent_config_tag: v9
case_type: new_term
difficulty: hard
f1: 0.0
precision: 0.0
recall: 0.0
jaccard: 0.0
outcome: partial_success
failure_modes:
- over_editing
- scope_creep
- missed_requirement
case_quality: poor
case_quality_reason: gold_pr_is_partial
companion_prs:
- 31677
reviewed_by: codex
reviewed_at: "2026-05-16"
---

<!-- Review this eval run following analysis/instructions/review-agent-eval.md

  Source issue: https://github.com/geneontology/go-ontology/issues/31670
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/31676
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/328
  Agent config: ai4curation/go-ontology-agent-config

  Quick reference:
    gh issue view 31670 --repo geneontology/go-ontology
    gh pr diff 31676 --repo geneontology/go-ontology
    gh pr diff 328 --repo ai4curation/eval-ont-agent-go
-->

## Summary

The source-level taxon-constraint reasoning is strong, but the submitted PR is not clean. The agent added the curator-style Eukaryota constraints for `GO:0000956` and `GO:0141065`, with useful source provenance. However, it also committed regenerated `only_in_taxon.ofn` and `go_taxon_constraints.owl`, producing massive generated-artifact churn. The F1 of 0 is therefore mostly an artifact of derived-file noise, but the PR would still need cleanup before review.

## Strengths

- Correctly chose the broad `only_in_taxon: NCBITaxon:2759` modeling for `GO:0000956`.
- Correctly included `GO:0141065` maternal mRNA clearance.
- Added provenance in the TSV source column pointing to issue #31670.
- Explained the parent-level modeling decision clearly.

## Issues

- Committed regenerated OFN/OWL taxon-constraint artifacts with large blank-node renumbering churn. The correct patch should have committed only the source TSV.
- Did not add the `GO:0000958` Eukaryota constraint.
- Did not reproduce the incidental `GO:0140494` migrasome cleanup.
- Did not address companion PR #31677's `GO:1990074` `never_in_taxon` addition.
