---
repo: geneontology/go-ontology
issue_number: 31636
pr_number: 31925
issue_title: "rename GO:1990334 Bfa1-Bub2 complex to make it species agnostic"
issue_created_at: "2026-02-25"
pr_author: dragon-ai-agent
pr_merged_at: "2026-04-20"
pr_num_commits: 1
files_changed:
  - path: src/ontology/go-edit.obo
    additions: 5
    deletions: 2
scoping: tightly_scoped
task_type: synonym_update
difficulty: simple
scope: single_term
review_outcome: approved_first_time
curated_by: claude-opus-4
curated_at: "2026-05-08"
rationale: Rename of a species-specific complex label to a species-agnostic name following GO naming conventions, with species-specific names retained as NARROW synonyms
case_quality: good
case_quality_reason: single_complete_gold_pr
quality_flagged_by: codex
quality_flagged_at: "2026-05-17"
---

## Context

GO:1990334 was named `Bfa1-Bub2 complex` using S. cerevisiae-specific gene names. GO naming conventions prefer species-agnostic labels for complexes that are conserved across species. This complex functions as a two-component GTPase-activating protein (GAP) in both the mitotic exit network (MEN) in budding yeast and the septation initiation network (SIN) in fission yeast, where it is known as the Byr4-Cdc16 complex.

## Changes Made

The primary label was changed from `Bfa1-Bub2 complex` to `SIN/MEN two-component GAP complex`. The old S. cerevisiae name was retained as a NARROW synonym (`Bfa1-Bub2 complex`), and the S. pombe equivalent was added as another NARROW synonym (`Byr4-Cdc16 GAP complex`). The definition was updated to reference both the mitotic exit network (MEN, budding yeast) and septation initiation network (SIN, fission yeast) to support the species-agnostic label.

## Resolution

Easy difficulty because the naming convention is well-established in GO (species-agnostic primary labels with species-specific NARROW synonyms) and the biological equivalence of Bfa1-Bub2 and Byr4-Cdc16 complexes is well-documented. The main decision was the choice of species-agnostic label, which used the functional description (SIN/MEN two-component GAP complex) rather than any single species' nomenclature.
