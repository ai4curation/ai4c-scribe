---
repo: obophenotype/cell-ontology
issue_number: 3453
pr_number: 3556
issue_title: "[NTR] CD4-positive exhausted alpha-beta T cell / CD8-positive exhausted alpha-beta T cell"
issue_created_at: "2025-11-20"
pr_author: app/copilot-swe-agent
pr_merged_at: "2026-02-16"
pr_num_commits: 5
files_changed:
  - path: src/ontology/cl-edit.owl
    additions: 34
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
  - exhaustion
  - CD4
  - CD8
  - immune-checkpoint
curated_by: claude-opus-4
curated_at: "2026-05-08"
rationale: New terms for exhausted T cell subsets requiring understanding of T cell exhaustion biology and inhibitory receptor expression patterns
case_quality: ok
case_quality_reason: sound_gold_but_complex_new_term_pair_scores_sensitive_to_definition_and_synonym_details
quality_flagged_by: codex
quality_flagged_at: "2026-05-17"
---

## Context

T cell exhaustion is a state of progressive dysfunction that occurs during chronic viral infection and in the tumor microenvironment. Issue #3453 requested new terms for CD4-positive and CD8-positive exhausted alpha-beta T cells, which are characterized by high expression of inhibitory receptors (PD-1, LAG-3, TIM-3) and diminished effector function. These terms are important for annotating tumor-infiltrating lymphocyte populations in cancer immunology datasets.

## Changes Made

Added 34 new lines to `cl-edit.owl` defining CD4-positive exhausted alpha-beta T cell and CD8-positive exhausted alpha-beta T cell. Each term includes class declaration, label, textual definition describing the exhaustion phenotype, parentage under the appropriate CD4+ or CD8+ alpha-beta T cell parent, and logical axioms capturing the expression of inhibitory checkpoint receptors and the relationship to the exhaustion biological process via GO terms.

## Resolution

Approved on first review in 5 commits. Medium difficulty because the exhaustion state is defined by a combination of phenotypic markers and functional properties, and the ontological representation must capture both the surface marker profile (PD-1, LAG-3, TIM-3) and the diminished functional capacity without conflating exhaustion with other hyporesponsive states like anergy.
