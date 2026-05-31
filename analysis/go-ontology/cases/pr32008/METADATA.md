---
repo: geneontology/go-ontology
issue_number: 25870
pr_number: 32008
issue_title: "GO terms with EC:1.13.11.37 xref"
issue_created_at: "2023-07-31"
pr_author: dragon-ai-agent
pr_merged_at: "2026-04-28"
pr_num_commits: 1
files_changed:
  - path: src/ontology/go-edit.obo
    additions: 7
    deletions: 8
  - path: src/ontology/imports/go-catalytic-activities-participants.owl
    additions: 0
    deletions: 31
scoping: tightly_scoped
task_type: obsoletion
difficulty: medium
scope: multi_term
review_outcome: approved_first_time
domain_area: molecular_function
tags:
  - obsoletion
  - enzymes
  - EC-xref
  - dioxygenase
  - import-cleanup
curated_by: claude-opus-4
curated_at: "2026-05-10"
rationale: Multi-file change involving both term obsoletion and OWL import cleanup, addressing a long-standing issue from 2023
case_quality: ok
case_quality_reason: sound_gold_but_multi_file_obsoletion_and_import_cleanup
quality_flagged_by: codex
quality_flagged_at: "2026-05-17"
---

## Context

Issue #25870 (opened July 2023) identified problems with GO terms carrying the EC:1.13.11.37 cross-reference. GO:0018581 "hydroxyquinol 1,2-dioxygenase activity" described only the first step of the reaction, while GO:0047074 described the complete reaction. This PR resolves the duplication by obsoleting GO:0018581 and renaming GO:0047074 to the more recognizable name.

## Changes Made

Two files were modified:
1. In `src/ontology/go-edit.obo`: GO:0018581 was obsoleted with `replaced_by: GO:0047074`, and GO:0047074 was renamed to "hydroxyquinol 1,2-dioxygenase activity" (taking the name from the obsoleted term since it is the more commonly used label)
2. In `src/ontology/imports/go-catalytic-activities-participants.owl`: Removed 31 lines of OWL axioms that referenced the obsoleted term's reaction participants

## Resolution

Merged directly. This addressed part of a long-standing issue (nearly 3 years old) about EC cross-reference alignment. The two-file change demonstrates that obsoletion can require cleanup in both the main edit file and the OWL imports that encode reaction participant relationships.
