---
repo: obophenotype/cell-ontology
issue_number: 3534
pr_number: 3535
issue_title: "[NTR] hybrid osteochondral skeletal cell"
issue_created_at: "2025-12-16"
pr_author: app/copilot-swe-agent
pr_merged_at: "2026-02-04"
pr_num_commits: 7
files_changed:
  - path: src/ontology/cl-edit.owl
    additions: 13
    deletions: 0
scoping: tightly_scoped
task_type: new_term
difficulty: medium
scope: single_term
review_outcome: approved_first_time
domain_area: skeletal
tags:
  - NTR
  - osteochondral
  - hybrid-cell
  - skeletal
  - bone-cartilage
curated_by: claude-opus-4
curated_at: "2026-05-08"
rationale: New term for a hybrid cell type at the bone-cartilage interface requiring understanding of dual osteogenic and chondrogenic identity
case_quality: ok
case_quality_reason: sound_gold_but_new_term_scores_sensitive_to_taxon_and_provenance
quality_flagged_by: codex
quality_flagged_at: "2026-05-17"
---

## Context

A new term was requested for the hybrid osteochondral skeletal cell, a recently characterized cell type found at the interface between bone and cartilage tissue that co-expresses both osteogenic and chondrogenic markers. This cell type represents a distinct population that does not fit neatly into either the osteoblast or chondrocyte lineage, reflecting the growing recognition of cellular plasticity in skeletal tissues.

## Changes Made

Added 13 new lines to `cl-edit.owl` defining the hybrid osteochondral skeletal cell with class declaration, label, textual definition citing recent single-cell RNA sequencing studies, parentage under skeletal cell, and logical axioms that capture both its osteogenic and chondrogenic characteristics without forcing it into a single lineage.

## Resolution

Approved on first review in 7 commits. Medium difficulty because modeling a hybrid cell type requires careful ontological decisions about parentage -- it cannot simply be a subclass of both osteoblast and chondrocyte, but needs to be represented as a distinct entity that shares properties of both lineages.
