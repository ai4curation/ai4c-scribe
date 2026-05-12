---
ontology: go-ontology
issue_number: 31876
pr_number: 31953
eval_repo_pr: 129
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
reviewed_by: gpt-5
reviewed_at: 2026-05-11
---

<!-- Review this eval run following analysis/instructions/review-agent-eval.md

  Source issue: https://github.com/geneontology/go-ontology/issues/31876
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/31953
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/129
  Agent config: ai4curation/go-ontology-agent-config

  Quick reference:
    gh issue view 31876 --repo geneontology/go-ontology
    gh pr diff 31953 --repo geneontology/go-ontology
    gh pr diff 129 --repo ai4curation/eval-ont-agent-go
-->

## Summary

The agent correctly handled the requested obsoletion of `GO:0140057` (vacuole-mitochondria membrane tethering), matching the human PR's substantive edit to `src/ontology/go-edit.obo`. The metadiff score of F1=1.0 is a fair reflection of the result: the only visible difference from the human PR is tag ordering within the obsolete term stanza, not ontology content.


## Strengths

- Applied the expected obsoletion pattern to `GO:0140057`: renamed the term to `obsolete vacuole-mitochondria membrane tethering`, prefixed the definition with `OBSOLETE.`, and preserved the original `PMID:27875684` definition xref.
- Removed the active hierarchy assertion `is_a: GO:0140056 ! organelle localization by membrane tethering`, so the obsolete biological process term no longer remains asserted under the membrane tethering branch.
- Added the correct obsoletion metadata: `comment: The reason for obsoletion is that this term was added in error.`, `property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31876" xsd:anyURI`, and `is_obsolete: true`.
- Correctly did not add `replaced_by` or `consider`, consistent with the issue/case context that this term was added in error and the human PR's no-replacement solution.
- Stayed tightly scoped to the requested single term and did not introduce unrelated ontology edits.


## Issues

- No substantive ontology-editing issues were found. The agent placed `property_value` and `is_obsolete` before `created_by` / `creation_date`, while the human PR placed them after the creation metadata, but this is a harmless ordering/style difference.
- Review caveat: direct `gh issue view 31876 --repo geneontology/go-ontology` failed in this environment with an API connection error, so issue context was checked against the local curated case metadata for PR 31953 in addition to the human and agent PR diffs.
