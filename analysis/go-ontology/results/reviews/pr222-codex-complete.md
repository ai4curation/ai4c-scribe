---
ontology: go-ontology
issue_number: 32018
pr_number: 32021
eval_repo_pr: 222
agent: std_codex_g54
model: gpt-5.4
runtime: codex
agent_config_tag: v9
case_type: obsoletion
difficulty: simple
f1: 0.148
precision: 1.0
recall: 0.08
jaccard: 0.08
outcome: success
failure_modes: []
reviewed_by: codex
reviewed_at: "2026-05-16"
---

<!-- Review this eval run following analysis/instructions/review-agent-eval.md

  Source issue: https://github.com/geneontology/go-ontology/issues/32018
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/32021
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/222
  Agent config: ai4curation/go-ontology-agent-config

  Quick reference:
    gh issue view 32018 --repo geneontology/go-ontology
    gh pr diff 32021 --repo geneontology/go-ontology
    gh pr diff 222 --repo ai4curation/eval-ont-agent-go
-->

## Summary

The agent implemented the substantive obsoletion requested in issue #32018: it obsoleted `GO:0052704` and `GO:0140479`, replaced both with `GO:0052699`, moved the two MetaCyc pathway mappings to `GO:0052699` as narrow matches, and removed the two taxon-constraint rows. The human PR #32021 only removed the `only_in_taxon.tsv` rows, so the low metadiff F1 of 0.148 under-represents the issue-level quality of the agent's solution. The agent's ontology edits are mostly well scoped to the issue, with only minor style/scope caveats.

## Strengths

- Correctly obsoleted `GO:0052704` (`ergothioneine biosynthesis from histidine via gamma-glutamyl-hercynylcysteine sulfoxide`) and `GO:0140479` (`ergothioneine biosynthesis from histidine via hercynylcysteine sulfoxide synthase`) with `is_obsolete: true`, obsolete-prefixed names/definitions, and `replaced_by: GO:0052699`.
- Added `MetaCyc:PWY-7255` and `MetaCyc:PWY-7550` to `GO:0052699 ergothioneine biosynthetic process` as `skos:narrowMatch`, matching the issue's requested treatment of variant pathway mappings.
- Included the human PR's concrete cleanup by deleting the `GO:0052704` bacterial-only and `GO:0140479` fungal-only rows from `src/taxon_constraints/only_in_taxon.tsv`.
- Cleaned up internal references to terms being obsoleted: `GO:0044875` and `GO:0061686` were rewired from `part_of` the child pathway terms to `part_of GO:0052699`, and obsolete `GO:0052707` was updated from `replaced_by GO:0052704` to `replaced_by GO:0052699`.
- Added issue tracker provenance for #32018 on the affected ontology terms, which makes the obsoletion rationale traceable.

## Issues

- No major correctness issues relative to the source issue. The agent did much more than the human PR, but those extra ontology edits are directly supported by the issue text rather than being gratuitous scope creep.
- Minor scope/style issue: while obsoleting `GO:0052704`, the agent removed an existing broad synonym and `Wikipedia:Ergothioneine` xref. That cleanup was not requested and may be less useful than retaining historical lookup metadata on the obsolete term.
