---
ontology: go-ontology
issue_number: 32005
pr_number: 32026
eval_repo_pr: 127
agent: std_codex_g55
model: gpt-5.5
runtime: codex
agent_config_tag: v9
case_type: obsoletion
difficulty: medium
f1: 0.927
precision: 0.905
recall: 0.95
jaccard: 0.864
outcome: success
failure_modes: []
reviewed_by: codex
reviewed_at: "2026-05-16"
---

<!-- Review this eval run following analysis/instructions/review-agent-eval.md

  Source issue: https://github.com/geneontology/go-ontology/issues/32005
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/32026
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/127
  Agent config: ai4curation/go-ontology-agent-config

  Quick reference:
    gh issue view 32005 --repo geneontology/go-ontology
    gh pr diff 32026 --repo geneontology/go-ontology
    gh pr diff 127 --repo ai4curation/eval-ont-agent-go
-->

## Summary

The agent correctly addressed issue `#32005` by obsoleting `GO:0009095` `aromatic amino acid biosynthetic process, prephenate pathway` and adding the requested `consider` targets `GO:0009094` and `GO:0006571`. The metadiff F1 of 0.927 is a fair reflection of a substantively correct solution with minor provenance/comment differences from the human PR. The main edit is ontologically sound: it removes the pre-composed superpathway term and leaves annotation review outside the ontology diff.


## Strengths

- Correctly renamed `GO:0009095` to `obsolete aromatic amino acid biosynthetic process, prephenate pathway`, prefixed the definition with `OBSOLETE.`, and added `is_obsolete: true`.
- Removed the active logical structure from the obsolete term: the `is_a: GO:0009073` parent and the `intersection_of` axioms involving `GO:0009058`, `CHEBI:57852`, and `CHEBI:33856`.
- Removed active synonyms and the standalone `xref: MetaCyc:PWY-3481`, matching the obsoletion pattern for a term whose external mapping was to the MetaCyc superpathway.
- Added both appropriate `consider` terms from the issue: `GO:0009094` `L-phenylalanine biosynthetic process` and `GO:0006571` `L-tyrosine biosynthetic process`.
- Added a `term_tracker_item` for `https://github.com/geneontology/go-ontology/issues/32005`.
- The agent's PR explanation correctly identified that `MetaCyc:PWY-3481` decomposes into phenylalanine and tyrosine biosynthesis pathways, with `MetaCyc:PWY-3462` and `MetaCyc:PWY-3461` already represented on `GO:0009094` and `GO:0006571`.


## Issues

- Minor provenance difference: the agent retained the older `property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31091"` while the human PR replaced it with only the obsoletion issue `#32005`. This is unlikely to break the ontology, but it leaves extra tracker provenance not present in the reference solution.
- Minor comment-quality difference: the obsolete comment says the term is a combined phenylalanine/tyrosine pathway better represented as GO-CAM, which is correct, but it is less specific than the human PR's comment. The human comment explicitly mentions `MetaCyc:PWY-3481`, constituent pathways `PWY-3462` and `PWY-3461`, their mappings to `GO:0009094` and `GO:0006571`, and annotation transfer guidance.
- No wrong term, syntax error, or substantive missed ontology edit was found.
