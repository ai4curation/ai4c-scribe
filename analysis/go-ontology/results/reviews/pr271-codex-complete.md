---
ontology: go-ontology
issue_number: 31964
pr_number: 31982
eval_repo_pr: 271
agent: std_opencode_kimi
model: kimi-k2.6
runtime: opencode
agent_config_tag: v9
case_type: axiom_repair
difficulty: medium
f1: 0.889
precision: 1.0
recall: 0.8
jaccard: 0.8
outcome: partial_success
failure_modes: [wrong_pattern, over_editing]
reviewed_by: gpt-5.5
reviewed_at: 2026-05-16
---

<!-- Review this eval run following analysis/instructions/review-agent-eval.md

  Source issue: https://github.com/geneontology/go-ontology/issues/31964
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/31982
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/271
  Agent config: ai4curation/go-ontology-agent-config

  Quick reference:
    gh issue view 31964 --repo geneontology/go-ontology
    gh pr diff 31982 --repo geneontology/go-ontology
    gh pr diff 271 --repo ai4curation/eval-ont-agent-go
-->

## Summary

The agent got both biological fixes right: it removed the redundant EC broadMatch from `GO:0052598` and reparented `GO:0004720` away from the diamine oxidase branch. The artifact is only a partial success because it replaced existing tracker provenance with #31964 instead of adding #31964 alongside the existing issue links.

## Strengths

- Correctly removed `xref: EC:1.4.3.22 {source="skos:broadMatch"}` from histamine oxidase activity.
- Correctly changed `GO:0004720` from `GO:0052597` to `GO:0016641`.
- Preserved the orthogonal protein catalytic activity parent and existing exact xrefs.
- The PR explanation shows the agent understood the EC scope issue.

## Issues

- Wrong metadata pattern on both edited terms: existing `term_tracker_item` values were overwritten rather than retained and supplemented.
- This deletes historical provenance for issue #30193, and on `GO:0052598` it leaves only #28199 plus the new #31964 link instead of preserving all prior trackers.
- The line score understates the severity because the core ontology changes are correct, but the provenance edit is a real data-loss defect.
