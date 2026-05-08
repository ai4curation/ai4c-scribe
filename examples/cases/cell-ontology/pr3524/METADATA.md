---
repo: obophenotype/cell-ontology
issue_number: 3523
pr_number: 3524
issue_title: "Revise textual definition of Retinal Ganglion Cell A into Alpha retinal ganglion cell"
issue_created_at: "2025-12-09"
pr_author: app/copilot-swe-agent
pr_merged_at: "2026-02-17"
pr_num_commits: 14
files_changed:
  - path: src/ontology/cl-edit.owl
    additions: 4
    deletions: 3
scoping: tightly_scoped
task_type: other
difficulty: simple
scope: single_term
review_outcome: approved_first_time
domain_area: neuroscience
tags:
  - definition-update
  - retinal-ganglion-cell
  - rename
  - alpha-RGC
  - mouse
curated_by: claude-opus-4
curated_at: "2026-05-08"
rationale: Rename and definition revision for alpha RGC aligning label with current nomenclature and adding species specificity
---

## Context

CL_0004117 was labeled "Retinal Ganglion Cell A" using an older naming convention. Issue #3523 requested renaming it to "alpha retinal ganglion cell (Mmus)" to align with current RGC nomenclature and to make the mouse-specific taxon scope explicit. This is part of the broader RGC refactoring effort (epic #2844) to modernize retinal ganglion cell terminology in CL.

## Changes Made

Updated `cl-edit.owl` with 4 additions and 3 deletions: the primary label was changed from "Retinal Ganglion Cell A" to "alpha retinal ganglion cell (Mmus)", the textual definition was revised to reference the alpha RGC classification and its large soma size and brisk transient responses, and a species-specific qualifier was added.

## Resolution

Approved on first review despite requiring 14 commits to finalize. Simple difficulty because the change is primarily a label and definition text update following the RGC nomenclature standardization pattern established across the series.
