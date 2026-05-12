---
ontology: go-ontology
issue_number: 31916
pr_number: 32024
eval_repo_pr: 180
agent: std_codex_g54
model: gpt-5.4
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
reviewed_by: gpt-5.5
reviewed_at: 2026-05-11
---

<!-- Review this eval run following analysis/instructions/review-agent-eval.md

  Source issue: https://github.com/geneontology/go-ontology/issues/31916
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/32024
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/180
  Agent config: ai4curation/go-ontology-agent-config

  Quick reference:
    gh issue view 31916 --repo geneontology/go-ontology
    gh pr diff 32024 --repo geneontology/go-ontology
    gh pr diff 180 --repo ai4curation/eval-ont-agent-go
-->

## Summary

The agent correctly addressed issue #31916 by obsoleting the Entner-Doudoroff pathway variant terms and moving the MetaCyc variant mappings onto the parent `GO:0061678` as `skos:narrowMatch` xrefs. It also matched the human PR's broader cleanup of `GO:0061688 glycolytic process via Entner-Doudoroff Pathway`, replacing it with `GO:0006096`. The high metadiff score (`F1=0.965`, precision `0.965`, recall `0.965`) is a fair reflection of the result: the substantive ontology edits match, with only minor comment/provenance differences.


## Strengths

- Correctly obsoleted the four Entner-Doudoroff child pathway variants requested in the issue: `GO:0009255`, `GO:0061679`, `GO:0061680`, and `GO:0061681`.
- Used the correct replacement for those variant terms, `replaced_by: GO:0061678`, and removed their active `is_a`, `xref`, synonym, and logical `intersection_of` axioms as appropriate for obsolete GO terms.
- Correctly updated `GO:0061678 Entner-Doudoroff pathway` by removing the grouping-class xref `MetaCyc:Entner-Doudoroff-Pathways` and adding the variant pathway xrefs `MetaCyc:ENTNER-DOUDOROFF-PWY`, `MetaCyc:NPGLUCAT-PWY`, `MetaCyc:PWY-2221`, and `MetaCyc:PWY-8004` with `source="skos:narrowMatch"`.
- Also matched the accepted PR's treatment of `GO:0061688 glycolytic process via Entner-Doudoroff Pathway`: obsoleted the term, stripped the active parent/logical axiom, and used `replaced_by: GO:0006096`.
- Preserved existing historical metadata where relevant, including the prior `term_tracker_item` for issue #28392 on `GO:0061680`, while adding traceability to issue #31916 on the obsolete terms.


## Issues

- No significant correctness issues. The agent's obsolete comments are less informative than the human PR's comments: for `GO:0009255`, `GO:0061679`, `GO:0061680`, and `GO:0061681`, the human text explicitly mentions MetaCyc variant pathways and GO-CAM representation, while the agent uses a generic "merged into the broader Entner-Doudoroff pathway" explanation.
- Minor extra provenance edit: the agent added `property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31916" xsd:anyURI` to the still-active parent `GO:0061678`, which the human PR did not. This is harmless but not necessary for the requested xref cleanup.
- The agent's comment for `GO:0061688` is weaker than the human PR's because it says only that the pathway variant is being merged into `GO:0006096`; the human comment gives the more specific annotation rationale that existing IEA annotations are better captured by `GO:0006096` and that variants are better represented as GO-CAMs.
