---
repo: monarch-initiative/mondo
issue_number: 9938
pr_number: 10221
issue_title: "request to relabel MONDO:0012277"
issue_created_at: "2026-02-11"
pr_author: MeeSiing
pr_merged_at: "2026-05-04"
pr_num_commits: 1
files_changed:
  - path: src/ontology/mondo-edit.obo
    additions: 2
    deletions: 0
scoping: tightly_scoped
task_type: synonym_update
difficulty: simple
scope: single_term
review_outcome: approved_first_time
curated_by: claude-opus-4
curated_at: "2026-05-10"
rationale: Minimal single-term synonym addition following a ClinGen relabel request with clear instructions.
---

## Context

Issue #9938 requested relabeling MONDO:0012277 (myofibrillar myopathy 4) to "LDB3-related myofibrillar myopathy" following ClinGen gene-centric naming conventions. The request included an ORCID for nano-attribution and a clear preferred label.

## Changes Made

The PR added "LDB3-related myofibrillar myopathy" as an exact synonym to MONDO:0012277 in the mondo-edit.obo file. This is a 2-line addition with no deletions, representing the simplest possible ontology edit pattern: adding a synonym annotation to an existing term stanza.

## Resolution

This is a straightforward synonym addition that requires minimal domain knowledge. The curator identified the correct term stanza in mondo-edit.obo and added the synonym with appropriate metadata. An automated agent should handle this type of task reliably given knowledge of OBO format synonym syntax and the Mondo synonym addition SOP.
