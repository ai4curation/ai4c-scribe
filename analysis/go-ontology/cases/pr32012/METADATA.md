---
repo: geneontology/go-ontology
issue_number: 31863
pr_number: 32012
issue_title: "NTR: MF vesicle membrane tethering activity"
issue_created_at: "2026-04-10"
pr_author: dragon-ai-agent
pr_merged_at: "2026-04-29"
pr_num_commits: 1
files_changed:
  - path: src/ontology/go-edit.obo
    additions: 40
    deletions: 30
scoping: tightly_scoped
task_type: obsoletion
difficulty: hard
scope: multi_term
review_outcome: approved_first_time
domain_area: biological_process
tags:
  - obsoletion
  - MF_in_BP
  - vesicle-tethering
  - complex-rewiring
  - multi-term
curated_by: claude-opus-4
curated_at: "2026-05-10"
rationale: Complex multi-term obsoletion with relationship rewiring, demonstrating how namespace corrections cascade through the ontology graph
agent_coverage: none
agent_coverage_note: "no eval attempts generated as of 2026-05-15"
case_quality: poor
case_quality_reason: gold_pr_wrong_issue
companion_prs: [31895]
scoring_caveat: "issue #31863 is a new-term request resolved by PR #31895 (created GO:7770062 + extended GO:0140177). The selected gold PR #32012 does NOT resolve #31863 — it is a downstream obsoletion cascade that addresses issues #31868/#31871/#31872/#31881. An agent prompted with #31863 would correctly produce a new-term PR (~#31895) and score ~F1 0 vs #32012. Re-pair the case (gold=#31895 for the NTR target, or correct issue refs to #31868/#31871/#31872/#31881 for the obsoletion target) before scoring."
quality_flagged_by: claude-opus-4.7
quality_flagged_at: 2026-05-15
---

## Curation Note (data quality)

**Issue-to-gold-PR misattribution.** The case links issue #31863 ("NTR: MF
vesicle membrane tethering activity", a new-term request) to gold PR #32012.
But PR #32012's own body states it "Closes/addresses: #31868, #31871, #31872,
#31881" — it obsoletes 5 vesicle-tethering BP terms (GO:0099022, GO:0099069,
GO:0090522, GO:0099041, GO:0099044) and rewires 8 complex terms to
`capable_of GO:7770062`. The actual resolution of issue #31863 is **PR #31895**
("NTR: vesicle membrane tethering activity (GO:7770062) (fixes #31863)"),
which created GO:7770062 and extended GO:0140177's definition.

PR #32012 is internally well-formed and ontologically sound as an
obsoletion-cascade PR, but it is the wrong reference for issue #31863: it is
neither the whole nor a sub-step of that issue's resolution — it resolves
*other* issues that depend on the term #31895 created. Any future attempt
prompted with issue #31863 should be judged against the issue's actual ask
(create GO:7770062 + extend GO:0140177, i.e. PR #31895), not against #32012's
metadiff. Recommend re-pairing or excluding from scoring. Case-level review:
`analysis/go-ontology/results/reviews/pr32012-claude-case-review.md`.

## Context

Issue #31863 requested a new MF term for vesicle membrane tethering activity, which was added in PR #31895 as GO:7770062. This follow-up PR completes the namespace correction by obsoleting 5 biological_process terms that described vesicle tethering activities and rewiring their associated protein complexes to point at the new MF term.

## Changes Made

In `src/ontology/go-edit.obo` (net +10 lines from 40 additions / 30 deletions):
- Obsoleted 5 vesicle-tethering BP terms that represented molecular functions
- Rewired protein complex terms that previously had `part_of` relationships to the obsoleted BP terms, pointing them instead to the new MF term GO:7770062
- Added appropriate `replaced_by` and `consider` tags for annotation migration guidance
- Updated relationship axioms on complex terms to maintain graph connectivity

## Resolution

Merged directly despite the complexity. This was a well-planned cascade from the new term addition in PR #31895, with clear obsoletion rationale (MF_in_BP correction) and explicit curator approval in the issue discussion. The 40-line addition reflects both obsoletion metadata and the relationship rewiring needed to maintain ontology coherence.
