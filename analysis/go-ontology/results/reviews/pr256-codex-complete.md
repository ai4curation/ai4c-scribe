---
ontology: go-ontology
issue_number: 31876
pr_number: 31953
eval_repo_pr: 256
agent: std_opencode_kimi
model: kimi-k2.6
runtime: opencode
agent_config_tag: v9
case_type: obsoletion
difficulty: simple
f1: 1.0
precision: 1.0
recall: 1.0
jaccard: 1.0
outcome: success
failure_modes: []
reviewed_by: gpt-5.5
reviewed_at: '2026-05-16'
---

<!-- Review this eval run following analysis/instructions/review-agent-eval.md

  Source issue: https://github.com/geneontology/go-ontology/issues/31876
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/31953
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/256
  Agent config: ai4curation/go-ontology-agent-config

  Quick reference:
    gh issue view 31876 --repo geneontology/go-ontology
    gh pr diff 31953 --repo geneontology/go-ontology
    gh pr diff 256 --repo ai4curation/eval-ont-agent-go
-->

## Summary

The agent correctly handled the obsoletion request for GO:0140057 `vacuole-mitochondria membrane tethering`, matching the human solution in all substantive ontology changes. The perfect metadiff score (F1 1.0, precision 1.0, recall 1.0) accurately reflects the quality here: the agent made the same narrowly scoped obsoletion edit with no meaningful omissions or extra ontology changes.


## Strengths

- Correctly identified the target term GO:0140057 and changed its label to `obsolete vacuole-mitochondria membrane tethering`.
- Preserved the original definition text and provenance (`PMID:27875684`) while adding the required `OBSOLETE.` prefix.
- Removed the active asserted parent `is_a: GO:0140056 ! organelle localization by membrane tethering`, which is appropriate for an obsolete GO term.
- Added the same obsoletion reason as the issue and human PR: `The reason for obsoletion is that this term was added in error.`
- Added the correct `term_tracker_item` pointing to `https://github.com/geneontology/go-ontology/issues/31876` and marked the term with `is_obsolete: true`.
- Stayed tightly scoped to `src/ontology/go-edit.obo` and did not alter neighboring terms such as GO:0140058.
- The agent's PR notes indicate it checked for internal GO references to GO:0140057, recognized the issue's note that the single PomBase annotation had already been removed, and ran `make travis_build` successfully.


## Issues

- No substantive issues. The only visible difference from the human PR is non-semantic stanza ordering: the agent placed `property_value` and `is_obsolete` before `created_by` / `creation_date`, while the human PR placed them after the creation metadata.
