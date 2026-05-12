---
ontology: go-ontology
issue_number: 31877
pr_number: 31973
eval_repo_pr: 185
agent: std_codex_g54
model: gpt-5.4
runtime: codex
agent_config_tag: v9
case_type: obsoletion
difficulty: hard
f1: 0.54
precision: 0.464
recall: 0.647
jaccard: 0.37
outcome: partial_success
failure_modes:
  - over_editing
  - scope_creep
reviewed_by: gpt-5.5
reviewed_at: 2026-05-11
---

<!-- Review this eval run following analysis/instructions/review-agent-eval.md

  Source issue: https://github.com/geneontology/go-ontology/issues/31877
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/31973
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/185
  Agent config: ai4curation/go-ontology-agent-config

  Quick reference:
    gh issue view 31877 --repo geneontology/go-ontology
    gh pr diff 31973 --repo geneontology/go-ontology
    gh pr diff 185 --repo ai4curation/eval-ont-agent-go
-->

## Summary

The agent correctly obsoleted `GO:0010381` "peroxisome-chloroplast membrane tethering" and pointed users to `GO:7770065` "peroxisome-chloroplast membrane tether activity" with `consider`, matching the main intent of issue #31877 and the human PR. The metadiff F1 of 0.54 is directionally fair but needs interpretation: much of the mismatch comes from generated taxon-constraint OWL churn, but there is also a real semantic difference because the agent moved the old `never_in_taxon` constraints onto `GO:7770065` while the human solution simply removed them from the obsolete term.


## Strengths

- Correctly applied the standard obsoletion pattern for `GO:0010381`: renamed it to `obsolete peroxisome-chloroplast membrane tethering`, prefixed the definition with `OBSOLETE.`, added `is_obsolete: true`, added the issue tracker property for #31877, removed the asserted parent `is_a: GO:0140056`, and removed the exact synonym `attachment of peroxisome to chloroplast`.
- Used `consider: GO:7770065` rather than `replaced_by`, which is appropriate for redirecting a biological process term to a molecular function term where annotation migration should be curated rather than automatic.
- Removed all taxon-constraint references from the obsolete `GO:0010381` term itself, including the four `never_in_taxon.tsv` rows for `NCBITaxon:28009`, `NCBITaxon:33208`, `NCBITaxon:4751`, and `NCBITaxon:554915`, plus the corresponding OFN and generated OWL assertions.
- The obsoletion comment accurately captures the reason for obsoletion: the old BP term represented a molecular function rather than a biological process.


## Issues

- The agent over-edited the taxon constraints by reassigning the four removed `GO:0010381` constraints to `GO:7770065` in `src/taxon_constraints/never_in_taxon.tsv`, `never_in_taxon.ofn`, and `go_taxon_constraints.owl`. The human PR deleted those constraints outright; the issue and curator follow-up required removing constraints from the obsolete term, not adding new constraints to the replacement MF term.
- That reassignment is biologically plausible but not justified by the source issue or human PR. Adding `never_in_taxon` constraints for `GO:7770065` against Choanoflagellida, Metazoa, Fungi, and Amoebozoa changes the logical constraints on a different, non-obsolete term and would deserve separate curator review.
- The generated `go_taxon_constraints.owl` diff does not match the human regeneration. Some non-task differences in the human PR, such as generated updates around `GO:0000956`, `GO:0140494`, and `GO:0141065`, are not required for solving #31877, but the agent's added `GO_7770065` block is a substantive extra change rather than harmless serialization drift.
