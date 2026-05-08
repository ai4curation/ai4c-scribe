---
repo: monarch-initiative/mondo
issue_number: 9873
pr_number: 10126
issue_title: "Request for new term Southern tick-associated rash illness"
issue_created_at: "2026-01-13"
pr_author: katiermullen
pr_merged_at: "2026-04-17"
pr_num_commits: 8
files_changed:
  - path: src/ontology/mondo-edit.obo
    additions: 13
    deletions: 0
scoping: tightly_scoped
scoping_notes: PR adds a single new disease term with definition, synonyms, and cross-references.
task_type: new_term
difficulty: medium
scope: single_term
review_outcome: changes_requested
domain_area: infectious-disease
tags:
  - new-term-request
  - tick-borne-disease
  - infectious-disease
  - STARI
  - NCIT
  - SNOMED
curated_by: claude-opus-4
curated_at: "2026-05-08"
rationale: New term request with review iteration on definition wording, requiring cross-reference alignment to NCIT and SNOMED
---

## Context

A user requested a new Mondo term for Southern tick-associated rash illness (STARI), also known as Masters disease. STARI is an infectious disease transmitted by the lone star tick (Amblyomma americanum) that presents with an erythema migrans-like rash similar to Lyme disease but with a distinct etiology. The request (issue #9873) included exact synonyms (STARI, Masters disease), a proposed definition with PubMed references, and cross-references to NCIT:C128427 and SNOMED:444100007.

## Changes Made

The PR added 13 lines to `src/ontology/mondo-edit.obo` introducing a new term stanza classified under MONDO:0025294 "tick-borne infectious disease." The 8 commits reflect review iteration: the initial submission received a CHANGES_REQUESTED review from a senior curator asking for an updated definition, after which the definition was revised and the PR was approved. Cross-references to NCIT and SNOMED were included for interoperability.

## Resolution

Medium difficulty because while the new term follows standard Mondo patterns, the definition required iteration based on reviewer feedback. An agent would need to construct the term stanza with the correct parent classification, parse the user-provided synonyms and cross-references, and be able to revise the definition in response to curator feedback. The review cycle (changes requested then approved) is representative of typical NTR workflows.
