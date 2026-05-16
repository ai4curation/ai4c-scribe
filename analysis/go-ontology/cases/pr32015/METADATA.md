---
repo: geneontology/go-ontology
issue_number: 31961
pr_number: 32015
issue_title: "obsolete GO:0008785 alkyl hydroperoxide reductase activity"
issue_labels:
  - enzymes
  - obsoletion
issue_created_at: "2026-04-24"
issue_closed_at: "2026-04-29"
pr_author: dragon-ai-agent
pr_merged_at: "2026-04-29"
pr_num_commits: 2
files_changed:
  - path: src/ontology/go-edit.obo
    additions: 5
    deletions: 2
scoping: tightly_scoped
scoping_notes: All changes directly address the obsoletion of the single term GO:0008785.
task_type: obsoletion
difficulty: simple
scope: single_term
review_outcome: approved_first_time
domain_area: molecular_function
tags:
  - enzyme
  - peroxidase
  - EC:1.11.1.26
curated_by: claude-opus-4
curated_at: "2026-05-03"
rationale: Clean single-term obsoletion with well-reasoned replaced_by, demonstrates standard obsoletion pattern
case_quality: ok
case_quality_reason: gold_complete_but_metadiff_low_resolution
companion_prs: []
scoring_caveat: "Single human PR #32015 fully and correctly resolved issue #31961 (gold is complete; NOT a partial-gold case). However the metadiff F1 is low-resolution on this case: (a) it systematically UNDER-credits the dominant correct agent pattern, which additionally rewires the GO:0009321 comment to GO:0102039 and deletes the spurious GO:0070937 GO:0008785 comment — both defensible ontology hygiene the human PR omitted, lowering recall to 0.727 with no quality loss; and (b) it FAILS TO DISCRIMINATE genuine regressions within the F1=0.800 tie — attempts #33 and #32 rewired the unrelated GO:0070937 mRNA-stability comment to point at GO:0102039 (laundering a nonsense cross-reference into an active term) yet score identically to fully-correct attempts. Judge attempts on substance: structurally-correct obsoletion + GO:0009321 rewire + GO:0070937 *deletion* is the best outcome; GO:0070937 *rewire* (#33,#32) and dropped historical tracker items (#225) and edits to generated comments.txt/ld.txt (#103,#84) are real defects the score masks. #362 is the only true failure (retained is_a on obsolete term, no obsolete name/def prefix, backwards consider:)."
quality_flagged_by: claude-opus-4.7
quality_flagged_at: "2026-05-15"
---

## Context

GO:0008785 "alkyl hydroperoxide reductase activity" was flagged for obsoletion because, despite its generic-sounding name, it represented a substrate-specific activity more specific than any known gene product. The enzyme name "alkyl hydroperoxide reductase" is actually listed as a synonym of EC:1.11.1.26 (NADH-dependent peroxiredoxin activity), which corresponds to GO:0102039.

## Changes Made

In `src/ontology/go-edit.obo`, the term GO:0008785 was modified:

- Name prefixed with "obsolete" -> "obsolete alkyl hydroperoxide reductase activity"
- Definition prefixed with "OBSOLETE."
- Added explanatory comment about why the term was obsoleted (substrate specificity mismatch with EC:1.11.1.26)
- Removed `is_a` relationship to GO:0016668 (oxidoreductase activity, acting on a sulfur group of donors, NAD(P) as acceptor)
- Added `is_obsolete: true`
- Added `replaced_by: GO:0102039` (NADH-dependent peroxiredoxin activity)
- Added term_tracker_item linking to issue #31961

## Resolution

Straightforward obsoletion following standard OBO pattern. The key reasoning was identifying that GO:0102039 is the correct replacement based on EC number alignment (EC:1.11.1.26). Approved without changes on first review.

## Curation Note (data quality)

Flagged by claude-opus-4.7 on 2026-05-15 during review of all 23 agent attempts.

**This is NOT a partial-gold case.** Step 3a checks confirm a single human PR
(#32015, by dragon-ai-agent, merged 2026-04-29) fully and correctly resolved
issue #31961; no companion PRs. The gold stanza is well-formed and standard.
`case_quality` is therefore `ok`, not `poor`.

**The caveat is metadiff resolution, not gold completeness.** This case is a
useful illustration of two metadiff limitations that downstream
scoring/aggregation should account for:

1. **Systematic under-crediting of the correct pattern.** 16 of 23 attempts
   converge on a diff that is structurally identical to the gold for the
   GO:0008785 stanza but additionally (a) rewires the GO:0009321 *alkyl
   hydroperoxide reductase complex* `comment` from GO:0008785 to the active
   replacement GO:0102039, and (b) deletes a pre-existing spurious comment on
   GO:0070937 *CRD-mediated mRNA stability complex* that erroneously
   referenced GO:0008785 (a long-standing copy/paste artifact; the two terms
   are biologically unrelated). Both are defensible ontology hygiene that
   discharge dangling references to the obsoleted term; the human PR simply
   did not do them. They cost recall (0.727) with no loss of correctness, so
   F1=0.800 *under*-represents quality for this cluster.

2. **Failure to discriminate real regressions within the F1=0.800 tie.**
   Attempts #33 (claude-haiku-4.5) and #32 (gpt-5.4/codex v8) did *not* delete
   the GO:0070937 comment — they rewired it to point at GO:0102039, launder-
   ing a biologically meaningless cross-reference into an active term. This is
   strictly worse than the artifact it "fixed," yet both score an identical
   F1=0.800 to the fully-correct attempts. The metadiff cannot see this.

**Other score-masked defects (judge on substance):**
- #225 (gemma-4-31b, F1=0.727): dropped the historical term_tracker_items
  #28261/#28340 — a provenance regression, not mere scope difference.
- #103/#84 (gpt-5.5/opencode, F1=0.696): edited the build-generated derived
  artifacts `src/ontology/comments.txt` and `src/ontology/ld.txt` directly —
  genuine scope creep into non-source files.
- #51/#50/#38 (F1=0.762): added a redundant near-duplicate EXACT synonym and a
  non-standard #31961 tracker item to the active replacement term GO:0102039 —
  benign churn; the recall penalty here is a fair one.
- #362 (gemini-2.5-flash, F1=0.308): the only true failure — retained `is_a`
  on the obsolete term, no "obsolete"/"OBSOLETE." prefixes, no #31961 tracker
  item, and a backwards `consider: GO:0008785` on the replacement. Would fail
  obsoletion QC. The low F1 here is accurate.

**Recommendation:** keep the case (it is a good standard-obsoletion exemplar)
but do not treat the F1=0.800 cluster as homogeneous in aggregation; the
narrative reviews distinguish the fully-correct majority from the
GO:0070937-rewire regressions (#33, #32).
