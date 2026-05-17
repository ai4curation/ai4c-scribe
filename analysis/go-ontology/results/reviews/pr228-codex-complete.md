---
ontology: go-ontology
issue_number: 31961
pr_number: 32015
eval_repo_pr: 228
agent: std_opencode_kimi
model: kimi-k2.6
runtime: opencode
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
reviewed_by: codex
reviewed_at: "2026-05-16"
---

<!-- Review this eval run following analysis/instructions/review-agent-eval.md

  Source issue: https://github.com/geneontology/go-ontology/issues/31961
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/32015
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/228
  Agent config: ai4curation/go-ontology-agent-config

  Quick reference:
    gh issue view 31961 --repo geneontology/go-ontology
    gh pr diff 32015 --repo geneontology/go-ontology
    gh pr diff 228 --repo ai4curation/eval-ont-agent-go
-->

## Summary

The agent correctly performed the core obsoletion requested in geneontology/go-ontology#31961: `GO:0008785` alkyl hydroperoxide reductase activity was made obsolete and replaced by `GO:0102039` NADH-dependent peroxiredoxin activity. The metadiff F1 of 0.8 is a fair signal of a mostly correct solution with scope problems: the central term edit matches the accepted pattern, but the agent retained two extra comment edits that the human PR originally made and then reverted after maintainer feedback.


## Strengths

- Correctly targeted `GO:0008785` and applied the standard obsoletion mechanics: renamed it to `obsolete alkyl hydroperoxide reductase activity`, prefixed the definition with `OBSOLETE.`, removed the asserted `is_a GO:0016668` parent, added `is_obsolete: true`, and added `replaced_by: GO:0102039`.
- Chose the correct replacement, `GO:0102039` NADH-dependent peroxiredoxin activity, consistent with the issue's statement that `GO:0008785` was a substrate-specific version of the broader EC 1.11.1.26-aligned activity.
- Preserved the existing `term_tracker_item` values for issues `28261` and `28340` and added a new tracker link for issue `31961`, matching the human PR's provenance handling.
- Searched beyond the target stanza and found the two remaining textual references to `GO:0008785` in `GO:0009321` alkyl hydroperoxide reductase complex and `GO:0070937` CRD-mediated mRNA stability complex. Those observations were biologically plausible cleanup candidates, even though they did not belong in the final accepted PR.


## Issues

- The agent over-edited outside the accepted scope. It changed the `GO:0009321` comment to point to `GO:0102039` and removed the stale `GO:0008785` comment from `GO:0070937`; however, the human PR discussion shows that a maintainer explicitly requested not changing comments in other terms, and the merged human diff contains only the `GO:0008785` obsoletion.
- The obsoletion comment on `GO:0008785` is less precise than the human PR. The agent wrote that the term is equivalent to `GO:0102039`, while the issue and accepted PR explain the more careful rationale: despite its generic name, `GO:0008785` represented a substrate-specific octane hydroperoxide activity more specific than known gene product specificity, and "alkyl hydroperoxide reductase" maps through EC 1.11.1.26 to `GO:0102039`.
- The agent's PR/issue comment claimed that no references to the obsolete term remained in the ontology. That was true only because it edited free-text comments in other terms; it did not reflect the curator's preferred handling, which was to leave those comment references untouched in this obsoletion PR.
