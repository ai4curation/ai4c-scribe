---
repo: geneontology/go-ontology
issue_number: 31963
pr_number: 32006
issue_title: "Obsolete GO:0045550 geranylgeranyl reductase activity"
issue_created_at: "2026-04-24"
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
  - enzymes
  - geranylgeranyl
  - definition-update
curated_by: claude-opus-4
curated_at: "2026-05-10"
rationale: Follow-up definition refinement based on curator feedback, showing iterative improvement of enzyme term definitions
---

## Context

Issue #31963 primarily requested obsoletion of GO:0045550, but discussion in the issue also identified that GO:0102067 (the replacement term) had an overly complex definition. After the obsoletion was merged in PR #32009, @sjm41 noted that the reaction description in GO:0102067's definition should be simplified to use "phytyl diphosphate" rather than spelling out the full IUPAC substrate name.

## Changes Made

In `src/ontology/go-edit.obo`, the `def:` field of GO:0102067 (geranylgeranyl diphosphate reductase activity) was updated to use simplified substrate naming, making the definition more readable while remaining biochemically accurate.

## Resolution

Merged directly. This single-line definition polish was a direct response to @sjm41's comment in the issue discussion. It demonstrates the common pattern of iterative refinement where obsoletion of one term prompts closer scrutiny of the replacement term's quality.
