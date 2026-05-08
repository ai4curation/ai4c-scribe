---
repo: obophenotype/uberon
issue_number: 3657
pr_number: 3671
issue_title: "New term requests by HRA/HuBMAP"
issue_created_at: "2026-02-02"
pr_author: nicolevasilevsky
pr_merged_at: "2026-03-23"
pr_num_commits: 7
files_changed:
  - path: src/ontology/uberon-edit.obo
    additions: 55
    deletions: 0
scoping: tightly_scoped
task_type: new_term
difficulty: medium
scope: multi_term
review_outcome: approved_first_time
domain_area: oral-anatomy
tags:
  - HRA
  - HuBMAP
  - salivary-gland
  - new-term-request
curated_by: claude-opus-4
curated_at: "2026-05-08"
rationale: Multi-term addition requiring domain knowledge of salivary gland and oral anatomy structures
---

## Context

The HRA/HuBMAP project requested five new anatomical terms related to oral and salivary gland anatomy: salivary gland ducto-acinar unit, parotid gland ducto-acinar unit, sublingual gland ducto-acinar unit, submandibular gland ducto-acinar unit, and dentogingival junction. These terms were needed to support the Human Reference Atlas tissue mapping efforts.

## Changes Made

The PR added 55 lines to src/ontology/uberon-edit.obo, creating five new term stanzas with definitions, is_a relationships, and appropriate part_of axioms linking each ducto-acinar unit to its parent salivary gland structure. The dentogingival junction was placed in the appropriate oral anatomical hierarchy.

## Resolution

Medium difficulty. While the individual term additions follow standard OBO patterns, an agent would need domain knowledge to correctly place the ducto-acinar units under their parent gland structures and assign appropriate part_of relationships. The seven commits suggest iterative refinement during review. Merged after approximately seven weeks from issue creation.
