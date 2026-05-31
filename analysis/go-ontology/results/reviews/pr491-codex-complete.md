---
ontology: go-ontology
issue_number: 32005
pr_number: 32026
eval_repo_pr: 491
agent: std_claude_son45
model: claude-sonnet-4.5
runtime: claude
agent_config_tag: v9
case_type: obsoletion
difficulty: medium
f1: 0.072
precision: 0.857
recall: 0.038
jaccard: 0.037
outcome: partial_success
failure_modes:
  - over_editing
  - scope_creep
reviewed_by: codex
reviewed_at: "2026-05-16"
---

<!-- Review this eval run following analysis/instructions/review-agent-eval.md

  Source issue: https://github.com/geneontology/go-ontology/issues/32005
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/32026
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/491
  Agent config: ai4curation/go-ontology-agent-config

  Quick reference:
    gh issue view 32005 --repo geneontology/go-ontology
    gh pr diff 32026 --repo geneontology/go-ontology
    gh pr diff 491 --repo ai4curation/eval-ont-agent-go
-->

## Summary

The agent correctly performed the core `GO:0009095` obsoletion requested in issue #32005, including the obsolete label, `OBSOLETE.` definition, removal of active logical axioms, `is_obsolete: true`, and `consider` links to `GO:0009094` and `GO:0006571`. However, the PR is massively over-scoped: the human PR changed only the `GO:0009095` stanza, while this attempt carries a large unrelated diff from many other ontology tickets. The F1 of 0.072 understates the correctness of the target stanza but fairly reflects that the submitted PR as a whole is unsafe.


## Strengths

- Correctly identified `GO:0009095` as the target term and renamed it to `obsolete aromatic amino acid biosynthetic process, prephenate pathway`.
- Correctly prefixed the definition with `OBSOLETE.` and added `is_obsolete: true`.
- Removed the active ontology structure from `GO:0009095`, including `is_a: GO:0009073` and the `intersection_of` axioms using `GO:0009058`, `CHEBI:57852`, and `CHEBI:33856`.
- Added both appropriate `consider` targets: `GO:0009094` `L-phenylalanine biosynthetic process` and `GO:0006571` `L-tyrosine biosynthetic process`.
- Added an obsoletion comment that captures the central rationale: `MetaCyc:PWY-3481` is a superpathway combining phenylalanine and tyrosine biosynthesis rather than a single atomic GO process.
- Retained useful provenance such as `xref: MetaCyc:PWY-3481` and the previous tracker while adding the current issue tracker for #32005.


## Issues

- Major scope creep: the PR contains a large unrelated diff touching many terms outside `GO:0009095`. The human PR for #32005 was a single-stanza obsoletion in `src/ontology/go-edit.obo`.
- The unrelated changes include signal-sequence receptor renames, vesicle tethering relationship rewrites, multiple other obsoletions, enzyme term edits, and support-file changes that belong to separate issues.
- The `GO:0009095` comment is correct but less curator-informative than the human PR's comment, which explicitly names `PWY-3462` and `PWY-3461` and explains their relationship to `GO:0009094` and `GO:0006571`.
- The agent retained the older tracker for issue #31091 in addition to adding #32005, while the human PR kept only the current obsoletion tracker. This is a minor provenance difference, not a biological error.
- The target edit is good enough to count as a partial success, but the PR would need substantial cleanup before it could be accepted for this issue.
