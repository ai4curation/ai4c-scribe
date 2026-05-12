---
ontology: go-ontology
issue_number: 31961
pr_number: 32015
eval_repo_pr: 31
agent: std_claude_son45
model: claude-sonnet-4.5
runtime: claude
agent_config_tag: v9
case_type: obsoletion
difficulty: simple
f1: 0.8
precision: 0.889
recall: 0.727
jaccard: 0.667
outcome: partial_success
failure_modes:
  - over_editing
reviewed_by: gpt-5
reviewed_at: "2026-05-11"
---

<!-- Review this eval run following analysis/instructions/review-agent-eval.md

  Source issue: https://github.com/geneontology/go-ontology/issues/31961
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/32015
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/31
  Agent config: ai4curation/go-ontology-agent-config

  Quick reference:
    gh issue view 31961 --repo geneontology/go-ontology
    gh pr diff 32015 --repo geneontology/go-ontology
    gh pr diff 31 --repo ai4curation/eval-ont-agent-go
-->

## Summary

The agent correctly performed the core requested obsoletion of `GO:0008785 alkyl hydroperoxide reductase activity` and replaced it with `GO:0102039 NADH-dependent peroxiredoxin activity`. However, it also changed comments on `GO:0009321` and `GO:0070937`; the final human PR deliberately reverted those same comment edits after maintainer feedback. The metadiff `F1=0.8` is directionally fair: the agent captured the substantive obsoletion but over-edited beyond the accepted scope.


## Strengths

- Correctly renamed `GO:0008785` to `obsolete alkyl hydroperoxide reductase activity`.
- Correctly prefixed the `GO:0008785` definition with `OBSOLETE.` while preserving the original reaction and `GOC:curators` attribution.
- Removed the active `is_a: GO:0016668` parent from the obsolete term, which is the expected obsoletion pattern.
- Added the issue tracker provenance `https://github.com/geneontology/go-ontology/issues/31961`.
- Added `is_obsolete: true` and the correct direct replacement `replaced_by: GO:0102039`, matching the issue request and the human PR.
- The agent's obsolete-term comment captures the main curator rationale: `GO:0008785` represented an overly substrate-specific octane hydroperoxide activity and should be mapped to the broader `GO:0102039`.


## Issues

- The agent over-edited by updating the free-text comment on `GO:0009321 alkyl hydroperoxide reductase complex` from a see-also reference to `GO:0008785` to one pointing to `GO:0102039`. This is understandable cleanup, but it was outside the final accepted PR.
- The agent also removed a free-text comment from `GO:0070937 CRD-mediated mRNA stability complex` because it referenced `GO:0008785`. That stale reference looks suspicious, but it is unrelated to the requested `GO:0008785` obsoletion and was not accepted in the human solution.
- The human PR history confirms this was not merely an arbitrary gold-standard difference: a maintainer explicitly asked the PR author not to change comments in other terms, and those edits were reverted before merge.
- Minor style difference: the agent's obsoletion comment is less specific than the human PR's wording because it omits the explicit `EC 1.11.1.26` synonym rationale and the named replacement `GO:0102039 NADH-dependent peroxiredoxin activity`.
