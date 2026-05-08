---
repo: obophenotype/uberon
issue_number: 3454
pr_number: 3455
issue_title: "Newly introduced crab and lobster terms violate taxon constraints"
issue_created_at: "2024-12-23"
pr_author: gouttegd
pr_merged_at: "2024-12-24"
pr_num_commits: 4
files_changed:
  - path: src/ontology/uberon-edit.obo
    additions: 39
    deletions: 54
  - path: src/ontology/imports/ncbitaxon_terms.txt
    additions: 1
    deletions: 0
  - path: src/ontology/imports/merged_import.owl
    additions: 42
    deletions: 3
scoping: tightly_scoped
task_type: axiom_repair
difficulty: hard
scope: multi_term
review_outcome: approved_first_time
domain_area: invertebrate-anatomy
tags:
  - taxon-constraint
  - crustacean
  - Pleocyemata
  - cross-reference-fix
curated_by: claude-opus-4
curated_at: "2026-05-08"
rationale: Taxon constraint violation fix requiring taxonomic knowledge to find the correct common ancestor taxon for crab and lobster terms
---

## Context

Issue #3454 reported that newly introduced nerve terms for crabs and lobsters (from PR #3445) were causing taxon constraint violations. The terms had separate in_taxon restrictions to Astacidea (lobsters) and Brachyura (crabs), but this pattern conflicted with Uberon's taxon constraint checking system. Additionally, several cross-references had formatting errors (spurious spaces after colons, e.g., "PMID: 17009928").

## Changes Made

The PR replaced the separate in_taxon restrictions to Astacidea (NCBITaxon:6712) and Brachyura (NCBITaxon:6752) with a single restriction to their common ancestor Pleocyemata (NCBITaxon:6692). The Pleocyemata term was explicitly imported into the NCBITaxon import (ncbitaxon_terms.txt and merged_import.owl). Cross-reference formatting errors were also corrected across multiple term stanzas, resulting in 39 additions and 54 deletions.

## Resolution

Hard difficulty. An agent would need to understand Uberon's taxon constraint system, look up the NCBI taxonomy to find the appropriate common ancestor for Astacidea and Brachyura (Pleocyemata), update the import configuration to include the new taxon term, and fix the cross-reference formatting issues. The multi-file changes and taxonomic reasoning make this significantly more complex than a simple axiom edit. Same-day merge reflects the urgency of fixing constraint violations.
