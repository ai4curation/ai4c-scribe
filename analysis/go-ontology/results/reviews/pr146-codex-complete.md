---
ontology: go-ontology
issue_number: 31877
pr_number: 31973
eval_repo_pr: 146
agent: std_opencode_g55
model: gpt-5.5
runtime: opencode
agent_config_tag: v9
case_type: obsoletion
difficulty: hard
f1: 0.553
precision: 0.458
recall: 0.698
jaccard: 0.382
outcome: success
failure_modes: []
reviewed_by: codex
reviewed_at: "2026-05-16"
---

<!-- Review this eval run following analysis/instructions/review-agent-eval.md

  Source issue: https://github.com/geneontology/go-ontology/issues/31877
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/31973
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/146
  Agent config: ai4curation/go-ontology-agent-config

  Quick reference:
    gh issue view 31877 --repo geneontology/go-ontology
    gh pr diff 31973 --repo geneontology/go-ontology
    gh pr diff 146 --repo ai4curation/eval-ont-agent-go
-->

## Summary

The agent successfully handled issue #31877 by obsoleting `GO:0010381` "peroxisome-chloroplast membrane tethering" and pointing users to the new molecular-function term `GO:7770065` with `consider`. The metadiff F1 of 0.553 understates the substantive quality: the core obsoletion and taxon-constraint cleanup are present, while much of the mismatch comes from generated `go_taxon_constraints.owl` churn and unrelated generated import updates in the human PR.


## Strengths

- Correctly obsoleted `GO:0010381`: renamed it to `obsolete peroxisome-chloroplast membrane tethering`, prefixed the definition with `OBSOLETE.`, added `is_obsolete: true`, added the issue tracker property for #31877, removed the asserted parent `is_a: GO:0140056`, and dropped the exact synonym.
- Used the correct obsoletion relationship, `consider: GO:7770065`, matching the human PR and the issue's request for a new molecular-function term rather than overusing `replaced_by`.
- Captured the reason for obsoletion: the biological-process term represents a molecular function. The human PR words this slightly more explicitly as "rather than a biological process", but the agent's comment is ontologically correct.
- Performed the important taxon-constraint cascade for the obsolete term by removing the four `never_in_taxon.tsv` rows for `GO:0010381` against `NCBITaxon:28009`, `NCBITaxon:33208`, `NCBITaxon:4751`, and `NCBITaxon:554915`, removing the matching OFN declaration/axioms, and deleting the `GO_0010381` block from `go_taxon_constraints.owl`.
- Kept the manual ontology edit focused on the requested single term and did not introduce unrelated `go-edit.obo` changes.


## Issues

- The generated `src/ontology/imports/go_taxon_constraints.owl` output does not exactly match the human PR. The agent removed the task-critical `GO_0010381` block, but the human regenerated import also included extra non-`GO:0010381` updates such as adding `GO_0000956` and `GO_0141065` taxon constraints and changing `GO_0140494` from `NCBITaxon_7742` to `NCBITaxon_2759` with cleaned `PMID:40712579` sources. These appear to be generated-file drift rather than a failure to solve the issue.
- Minor style difference: the obsoletion comment is less explicit than the human PR because it says only that the term represents a molecular function, omitting "rather than a biological process." This does not change the ontology semantics.
