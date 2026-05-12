---
ontology: go-ontology
issue_number: 31877
pr_number: 31973
eval_repo_pr: 164
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
reviewed_by: gpt-5.5
reviewed_at: 2026-05-11
---

<!-- Review this eval run following analysis/instructions/review-agent-eval.md

  Source issue: https://github.com/geneontology/go-ontology/issues/31877
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/31973
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/164
  Agent config: ai4curation/go-ontology-agent-config

  Quick reference:
    gh issue view 31877 --repo geneontology/go-ontology
    gh pr diff 31973 --repo geneontology/go-ontology
    gh pr diff 164 --repo ai4curation/eval-ont-agent-go
-->

## Summary

The agent successfully handled issue #31877 by obsoleting `GO:0010381` "peroxisome-chloroplast membrane tethering", using `consider: GO:7770065` for the already-created molecular-function replacement, and removing the obsolete term's taxon constraints. The metadiff F1 of 0.553 understates the practical quality: the core ontology edit matches the human PR, while much of the mismatch is generated `go_taxon_constraints.owl` drift and unrelated taxon-constraint updates present in the human PR.


## Strengths

- Correctly applied the obsoletion pattern for `GO:0010381`: renamed the term to `obsolete peroxisome-chloroplast membrane tethering`, prefixed the definition with `OBSOLETE.`, added `is_obsolete: true`, added the `term_tracker_item` for issue #31877, removed the asserted parent `is_a: GO:0140056`, and removed the exact synonym `attachment of peroxisome to chloroplast`.
- Used `consider: GO:7770065` rather than `replaced_by`, which is appropriate because the old term is in `biological_process` and the suggested replacement `GO:7770065` "peroxisome-chloroplast membrane tether activity" is in `molecular_function`.
- Cleaned up the important taxon-constraint cascade for the obsolete term by removing the four `never_in_taxon.tsv` rows for `GO:0010381` against `NCBITaxon:28009`, `NCBITaxon:33208`, `NCBITaxon:4751`, and `NCBITaxon:554915`, removing the corresponding OFN declaration/axioms, and deleting the `GO_0010381` block from `go_taxon_constraints.owl`.
- The agent's PR notes show appropriate methodology: it checked the existing replacement term, recognized the BP-to-MF namespace issue, regenerated taxon-constraint artifacts, and reported validation with `make travis_build`.


## Issues

- The obsoletion comment is slightly less explicit than the human PR. The agent wrote that the term represents a molecular function, while the human PR says it represents a molecular function rather than a biological process. This is a minor style/narrative difference, not a semantic failure.
- The generated `src/ontology/imports/go_taxon_constraints.owl` output does not exactly match the human PR. The agent removed the task-critical `GO_0010381` block, but the human regenerated import also included unrelated updates such as adding Eukaryota constraints for `GO_0000956` and `GO_0141065` and changing `GO_0140494` "migrasome" from `NCBITaxon_7742` to `NCBITaxon_2759` with source cleanup. These differences explain much of the low precision/recall score but are not required to solve issue #31877.
