---
repo: monarch-initiative/mondo
issue_number: 9861
pr_number: 10113
issue_title: "[NTR/gene] Hyperinsulinemic hypoglycemia, familial 3"
issue_created_at: "2026-01-07"
pr_author: MeeSiing
pr_merged_at: "2026-04-02"
pr_num_commits: 6
files_changed:
  - path: src/ontology/mondo-edit.obo
    additions: 13
    deletions: 6
scoping: tightly_scoped
scoping_notes: PR relabels an existing term and updates its classification and synonyms based on user request.
task_type: other
difficulty: medium
scope: single_term
review_outcome: changes_requested
domain_area: metabolic-disease
tags:
  - relabel
  - gene-disease
  - GCK
  - hyperinsulinism
  - OMIM
  - familial-hyperinsulinism
curated_by: claude-opus-4
curated_at: "2026-05-08"
rationale: Term relabeling with review iteration on classification, requiring confirmation that existing OMIM term matches the user request
case_quality: ok
case_quality_reason: ambiguous_requirement_plus_review_driven_change
companion_prs: []
scoring_caveat: "Gold PR #10113 is the complete, sole resolution (PR #10090 is only its conflicted predecessor, not a companion). Low metadiff F1 (0.19-0.42 across all 10 attempts) is NOT a metadiff artifact and NOT a partial-gold problem; it reflects two genuine, largely unforeseeable divergences: (1) the issue is internally contradictory on the primary label — the issue body lists 'Hyperinsulinemic hypoglycemia, familial 3' as the preferred label while commenter tpollin (ClinGen GCEP Co-Chair) explicitly asks for 'GCK-related hyperinsulinism' as primary; the gold curator chose the OMIM-style label as primary and made 'GCK-related hyperinsulinism' a ClinGen-preferred EXACT synonym (OMO:0002001), the opposite of tpollin's stated request, so 9/10 agents that reasonably honored the explicit request were systematically penalized; (2) the gold removed is_a MONDO:0015624, added relationship excluded_subClassOf MONDO:0015624, and added is_a MONDO:0019010 — a reclassification that emerged only from the reviewer's CHANGES_REQUESTED dialogue and is not derivable from the issue. Judge attempts primarily on the core disambiguation (recognize MONDO:0011236 already covers the request and update in place), definition refresh with the supplied PMIDs, ClinGen OMO:0002001 synonym handling, and provenance hygiene (keep #4985 tracker, add #9861); treat the primary-label choice as a defensible interpretation and the classification restructuring as out-of-foresight."
quality_flagged_by: claude-opus-4.7
quality_flagged_at: "2026-05-15"
---

## Context

A user requested a new gene-disease term for "hyperinsulinemic hypoglycemia, familial 3" (GCK-related hyperinsulinism) under issue #9861. During curation, it was determined that the existing term MONDO:0011236 already represented this disease but carried an outdated label. Rather than creating a duplicate, the curator updated the label and synonyms of the existing term. The PR also replaced an earlier failed attempt (PR #10090) that had git conflicts.

## Changes Made

The PR modified MONDO:0011236 in `src/ontology/mondo-edit.obo` with 13 additions and 6 deletions across 6 commits. Changes included updating the rdfs:label to "hyperinsulinemic hypoglycemia, familial, 3", adding "GCK-related hyperinsulinism" as an exact synonym, and adjusting the classification under MONDO:0017182 "familial hyperinsulinism." The multiple commits reflect both the review iteration (a CHANGES_REQUESTED review asking about classification) and the recreation of the PR after rebasing issues.

## Resolution

Medium difficulty because the curator needed to recognize that an existing term matched the new term request rather than creating a duplicate. The review process involved a classification question from the reviewer, requiring the contributor to confirm that the OMIM entry and the requested term were the same concept. An agent would need to search for existing terms before creating new ones and handle reviewer questions about hierarchical placement.

## Curation Note (data quality)

Flagged by claude-opus-4.7 on 2026-05-15 during agent-attempt review.

**This is NOT a poor case in the gold-PR sense:** PR #10113 is the complete and
sole human resolution of issue #9861. The other PR returned by search, #10090, is
merely the conflicted predecessor that #10113 replaced (`replace #10090` in the PR
body) — there are no companion PRs, and the CASE_BRIEF gold diff matches the merged
PR diff byte-for-byte.

**Why every attempt scores low F1 (0.188–0.421), and how to read it:** the low
scores are genuine substantive divergence, not a metadiff artifact. Two factors:

1. **Contradictory primary-label requirement.** The issue body lists
   "Hyperinsulinemic hypoglycemia, familial 3" as the *preferred gene-related
   syndrome label* and "GCK-related hyperinsulinism" as a *synonym*. The comment
   thread then reverses this: `tpollin` (Co-Chair, ClinGen Monogenic Diabetes GCEP)
   explicitly asks for "GCK-related hyperinsulinism" as the **primary** term. The
   gold curator chose the OMIM-style label "hyperinsulinemic hypoglycemia, familial,
   3" as primary and made "GCK-related hyperinsulinism" a ClinGen-preferred EXACT
   synonym (`{OMO:0002001=".../clingen"}`) — the opposite of `tpollin`'s stated
   request. 9/10 agents reasonably honored the explicit ClinGen request and were
   systematically penalized on precision for it. Treat the primary-label choice as a
   defensible interpretation, not an error.

2. **Reviewer-driven reclassification.** After a CHANGES_REQUESTED review by
   `katiermullen` about classification, the gold *removed* `is_a: MONDO:0015624`
   (diazoxide-sensitive diffuse hyperinsulinism), added
   `relationship: excluded_subClassOf MONDO:0015624`, and added
   `is_a: MONDO:0019010` (congenital isolated hyperinsulinism). This is not derivable
   from the issue text; no agent (single-shot, no reviewer dialogue) could foresee
   it. Do not penalize attempts for missing it beyond noting incompleteness.

**Recommended grading basis:** judge attempts on (a) the core disambiguation —
recognizing MONDO:0011236 already covers the request and updating it in place rather
than minting a duplicate; (b) refreshing the definition with the supplied
PMID:15277402/24890200/34680961 (and retaining Orphanet:79299); (c) correct ClinGen
`OMO:0002001` synonym handling; (d) provenance hygiene — adding the `#9861`
`IAO:0000233` tracker *without dropping* the existing `#4985` tracker. Metadiff F1
materially under-represents quality for the higher-tier attempts (kimi #270, the
gpt/copilot runs) and roughly tracks quality for the weakest (haiku #194, which also
has a malformed `intersection_of` axiom and an empty PR narrative).
