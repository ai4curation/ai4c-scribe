---
repo: obophenotype/cell-ontology
issue_number: 3252
pr_number: 3253
issue_title: "[NTR] quiescent fibroblast"
issue_created_at: "2025-08-13"
issue_closed_at: "2025-09-04"
pr_author: Caroline-99
pr_merged_at: "2025-09-04"
pr_num_commits: 5
files_changed:
  - path: src/ontology/cl-edit.owl
    additions: 11
    deletions: 0
scoping: tightly_scoped
task_type: new_term
difficulty: medium
scope: single_term
review_outcome: approved_first_time
domain_area: connective-tissue
tags:
  - fibroblast
  - quiescence
  - NTR
  - cell-state
curated_by: claude-opus-4
curated_at: "2026-05-08"
rationale: New term request requiring reasoning about cell state vs cell type and proper placement in the fibroblast hierarchy
---

## Context

A new term request was filed for "quiescent fibroblast" as part of a broader effort to improve the fibroblast branch of the cell ontology (tracked in issue #2097). Quiescent fibroblasts are fibroblasts in a reversible G0 cell cycle arrest state, distinct from senescent fibroblasts. This is part of a larger initiative to add cell-state-qualified fibroblast subtypes.

## Changes Made

Added 11 new lines to `cl-edit.owl` defining the quiescent fibroblast term. This includes the class declaration, label, textual definition with literature references, parentage under fibroblast, and any relevant logical axioms linking the cell to its quiescent state via Gene Ontology biological process terms.

## Resolution

Approved on first review. Medium difficulty because creating a cell-state-qualified term requires understanding the distinction between cell states and cell types in ontology modeling, choosing appropriate GO terms for the quiescent state, and correctly structuring the logical definition.
