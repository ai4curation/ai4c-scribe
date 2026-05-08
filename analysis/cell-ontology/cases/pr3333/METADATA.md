---
repo: obophenotype/cell-ontology
issue_number: 3332
pr_number: 3333
issue_title: "Re-labelling of imported annotation properties in the -edit file"
issue_created_at: "2025-09-16"
issue_closed_at: "2025-09-17"
pr_author: gouttegd
pr_merged_at: "2025-09-17"
pr_num_commits: 4
files_changed:
  - path: src/ontology/cl-edit.owl
    additions: 32
    deletions: 92
scoping: mostly_scoped
scoping_notes: >-
  Primarily removes redundant labels but also adds SPARQL-based annotations to prevent
  future regressions, which goes slightly beyond the original issue scope.
task_type: bulk_edit
difficulty: medium
scope: multi_term
review_outcome: approved_first_time
domain_area: ontology-maintenance
tags:
  - annotation-properties
  - import-management
  - SPARQL
  - cleanup
  - regression-prevention
curated_by: claude-opus-4
curated_at: "2026-05-08"
rationale: Large-scale cleanup with net 60-line reduction plus preventive measures, demonstrating ontology import hygiene
---

## Context

The cell ontology edit file had accumulated many redundant `rdfs:label` annotations for annotation properties that are already labeled in the imported modules (e.g., oboInOwl properties, IAO properties). These redundant labels cause confusion for contributors who may think they need to maintain them, and can mask the canonical labels from imports.

## Changes Made

Removed 92 lines of redundant annotation property labels from `cl-edit.owl` and added 32 lines of replacement content including SPARQL-based annotations to help detect future re-introduction of these labels. The net effect is a 60-line reduction in the edit file.

## Resolution

Approved on first review despite a dismissed review comment. Medium difficulty because the change requires understanding the OWL import chain to identify which labels are redundant versus essential, and adding preventive measures requires knowledge of SPARQL-based quality checking in OBO ontology workflows.
