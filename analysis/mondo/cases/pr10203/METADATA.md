---
repo: monarch-initiative/mondo
issue_number: 9882
pr_number: 10203
issue_title: "Request for new synonyms to: arhinia, choanal atresia, and microphthalmia MONDO:0011323"
issue_created_at: "2026-01-16"
pr_author: MeeSiing
pr_merged_at: "2026-04-30"
pr_num_commits: 1
files_changed:
  - path: src/ontology/mondo-edit.obo
    additions: 6
    deletions: 0
scoping: tightly_scoped
task_type: synonym_update
difficulty: simple
scope: single_term
review_outcome: approved_first_time
curated_by: claude-opus-4
curated_at: "2026-05-10"
rationale: Multiple synonym additions to a single congenital disorder term from a community request.
---

## Context

Issue #9882 requested adding new synonyms to MONDO:0011323 (arhinia, choanal atresia, and microphthalmia). The requested synonyms included longer descriptive forms such as "Arhinia, choanal atresia, microphthalmia, and hypogonadotropic hypogonadism" that capture the full phenotypic spectrum of this SMCHD1-related condition.

## Changes Made

The PR added 6 synonym lines to MONDO:0011323 in mondo-edit.obo with no deletions. Each synonym was annotated with appropriate scope (EXACT) and evidence. The additions capture variant clinical descriptions of this complex congenital syndrome that combines craniofacial and endocrine features.

## Resolution

Simple difficulty as a pure additive synonym change. The curator needed to verify each requested synonym was appropriate for EXACT scope and add proper evidence annotations. An agent could handle this by parsing the issue template, extracting requested synonyms, and generating the correct OBO synonym syntax with appropriate xref evidence.
