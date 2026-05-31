---
ontology: go-ontology
issue_number: 31961
pr_number: 32015
eval_repo_pr: 50
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
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/50
  Agent config: ai4curation/go-ontology-agent-config

  Quick reference:
    gh issue view 31961 --repo geneontology/go-ontology
    gh pr diff 32015 --repo geneontology/go-ontology
    gh pr diff 50 --repo ai4curation/eval-ont-agent-go
-->

## Summary

The agent correctly performed the core requested obsoletion of `GO:0008785 alkyl hydroperoxide reductase activity` and pointed it to `GO:0102039 NADH-dependent peroxiredoxin activity`. The metadiff score (`f1: 0.762`, precision `0.889`, recall `0.667`) is directionally accurate: the main term edit matches the human solution, but the agent made several extra ontology edits outside the final accepted PR. Those extra edits are mostly defensible cleanup, but maintainer feedback on the human PR explicitly narrowed the accepted change to `GO:0008785` only.


## Strengths

- Correctly identified `GO:0008785` as the obsolete term and `GO:0102039` as the replacement requested by issue #31961.
- Applied the standard obsoletion pattern to `GO:0008785`: changed the label to `obsolete alkyl hydroperoxide reductase activity`, prefixed the definition with `OBSOLETE.`, removed the active `is_a GO:0016668` parent, added `is_obsolete: true`, and added `replaced_by: GO:0102039`.
- Added the issue tracker metadata for `https://github.com/geneontology/go-ontology/issues/31961` on `GO:0008785`, matching the human PR.
- Preserved the original definition text and `GOC:curators` provenance while making the term obsolete.
- The agent did search for other references to `GO:0008785`, finding the stale free-text mentions in `GO:0009321 alkyl hydroperoxide reductase complex` and `GO:0070937 CRD-mediated mRNA stability complex`.


## Issues

- The agent over-edited outside the accepted scope. The final human PR only changes `GO:0008785`, while the agent also changed comments on `GO:0009321` and `GO:0070937`.
- The comment edits to `GO:0009321` and `GO:0070937` are specifically contrary to the human PR history: the human PR initially made similar cleanup, but a maintainer requested "please do not change the comments in other terms," and those edits were reverted before merge.
- The agent also edited the active replacement term `GO:0102039` by adding the exact synonym `alkyl hydroperoxide reductase activity` and a `term_tracker_item` for issue #31961. The synonym is biologically plausible because the issue notes that alkyl hydroperoxide reductase is a synonym of EC:1.11.1.26, but this was not requested and was not part of the final human solution.
- The obsoletion comment on `GO:0008785` is acceptable but less complete than the human wording: it captures that the term is too specific and replaced by `GO:0102039`, but omits the issue's EC:1.11.1.26 synonym rationale and the generic-name/substrate-specificity nuance.
