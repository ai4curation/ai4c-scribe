---
repo: obophenotype/uberon
issue_number: 3522
pr_number: 3525
issue_title: "relationship is reversed between Uberon and NCIT for foramen secundum"
issue_created_at: "2025-05-15"
pr_author: rays22
pr_merged_at: "2025-05-27"
pr_num_commits: 2
files_changed:
  - path: src/ontology/uberon-edit.obo
    additions: 5
    deletions: 5
scoping: tightly_scoped
task_type: axiom_repair
difficulty: medium
scope: multi_term
review_outcome: approved_first_time
domain_area: cardiac-anatomy
tags:
  - logical-definition
  - equivalence-axiom
  - cardiac
  - foramen
curated_by: claude-opus-4
curated_at: "2026-05-08"
rationale: Logical definition repair for two cardiac foramen terms, replacing non-unique equivalence axioms with subclass assertions
---

## Context

Issue #3522 reported that the logical definition (equivalence axiom) for foramen secundum (UBERON:0006678) was reversed relative to NCIT, and that foramen primum (UBERON:0009149) had a non-unique equivalence axiom that could cause reasoning errors. Both terms relate to openings in the interatrial septum during cardiac development.

## Changes Made

For UBERON:0009149 (foramen primum), the non-unique equivalence axiom was replaced with two explicit subclass assertions. For UBERON:0006678 (foramen secundum), the incorrect equivalence axiom was similarly replaced with subclass assertions, and the text definition was corrected. The changes totaled 5 additions and 5 deletions in uberon-edit.obo.

## Resolution

Medium difficulty. An agent would need to understand the difference between equivalence axioms and subclass assertions in OBO/OWL, recognize when an equivalence axiom is non-unique or incorrect, and have sufficient cardiac embryology knowledge to verify the corrected relationships between foramen primum, foramen secundum, and the interatrial septum. Merged after twelve days with no changes requested.
