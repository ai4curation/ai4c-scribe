---
ontology: go-ontology
issue_number: 32005
pr_number: 32026
eval_repo_pr: 145
agent: std_opencode_g55
model: gpt-5.5
runtime: opencode
agent_config_tag: v9
case_type: obsoletion
difficulty: medium
f1: 0.927
precision: 0.905
recall: 0.95
jaccard: 0.864
outcome: success
failure_modes: []
reviewed_by: gpt-5.5
reviewed_at: 2026-05-11
---

<!-- Review this eval run following analysis/instructions/review-agent-eval.md

  Source issue: https://github.com/geneontology/go-ontology/issues/32005
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/32026
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/145
  Agent config: ai4curation/go-ontology-agent-config

  Quick reference:
    gh issue view 32005 --repo geneontology/go-ontology
    gh pr diff 32026 --repo geneontology/go-ontology
    gh pr diff 145 --repo ai4curation/eval-ont-agent-go
-->

## Summary

The agent correctly addressed issue `#32005` by obsoleting `GO:0009095` `aromatic amino acid biosynthetic process, prephenate pathway` and adding the two appropriate `consider` targets, `GO:0009094` and `GO:0006571`. The metadiff F1 of 0.927 is a fair reflection of the actual quality: the ontology edit is substantively correct, with only minor differences from the human PR in tracker provenance and the level of detail in the obsolete-term comment.


## Strengths

- Correctly converted `GO:0009095` to an obsolete term by renaming it to `obsolete aromatic amino acid biosynthetic process, prephenate pathway`, prefixing the definition with `OBSOLETE.`, and adding `is_obsolete: true`.
- Removed the active logical structure from the obsolete stanza, including `is_a: GO:0009073` and the `intersection_of` axioms involving `GO:0009058`, `CHEBI:57852`, and `CHEBI:33856`.
- Removed active synonyms and the standalone `xref: MetaCyc:PWY-3481`, matching the expected obsoletion pattern for a term whose xref was to a MetaCyc superpathway.
- Added both requested `consider` terms: `GO:0009094` `L-phenylalanine biosynthetic process` and `GO:0006571` `L-tyrosine biosynthetic process`, rather than incorrectly choosing a single `replaced_by`.
- Added a tracker link for the active obsoletion request, `https://github.com/geneontology/go-ontology/issues/32005`.
- The agent's PR explanation showed good understanding of the issue: it identified `MetaCyc:PWY-3481` as a superpathway composed of `PWY-3462` and `PWY-3461`, already represented as narrow matches on `GO:0009094` and `GO:0006571`.


## Issues

- Minor provenance difference: the agent retained the older `property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31091"` and added `#32005`, whereas the human PR replaced the old tracker item with only `#32005`. This is not a substantive ontology error, but it leaves extra provenance not present in the reference solution.
- Minor comment-quality difference: the agent's obsolete comment correctly says the term is a pre-composed superpathway combining L-phenylalanine and L-tyrosine biosynthesis via prephenate, but it is less informative than the human PR's comment. The human comment explicitly names `MetaCyc:PWY-3481`, `PWY-3462`, `PWY-3461`, their mappings to `GO:0009094` and `GO:0006571`, and advises transfer to the appropriate `consider` term(s).
- No wrong term, syntax error, missing `consider`, or substantive missed ontology edit was found.
