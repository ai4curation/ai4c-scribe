---
repo: obophenotype/uberon
issue_number: 3596
pr_number: 3597
issue_title: "Revise lofical definition causing violations of taxon constraints"
issue_labels:
  - logical definition
issue_created_at: "2025-08-14"
issue_closed_at: "2025-08-14"
pr_author: aleixpuigb
pr_merged_at: "2025-08-14"
pr_num_commits: 1
files_changed:
  - path: src/ontology/uberon-edit.obo
    additions: 2
    deletions: 2
scoping: tightly_scoped
task_type: axiom_repair
difficulty: hard
scope: multi_term
review_outcome: approved_first_time
domain_area: comparative-anatomy
tags:
  - logical-definition
  - taxon-constraint
  - epiphyseal-tract
  - adductor-muscle
curated_by: claude-opus-4
curated_at: "2026-05-08"
rationale: Taxon constraint violations require understanding how logical definitions interact with species-specific anatomy
case_quality: ok
case_quality_reason: sound_gold_but_taxon_constraint_repair_requires_reasoner_context
quality_flagged_by: codex
quality_flagged_at: "2026-05-17"
---

## Context

Two terms had logical definitions that caused violations of taxon constraints. The epiphyseal tract was defined as innervating the parietal organ (which is taxon-restricted), and the adductor muscle of hip had a similarly problematic logical definition. Both needed revision to avoid reasoning errors.

## Changes Made

For the epiphyseal tract, changed the innervation target from parietal organ to pineal complex, which is the correct broader structure. For the adductor muscle of hip, revised the logical definition to avoid the taxon constraint violation. Two lines changed, two lines added.

## Resolution

Hard difficulty because taxon constraint violations require understanding how OWL reasoning propagates constraints through logical definitions. The agent must know that if term A is defined as "innervates B" and B is restricted to taxon X, then A inherits that restriction. Fixing requires choosing alternative logical definition targets that are taxonomically broader while remaining anatomically accurate.
