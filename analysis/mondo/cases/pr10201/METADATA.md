---
repo: monarch-initiative/mondo
issue_number: 9871
pr_number: 10201
issue_title: "MONDO:0009106 diastematomyelia"
issue_created_at: "2026-01-12"
pr_author: MeeSiing
pr_merged_at: "2026-05-04"
pr_num_commits: 5
files_changed:
  - path: src/ontology/mondo-edit.obo
    additions: 59
    deletions: 21
scoping: loosely_scoped
task_type: other
difficulty: medium
scope: multi_term
review_outcome: changes_requested
curated_by: claude-opus-4
curated_at: "2026-05-10"
rationale: Initially a simple xref fix that expanded into creating 3 subtypes after investigation of split cord malformation classification.
---

## Context

Issue #9871 reported that MONDO:0009106 (diastematomyelia) had an incorrect Orphanet cross-reference (Orphanet:1671 for "Split cord malformation type I" rather than the broader concept). Investigation revealed that Orphanet:573278 correctly maps to the broader concept of diastematomyelia/split cord malformation, and that subtypes (type I with osseous spur, type II with fibrous septum) should be represented.

## Changes Made

The PR evolved from a simple xref correction into a multi-term edit across 5 commits. The initial commit updated the Orphanet xref from 1671 to 573278. A proxy merge was fixed in the second commit. The third commit added 3 new subtypes (MONDO:1060220-1060222) for split cord malformation classification. The fourth and fifth commits resolved merge conflicts with master. The 59 additions and 21 deletions reflect both the xref correction and the creation of new subtype terms with definitions, synonyms, and parent axioms.

## Resolution

Moderate difficulty because the scope expanded significantly from the original request. What began as a cross-reference correction required domain knowledge about split cord malformation types to realize that subtypes were needed. The merge conflicts and multiple commits show iterative development. An agent would need to recognize when an xref discrepancy indicates a deeper modeling issue requiring new terms.
