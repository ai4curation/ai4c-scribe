---
repo: obophenotype/cell-ontology
issue_number: 3597
pr_number: 3598
issue_title: "[NTR] Add mouth terms for HubMap"
issue_created_at: "2026-03-24"
pr_author: app/copilot-swe-agent
pr_merged_at: "2026-03-26"
pr_num_commits: 3
files_changed:
  - path: src/ontology/cl-edit.owl
    additions: 113
    deletions: 0
scoping: loosely_scoped
task_type: new_term
difficulty: hard
scope: multi_term
review_outcome: approved_first_time
domain_area: oral
tags:
  - NTR
  - mouth
  - salivary-gland
  - HuBMAP
  - batch-addition
  - oral-tissue
curated_by: claude-opus-4
curated_at: "2026-05-08"
rationale: Batch addition of 8 oral/salivary gland cell types with diverse axiom patterns for HuBMAP tissue annotation
---

## Context

The HuBMAP consortium requested cell type terms for oral and salivary gland tissue annotation as part of the broader HuBMAP term request effort (#3471). Issue #3597 specified 8 new cell types including serous demilune cells, basal duct cells, periductal fibroblasts, junctional epithelial cells, tuft cells of specific glands, ionocytes, and myoepithelial cells of salivary glands. Each requires specific anatomical contextualization within oral and salivary gland structures.

## Changes Made

Added 113 new lines to `cl-edit.owl` defining 8 new cell types. Each term follows the standard compositional pattern with EquivalentClasses axioms using intersectionOf with a parent cell type and part_of an UBERON anatomical structure. Terms include capability axioms (capable_of GO processes like saliva secretion, ion homeostasis, smooth muscle contraction) and synonym annotations with PMID cross-references as specified in the issue.

## Resolution

Approved on first review in just 3 commits, reflecting efficient implementation. Hard difficulty because the 8 terms span diverse parent cell types (epithelial cells, fibroblasts, ionocytes, myoepithelial cells) each requiring different axiom patterns, and the salivary gland anatomy involves specific UBERON structures (parotid, sublingual, submandibular) that must be correctly referenced.
