---
ontology: go-ontology
issue_number: 31916
pr_number: 32024
eval_repo_pr: 106
agent: std_opencode_g55
model: gpt-5.5
runtime: opencode
agent_config_tag: v9
case_type: obsoletion
difficulty: medium
f1: 0.965
precision: 0.965
recall: 0.965
jaccard: 0.932
outcome: success
failure_modes: []
reviewed_by: gpt-5.5
reviewed_at: 2026-05-11
---

<!-- Review this eval run following analysis/instructions/review-agent-eval.md

  Source issue: https://github.com/geneontology/go-ontology/issues/31916
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/32024
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/106
  Agent config: ai4curation/go-ontology-agent-config

  Quick reference:
    gh issue view 31916 --repo geneontology/go-ontology
    gh pr diff 32024 --repo geneontology/go-ontology
    gh pr diff 106 --repo ai4curation/eval-ont-agent-go
-->

## Summary

The agent essentially matched the merged human solution for issue #31916. It obsoleted the Entner-Doudoroff pathway variant terms, preserved the requested MetaCyc variant mappings as `skos:narrowMatch` xrefs on `GO:0061678`, and included the additional `GO:0061688` obsoletion present in the human PR. The high metadiff score (`F1=0.965`, `precision=0.965`, `recall=0.965`) accurately reflects a near-exact substantive match; the remaining differences are mostly comment wording and one extra tracker item.

## Strengths

- Correctly obsoleted the four issue-requested variant pathway terms `GO:0009255`, `GO:0061679`, `GO:0061680`, and `GO:0061681`, with obsolete names/definitions, `is_obsolete: true`, issue #31916 tracker metadata, and `replaced_by: GO:0061678`.
- Correctly stripped active logical structure from those obsolete terms, including `is_a`, `intersection_of`, and variant-specific xrefs such as `MetaCyc:PWY-8004`, `MetaCyc:NPGLUCAT-PWY`, and `MetaCyc:PWY-2221`.
- Correctly updated the retained parent `GO:0061678` by removing the grouping-class xref `MetaCyc:Entner-Doudoroff-Pathways` and adding the four requested variant pathway xrefs as narrow matches: `MetaCyc:ENTNER-DOUDOROFF-PWY`, `MetaCyc:NPGLUCAT-PWY`, `MetaCyc:PWY-2221`, and `MetaCyc:PWY-8004`.
- Matched the human PR's additional obsoletion of `GO:0061688` (`glycolytic process via Entner-Doudoroff Pathway`) with `replaced_by: GO:0006096`, removing its `is_a`, `intersection_of`, and related synonym from the active term body.
- The agent report indicates a reasonable ontology-editing process: term search, obsoletion pattern use, mapping guidance, and post-edit `make travis_build` validation.

## Issues

- Minor style difference: the agent's obsolete-term comments are less specific than the human PR's comments. For example, the human comments for `GO:0009255`, `GO:0061679`, `GO:0061680`, and `GO:0061681` explicitly mention replacement by `GO:0061678` and MetaCyc's treatment of the pathways as variants; the agent uses a shorter generic GO-CAM rationale. This is still valid and does not change the ontology semantics.
- Minor scope/metadata difference: the agent added `property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31916"` to the active parent `GO:0061678`, which the human PR did not. This is harmless traceability metadata, but it is an extra edit beyond the merged reference solution.
