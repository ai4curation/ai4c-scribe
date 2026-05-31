---
ontology: cell-ontology
issue_number: 3447
pr_number: 3448
eval_repo_pr: 52
agent: std_opencode_g55
model: openai/gpt-5.5
runtime: opencode
agent_config_tag: ai4curation/cl-agent-config@v3
case_type: other
difficulty: medium
f1: 0.462
precision: 0.375
recall: 0.600
jaccard: 0.300
outcome: success
failure_modes:
  - over_editing
case_quality: poor
case_quality_reason: gold_has_out_of_scope_extras_and_provenance
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-16
---

## Summary

This is a duplicate run of the same gpt-5.5/opencode configuration as eval PR
#72 and produced a **byte-identical edit-file blob (`26c8a14`)**. The
assessment is therefore the same: the agent correctly retained the existing
`doi:10.1016/j.cub.2021.10.015` xref, added both requested PMIDs, corrected the
label, added the GABAergic neuron parent, and preserved existing axioms. The
definition is a faithful paraphrase rather than the issue's verbatim text, and
an `IAO_0000233` tracker plus a CPNE4 comment tidy were added. F1=0.462
under-represents the actual quality for the same reasons as #72.

## Strengths

- Identical correct output to #72 (blob `26c8a14`), demonstrating run-to-run
  determinism for this configuration.
- Reference handling exactly honors the issue: existing DOI retained,
  `PMID:34795450` and `PMID:37898623` added.
- Label corrected; GABAergic neuron parent `SubClassOf(obo:CL_4030053
  obo:CL_0000617)` added; `CL_0000120` and location/expression axioms
  preserved.
- Good methodology: confirmed `CL_0000617` label, consulted PubMed records for
  both PMIDs, ran `robot convert` successfully.

## Issues

- **Style**: paraphrased definition rather than the issue's verbatim text;
  drops the inline "(Zhang et al., …)" citations. Same as #72.
- **Over-editing (defensible)**: added `IAO_0000233` tracker annotation (not
  requested, gold did not add one) and changed the CPNE4 `rdfs:comment` to use
  the plural "Islands". Reasonable consistency edit plus a common-practice
  extra.
- Metadiff note: F1=0.462 understates quality; the recall gap is dominated by
  gold extras (author ORCID `terms:contributor`, the unrelated `hasDbXref`
  comment edit, `hra_subset.owl` auto-churn) the issue never asked for and the
  agent could not reproduce. Substantively this is a correct, well-scoped
  resolution.
