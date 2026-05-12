---
ontology: go-ontology
issue_number: 31945
pr_number: 32013
eval_repo_pr: 183
agent: std_codex_g54
model: gpt-5.4
runtime: codex
agent_config_tag: v9
case_type: reclassification
difficulty: medium
f1: 0.864
precision: 0.95
recall: 0.792
jaccard: 0.76
outcome: partial_success
failure_modes:
  - over_editing
  - under_editing
reviewed_by: gpt-5.5
reviewed_at: 2026-05-11
---

<!-- Review this eval run following analysis/instructions/review-agent-eval.md

  Source issue: https://github.com/geneontology/go-ontology/issues/31945
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/32013
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/183
  Agent config: ai4curation/go-ontology-agent-config

  Quick reference:
    gh issue view 31945 --repo geneontology/go-ontology
    gh pr diff 32013 --repo geneontology/go-ontology
    gh pr diff 183 --repo ai4curation/eval-ont-agent-go
-->

## Summary

The agent correctly handled the central request from geneontology/go-ontology#31945: it obsoleted `GO:0003400 regulation of COPII vesicle coating`, used `GO:0048208` as the replacement, and renamed both `GO:0048208` and `GO:0006901` from "coating" to "coat assembly" terminology. The metadiff score (`f1: 0.864`, `precision: 0.95`, `recall: 0.792`) is a fair reflection of a strong but imperfect solution: the core biological edits match the human PR, but the agent missed two accepted comment-maintenance edits and made unrequested definition changes to active terms.


## Strengths

- Correctly obsoleted `GO:0003400` by changing the label to `obsolete regulation of COPII vesicle coating`, prefixing the definition with `OBSOLETE.`, removing the `intersection_of` logical definition for regulation of `GO:0048208`, adding `is_obsolete: true`, and adding `replaced_by: GO:0048208`.
- Added the expected obsoletion provenance for `GO:0003400`, including `property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31945" xsd:anyURI`.
- Correctly selected `GO:0048208` as the replacement term, consistent with the issue statement that the annotated gene products are part of the COPII vesicle coating pathway rather than upstream regulators.
- Correctly renamed `GO:0048208` from `COPII vesicle coating` to `COPII vesicle coat assembly` and retained the old label as an exact synonym.
- Correctly renamed `GO:0006901` from `vesicle coating` to `vesicle coat assembly` and changed the old broad synonym into an exact synonym for the former label.


## Issues

- The agent over-edited the definitions of active terms. The human PR only changed labels and synonyms for `GO:0006901` and `GO:0048208`; the agent also rewrote `GO:0006901` from the established "A protein coat is added..." definition to a generic "aggregation, arrangement and bonding..." assembly definition, and rewrote the `GO:0048208` definition from COPII protein/adaptor addition to a similarly generic COPII coat assembly definition. These may be defensible modeling ideas, but they go beyond the requested rename and remove biological detail that the accepted PR preserved.
- The agent missed two accepted inline-comment updates on incoming `is_a` edges to `GO:0006901`: `GO:0016183 synaptic vesicle coating` and `GO:0048200 Golgi transport vesicle coating` still point to `GO:0006901 ! vesicle coating` in the agent diff, while the human PR updates both comments to `GO:0006901 ! vesicle coat assembly`.
- The obsoletion comment for `GO:0003400` is less informative than the accepted PR. It says only that the data can be described using `COPII vesicle coat assembly`, while the human PR records the key rationale that the proteins are part_of the COPII vesicle coating pathway rather than upstream regulators and directs annotations to `GO:0048208`.
