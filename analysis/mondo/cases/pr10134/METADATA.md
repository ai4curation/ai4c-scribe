---
repo: monarch-initiative/mondo
issue_number: 9749
pr_number: 10134
issue_title: "FAS-related autoimmune lymphoproliferative syndrome"
issue_labels:
  - New term request
  - user request
  - Need ClinGen Review
issue_created_at: "2025-11-13"
pr_author: MeeSiing
pr_merged_at: "2026-04-08"
pr_num_commits: 1
files_changed:
  - path: src/ontology/mondo-edit.obo
    additions: 2
    deletions: 2
scoping: tightly_scoped
scoping_notes: Minimal change updating only the label of a single term.
task_type: synonym_update
difficulty: simple
scope: single_term
review_outcome: approved_first_time
domain_area: rare-disease
tags:
  - relabel
  - ClinGen
  - autoimmune
  - lymphoproliferative
  - FAS
curated_by: claude-opus-4
curated_at: "2026-05-08"
rationale: Simple label update driven by ClinGen request demonstrating external stakeholder-driven curation
case_quality: good
case_quality_reason: single_complete_gold_pr
quality_flagged_by: codex
quality_flagged_at: "2026-05-17"
---

## Context

ClinGen requested an update to the label of a term they had previously requested. The term for FAS-related autoimmune lymphoproliferative syndrome needed its label adjusted to match ClinGen's preferred naming convention. This type of post-creation label refinement is common when external databases refine their nomenclature.

## Changes Made

Updated the label of the FAS-related autoimmune lymphoproliferative syndrome term in `src/ontology/mondo-edit.obo`. The change is minimal: 2 additions and 2 deletions, reflecting a straightforward label swap. The old label was likely preserved as a synonym.

## Resolution

Easy difficulty as this is a simple relabeling operation. An agent needs only to identify the correct term, update its label, and ensure the old label is preserved as a synonym. The main challenge is correctly interpreting the ClinGen request and applying the naming convention.
