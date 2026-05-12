---
ontology: go-ontology
issue_number: 31964
pr_number: 31982
eval_repo_pr: 56
agent: std_codex_g55
model: gpt-5.5
runtime: codex
agent_config_tag: v9
case_type: axiom_repair
difficulty: medium
f1: 0.857
precision: 0.75
recall: 1.0
jaccard: 0.75
outcome: partial_success
failure_modes:
  - under_editing
  - missed_requirement
  - instruction_violation
reviewed_by: gpt-5.5
reviewed_at: 2026-05-11
---

<!-- Review this eval run following analysis/instructions/review-agent-eval.md

  Source issue: https://github.com/geneontology/go-ontology/issues/31964
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/31982
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/56
  Agent config: ai4curation/go-ontology-agent-config

  Quick reference:
    gh issue view 31964 --repo geneontology/go-ontology
    gh pr diff 31982 --repo geneontology/go-ontology
    gh pr diff 56 --repo ai4curation/eval-ont-agent-go
-->

## Summary

The agent solved the core ontology-editing request for issue `#31964`: it removed the redundant `EC:1.4.3.22 {source="skos:broadMatch"}` xref from `GO:0052598 histamine oxidase activity` and reparented `GO:0004720 protein-lysine 6-oxidase activity` from `GO:0052597 diamine oxidase activity` to `GO:0016641 oxidoreductase activity, acting on the CH-NH2 group of donors, oxygen as acceptor`. The metadiff score (`f1: 0.857`, `precision: 0.75`, `recall: 1.0`) is a fair signal that the agent matched the functional edits but missed metadata added by the human PR and required by the agent configuration.


## Strengths

- Correctly identified that `GO:0052598 histamine oxidase activity` should not duplicate the parent-level broad EC mapping to `EC:1.4.3.22`; the agent removed that broadMatch while preserving the exact reaction mapping `RHEA:25625`.
- Correctly left `GO:0052597 diamine oxidase activity` as the term carrying the broad `EC:1.4.3.22` mapping, matching the issue's instruction to keep the broadMatch on the parent.
- Correctly changed the asserted parent of `GO:0004720 protein-lysine 6-oxidase activity` to `GO:0016641`, avoiding the false assertion that protein-lysine 6-oxidase is a diamine oxidase activity.
- Preserved the second asserted parent of `GO:0004720`, `GO:0140096 catalytic activity, acting on a protein`, which is important because the enzyme acts on protein-bound lysine.
- Stayed tightly scoped to `src/ontology/go-edit.obo` and did not alter `GO:0050232 putrescine oxidase activity`, which the issue mentioned only as context.


## Issues

- The agent omitted the `property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31964" xsd:anyURI` metadata on both edited terms. The accepted PR added this tracker to `GO:0004720` and `GO:0052598`, and the GO agent configuration explicitly says modified terms should link back to the relevant GitHub issue using `term_tracker_item`.
- The agent's PR text says no metadata stamps were added because these were edits to existing terms. That is correct for `created_by` and `creation_date`, but it incorrectly treats `term_tracker_item` as unnecessary; the metadata guidance distinguishes tracker links from new-term creation stamps.
- No biological or syntactic error is apparent in the ontology edits themselves. The outcome is partial rather than full success because the core axiom and xref repairs are correct, but the metadata requirement was missed.
