---
ontology: go-ontology
issue_number: 31961
pr_number: 32015
eval_repo_pr: 46
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
reviewed_by: codex
reviewed_at: "2026-05-16"
---

<!-- Review this eval run following analysis/instructions/review-agent-eval.md

  Source issue: https://github.com/geneontology/go-ontology/issues/31961
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/32015
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/46
  Agent config: ai4curation/go-ontology-agent-config

  Quick reference:
    gh issue view 31961 --repo geneontology/go-ontology
    gh pr diff 32015 --repo geneontology/go-ontology
    gh pr diff 46 --repo ai4curation/eval-ont-agent-go
-->

## Summary

The agent correctly performed the requested obsoletion of `GO:0008785 alkyl hydroperoxide reductase activity` and added `replaced_by: GO:0102039 NADH-dependent peroxiredoxin activity`, matching the main substance of the human solution. The metadiff score (`f1: 0.8`, precision `0.889`, recall `0.727`) is a fair signal: the core edit is right, but the agent made extra comment edits outside the final accepted human PR. Those extras are plausible ontology hygiene, but maintainer feedback on the human PR explicitly asked not to change comments in other terms, so this should be treated as a partial success rather than a clean success.


## Strengths

- Correctly identified `GO:0008785` as the term to obsolete and `GO:0102039` as the appropriate replacement requested by issue #31961.
- Applied the standard obsoletion pattern to `GO:0008785`: prefixed the name with `obsolete`, prefixed the definition with `OBSOLETE.`, removed the active `is_a GO:0016668` parent, added `is_obsolete: true`, and added `replaced_by: GO:0102039`.
- Added the issue tracker property for `https://github.com/geneontology/go-ontology/issues/31961`, matching the human solution.
- Preserved the existing definition text and provenance on `GO:0008785` while making it obsolete.
- The agent appears to have searched for internal references to `GO:0008785`; that found real free-text references in `GO:0009321` and `GO:0070937`, even though editing them was ultimately outside the accepted scope.


## Issues

- Over-edited outside the requested term. The final human PR only changes `GO:0008785`, while the agent also changed the `GO:0009321 alkyl hydroperoxide reductase complex` comment and removed a comment from `GO:0070937 CRD-mediated mRNA stability complex`.
- The `GO:0009321` and `GO:0070937` comment edits are specifically disfavored by the accepted PR history: the human PR initially made similar comment cleanup, but a maintainer requested "please do not change the comments in other terms," and those edits were reverted.
- The agent's obsoletion comment for `GO:0008785` is shorter and says the term "is equivalent to GO:0102039"; the issue rationale is slightly more nuanced, describing `GO:0008785` as a substrate-specific version of the broader `GO:0102039`. This is not a blocking ontology error because the `replaced_by` target is correct, but the human comment captures the rationale more carefully.
