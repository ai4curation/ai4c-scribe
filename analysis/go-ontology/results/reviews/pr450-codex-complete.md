---
ontology: go-ontology
issue_number: 32005
pr_number: 32026
eval_repo_pr: 450
agent: std_copilot_son45
model: claude-sonnet-4.5
runtime: copilot
agent_config_tag: v9
case_type: obsoletion
difficulty: medium
f1: 0.017
precision: 0.19
recall: 0.009
jaccard: 0.008
outcome: failure
failure_modes:
- under_editing
- missed_requirement
- over_editing
- scope_creep
reviewed_by: gpt-5.5
reviewed_at: '2026-05-16'
---

<!-- Review this eval run following analysis/instructions/review-agent-eval.md

  Source issue: https://github.com/geneontology/go-ontology/issues/32005
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/32026
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/450
  Agent config: ai4curation/go-ontology-agent-config

  Quick reference:
    gh issue view 32005 --repo geneontology/go-ontology
    gh pr diff 32026 --repo geneontology/go-ontology
    gh pr diff 450 --repo ai4curation/eval-ont-agent-go
-->

## Summary

The agent did not perform the requested obsoletion of `GO:0009095` aromatic amino acid biosynthetic process, prephenate pathway. Human PR #32026 changes only the `GO:0009095` stanza, converting it to an obsolete term with `consider` targets `GO:0006571` and `GO:0009094`. This attempt instead submitted a very large unrelated ontology diff touching many terms and support files, so the very low metadiff F1 is a fair warning that the PR is not a usable solution.


## Strengths

- Some edits in the submitted diff appear to correspond to real GO maintenance work from other tickets, such as signal-sequence receptor renaming, vesicle tethering relationship changes, and enzyme obsoletions.
- The patch format is an ordinary ontology diff rather than a malformed file or empty PR.
- No evidence suggests the agent intentionally altered the requested term incorrectly; the more serious problem is that it did not reach the requested term at all.


## Issues

- The agent never edits `GO:0009095`, the only term changed by the human PR and the explicit target of issue #32005. It does not add `is_obsolete: true`, an `OBSOLETE.` definition, `consider` tags, an obsoletion comment, or the current issue tracker link for `GO:0009095`.
- The submitted diff is dominated by unrelated changes, including signal-sequence term renames/reparenting, vesicle tethering relationship changes, obsoletions for other tickets, new term additions, and generated import or taxon-constraint changes.
- Because the target stanza is untouched, this is not merely a low-recall version of the human PR. It fails the central requirement while also creating a large review burden from unrelated edits.
- Merging this as a response to #32005 would leave `GO:0009095` active and would import many unrelated ontology changes that should be reviewed under their own issues.
