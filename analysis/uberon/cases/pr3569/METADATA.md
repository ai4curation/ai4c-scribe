---
repo: obophenotype/uberon
issue_number: 3457
pr_number: 3569
issue_title: "Track the addition of VCCF vasculature terms here"
issue_created_at: "2024-12-24"
pr_author: ar-ibrahim
pr_merged_at: "2025-07-03"
pr_num_commits: 6
files_changed:
  - path: src/patterns/data/default/artery_and_arteriole_pattern.tsv
    additions: 4
    deletions: 0
  - path: src/patterns/data/default/vein_and_venule_pattern.tsv
    additions: 3
    deletions: 0
  - path: src/patterns/definitions.owl
    additions: 106
    deletions: 2
scoping: tightly_scoped
task_type: new_term
difficulty: medium
scope: multi_term
review_outcome: changes_requested
domain_area: vascular-anatomy
tags:
  - VCCF
  - vasculature
  - DOSDP-pattern
  - artery
  - vein
curated_by: claude-opus-4
curated_at: "2026-05-08"
rationale: Pattern-based vasculature term addition using DOSDP templates, part of a multi-PR series for VCCF integration
---

## Context

Issue #3457 tracked the addition of vasculature terms from the Vasculature Common Coordinate Framework (VCCF) into Uberon. This was the fifth PR in a series (following PRs #3497, #3513, #3559, #3566) adding batches of arterial and venous terms. Seven new terms were added in this installment.

## Changes Made

The PR added four new entries to the artery_and_arteriole_pattern.tsv and three to the vein_and_venule_pattern.tsv DOSDP pattern data files. The definitions.owl file was updated with 106 new lines containing the generated logical definitions and annotations for the new vasculature terms, linking them to their anatomical regions via supplies/drains relationships.

## Resolution

Medium difficulty. An agent would need to understand the DOSDP (Dead Simple OWL Design Patterns) framework used for systematic vasculature term creation, populate the correct pattern data TSV files with appropriate anatomical region references, and ensure the generated OWL definitions are consistent with existing vasculature terms. The six commits and multi-PR series suggest iterative review feedback across the batch import effort.
