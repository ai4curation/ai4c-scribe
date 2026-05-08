---
repo: monarch-initiative/mondo
issue_number: 5726
pr_number: 10155
issue_title: "Add non-human animal diseases from VeNom"
issue_created_at: "2022-12-12"
pr_author: katiermullen
pr_merged_at: "2026-04-16"
pr_num_commits: 3
files_changed:
  - path: src/ontology/mondo-edit.obo
    additions: 9006
    deletions: 0
scoping: loosely_scoped
scoping_notes: Bulk addition of hundreds of non-human animal disease terms from the VeNom coding system.
task_type: new_term
difficulty: hard
scope: structural_refactor
review_outcome: approved_first_time
domain_area: veterinary-disease
tags:
  - VeNom
  - non-human-animal
  - bulk-addition
  - veterinary
curated_by: claude-opus-4
curated_at: "2026-05-08"
rationale: Large-scale batch import of veterinary disease terms requiring cross-reference alignment and classification decisions across multiple animal groups
---

## Context

Issue #5726 was a long-running initiative (opened December 2022) to incorporate non-human animal diseases from the VeNom (Veterinary Nomenclature) coding system into Mondo. VeNom contains over 6,000 diagnosis entries spanning large animals, small animals, farm animals, equines, and exotics. This PR represents one tranche of that effort, adding curated veterinary disease terms with appropriate VeNom cross-references and classifications.

## Changes Made

The PR added 9,006 lines to `src/ontology/mondo-edit.obo` across 3 commits, with zero deletions. Each new term stanza includes a label, definition, VeNom cross-reference, and classification under the non-human animal disease hierarchy. The scale of this change required careful curation to map VeNom diagnoses to appropriate Mondo parent classes and to exclude entries that are phenotypes rather than diseases.

## Resolution

Complex difficulty due to the sheer volume of terms and the need for systematic curation decisions. Each VeNom entry required evaluation of whether it represents a true disease (vs. a phenotype or procedure), selection of an appropriate parent class, and construction of valid cross-references. This task is not well-suited to a single agent pass and instead required iterative human curation across multiple PRs addressing the same long-running issue.
