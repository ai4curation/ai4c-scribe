---
repo: monarch-initiative/mondo
issue_number: 9795
pr_number: 10110
issue_title: "[Obsolete] OMIM merges"
issue_labels:
  - obsolete
  - merge
  - on list
  - user request
issue_created_at: "2025-11-26"
pr_author: MeeSiing
pr_merged_at: "2026-04-02"
pr_num_commits: 1
files_changed:
  - path: src/ontology/mondo-edit.obo
    additions: 14
    deletions: 28
scoping: tightly_scoped
scoping_notes: PR merges one obsolete term into a surviving term, transferring annotations.
task_type: obsoletion
difficulty: medium
scope: single_term
review_outcome: approved_first_time
domain_area: rare-disease
tags:
  - merge
  - obsoletion
  - Usher-syndrome
  - hearing-loss
  - OMIM
curated_by: claude-opus-4
curated_at: "2026-05-08"
rationale: Term merge requiring analysis of whether Usher syndrome type 1J and nonsyndromic hearing loss 48 are the same entity
---

## Context

As part of a broader OMIM merge review (issue #9795), Usher syndrome type 1J was identified for merger into MONDO:0012273 (autosomal recessive nonsyndromic hearing loss 48). OMIM had consolidated these entries, and Mondo needed to follow suit. The decision required evaluating whether the syndromic (Usher) and nonsyndromic (hearing loss) presentations truly represent the same genetic entity.

Supporting documentation was maintained in a shared Google Doc tracking all OMIM merges for this batch.

## Changes Made

Merged Usher syndrome type 1J into MONDO:0012273 by obsoleting the Usher term and transferring its cross-references and annotations to the surviving hearing loss term. The 14 additions and 28 deletions reflect that more content was removed (obsoleted stanza) than added (transferred annotations plus obsoletion metadata).

## Resolution

Medium difficulty because the curator must evaluate whether merging a syndromic presentation (Usher syndrome, which includes retinal degeneration) with a nonsyndromic hearing loss term is scientifically justified. This requires understanding the genetic basis and phenotypic spectrum of the underlying mutation, not just following OMIM's lead blindly.
