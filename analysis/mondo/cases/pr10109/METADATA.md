---
repo: monarch-initiative/mondo
issue_number: 9795
pr_number: 10109
issue_title: "[Obsolete] OMIM merges"
issue_created_at: "2025-11-26"
pr_author: MeeSiing
pr_merged_at: "2026-04-02"
pr_num_commits: 2
files_changed:
  - path: src/ontology/mondo-edit.obo
    additions: 20
    deletions: 21
scoping: tightly_scoped
task_type: obsoletion
difficulty: medium
scope: single_term
review_outcome: changes_requested
curated_by: claude-opus-4
curated_at: "2026-05-10"
rationale: Complex neurology term merge requiring QC fix, reflecting the challenge of merging terms with overlapping but distinct clinical phenotypes.
---

## Context

Issue #9795 identified several OMIM entries that had been merged upstream and needed corresponding merges in Mondo. This PR specifically merged "Charcot-Marie-Tooth peroneal muscular atrophy and Friedreich ataxia, combined" into MONDO:0010549, following OMIM:214380's merge into OMIM:302800. The conditions share overlapping neuropathy features but were historically maintained as separate entries.

## Changes Made

The PR required 2 commits: the initial merge operation and a subsequent QC fix. The merge obsoleted one term and transferred its metadata (synonyms, xrefs, definitions) to MONDO:0010549. The 20 additions and 21 deletions reflect the standard merge pattern: adding replaced_by annotations, transferring cross-references, and removing the obsoleted term's active axioms. The QC failure in the first commit likely involved a missing annotation or invalid axiom pattern that automated checks caught.

## Resolution

Moderate difficulty because neurology term merges require understanding whether two clinical presentations truly represent the same underlying disease entity. The OMIM merge provides strong evidence, but the curator must still correctly execute the merge procedure and handle any QC issues that arise from combining annotation sets from different provenance sources.
