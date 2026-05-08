---
repo: obophenotype/cell-ontology
issue_number: 3559
pr_number: 3564
issue_title: "[Synonym] abbreviations like PBMC"
issue_created_at: "2026-01-23"
issue_closed_at: "2026-02-06"
pr_author: RiveraAndrea83
pr_merged_at: "2026-02-06"
pr_num_commits: 2
files_changed:
  - path: src/ontology/cl-edit.owl
    additions: 3
    deletions: 0
scoping: tightly_scoped
task_type: synonym_update
difficulty: simple
scope: multi_term
review_outcome: approved_first_time
domain_area: cell-biology
tags:
  - synonyms
  - abbreviations
  - PBMC
  - WBC
  - leukocyte
curated_by: claude-opus-4
curated_at: "2026-05-08"
rationale: Clean synonym addition case demonstrating how common abbreviations are added with appropriate synonym scope
---

## Context

A community request asked for standard abbreviations to be added as synonyms for commonly referenced cell types. Specifically, PBMC (peripheral blood mononuclear cell) and WBC (white blood cell / leukocyte) are widely used abbreviations in clinical and research literature that were missing from the ontology.

## Changes Made

Added 3 exact synonym annotations to `cl-edit.owl`: "PBMC" for peripheral blood mononuclear cell (CL:2000001) with a literature reference, and "WBC" for leukocyte (CL:0000738). Each synonym includes appropriate database cross-references.

## Resolution

Approved on first review. This is a straightforward synonym addition requiring knowledge of OWL synonym annotation patterns (exact vs. related scope) and proper cross-referencing. An agent would need to identify the correct terms and apply the right synonym type with provenance.
