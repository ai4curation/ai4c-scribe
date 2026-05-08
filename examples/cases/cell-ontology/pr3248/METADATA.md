---
repo: obophenotype/cell-ontology
issue_number: 3196
pr_number: 3248
issue_title: "[NTR] Unclassified Fallopian Tube Progenitor (UCFP)"
issue_created_at: "2025-07-15"
issue_closed_at: "2025-08-13"
pr_author: Caroline-99
pr_merged_at: "2025-08-13"
pr_num_commits: 5
files_changed:
  - path: src/ontology/cl-edit.owl
    additions: 16
    deletions: 2
scoping: tightly_scoped
task_type: new_term
difficulty: medium
scope: single_term
review_outcome: approved_first_time
domain_area: reproductive-biology
tags:
  - NTR
  - progenitor-cell
  - fallopian-tube
  - reproductive-tract
  - dual-feature
curated_by: claude-opus-4
curated_at: "2026-05-08"
rationale: New term request from external community requiring novel cell type placement with dual-lineage progenitor characteristics
---

## Context

A new term request was submitted by an external contributor for the "unclassified fallopian tube progenitor" (UCFP), a dual-feature progenitor cell found in the fallopian tube that can give rise to both epithelial and stromal lineages. This cell type was identified through single-cell transcriptomic studies of the human fallopian tube.

## Changes Made

Added 16 lines and modified 2 lines in `cl-edit.owl`. The new term includes a class declaration, label, textual definition citing relevant single-cell RNA-seq publications, synonyms, parentage under an appropriate progenitor cell class, and anatomical location assertions linking to fallopian tube structures in UBERON.

## Resolution

Approved on first review. Medium difficulty because placing a novel dual-lineage progenitor cell requires understanding progenitor cell classification patterns, choosing appropriate parent classes when the cell has multi-potent differentiation potential, and correctly asserting anatomical location relationships.
