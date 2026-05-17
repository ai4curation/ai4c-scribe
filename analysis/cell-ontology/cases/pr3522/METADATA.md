---
repo: obophenotype/cell-ontology
issue_number: 3408
pr_number: 3522
issue_title: "Update type I-IV otic fibrocytes"
issue_created_at: "2025-10-27"
pr_author: app/copilot-swe-agent
pr_merged_at: "2026-02-04"
pr_num_commits: 6
files_changed:
  - path: src/ontology/cl-edit.owl
    additions: 63
    deletions: 26
scoping: mostly_scoped
task_type: other
difficulty: hard
scope: multi_term
review_outcome: approved_first_time
domain_area: auditory
tags:
  - definition-update
  - otic-fibrocyte
  - spiral-ligament
  - rename
  - cochlea
curated_by: claude-opus-4
curated_at: "2026-05-08"
rationale: Large-scale update renaming and redefining 5 otic fibrocyte types with enhanced definitions and corrected anatomy references
case_quality: poor
case_quality_reason: gold_dominated_by_odk_serialization_artifact_and_unrequested_style
companion_prs: [3409, 3410]
scoring_caveat: "Gold #3522 shares the exact eval base commit (0c07461c), so the metadiff is base-aligned, but ~45% of the gold's 51 added lines are NOT issue-driven curation: a 14-line ODK/ROBOT-regenerated annotation-property-label-declaration block (hasBroadSynonym/hasDbXref/hasExactSynonym/hasNarrowSynonym/hasRelatedSynonym/hasSynonymType labels) + 2 UBERON Declaration housekeeping lines (serialization artifacts), 5 gold-only 'type N SLF' OMO_0003000 related synonyms, 4 gold-only Arabic 'type N spiral ligament fibrocyte' exact synonyms, and a CL_0020005 SubClassOf->EquivalentClasses reasoner-equivalence refactor. The issue #3408 never requested any of these. Judge attempts against the issue's explicit asks (relabel, broad synonym, def update, ADD PMIDs, part-of spiral ligament, type-I adjacent-to stria vascularis, type-III tension fibroblast synonym), not the padded metadiff. F1 (~0.48-0.63) under-represents quality for all attempts except where genuine defects exist (#211 wrong part-of target UBERON_0001863; #97 deleted existing def xrefs)."
quality_flagged_by: claude-opus-4.7
quality_flagged_at: 2026-05-16
---

## Context

The existing type I through V otic fibrocyte terms in CL had outdated labels and sparse definitions that did not reflect current understanding of their roles in cochlear ion homeostasis. Issue #3408 requested renaming these to "spiral ligament fibrocyte type I-V" to better reflect their anatomical localization, and expanding their definitions with information about ion transport functions, spatial distribution within the spiral ligament, and marker gene expression.

## Changes Made

Extensively updated `cl-edit.owl` with 63 additions and 26 deletions affecting all five otic fibrocyte types. Each term received a renamed label (e.g., "type I otic fibrocyte" became "spiral ligament fibrocyte type I"), an expanded textual definition with literature references, and updated logical axioms linking to UBERON spiral ligament subdivisions and GO ion transport processes. The changes ensure consistency across the entire fibrocyte type series.

## Resolution

Approved on first review in 6 commits. Hard difficulty because the update required coordinating changes across 5 related terms simultaneously, ensuring consistent naming conventions, accurate anatomical placement within cochlear substructures, and correct representation of each type's distinct ion transport roles in endolymph homeostasis.

## Curation Note (data quality)

Flagged `case_quality: poor` (claude-opus-4.7, 2026-05-16). The gold PR #3522 shares the **exact** eval base commit `0c07461c` (verified via `gh pr view 184` baseRefOid == gold PR baseRefOid), so the metadiff is base-aligned and not contaminated. However, the gold diff is **dominated by non-issue-driven content** that mechanically depresses recall/F1 for every attempt:

- **ODK/ROBOT serialization artifact (~14 of 51 added lines, ~27%)**: a block of six annotation-property `rdfs:label` declarations (`hasBroadSynonym`, `hasDbXref`, `hasExactSynonym`, `hasNarrowSynonym`, `hasRelatedSynonym`, `hasSynonymType`) plus blank lines, and 2 `Declaration(Class(obo:UBERON_0002282))`/`Declaration(Class(obo:UBERON_0006725))` housekeeping lines. The eval base already *uses* `hasBroadSynonym` 282× and `hasExactSynonym` 2436× and already uses UBERON_0006725, so these declarations were injected by a ROBOT round-trip / build pipeline, not by issue #3408 curation. No agent should (or did) reproduce them.
- **Gold-only stylistic synonyms not requested by the issue**: 5 "type N SLF" `hasRelatedSynonym` lines with `oboInOwl:hasSynonymType obo:OMO_0003000` + PMID:33193034, and 4 Arabic "type N spiral ligament fibrocyte" `hasExactSynonym` lines. Issue #3408 only asked for the old labels as **broad** synonyms.
- **Gold-only strategic refactor**: gold keeps `SubClassOf CL_0002665` and instead converts `CL_0020005` from two SubClassOf axioms to `EquivalentClasses(CL_0020005 ObjectIntersectionOf(CL_0002665 part-of UBERON_0006725))`, making type I–V inferred (not asserted) subclasses of spiral ligament fibrocyte. Every agent instead asserted `SubClassOf CL_0020005` directly — an equally valid, more conventional choice that is ontologically equivalent post-reasoning. The issue never specified either approach.

Net: ~45% of the 51 gold additions are artifacts or unrequested gold-only style/strategy. Attempts should be judged against the issue's explicit asks (relabel; old label as broad synonym; update definition text; **ADD** the per-type PMIDs to existing `GOC:tfm`/`PMID:18353863`; `part of some spiral ligament` UBERON_0006725; type-I `adjacent to some stria vascularis of cochlear duct` UBERON_0002282; type-III `tension fibroblast` exact synonym). Under that lens, attempts #184 (opus), #32 (codex gpt-5.5), #69/#51 (opencode gpt-5.5) are substantive successes despite F1≈0.56–0.63; the metadiff under-represents them. Genuine defects remain real: **#211** (sonnet-4.5) used the wrong `part of` target `UBERON_0001863` (scala vestibuli) instead of UBERON_0006725 on all five terms; **#97** (haiku-4.5) deleted the existing `GOC:tfm`/`PMID:18353863` definition xrefs in direct violation of the issue's bolded "DO NOT replace references" instruction and omitted the type-I adjacency axiom.

Companion PRs for the broader otic-fibrocyte refactor program (different issues, listed for context, not part of #3408's gold): #3409 (broaden CL_0002665 otic fibrocyte to `part of internal ear`, issue #3246) and #3410 (create `spiral ligament fibrocyte` term, issue #3407; later renumbered to CL_0020005 in the eval base). These were resolved before #3522 and are not required to satisfy issue #3408.
