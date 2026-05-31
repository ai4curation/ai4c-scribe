---
repo: obophenotype/cell-ontology
issue_number: 3454
pr_number: 3555
issue_title: "[Class hierarchy] Remove CD44-high and CD122-high from CD45RO-positive memory T cells"
issue_created_at: "2025-11-20"
issue_closed_at: "2026-02-16"
pr_author: copilot-swe-agent
pr_merged_at: "2026-02-16"
pr_num_commits: 4
files_changed:
  - path: src/ontology/cl-edit.owl
    additions: 4
    deletions: 4
scoping: tightly_scoped
task_type: axiom_repair
difficulty: medium
scope: single_term
review_outcome: approved_first_time
domain_area: immunology
tags:
  - axiom-repair
  - marker-removal
  - CD44
  - CD122
  - memory-T-cell
  - species-specific-marker
curated_by: claude-opus-4
curated_at: "2026-05-08"
rationale: Marker correction requiring knowledge of species-specific expression differences between mouse and human T cells
case_quality: poor
case_quality_reason: gold_incomplete_vs_issue_caps_metadiff
scoring_caveat: "Gold PR #3555 added only PMID:24258910 + PMID:21926977 but the issue explicitly requested THREE references added 'along existing ones', including PMID:41254224 (the 'Guidelines for T cell nomenclature' paper the issue flagged for its Table 4 marker list). Every attempt that complied with the issue (added all 3 PMIDs) is penalized by metadiff (precision capped at 0.750, recall reduced by the issue-compliant 3rd PMID line). Attempts that additionally added a term_tracker_item (IAO_0000233) — directed by the config CLAUDE.md — are penalized further (F1 0.667/0.600). The core axiom-repair task (removing RO_0015015 PR_000001307 / PR_000001381 from CL_0001203 and CL_0001204 EquivalentClasses + cleaning both definitions) was performed correctly by ALL 11 attempts. Metadiff here inverts the quality signal: judge attempts against the issue text, not the partial gold."
companion_prs: []
quality_flagged_by: claude-opus-4.7
quality_flagged_at: "2026-05-16"
---

## Context

CD44-high and CD122-high markers were included in the definition of CD45RO-positive memory T cells, but these markers are mouse-specific and not defining characteristics of human memory T cells. CD44 is broadly expressed across human T cell subsets (not specific to memory), and CD122-high expression is specific to mouse memory T cells. Since CD45RO is a human-specific marker, the term definition should not include mouse-specific marker assertions.

## Changes Made

Removed CD44-high and CD122-high marker assertions from the CD45RO-positive memory T cell definition in `cl-edit.owl`, with 4 lines added and 4 removed. The equal line counts reflect removing incorrect marker axioms and updating the definition text accordingly.

## Resolution

Approved on first review. Medium difficulty because correctly identifying which markers are species-specific requires understanding of comparative immunology between mouse and human T cell biology. An agent would need to recognize that combining mouse markers (CD44-high, CD122-high) with a human marker (CD45RO) is biologically inconsistent.

## Curation Note (data quality)

Flagged `case_quality: poor` by claude-opus-4.7 on 2026-05-16.

**Finding.** The single gold PR (#3555, copilot-swe-agent, the only PR for
issue #3454 — no companion PRs) is **incomplete relative to the issue's
explicit instruction**. Issue #3454 states, for both CL_0001203 and
CL_0001204, under a heading reading *"References — do not replace existing
references but add these along existing ones"*: PMID:24258910, PMID:21926977,
**and PMID:41254224**. The gold PR added only the first two and **omitted
PMID:41254224** ("Guidelines for T cell nomenclature", which the issue
specifically called out for its Table 4 list of memory T-cell markers — all
three PMIDs are real and valid, verified via NCBI eUtils).

**Effect on scoring.** Whole-file OBO metadiff compares each attempt to this
partial gold. Consequently:

- The core ontological repair — removing
  `ObjectSomeValuesFrom(obo:RO_0015015 obo:PR_000001307)` (CD44-high) and
  `ObjectSomeValuesFrom(obo:RO_0015015 obo:PR_000001381)` (CD122-high) from the
  EquivalentClasses axioms of CL_0001203 and CL_0001204, plus deleting
  "CD44-high, and CD122-high" from both IAO_0000115 definitions — was performed
  **correctly and completely by all 11 attempts**.
- Every attempt that *complied with the issue* by adding all three requested
  PMIDs is penalized: precision is capped at 0.750 and recall is reduced by the
  issue-compliant 3rd-PMID line, so the best achievable F1 is ~0.750 even for a
  fully correct, more-faithful-than-gold answer.
- Attempts that additionally added a `term_tracker_item` (IAO_0000233 →
  issue #3454) — which the config CLAUDE.md explicitly directs ("Link back to
  the issue ... using the `term_tracker_item`") — are penalized further to
  F1 0.667 / 0.600 for following their instructions.
- Several codex/opencode attempts also carry a benign end-of-file
  serialization artifact (no-op `)` → `)` adding a trailing newline at
  ~line 35622–35624) from their editing tooling; issue-irrelevant churn that
  whole-file metadiff can over-weight.

**Guidance for downstream scoring.** Metadiff here **inverts the quality
signal**. All 11 attempts solved the substantive task; the F1 spread
(0.750 → 0.600) reflects issue-compliant and config-directed extras, not
correctness. Judge attempts against the issue text and the union of (a) the
two marker-axiom removals, (b) both definition text edits, and (c) the three
requested PMIDs — not against the partial gold. Down-weight or exclude this
case from aggregate F1-based agent ranking.
