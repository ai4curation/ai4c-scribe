---
repo: monarch-initiative/mondo
issue_number: 9864
pr_number: 10105
issue_title: "Request for new term SYCE1-related gametogenic failure"
issue_created_at: "2026-01-07"
pr_author: MeeSiing
pr_merged_at: "2026-03-31"
pr_num_commits: 1
files_changed:
  - path: src/ontology/mondo-edit.obo
    additions: 12
    deletions: 0
scoping: tightly_scoped
task_type: new_term
difficulty: medium
scope: single_term
review_outcome: approved_first_time
curated_by: claude-opus-4
curated_at: "2026-05-10"
rationale: New term creation with logical definition and ClinGen label, requiring knowledge of DOSDP patterns and meiosis-related disease classification.
---

## Context

Issue #9864 requested a new term for "SYCE1-related gametogenic failure" describing a condition where variants in SYCE1 (synaptonemal complex central element protein 1) cause varying gametogenic phenotypes in both 46,XY and 46,XX individuals, ranging from spermatogenic failure to premature ovarian insufficiency.

## Changes Made

The PR created MONDO:1060214 with 12 additions to mondo-edit.obo: the term ID, label, definition referencing the gametogenic failure phenotype, ClinGen preferred label as exact synonym, logical definition (likely using the gene-related disease pattern linking to SYCE1), parent classification under gametogenic failure, and appropriate cross-references. The curator noted that child terms were not requested and would be handled by the reasoner.

## Resolution

Moderate difficulty because new term creation requires understanding of Mondo's DOSDP patterns, correct parent placement, and logical definition construction. The curator needed to craft a definition that captures the variable expressivity (both male and female presentations) and set up the logical axiom so the reasoner can infer additional classification. An agent would need knowledge of Mondo's term creation SOP and gene-disease patterns.
