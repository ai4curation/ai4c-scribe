---
repo: obophenotype/uberon
issue_number: 3629
pr_number: 3630
issue_title: "[NTR] carotid artery intima-media region"
issue_labels:
  - new term request
issue_created_at: "2025-11-14"
issue_closed_at: "2025-11-25"
pr_author: dragon-ai-agent
pr_merged_at: "2025-11-25"
pr_num_commits: 4
files_changed:
  - path: src/ontology/uberon-edit.obo
    additions: 15
    deletions: 0
scoping: tightly_scoped
task_type: new_term
difficulty: medium
scope: single_term
review_outcome: approved_first_time
domain_area: cardiovascular-anatomy
tags:
  - new-term
  - carotid-artery
  - cardiovascular
  - clinical-anatomy
curated_by: claude-opus-4
curated_at: "2026-05-08"
rationale: Clinical anatomy NTR requiring understanding of vessel wall layers and composite region modeling
---

## Context

A new term was requested for the carotid artery intima-media region, a composite anatomical region of the carotid artery wall comprising the tunica intima and tunica media. This region is clinically significant as the target of carotid intima-media thickness (CIMT) measurements, a common cardiovascular risk biomarker.

## Changes Made

Added UBERON:9900000 for "carotid artery intima-media region" with a definition describing the composite wall region, appropriate synonyms, and relationships placing it as part of the carotid artery. The 4 commits suggest some iteration was needed to get the term stanza correct.

## Resolution

Medium difficulty because the term describes a composite anatomical region (two layers of a vessel wall considered together) rather than a single discrete structure. An agent must understand vascular anatomy and how to model a region that spans multiple tissue layers. Approved on first review.
