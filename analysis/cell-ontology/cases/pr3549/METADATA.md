---
repo: obophenotype/cell-ontology
issue_number: 3346
pr_number: 3549
issue_title: "Revise intraepithelial lymphocyte and subclasses"
issue_created_at: "2025-09-25"
issue_closed_at: "2026-02-18"
pr_author: copilot-swe-agent
pr_merged_at: "2026-02-18"
pr_num_commits: 6
files_changed:
  - path: src/ontology/cl-edit.owl
    additions: 15
    deletions: 2
scoping: tightly_scoped
task_type: axiom_repair
difficulty: hard
scope: multi_term
review_outcome: approved_first_time
domain_area: immunology
tags:
  - lymphocyte
  - intraepithelial
  - definition-broadening
  - intestinal
  - mucosal-immunity
curated_by: claude-opus-4
curated_at: "2026-05-08"
rationale: Complex definition revision broadening a cell type from tissue-specific to pan-epithelial, requiring immunology domain expertise
case_quality: poor
case_quality_reason: scoring_artifact_placeholder_id_and_xref_placement_plus_gold_term_tracker_misattribution
companion_prs: []
scoring_caveat: "Single gold PR #3549 fully resolves issue #3346; no companion PRs. Metadiff F1 is depressed for both attempts by (a) the non-deterministic new-term placeholder ID (gold minted CL_9900000; sonnet matched it by convention, haiku used CL_9900001), (b) xref-placement convention (top-level hasDbXref line vs. WIKIPEDIA embedded in the definition's xref annotation), and (c) unscoreable provenance (date stamp, term-tracker URL). The gold PR itself misattributes its IAO_0000233 term-tracker to issue #3455 instead of #3346, so faithfully reproducing gold is not the quality target for that field. Judge attempts against the issue's explicit asks, not the line-level metadiff."
quality_flagged_by: claude-opus-4.7
quality_flagged_at: "2026-05-16"
---

## Context

The intraepithelial lymphocyte (IEL) term (CL:0002496) was incorrectly restricted to intestinal epithelium only. In reality, IELs are found throughout mucosal epithelia including gastrointestinal, respiratory, and reproductive tracts. The definition needed broadening to reflect the true biological scope, and a new intestinal-specific subclass was needed for backward compatibility.

## Changes Made

Modified `cl-edit.owl` with 15 additions and 2 deletions. The changes broaden the IEL definition to encompass all epithelial tissues, remove the intestinal-specific restriction from the parent term, and add a new "intestinal intraepithelial lymphocyte" subclass to preserve the original narrower concept.

## Resolution

Approved on first review. Hard difficulty because this requires: (1) understanding mucosal immunology well enough to know IELs exist outside the gut, (2) correctly broadening a definition without breaking existing annotations, (3) creating a subclass to preserve backward compatibility, and (4) ensuring the logical axioms correctly reflect the broader anatomical scope.

## Curation Note (data quality)

Flagged `case_quality: poor` (quality_flagged_by: claude-opus-4.7, 2026-05-16).
This is a single-PR resolution (gold #3549 fully covers issue #3346; no companion
PRs), so there is no multi-PR fragmentation. The poor flag is for **metadiff
scoring artifacts** that make F1 a misleading quality proxy here:

- **Placeholder-vs-canonical CL ID artifact**: the issue requires minting a new
  `intestinal intraepithelial lymphocyte` term. Gold minted `CL_9900000`. The agent
  cannot predict which placeholder/canonical ID the curators will assign:
  sonnet-4.5 (eval PR #207) used `CL_9900000` and matched by convention; haiku-4.5
  (eval PR #144) used `CL_9900001` and is penalized across the entire subclass block
  for an ID it had no way to know.
- **OWL serialization / xref-placement convention**: both attempts add the
  issue-requested `WIKIPEDIA:Intraepithelial_lymphocyte` (sonnet) as a top-level
  `AnnotationAssertion(oboInOwl:hasDbXref ...)` line, whereas gold embeds it as an
  axiom-annotation inside the IAO_0000115 definition. Same content, different line
  shape — line-oriented metadiff penalizes it.
- **Gold term-tracker misattribution**: gold's `AnnotationAssertion(obo:IAO_0000233
  obo:CL_9900000 "https://github.com/.../issues/3455")` points to issue **#3455**,
  not the actual issue **#3346**. Reproducing gold faithfully on this field is not
  the quality target; sonnet's use of #3346 is arguably more correct.

Net: eval PR #207 (sonnet-4.5) is a substantively correct/complete resolution
scored `success` (F1=0.615 under-represents). Eval PR #144 (haiku-4.5) is
`partial_success` — core axiom repair correct, but it omitted the explicitly
requested WIKIPEDIA xref on both terms, omitted the ORCID contributor on the
broadened parent, and introduced an `is_inferred="true"` modeling error on the new
asserted subclass edge (real defects, not artifacts). Downstream aggregation should
down-weight the line-level F1 for this case and use the substance assessment in the
per-attempt reviews.
