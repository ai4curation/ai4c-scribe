---
ontology: go-ontology
issue_number: 32005
pr_number: 32026
eval_repo_pr: 223
agent: std_codex_g54
model: gpt-5.4
runtime: codex
agent_config_tag: v9
case_type: obsoletion
difficulty: medium
f1: 0.076
precision: 0.905
recall: 0.04
jaccard: 0.04
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
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/223
  Agent config: ai4curation/go-ontology-agent-config

  Quick reference:
    gh issue view 32005 --repo geneontology/go-ontology
    gh pr diff 32026 --repo geneontology/go-ontology
    gh pr diff 223 --repo ai4curation/eval-ont-agent-go
-->

## Summary

The agent did make the core requested edit for issue `#32005`: it obsoleted `GO:0009095` `aromatic amino acid biosynthetic process, prephenate pathway` and added `consider` links to `GO:0009094` and `GO:0006571`. However, the PR is badly over-scoped: instead of the human PR's single-term `src/ontology/go-edit.obo` change, the agent PR includes a large unrelated diff touching many GO terms, imports, and taxon constraint files. The metadiff F1 of 0.076 is directionally fair for PR-level quality, though it under-represents that the `GO:0009095` stanza itself is mostly correct.


## Strengths

- Correctly identified `GO:0009095` as the term to obsolete and changed its label to `obsolete aromatic amino acid biosynthetic process, prephenate pathway`.
- Correctly prefixed the definition with `OBSOLETE.` and added `is_obsolete: true`.
- Removed the active ontology structure from `GO:0009095`: the `is_a: GO:0009073` parent, the genus `intersection_of: GO:0009058`, and the logical axioms using `CHEBI:57852` prephenate and `CHEBI:33856` aromatic amino acid.
- Removed the active synonyms and the direct `xref: MetaCyc:PWY-3481`, which is appropriate because the issue explains that `PWY-3481` is a combined superpathway rather than a single GO pathway term.
- Added both issue-requested `consider` targets: `GO:0009094` `L-phenylalanine biosynthetic process` and `GO:0006571` `L-tyrosine biosynthetic process`.
- Added a tracker link for the active obsoletion request, `https://github.com/geneontology/go-ontology/issues/32005`.


## Issues

- Major scope creep: the agent PR includes a 1654-line diff across `src/ontology/go-edit.obo`, `src/ontology/imports/go-catalytic-activities-participants.owl`, `src/ontology/imports/go_taxon_constraints.owl`, `src/taxon_constraints/only_in_taxon.ofn`, and `src/taxon_constraints/only_in_taxon.tsv`. The human PR for this issue changed only the `GO:0009095` stanza.
- The unrelated ontology edits are extensive and not justified by issue `#32005`. Examples include obsoleting `GO:0003400`, `GO:0008785`, `GO:0008875`, `GO:0009255`, `GO:0018581`, `GO:0045550`, `GO:0099022`, `GO:0099041`, `GO:0099044`, and `GO:0099069`; renaming/reparenting signal-sequence terms such as `GO:0005048`, `GO:0000268`, `GO:0030941`, and `GO:0045048`; adding new terms such as `GO:0140419` and `GO:7770069`; and changing taxon constraints for terms such as `GO:0052704`, `GO:0140479`, `GO:0000956`, and `GO:0141065`.
- The obsolete comment for `GO:0009095` is much less informative than the human PR's comment. It says only that the term "represents a GO-CAM model"; the issue/human solution specifically explains that `MetaCyc:PWY-3481` is the superpathway of L-phenylalanine and L-tyrosine biosynthesis, decomposing into `PWY-3462` and `PWY-3461`, already represented as narrow matches on `GO:0009094` and `GO:0006571`.
- Minor provenance difference: the agent retained the old `term_tracker_item` for issue `#31091` and added `#32005`, whereas the human PR replaced the old tracker metadata with the current obsoletion issue only.
- No wrong target term or obvious syntax error was found in the `GO:0009095` obsoletion itself, but the PR as a whole would not be acceptable without removing the unrelated edits.
