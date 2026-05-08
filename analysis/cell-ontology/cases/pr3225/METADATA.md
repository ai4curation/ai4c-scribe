---
repo: obophenotype/cell-ontology
issue_number: 3224
pr_number: 3225
issue_title: "[Typo/Bug] Obsoleting terms affected by skos:prefLabel import from MBAO"
issue_created_at: "2025-08-04"
pr_author: Caroline-99
pr_merged_at: "2025-08-07"
pr_num_commits: 2
files_changed:
  - path: src/ontology/cl-edit.owl
    additions: 9
    deletions: 7
scoping: tightly_scoped
task_type: obsoletion
difficulty: medium
scope: multi_term
review_outcome: approved_first_time
domain_area: ontology-maintenance
tags:
  - obsoletion
  - skos-prefLabel
  - MBAO
  - import-artifact
  - structural-cell
curated_by: claude-opus-4
curated_at: "2026-05-08"
rationale: Obsoletion case involving terms inadvertently affected by cross-ontology import artifacts
---

## Context

Terms in the cell ontology were incorrectly affected by a `skos:prefLabel` import from the Molecular Biology Abstract Ontology (MBAO). This introduced erroneous label annotations that needed to be cleaned up. The affected terms, including "structural cell," needed to be obsoleted since they were artifacts of the import rather than intentional term additions.

## Changes Made

Modified `cl-edit.owl` with 9 additions and 7 deletions. The changes involve adding obsoletion annotations (deprecated status, obsoletion reason, replacement term pointers) while removing the incorrect active-term assertions. This follows the standard OBO obsoletion pattern.

## Resolution

Approved on first review. Medium difficulty because obsoletion requires following a specific protocol: marking the term as deprecated, providing a reason for obsoletion, suggesting replacement terms where applicable, and ensuring no other terms have dangling references to the obsoleted classes.
