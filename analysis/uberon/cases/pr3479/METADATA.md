---
repo: obophenotype/uberon
issue_number: 3478
pr_number: 3479
issue_title: "'late embryo' connected to effectively vertebrate-specific stages"
issue_created_at: "2025-02-12"
pr_author: gouttegd
pr_merged_at: "2025-02-13"
pr_num_commits: 1
files_changed:
  - path: src/ontology/uberon-edit.obo
    additions: 5
    deletions: 5
scoping: tightly_scoped
task_type: axiom_repair
difficulty: hard
scope: multi_term
review_outcome: approved_first_time
domain_area: developmental-anatomy
tags:
  - taxon-restriction
  - GCI
  - developmental-stage
  - chordate
  - pharyngula
curated_by: claude-opus-4
curated_at: "2026-05-08"
rationale: Taxon restriction correction using GCI axiom pattern to decouple a general stage from chordate-specific stages
case_quality: ok
case_quality_reason: gold_pr_genuine_but_metadiff_under_represents_top_attempts
companion_prs: []
scoring_caveat: "Gold PR #3479 is the single, complete, approved-first-time human resolution (no companion PRs, not curator-repudiated). However metadiff F1 systematically under-represents the strongest attempts: (a) the gold added definition-text rewrites of neurula/pharyngula ('A chordate developmental stage ...') that the *issue body* never explicitly requested (issue proposal items 1-2 only ask for the Chordata in_taxon restriction and the GCI), so every well-scoped agent loses ~0.5 recall on those two def lines despite fully resolving the issue's explicit asks; (b) the gold encodes the GCI as gci_relation=\"BFO:0000066\" (the IRI form of 'occurs in'), while semantically-correct label/alternative forms (occurs_in, part_of) are surface-penalized. Judge attempts against the issue's two explicit proposals plus the gold's optional def polish."
quality_flagged_by: claude-opus-4.7
quality_flagged_at: "2026-05-16"
---

## Context

Issue #3478 reported that UBERON:0007220 (late embryonic stage) was connected via a preceded_by axiom to UBERON:0004707 (pharyngula stage), a chordate-specific developmental stage. This made the late embryonic stage effectively vertebrate-specific, which is incorrect since many non-chordate organisms have a late embryonic stage. Additionally, the pharyngula and neurula stages had overly broad taxon restrictions (Eumetazoa) that needed tightening to Chordata.

## Changes Made

The PR made three changes in uberon-edit.obo: (1) narrowed the taxon restriction on pharyngula (UBERON:0004707) and neurula (UBERON:0000110) from Eumetazoa to Chordata; (2) replaced the direct SubClassOf preceded_by pharyngula axiom on late embryonic stage with a GCI (General Class Inclusion) axiom that applies only when the stage occurs in Chordata. This decouples the general late embryonic stage concept from chordate-specific developmental sequences.

## Resolution

Hard difficulty. An agent would need to understand GCI axiom patterns in OBO format, reason about taxon-appropriate developmental stage sequences, and recognize that a general stage concept should not be tied to taxon-specific precursors. The GCI pattern (class AND occurs_in some Taxon SubClassOf preceded_by some Stage) is an advanced OWL modeling technique. Same-day merge reflects the clear rationale provided in the issue.

## Curation Note (data quality)

Flagged by claude-opus-4.7 on 2026-05-16 after reviewing all 7 attempts.

This is a *genuine, sound* evaluation case — gold PR #3479 is the single, complete
human resolution: approved first time (cmungall APPROVED), merged same day, one
commit, one file, 5+/5-, no companion PRs, and not curator-repudiated. It is NOT
a poor case (not partial, not contaminated, not renegotiated). `case_quality: ok`.

However, two metadiff under-representation effects matter for downstream scoring and
should be applied when interpreting the F1 column:

1. **Issue-vs-PR scope gap (recall cap ~0.5 on top attempts).** Issue #3478's
   explicit proposal has exactly two items: (1) mark neurula stage (UBERON:0000110)
   and pharyngula stage (UBERON:0004707) as `in taxon` some Chordata
   (NCBITaxon:7711); (2) convert the `late embryonic stage` (UBERON:0007220)
   `preceded_by` pharyngula axiom to a GCI scoped to Chordata. The gold PR
   additionally rewrote the *textual definitions* of both neurula and pharyngula to
   begin "A chordate developmental stage ..." — an improvement the PR author added
   ("amend their definition accordingly") that the issue body never requested. All
   seven agents performed both explicit issue asks correctly but none made the
   unrequested def rewrites, so every well-scoped attempt is capped near F1=0.50 by
   two def lines that were not part of the stated task.

2. **GCI-relation surface penalty.** The gold encodes the GCI as
   `gci_relation="BFO:0000066"` (the IRI form of `occurs in`, exactly the issue's
   proposal). Attempts using the equivalent label form `occurs_in` (pr336/pr279) or
   the defensible same-stanza-consistent `part_of` (pr321/pr234, mirroring the
   pre-existing `RnorDv:0000010 {gci_relation="part_of"}` GCI on the very same term)
   are surface-penalized though semantically correct for the
   taxon-constraint-propagation goal the issue targets. (`in_taxon` as the GCI
   differentia in pr20/pr57/pr38 is a genuinely weaker/different model and a fair
   penalty.)

3. **pr234 robot-reserialization over-edit (not contamination).** The lowest-F1
   attempt (pr234, opus-4.7, F1 0.273) is the best-reasoned but was dragged down by
   ~10 unrelated CL label-refresh lines (CL:1000271, CL:0002145, CL:0002332,
   CL:1000223, CL:0000150) that `robot convert` re-synced from a newer merged CL
   import. Verified this hunk appears ONLY in pr234, not in the other six attempts —
   so it is an ODK/robot whole-file reserialization artifact specific to that run,
   NOT eval-base contamination and NOT a gold-leakage effect.

Recommendation: when aggregating, treat the top tier (pr336, pr279; then pr321) as
substantively successful on the issue's explicit asks despite F1≈0.50, and read the
F1 column as under-representing quality for the claude-runtime attempts.
