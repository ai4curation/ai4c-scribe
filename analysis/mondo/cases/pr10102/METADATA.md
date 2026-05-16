---
repo: monarch-initiative/mondo
issue_number: 9771
pr_number: 10102
issue_title: "[Obsolete] 'heart, malformation of' (MONDO:0009327)"
issue_labels:
  - obsolete
  - on list
issue_created_at: "2025-11-19"
pr_author: sabrinatoro
pr_merged_at: "2026-03-31"
pr_num_commits: 1
files_changed:
  - path: src/ontology/mondo-edit.obo
    additions: 9
    deletions: 10
scoping: tightly_scoped
scoping_notes: PR obsoletes a single term with appropriate replaced_by annotation.
task_type: obsoletion
difficulty: simple
scope: single_term
review_outcome: approved_first_time
domain_area: congenital-disease
tags:
  - obsoletion
  - heart-malformation
  - congenital
  - OMIM
curated_by: claude-opus-4
curated_at: "2026-05-08"
rationale: Straightforward obsoletion of a vague legacy term following standard Mondo obsoletion patterns
case_quality: poor
case_quality_reason: gold_incomplete_dangling_replaced_by
companion_prs: []
scoring_caveat: "Gold PR #10102 obsoletes MONDO:0009327 but leaves MONDO:0007703 with replaced_by: MONDO:0009327, a dangling pointer to a now-obsolete term (still broken in the live ontology as of 2026-05-15). The mondo-agent-config explicitly requires 'No relationship should point to an obsolete term'. 11 of 14 attempts correctly rewired MONDO:0007703 to consider: MONDO:0005267 — a real improvement over the gold — but metadiff scores that extra-but-correct edit against recall, depressing F1 for the strongest attempts. Best F1 is only 0.812 and the 0.56–0.81 spread is dominated by (a) this gold omission, (b) free-text comment-wording differences, and (c) minor xref source-qualifier variation, none of which metadiff can normalize. Judge attempts against the issue + the agent-config obsoletion SOP, not the line-level metadiff."
quality_flagged_by: claude-opus-4.7
quality_flagged_at: "2026-05-15"
---

## Context

MONDO:0009327 "heart, malformation of" was identified as an overly vague legacy term that did not add value to the ontology. The term originated from an OMIM entry but lacked the specificity needed for a useful disease classification. Such terms are periodically reviewed and obsoleted when they do not represent a distinct disease entity.

## Changes Made

Obsoleted MONDO:0009327 by marking it as obsolete, removing its classification axioms, and adding appropriate replaced_by and consider annotations to redirect users to more specific terms. The 9 additions and 10 deletions reflect the standard obsoletion pattern: removing active axioms and adding obsoletion metadata.

## Resolution

Easy difficulty because this follows the standard Mondo obsoletion pattern. The curator needs to mark the term as obsolete, remove is_a parents and logical definitions, and add replaced_by or consider pointers. An agent should be able to handle this with knowledge of the obsoletion SOP.

## Curation Note (data quality)

`case_quality: poor` — flagged by claude-opus-4.7 on 2026-05-15.

The gold PR #10102 is a faithful but **incomplete** resolution of issue #9771.
It correctly obsoletes MONDO:0009327, but it does **not** rewire
`MONDO:0007703` (an already-obsolete term whose stanza reads
`replaced_by: MONDO:0009327`). After #10102, MONDO:0007703 points via
`replaced_by` to a term that is itself now obsolete — a dangling/QC-violating
reference. This was verified still broken in the live `mondo-edit.obo`
(MONDO:0007703 stanza unchanged) as of 2026-05-15. No companion PR fixed it
(`gh search prs --repo monarch-initiative/mondo "9771"` returns only #10102;
#9768 is unrelated).

The `mondo-agent-config` CLAUDE.md states explicitly: *"No relationship should
point to an obsolete term - when you obsolete a term, you may need to also
rewire terms to 'skip' the obsoleted term"*, and the `merge-terms` skill has a
dedicated "Step 6 — Rewire children/references of the obsoleted term". 11 of
14 agent attempts (#31, #275, #28, #27, #33, #70, #51, #26, #332, #229, #19)
correctly performed this rewiring (`MONDO:0007703 replaced_by: MONDO:0009327`
→ `consider: MONDO:0005267`). This extra-but-correct edit is **penalized by
the whole-file metadiff** because it has no counterpart in the single selected
gold PR, suppressing recall/F1 for the best attempts (best F1 only 0.812;
several substantively-correct runs score 0.70–0.81).

Additional metadiff under-representation in this case (normal, not flagged
per-attempt as failure): the gold's free-text `comment` rewording, and the
choice of OMIM xref source qualifier (`MONDO:obsoleteEquivalentObsolete` vs
`MONDO:obsoleteEquivalent`) where both are defensible. Conversely, several
genuinely poor edits *are* charged against attempts in the per-attempt
reviews: invalid synonym evidence tokens (raw URLs, `MONDO:obsolete`,
self-citation), subset/provenance over-stripping, `replaced_by` instead of
`consider` (#24), and adding a `def:` to an obsolete stanza (#24).

Downstream scoring should down-weight or exclude the metadiff F1 for this case
and instead use the per-attempt narrative reviews, which judge each attempt
against the issue and the documented Mondo obsoletion SOP rather than the
incomplete gold.
