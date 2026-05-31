---
ontology: go-ontology
issue_number: 31981
pr_number: 31995
eval_repo_pr: 97
agent: std_opencode_g55
model: gpt-5.5
runtime: opencode
agent_config_tag: v9
case_type: axiom_repair
difficulty: simple
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

  Source issue: https://github.com/geneontology/go-ontology/issues/31981
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/31995
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/97
  Agent config: ai4curation/go-ontology-agent-config

  Quick reference:
    gh issue view 31981 --repo geneontology/go-ontology
    gh pr diff 31995 --repo geneontology/go-ontology
    gh pr diff 97 --repo ai4curation/eval-ont-agent-go
-->

## Summary

The agent successfully addressed issue #31981 by making the same edit as the merged human PR: adding `relationship: part_of GO:0072583 ! clathrin-dependent endocytosis` to `GO:0072318 clathrin coat disassembly`, plus the issue tracker property. The metadiff score of 1.0 accurately reflects the substantive result here: the agent diff is an exact match to the human diff and stays tightly scoped to the requested axiom repair.


## Strengths

- Correctly identified the requested target term, `GO:0072318 clathrin coat disassembly`, and added the requested parentage to `GO:0072583 clathrin-dependent endocytosis`.
- Used the appropriate `part_of` relationship rather than forcing an `is_a` superclass. This matches the human PR and is ontologically sensible because clathrin coat disassembly is a subprocess within clathrin-dependent endocytosis, not a subtype of it.
- Preserved the existing logical definition structure for `GO:0072318`, including `is_a: GO:0072319 ! vesicle uncoating` and `intersection_of: results_in_disassembly_of GO:0030118 ! clathrin coat`.
- Added the expected `term_tracker_item` property pointing to `https://github.com/geneontology/go-ontology/issues/31981`.
- Kept the change minimal: one ontology stanza, two added lines, no unrelated edits.


## Issues

No substantive issues. The agent's diff matches the human PR exactly and satisfies the source issue without under-editing or scope creep.
