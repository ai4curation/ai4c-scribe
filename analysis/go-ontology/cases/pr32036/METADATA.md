---
repo: geneontology/go-ontology
issue_number: 31882
pr_number: 32036
issue_title: "Obsolete: GO:0097711 ciliary basal body-plasma membrane docking Biological Process"
issue_created_at: "2026-04-10"
pr_author: dragon-ai-agent
pr_merged_at: "2026-05-05"
pr_num_commits: 1
files_changed:
  - path: src/ontology/go-edit.obo
    additions: 13
    deletions: 36
scoping: tightly_scoped
task_type: obsoletion
difficulty: simple
scope: multi_term
review_outcome: approved_first_time
curated_by: claude-opus-4
curated_at: "2026-05-08"
rationale: Batch obsoletion of two redundant cilium assembly terms with clear replaced_by targets, agreed upon by multiple curators
case_quality: good
case_quality_reason: single_complete_gold_pr
quality_flagged_by: codex
quality_flagged_at: "2026-05-17"
---

## Context

Two terms in the cilium assembly branch were identified as redundant with `GO:1905349 ciliary transition zone assembly`. GO:1905353 `ciliary transition fiber assembly` and GO:0097711 `ciliary basal body-plasma membrane docking` both described aspects of the same biological process already captured by the replacement term. The obsoletion was discussed and confirmed by curators ValWood, hattrill, pgaudet, and raymond91125.

## Changes Made

Both GO:1905353 and GO:0097711 were obsoleted in `go-edit.obo` with `replaced_by` pointing to GO:1905349 `ciliary transition zone assembly`. The obsoletion involved removing logical axioms (is_a relationships, intersection_of definitions), adding the "OBSOLETE." prefix to definitions, and renaming terms with the "obsolete" prefix. The net change removed 36 lines (axioms and active term stanzas) and added 13 lines (obsoletion markers and replaced_by references).

## Resolution

This was a straightforward obsoletion with pre-existing curator consensus. Easy difficulty because the replacement term was already identified, multiple curators had agreed on the action, and no annotation migration complexity was involved. The large line deletion count reflects the removal of logical definitions and axioms from both terms.
