---
repo: monarch-initiative/mondo
issue_number: 9859
pr_number: 10219
issue_title: "primary hypophysitis synonyms"
issue_labels:
  - synonym
  - user request
issue_created_at: "2026-01-06"
pr_author: MeeSiing
pr_merged_at: "2026-05-04"
pr_num_commits: 6
files_changed:
  - path: src/ontology/mondo-edit.obo
    additions: 45
    deletions: 18
scoping: tightly_scoped
scoping_notes: All changes are within the hypophysitis branch of the ontology, restructuring subtypes.
task_type: reclassification
difficulty: hard
scope: multiple_terms
review_outcome: approved_with_revisions
domain_area: rare-disease
tags:
  - hypophysitis
  - reclassification
  - hierarchy-restructure
  - autoimmune
curated_by: claude-opus-4
curated_at: "2026-05-08"
rationale: Complex hierarchy restructure requiring domain knowledge about hypophysitis subtypes and careful reclassification
---

## Context

A user request was filed to update synonyms for primary hypophysitis. However, the resolution required a broader restructuring of the hypophysitis branch. The existing classification conflated primary vs secondary hypophysitis with histological subtypes (lymphocytic, granulomatous, etc.), making the hierarchy confusing.

The issue required domain expertise to determine that histological and anatomical subtypes should be classified as children of hypophysitis rather than maintaining the primary/secondary distinction, which is clinically less useful for classification purposes.

## Changes Made

The PR relabeled MONDO:0019835 to "lymphocytic hypophysitis" and restructured all histological and anatomical subtypes as child terms under the main hypophysitis term. With 6 commits, 45 additions and 18 deletions, this involved modifying multiple term stanzas to correct parent-child relationships and update labels.

## Resolution

This is a hard case because it requires understanding the clinical distinction between primary/secondary hypophysitis and histological subtypes, then making a judgment call about how best to restructure the hierarchy. An agent would need domain knowledge about hypophysitis classification and the ability to reorganize multiple related terms consistently while preserving cross-references.
