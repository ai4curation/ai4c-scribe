---
repo: monarch-initiative/mondo
issue_number: 9930
pr_number: 10209
issue_title: "Request to add synonyms to: GRIN-related complex neurodevelopmental disorder (MONDO:1060138)"
issue_created_at: "2026-02-03"
pr_author: MeeSiing
pr_merged_at: "2026-05-01"
pr_num_commits: 3
files_changed:
  - path: src/ontology/mondo-edit.obo
    additions: 4
    deletions: 0
scoping: tightly_scoped
task_type: synonym_update
difficulty: simple
scope: single_term
review_outcome: changes_requested
curated_by: claude-opus-4
curated_at: "2026-05-10"
rationale: Synonym addition that required scope correction across multiple commits, illustrating the importance of synonym type accuracy.
case_quality: ok
case_quality_reason: metadiff_underrepresents_synonym_provenance_and_spelling
scoring_caveat: "Synonym line matching is dominated by requester ORCID provenance plus exact spelling and capitalization; attempts with substantively correct synonym additions may only match the term tracker line."
quality_flagged_by: codex
quality_flagged_at: "2026-05-17"
---

## Context

Issue #9930 was a request from NORD (National Organization for Rare Disorders) to add multiple synonyms to MONDO:1060138 (GRIN-related complex neurodevelopmental disorder). The requested synonyms included "GRINopathies", "GRIN-related Encephalopathy", and "GRIN-related Neurodevelopmental Disorder", reflecting terminology used in their rare disease report.

## Changes Made

The PR went through 3 commits: the initial synonym addition, then an update to correct a synonym value, and finally a scope correction. The final result added 4 synonym lines to MONDO:1060138 in mondo-edit.obo. The revisions demonstrate that synonym scope (EXACT vs RELATED vs BROAD) requires careful consideration, particularly when a requested synonym like "GRINopathies" is plural and may warrant RELATED rather than EXACT scope.

## Resolution

Although the individual edits are simple, this case illustrates that synonym requests from external stakeholders may need scope adjustment. The plural form "GRINopathies" could be argued as BROAD or RELATED rather than EXACT. An agent handling such requests needs to evaluate whether requested synonyms truly represent exact equivalence or require scope downgrading based on linguistic or semantic analysis.
