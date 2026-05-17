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
case_quality: poor
case_quality_reason: gold_internally_inconsistent_and_out_of_scope
companion_prs: []
scoring_caveat: "metadiff vs #3537 is unreliable: (1) the gold PR is internally inconsistent — its OWL axioms use PATO:0001872 (cuboid, exact syn. 'cuboidal') for the cuboidal characteristic, but its docs/patterns/cuboidalEpithelialCell.md, relations_guide.md, and cuboidalEpithelialCell.yaml DOSDP all cite PATO:0002312, which is actually 'segmented', not 'cuboidal' (a gold error); (2) the gold makes out-of-scope structural edits the issue never asked for (reparenting CL_0000237 from CL_0000240 to CL_0000066, adding EquivalentClasses to CL_0000079 and CL_0000240 with part_of UBERON_0000486, merging CL_0002063 axioms). Judge attempts against the issue's four explicit asks, not the line-level diff."
quality_flagged_by: claude-opus-4.7
quality_flagged_at: "2026-05-16"
---

## Context

The logical definitions for squamous and cuboidal epithelial cell types had inconsistent or missing design patterns. Issue #3536 identified that these cell types lacked formal Dead Simple OWL Design Patterns (DOSDP) and that existing axioms did not follow a consistent compositional structure. This affected the ability to systematically generate and validate epithelial cell subtypes using standard tooling.

## Changes Made

Added new DOSDP pattern YAML files for both cuboidal and squamous epithelial cells under `src/patterns/dosdp-patterns/`, created corresponding documentation under `docs/patterns/`, updated the relations guide, and revised 31 lines in `cl-edit.owl` to align existing epithelial cell term axioms with the new patterns. The edit file changes refactored logical definitions for multiple epithelial cell types to use consistent has_quality/part_of compositional patterns.

## Resolution

Approved on first review in 10 commits. Hard difficulty because this required designing DOSDP patterns from scratch, understanding PATO quality terms for cell morphology (squamous, cuboidal), ensuring the patterns correctly compose with anatomical location, and updating multiple existing terms to conform to the new patterns while maintaining backward compatibility.

## Curation Note (data quality)

flagged_by: claude-opus-4.7 — flagged_at: 2026-05-16

This case is **`case_quality: poor`**. The gold PR #3537 should not be used as a
line-level metadiff reference; judge attempts against the issue's four explicit asks.

1. **Gold PR is internally inconsistent (gold error).** The issue asks for
   `cuboidal epithelial cell ≡ epithelial cell and has_characteristic some cuboidal`.
   PATO has no class literally labelled "cuboidal"; the correct term is
   **`PATO:0001872`** ("cuboid", with exact synonyms "cuboidal" and "block-like").
   The gold's OWL axioms correctly use `PATO:0001872` (for `CL_9900001`, `CL_0000634`,
   `CL_0002223`, `CL_0002662`, `CL_4033084`). However, the gold's **documentation and
   pattern files use `PATO:0002312`**, which is actually labelled **"segmented"**
   ("Consisting of segments… arranged in a longitudinal series") — a clear error in
   `docs/patterns/cuboidalEpithelialCell.md`, `docs/relations_guide.md`, and
   `src/patterns/dosdp-patterns/cuboidalEpithelialCell.yaml`. Agents that used
   `PATO:0001872` consistently everywhere (pr188 opus, pr151 haiku) are *more*
   internally consistent than the gold but are penalized by metadiff.

2. **Gold contains out-of-scope structural edits.** Beyond the issue's asks, the gold
   reparents `CL_0000237` (keratinizing barrier epithelial cell) from `CL_0000240` to
   `CL_0000066` and adds `part_of UBERON_0000486`; adds `EquivalentClasses` to
   `CL_0000079` (stratified epithelial cell) and rewrites the `CL_0000240` equivalence
   with `part_of UBERON_0000486`; and merges/reorders `CL_0002063` axioms. None of
   this is requested by issue #3536. Well-scoped agents that omit these are penalized
   on recall.

3. **Effect on scoring.** All three attempts scored F1 0.26–0.32. For pr188 (opus) and
   pr151 (haiku) the metadiff **substantially under-represents quality** — both met all
   four explicit asks with correct, reasoner-safe axioms. pr222 (sonnet) is a genuine
   partial: it correctly did the squamous half but abandoned the entire cuboidal half
   on the false premise that PATO has no cuboidal term, so its low score is only
   *partly* a case-quality artifact.
