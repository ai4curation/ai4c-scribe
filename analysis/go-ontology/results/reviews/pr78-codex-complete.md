---
ontology: go-ontology
issue_number: 31964
pr_number: 31982
eval_repo_pr: 78
agent: std_opencode_g55
model: gpt-5.5
runtime: opencode
agent_config_tag: v9
case_type: axiom_repair
difficulty: medium
f1: 1.0
precision: 1.0
recall: 1.0
jaccard: 1.0
outcome: success
failure_modes: []
reviewed_by: codex
reviewed_at: "2026-05-16"
---

<!-- Review this eval run following analysis/instructions/review-agent-eval.md

  Source issue: https://github.com/geneontology/go-ontology/issues/31964
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/31982
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/78
  Agent config: ai4curation/go-ontology-agent-config

  Quick reference:
    gh issue view 31964 --repo geneontology/go-ontology
    gh pr diff 31982 --repo geneontology/go-ontology
    gh pr diff 78 --repo ai4curation/eval-ont-agent-go
-->

## Summary

The agent successfully addressed geneontology/go-ontology#31964 with the same surgical `go-edit.obo` changes as the human PR. It removed the redundant `EC:1.4.3.22 {source="skos:broadMatch"}` from `GO:0052598 histamine oxidase activity`, reparented `GO:0004720 protein-lysine 6-oxidase activity` from `GO:0052597` to `GO:0016641`, and added the issue tracker metadata to both edited terms. The perfect metadiff score (`f1: 1.0`, `precision: 1.0`, `recall: 1.0`) accurately reflects the substantive quality of this run.


## Strengths

- Correctly removed the child-level broad EC mapping from `GO:0052598 histamine oxidase activity`, matching the issue's instruction that `EC:1.4.3.22` is a group-level diamine oxidase mapping and should remain only on the parent `GO:0052597 diamine oxidase activity`.
- Correctly preserved the rest of the `GO:0052598` stanza, including its parentage under `GO:0052597` and the exact reaction mapping `xref: RHEA:25625 {source="skos:exactMatch"}`.
- Correctly reparented `GO:0004720 protein-lysine 6-oxidase activity` from `GO:0052597 diamine oxidase activity` to `GO:0016641 oxidoreductase activity, acting on the CH-NH2 group of donors, oxygen as acceptor`, the EC:1.4.3.- class-level parent requested in the issue.
- Preserved the second asserted parent on `GO:0004720`, `GO:0140096 catalytic activity, acting on a protein`, avoiding an accidental loss of the protein-acting classification.
- Added `property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31964" xsd:anyURI` to both edited terms, matching the human PR's provenance pattern.
- Kept scope tight: `GO:0052597 diamine oxidase activity` and `GO:0050232 putrescine oxidase activity` were not otherwise modified.


## Issues

No issues found. The agent's diff matches the human PR exactly and implements all requested ontology edits without extra changes.
