---
repo: monarch-initiative/mondo
issue_number: 9862
pr_number: 10103
issue_title: "Request for new synonym [Add GEMIN5-related neurodevelopmental disorders and GEMIN5 disorders as new synonym for Neurodevelopmental disorder with cerebellar atrophy and motor dysfunction]"
issue_created_at: "2026-01-07"
pr_author: MeeSiing
pr_merged_at: "2026-03-31"
pr_num_commits: 1
files_changed:
  - path: src/ontology/mondo-edit.obo
    additions: 8
    deletions: 0
scoping: tightly_scoped
task_type: synonym_update
difficulty: simple
scope: single_term
review_outcome: approved_first_time
curated_by: claude-opus-4
curated_at: "2026-05-10"
rationale: Synonym addition combined with definition and logical definition creation for an under-annotated term.
case_quality: poor
case_quality_reason: gold_scope_expanded_beyond_synonym_request
scoring_caveat: "Gold adds definition, comment, logical definition, abbreviation synonym, and tracker beyond the explicit synonym request; agents that only add requested synonyms are penalized, so metadiff is a poor quality proxy."
quality_flagged_by: codex
quality_flagged_at: "2026-05-17"
---

## Context

Issue #9862 requested adding "GEMIN5-related neurodevelopmental disorders" and "GEMIN5 disorders" as exact synonyms for MONDO:0859152 (neurodevelopmental disorder with cerebellar atrophy and motor dysfunction). The requester specifically asked for EXACT scope for both synonyms. The PR body notes that "GEMIN5 disorder" was added as exact based on the user's specific request.

## Changes Made

The PR added 8 lines to MONDO:0859152 in mondo-edit.obo with no deletions. Beyond the two requested synonyms, the curator also added a definition and logical definition to the term, which previously lacked both. This enrichment beyond the original request improves the term's utility for both human users and automated reasoning.

## Resolution

Simple difficulty for the synonym additions, but the curator went beyond the request to add definition and logical definition. This represents good curatorial practice of enriching under-annotated terms when they are being edited. An agent should ideally detect when a term lacks essential annotations (definition, logical definition) and proactively add them during other edits.
