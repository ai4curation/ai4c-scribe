---
repo: geneontology/go-ontology
issue_number: 31601
pr_number: 32007
issue_title: "Textual definition update: protein carrier activity and unfolded protein holdase activity"
issue_created_at: "2026-02-18"
pr_author: dragon-ai-agent
pr_merged_at: "2026-04-28"
pr_num_commits: 1
files_changed:
  - path: src/ontology/go-edit.obo
    additions: 1
    deletions: 1
scoping: tightly_scoped
task_type: synonym_update
difficulty: simple
scope: single_term
review_outcome: approved_first_time
domain_area: molecular_function
tags:
  - textual-definition
  - protein-carrier
  - definition-update
curated_by: claude-opus-4
curated_at: "2026-05-10"
rationale: Minimal single-line definition change demonstrating how definition consistency is maintained across parent-child term pairs
---

## Context

Issue #31601 requested updates to the textual definitions of "protein carrier activity" (GO:0140597) and "unfolded protein holdase activity" to improve clarity and structural consistency. This PR addresses the protein carrier activity definition specifically, aligning its wording with the parent term "molecular carrier activity" (GO:0140596).

## Changes Made

In `src/ontology/go-edit.obo`, a single line was changed: the `def:` field of GO:0140597 was revised to mirror the structural pattern used by its parent term. This ensures that child term definitions are recognizable specializations of their parent's definition, a key GO editorial principle.

## Resolution

Merged directly as a minimal, well-motivated definition improvement. The change was requested by @hattrill and the implementation faithfully followed the requested wording. This type of definition harmonization is common in GO maintenance and represents low-risk editorial work.
