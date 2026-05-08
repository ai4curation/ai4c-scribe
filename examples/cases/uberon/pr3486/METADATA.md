---
repo: obophenotype/uberon
issue_number: 3354
pr_number: 3486
issue_title: "ZFA/Uberon issues: simple errors in Uberon"
issue_created_at: "2024-09-04"
pr_author: gouttegd
pr_merged_at: "2025-03-06"
pr_num_commits: 4
files_changed:
  - path: src/ontology/uberon-edit.obo
    additions: 3
    deletions: 4
scoping: tightly_scoped
task_type: axiom_repair
difficulty: hard
scope: multi_term
review_outcome: approved_first_time
domain_area: cross-species-anatomy
tags:
  - ZFA-compatibility
  - uvea
  - brain-vesicle
  - scale-circulus
  - materiality
curated_by: claude-opus-4
curated_at: "2026-05-08"
rationale: Three independent cross-species compatibility fixes requiring deep reasoning about anatomical materiality and spatial relationships
---

## Context

Issue #3354 reported three incompatibility issues between Uberon and ZFA (Zebrafish Anatomy Ontology). First, UBERON:0001768 (uvea) was incorrectly asserted as part_of the anterior segment of eyeball, but the uvea spans both anterior and posterior segments. Second, UBERON:0013150 (future brain vesicle) was incorrectly classified as an immaterial open anatomical space, inconsistent with its child terms (brain ventricles) being material structures. Third, UBERON:2002051 (scale circulus) was incorrectly classified as an immaterial anatomical line, when ZFA and published literature indicate circuli are material structures.

## Changes Made

The PR made three targeted corrections in uberon-edit.obo: removed the incorrect part_of axiom linking uvea to the anterior segment, reclassified future brain vesicle from immaterial to material entity, and reclassified scale circulus from anatomical line to a material structure. Each fix required independent anatomical reasoning supported by literature references.

## Resolution

Hard difficulty despite the small diff (3 additions, 4 deletions). An agent would need to reason about anatomical spatial relationships (uvea spanning anterior and posterior eye segments), ontological materiality distinctions (BFO material vs immaterial entities), and cross-species consistency with ZFA. Each of the three fixes requires independent domain knowledge and careful consideration of downstream inference impacts.
