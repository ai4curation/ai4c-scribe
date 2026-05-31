---
ontology: go-ontology
issue_number: 31916
pr_number: 32024
eval_repo_pr: 65
agent: std_codex_g55
model: gpt-5.5
runtime: codex
agent_config_tag: v9
case_type: obsoletion
difficulty: medium
f1: 0.965
precision: 0.965
recall: 0.965
jaccard: 0.932
outcome: success
failure_modes: []
reviewed_by: codex
reviewed_at: "2026-05-16"
---

<!-- Review this eval run following analysis/instructions/review-agent-eval.md

  Source issue: https://github.com/geneontology/go-ontology/issues/31916
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/32024
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/65
  Agent config: ai4curation/go-ontology-agent-config

  Quick reference:
    gh issue view 31916 --repo geneontology/go-ontology
    gh pr diff 32024 --repo geneontology/go-ontology
    gh pr diff 65 --repo ai4curation/eval-ont-agent-go
-->

## Summary

The agent essentially solved issue #31916 and closely matched the human PR. It obsoleted the Entner-Doudoroff pathway variant terms, moved the MetaCyc variant mappings onto the retained parent `GO:0061678` as `skos:narrowMatch` xrefs, and also included the human PR's obsoletion of `GO:0061688`. The high metadiff score (`F1=0.965`, `precision=0.965`, `recall=0.965`) is a fair reflection of the result; the differences are minor comment wording and one extra tracker item.


## Strengths

- Correctly obsoleted the issue-requested Entner-Doudoroff child pathway terms `GO:0009255`, `GO:0061679`, `GO:0061680`, and `GO:0061681`, with obsolete labels/definitions, `is_obsolete: true`, issue #31916 tracker metadata, and `replaced_by: GO:0061678`.
- Correctly removed active logical structure from those obsolete terms, including `is_a` parents, `intersection_of` axioms, and term-level MetaCyc xrefs such as `MetaCyc:PWY-8004`, `MetaCyc:NPGLUCAT-PWY`, and `MetaCyc:PWY-2221`.
- Correctly updated the retained parent `GO:0061678` by replacing the grouping-class xref `MetaCyc:Entner-Doudoroff-Pathways` with the four variant pathway xrefs as narrow matches: `MetaCyc:ENTNER-DOUDOROFF-PWY`, `MetaCyc:NPGLUCAT-PWY`, `MetaCyc:PWY-2221`, and `MetaCyc:PWY-8004`.
- Preserved the pre-existing issue #28392 tracker item on `GO:0061680` while adding the new issue #31916 tracker item, avoiding unrelated metadata loss.
- Matched the human PR's additional cleanup of `GO:0061688` (`glycolytic process via Entner-Doudoroff Pathway`), obsoleting it with `replaced_by: GO:0006096` and removing its active parentage, logical axiom, and related synonym.


## Issues

- Minor style difference: the agent's obsoletion comments are less specific than the human PR's comments. For `GO:0009255`, `GO:0061679`, `GO:0061680`, and `GO:0061681`, the human PR explicitly says the variants are better represented by `GO:0061678` and notes MetaCyc's treatment of them as variant pathways; the agent uses a shorter GO-CAM rationale. This does not change the ontology semantics.
- Minor scope/metadata difference: the agent added `property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31916" xsd:anyURI` to the still-active parent `GO:0061678`, which the human PR did not. This is harmless traceability metadata, but it is extra relative to the reference solution.
