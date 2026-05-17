---
ontology: go-ontology
issue_number: 32018
pr_number: 32021
eval_repo_pr: 138
agent: std_codex_g55
model: gpt-5.5
runtime: codex
agent_config_tag: v9
case_type: obsoletion
difficulty: simple
f1: 0.0
precision: 0.0
recall: 0.0
jaccard: 0.0
outcome: partial_success
failure_modes:
  - missed_requirement
  - wrong_pattern
  - over_editing
reviewed_by: codex
reviewed_at: "2026-05-16"
---

<!-- Review this eval run following analysis/instructions/review-agent-eval.md

  Source issue: https://github.com/geneontology/go-ontology/issues/32018
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/32021
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/138
  Agent config: ai4curation/go-ontology-agent-config

  Quick reference:
    gh issue view 32018 --repo geneontology/go-ontology
    gh pr diff 32021 --repo geneontology/go-ontology
    gh pr diff 138 --repo ai4curation/eval-ont-agent-go
-->

## Summary

The agent made a broad ontology-editing solution for issue #32018: it obsoleted `GO:0052704` and `GO:0140479`, replaced them with `GO:0052699`, moved the MetaCyc pathway xrefs to `GO:0052699` as narrow matches, and adjusted related `part_of` links. That is much closer to the issue-level obsoletion request than the F1=0.0 suggests, but it does not reproduce the human PR's actual source change: deleting the two rows from `src/taxon_constraints/only_in_taxon.tsv`. The missing TSV edit is significant because the agent instead changed generated taxon-constraint artifacts, so the human PR's cleanup would not survive regeneration.

## Strengths

- Correctly targeted the two requested variant pathway terms: `GO:0052704` (ergothioneine biosynthesis via gamma-glutamyl-hercynylcysteine sulfoxide) and `GO:0140479` (ergothioneine biosynthesis via hercynylcysteine sulfoxide synthase).
- Applied a plausible GO obsoletion pattern to both target terms: prefixed the names with `obsolete`, added `OBSOLETE.` definitions, added obsoletion comments, set `is_obsolete: true`, and added `replaced_by: GO:0052699`.
- Added the requested MetaCyc pathway mappings `MetaCyc:PWY-7255` and `MetaCyc:PWY-7550` to the parent `GO:0052699` as `skos:narrowMatch`, matching the issue's recommendation that the variant pathways are too specific for GO terms.
- Repaired some dependent ontology references that would otherwise point at obsolete terms, including changing enzymatic activity `part_of` links from `GO:0052704`/`GO:0140479` to `GO:0052699`.
- Updated already-obsolete related terms such as `GO:0052707` and `GO:0052711` so their comments or replacements no longer depend on `GO:0052704`.

## Issues

- Missed the exact source edit made by the human PR: it did not remove the two `src/taxon_constraints/only_in_taxon.tsv` rows for `GO:0052704` restricted to `NCBITaxon:2` Bacteria and `GO:0140479` restricted to `NCBITaxon:4751` Fungi.
- Edited generated taxon-constraint outputs (`src/ontology/imports/go_taxon_constraints.owl` and `src/taxon_constraints/only_in_taxon.ofn`) instead of the source TSV. Because `only_in_taxon.tsv` remains unchanged, those generated deletions are likely non-durable and would be reintroduced by the normal build.
- The diff overreaches relative to the human cleanup PR, which only removed taxon constraints. The broader obsoletion edits are defensible from the issue text, but they were not part of the merged human solution being evaluated here.
- The agent removed existing metadata from `GO:0052704`, including the broad synonym for N-alpha,N-alpha,N-alpha-trimethyl-L-histidine and the `Wikipedia:Ergothioneine` xref, without a clear requirement. That may be acceptable for an obsolete term, but it is an unnecessary extra change and could discard useful search metadata.
