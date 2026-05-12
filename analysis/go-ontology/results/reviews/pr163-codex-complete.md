---
ontology: go-ontology
issue_number: 32005
pr_number: 32026
eval_repo_pr: 163
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
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/163
  Agent config: ai4curation/go-ontology-agent-config

  Quick reference:
    gh issue view 32005 --repo geneontology/go-ontology
    gh pr diff 32026 --repo geneontology/go-ontology
    gh pr diff 163 --repo ai4curation/eval-ont-agent-go
-->

## Summary

The agent successfully implemented the requested obsoletion of `GO:0009095` aromatic amino acid biosynthetic process, prephenate pathway. It made the same core ontology changes as the human PR: obsolete label, `OBSOLETE.` definition prefix, removal of active synonyms/xref/classification/logical axioms, `is_obsolete: true`, and `consider` links to `GO:0009094` L-phenylalanine biosynthetic process and `GO:0006571` L-tyrosine biosynthetic process. The metadiff F1 of 0.927 is a fair high score; the remaining differences are mostly comment detail and the agent retaining an older tracker link.


## Strengths

- Correctly identified `GO:0009095` as the term to obsolete and captured the issue rationale: `MetaCyc:PWY-3481` is a combined superpathway for L-phenylalanine and L-tyrosine biosynthesis rather than a single GO process term.
- Added the right obsoletion migration metadata: `consider: GO:0009094` and `consider: GO:0006571`, matching the issue request and the human PR.
- Applied the standard GO obsoletion pattern by renaming the term to `obsolete aromatic amino acid biosynthetic process, prephenate pathway`, prefixing the definition with `OBSOLETE.`, and adding `is_obsolete: true`.
- Removed the active ontology content that should not remain on an obsolete term: the asserted parent `is_a: GO:0009073`, the `intersection_of` axioms involving `GO:0009058`, `CHEBI:57852`, and `CHEBI:33856`, the exact synonyms, and the direct `xref: MetaCyc:PWY-3481`.
- Added a new `term_tracker_item` for `https://github.com/geneontology/go-ontology/issues/32005`.
- Kept the edit scoped to the `GO:0009095` stanza in `src/ontology/go-edit.obo`, with no unrelated ontology changes.


## Issues

- Minor metadata difference: the agent retained the pre-existing `property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31091" xsd:anyURI` and added `#32005` as a second tracker item, whereas the human PR replaced the tracker metadata with only issue `#32005`. This is unlikely to break ontology behavior, but it leaves stale curator-facing metadata compared with the accepted edit.
- Minor style/completeness difference: the agent's obsoletion comment only says the term is a pre-composed superpathway combining L-phenylalanine and L-tyrosine biosynthesis via prephenate. The human PR's comment is more useful because it explicitly records that `MetaCyc:PWY-3481` decomposes into `PWY-3462` and `PWY-3461`, already represented as narrowMatch xrefs on `GO:0009094` and `GO:0006571`, and tells annotators to transfer annotations to the appropriate consider term(s).
