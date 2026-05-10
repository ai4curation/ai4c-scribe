---
repo: geneontology/go-ontology
issue_number: 31114
pr_number: 32028
issue_title: "NTR: Terreic acid biosynthetic process"
issue_created_at: "2025-11-21"
pr_author: dragon-ai-agent
pr_merged_at: "2026-05-05"
pr_num_commits: 1
files_changed:
  - path: src/ontology/go-edit.obo
    additions: 3
    deletions: 3
scoping: tightly_scoped
task_type: axiom_repair
difficulty: simple
scope: multi_term
review_outcome: changes_requested
domain_area: biological_process
tags:
  - metadata-fix
  - created_by
  - terreic-acid
curated_by: claude-opus-4
curated_at: "2026-05-10"
rationale: Illustrates how an apparently simple fix can be wrong when conventions are ambiguous, leading to a follow-up correction
---

## Context

Issue #31114 originally requested new terms for terreic acid biosynthetic processes. During implementation, it was noticed that three terms had `created_by: PomBase:vw` instead of the expected GO convention. This PR attempted to fix them by changing to `GOC:vw`.

## Changes Made

In `src/ontology/go-edit.obo`, the `created_by` field on three terms was changed from `PomBase:vw` to `GOC:vw`:
- GO:0180067 (terreate biosynthetic process)
- GO:0180068 (negative regulation of terreate biosynthetic process)
- One additional related term

## Resolution

While the PR was merged, @pgaudet subsequently clarified that the correct format uses bare initials (`vw`) without any prefix. This prompted a follow-up PR (#32032) to make the final correction. This case demonstrates the importance of verifying metadata conventions with experienced curators rather than guessing at the pattern.
