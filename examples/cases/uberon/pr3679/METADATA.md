---
repo: obophenotype/uberon
issue_number: 3678
pr_number: 3679
issue_title: "Add bone part terms from HubMap - HRA"
issue_created_at: "2026-03-20"
pr_author: dosumis
pr_merged_at: "2026-03-25"
pr_num_commits: 5
files_changed:
  - path: src/templates/hra-skeleton.template.tsv
    additions: 286
    deletions: 0
  - path: src/ontology/components/hra_skeleton.owl
    additions: 5156
    deletions: 0
  - path: src/templates/hra-skeleton-prefixes.owl
    additions: 15
    deletions: 0
  - path: src/ontology/uberon-odk.yaml
    additions: 4
    deletions: 0
  - path: src/ontology/uberon.Makefile
    additions: 10
    deletions: 0
  - path: src/ontology/Makefile
    additions: 12
    deletions: 4
  - path: src/ontology/catalog-v001.xml
    additions: 1
    deletions: 0
  - path: docs/odk-workflows/RepositoryFileStructure.md
    additions: 1
    deletions: 0
  - path: src/templates/hra-skeleton-reports/corrections_report.md
    additions: 79
    deletions: 0
  - path: src/templates/hra-skeleton-reports/duplicate_candidates_report.md
    additions: 1536
    deletions: 0
  - path: src/templates/hra-skeleton-reports/term_mapping_table.md
    additions: 119
    deletions: 0
scoping: tightly_scoped
task_type: new_term
difficulty: hard
scope: multi_term
review_outcome: approved_first_time
domain_area: skeletal-anatomy
tags:
  - HRA
  - HuBMAP
  - ROBOT-template
  - batch-import
  - component
curated_by: claude-opus-4
curated_at: "2026-05-08"
rationale: Large-scale batch import of 386 skeletal terms via ROBOT template component, requiring ODK pipeline integration and prefix management
---

## Context

The Human Reference Atlas (HRA) / HuBMAP project needed 386 new skeletal anatomical terms integrated into Uberon. These terms cover bone zones, projections, fossae, foramina, and other features of the human skeleton. IDs were assigned in the automation range UBERON:1200004 through UBERON:1200389, each with definitions, part_of axioms, cross-references, and present_in_taxon restrictions to NCBITaxon:9606.

## Changes Made

Rather than editing uberon-edit.obo directly, the PR introduced a ROBOT template-based component (hra_skeleton.owl) built from src/templates/hra-skeleton.template.tsv. The ODK configuration (uberon-odk.yaml) was updated to register the new component, and a custom Makefile rule was added in uberon.Makefile to supply dcterms/dc prefix declarations during the build. Four problematic terms were dropped after quality review, as documented in a corrections report.

## Resolution

This is a complex case requiring understanding of the ODK component pipeline, ROBOT template syntax, prefix management in OWL builds, and batch term quality review. The PR touches 11 files across templates, build configuration, and documentation. An agent would need to generate the ROBOT template TSV, wire it into the build system, and handle edge cases around prefix declarations. Approved after review with no changes requested.
