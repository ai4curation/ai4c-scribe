---
repo: geneontology/go-ontology
issue_number: 32005
pr_number: 32026
issue_title: "Obsoletion request: GO:0009095 aromatic amino acid biosynthetic process, prephenate pathway"
issue_created_at: "2026-04-28"
pr_author: dragon-ai-agent
pr_merged_at: "2026-05-04"
pr_num_commits: 1
files_changed:
  - path: src/ontology/go-edit.obo
    additions: 8
    deletions: 14
scoping: tightly_scoped
task_type: obsoletion
difficulty: medium
scope: single_term
review_outcome: approved_first_time
domain_area: biological_process
tags:
  - obsoletion
  - metabolism
  - prephenate-pathway
  - superpathway
curated_by: claude-opus-4
curated_at: "2026-05-10"
rationale: Medium difficulty obsoletion requiring understanding of why pre-composed superpathway terms are problematic in GO
---

## Context

Issue #32005 requested obsoletion of GO:0009095 "aromatic amino acid biosynthetic process, prephenate pathway". This term represented a pre-composed superpathway that conflated the general aromatic amino acid biosynthetic process with a specific pathway variant. The MetaCyc cross-reference it carried was to a superpathway entry, which is not how GO typically represents metabolic specificity.

## Changes Made

In `src/ontology/go-edit.obo`, GO:0009095 was obsoleted:
- Removed all logical axioms (is_a relationships, intersection_of definitions)
- Added obsoletion metadata: `is_obsolete: true`, `consider` tags pointing to the individual pathway steps
- Retained the MetaCyc xref for provenance
- Net reduction of 6 lines, reflecting removal of redundant axioms

## Resolution

Merged directly. The obsoletion rationale was clear: GO prefers atomic terms that can be composed via GO-CAM models rather than pre-composed superpathway terms. No annotation migration was needed since the term had minimal direct annotations.
