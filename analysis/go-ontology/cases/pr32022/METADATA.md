---
repo: geneontology/go-ontology
issue_number: 31873
pr_number: 32022
issue_title: "Obsoletion request: GO:0061817 endoplasmic reticulum-plasma membrane tethering"
issue_created_at: "2026-04-10"
pr_author: dragon-ai-agent
pr_merged_at: "2026-05-04"
pr_num_commits: 1
files_changed:
  - path: src/ontology/go-edit.obo
    additions: 7
    deletions: 5
scoping: tightly_scoped
task_type: obsoletion
difficulty: medium
scope: single_term
review_outcome: approved_first_time
domain_area: biological_process
tags:
  - obsoletion
  - MF_in_BP
  - membrane-tethering
  - ER
  - plasma-membrane
curated_by: claude-opus-4
curated_at: "2026-05-10"
rationale: Part of systematic effort to reclassify membrane tethering terms from BP to MF namespace, demonstrating ontological namespace correction
case_quality: good
case_quality_reason: single_complete_gold_pr
quality_flagged_by: codex
quality_flagged_at: "2026-05-17"
---

## Context

Issue #31873 was part of a broader initiative to correct membrane tethering terms that were incorrectly placed in the biological_process namespace. GO:0061817 "endoplasmic reticulum-plasma membrane tethering" described what is fundamentally a molecular function (binding activity that brings two membranes together) rather than a biological process. This is one of many related obsoletion requests (tagged "MF_in_BP") addressing this systematic error.

## Changes Made

In `src/ontology/go-edit.obo`, GO:0061817 was obsoleted:
- Marked `is_obsolete: true`
- Removed logical axioms and relationships
- Added appropriate `consider` tags pointing curators to the correct MF replacement terms
- The corresponding MF tether activity term already existed from earlier PRs in this series

## Resolution

Merged directly without review. The obsoletion was part of a well-established pattern where biological_process terms describing membrane-membrane tethering activities are being systematically obsoleted and replaced by molecular_function tether activity terms. The clear rationale and established precedent made this straightforward.
