---
ontology: go-ontology
issue_number: 32005
pr_number: 32026
eval_repo_pr: 291
agent: std_opencode_kimi
model: kimi-k2.6
runtime: opencode
agent_config_tag: v9
case_type: obsoletion
difficulty: medium
f1: 0.08
precision: 0.952
recall: 0.042
jaccard: 0.042
outcome: partial_success
failure_modes:
  - over_editing
  - scope_creep
reviewed_by: gpt-5.5
reviewed_at: 2026-05-16
---

<!-- Review this eval run following analysis/instructions/review-agent-eval.md

  Source issue: https://github.com/geneontology/go-ontology/issues/32005
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/32026
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/291
  Agent config: ai4curation/go-ontology-agent-config

  Quick reference:
    gh issue view 32005 --repo geneontology/go-ontology
    gh pr diff 32026 --repo geneontology/go-ontology
    gh pr diff 291 --repo ai4curation/eval-ont-agent-go
-->

## Summary

The agent correctly obsoleted the target term `GO:0009095` and added the two expected `consider` targets, so the core biological edit is present. Like several other attempts on this case, though, the submitted PR includes a very large unrelated ontology diff rather than the human PR's focused single-stanza change. The metadiff F1 of 0.08 is low because of that severe scope problem, not because the `GO:0009095` stanza itself is mostly wrong.


## Strengths

- Correctly changed the target label to `obsolete aromatic amino acid biosynthetic process, prephenate pathway`.
- Correctly prefixed the definition with `OBSOLETE.` and added `is_obsolete: true`.
- Removed the active synonyms, `xref: MetaCyc:PWY-3481`, `is_a: GO:0009073`, and the logical `intersection_of` axioms from the obsolete term.
- Added both issue-appropriate `consider` targets: `GO:0009094` `L-phenylalanine biosynthetic process` and `GO:0006571` `L-tyrosine biosynthetic process`.
- Added a current `term_tracker_item` for issue #32005.
- The obsoletion comment correctly states that `MetaCyc:PWY-3481` is a superpathway combining L-phenylalanine and L-tyrosine biosynthesis, which should be represented by separate GO terms or GO-CAM modeling.


## Issues

- Major scope creep: this is not a focused `GO:0009095` obsoletion PR. The diff contains extensive unrelated edits across `go-edit.obo` and generated/support files.
- The unrelated edits cover many independent tickets, including signal-sequence receptor renames, vesicle tethering relationship updates, other enzyme obsoletions, new terms, and taxon-constraint changes. Those changes are not justified by issue #32005.
- The obsolete comment is less complete than the human PR's comment. It explains the superpathway problem, but it does not explicitly connect `PWY-3462` to `GO:0009094` and `PWY-3461` to `GO:0006571` as the accepted PR does.
- The inline labels on `consider` lines are acceptable OBO style, but they differ from the bare-ID form in the human diff.
- The target stanza is a reasonable partial solution, but the PR-level output is not mergeable without removing the unrelated changes.
