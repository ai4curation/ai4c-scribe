---
repo: obophenotype/cell-ontology
issue_number: 3590
pr_number: 3591
issue_title: "add subset tag 'add_by_HRA'"
issue_created_at: "2026-03-14"
issue_closed_at: "2026-03-20"
pr_author: nicolevasilevsky
pr_merged_at: "2026-03-20"
pr_num_commits: 4
files_changed:
  - path: src/ontology/cl-edit.owl
    additions: 6
    deletions: 0
scoping: tightly_scoped
task_type: other
difficulty: simple
scope: single_term
review_outcome: changes_requested
domain_area: metadata
tags:
  - subset-annotation
  - HRA
  - annotation-property
curated_by: claude-opus-4
curated_at: "2026-05-08"
rationale: Simple annotation property addition demonstrating subset tagging patterns used for HRA provenance tracking
case_quality: poor
case_quality_reason: gold_renegotiated_in_pr_comments
companion_prs: []
scoring_caveat: "Metadiff caps achievable F1 well below 1.0 for two reasons unobservable to any agent: (1) the gold rdfs:comment text was dictated verbatim by reviewer @dosumis in a post-submission PR review comment ('Classes tagged with this subset property were added on request from HuBMAP to support the HuBMAP Human Reference Atlas (HRA).'), replacing the author's original wording; (2) the issue title/body request the property name 'add_by_HRA' (a typo) but the human silently used 'added_by_HRA'. Agents using the typo name score F1=0.000 despite correct OWL mechanics; agents using the corrected name cap at F1=0.667 due to comment wording + a defensible extra rdfs:label. Judge attempts on substance (declaration + SubAnnotationPropertyOf subset axiom + correct name) not the metadiff."
quality_flagged_by: claude-opus-4.7
quality_flagged_at: "2026-05-16"
---

## Context

The Human Reference Atlas (HRA) project needed a way to track which cell types were contributed through their program. A new subset annotation tag `added_by_HRA` was requested to mark terms added at HRA's request.

## Changes Made

Added a new `oboInOwl:SubsetProperty` declaration for `added_by_HRA` to `src/ontology/cl-edit.owl`. This involved declaring the annotation property and adding appropriate label and comment annotations. The change is purely additive with 6 new lines.

## Resolution

Despite being a simple change, this PR went through review: an initial review was dismissed and a subsequent approval was given. The difficulty is simple because it only requires knowing how OWL subset properties are declared in OBO-format ontologies, but it demonstrates the pattern for provenance-tracking subsets.

## Curation Note (data quality)

`case_quality: poor` — `gold_renegotiated_in_pr_comments` (flagged claude-opus-4.7, 2026-05-16).

This is a single-PR resolution (PR #3591 fully resolves issue #3590; the
issue's follow-up comment about tagging individual terms is an explicitly
separate future task, not part of this gold). There is no multi-PR partial-gold
problem. However, the metadiff is a poor proxy for quality here for two
reasons that no agent could have observed at submission time:

1. **Gold comment text renegotiated in PR review.** The author's original
   `rdfs:comment` was rejected by reviewer @dosumis, who dictated the exact
   replacement wording in a PR review comment / issue comment on 2026-03-18:
   *"Classes tagged with this subset property were added on request from
   HuBMAP to support the HuBMAP Human Reference Atlas (HRA)."* The merged gold
   uses precisely this text. An agent working only from the issue cannot
   reproduce text that did not exist until a human review round, so the
   comment line mismatches for every attempt.

2. **Issue-title typo vs. silent human correction.** The issue title and body
   request the subset name **`add_by_HRA`** (a typo). The human curator
   silently used **`added_by_HRA`** (consistent with the existing
   `added_for_HCA` pattern). Agents that faithfully reproduced the literal
   request (`add_by_HRA`: pr274 opus, pr146 haiku, pr125 gemma) score
   F1=0.000 on a token mismatch despite ontologically correct work. Agents
   that inferred the correction (`added_by_HRA`: pr250, pr201 sonnet) cap at
   F1=0.667 due to the comment wording plus one extra, defensible `rdfs:label`
   assertion (gold adds no label, per CL subset-property convention).

**Consequence for scoring:** maximum achievable F1 on this case is ~0.667 and
is gated by unobservable post-submission negotiation, so F1 systematically
under-represents agent quality. All five attempts implemented the correct OWL
subset-property mechanism (`Declaration` + `SubAnnotationPropertyOf(...
oboInOwl:SubsetProperty)`); the discriminating signals are (a) whether the
agent corrected the issue typo and (b) declaration ordering (pr125 mis-ordered
the declaration after `added_for_HCA`). Downstream aggregation should
down-weight or exclude this case, or judge it on substance rather than
metadiff.
