---
ontology: go-ontology
issue_number: 31961
pr_number: 32015
eval_repo_pr: 51
agent: std_opencode_g54
model: gpt-5.4
runtime: opencode
agent_config_tag: v9
case_type: obsoletion
difficulty: simple
f1: 0.762
precision: 0.889
recall: 0.667
jaccard: 0.615
outcome: partial_success
failure_modes:
  - over_editing
  - scope_creep
reviewed_by: codex
reviewed_at: "2026-05-16"
---

<!-- Review this eval run following analysis/instructions/review-agent-eval.md

  Source issue: https://github.com/geneontology/go-ontology/issues/31961
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/32015
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/51
  Agent config: ai4curation/go-ontology-agent-config

  Quick reference:
    gh issue view 31961 --repo geneontology/go-ontology
    gh pr diff 32015 --repo geneontology/go-ontology
    gh pr diff 51 --repo ai4curation/eval-ont-agent-go
-->

## Summary

The agent correctly handled the central request: obsolete `GO:0008785 alkyl hydroperoxide reductase activity` and replace it with `GO:0102039 NADH-dependent peroxiredoxin activity`. The metadiff score (`f1: 0.762`, precision `0.889`, recall `0.667`) is directionally fair: most of the core obsoletion matches the human solution, but the agent also made extra edits outside the final accepted scope. The most important caveat is that the human PR originally tried similar cleanup around other comments, but maintainer feedback narrowed the final PR to `GO:0008785` only.


## Strengths

- Correctly identified `GO:0008785` as the obsolete molecular function term and `GO:0102039` as the replacement specified in issue #31961.
- Applied the standard GO obsoletion pattern to `GO:0008785`: changed the label to `obsolete alkyl hydroperoxide reductase activity`, prefixed the definition with `OBSOLETE.`, removed the active `is_a GO:0016668` parent, added `is_obsolete: true`, and added `replaced_by: GO:0102039`.
- Added the issue tracker metadata for `https://github.com/geneontology/go-ontology/issues/31961` on `GO:0008785`, matching the human PR.
- Preserved the original definition text and `GOC:curators` provenance while converting the term to obsolete form.
- Found the free-text internal references to `GO:0008785` in `GO:0009321 alkyl hydroperoxide reductase complex` and `GO:0070937 CRD-mediated mRNA stability complex`, showing reasonable search methodology even though changing them was not accepted in the final human PR.


## Issues

- The agent over-edited outside the accepted scope. The final human PR changes only `GO:0008785`, while the agent also changed the comment on `GO:0009321`, removed a comment from `GO:0070937`, and edited the active replacement term `GO:0102039`.
- The comment edits to `GO:0009321` and `GO:0070937` conflict with the human PR history: the human PR initially made similar cleanup, but a maintainer explicitly requested not to change comments in other terms, and those edits were reverted before merge.
- The agent added `synonym: "alkyl hydroperoxide reductase activity" EXACT []` and a new `term_tracker_item` for issue #31961 to `GO:0102039`. The synonym is biologically plausible given the issue's EC:1.11.1.26 rationale and the existing `alkylhydroperoxide reductase activity` synonym, but it was not requested and was not part of the accepted human solution.
- The obsoletion comment on `GO:0008785` is acceptable but less informative than the human version. It says the term is too specific and replaced by `GO:0102039`, but it omits the issue's fuller rationale that the generic-sounding label actually represented a substrate-specific octane hydroperoxide reaction and that Expasy lists "alkyl hydroperoxide reductase" as a synonym of EC:1.11.1.26.
