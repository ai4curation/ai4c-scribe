---
repo: obophenotype/uberon
issue_number: 3409
pr_number: 3466
issue_title: "What relation should link a life stage term to its taxon-specific counterpart?"
issue_created_at: "2024-11-06"
pr_author: gouttegd
pr_merged_at: "2025-01-30"
pr_num_commits: 4
files_changed:
  - path: docs/bridges.md
    additions: 3
    deletions: 3
  - path: docs/combined_multispecies.md
    additions: 2
    deletions: 2
  - path: src/ontology/config/taxa.yaml
    additions: 1
    deletions: 2
  - path: src/ontology/imports/ro_terms.txt
    additions: 1
    deletions: 0
  - path: src/scripts/taxa.py
    additions: 8
    deletions: 2
scoping: mostly_scoped
task_type: other
difficulty: hard
scope: structural_refactor
review_outcome: approved_first_time
domain_area: cross-species-bridging
tags:
  - bridge-ontology
  - in-taxon
  - equivalence-axiom
  - composite-metazoan
  - cross-species
curated_by: claude-opus-4
curated_at: "2026-05-08"
rationale: Infrastructure-level refactoring of cross-species bridge axiom patterns, changing from single to dual axiom form
---

## Context

Issues #3409 and #3378 discussed the correct axiom pattern for linking taxon-specific anatomy terms (e.g., FBbt terms for Drosophila) to their Uberon counterparts in cross-species bridge ontologies. The existing single-axiom pattern using part_of/occurs_in had been intended as temporary. The original design called for a two-axiom form using in_taxon for the equivalence and a separate SubClassOf for the part_of/occurs_in relationship.

## Changes Made

The PR updated the bridging pipeline in src/scripts/taxa.py and src/ontology/config/taxa.yaml to generate two-axiom bridge patterns instead of single-axiom ones. For continuants, this means generating both an EquivalentTo axiom using in_taxon and a SubClassOf using part_of. For occurrents, the SubClassOf uses occurs_in instead. The Composite Metazoan pipeline was updated to unfold over in_taxon. Documentation in docs/bridges.md and docs/combined_multispecies.md was updated accordingly. The RO import was extended with the in_taxon relation.

## Resolution

Hard difficulty. An agent would need to understand the cross-species bridge ontology architecture, the difference between in_taxon and part_of/occurs_in semantics in OWL, and the Composite Metazoan build pipeline. The changes span five files including Python build scripts, YAML configuration, and documentation. This is infrastructure-level work that affects how all taxon-specific ontologies interoperate with Uberon.
