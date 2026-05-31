---
repo: geneontology/go-ontology
issue_number: 31876
pr_number: 31953
issue_title: "Obsoletion request: GO:0140057 vacuole-mitochondria membrane tethering"
issue_created_at: "2026-04-10"
pr_author: dragon-ai-agent
pr_merged_at: "2026-04-23"
pr_num_commits: 2
files_changed:
  - path: src/ontology/go-edit.obo
    additions: 5
    deletions: 3
scoping: tightly_scoped
task_type: obsoletion
difficulty: simple
scope: single_term
review_outcome: approved_first_time
domain_area: biological_process
tags:
  - obsoletion
  - MF_in_BP
  - membrane-tethering
  - vacuole
  - mitochondria
  - no-replacement
curated_by: claude-opus-4
curated_at: "2026-05-10"
rationale: Obsoletion without replacement demonstrating the case where a term was added in error and no corresponding MF term is needed
case_quality: good
case_quality_reason: single_complete_gold_pr
quality_flagged_by: codex
quality_flagged_at: "2026-05-17"
---

## Context

Issue #31876 requested obsoletion of GO:0140057 "vacuole-mitochondria membrane tethering" as part of the broader MF_in_BP cleanup initiative. Unlike some other membrane tethering terms in this series, this one was flagged as having been "added in error" with no replacement term needed -- the specific vacuole-mitochondria tethering concept was not judged to warrant its own MF term.

## Changes Made

In `src/ontology/go-edit.obo`, GO:0140057 was obsoleted:
- Marked `is_obsolete: true`
- No `replaced_by` tag (term added in error, no replacement warranted)
- Removed logical axioms
- Impact analysis confirmed no internal ontology references or external annotations existed

## Resolution

Merged after 2 commits (likely a minor formatting fix in the second commit). The key distinction from other membrane tethering obsoletions is that no replacement MF term was created. Per @raymond91125's assessment, the vacuole-mitochondria tethering concept at this granularity does not need representation in GO.
