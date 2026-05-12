---
ontology: go-ontology
issue_number: 31945
pr_number: 32013
eval_repo_pr: 104
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
reviewed_by: gpt-5.5
reviewed_at: 2026-05-11
---

<!-- Review this eval run following analysis/instructions/review-agent-eval.md

  Source issue: https://github.com/geneontology/go-ontology/issues/31945
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/32013
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/104
  Agent config: ai4curation/go-ontology-agent-config

  Quick reference:
    gh issue view 31945 --repo geneontology/go-ontology
    gh pr diff 32013 --repo geneontology/go-ontology
    gh pr diff 104 --repo ai4curation/eval-ont-agent-go
-->

## Summary

The agent correctly addressed the main biological request from geneontology/go-ontology#31945: it obsoleted `GO:0003400 regulation of COPII vesicle coating`, used `GO:0048208` as the replacement, and renamed both `GO:0048208` and `GO:0006901` from "coating" to "coat assembly" labels. The metadiff score (`f1: 0.818`, `precision: 0.9`, `recall: 0.75`) is a fair signal of a mostly correct but imperfect result: the agent matched the core changes, missed two accepted inline-comment updates, and added unrequested logical/definition edits to `GO:0006901`.


## Strengths

- Correctly obsoleted `GO:0003400` by changing the label to `obsolete regulation of COPII vesicle coating`, prefixing the definition with `OBSOLETE.`, removing the `intersection_of` logical definition for regulation of `GO:0048208`, adding `is_obsolete: true`, and adding `replaced_by: GO:0048208`.
- Added appropriate obsoletion provenance for `GO:0003400`, including `property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31945" xsd:anyURI`.
- The obsoletion comment captures the issue's rationale that the annotated proteins are part of the COPII vesicle coat assembly pathway rather than upstream regulators.
- Correctly renamed `GO:0048208` from `COPII vesicle coating` to `COPII vesicle coat assembly` and retained the old label as an exact synonym.
- Correctly renamed `GO:0006901` from `vesicle coating` to `vesicle coat assembly` and converted the previous "coat assembly" wording from synonym to primary label, which was the broader rename requested in the issue.


## Issues

- The agent over-edited `GO:0006901`. The accepted PR only renamed the term and swapped the old label into an exact synonym; the agent also rewrote the definition from the established vesicle-coating wording to a generic assembly definition and added `intersection_of: GO:0022607 ! cellular component assembly` plus `intersection_of: results_in_assembly_of GO:0030120 ! vesicle coat`. Those axioms may be biologically plausible, but they were not requested and should have been a separate curator-reviewed modeling change.
- The agent added `term_tracker_item` provenance to renamed active terms `GO:0006901` and `GO:0048208`. The human PR only added the tracker item to the obsoleted term `GO:0003400`; adding issue tracker metadata to ordinary rename targets is unnecessary extra scope.
- The agent missed two accepted comment-maintenance edits: `GO:0016183 synaptic vesicle coating` and `GO:0048200 Golgi transport vesicle coating` still have inline parent comments pointing to `GO:0006901 ! vesicle coating` in the agent diff, while the human PR updated those to `GO:0006901 ! vesicle coat assembly`.
- The synonym xref handling for `GO:0006901` differs from the accepted PR. The human PR used `synonym: "vesicle coating" EXACT []`; the agent used `synonym: "vesicle coating" EXACT [GOC:jid]`. This is minor, but it is another instance where the agent made an unsupported metadata choice instead of a minimal rename.
