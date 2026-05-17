---
ontology: go-ontology
issue_number: 31966
pr_number: 32003
eval_repo_pr: 141
agent: std_opencode_g55
model: gpt-5.5
runtime: opencode
agent_config_tag: v9
case_type: obsoletion
difficulty: medium
f1: 0.889
precision: 0.889
recall: 0.889
jaccard: 0.8
outcome: success
failure_modes: []
reviewed_by: codex
reviewed_at: "2026-05-16"
---

<!-- Review this eval run following analysis/instructions/review-agent-eval.md

  Source issue: https://github.com/geneontology/go-ontology/issues/31966
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/32003
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/141
  Agent config: ai4curation/go-ontology-agent-config

  Quick reference:
    gh issue view 31966 --repo geneontology/go-ontology
    gh pr diff 32003 --repo geneontology/go-ontology
    gh pr diff 141 --repo ai4curation/eval-ont-agent-go
-->

## Summary

The agent correctly implemented the requested obsoletion of `GO:0043713` `(R)-2-hydroxyisocaproate dehydrogenase activity` and used `GO:0140175` `(2R)-2-hydroxyacid dehydrogenase (NAD+) activity` as the replacement. Its ontology edit matches the human PR in all functional changes: obsolete label and definition prefix, removal of the `is_a: GO:0016616` parent, `term_tracker_item`, `is_obsolete: true`, and `replaced_by: GO:0140175`. The metadiff F1 of 0.889 slightly under-represents the actual quality because the only substantive mismatch is that the agent used a shorter obsoletion comment.

## Strengths

- Selected the correct obsolete term, `GO:0043713`, and the correct replacement, `GO:0140175`, exactly as requested in issue `#31966`.
- Followed the GO obsoletion pattern: prefixed the name with `obsolete`, prefixed the definition with `OBSOLETE.`, removed the active `is_a: GO:0016616` assertion, and added `is_obsolete: true`.
- Added `replaced_by: GO:0140175`, which is the key annotation migration metadata for this enzyme activity consolidation.
- Added the correct tracker metadata, `property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31966" xsd:anyURI`.
- Kept the edit tightly scoped to the single affected stanza in `src/ontology/go-edit.obo`, with no unrelated ontology changes.

## Issues

- Minor: the obsoletion comment is less informative than the human PR's comment. The human version records the supporting details that `(R)-2-hydroxyisocaproate dehydrogenase` is a synonym of `EC:1.1.1.345`, that `GO:0140175` has `EC:1.1.1.345` as an exact-match xref, and that the specific `RHEA:10052` reaction is a narrowMatch instance of the broader `GO:0140175` reaction. The agent's shorter comment is still correct and sufficient for the obsoletion, but it preserves less curator-facing rationale in the ontology.
