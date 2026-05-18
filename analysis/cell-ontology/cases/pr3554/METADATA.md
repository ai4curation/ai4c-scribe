---
repo: obophenotype/cell-ontology
issue_number: 3452
pr_number: 3554
issue_title: "[NTR] Add new terms for stem cell memory T cells (TSCM): CD4+ and CD8+ subsets"
issue_created_at: "2025-11-20"
pr_author: app/copilot-swe-agent
pr_merged_at: "2026-02-18"
pr_num_commits: 6
files_changed:
  - path: src/ontology/cl-edit.owl
    additions: 40
    deletions: 0
scoping: tightly_scoped
task_type: new_term
difficulty: medium
scope: multi_term
review_outcome: approved_first_time
domain_area: immunology
tags:
  - NTR
  - T-cell
  - memory
  - stem-cell
  - CD4
  - CD8
  - TSCM
curated_by: claude-opus-4
curated_at: "2026-05-08"
rationale: New terms for CD4+ and CD8+ stem cell memory T cells requiring understanding of T cell differentiation hierarchy and memory compartments
case_quality: ok
case_quality_reason: sound_gold_but_metadiff_sensitive_to_new_term_provenance_and_wording
quality_flagged_by: codex
quality_flagged_at: "2026-05-17"
---

## Context

Stem cell memory T cells (TSCM) are a recently described subset of memory T cells that possess stem cell-like self-renewal capacity while maintaining the ability to differentiate into other memory and effector T cell subsets. Issue #3452 requested adding both CD4-positive and CD8-positive TSCM terms to enable annotation of these populations in single-cell datasets, particularly for CellxGene and HuBMAP.

## Changes Made

Added 40 new lines to `cl-edit.owl` defining two new terms: CD4-positive stem cell memory alpha-beta T cell and CD8-positive stem cell memory alpha-beta T cell. Each term includes a class declaration, label, synonyms, textual definition referencing the stem-like properties and surface marker profile, parentage under the appropriate CD4+ or CD8+ memory T cell parent, and logical axioms capturing surface marker expression (CD95+, CD122+) and the stem cell-like self-renewal capability.

## Resolution

Approved on first review in 6 commits. Medium difficulty because correctly modeling TSCM cells requires understanding their position in the T cell differentiation hierarchy -- they are the least differentiated memory subset, sitting between naive T cells and central memory T cells, and their definition involves multiple surface markers that distinguish them from other memory compartments.
