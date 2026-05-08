---
repo: obophenotype/cell-ontology
issue_number: 3536
pr_number: 3537
issue_title: "Fix design patterns for columnar cuboidal and squamous epithelial cells"
issue_created_at: "2025-12-16"
pr_author: app/copilot-swe-agent
pr_merged_at: "2026-02-12"
pr_num_commits: 10
files_changed:
  - path: docs/patterns/cuboidalEpithelialCell.md
    additions: 29
    deletions: 0
  - path: docs/patterns/squamousEpithelialCell.md
    additions: 30
    deletions: 0
  - path: docs/relations_guide.md
    additions: 13
    deletions: 0
  - path: src/ontology/cl-edit.owl
    additions: 31
    deletions: 8
  - path: src/patterns/dosdp-patterns/cuboidalEpithelialCell.yaml
    additions: 35
    deletions: 0
scoping: loosely_scoped
task_type: axiom_repair
difficulty: hard
scope: multi_term
review_outcome: approved_first_time
domain_area: epithelial
tags:
  - design-pattern
  - DOSDP
  - epithelial
  - squamous
  - cuboidal
  - logical-definition
curated_by: claude-opus-4
curated_at: "2026-05-08"
rationale: Complex design pattern fix affecting multiple epithelial cell terms with new DOSDP patterns and documentation
---

## Context

The logical definitions for squamous and cuboidal epithelial cell types had inconsistent or missing design patterns. Issue #3536 identified that these cell types lacked formal Dead Simple OWL Design Patterns (DOSDP) and that existing axioms did not follow a consistent compositional structure. This affected the ability to systematically generate and validate epithelial cell subtypes using standard tooling.

## Changes Made

Added new DOSDP pattern YAML files for both cuboidal and squamous epithelial cells under `src/patterns/dosdp-patterns/`, created corresponding documentation under `docs/patterns/`, updated the relations guide, and revised 31 lines in `cl-edit.owl` to align existing epithelial cell term axioms with the new patterns. The edit file changes refactored logical definitions for multiple epithelial cell types to use consistent has_quality/part_of compositional patterns.

## Resolution

Approved on first review in 10 commits. Hard difficulty because this required designing DOSDP patterns from scratch, understanding PATO quality terms for cell morphology (squamous, cuboidal), ensuring the patterns correctly compose with anatomical location, and updating multiple existing terms to conform to the new patterns while maintaining backward compatibility.
