---
repo: monarch-initiative/mondo
issue_number: 9909
pr_number: 10208
issue_title: "macrothrombocytopenia and granulocyte inclusions with or without nephritis or sensorineural hearing loss nomenclature and synonyms"
issue_created_at: "2026-01-28"
pr_author: MeeSiing
pr_merged_at: "2026-05-01"
pr_num_commits: 1
files_changed:
  - path: src/ontology/mondo-edit.obo
    additions: 9
    deletions: 7
scoping: tightly_scoped
task_type: synonym_update
difficulty: simple
scope: single_term
review_outcome: approved_first_time
curated_by: claude-opus-4
curated_at: "2026-05-10"
rationale: Synonym cleanup and addition for a term with complex nomenclature, requiring careful assessment of which synonyms are truly exact.
---

## Context

Issue #9909 addressed the nomenclature for MONDO:0015912 (macrothrombocytopenia and granulocyte inclusions with or without nephritis or sensorineural hearing loss). The request specified which synonyms should be marked as exact: "MATINS", "MYH9-Related Disease", and "MYH9-related syndromic thrombocytopenia", reflecting current clinical usage.

## Changes Made

The PR modified synonym annotations on MONDO:0015912, adding 9 lines and removing 7. This pattern of additions exceeding deletions while both being present indicates synonym scope corrections (e.g., changing RELATED to EXACT) alongside new synonym additions. The MYH9-related naming follows ClinGen gene-centric conventions.

## Resolution

Simple difficulty but requires attention to synonym scope accuracy. The curator needed to evaluate which existing synonyms had incorrect scope and which new synonyms to add. An agent would need to parse the issue request carefully, identify the target term, and apply both additions and scope modifications in a single coherent edit.
