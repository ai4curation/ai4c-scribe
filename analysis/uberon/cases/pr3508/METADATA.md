---
repo: obophenotype/uberon
issue_number: 2911
pr_number: 3508
issue_title: "relation error: conus arteriosus has_part *uterine tube"
issue_created_at: "2023-06-06"
pr_author: cmungall
pr_merged_at: "2025-04-23"
pr_num_commits: 2
files_changed:
  - path: src/ontology/uberon-edit.obo
    additions: 2
    deletions: 2
scoping: tightly_scoped
task_type: axiom_repair
difficulty: medium
scope: multi_term
review_outcome: approved_first_time
domain_area: cardiac-anatomy
tags:
  - relation-error
  - homonym-confusion
  - conus-arteriosus
  - uterine-tube
curated_by: claude-opus-4
curated_at: "2026-05-08"
rationale: Axiom repair fixing cross-system anatomical confusion caused by the homonymous term "infundibulum"
case_quality: good
case_quality_reason: single_complete_axiom_repair_gold_pr
quality_flagged_by: codex
quality_flagged_at: "2026-05-17"
---

## Context

Issue #2911 reported that UBERON:0007181 (serosa of infundibulum of uterine tube) and UBERON:0007182 (muscle layer of infundibulum of uterine tube) had erroneous part_of relationships to UBERON:0003983 (conus arteriosus), a cardiac structure. The error likely arose because "infundibulum" is used in both cardiac anatomy (infundibulum of the right ventricle / conus arteriosus) and reproductive anatomy (infundibulum of the uterine tube).

## Changes Made

The PR removed the incorrect part_of relationships linking the two uterine tube structures to the conus arteriosus. Two lines were replaced in uberon-edit.obo, correcting the relationship targets so that the uterine tube structures relate only to the uterine tube infundibulum, not the cardiac infundibulum.

## Resolution

Medium difficulty. An agent would need to recognize the homonym-based confusion between cardiac and reproductive uses of "infundibulum," identify which relationships are erroneous, and remove them without affecting the correct uterine tube hierarchy. The issue was open for nearly two years before resolution. Co-authored by the dragon-ai-agent.
