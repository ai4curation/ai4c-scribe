---
ontology: go-ontology
issue_number: 31670
pr_number: 31676
eval_repo_pr: 177
agent: std_codex_g54
model: gpt-5.4
runtime: codex
agent_config_tag: v9
case_type: new_term
difficulty: hard
f1: 0.571
precision: 0.4
recall: 1.0
jaccard: 0.4
outcome: success
failure_modes: []
reviewed_by: gpt-5.5
reviewed_at: 2026-05-11
---

<!-- Review this eval run following analysis/instructions/review-agent-eval.md

  Source issue: https://github.com/geneontology/go-ontology/issues/31670
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/31676
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/177
  Agent config: ai4curation/go-ontology-agent-config

  Quick reference:
    gh issue view 31670 --repo geneontology/go-ontology
    gh pr diff 31676 --repo geneontology/go-ontology
    gh pr diff 177 --repo ai4curation/eval-ont-agent-go
-->

## Summary

The agent correctly addressed the biological intent of issue #31670 by adding Eukaryota-only taxon constraints for `GO:0000956` nuclear-transcribed mRNA catabolic process and `GO:0141065` maternal mRNA clearance. The metadiff score is modest (F1 0.571, precision 0.4, recall 1.0), but it under-represents the quality: the agent placed constraints near related existing rows and did not duplicate `GO:0000958`, which was already constrained in its baseline. The only real difference from the merged human PR is that the agent did not fix an incidental malformed `GO:0140494` migrasome row.


## Strengths

- Added `GO:0000956` as `only_in_taxon NCBITaxon:2759` Eukaryota, which is the right parent-level fix for the reported bacterial annotations to descendant `GO:0070478` nuclear-transcribed mRNA catabolic process, 3'-5' exonucleolytic nonsense-mediated decay.
- Added `GO:0141065` maternal mRNA clearance as Eukaryota-only, matching the human PR and covering another related mRNA decay process that should not apply to bacteria.
- Correctly recognized that the requester asked for `never_in_taxon: 2` Bacteria, but the accepted GO pattern here is to use the broader positive constraint `only_in_taxon NCBITaxon:2759` Eukaryota.
- Did not add a second `GO:0000958` mitochondrial mRNA catabolic process row when its baseline already contained `GO:0000958` constrained to Eukaryota. This is more disciplined than blindly matching the human diff.
- Kept the edit scoped to `src/taxon_constraints/only_in_taxon.tsv` and reported validation plus term lookup in the PR description.


## Issues

- The agent did not make the incidental formatting cleanup for `GO:0140494` migrasome, where the human PR removed an erroneous extra `NCBITaxon:7742` column and normalized the PMID evidence column. This was not part of issue #31670's mRNA decay request, but it was part of the merged human solution and review discussion.
- The PR did not add a direct constraint to `GO:0070478`; it relied on the parent `GO:0000956` constraint being inherited. That matches the human solution and is ontologically preferable, but the PR text could have been clearer that `GO:0070478` is handled through inheritance rather than by a direct row.
