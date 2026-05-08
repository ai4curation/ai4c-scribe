---
repo: obophenotype/cell-ontology
issue_number: 3457
pr_number: 3467
issue_title: "Add fibrochondrocyte (CL_4072104) term"
issue_created_at: "2025-11-20"
issue_closed_at: "2025-11-27"
pr_author: copilot-swe-agent
pr_merged_at: "2025-11-27"
pr_num_commits: 7
files_changed:
  - path: src/ontology/cl-edit.owl
    additions: 5
    deletions: 4
scoping: mostly_scoped
scoping_notes: >-
  Primary change is the new fibrochondrocyte term in cl-edit.owl, but component
  files were also regenerated as part of the build process.
task_type: new_term
difficulty: medium
scope: single_term
review_outcome: approved_first_time
domain_area: musculoskeletal
tags:
  - NTR
  - fibrochondrocyte
  - chondrocyte
  - fibrocartilage
  - hybrid-cell
curated_by: claude-opus-4
curated_at: "2026-05-08"
rationale: New term for a hybrid cell type requiring understanding of chondrocyte and fibroblast dual characteristics
---

## Context

A new term request was filed for fibrochondrocyte, a hybrid cell type found in fibrocartilaginous tissues (meniscus, intervertebral disc, TMJ disc) that exhibits characteristics of both chondrocytes and fibroblasts. This cell type produces both type I and type II collagen, distinguishing it from typical hyaline cartilage chondrocytes.

## Changes Made

Added the fibrochondrocyte term (CL:4072104) to `cl-edit.owl` with proper parentage under both chondrocyte and fibroblast lineages, a textual definition citing relevant literature, and synonyms. The term uses a permanent CL ID rather than a temporary one, indicating it was minted through the standard ID allocation process.

## Resolution

Approved on first review. Medium difficulty because properly modeling a hybrid cell type requires understanding dual-lineage classification, choosing appropriate parent classes, and writing a definition that captures the distinguishing features (collagen type production, anatomical location in fibrocartilage).
