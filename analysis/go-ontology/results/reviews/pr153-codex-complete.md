---
ontology: go-ontology
issue_number: 32018
pr_number: 32021
eval_repo_pr: 153
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
  - under_editing
  - missed_requirement
  - wrong_pattern
reviewed_by: codex
reviewed_at: "2026-05-16"
---

<!-- Review this eval run following analysis/instructions/review-agent-eval.md

  Source issue: https://github.com/geneontology/go-ontology/issues/32018
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/32021
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/153
  Agent config: ai4curation/go-ontology-agent-config

  Quick reference:
    gh issue view 32018 --repo geneontology/go-ontology
    gh pr diff 32021 --repo geneontology/go-ontology
    gh pr diff 153 --repo ai4curation/eval-ont-agent-go
-->

## Summary

The agent made a biologically plausible obsoletion-oriented solution for the ergothioneine pathway-variant terms `GO:0052704` and `GO:0140479`, including replacement by `GO:0052699` and MetaCyc narrow mappings on the parent. However, it missed the only source-file change in the human PR: removing the two `only_in_taxon.tsv` rows for `GO:0052704` and `GO:0140479`. The metadiff F1=0.0 is harsh because the agent did useful ontology work requested by the issue text, but it correctly flags that the agent did not match the curated PR and left the durable taxon-constraint source unchanged.


## Strengths

- Correctly identified the two pathway-variant biological process terms named in the issue, `GO:0052704` and `GO:0140479`, as the terms to obsolete.
- Used the intended replacement target, `GO:0052699` `ergothioneine biosynthetic process`, for both obsolete terms.
- Added the two MetaCyc pathway mappings requested in the issue to the retained parent `GO:0052699` as narrow mappings: `MetaCyc:PWY-7255` and `MetaCyc:PWY-7550`.
- Removed active hierarchy from the obsolete stanzas in `go-edit.obo` by dropping the `is_a: GO:0052699` assertions on `GO:0052704` and `GO:0140479`.
- Rewired affected molecular function `part_of` links away from newly obsolete process terms: `GO:0044875` now points to `GO:0052699` instead of `GO:0052704`, and `GO:0061686` now points to `GO:0052699` instead of `GO:0140479`.
- Noticed dependent obsolete-term metadata that referenced `GO:0052704`, updating `GO:0052707` and the comment on `GO:0052711` so they no longer direct users toward the newly obsolete pathway variant.


## Issues

- The agent missed the human PR's actual source edit in `src/taxon_constraints/only_in_taxon.tsv`: deleting the `GO:0052704` bacteria-only row and the `GO:0140479` fungi-only row. This is the key reason the diff has F1=0.0.
- Instead of updating the source TSV, the agent removed `GO:0052704` and `GO:0140479` constraints directly from generated taxon-constraint artifacts (`src/taxon_constraints/only_in_taxon.ofn` and `src/ontology/imports/go_taxon_constraints.owl`). Because the TSV source remains unchanged, those generated deletions are not durable and may be regenerated back.
- The agent edited several generated or derivative ontology files (`comments.txt`, `ec.obo`, `ec_in_xref.txt`, taxon-constraint OFN/OWL) in addition to `go-edit.obo`. Some derivative updates mirror real consequences of obsoleting the terms, but the pattern is risky when the corresponding source files are not all updated.
- Compared with the human PR, the agent substantially over-expanded the patch. This extra ontology work is defensible from the issue text, which explicitly proposed obsoleting `GO:0052704` and `GO:0140479`, but it diverges from the reviewed human solution and introduces more maintenance surface.
