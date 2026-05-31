---
ontology: go-ontology
issue_number: 31961
pr_number: 32015
eval_repo_pr: 84
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
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/84
  Agent config: ai4curation/go-ontology-agent-config

  Quick reference:
    gh issue view 31961 --repo geneontology/go-ontology
    gh pr diff 32015 --repo geneontology/go-ontology
    gh pr diff 84 --repo ai4curation/eval-ont-agent-go
-->

## Summary

The agent correctly performed the core requested obsoletion from geneontology/go-ontology#31961: `GO:0008785 alkyl hydroperoxide reductase activity` was made obsolete and replaced with `GO:0102039 NADH-dependent peroxiredoxin activity`. The metadiff score (`f1: 0.696`, `precision: 0.889`, `recall: 0.571`) is directionally fair: the central edit matches the human solution, but the agent made several extra edits outside the final accepted PR. This is a partial success because the ontology target and replacement were right, but the PR would have needed scope cleanup before acceptance.


## Strengths

- Correctly identified `GO:0008785` as the term to obsolete and `GO:0102039` as the `replaced_by` target requested by the issue.
- Applied the main GO obsoletion mechanics to `GO:0008785`: changed the name to `obsolete alkyl hydroperoxide reductase activity`, prefixed the definition with `OBSOLETE.`, removed the active `is_a GO:0016668` parent, added `is_obsolete: true`, and added `replaced_by: GO:0102039`.
- Preserved the original `GO:0008785` reaction definition and `GOC:curators` attribution while converting it to an obsolete definition.
- Added a `term_tracker_item` for `https://github.com/geneontology/go-ontology/issues/31961` on the obsoleted term, matching the accepted human PR.
- The obsoletion comment captures the main biological rationale: `GO:0008785` represented an overly substrate-specific version of NADH-dependent peroxiredoxin activity, more specific than the known gene product specificity.
- The agent appears to have searched for remaining references to `GO:0008785`, finding the free-text references on `GO:0009321` and `GO:0070937` and the logical-definition-style reference in `ld.txt`.


## Issues

- The agent over-edited outside the accepted scope. The merged human PR changes only `GO:0008785`, while the agent also changed `comments.txt`, `GO:0009321 alkyl hydroperoxide reductase complex`, `GO:0070937 CRD-mediated mRNA stability complex`, `GO:0102039`, and `ld.txt`.
- The `GO:0009321` comment update from `GO:0008785` to `GO:0102039` is biologically plausible, but it was explicitly rejected during review of the human PR: Raymond asked not to change comments in other terms, and the final human PR reverted those comment edits.
- Removing the `GO:0070937` comment that referenced `GO:0008785` is also plausible cleanup because the CRD-mediated mRNA stability complex is unrelated to alkyl hydroperoxide reductase activity, but it was not requested by the issue and was not part of the accepted solution.
- The agent modified the replacement term `GO:0102039` by adding the exact synonym `"alkyl hydroperoxide reductase activity"` and a `term_tracker_item` for issue `31961`. The synonym is defensible given the issue's EC 1.11.1.26 rationale, but it is still extra curation on a non-target term.
- The `ld.txt` change from `intersection_of: capable_of GO:0008785` to `intersection_of: capable_of GO:0102039` is a substantive logical-definition change for the related complex pattern. That may be a reasonable follow-up cleanup, but it goes beyond the simple obsoletion task and the final human PR.
