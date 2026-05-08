---
repo: obophenotype/uberon
issue_number: 3672
pr_number: 3673
issue_title: "add 'addedByHRA' subset tag"
issue_created_at: "2026-03-14"
issue_closed_at: "2026-03-19"
pr_author: nicolevasilevsky
pr_merged_at: "2026-03-19"
pr_num_commits: 2
files_changed:
  - path: src/ontology/uberon-edit.obo
    additions: 1
    deletions: 0
scoping: tightly_scoped
task_type: other
difficulty: simple
scope: single_term
review_outcome: approved_first_time
domain_area: metadata
tags:
  - subset-tag
  - HRA
  - metadata
curated_by: claude-opus-4
curated_at: "2026-05-08"
rationale: Minimal metadata addition showing how subset tags are declared in the OBO header
---

## Context

The Human Reference Atlas (HRA) project needed a new subset tag "added_by_HRA" to track which terms in Uberon were contributed by HRA. This requires adding a subsetdef declaration to the OBO file header.

## Changes Made

A single line was added to the ontology header in uberon-edit.obo declaring the new subset "added_by_HRA" with a description. This is a minimal change that only modifies the file header, not any term stanzas.

## Resolution

Simple metadata addition. An agent would need to know where subset declarations go in OBO format (in the header section) and follow the existing subsetdef pattern. Approved on first review.
