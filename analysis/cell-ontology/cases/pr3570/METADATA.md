---
repo: obophenotype/cell-ontology
issue_number: 3500
pr_number: 3570
issue_title: "Add taxon constraints to DN2a and DN2b thymocytes"
issue_created_at: "2025-12-01"
pr_author: app/copilot-swe-agent
pr_merged_at: "2026-02-20"
pr_num_commits: 4
files_changed:
  - path: src/ontology/cl-edit.owl
    additions: 2
    deletions: 0
scoping: tightly_scoped
task_type: other
difficulty: simple
scope: multi_term
review_outcome: approved_first_time
domain_area: immunology
tags:
  - taxon-constraint
  - thymocyte
  - DN2
  - mouse
  - Mus-musculus
curated_by: claude-opus-4
curated_at: "2026-05-08"
rationale: Simple taxon constraint addition restricting DN2a/DN2b thymocyte terms to Mus musculus
---

## Context

The DN2a (CL_0002423) and DN2b (CL_0002424) thymocyte subtypes are defined based on mouse thymic development staging that does not directly translate to human T cell development. Issue #3500 requested adding taxon constraints to restrict these terms to Mus musculus, preventing their misuse in annotating human datasets where the DN2a/DN2b distinction is not applicable.

## Changes Made

Added 2 new lines to `cl-edit.owl`, one for each term, adding an `in_taxon some NCBITaxon:10090` (Mus musculus) constraint to CL_0002423 (DN2a thymocyte) and CL_0002424 (DN2b thymocyte). This is the standard CL pattern for species-restricted cell types.

## Resolution

Approved on first review in 4 commits. Simple difficulty because adding taxon constraints follows a well-established pattern in CL, and the biological rationale for restricting these terms to mouse is straightforward -- the DN2a/DN2b distinction is based on mouse-specific developmental staging.
