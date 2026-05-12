---
ontology: go-ontology
issue_number: 31956
pr_number: 31960
eval_repo_pr: 184
agent: std_codex_g54
model: gpt-5.4
runtime: codex
agent_config_tag: v9
case_type: obsoletion
difficulty: simple
f1: 0.9
precision: 0.9
recall: 0.9
jaccard: 0.818
outcome: success
failure_modes: []
reviewed_by: gpt-5.5
reviewed_at: 2026-05-11
---

<!-- Review this eval run following analysis/instructions/review-agent-eval.md

  Source issue: https://github.com/geneontology/go-ontology/issues/31956
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/31960
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/184
  Agent config: ai4curation/go-ontology-agent-config

  Quick reference:
    gh issue view 31956 --repo geneontology/go-ontology
    gh pr diff 31960 --repo geneontology/go-ontology
    gh pr diff 184 --repo ai4curation/eval-ont-agent-go
-->

## Summary

The agent correctly implemented the requested direct-replacement obsoletion from geneontology/go-ontology#31956: `GO:0005870` actin capping protein of dynactin complex was made obsolete and pointed to `GO:0008290` F-actin capping protein complex. The metadiff score (`f1: 0.9`, `precision: 0.9`, `recall: 0.9`) slightly under-represents the practical quality of the result, because the only real mismatch with human PR #31960 is the exact wording of the obsoletion comment.


## Strengths

- Correctly changed `GO:0005870` from `actin capping protein of dynactin complex` to `obsolete actin capping protein of dynactin complex`.
- Preserved the original definition and provenance while prefixing the definition with `OBSOLETE.`, retaining `GOC:jl`, `PMID:18221362`, and `PMID:18544499`.
- Correctly removed both logical definition axioms from the obsolete term: the genus `intersection_of: GO:0008290 ! F-actin capping protein complex` and the `part_of GO:0005869 ! dynactin complex` differentia.
- Added the expected obsoletion metadata: `property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31956" xsd:anyURI`, `is_obsolete: true`, and `replaced_by: GO:0008290`.
- Chose the correct replacement term, matching the issue request that annotations can safely move to `GO:0008290` and the reported zero EXP annotations on `GO:0005870`.
- Kept the edit tightly scoped to the single target stanza in `src/ontology/go-edit.obo`, with no unrelated ontology changes.


## Issues

- No significant correctness, completeness, or scope issues. The agent's obsoletion comment differs from the human PR: it says the term is "an unused specialization that should be replaced by F-actin capping protein complex" rather than the accepted wording that it is redundant with `GO:0008290` and that annotations can be migrated. This is a stylistic mismatch, not a substantive modeling error.
- The PR report noted that full `make travis_build` was killed in the evaluation environment and that the agent relied on fallback `robot verify` and `robot reason` checks. That is a validation limitation, but it did not result in an incorrect diff for this simple obsoletion.
