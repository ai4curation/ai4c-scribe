---
ontology: go-ontology
issue_number: 31670
pr_number: 31676
eval_repo_pr: 64
agent: std_codex_g55
model: gpt-5.5
runtime: codex
agent_config_tag: v9
case_type: new_term
difficulty: hard
f1: 0.005
precision: 0.4
recall: 0.002
jaccard: 0.002
outcome: partial_success
failure_modes:
  - over_editing
  - under_editing
  - scope_creep
reviewed_by: codex
reviewed_at: "2026-05-16"
---

<!-- Review this eval run following analysis/instructions/review-agent-eval.md

  Source issue: https://github.com/geneontology/go-ontology/issues/31670
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/31676
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/64
  Agent config: ai4curation/go-ontology-agent-config

  Quick reference:
    gh issue view 31670 --repo geneontology/go-ontology
    gh pr diff 31676 --repo geneontology/go-ontology
    gh pr diff 64 --repo ai4curation/eval-ont-agent-go
-->

## Summary

The agent addressed the core taxon-constraint request by adding Eukaryota-only constraints for `GO:0000956` nuclear-transcribed mRNA catabolic process and `GO:0141065` maternal mRNA clearance, which is the same broad strategy the human PR used to cover the reported bacterial `GO:0070478` NMD annotation problem. The metadiff F1 of 0.005 substantially under-represents the biological correctness of the core edit because most of the mismatch comes from regenerated derived files and blank-node churn, but the agent still missed one human source-file cleanup and produced a much noisier PR than necessary.


## Strengths

- Correctly recognized that a broad `only_in_taxon: NCBITaxon:2759` Eukaryota constraint on `GO:0000956` is an appropriate way to cover the reported `GO:0070478` nuclear-transcribed mRNA 3'-5' exonucleolytic nonsense-mediated decay issue without adding a narrower child-only constraint.
- Correctly added `GO:0141065` maternal mRNA clearance as Eukaryota-only, matching one of the human PR's substantive added constraints for related mRNA clearance biology.
- Did not add a direct `never_in_taxon: NCBITaxon:2` Bacteria constraint for `GO:0070478`; although the issue asked for "never in taxon: 2", the human solution also used broader Eukaryota-only constraints, so the agent's modeling choice is defensible.
- The final eval branch already had `GO:0000958` mitochondrial mRNA catabolic process constrained to Eukaryota, and the agent noticed this rather than duplicating the row.


## Issues

- The agent did not reproduce the human PR's `GO:0140494` migrasome repair in `src/taxon_constraints/only_in_taxon.tsv`. The human changed a malformed/incorrect row from `NCBITaxon:7742` with an embedded `Eukaryota  PMID:40712579` source field to a clean `NCBITaxon:2759` Eukaryota row with `PMID:40712579|PMID:25342562`; the agent left the bad Vertebrata/malformed-source constraint in place.
- The human PR added `GO:0000958` as an explicit source-file edit. The agent did not add it in its diff because it was already present in the eval base, so this is not a final-state biological error, but it does mean the agent PR is not fully comparable to the human source edit.
- The agent committed regenerated `src/taxon_constraints/only_in_taxon.ofn` and `src/ontology/imports/go_taxon_constraints.owl`, causing hundreds of unrelated blank-node ID changes. The human PR touched only `src/taxon_constraints/only_in_taxon.tsv`, and its CI reported "Ontologies are identical"; the generated artifact churn is unnecessary scope creep and makes the PR much harder to review.
