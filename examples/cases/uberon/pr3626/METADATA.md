---
repo: obophenotype/uberon
issue_number: 3625
pr_number: 3626
issue_title: "Edit vestibular nerve ABA xrefs"
issue_created_at: "2025-11-10"
issue_closed_at: "2025-11-10"
pr_author: dragon-ai-agent
pr_merged_at: "2025-11-10"
pr_num_commits: 1
files_changed:
  - path: src/ontology/uberon-edit.obo
    additions: 0
    deletions: 1
scoping: tightly_scoped
task_type: axiom_repair
difficulty: simple
scope: single_term
review_outcome: approved_first_time
domain_area: neuroanatomy
tags:
  - xref-removal
  - DHBA
  - vestibular-nerve
curated_by: claude-opus-4
curated_at: "2026-05-08"
rationale: Minimal single-line xref removal on a single term, the simplest possible ontology edit
---

## Context

The DHBA:12869 cross-reference on the vestibular nerve term (UBERON:0003723) was incorrect and needed to be removed. This was a companion fix to the broader DHBA xref cleanup effort.

## Changes Made

Removed the single line `xref: DHBA:12869` from the vestibular nerve term stanza in uberon-edit.obo. No other changes were made.

## Resolution

This is the simplest possible ontology edit: locating a specific term by ID and removing one annotation line. An agent only needs to find UBERON:0003723 in the edit file and delete the offending xref. Approved on first review the same day.
