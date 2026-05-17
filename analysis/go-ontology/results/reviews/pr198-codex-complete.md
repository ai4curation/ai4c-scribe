---
ontology: go-ontology
issue_number: 31876
pr_number: 31953
eval_repo_pr: 198
agent: std_claude_hai45
model: claude-haiku-4.5
runtime: claude
agent_config_tag: v9
case_type: obsoletion
difficulty: simple
f1: 1.0
precision: 1.0
recall: 1.0
jaccard: 1.0
outcome: partial_success
failure_modes:
  - over_editing
reviewed_by: codex
reviewed_at: "2026-05-16"
---

<!-- Review this eval run following analysis/instructions/review-agent-eval.md

  Source issue: https://github.com/geneontology/go-ontology/issues/31876
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/31953
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/198
  Agent config: ai4curation/go-ontology-agent-config

  Quick reference:
    gh issue view 31876 --repo geneontology/go-ontology
    gh pr diff 31953 --repo geneontology/go-ontology
    gh pr diff 198 --repo ai4curation/eval-ont-agent-go
-->

## Summary

The agent correctly obsolete-marked `GO:0140057` (`vacuole-mitochondria membrane tethering`) for the reason requested in issue #31876 and made the same core ontology changes as the human PR: obsolete label, obsolete definition prefix, obsoletion comment, tracker item, removal of the asserted parent, and `is_obsolete: true`. However, unlike the human PR, the agent also removed the term's `created_by` and `creation_date` provenance metadata. The reported metadiff score is `f1=1.0`, but that overstates the actual quality because this extra metadata deletion is a real scope/provenance issue.


## Strengths

- Correctly targeted the requested term, `GO:0140057`, and did not edit unrelated GO terms.
- Added the standard obsolete naming pattern, changing the label to `obsolete vacuole-mitochondria membrane tethering`.
- Preserved the original definition text while prefixing it with `OBSOLETE.`, matching the human PR.
- Added the requested obsoletion rationale as a comment: the term was added in error.
- Removed the active asserted parent `is_a: GO:0140056 ! organelle localization by membrane tethering`, which is appropriate for an obsolete term.
- Added `property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31876" xsd:anyURI` and `is_obsolete: true`.
- Did not add an unwarranted `replaced_by` or `consider` target; the issue requested obsoletion because the term was added in error and did not identify a replacement.


## Issues

- The agent removed `created_by: pg` and `creation_date: 2017-06-27T10:31:12Z` from `GO:0140057`. The human PR retained these provenance fields, and deleting them is unnecessary for obsoletion and loses useful audit metadata.
- Because of that extra deletion, the agent's edit is slightly broader than the requested obsoletion even though the biological/ontological outcome is otherwise correct.
