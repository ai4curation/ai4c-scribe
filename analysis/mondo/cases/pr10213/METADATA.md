---
repo: monarch-initiative/mondo
issue_number: 9940
pr_number: 10213
issue_title: "EFL1-related Shwachman-Diamond syndrome"
issue_created_at: "2026-02-12"
pr_author: MeeSiing
pr_merged_at: "2026-05-01"
pr_num_commits: 1
files_changed:
  - path: src/ontology/mondo-edit.obo
    additions: 5
    deletions: 1
scoping: tightly_scoped
task_type: synonym_update
difficulty: simple
scope: single_term
review_outcome: approved_first_time
curated_by: claude-opus-4
curated_at: "2026-05-10"
rationale: Single-term update adding ClinGen preferred label and updating definition with minimal changes.
---

## Context

Issue #9940 requested adding "EFL1-related Shwachman-Diamond syndrome" as the ClinGen preferred label for MONDO:0044205. The request followed the standard ClinGen gene-centric naming template, providing the preferred label, synonyms, parent term, and supporting evidence.

## Changes Made

The PR added the ClinGen preferred label as an exact synonym to MONDO:0044205 and updated the term's definition. The 5 additions and 1 deletion reflect adding synonym lines and modifying the definition text to better align with current understanding of this EFL1-associated variant of Shwachman-Diamond syndrome.

## Resolution

Simple difficulty because it follows a well-established pattern for ClinGen label requests. The curator needs to locate the term stanza, add the synonym with appropriate scope and source annotations, and optionally update the definition. An agent with knowledge of OBO synonym format and ClinGen naming conventions could handle this reliably.
