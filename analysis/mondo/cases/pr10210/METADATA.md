---
repo: monarch-initiative/mondo
issue_number: 9933
pr_number: 10210
issue_title: "GINS3 Meier-Gorlin syndrome"
issue_created_at: "2026-02-06"
pr_author: MeeSiing
pr_merged_at: "2026-05-01"
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
rationale: Multiple synonym additions to a single term following a gene-disease association request.
case_quality: ok
case_quality_reason: gold_scope_includes_design_pattern_enrichment_beyond_synonym_request
scoring_caveat: "Gold includes disease-series design-pattern enrichment in addition to synonym additions; F1 partly measures Mondo pattern completion rather than simple synonym extraction."
quality_flagged_by: codex
quality_flagged_at: "2026-05-17"
---

## Context

Issue #9933 raised a question about whether there was sufficient evidence to associate GINS3 with Meier-Gorlin syndrome, noting a 2024 publication confirming pathogenicity of GINS3 variants. The issue referenced functional studies in yeast confirming the disease association for MONDO:0980992.

## Changes Made

The PR added 8 lines of synonym annotations to MONDO:0980992 in mondo-edit.obo. These additions likely include gene-centric synonyms (e.g., "GINS3-related Meier-Gorlin syndrome") and potentially alternate disease names referenced in the literature, each with appropriate synonym scope and evidence annotations.

## Resolution

Simple difficulty as this is a pure additive change with no deletions. The curator identified the relevant term and added multiple synonyms with evidence codes. An agent needs to understand OBO synonym syntax, appropriate scope tags (EXACT, RELATED, etc.), and how to cite PMIDs as evidence for synonym assertions.
