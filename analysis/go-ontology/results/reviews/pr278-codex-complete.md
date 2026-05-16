---
ontology: go-ontology
issue_number: 31945
pr_number: 32013
eval_repo_pr: 278
agent: std_opencode_kimi
model: kimi-k2.6
runtime: opencode
agent_config_tag: v9
case_type: reclassification
difficulty: medium
f1: 0.9
precision: 0.9
recall: 0.9
jaccard: 0.818
outcome: partial_success
failure_modes:
- over_editing
- missed_requirement
reviewed_by: gpt-5.5
reviewed_at: '2026-05-16'
---

<!-- Review this eval run following analysis/instructions/review-agent-eval.md

  Source issue: https://github.com/geneontology/go-ontology/issues/31945
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/32013
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/278
  Agent config: ai4curation/go-ontology-agent-config

  Quick reference:
    gh issue view 31945 --repo geneontology/go-ontology
    gh pr diff 32013 --repo geneontology/go-ontology
    gh pr diff 278 --repo ai4curation/eval-ont-agent-go
-->

## Summary

The agent implemented the visible rename and obsoletion work, including the inline label-comment updates, but it introduced metadata problems. The 0.900 metadiff score overstates quality slightly because the patch deletes GO:0003400 creation provenance and adds issue tracker metadata to active renamed terms that the human PR left alone.

## Strengths

- Correctly obsoleted GO:0003400 and used GO:0048208 as the replacement target.
- Correctly renamed GO:0006901 and GO:0048208 to `vesicle coat assembly` / `COPII vesicle coat assembly`.
- Updated incoming `is_a: GO:0006901` label comments for GO:0016183, GO:0048200, and GO:0048208.
- Preserved active-term definitions and logical axioms.

## Issues

- Metadata regression: it removed `created_by: dph` and `creation_date: 2009-12-17T08:38:14Z` from GO:0003400. Obsoletion should preserve original term provenance.
- Scope issue: it added `term_tracker_item` links for issue 31945 to active renamed terms GO:0006901 and GO:0048208, while the accepted PR only added tracker provenance to the obsoleted term.
- The obsoletion comment says GO:0003400 is equivalent to GO:0048208, which is less precise than the issue rationale that annotations were pathway participants rather than upstream regulators.
- The demoted `COPII vesicle coating` synonym loses the source attribution used in the accepted PR.
