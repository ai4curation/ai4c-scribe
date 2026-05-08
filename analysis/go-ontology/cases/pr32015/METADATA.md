---
repo: geneontology/go-ontology
issue_number: 31961
pr_number: 32015
issue_title: "obsolete GO:0008785 alkyl hydroperoxide reductase activity"
issue_labels:
  - enzymes
  - obsoletion
issue_created_at: "2026-04-24"
issue_closed_at: "2026-04-29"
pr_author: dragon-ai-agent
pr_merged_at: "2026-04-29"
pr_num_commits: 2
files_changed:
  - path: src/ontology/go-edit.obo
    additions: 5
    deletions: 2
scoping: tightly_scoped
scoping_notes: All changes directly address the obsoletion of the single term GO:0008785.
task_type: obsoletion
difficulty: simple
scope: single_term
review_outcome: approved_first_time
domain_area: molecular_function
tags:
  - enzyme
  - peroxidase
  - EC:1.11.1.26
curated_by: claude-opus-4
curated_at: "2026-05-03"
rationale: Clean single-term obsoletion with well-reasoned replaced_by, demonstrates standard obsoletion pattern
---

## Context

GO:0008785 "alkyl hydroperoxide reductase activity" was flagged for obsoletion because, despite its generic-sounding name, it represented a substrate-specific activity more specific than any known gene product. The enzyme name "alkyl hydroperoxide reductase" is actually listed as a synonym of EC:1.11.1.26 (NADH-dependent peroxiredoxin activity), which corresponds to GO:0102039.

## Changes Made

In `src/ontology/go-edit.obo`, the term GO:0008785 was modified:

- Name prefixed with "obsolete" -> "obsolete alkyl hydroperoxide reductase activity"
- Definition prefixed with "OBSOLETE."
- Added explanatory comment about why the term was obsoleted (substrate specificity mismatch with EC:1.11.1.26)
- Removed `is_a` relationship to GO:0016668 (oxidoreductase activity, acting on a sulfur group of donors, NAD(P) as acceptor)
- Added `is_obsolete: true`
- Added `replaced_by: GO:0102039` (NADH-dependent peroxiredoxin activity)
- Added term_tracker_item linking to issue #31961

## Resolution

Straightforward obsoletion following standard OBO pattern. The key reasoning was identifying that GO:0102039 is the correct replacement based on EC number alignment (EC:1.11.1.26). Approved without changes on first review.
