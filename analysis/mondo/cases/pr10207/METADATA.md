---
repo: monarch-initiative/mondo
issue_number: 9896
pr_number: 10207
issue_title: "GCSH-related glycine encephalopathy"
issue_created_at: "2026-01-23"
pr_author: MeeSiing
pr_merged_at: "2026-05-01"
pr_num_commits: 2
files_changed:
  - path: src/ontology/mondo-edit.obo
    additions: 4
    deletions: 0
scoping: tightly_scoped
task_type: synonym_update
difficulty: simple
scope: single_term
review_outcome: changes_requested
curated_by: claude-opus-4
curated_at: "2026-05-10"
rationale: Synonym addition with an additional cleanup commit removing an incorrect subset annotation.
---

## Context

Issue #9896 requested relabeling MONDO:0957382 (multiple mitochondrial dysfunctions syndrome 7) to "GCSH-related glycine encephalopathy" following ClinGen gene-centric naming. The request included ORCID 0000-0002-* for nano-attribution and proposed the gene-based label as the preferred name.

## Changes Made

The PR was completed in 2 commits. The first added "GCSH-related glycine encephalopathy" as an exact synonym to MONDO:0957382. The second commit removed an incorrect subset annotation that was discovered during the initial edit. The net result is 4 additions with no deletions, adding the synonym and cleaning up metadata.

## Resolution

Simple difficulty overall, though the second commit shows that curators often catch incidental issues while editing a term stanza. The subset removal suggests the term was incorrectly tagged (perhaps in an outdated classification subset). An agent should ideally flag such incidental quality issues when encountered but may need human guidance on whether to fix them in the same PR.
