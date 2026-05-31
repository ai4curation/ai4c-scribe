---
ontology: go-ontology
issue_number: 31961
pr_number: 32015
eval_repo_pr: 103
agent: std_opencode_g55
model: gpt-5.5
runtime: opencode
agent_config_tag: v9
case_type: obsoletion
difficulty: simple
f1: 0.696
precision: 0.889
recall: 0.571
jaccard: 0.533
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
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/103
  Agent config: ai4curation/go-ontology-agent-config

  Quick reference:
    gh issue view 31961 --repo geneontology/go-ontology
    gh pr diff 32015 --repo geneontology/go-ontology
    gh pr diff 103 --repo ai4curation/eval-ont-agent-go
-->

## Summary

The agent correctly performed the core obsoletion requested in geneontology/go-ontology#31961: `GO:0008785 alkyl hydroperoxide reductase activity` was made obsolete and replaced by `GO:0102039 NADH-dependent peroxiredoxin activity`. The metadiff score (`f1: 0.696`, `precision: 0.889`, `recall: 0.571`) reflects that the agent matched the central edit but made several extra changes outside the accepted final PR. This is a partial success: the ontology target and obsoletion mechanics are right, but the PR would need scope reduction before acceptance.


## Strengths

- Correctly identified `GO:0102039 NADH-dependent peroxiredoxin activity` as the replacement for `GO:0008785`, matching the issue's explicit instruction.
- Applied the standard obsoletion mechanics to `GO:0008785`: changed the label to `obsolete alkyl hydroperoxide reductase activity`, prefixed the definition with `OBSOLETE.`, removed the asserted `is_a GO:0016668` parent, added `is_obsolete: true`, added `replaced_by: GO:0102039`, and added a `term_tracker_item` for issue `31961`.
- Added an obsoletion comment that captures the key biological rationale: `GO:0008785` represented a substrate-specific activity more specific than the specificity of known gene products and should be replaced by the broader NADH-dependent peroxiredoxin activity.
- Did useful term-search work by finding remaining textual/logical references to `GO:0008785`, including the `GO:0009321 alkyl hydroperoxide reductase complex` see-also comment and the unrelated stale `GO:0070937 CRD-mediated mRNA stability complex` comment.


## Issues

- The agent over-edited neighboring terms. It changed the `GO:0009321` comment from pointing to `GO:0008785` to pointing to `GO:0102039`, and removed a stale `GO:0008785` comment from `GO:0070937`. The accepted PR initially made similar comment edits, but Raymond explicitly asked that comments in other terms not be changed, and the merged human PR reverted them.
- The agent also changed `comments.txt` and `ld.txt`, including an `ld.txt` capability reference from `capable_of GO:0008785` to `capable_of GO:0102039`. That cleanup may be biologically plausible, but it was not part of the accepted solution and should have been left for curator review or a separate cleanup PR.
- The agent modified the replacement term `GO:0102039` by adding the exact synonym `"alkyl hydroperoxide reductase activity"` and another `term_tracker_item` for issue `31961`. The synonym is defensible for searchability because the issue notes the EC synonym, but it was not requested and was not in the final human PR.
- No syntax or wrong-term problems were evident. The weakness is scope discipline rather than failure to understand the requested replacement.
