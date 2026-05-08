---
repo: obophenotype/cell-ontology
issue_number: 3259
pr_number: 3450
issue_title: "[NTR] tPC-IC cell"
issue_created_at: "2025-08-21"
pr_author: app/copilot-swe-agent
pr_merged_at: "2025-11-21"
pr_num_commits: 7
files_changed:
  - path: src/ontology/cl-edit.owl
    additions: 14
    deletions: 1
scoping: tightly_scoped
task_type: new_term
difficulty: medium
scope: single_term
review_outcome: changes_requested
domain_area: renal
tags:
  - NTR
  - kidney
  - collecting-duct
  - transitional-cell
  - intercalated-cell
curated_by: claude-opus-4
curated_at: "2026-05-08"
rationale: New term for a transitional cell type in kidney collecting duct requiring understanding of principal-intercalated cell plasticity
---

## Context

A new term request was filed for the transitional principal-intercalated cell (tPC-IC), a recently described cell type in the kidney collecting duct that exhibits characteristics of both principal cells and intercalated cells. This cell type represents an intermediate state in the plasticity between these two well-established collecting duct cell populations. The issue had been open since August 2025 as part of ongoing kidney cell type curation.

## Changes Made

Added 14 new lines to `cl-edit.owl` defining the tPC-IC term with a class declaration, rdfs:label, textual definition with literature references, appropriate parentage, and logical axioms linking the cell to UBERON kidney collecting duct structures via part_of relations. One existing line was modified to accommodate the new term in the class hierarchy.

## Resolution

The PR required changes during review before approval and merge, going through 7 commits total. Medium difficulty because modeling a transitional cell state between two existing cell types requires careful consideration of the ontological relationship -- it is not simply a subclass of either parent type but represents a hybrid phenotype that needed appropriate axiomatization.
