---
repo: obophenotype/cell-ontology
issue_number: 3457
pr_number: 3467
issue_title: "Add fibrochondrocyte (CL_4072104) term"
issue_created_at: "2025-11-20"
issue_closed_at: "2025-11-27"
pr_author: copilot-swe-agent
pr_merged_at: "2025-11-27"
pr_num_commits: 7
files_changed:
  - path: src/ontology/cl-edit.owl
    additions: 5
    deletions: 4
scoping: mostly_scoped
scoping_notes: >-
  Primary change is the new fibrochondrocyte term in cl-edit.owl, but component
  files were also regenerated as part of the build process.
task_type: new_term
difficulty: medium
scope: single_term
review_outcome: approved_first_time
domain_area: musculoskeletal
tags:
  - NTR
  - fibrochondrocyte
  - chondrocyte
  - fibrocartilage
  - hybrid-cell
curated_by: claude-opus-4
curated_at: "2026-05-08"
rationale: New term for a hybrid cell type requiring understanding of chondrocyte and fibroblast dual characteristics
case_quality: poor
case_quality_reason: scoring_artifact_placeholder_id_and_build_regenerated_files
companion_prs: []
scoring_caveat: >-
  metadiff F1 (best 0.093, five attempts 0.000) drastically under-represents
  agent quality. Two structural artifacts: (1) the gold PR #3467 uses the
  post-reserialization permanent ID CL_4072104 while CLAUDE.md instructs agents
  to mint temporary CL_99xxxxx IDs (idrange:81) — correctly-instructed agents
  therefore line-mismatch every axiom and score F1=0 even when substantively
  equivalent (placeholder-vs-canonical CL ID artifact); (2) the gold diff is
  dominated by ODK build-regenerated files (merged_import.owl, bgo-cl-comp.owl,
  cellxgene_subset.owl, clm-cl.owl, wmbo-cl-comp.owl, pr_terms.txt, version
  IRIs, COL3A1/COL6A1 PR declarations) that an edit-only agent cannot
  reproduce, structurally capping recall. Judge attempts on cl-edit.owl
  substance vs the issue, not on metadiff.
quality_flagged_by: claude-opus-4.7
quality_flagged_at: "2026-05-16"
---

## Context

A new term request was filed for fibrochondrocyte, a hybrid cell type found in fibrocartilaginous tissues (meniscus, intervertebral disc, TMJ disc) that exhibits characteristics of both chondrocytes and fibroblasts. This cell type produces both type I and type II collagen, distinguishing it from typical hyaline cartilage chondrocytes.

## Changes Made

Added the fibrochondrocyte term (CL:4072104) to `cl-edit.owl` with proper parentage under both chondrocyte and fibroblast lineages, a textual definition citing relevant literature, and synonyms. The term uses a permanent CL ID rather than a temporary one, indicating it was minted through the standard ID allocation process.

## Resolution

Approved on first review. Medium difficulty because properly modeling a hybrid cell type requires understanding dual-lineage classification, choosing appropriate parent classes, and writing a definition that captures the distinguishing features (collagen type production, anatomical location in fibrocartilage).

## Curation Note (data quality)

`case_quality: poor` — flagged 2026-05-16 by claude-opus-4.7 after reviewing all
7 attempts. **The metadiff scores are not usable as a quality signal for this
case** for two independent structural reasons:

1. **Placeholder-vs-canonical CL ID artifact.** The gold PR (#3467) uses the
   permanent ID `CL_4072104` assigned by the release reserialization pipeline.
   The agent config CLAUDE.md explicitly instructs agents to mint temporary IDs
   in the `CL_99xxxxx` range (idrange:81). Agents that *correctly followed this
   instruction* (sonnet #208, opus #180 → `CL_9900000`; haiku #99, codex #83/#36
   → `CL_9900001`) line-mismatch every axiom against gold and score **F1=0.000
   by construction**, despite producing substantively equivalent terms. The only
   non-zero attempts (#73, #54 = 0.093) are the two opencode runs that *violated*
   the instruction by scraping `CL_4072104` from OLS, so their declaration/header
   lines coincidentally line-matched gold. The metric thus rewards the
   instruction violation and zeros out the correct behavior.

2. **Build-regenerated-file domination.** Gold's 373-line diff is mostly
   ODK-regenerated artifacts: `merged_import.owl`, `bgo-cl-comp.owl`,
   `cellxgene_subset.owl`, `clm-cl.owl`, `wmbo-cl-comp.owl`, `pr_terms.txt`,
   release version IRIs, and downstream COL3A1 (`PR_000003328`) / COL6A1
   (`PR_000003353`) PR-class declarations. An edit-only agent that does not run
   the release pipeline cannot reproduce these, structurally capping recall.

Substantive assessment (judge against the issue, not metadiff): all 7 attempts
correctly added `fibrochondrocyte` under chondrocyte (`CL_0000138`) with
`part_of fibrocartilage` (`UBERON_0001995`), three correctly typed PMID-backed
synonyms, and contributor ORCID. Best: **opus #180** (clean genus-differentia
equivalence + separate COL1A1 marker SubClassOf, verbatim definition, correct
temp-ID handling and reasoning). Solid: sonnet #208, codex #36 (ran `robot
reason`), opencode #73/#54. Weaker: haiku #99 (used plain `SubClassOf` instead
of the `cellPartOfAnatomicalEntity` DOSDP equivalence axiom — wrong pattern);
codex #83 (gutted the definition to one sentence and dropped PMID:31871141).
Common gap across all: only COL1A1 `expresses` asserted, whereas gold also
asserts COL3A1 and COL6A1 (the issue's explicit "expresses some" line named only
collagen alpha-1(I) chain, so this is a defensible literal reading).

Note: the case directory is named `pr3466` but the gold PR for issue #3457 is
**#3467** (correct in frontmatter). Source PR #3466 is an unrelated change
("Generalize chondrocyte definition and add skeletogenic cell parent") and is
**not** a companion PR — `companion_prs: []`. Step 3a (multi-PR partial gold)
does not apply; this is a single-PR resolution.
