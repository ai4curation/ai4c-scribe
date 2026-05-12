---
ontology: go-ontology
issue_number: 31882
pr_number: 32036
eval_repo_pr: 158
agent: std_opencode_g55
model: gpt-5.5
runtime: opencode
agent_config_tag: v9
case_type: obsoletion
difficulty: simple
f1: 1.0
precision: 1.0
recall: 1.0
jaccard: 1.0
outcome: success
failure_modes: []
reviewed_by: gpt-5.5
reviewed_at: 2026-05-11
---

<!-- Review this eval run following analysis/instructions/review-agent-eval.md

  Source issue: https://github.com/geneontology/go-ontology/issues/31882
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/32036
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/158
  Agent config: ai4curation/go-ontology-agent-config

  Quick reference:
    gh issue view 31882 --repo geneontology/go-ontology
    gh pr diff 32036 --repo geneontology/go-ontology
    gh pr diff 158 --repo ai4curation/eval-ont-agent-go
-->

## Summary

The agent successfully implemented the requested obsoletion in issue #31882: `GO:1905353` ciliary transition fiber assembly and `GO:0097711` ciliary basal body-plasma membrane docking were both obsoleted and marked `replaced_by: GO:1905349` ciliary transition zone assembly. It also removed the now-invalid `starts_with GO:0097711` relationship from `GO:0060271` cilium assembly. The metadiff F1 of 1.0 accurately reflects the outcome: the agent diff matches the accepted human PR exactly.


## Strengths

- Correctly identified both terms in the final issue decision: `GO:1905353` and `GO:0097711`.
- Applied the standard GO obsoletion pattern to both terms: changed the name to `obsolete ...`, prefixed the original definition with `OBSOLETE.`, removed active logical axioms and synonyms, added `is_obsolete: true`, and added `replaced_by: GO:1905349`.
- Preserved the original definition xrefs on both obsolete terms while adding `property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31882" xsd:anyURI`.
- Added term-specific obsoletion comments explaining why each term is redundant with `GO:1905349` ciliary transition zone assembly, including the PMID:27646273 rationale for `GO:0097711`.
- Correctly removed the remaining in-ontology reference from `GO:0060271` cilium assembly: `relationship: starts_with GO:0097711`, avoiding a relationship to an obsolete process term.
- Kept the scope narrow: only `src/ontology/go-edit.obo` was changed, and there were no unrelated ontology edits.


## Issues

- No substantive issues found. The agent's ontology edit is identical to the human PR #32036 and resolves the stated issue.
