---
ontology: go-ontology
issue_number: 31877
pr_number: 31973
eval_repo_pr: 130
agent: std_codex_g55
model: gpt-5.5
runtime: codex
agent_config_tag: v9
case_type: obsoletion
difficulty: hard
f1: 0.552
precision: 0.457
recall: 0.697
jaccard: 0.381
outcome: partial_success
failure_modes:
  - wrong_pattern
reviewed_by: gpt-5.5
reviewed_at: 2026-05-11
---

<!-- Review this eval run following analysis/instructions/review-agent-eval.md

  Source issue: https://github.com/geneontology/go-ontology/issues/31877
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/31973
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/130
  Agent config: ai4curation/go-ontology-agent-config

  Quick reference:
    gh issue view 31877 --repo geneontology/go-ontology
    gh pr diff 31973 --repo geneontology/go-ontology
    gh pr diff 130 --repo ai4curation/eval-ont-agent-go
-->

## Summary

The agent correctly identified the target of issue #31877 and obsoleted `GO:0010381` "peroxisome-chloroplast membrane tethering", including removal of its taxon constraints from the TSV/OFN sources and generated OWL import. The metadiff F1 of 0.552 understates the quality somewhat because much of the mismatch is generated `go_taxon_constraints.owl` churn, but it also captures a real semantic difference: the agent used `replaced_by: GO:7770065` where the human PR used `consider: GO:7770065`.

## Strengths

- Correctly obsoleted `GO:0010381` by renaming it to `obsolete peroxisome-chloroplast membrane tethering`, adding `is_obsolete: true`, adding the issue tracker property for #31877, prefixing the definition with `OBSOLETE.`, and removing the asserted parent `is_a: GO:0140056`.
- Correctly recognized the intended replacement candidate, `GO:7770065` "peroxisome-chloroplast membrane tether activity", and documented that the BP term was obsolete because it represented a molecular function rather than a biological process.
- Performed the important taxon-constraint cleanup cascade for the obsoleted term: removed the four `never_in_taxon.tsv` rows for `GO:0010381` against `NCBITaxon:28009`, `NCBITaxon:33208`, `NCBITaxon:4751`, and `NCBITaxon:554915`; removed the corresponding OFN declaration/axioms; and removed the `GO_0010381` class block from `go_taxon_constraints.owl`.
- Kept the ontology edit focused on the single requested obsolete term and did not invent unrelated ontology term changes in `go-edit.obo`.

## Issues

- The agent used `replaced_by: GO:7770065`, while the human PR used `consider: GO:7770065`. For an obsolete biological_process term being redirected to a molecular_function term, `replaced_by` is too strong because it implies automatic annotation migration; the human solution's `consider` is the safer GO obsoletion pattern.
- The comment text also says "Replaced by the molecular_function term GO:7770065", reinforcing the same over-strong replacement interpretation. The human comment only states the reason for obsoletion and leaves the replacement candidate in `consider`.
- The regenerated `src/ontology/imports/go_taxon_constraints.owl` does not fully match the human regenerated file. The agent removed the `GO_0010381` block, which is the task-critical part, but it did not include the human PR's additional generated import updates such as adding constraints for `GO_0000956` and `GO_0141065` and changing `GO_0140494` from `NCBITaxon_7742` to `NCBITaxon_2759` with cleaned `PMID:40712579` source annotations. These appear to be generated-file drift rather than core issue failures, but they explain part of the low recall.
