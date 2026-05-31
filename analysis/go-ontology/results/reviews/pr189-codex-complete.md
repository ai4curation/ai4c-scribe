---
ontology: go-ontology
issue_number: 31966
pr_number: 32003
eval_repo_pr: 189
agent: std_codex_g54
model: gpt-5.4
runtime: codex
agent_config_tag: v9
case_type: obsoletion
difficulty: medium
f1: 1.0
precision: 1.0
recall: 1.0
jaccard: 1.0
outcome: success
failure_modes: []
reviewed_by: codex
reviewed_at: "2026-05-16"
---

<!-- Review this eval run following analysis/instructions/review-agent-eval.md

  Source issue: https://github.com/geneontology/go-ontology/issues/31966
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/32003
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/189
  Agent config: ai4curation/go-ontology-agent-config

  Quick reference:
    gh issue view 31966 --repo geneontology/go-ontology
    gh pr diff 32003 --repo geneontology/go-ontology
    gh pr diff 189 --repo ai4curation/eval-ont-agent-go
-->

## Summary

The agent correctly implemented the requested obsoletion of `GO:0043713` `(R)-2-hydroxyisocaproate dehydrogenase activity` and replaced it with `GO:0140175` `(2R)-2-hydroxyacid dehydrogenase (NAD+) activity`. Its diff matches the human PR exactly, so the metadiff F1/precision/recall of 1.0 accurately reflects a complete and tightly scoped solution.


## Strengths

- Selected the exact target term from issue `#31966`, `GO:0043713`, and the exact replacement requested by the curator, `GO:0140175`.
- Followed the GO obsoletion pattern correctly: changed the label to `obsolete ...`, prefixed the definition with `OBSOLETE.`, removed the active `is_a: GO:0016616` parent, added `is_obsolete: true`, and added `replaced_by: GO:0140175`.
- Preserved the full curator-facing obsoletion rationale from the human PR, including the link between `(R)-2-hydroxyisocaproate dehydrogenase`, `EC:1.1.1.345`, the exact-match xref on `GO:0140175`, and the `RHEA:10052` narrowMatch reaction.
- Added the correct tracker metadata, `property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31966" xsd:anyURI`.
- Kept the edit limited to the `GO:0043713` stanza in `src/ontology/go-edit.obo`, with no unrelated ontology changes.


## Issues

- No issues found. The agent PR is equivalent to the merged human solution for this single-term obsoletion.
