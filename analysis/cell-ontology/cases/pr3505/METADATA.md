---
repo: obophenotype/cell-ontology
issue_number: 3458
pr_number: 3505
issue_title: "NTR Fibrochondrocyte progenitor cell (FCP)"
issue_created_at: "2025-11-20"
pr_author: app/copilot-swe-agent
pr_merged_at: "2025-12-11"
pr_num_commits: 8
files_changed:
  - path: src/ontology/cl-edit.owl
    additions: 14
    deletions: 0
scoping: tightly_scoped
task_type: new_term
difficulty: medium
scope: single_term
review_outcome: approved_first_time
domain_area: skeletal
tags:
  - NTR
  - fibrochondrocyte
  - progenitor
  - cartilage
  - stem-cell
curated_by: claude-opus-4
curated_at: "2026-05-08"
rationale: New progenitor cell type requiring understanding of chondrocyte differentiation lineages in fibrocartilage
case_quality: ok
case_quality_reason: metadiff_underrepresents_due_to_placeholder_id_artifact
companion_prs: []
scoring_caveat: "Single-PR gold (#3505) is the complete human resolution; not multi-PR or contaminated. However F1 substantially under-represents quality: (1) placeholder-vs-canonical CL ID artifact — gold used CL_9900000; attempts that picked CL_9900001 (pr100, pr29) or CL_0020021 (pr66, pr48) score F1=0.000 by whole-line metadiff even when substantively close (pr100/haiku is the closest model to gold yet scores 0). (2) Gold deliberately omitted all marker `expresses` axioms (RO_0002292) that the issue explicitly requested, after reviewer dosumis steered toward conservative non-in-vitro modeling; attempts that added the requested markers (all except pr100) lose recall against the conservative gold despite arguably more complete work. Judge substance, not the metadiff score."
quality_flagged_by: claude-opus-4.7
quality_flagged_at: "2026-05-16"
---

## Context

A new term request was filed for the fibrochondrocyte progenitor cell (FCP), a precursor cell that gives rise to fibrochondrocytes in fibrocartilaginous tissues such as the meniscus and temporomandibular joint disc. This term is part of a broader effort to populate the chondrocyte and cartilage cell branches of CL, complementing related terms like fibrochondrocyte (CL_4072104) added in PR #3467.

## Changes Made

Added 14 new lines to `cl-edit.owl` defining the FCP term with appropriate class declaration, label, textual definition referencing the progenitor-to-fibrochondrocyte differentiation pathway, parentage linking it to both progenitor cell and the chondrocyte lineage, and logical axioms capturing its developmental potential.

## Resolution

Approved on first review after 8 commits of iterative refinement. Medium difficulty because correctly modeling a progenitor cell requires establishing the develops_into relationship to the mature fibrochondrocyte and positioning the term appropriately within both the progenitor cell hierarchy and the cartilage cell lineage.

## Curation Note (data quality)

`quality_flagged_by: claude-opus-4.7` · `quality_flagged_at: 2026-05-16`

This is **not** a poor evaluation case: gold PR #3505 is the single, complete,
merged human resolution of issue #3458 (confirmed via `gh search prs --repo
obophenotype/cell-ontology 3458` → only #3505; PR metadata shows files_changed =
src/ontology/cl-edit.owl only). No base-state contamination, no gold leakage, no
curator repudiation, no multi-PR partial gold, no metadiff-blind gold field.
Marked `case_quality: ok`.

Two durable scoring caveats nonetheless make the F1 numbers misleading and
should down-weight metadiff-based aggregation for this case:

1. **Placeholder-vs-canonical CL ID artifact.** Gold (Copilot-authored, merged)
   allocated `CL_9900000`. The agent config mandates the CL_99xxxxx range but
   agents cannot know which exact free offset the human picked. Attempts pr100
   (`CL_9900001`) and pr29 (`CL_9900001`) used in-range but offset IDs; pr66/pr48
   (`CL_0020021`) used a different range entirely. All four score F1=precision=
   recall=0.000 by whole-line metadiff purely because the subject IRI differs on
   every line. pr100 (claude-haiku-4.5) is in fact the **closest model to gold**
   of all six attempts (correct conservative parentage, no marker axioms) yet
   scores 0.000 — a stark metadiff under-representation. Only pr230 and pr280
   (both `CL_9900000`) get non-zero F1.

2. **Gold omitted issue-requested marker axioms.** The issue explicitly asked
   for `expresses some` COL1A1, COL3A1, MCAM/CD146, MYLK. Reviewer @dosumis
   raised that the in-vitro colony-forming/multi-lineage text was "too in vitro
   (non-canonical) for a CL def"; gold responded conservatively — split that
   text to an `rdfs:comment` and added **no** `RO_0002292` marker axioms at all.
   Gold also added a reciprocal `SubClassOf(CL_4072104 RO_0002202 some
   CL_9900000)` (fibrochondrocyte develops_from FCP) which no agent reproduced
   (the issue author said they would add it themselves later). Agents that
   formalized the requested markers (all except pr100) therefore lose recall
   against the conservative gold despite doing arguably more complete,
   issue-faithful work.

Net: judge attempts on substance (cell model correctness, parentage, location,
synonym/definition fidelity, modeling pattern) against the issue, not on the
metadiff F1. Reviews in `analysis/cell-ontology/results/reviews/pr{230,280,100,
66,48,29}-claude-complete.md` grade accordingly.
