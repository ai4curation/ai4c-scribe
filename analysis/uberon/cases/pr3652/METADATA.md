---
repo: obophenotype/uberon
issue_number: 3651
pr_number: 3652
issue_title: "Newly introduced disjointness axioms cause OBO serialisation issue"
issue_created_at: "2026-01-19"
pr_author: aleixpuigb
pr_merged_at: "2026-01-21"
pr_num_commits: 7
files_changed:
  - path: src/ontology/uberon-edit.obo
    additions: 0
    deletions: 8
  - path: src/ontology/components/disjoint_union_over.owl
    additions: 1
    deletions: 0
  - path: src/ontology/imports/merged_import.owl
    additions: 7012
    deletions: 6419
scoping: tightly_scoped
task_type: other
difficulty: hard
scope: structural_refactor
review_outcome: approved_first_time
domain_area: ontology-infrastructure
tags:
  - disjointness
  - OBO-serialisation
  - ODK-component
  - refactor
curated_by: claude-opus-4
curated_at: "2026-05-08"
rationale: Structural refactoring moving disjoint axioms between files to fix OBO serialisation, requiring ODK pipeline understanding
---

## Context

Issue #3651 reported that newly introduced disjointness axioms in uberon-edit.obo were causing OBO serialisation problems. The OBO format has limited support for certain OWL axiom patterns, and disjoint union axioms needed to be housed in a dedicated OWL component file rather than in the OBO edit file.

## Changes Made

The PR removed eight lines of disjoint axioms from src/ontology/uberon-edit.obo and relocated them to the OWL component file src/ontology/components/disjoint_union_over.owl. The merged_import.owl file was regenerated with significant churn (7012 additions, 6419 deletions) as a side effect of the pipeline rebuild. Seven commits indicate iterative refinement during the migration.

## Resolution

Hard difficulty. An agent would need to understand the limitations of OBO format serialisation for disjoint union axioms, know that the ODK pipeline supports component-based OWL files for axioms that cannot be represented in OBO, and correctly move the axioms while ensuring the build pipeline picks them up. The large diff in merged_import.owl is a pipeline artifact, not manual editing. Two-day turnaround from issue to merge.
