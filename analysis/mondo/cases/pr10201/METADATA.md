---
repo: monarch-initiative/mondo
issue_number: 9871
pr_number: 10201
issue_title: "MONDO:0009106 diastematomyelia"
issue_created_at: "2026-01-12"
pr_author: MeeSiing
pr_merged_at: "2026-05-04"
pr_num_commits: 5
files_changed:
  - path: src/ontology/mondo-edit.obo
    additions: 59
    deletions: 21
scoping: loosely_scoped
task_type: other
difficulty: medium
scope: multi_term
review_outcome: changes_requested
curated_by: claude-opus-4
curated_at: "2026-05-10"
rationale: Initially a simple xref fix that expanded into creating 3 subtypes after investigation of split cord malformation classification.
case_quality: poor
case_quality_reason: gold_scope_expanded_off_issue
companion_prs: []
scoring_caveat: "metadiff vs #10201 penalizes well-scoped agents: ~45 of 59 gold additions are 3 new subtype terms (MONDO:1060220-1060222) plus an obsoletion-merge rewrite of MONDO:0035541/0035542 that issue #9871 did NOT request (it explicitly flagged subtypes as 'may or may not be in scope') and that originated from a private curator 1:1, not the issue thread. Judge attempts against the issue's actual ask (Orphanet:1671 -> Orphanet:573278 equivalent swap + provenance cleanup); F1 systematically under-represents quality for attempts that correctly did the xref fix."
quality_flagged_by: claude-opus-4.7
quality_flagged_at: "2026-05-15"
---

## Context

Issue #9871 reported that MONDO:0009106 (diastematomyelia) had an incorrect Orphanet cross-reference (Orphanet:1671 for "Split cord malformation type I" rather than the broader concept). Investigation revealed that Orphanet:573278 correctly maps to the broader concept of diastematomyelia/split cord malformation, and that subtypes (type I with osseous spur, type II with fibrous septum) should be represented.

## Changes Made

The PR evolved from a simple xref correction into a multi-term edit across 5 commits. The initial commit updated the Orphanet xref from 1671 to 573278. A proxy merge was fixed in the second commit. The third commit added 3 new subtypes (MONDO:1060220-1060222) for split cord malformation classification. The fourth and fifth commits resolved merge conflicts with master. The 59 additions and 21 deletions reflect both the xref correction and the creation of new subtype terms with definitions, synonyms, and parent axioms.

## Resolution

Moderate difficulty because the scope expanded significantly from the original request. What began as a cross-reference correction required domain knowledge about split cord malformation types to realize that subtypes were needed. The merge conflicts and multiple commits show iterative development. An agent would need to recognize when an xref discrepancy indicates a deeper modeling issue requiring new terms.

## Curation Note (data quality)

Flagged `case_quality: poor` (`gold_scope_expanded_off_issue`) by claude-opus-4.7 on
2026-05-15 during agent-eval review.

There are **no companion PRs** — issue #9871 was resolved entirely by the single gold PR
#10201. The poor-case signature here is Step-3b "gold has a large out-of-scope expansion":

- **What the issue asked for:** swap the over-narrow Orphanet equivalent `Orphanet:1671`
  (SCM type I) for `Orphanet:573278` (split cord malformation) on MONDO:0009106. The
  reporter *explicitly* added: "SCM type 1 and 2 are narrower subtypes that **may or may
  not be in scope for Mondo**." So subtype creation was flagged as uncertain scope in the
  issue itself.
- **What the gold PR did:** the requested xref fix + synonym-scope refinements (≈14 of 59
  additions), PLUS three brand-new subtype terms MONDO:1060220 (type I), MONDO:1060221
  (type II), MONDO:1060222 (composite type) and a full obsoletion-merge rewrite of
  MONDO:0035541 / MONDO:0035542 (TermsMerged, replaced_by) — ≈45 of 59 additions.
- **Why this is off-issue:** the subtype expansion did not come from the issue thread; per
  the human PR comments it came from a private curator 1:1 ("Sabrina agreed ... She asked
  for all 3 subtypes ... to be added"). The subtype MONDO IDs (MONDO:1060220-1060222) are
  also unguessable placeholders — no agent could reproduce them even with correct intent.

Consequently the metadiff F1 (best 0.45) **systematically under-represents** the quality of
attempts that correctly performed the requested xref fix and made a defensible, issue-cited
decision to leave subtype modeling for editor follow-up (notably eval PRs #391 opus, #563
codex, #249 kimi). Downstream scoring/aggregation should down-weight or exclude this case,
and attempts should be judged against the issue's actual ask, not the full gold diff. Note
two attempts (#489/#524, copilot/sonnet-4.5, identical blob `fff2006`) genuinely failed the
in-scope ask (no Orphanet:573278 equivalent added) — their low F1 is not solely an artifact.
