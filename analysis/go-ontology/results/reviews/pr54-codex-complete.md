---
ontology: go-ontology
issue_number: 31961
pr_number: 32015
eval_repo_pr: 54
agent: std_codex_g55
model: gpt-5.5
runtime: codex
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
  - scope_creep
reviewed_by: gpt-5
reviewed_at: 2026-05-11
---

<!-- Review this eval run following analysis/instructions/review-agent-eval.md

  Source issue: https://github.com/geneontology/go-ontology/issues/31961
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/32015
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/54
  Agent config: ai4curation/go-ontology-agent-config

  Quick reference:
    gh issue view 31961 --repo geneontology/go-ontology
    gh pr diff 32015 --repo geneontology/go-ontology
    gh pr diff 54 --repo ai4curation/eval-ont-agent-go
-->

## Summary

The agent correctly performed the core requested obsoletion of `GO:0008785 alkyl hydroperoxide reductase activity` and marked it as replaced by `GO:0102039 NADH-dependent peroxiredoxin activity`. The metadiff score (`f1: 0.8`, precision `0.889`, recall `0.727`) is directionally fair: the central term edit is mostly the same as the human solution, but the agent also made extra comment edits outside the final accepted scope. This is a partial success because the extra edits mirror cleanup that was explicitly rejected during review of the human PR.


## Strengths

- Correctly identified the issue's requested obsolete term, `GO:0008785`, and the intended replacement, `GO:0102039`.
- Applied the standard GO obsoletion pattern to `GO:0008785`: changed the name to `obsolete alkyl hydroperoxide reductase activity`, prefixed the definition with `OBSOLETE.`, removed the active `is_a GO:0016668` parent, added `is_obsolete: true`, and added `replaced_by: GO:0102039`.
- Added the issue tracker metadata for `https://github.com/geneontology/go-ontology/issues/31961`, matching the human PR.
- Preserved the original definition text and `GOC:curators` provenance while converting the term to obsolete form.
- The obsoletion comment captures the main rationale from issue #31961: `GO:0008785` was too substrate-specific for known gene products and should be replaced by `GO:0102039`.
- Found the other free-text references to `GO:0008785` in `GO:0009321 alkyl hydroperoxide reductase complex` and `GO:0070937 CRD-mediated mRNA stability complex`, showing reasonable reference-search methodology even though changing those comments was not accepted.


## Issues

- The agent over-edited outside the accepted scope. The final human PR changes only the `GO:0008785` stanza, while the agent also changed the comment on `GO:0009321` and removed the comment on `GO:0070937`.
- The extra edits conflict with the human PR review history. The human PR initially made similar comment cleanup, but a maintainer explicitly requested not to change comments in other terms, and those edits were reverted before merge.
- The `GO:0009321` edit changes a free-text "see also" from `GO:0008785` to `GO:0102039`. That is defensible as stale-reference cleanup, but it was not part of the requested obsoletion and was specifically excluded from the accepted solution.
- The `GO:0070937` edit removes a clearly unrelated copied comment about `alkyl hydroperoxide reductase activity`; this is likely a real pre-existing issue, but it should have been left for a separate cleanup PR rather than bundled with the obsoletion.
- The obsoletion comment on `GO:0008785` is acceptable but less informative than the human version. It omits the issue's fuller rationale that the generic-sounding label actually represented an octane hydroperoxide reaction and that "alkyl hydroperoxide reductase" is listed as a synonym of EC:1.11.1.26.
