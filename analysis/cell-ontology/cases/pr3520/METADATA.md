---
repo: obophenotype/cell-ontology
issue_number: 3519
pr_number: 3520
issue_title: "[NTR] Create term for oRGC2"
issue_created_at: "2025-12-08"
pr_author: app/copilot-swe-agent
pr_merged_at: "2026-02-16"
pr_num_commits: 14
files_changed:
  - path: src/ontology/cl-edit.owl
    additions: 9
    deletions: 0
scoping: tightly_scoped
task_type: new_term
difficulty: simple
scope: single_term
review_outcome: approved_first_time
domain_area: neuroscience
tags:
  - NTR
  - retinal-ganglion-cell
  - orthotype
  - oRGC2
  - retina
curated_by: claude-opus-4
curated_at: "2026-05-08"
rationale: New retinal ganglion cell orthotype term following established pattern from RGC refactoring series
---

## Context

As part of the ongoing retinal ganglion cell (RGC) refactoring tracked in epic #2844, a new term was requested for the oRGC2 orthotype. The oRGC classification system defines conserved RGC types across species based on transcriptomic similarity. oRGC2 is one of several orthotype classes being systematically added to CL to enable cross-species annotation of retinal ganglion cells.

## Changes Made

Added 9 new lines to `cl-edit.owl` defining the oRGC2 retinal ganglion cell orthotype term. The term follows the same compositional pattern as other oRGC terms in the series (oRGC1, oRGC4, oRGC5), with a class declaration, label, textual definition, parentage under retinal ganglion cell, and a see_also link to the reference transcriptomic dataset.

## Resolution

Approved on first review, though it took 14 commits to reach the final state, reflecting iterative refinement. Simple difficulty because the term follows an established pattern already used for other oRGC orthotype terms in the same series, requiring only the specific identifiers and definition text for this particular orthotype.
