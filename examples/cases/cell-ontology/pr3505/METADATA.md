---
repo: obophenotype/cell-ontology
issue_number: 3458
pr_number: 3505
issue_title: "NTR Fibrochondrocyte progenitor cell (FCP)"
issue_created_at: "2025-11-20"
pr_author: app/copilot-swe-agent
pr_merged_at: "2025-12-11"
pr_num_commits: 8
files_changed:
  - path: src/ontology/cl-edit.owl
    additions: 14
    deletions: 0
scoping: tightly_scoped
task_type: new_term
difficulty: medium
scope: single_term
review_outcome: approved_first_time
domain_area: skeletal
tags:
  - NTR
  - fibrochondrocyte
  - progenitor
  - cartilage
  - stem-cell
curated_by: claude-opus-4
curated_at: "2026-05-08"
rationale: New progenitor cell type requiring understanding of chondrocyte differentiation lineages in fibrocartilage
---

## Context

A new term request was filed for the fibrochondrocyte progenitor cell (FCP), a precursor cell that gives rise to fibrochondrocytes in fibrocartilaginous tissues such as the meniscus and temporomandibular joint disc. This term is part of a broader effort to populate the chondrocyte and cartilage cell branches of CL, complementing related terms like fibrochondrocyte (CL_4072104) added in PR #3467.

## Changes Made

Added 14 new lines to `cl-edit.owl` defining the FCP term with appropriate class declaration, label, textual definition referencing the progenitor-to-fibrochondrocyte differentiation pathway, parentage linking it to both progenitor cell and the chondrocyte lineage, and logical axioms capturing its developmental potential.

## Resolution

Approved on first review after 8 commits of iterative refinement. Medium difficulty because correctly modeling a progenitor cell requires establishing the develops_into relationship to the mature fibrochondrocyte and positioning the term appropriately within both the progenitor cell hierarchy and the cartilage cell lineage.
