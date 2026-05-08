---
repo: obophenotype/uberon
issue_number: 3475
pr_number: 3477
issue_title: "Remove Thoracic dorsal root ganglion as a part of thoracic ganglion"
issue_created_at: "2025-02-06"
pr_author: tgbugs
pr_merged_at: "2025-04-24"
pr_num_commits: 1
files_changed:
  - path: src/ontology/uberon-edit.obo
    additions: 0
    deletions: 1
scoping: tightly_scoped
task_type: axiom_repair
difficulty: medium
scope: single_term
review_outcome: approved_first_time
domain_area: neuroanatomy
tags:
  - subclass-removal
  - ganglion
  - classification-error
  - dorsal-root
curated_by: claude-opus-4
curated_at: "2026-05-08"
rationale: Single axiom removal requiring understanding of the distinction between paravertebral and dorsal root ganglia
---

## Context

Issue #3475 reported that UBERON:0002835 (thoracic dorsal root ganglion) was incorrectly classified as a subclass of UBERON:0000961 (thoracic ganglion). The thoracic ganglion in Uberon refers to a paravertebral ganglion of the sympathetic trunk, while a dorsal root ganglion is a sensory ganglion. These are fundamentally different types of ganglia despite both being located in the thoracic region.

## Changes Made

The PR removed a single is_a line from uberon-edit.obo, deleting the incorrect SubClassOf axiom that placed thoracic dorsal root ganglion under thoracic ganglion. No replacement axiom was needed since the dorsal root ganglion already had correct classification through its other parent terms.

## Resolution

Medium difficulty. While the change is a single line deletion, an agent would need to understand the neuroanatomical distinction between dorsal root ganglia (sensory, spinal nerve associated) and paravertebral ganglia (autonomic, sympathetic trunk associated) to verify that the removal is correct and that no replacement axiom is needed. The two-month gap between issue and merge suggests the fix waited for a batch merge cycle.
