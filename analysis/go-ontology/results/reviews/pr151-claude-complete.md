---
ontology: go-ontology
issue_number: 31956
pr_number: 31960
eval_repo_pr: 151
agent: std_opencode_g55
model: gpt-5.5
runtime: opencode
agent_config_tag: v9
case_type: obsoletion
difficulty: simple
f1: 0.9
precision: 0.9
recall: 0.9
jaccard: 0.818
outcome: success
failure_modes: []
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

## Summary

Running gpt-5.5 under opencode, the agent obsoleted GO:0005870 "actin capping protein of dynactin complex" with `replaced_by: GO:0008290`, producing a diff functionally identical to human gold PR #31960 apart from the obsoletion `comment:` prose. F1=0.900 under-represents quality — this is a correct, complete obsoletion.

## Strengths

- Diff matches gold semantically: name prefixed "obsolete", definition prefixed "OBSOLETE." (original `[GOC:jl, PMID:18221362, PMID:18544499]` xrefs preserved), both `intersection_of` axioms removed (genus `GO:0008290`, differentia `part_of GO:0005869`), `is_obsolete: true`, `replaced_by: GO:0008290`, and `term_tracker_item` for #31956 added.
- Concise, accurate PR summary that correctly enumerates each obsoletion step; tight scope confined to the single GO:0005870 stanza in `src/ontology/go-edit.obo`.
- Correct replacement target — GO:0008290 was the genus of the original logical definition, the standard choice for this redundant specialization.

## Issues

- Brief methodology narrative: the PR comment lists the changes but provides little evidence of independent reference/annotation verification (no robot/runoak output reported in the attempt detail). For a trivial unused-term obsoletion this is acceptable, but it is thinner than the claude/codex sibling runs.
- The `comment:` text ("this term is equivalent to F-actin capping protein complex") slightly overstates the relationship — GO:0005870 was a specialization, not an equivalent class. Harmless for an unused term, consistent with several sibling attempts, and the sole contributor to the 0.1 F1 gap (a normalization artifact, not an error).
