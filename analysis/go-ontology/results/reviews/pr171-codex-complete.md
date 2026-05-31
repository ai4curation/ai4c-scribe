---
ontology: go-ontology
issue_number: 32018
pr_number: 32021
eval_repo_pr: 171
agent: std_opencode_g55
model: gpt-5.5
runtime: opencode
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
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/171
  Agent config: ai4curation/go-ontology-agent-config

  Quick reference:
    gh issue view 32018 --repo geneontology/go-ontology
    gh pr diff 32021 --repo geneontology/go-ontology
    gh pr diff 171 --repo ai4curation/eval-ont-agent-go
-->

## Summary

The agent made a broad obsoletion-oriented edit for the ergothioneine pathway variants: it obsoleted `GO:0052704` and `GO:0140479`, replaced both with `GO:0052699`, moved the two MetaCyc pathway mappings to the parent as narrow matches, and rewired several internal references. That is biologically aligned with the issue text, so the F1=0.0 under-represents some real useful work, but it still misses the actual human PR change: deleting the two `src/taxon_constraints/only_in_taxon.tsv` rows.

The main problem is durability and scope. The agent removed taxon constraints from generated/derived artifacts, but left the source TSV unchanged, while also adding a much larger ontology edit than the human reviewed solution.


## Strengths

- Correctly identified the two child pathway-variant terms named in the issue, `GO:0052704` and `GO:0140479`, as obsolete candidates.
- Used the intended replacement target, `GO:0052699` `ergothioneine biosynthetic process`, adding `replaced_by: GO:0052699` to both obsoleted terms and removing their active `is_a` links.
- Added the requested pathway-specific MetaCyc mappings to the retained parent as narrow matches: `MetaCyc:PWY-7255` and `MetaCyc:PWY-7550` on `GO:0052699`.
- Rewired internal molecular-function process links away from the obsolete terms: `GO:0044875` now points to `GO:0052699` instead of `GO:0052704`, and `GO:0061686` now points to `GO:0052699` instead of `GO:0140479`.
- Noticed related stale references to `GO:0052704`, including the `GO:0052707` `replaced_by` target and comments on `GO:0052707`/`GO:0052711`.


## Issues

- Missed the exact durable source edit made by the human PR: removing the `GO:0052704` bacteria-only row (`NCBITaxon:2`) and the `GO:0140479` fungi-only row (`NCBITaxon:4751`) from `src/taxon_constraints/only_in_taxon.tsv`.
- Removed those taxon constraints only from generated/derived files (`src/taxon_constraints/only_in_taxon.ofn` and `src/ontology/imports/go_taxon_constraints.owl`). Because `only_in_taxon.tsv` remains unchanged, regeneration would likely restore the constraints.
- Compared with the human PR, the patch is substantially over-expanded. The obsoletion and MetaCyc xref work is defensible from issue #32018, but it diverges from the reviewed human solution, which only updated taxon-constraint source data.
- The agent deleted existing metadata from `GO:0052704`, including the broad synonym for N-alpha,N-alpha,N-alpha-trimethyl-L-histidine and the `Wikipedia:Ergothioneine` xref. That may be acceptable during obsoletion, but it was not explicitly requested and discards search/mapping metadata.
