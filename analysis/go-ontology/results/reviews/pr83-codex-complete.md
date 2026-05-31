---
ontology: go-ontology
issue_number: 31945
pr_number: 32013
eval_repo_pr: 83
agent: std_opencode_g55
model: gpt-5.5
runtime: opencode
agent_config_tag: v9
case_type: reclassification
difficulty: medium
f1: 0.818
precision: 0.9
recall: 0.75
jaccard: 0.692
outcome: partial_success
failure_modes:
  - over_editing
  - under_editing
  - scope_creep
reviewed_by: codex
reviewed_at: "2026-05-16"
---

<!-- Review this eval run following analysis/instructions/review-agent-eval.md

  Source issue: https://github.com/geneontology/go-ontology/issues/31945
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/32013
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/83
  Agent config: ai4curation/go-ontology-agent-config

  Quick reference:
    gh issue view 31945 --repo geneontology/go-ontology
    gh pr diff 32013 --repo geneontology/go-ontology
    gh pr diff 83 --repo ai4curation/eval-ont-agent-go
-->

## Summary

The agent addressed the central request from geneontology/go-ontology#31945: it obsoleted `GO:0003400 regulation of COPII vesicle coating`, pointed it to `GO:0048208`, and renamed both `GO:0048208` and `GO:0006901` to "coat assembly" wording. The metadiff score (`f1: 0.818`, `precision: 0.9`, `recall: 0.75`) is a fair signal of a mostly correct but imperfect result: the agent matched the core biological edits, but it made extra active-term modeling changes and missed two accepted comment-maintenance edits.


## Strengths

- Correctly obsoleted `GO:0003400` by changing the label to `obsolete regulation of COPII vesicle coating`, prefixing the definition with `OBSOLETE.`, removing the `intersection_of` logical definition over `GO:0065007` and `regulates GO:0048208`, adding `is_obsolete: true`, and adding `replaced_by: GO:0048208`.
- Added the expected obsoletion provenance for `GO:0003400`, including `property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31945" xsd:anyURI`.
- The obsoletion comment captures the issue's main rationale that the proteins annotated to `GO:0003400` are part of COPII vesicle coat assembly rather than upstream regulators.
- Correctly renamed `GO:0048208` from `COPII vesicle coating` to `COPII vesicle coat assembly`, retained the old label as an exact synonym, and preserved the existing logical definition with `results_in_assembly_of GO:0030127`.
- Correctly renamed `GO:0006901` from `vesicle coating` to `vesicle coat assembly` and retained the old label as an exact synonym.


## Issues

- The agent over-edited `GO:0006901`. The accepted PR only changed the label and synonym, while the agent also rewrote the definition to a generic assembly definition and added `intersection_of: GO:0022607 ! cellular component assembly` plus `intersection_of: results_in_assembly_of GO:0030120 ! vesicle coat`. These axioms may be plausible, but they were not requested and should have been a separate curator-reviewed modeling change.
- The agent added `term_tracker_item` provenance to active renamed terms `GO:0006901` and `GO:0048208`. The human PR only added the tracker item to the obsoleted term `GO:0003400`; adding issue metadata to ordinary rename targets is unnecessary scope creep.
- The agent missed two accepted inline-comment updates after renaming `GO:0006901`: `GO:0016183 synaptic vesicle coating` and `GO:0048200 Golgi transport vesicle coating` still lack the human PR's updated `is_a: GO:0006901 ! vesicle coat assembly` comments in the agent diff.
- The synonym xref handling for `GO:0006901` differs from the accepted PR. The human PR used `synonym: "vesicle coating" EXACT []`, while the agent used `synonym: "vesicle coating" EXACT [GOC:jid]`; this is minor, but it is another unsupported metadata choice.
