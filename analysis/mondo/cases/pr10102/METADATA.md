---
repo: monarch-initiative/mondo
issue_number: 9771
pr_number: 10102
issue_title: "[Obsolete] 'heart, malformation of' (MONDO:0009327)"
issue_labels:
  - obsolete
  - on list
issue_created_at: "2025-11-19"
pr_author: sabrinatoro
pr_merged_at: "2026-03-31"
pr_num_commits: 1
files_changed:
  - path: src/ontology/mondo-edit.obo
    additions: 9
    deletions: 10
scoping: tightly_scoped
scoping_notes: PR obsoletes a single term with appropriate replaced_by annotation.
task_type: obsoletion
difficulty: simple
scope: single_term
review_outcome: approved_first_time
domain_area: congenital-disease
tags:
  - obsoletion
  - heart-malformation
  - congenital
  - OMIM
curated_by: claude-opus-4
curated_at: "2026-05-08"
rationale: Straightforward obsoletion of a vague legacy term following standard Mondo obsoletion patterns
---

## Context

MONDO:0009327 "heart, malformation of" was identified as an overly vague legacy term that did not add value to the ontology. The term originated from an OMIM entry but lacked the specificity needed for a useful disease classification. Such terms are periodically reviewed and obsoleted when they do not represent a distinct disease entity.

## Changes Made

Obsoleted MONDO:0009327 by marking it as obsolete, removing its classification axioms, and adding appropriate replaced_by and consider annotations to redirect users to more specific terms. The 9 additions and 10 deletions reflect the standard obsoletion pattern: removing active axioms and adding obsoletion metadata.

## Resolution

Easy difficulty because this follows the standard Mondo obsoletion pattern. The curator needs to mark the term as obsolete, remove is_a parents and logical definitions, and add replaced_by or consider pointers. An agent should be able to handle this with knowledge of the obsoletion SOP.
