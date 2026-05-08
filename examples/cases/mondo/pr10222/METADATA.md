---
repo: monarch-initiative/mondo
issue_number: 9963
pr_number: 10222
issue_title: "RNU12 - related minor spliceopathy disorder"
issue_labels:
  - New term request
  - user request
issue_created_at: "2026-02-20"
pr_author: MeeSiing
pr_merged_at: "2026-05-04"
pr_num_commits: 1
files_changed:
  - path: src/ontology/mondo-edit.obo
    additions: 15
    deletions: 0
scoping: tightly_scoped
scoping_notes: PR adds exactly one new disease term stanza with no unrelated modifications.
task_type: new_term
difficulty: medium
scope: single_term
review_outcome: approved_first_time
domain_area: rare-disease
tags:
  - spliceopathy
  - gene-disease
  - RNU12
  - ClinGen
curated_by: claude-opus-4
curated_at: "2026-05-08"
rationale: New gene-disease term requiring correct logical axioms linking RNU12 to a spliceopathy phenotype
---

## Context

A new term request was filed for an RNU12-related minor spliceopathy disorder. RNU12 encodes a small nuclear RNA component of the minor spliceosome (U12-type), and mutations disrupt splicing of U12-type introns. The resulting phenotype is a developmental disorder with features overlapping other spliceopathies.

The request was supported by ClinGen curation and required creating a new Mondo term with appropriate gene-disease logical axioms and classification under the spliceopathy hierarchy.

## Changes Made

Added a single new term stanza to `src/ontology/mondo-edit.obo` with 15 lines of additions. The term includes a definition, logical axioms linking to RNU12 via germline mutation, and appropriate classification. This is a straightforward new term addition following established Mondo patterns for gene-disease terms.

## Resolution

Medium difficulty because it requires understanding the spliceopathy disease hierarchy and constructing the correct equivalence axiom linking the disease to RNU12. An agent would need to determine the appropriate parent class and apply the standard gene-disease term pattern with proper provenance attribution.
