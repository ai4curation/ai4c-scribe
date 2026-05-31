---
repo: monarch-initiative/mondo
issue_number: 9892
pr_number: 10206
issue_title: "chronic myelogenous leukemia, BCR-ABL1 positive"
issue_labels:
  - relabel term
  - user request
issue_created_at: "2026-01-22"
pr_author: MeeSiing
pr_merged_at: "2026-04-30"
pr_num_commits: 3
files_changed:
  - path: src/ontology/mondo-edit.obo
    additions: 7
    deletions: 8
scoping: tightly_scoped
scoping_notes: Changes limited to relabeling one term and updating its synonyms.
task_type: synonym_update
difficulty: simple
scope: single_term
review_outcome: changes_requested
domain_area: oncology
tags:
  - relabel
  - leukemia
  - BCR-ABL1
  - OMIM
  - nomenclature
curated_by: claude-opus-4
curated_at: "2026-05-08"
rationale: Label update requiring judgment about naming conventions and alignment with OMIM nomenclature
case_quality: poor
case_quality_reason: gold_has_out_of_scope_extra_edits
companion_prs: []
scoring_caveat: "Issue #9892 asked only to relabel MONDO:0011996 to 'chronic myeloid leukemia' and keep the prior precise label as a synonym. Gold PR #10206 additionally performed unrequested OMIM-alignment/QC churn — repointing the 'chronic myeloid leukemia' synonym xref list (adding the issue's 3 source URLs PLUS curator ORCID 0000-0001-9310-0163), deleting three 'leukemia, ...' synonyms, and adding the typo-bearing 'synonym: \"leukimia, chronic myeloid\" EXACT [OMIM:608232]' (a byproduct of its 'normalize to fix failed qc' / 'fix failed qc of double genes' commits). None of this is derivable from the issue, so metadiff caps every well-scoped agent at ~0.769 by construction and UNDER-represents quality for the 0.769 cluster. The 0.211 gemma runs, by contrast, are genuinely incomplete (missed referrer comments, term-tracker, and a likely label/synonym QC violation) — that low F1 is representative, not an artifact."
quality_flagged_by: claude-opus-4.7
quality_flagged_at: "2026-05-15"
---

## Context

A request was made to relabel MONDO:0011996 to "chronic myeloid leukemia" to better align with OMIM's naming ("leukemia, chronic myeloid"). The existing label "chronic myelogenous leukemia, BCR-ABL1 positive" was considered overly specific for the primary label, as the BCR-ABL1 qualifier could be captured as a synonym instead.

The PR involved some discussion about how strictly Mondo should follow OMIM naming conventions, reflected in the 3 commits needed to finalize the label.

## Changes Made

Relabeled MONDO:0011996 from "chronic myelogenous leukemia, BCR-ABL1 positive" to "chronic myeloid leukemia" in `src/ontology/mondo-edit.obo`. The old label and variations were preserved as synonyms. The 7 additions and 8 deletions reflect the label change plus synonym adjustments across 3 commits.

## Resolution

Easy difficulty overall, though it required a minor judgment call about naming conventions. The multiple commits suggest some back-and-forth about the exact label wording. An agent would need to understand Mondo's relationship with OMIM naming and when to simplify versus preserve qualifier terms.

## Curation Note (data quality)

*Added by claude-opus-4.7, 2026-05-15.*

This is flagged `case_quality: poor` because the gold PR over-reaches the issue,
making metadiff F1 a poor proxy for the well-scoped attempts.

**What issue #9892 actually asked for** (verified against the issue body and the only
PR resolving it, #10206 — there are no companion PRs): (1) relabel MONDO:0011996 to
"chronic myeloid leukemia"; (2) keep "chronic myelogenous leukemia, BCR-ABL1 positive"
as a synonym. The issue body cites three source URLs (cancer.gov, medlineplus.gov,
cancer.org).

**What gold PR #10206 additionally did, none of it requested by the issue:**

- Repointed the existing `synonym: "chronic myeloid leukemia" EXACT` xref list from
  `[DOID:8552, NCIT:C3174, Orphanet:521]` to additionally include the three issue
  URLs **plus the human curator's own ORCID** `https://orcid.org/0000-0001-9310-0163`
  (the ORCID is not derivable from the issue by any agent).
- Deleted `synonym: "leukemia, chronic myeloid" RELATED []`,
  `synonym: "leukemia, chronic myeloid, Philadelphia chromosome positive, somatic"
  EXACT []`, and `synonym: "leukemia, Philadelphia chromosome-positive, resistant to
  imatinib, Somatic mutation" EXACT []`.
- Added `synonym: "leukimia, chronic myeloid" EXACT [OMIM:608232]` — a verbatim,
  typo-bearing OMIM-pipeline synonym introduced by the PR's "normalize to fix failed
  qc" / "fix failed qc of double genes" commits, not a curation decision tied to the
  issue.

**Consequence for scoring.** Every well-scoped attempt is capped at ~0.769 F1 purely
because it (correctly) did not reproduce this gold-only OMIM/QC churn. The four 0.769
runs (#520, #488, #397, #251) and the four 0.741 runs (#435, #82, #63, #44) are
substantively correct, complete, tightly scoped solutions to the *issue*; their F1
**under-represents** quality. #251 (kimi-k2.6) is the strongest — it actually read the
issue's cited URLs and migrated them onto the synonym, matching gold's intent.

Conversely, the two gemma-4-31b runs (#291, #206, F1=0.211) are **genuinely
incomplete**, not metadiff victims: they skipped the three `is_a` referrer comment
updates and the `IAO:0000233` term-tracker item, left an EXACT synonym identical to the
new primary label (a likely Mondo QC failure), and made inaccurate self-reports
("moved to synonyms list" when no synonym was added). For these runs the low F1 is
representative. Downstream aggregation should down-weight the 0.769/0.741 cap as a gold
artifact but treat the gemma gap as real.
