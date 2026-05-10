---
repo: geneontology/go-ontology
issue_number: 31966
pr_number: 32003
issue_title: "Obsolete GO:0043713 (R)-2-hydroxyisocaproate dehydrogenase activity"
issue_created_at: "2026-04-24"
pr_author: dragon-ai-agent
pr_merged_at: "2026-04-28"
pr_num_commits: 1
files_changed:
  - path: src/ontology/go-edit.obo
    additions: 6
    deletions: 3
scoping: tightly_scoped
task_type: obsoletion
difficulty: medium
scope: single_term
review_outcome: approved_first_time
domain_area: molecular_function
tags:
  - obsoletion
  - enzymes
  - dehydrogenase
  - EC-alignment
  - replaced_by
curated_by: claude-opus-4
curated_at: "2026-05-10"
rationale: Enzyme obsoletion requiring biochemical knowledge to identify the correct broader replacement term
---

## Context

Issue #31966 requested obsoletion of GO:0043713 "(R)-2-hydroxyisocaproate dehydrogenase activity". Per @sjm41's analysis, this term had no direct EC cross-reference, but "(R)-2-hydroxyisocaproate dehydrogenase" is listed as a synonym of EC:1.1.1.345, which corresponds to GO:0140175 "(2R)-2-hydroxyacid dehydrogenase (NAD+) activity". The specific substrate (isocaproate) is just one instance of the broader (2R)-2-hydroxyacid class.

## Changes Made

In `src/ontology/go-edit.obo`, GO:0043713 was obsoleted:
- Marked `is_obsolete: true`
- Added `replaced_by: GO:0140175` for annotation migration
- Removed logical axioms
- The replacement points annotators to the correct broader activity term

## Resolution

Merged directly. The biochemical reasoning was clearly laid out in the issue: the specific substrate term (isocaproate) is subsumed by the generic substrate class term ((2R)-2-hydroxyacid). This is a typical enzyme term consolidation where overly specific terms are replaced by appropriately general ones that match EC classification granularity.
