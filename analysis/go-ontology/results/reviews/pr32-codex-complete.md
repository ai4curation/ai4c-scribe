---
ontology: go-ontology
issue_number: 31961
pr_number: 32015
eval_repo_pr: 32
agent: std_codex_g54
model: gpt-5.4
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
reviewed_by: gpt-5.5
reviewed_at: 2026-05-11
---

<!-- Review this eval run following analysis/instructions/review-agent-eval.md

  Source issue: https://github.com/geneontology/go-ontology/issues/31961
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/32015
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/32
  Agent config: ai4curation/go-ontology-agent-config

  Quick reference:
    gh issue view 31961 --repo geneontology/go-ontology
    gh pr diff 32015 --repo geneontology/go-ontology
    gh pr diff 32 --repo ai4curation/eval-ont-agent-go
-->

## Summary

The agent correctly handled the core request from geneontology/go-ontology#31961: `GO:0008785 alkyl hydroperoxide reductase activity` was obsoleted and replaced with `GO:0102039 NADH-dependent peroxiredoxin activity`. The metadiff `F1=0.8` is a fair signal of a mostly correct solution with extra scope: the central `GO:0008785` edit matches the accepted PR, but the agent also changed comments on two other terms that the final human PR deliberately left unchanged after maintainer feedback.

## Strengths

- Correctly targeted `GO:0008785` and applied the standard obsolete-term pattern: renamed it to `obsolete alkyl hydroperoxide reductase activity`, prefixed the definition with `OBSOLETE.`, removed the asserted `is_a GO:0016668` parent, added `is_obsolete: true`, and added `replaced_by: GO:0102039`.
- Chose the right replacement, `GO:0102039 NADH-dependent peroxiredoxin activity`, matching the issue's statement that `GO:0008785` was an overly substrate-specific version of the EC 1.11.1.26-aligned activity.
- Preserved the existing `term_tracker_item` provenance links for issues `28261` and `28340` while adding the new tracker link for issue `31961`.
- Added a reasonable obsoletion comment for `GO:0008785` that captures the main curator rationale: the old activity was more specific than the specificity of known gene products and should be replaced by the broader peroxiredoxin activity term.
- The extra edits show that the agent searched for remaining textual references to `GO:0008785`, finding references in `GO:0009321 alkyl hydroperoxide reductase complex` and `GO:0070937 CRD-mediated mRNA stability complex`.

## Issues

- The agent over-edited outside the final accepted scope. It changed the `GO:0009321` comment from a see-also reference to `GO:0008785` to a reference to `GO:0102039`; that cleanup is understandable, but the merged human PR reverted this class of comment edits after maintainer feedback.
- The `GO:0070937 CRD-mediated mRNA stability complex` edit is more problematic: the original `GO:0008785` see-also comment appears unrelated to an mRNA stability complex, but replacing it with `GO:0102039` still leaves a misleading peroxiredoxin-related comment on an unrelated cellular component. The accepted solution did not make this change.
- The agent's obsoletion comment is less specific than the human PR's comment because it omits the explicit "alkyl hydroperoxide reductase" synonym / `EC 1.11.1.26` rationale tying the issue text to `GO:0102039`.
