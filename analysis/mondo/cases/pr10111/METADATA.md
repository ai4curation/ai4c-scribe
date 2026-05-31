---
repo: monarch-initiative/mondo
issue_number: 9781
pr_number: 10111
issue_title: "Request for new term [preneoplastic lesion]"
issue_labels:
  - New term request
  - user request
issue_created_at: "2025-11-20"
pr_author: MeeSiing
pr_merged_at: "2026-04-02"
pr_num_commits: 1
files_changed:
  - path: src/ontology/mondo-edit.obo
    additions: 8
    deletions: 0
scoping: tightly_scoped
scoping_notes: PR adds a single new term with definition and classification.
task_type: new_term
difficulty: simple
scope: single_term
review_outcome: approved_first_time
domain_area: oncology
tags:
  - preneoplastic
  - oncology
  - grouping-term
curated_by: claude-opus-4
curated_at: "2026-05-08"
rationale: Simple new grouping term with definition confirmed by the requesting user
case_quality: ok
case_quality_reason: sound_gold_but_new_grouping_term_has_sparse_issue_signal
quality_flagged_by: codex
quality_flagged_at: "2026-05-17"
---

## Context

A user requested a new term for "preneoplastic lesion" to capture conditions that precede neoplastic transformation. This is a high-level grouping class rather than a specific gene-disease term. The definition and parent term were confirmed through discussion with the requesting user in the issue thread.

## Changes Made

Added MONDO:1060215 (preneoplastic lesion) to `src/ontology/mondo-edit.obo` with 8 lines. The term is compact, containing an ID, name, definition, and parent classification. No logical axioms or complex cross-references were needed for this grouping term.

## Resolution

Easy difficulty because it is a simple grouping term without gene-disease logical axioms or complex cross-references. The main requirement was confirming the definition and appropriate parent class with the requesting user, which was done in the issue discussion.
