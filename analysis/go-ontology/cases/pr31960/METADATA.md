---
repo: geneontology/go-ontology
issue_number: 31956
pr_number: 31960
issue_title: "Obsoletion request: GO:0005870 actin capping protein of dynactin complex (unused, direct replacement)"
issue_created_at: "2026-04-23"
pr_author: dragon-ai-agent
pr_merged_at: "2026-04-23"
pr_num_commits: 1
files_changed:
  - path: src/ontology/go-edit.obo
    additions: 6
    deletions: 4
scoping: tightly_scoped
task_type: obsoletion
difficulty: simple
scope: single_term
review_outcome: approved_first_time
domain_area: cellular_component
tags:
  - obsoletion
  - cellular-component
  - protein-complex
  - dynactin
  - cytoskeleton
  - replaced_by
curated_by: claude-opus-4
curated_at: "2026-05-10"
rationale: Simple obsoletion of an overly specific complex subunit term with clear direct replacement
---

## Context

Issue #31956 requested obsoletion of GO:0005870 "actin capping protein of dynactin complex". The term was logically defined as an F-actin capping protein complex (GO:0008290) that is `part_of` a dynactin complex -- essentially a redundant subclass that no annotations used. Since the compositional relationship can be captured in GO-CAM models rather than pre-composed CC terms, the overly specific term was marked for obsoletion.

## Changes Made

In `src/ontology/go-edit.obo`, GO:0005870 was obsoleted:
- Marked `is_obsolete: true`
- Added `replaced_by: GO:0008290` (F-actin capping protein complex)
- Removed the `intersection_of` and `relationship: part_of` axioms that defined it as a subclass
- Retained the term stanza for provenance

## Resolution

Merged same-day. This is a textbook obsoletion case: unused term, clear 1:1 replacement, and the specificity it captured (being part of dynactin) is better modeled compositionally in GO-CAM rather than through pre-composed CC terms.
