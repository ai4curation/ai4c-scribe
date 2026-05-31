---
repo: monarch-initiative/mondo
issue_number: 9493
pr_number: 9726
issue_title: "Add parent term to MONDO:0005709 common cold"
issue_labels:
  - user request
  - everycure
  - ai-curation
  - ai-success
  - ai-needed-some-guidance
issue_created_at: "2025-08-22"
pr_author: dragon-ai-agent
pr_merged_at: "2025-12-01"
pr_num_commits: 2
files_changed:
  - path: src/ontology/mondo-edit.obo
    additions: 2
    deletions: 0
scoping: tightly_scoped
scoping_notes: Adds a single is_a parent axiom to an existing term.
task_type: reclassification
difficulty: simple
scope: single_term
review_outcome: changes_requested
domain_area: infectious-disease
tags:
  - reclassification
  - ai-agent
  - common-cold
  - viral-infection
  - respiratory
  - dragon-ai
curated_by: claude-opus-4
curated_at: "2026-05-08"
rationale: AI agent-authored PR demonstrating automated ontology curation with human guidance for a simple reclassification
case_quality: poor
case_quality_reason: gold_has_reviewer_added_pmid_xref
companion_prs: []
scoring_caveat: "The gold PR #9726 is a single PR (no companion PRs), but the merged is_a line is `is_a: MONDO:0024352 {source=\"PMID:37426629\", source=\"https://orcid.org/0000-0003-2955-4640\"}`. PMID:37426629 was added by reviewer @MeeSiing DURING PR review (comment: 'ORCID can't serve as the only cross reference'), and that specific PMID appears nowhere in issue #9493 or its comments. No agent can derive it. This caps every well-scoped agent at F1<=0.5 by construction: the only line agents can match gold on is the IAO:0000233 issue-9493 tracker. Judge attempts against the curator's explicit instruction in the issue (@matentzn: implement Option 3 = is_a MONDO:0024352, no logical definition, ORCID as source, check PMIDs for applicability), not against the line-level metadiff."
quality_flagged_by: claude-opus-4.7
quality_flagged_at: "2026-05-15"
---

## Context

An issue was filed requesting that "common cold" (MONDO:0005709) be given "viral respiratory tract infection" (MONDO:0024352) as a parent term. The common cold was missing this classification, which is important for grouping viral respiratory infections. The issue was addressed by the dragon-ai-agent, an automated curation system, making this one of the first AI-authored PRs in Mondo.

The AI agent analyzed multiple options from its issue analysis and selected the appropriate parent term addition. The issue labels indicate the AI succeeded but needed some human guidance during the process.

## Changes Made

Added 2 lines to `src/ontology/mondo-edit.obo`: an is_a relationship making "common cold" a subclass of "viral respiratory tract infection" and a source attribution annotation. This is a minimal but important classification fix that connects common cold to the broader respiratory infection hierarchy.

## Resolution

Easy difficulty for the ontology change itself (adding one parent axiom), but notable as an AI agent-authored PR. The main challenge was selecting the correct option from multiple possibilities discussed in the issue. An agent needs to understand disease classification well enough to determine that common cold should be classified as a viral respiratory tract infection rather than alternative groupings.

## Curation Note (data quality)

**Flagged poor for scoring purposes by claude-opus-4.7 on 2026-05-15.**

This case is a poor *metadiff* reference even though the gold PR is well-formed
and there are no companion PRs. The merged gold diff is two lines:

```
is_a: MONDO:0024352 {source="PMID:37426629", source="https://orcid.org/0000-0003-2955-4640"} ! viral respiratory tract infection
property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9493" xsd:anyURI
```

The curator instruction in issue #9493 (@matentzn, 2025-11-04) was: *"please
implement Option 3, but I dont add the logical definition. Add
https://orcid.org/0000-0003-2955-4640 as source where suitable, and check any
PMIDs for applicability."* Option 3 = add `is_a: MONDO:0024352` (viral
respiratory tract infection). No PMID for this edit is present anywhere in the
issue body or comments.

`PMID:37426629` was introduced by reviewer **@MeeSiing during PR review**
(2025-12-01, "I have added a PMID to support 'viral respiratory tract
infection' as a parent term... ORCID can't serve as the only cross reference").
Because the gold `is_a` line is sourced to that reviewer-added PMID, **no agent
working only from the issue can reproduce it**, so the `is_a` line never
metadiff-matches gold. The only gold line an agent can match is the
`IAO:0000233` issue-9493 tracker. Consequence:

- Attempts that did everything the curator asked (correct Option-3 parent,
  ORCID source, no logical definition) **and** added the tracker line score
  **F1=0.5** (#310, #179, #256, #157, #87, #66, #46) — these are
  substantively **success**, not partial.
- Attempts that did the correct Option-3 reclassification but omitted the
  tracker line score **F1=0.0** (#406, #495, #529) despite being
  substantively almost-correct — these are **partial_success** (one cheap
  annotation missed), not failure.
- Genuine failures are only the gemma runs (#292, #204), which implemented
  **Option 1** (`is_a: MONDO:0005550` infectious disease) — the literal user
  request, explicitly *not* what the curator directed — with #204 also
  mis-ordering the `is_a` element in the stanza.

Downstream aggregation should down-weight or exclude the metadiff F1 for this
case and judge attempts against the curator's explicit Option-3 instruction.
