---
repo: monarch-initiative/mondo
issue_number: 10149
pr_number: 10156
issue_title: "Request for new term [podocytopathy]"
issue_labels:
  - New term request
issue_created_at: "2026-04-14"
pr_author: sabrinatoro
pr_merged_at: "2026-04-15"
pr_num_commits: 1
files_changed:
  - path: src/ontology/mondo-edit.obo
    additions: 17
    deletions: 0
scoping: tightly_scoped
scoping_notes: PR adds a new parent term and reclassifies three existing children under it.
task_type: new_term
difficulty: medium
scope: multiple_terms
review_outcome: approved_first_time
domain_area: kidney-disease
tags:
  - podocytopathy
  - nephrology
  - glomerular-disease
  - hierarchy-grouping
curated_by: claude-opus-4
curated_at: "2026-05-08"
rationale: New grouping term with child reclassification requiring knowledge of renal pathology taxonomy
---

## Context

A request was made for a new term "podocytopathy" to serve as a grouping class for diseases caused by podocyte dysfunction. Podocytes are specialized cells in the kidney glomerulus, and podocytopathies include conditions like minimal change disease and focal segmental glomerulosclerosis. The term was needed to provide a clinically meaningful grouping in the disease hierarchy.

This was a collaborative effort with a domain expert (cws99) who helped define the scope and children of the new term.

## Changes Made

Added the new term "podocytopathy" to `src/ontology/mondo-edit.obo` with 17 lines of additions. The PR created the parent term with a definition and also reclassified three existing disease terms as children of the new grouping class. No lines were deleted, indicating clean additions to the hierarchy.

## Resolution

Medium difficulty because it requires understanding renal pathology well enough to determine which existing Mondo terms should be classified as podocytopathies. The curator needed to create a proper definition and identify the correct children, which requires domain knowledge about glomerular disease classification.
