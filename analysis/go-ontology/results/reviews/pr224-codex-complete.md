---
ontology: go-ontology
issue_number: 32005
pr_number: 32026
eval_repo_pr: 224
agent: std_claude_hai45
model: claude-haiku-4.5
runtime: claude
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
reviewed_by: codex
reviewed_at: "2026-05-16"
---

<!-- Review this eval run following analysis/instructions/review-agent-eval.md

  Source issue: https://github.com/geneontology/go-ontology/issues/32005
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/32026
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/224
  Agent config: ai4curation/go-ontology-agent-config

  Quick reference:
    gh issue view 32005 --repo geneontology/go-ontology
    gh pr diff 32026 --repo geneontology/go-ontology
    gh pr diff 224 --repo ai4curation/eval-ont-agent-go
-->

## Summary

The agent correctly performed the core obsoletion requested for `GO:0009095` (`aromatic amino acid biosynthetic process, prephenate pathway`): it made the term obsolete and pointed users to `GO:0009094` and `GO:0006571`. However, the PR is massively over-scoped compared with the human PR, which only changed the `GO:0009095` stanza. The metadiff F1 of 0.08 is low because the agent PR contains a large unrelated diff; it under-represents the quality of the target `GO:0009095` edit but fairly flags the PR-level scope problem.


## Strengths

- Correctly identified `GO:0009095` as the term to obsolete and changed its label to `obsolete aromatic amino acid biosynthetic process, prephenate pathway`.
- Correctly prefixed the definition with `OBSOLETE.` and added `is_obsolete: true`.
- Removed the active ontology structure from `GO:0009095`, including `is_a: GO:0009073`, `intersection_of: GO:0009058`, `has_intermediate CHEBI:57852`, and `has_primary_output CHEBI:33856`.
- Removed the active synonyms and direct `xref: MetaCyc:PWY-3481`, consistent with the issue's explanation that `PWY-3481` is a superpathway rather than a single GO pathway term.
- Added both requested `consider` targets: `GO:0009094` (`L-phenylalanine biosynthetic process`) and `GO:0006571` (`L-tyrosine biosynthetic process`).
- Added a useful obsoletion comment explaining that `MetaCyc:PWY-3481` combines `PWY-3462` and `PWY-3461`, and added the current tracker link for issue `#32005`.


## Issues

- Major scope creep: the agent PR is a 1654-line diff touching `src/ontology/go-edit.obo`, generated import files, and taxon constraint files. The human PR for issue `#32005` changed only the `GO:0009095` stanza in `src/ontology/go-edit.obo`.
- The unrelated edits are extensive and not justified by the issue. Examples include obsoleting or changing terms from other tickets such as `GO:0003400`, `GO:0008785`, `GO:0008875`, `GO:0009255`, `GO:0018581`, `GO:0045550`, `GO:0099022`, `GO:0099041`, and `GO:0099069`; renaming signal-sequence terms such as `GO:0005048`, `GO:0000268`, `GO:0030941`, and `GO:0045048`; and adding new terms `GO:0140419` and `GO:7770069`.
- The PR also changes taxon constraint files unrelated to `GO:0009095`, including removals for `GO:0052704` and `GO:0140479` and additions for `GO:0000956` and `GO:0141065`. Those changes make the submitted PR unsuitable even though the target obsoletion is mostly right.
- Minor style difference: the agent's `consider` lines include inline labels (`! L-phenylalanine biosynthetic process`, `! L-tyrosine biosynthetic process`), while the human PR used bare IDs. This is not a substantive correctness problem, but it differs from the accepted patch.
- No wrong target term or obvious syntax error was found in the `GO:0009095` edit itself; the main failure is bundling many unrelated ontology edits into the evaluation PR.
