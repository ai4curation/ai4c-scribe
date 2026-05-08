---
repo: obophenotype/cell-ontology
issue_number: 3346
pr_number: 3549
issue_title: "Revise intraepithelial lymphocyte and subclasses"
issue_created_at: "2025-09-25"
issue_closed_at: "2026-02-18"
pr_author: copilot-swe-agent
pr_merged_at: "2026-02-18"
pr_num_commits: 6
files_changed:
  - path: src/ontology/cl-edit.owl
    additions: 15
    deletions: 2
scoping: tightly_scoped
task_type: axiom_repair
difficulty: hard
scope: multi_term
review_outcome: approved_first_time
domain_area: immunology
tags:
  - lymphocyte
  - intraepithelial
  - definition-broadening
  - intestinal
  - mucosal-immunity
curated_by: claude-opus-4
curated_at: "2026-05-08"
rationale: Complex definition revision broadening a cell type from tissue-specific to pan-epithelial, requiring immunology domain expertise
---

## Context

The intraepithelial lymphocyte (IEL) term (CL:0002496) was incorrectly restricted to intestinal epithelium only. In reality, IELs are found throughout mucosal epithelia including gastrointestinal, respiratory, and reproductive tracts. The definition needed broadening to reflect the true biological scope, and a new intestinal-specific subclass was needed for backward compatibility.

## Changes Made

Modified `cl-edit.owl` with 15 additions and 2 deletions. The changes broaden the IEL definition to encompass all epithelial tissues, remove the intestinal-specific restriction from the parent term, and add a new "intestinal intraepithelial lymphocyte" subclass to preserve the original narrower concept.

## Resolution

Approved on first review. Hard difficulty because this requires: (1) understanding mucosal immunology well enough to know IELs exist outside the gut, (2) correctly broadening a definition without breaking existing annotations, (3) creating a subclass to preserve backward compatibility, and (4) ensuring the logical axioms correctly reflect the broader anatomical scope.
