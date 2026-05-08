---
repo: obophenotype/uberon
issue_number: 3495
pr_number: 3542
issue_title: "epithelium and lamina propria for GI tract"
issue_labels:
  - new term request
  - high-priority
  - GutCellAtlas
issue_created_at: "2025-03-18"
issue_closed_at: "2025-05-27"
pr_author: cmungall
pr_merged_at: "2025-05-27"
pr_num_commits: 5
files_changed:
  - path: src/ontology/uberon-edit.obo
    additions: 88
    deletions: 9
scoping: mostly_scoped
scoping_notes: >-
  The issue requested both epithelium and lamina propria terms for GI tract segments.
  This PR addresses the lamina propria portion; epithelium terms were in a separate PR.
task_type: new_term
difficulty: hard
scope: multi_term
review_outcome: approved_first_time
domain_area: gastrointestinal-anatomy
tags:
  - new-term
  - lamina-propria
  - GI-tract
  - GutCellAtlas
  - batch-NTR
curated_by: claude-opus-4
curated_at: "2026-05-08"
rationale: Large batch NTR following a compositional pattern across seven gut segments, requiring consistent axiom construction
---

## Context

The Gut Cell Atlas project needed lamina propria terms for seven gut segments (ascending colon, descending colon, sigmoid colon, transverse colon, stomach, caecum, and rectum). Each term follows a compositional pattern: "The lamina propria that underlies the epithelial lining of the {gut segment}."

## Changes Made

Added seven new lamina propria terms to uberon-edit.obo with 88 lines of additions. Each term included a definition following the compositional pattern, appropriate synonyms, is_a classification under lamina propria, and part_of relationships to the specific gut segment. Some existing term stanzas were also updated (9 deletions).

## Resolution

Hard difficulty due to the scale and consistency requirements. The agent must create seven parallel term stanzas, each following the same compositional pattern but with segment-specific relationships. It must correctly identify the parent lamina propria class, use the right part_of targets for each colon region, and ensure no inconsistencies across the batch. This was a high-priority request from an external project.
