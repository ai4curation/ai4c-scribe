---
ontology: go-ontology
issue_number: 31961
pr_number: 32015
eval_repo_pr: 66
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
reviewed_by: gpt-5-codex
reviewed_at: 2026-05-11
---

<!-- Review this eval run following analysis/instructions/review-agent-eval.md

  Source issue: https://github.com/geneontology/go-ontology/issues/31961
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/32015
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/66
  Agent config: ai4curation/go-ontology-agent-config

  Quick reference:
    gh issue view 31961 --repo geneontology/go-ontology
    gh pr diff 32015 --repo geneontology/go-ontology
    gh pr diff 66 --repo ai4curation/eval-ont-agent-go
-->

## Summary

The agent correctly performed the core obsoletion requested in geneontology/go-ontology#31961: `GO:0008785 alkyl hydroperoxide reductase activity` was made obsolete and replaced by `GO:0102039 NADH-dependent peroxiredoxin activity`. The metadiff score (`f1: 0.8`, `precision: 0.889`, `recall: 0.727`) is directionally accurate: the central ontology edit matches the accepted solution, but the agent also made two extra free-text comment edits outside the final human PR. This is a partial success because the requested term was handled correctly, but the PR would need scope cleanup before it matched maintainer expectations.

## Strengths

- Correctly identified `GO:0008785` as the term to obsolete and `GO:0102039` as the requested replacement, matching the issue's statement that `GO:0008785` was an over-specific substrate-specific version of the EC `1.11.1.26`-aligned activity.
- Applied the standard obsoletion mechanics to `GO:0008785`: renamed it to `obsolete alkyl hydroperoxide reductase activity`, prefixed the definition with `OBSOLETE.`, removed the active `is_a GO:0016668` parent, added `is_obsolete: true`, and added `replaced_by: GO:0102039`.
- Preserved the existing `term_tracker_item` links for issues `28261` and `28340` and added the new tracker link for issue `31961`, matching the human PR's provenance handling.
- Added an obsoletion comment that captures the main rationale that `GO:0008785` is more specific than the specificity of known gene products and should be replaced by `GO:0102039`.
- The agent did useful term-search work by finding remaining free-text references to `GO:0008785` in `GO:0009321 alkyl hydroperoxide reductase complex` and `GO:0070937 CRD-mediated mRNA stability complex`; those are plausible cleanup candidates even though they did not belong in the accepted PR.

## Issues

- The agent over-edited outside the requested term. The final human PR only changes `GO:0008785`, while the agent also changed the `GO:0009321` comment to point to `GO:0102039` and removed the `GO:0008785` see-also comment from `GO:0070937`.
- The scope issue is not just a metadiff artifact: in the human PR discussion, Raymond explicitly asked not to change comments in other terms, and the accepted human diff reverted those same comment edits. The agent's `GO:0009321` and `GO:0070937` changes may be biologically understandable, but they should have been left for curator approval or a separate cleanup PR.
- The `GO:0008785` obsoletion comment is less precise than the accepted one. It says the term is more specific than known gene-product specificity and has been replaced by `GO:0102039`, but it omits the issue's fuller explanation that the old term represented an octane hydroperoxide-specific reaction and that "alkyl hydroperoxide reductase" maps via EC `1.11.1.26` to `GO:0102039`.
