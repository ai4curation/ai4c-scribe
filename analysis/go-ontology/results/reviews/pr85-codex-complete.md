---
ontology: go-ontology
issue_number: 31916
pr_number: 32024
eval_repo_pr: 85
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
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/85
  Agent config: ai4curation/go-ontology-agent-config

  Quick reference:
    gh issue view 31916 --repo geneontology/go-ontology
    gh pr diff 32024 --repo geneontology/go-ontology
    gh pr diff 85 --repo ai4curation/eval-ont-agent-go
-->

## Summary

The agent essentially solved issue #31916 and closely matched the merged human PR. It obsoleted the Entner-Doudoroff pathway variant terms, moved the individual MetaCyc pathway IDs onto the retained parent `GO:0061678` as `skos:narrowMatch` xrefs, and also included the human PR's additional obsoletion of `GO:0061688`. The high metadiff score (`F1=0.965`, `precision=0.965`, `recall=0.965`) is a fair reflection of the result; the remaining differences are minor wording and provenance details.

## Strengths

- Correctly obsoleted the four child variant pathway terms requested in the issue: `GO:0009255`, `GO:0061679`, `GO:0061680`, and `GO:0061681`.
- Used the right replacement target for those four variants, `replaced_by: GO:0061678`, and removed their active ontology structure, including `is_a`, `intersection_of`, and variant-specific xrefs such as `MetaCyc:PWY-8004`, `MetaCyc:NPGLUCAT-PWY`, and `MetaCyc:PWY-2221`.
- Correctly updated `GO:0061678 Entner-Doudoroff pathway` by removing the grouping-class xref `MetaCyc:Entner-Doudoroff-Pathways` and adding the requested narrow matches: `MetaCyc:ENTNER-DOUDOROFF-PWY`, `MetaCyc:NPGLUCAT-PWY`, `MetaCyc:PWY-2221`, and `MetaCyc:PWY-8004`.
- Preserved the pre-existing issue #28392 tracker metadata on `GO:0061680` while adding issue #31916 tracker metadata to the obsoleted terms.
- Matched the human PR's broader cleanup of `GO:0061688 glycolytic process via Entner-Doudoroff Pathway`, obsoleting it with `replaced_by: GO:0006096` and removing its active parentage, logical axiom, and related synonym.

## Issues

- No significant correctness issues. The agent's obsoletion comments are less specific than the human PR's comments: for `GO:0009255`, `GO:0061679`, `GO:0061680`, and `GO:0061681`, the human text explicitly says the variants are better represented by `GO:0061678` and notes MetaCyc's treatment of them as variant pathways; the agent uses a shorter generic GO-CAM rationale.
- Minor metadata difference: the agent added `property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31916" xsd:anyURI` to the active parent `GO:0061678`, which the human PR did not. This is harmless traceability metadata, but it is extra relative to the reference solution.
- The agent's comment for `GO:0061688` is also weaker than the human PR's because it does not mention the specific annotation rationale that existing IEA annotations are better captured by `GO:0006096`.
