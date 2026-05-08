---
repo: obophenotype/cell-ontology
issue_number: 2844
pr_number: 3451
issue_title: "[EPIC] Retinal Ganglion Cells refactoring"
issue_created_at: "2024-12-05"
pr_author: app/copilot-swe-agent
pr_merged_at: "2025-11-20"
pr_num_commits: 3
files_changed:
  - path: src/ontology/cl-edit.owl
    additions: 15
    deletions: 0
scoping: tightly_scoped
task_type: new_term
difficulty: medium
scope: single_term
review_outcome: approved_first_time
domain_area: neuroscience
tags:
  - NTR
  - retinal-ganglion-cell
  - ipRGC
  - photosensitive
  - melanopsin
curated_by: claude-opus-4
curated_at: "2026-05-08"
rationale: New term for intrinsically photosensitive RGC as part of large-scale retinal ganglion cell refactoring epic
---

## Context

As part of the large-scale retinal ganglion cell (RGC) refactoring effort tracked in epic issue #2844, a new term was needed for the intrinsically photosensitive retinal ganglion cell (ipRGC). This cell type is distinguished from conventional RGCs by its expression of melanopsin (OPN4) and its ability to respond directly to light independently of rod and cone photoreceptors. The request also referenced earlier issues #1905 and #2217 that had discussed this cell type.

## Changes Made

Added 15 new lines to `cl-edit.owl` defining the ipRGC term. This includes the class declaration, label, textual definition citing key melanopsin/photosensitivity literature, parentage under retinal ganglion cell, and logical axioms capturing the capable_of relationship to phototransduction-related GO processes and the expresses relationship to melanopsin.

## Resolution

Approved on first review in 3 commits. Medium difficulty because the term requires understanding of the melanopsin signaling pathway and the functional distinction between intrinsic photosensitivity and synaptically-driven light responses in retinal ganglion cells.
