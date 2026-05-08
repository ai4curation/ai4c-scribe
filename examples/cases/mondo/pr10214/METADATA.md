---
repo: monarch-initiative/mondo
issue_number: 9956
pr_number: 10214
issue_title: "New Term Request/TSEN2-related neurodevelopmental disorder with or without thrombotic microangiopathy"
issue_labels:
  - New term request
  - user request
issue_created_at: "2026-02-18"
issue_closed_at: "2026-05-01"
pr_author: MeeSiing
pr_merged_at: "2026-05-01"
pr_num_commits: 2
files_changed:
  - path: src/ontology/mondo-edit.obo
    additions: 13
    deletions: 0
scoping: tightly_scoped
scoping_notes: PR adds exactly one new disease term stanza with no unrelated modifications.
task_type: new_term
difficulty: medium
scope: single_term
review_outcome: approved_first_time
domain_area: rare-disease
tags:
  - neurodevelopmental-disorder
  - gene-disease
  - TSEN2
  - HGNC:28422
  - ClinGen
  - thrombotic-microangiopathy
curated_by: claude-opus-4
curated_at: "2026-05-03"
rationale: Clean new disease term requiring gene-disease logical axioms, ClinGen provenance, and multi-parent classification
---

## Context

A new term request was filed for a TSEN2-related neurodevelopmental disorder with or without thrombotic microangiopathy. TSEN2 encodes a subunit of the tRNA splicing endonuclease complex. Mutations cause a complex phenotype including intellectual disability, growth delay, hypotonia, motor delay, ataxia, vision issues, cardiac features, pulmonary complications, and brain structural anomalies. Some patients also develop renal thrombotic microangiopathy.

The request was backed by ClinGen curation (https://clinicalgenome.org/affiliation/40069/) and supported by 8 PMIDs.

## Changes Made

Added new term MONDO:1060216 to `src/ontology/mondo-edit.obo`:

- **ID**: MONDO:1060216
- **Name**: TSEN2-related neurodevelopmental disorder with or without thrombotic microangiopathy
- **Definition**: Comprehensive clinical description citing 8 PMIDs (PMID:18711368, PMID:20952379, PMID:23562994, PMID:32404165, PMID:38347586, PMID:38438125, PMID:38622473) and ClinGen as source
- **Classification** (multi-parent):
  - is_a MONDO:0002254 (syndromic disease) — because multiple organ systems affected
  - is_a MONDO:0700092 (neurodevelopmental disorder) — primary presentation
- **Logical definition** (equivalence axiom):
  - intersection_of: MONDO:0700092 (neurodevelopmental disorder)
  - intersection_of: has_material_basis_in_germline_mutation_in HGNC:28422 (TSEN2)
- **Gene relationship**: has_material_basis_in_germline_mutation_in HGNC:28422 (TSEN2)
- **Provenance**: ClinGen affiliation as source on all axioms, creator ORCID, term_tracker_item

## Resolution

Medium difficulty because it requires:
1. **Multi-parent classification**: Determining that the disease is both a syndromic disease AND a neurodevelopmental disorder (not just one or the other)
2. **Logical axiom construction**: Building the equivalence axiom (intersection_of) correctly linking the disease class to its causal gene via the appropriate relation
3. **Source attribution**: Every axiom annotated with ClinGen provenance
4. **Definition writing**: Comprehensive clinical description synthesizing findings from 8 publications

An agent would need to understand Mondo's patterns for gene-disease terms: the specific use of `has_material_basis_in_germline_mutation_in`, the intersection_of pattern for logical definitions, and how to correctly attribute sources to individual axioms.
