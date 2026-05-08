---
repo: geneontology/go-ontology
issue_number: 32046
pr_number: 32047
issue_title: "NTR: [double-stranded RNA immune receptor activity]"
issue_created_at: "2026-05-07"
pr_author: dragon-ai-agent
pr_merged_at: "2026-05-07"
pr_num_commits: 1
files_changed:
  - path: src/ontology/go-edit.obo
    additions: 25
    deletions: 0
scoping: tightly_scoped
task_type: new_term
difficulty: medium
scope: multi_term
review_outcome: approved_first_time
curated_by: claude-opus-4
curated_at: "2026-05-08"
rationale: Two new MF terms in a parent-child hierarchy requiring accurate immunology knowledge about cytosolic RNA sensors
---

## Context

A new term request was filed for molecular function terms covering cytosolic double-stranded RNA immune receptor activity. The existing GO term `GO:0038187 pattern recognition receptor activity` lacked specific children for dsRNA sensors such as NLRP1, NLRP6, IFIH1/MDA5, and ZBP1. The request came from a signaling domain expert who needed these terms for annotation of innate immune signaling pathways.

## Changes Made

Two new terms were added to `go-edit.obo` in a parent-child relationship: GO:7770072 `double-stranded RNA immune receptor activity` as a child of `GO:0038187 pattern recognition receptor activity`, covering broad cytosolic dsRNA sensors, and GO:7770073 `left-handed Z-RNA immune receptor activity` as a more specific child term covering ZBP1-type receptors that specifically recognize the Z-RNA conformation of dsRNA.

## Resolution

The PR was created and merged within the same day by the AI agent. The task required medium difficulty because the two terms needed to correctly reflect the immunological distinction between general dsRNA recognition (by sensors like MDA5) and the specialized Z-RNA conformation recognition (by ZBP1), which is a relatively recent discovery in innate immunity. The hierarchical relationship between the two terms had to be biologically accurate.
