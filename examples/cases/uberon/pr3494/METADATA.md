---
repo: obophenotype/uberon
issue_number: 3473
pr_number: 3494
issue_title: "Not all epithelia with squamous cells are squamous epithelium"
issue_created_at: "2025-02-04"
pr_author: dosumis
pr_merged_at: "2025-03-19"
pr_num_commits: 3
files_changed:
  - path: src/ontology/uberon-edit.obo
    additions: 15
    deletions: 18
scoping: tightly_scoped
task_type: axiom_repair
difficulty: hard
scope: multi_term
review_outcome: approved_first_time
domain_area: epithelial-tissue
tags:
  - definition-refinement
  - squamous-epithelium
  - cell-type
  - classification-logic
curated_by: claude-opus-4
curated_at: "2026-05-08"
rationale: Definitional correction requiring nuanced histological understanding of epithelial classification criteria
---

## Context

Issue #3473 identified that the definition of squamous epithelium in Uberon was too broad: not all epithelia containing squamous cells qualify as squamous epithelium. The distinction is histologically significant because transitional epithelium and stratified epithelia may contain squamous cells in their superficial layers without being classified as squamous epithelium proper.

## Changes Made

The PR modified 15 lines and removed 18 lines in uberon-edit.obo, refining the definition and logical axioms for squamous epithelium and related terms. The changes tightened the classification criteria so that the presence of squamous cells alone is insufficient for classification as squamous epithelium, requiring instead that the epithelium be predominantly composed of squamous cells or classified as such by standard histological criteria.

## Resolution

Hard difficulty. An agent would need deep histological knowledge to understand why the original definition was too permissive, distinguish between squamous epithelium proper and epithelia that merely contain squamous cells, and craft logical axioms that correctly capture this distinction without breaking existing classification hierarchies. The three commits over six weeks suggest careful deliberation.
