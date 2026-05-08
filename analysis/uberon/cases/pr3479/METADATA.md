---
repo: obophenotype/uberon
issue_number: 3478
pr_number: 3479
issue_title: "'late embryo' connected to effectively vertebrate-specific stages"
issue_created_at: "2025-02-12"
pr_author: gouttegd
pr_merged_at: "2025-02-13"
pr_num_commits: 1
files_changed:
  - path: src/ontology/uberon-edit.obo
    additions: 5
    deletions: 5
scoping: tightly_scoped
task_type: axiom_repair
difficulty: hard
scope: multi_term
review_outcome: approved_first_time
domain_area: developmental-anatomy
tags:
  - taxon-restriction
  - GCI
  - developmental-stage
  - chordate
  - pharyngula
curated_by: claude-opus-4
curated_at: "2026-05-08"
rationale: Taxon restriction correction using GCI axiom pattern to decouple a general stage from chordate-specific stages
---

## Context

Issue #3478 reported that UBERON:0007220 (late embryonic stage) was connected via a preceded_by axiom to UBERON:0004707 (pharyngula stage), a chordate-specific developmental stage. This made the late embryonic stage effectively vertebrate-specific, which is incorrect since many non-chordate organisms have a late embryonic stage. Additionally, the pharyngula and neurula stages had overly broad taxon restrictions (Eumetazoa) that needed tightening to Chordata.

## Changes Made

The PR made three changes in uberon-edit.obo: (1) narrowed the taxon restriction on pharyngula (UBERON:0004707) and neurula (UBERON:0000110) from Eumetazoa to Chordata; (2) replaced the direct SubClassOf preceded_by pharyngula axiom on late embryonic stage with a GCI (General Class Inclusion) axiom that applies only when the stage occurs in Chordata. This decouples the general late embryonic stage concept from chordate-specific developmental sequences.

## Resolution

Hard difficulty. An agent would need to understand GCI axiom patterns in OBO format, reason about taxon-appropriate developmental stage sequences, and recognize that a general stage concept should not be tied to taxon-specific precursors. The GCI pattern (class AND occurs_in some Taxon SubClassOf preceded_by some Stage) is an advanced OWL modeling technique. Same-day merge reflects the clear rationale provided in the issue.
