---
ontology: go-ontology
issue_number: 31966
pr_number: 32003
eval_repo_pr: 502
agent: std_copilot_son45
model: claude-sonnet-4.5
runtime: copilot
agent_config_tag: v9
case_type: obsoletion
difficulty: medium
f1: 0.889
precision: 0.889
recall: 0.889
jaccard: 0.8
outcome: success
failure_modes: []
reviewed_by: gpt-5.5
reviewed_at: '2026-05-16'
---

<!-- Review this eval run following analysis/instructions/review-agent-eval.md

  Source issue: https://github.com/geneontology/go-ontology/issues/31966
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/32003
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/502
  Agent config: ai4curation/go-ontology-agent-config

  Quick reference:
    gh issue view 31966 --repo geneontology/go-ontology
    gh pr diff 32003 --repo geneontology/go-ontology
    gh pr diff 502 --repo ai4curation/eval-ont-agent-go
-->

## Summary

The agent correctly implemented the requested obsoletion of `GO:0043713` `(R)-2-hydroxyisocaproate dehydrogenase activity` and used `GO:0140175` `(2R)-2-hydroxyacid dehydrogenase (NAD+) activity` as the replacement. Its ontology diff matches the human PR in all functional changes: obsolete label, `OBSOLETE.` definition prefix, removal of the active `is_a: GO:0016616` parent, tracker metadata, `is_obsolete: true`, and `replaced_by: GO:0140175`. The metadiff F1 of 0.889 slightly under-rates the result because the only real difference is a shorter obsoletion comment.


## Strengths

- Selected the correct target term, `GO:0043713`, and the correct replacement term, `GO:0140175`, matching the issue and the merged human PR.
- Followed the GO obsoletion pattern for the term stanza: prefixed the name with `obsolete`, prefixed the definition with `OBSOLETE.`, removed the asserted `is_a: GO:0016616` classification, and added `is_obsolete: true`.
- Added `replaced_by: GO:0140175`, which is the key migration metadata for annotations to the obsolete specific enzyme activity.
- Added the expected tracker link, `property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31966" xsd:anyURI`.
- Kept the change tightly scoped to `GO:0043713` in `src/ontology/go-edit.obo`, with no unrelated term edits.


## Issues

- Minor: the obsoletion comment is less informative than the human PR's comment. The merged PR records the biochemical rationale that `(R)-2-hydroxyisocaproate dehydrogenase` is a synonym of `EC:1.1.1.345`, that this EC entry is an exact-match xref for `GO:0140175`, and that the specific `RHEA:10052` reaction is a narrowMatch instance of the broader replacement term. The agent's shorter comment is still correct, but it preserves less curator-facing evidence in the ontology.
