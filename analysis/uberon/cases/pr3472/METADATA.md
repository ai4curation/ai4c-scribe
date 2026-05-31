---
repo: obophenotype/uberon
issue_number: 3471
pr_number: 3472
issue_title: "[Text Def] UBERON:0022232 secondary visual cortex has no textual definition"
issue_created_at: "2025-02-04"
pr_author: shawntanzk
pr_merged_at: "2025-02-04"
pr_num_commits: 2
files_changed:
  - path: src/ontology/uberon-edit.obo
    additions: 1
    deletions: 0
scoping: tightly_scoped
task_type: axiom_repair
difficulty: simple
scope: single_term
review_outcome: approved_first_time
domain_area: neuroanatomy
tags:
  - definition-addition
  - visual-cortex
  - missing-definition
curated_by: claude-opus-4
curated_at: "2026-05-08"
rationale: Adding a missing text definition to a single neuroanatomical term, same-day turnaround
case_quality: poor
case_quality_reason: gold_pr_is_partial
companion_prs: []
scoring_caveat: "metadiff vs gold PR #3472 only covers the def-addition half of issue #3471; gold never removed the redundant `part_of UBERON:0002021 ! occipital lobe` axiom that the issue explicitly requested (axiom still present in upstream master as of 2026-05-16). All 9 agents correctly removed it and are therefore penalized on recall for doing the correct, issue-mandated work. Judge attempts against the full issue (def + redundancy removal), not against the partial gold."
quality_flagged_by: claude-opus-4.7
quality_flagged_at: "2026-05-16"
---

## Context

Issue #3471 reported that UBERON:0022232 (secondary visual cortex) lacked a textual definition. This is a well-characterized brain region (also known as V2 or Brodmann area 18) adjacent to the primary visual cortex, responsible for further processing of visual information.

## Changes Made

The PR added a single definition line to the secondary visual cortex term stanza in src/ontology/uberon-edit.obo. The definition describes the region's location, function in visual processing, and relationship to the primary visual cortex.

## Resolution

Simple difficulty. Adding a text definition to an existing term is a mechanical operation in OBO format. An agent needs to locate the term stanza and add a properly formatted def tag with an accurate definition. The same-day turnaround from issue to merge confirms the straightforward nature of this task.

## Curation Note (data quality)

`case_quality: poor` — `gold_pr_is_partial`. Flagged by claude-opus-4.7 on 2026-05-16.

Issue #3471 contained **two explicit asks**:

1. Add the suggested textual definition (verbatim wording + xrefs `ISBN:978-0-323-10027-4`, `ISSN:0072-9752`, `WikipediaVersioned:Visual_cortex&oldid=1268682728`).
2. Remove the redundant `relationship: part_of UBERON:0002021 ! occipital lobe` axiom (the reporter explicitly noted: "There already is 'part of' some 'visual cortex', and 'visual cortex' is 'part of' some 'occipital lobe'").

The gold PR #3472 (`add def for secondary visual cortex`, shawntanzk, merged 2025-02-04) only performed ask #1 — a single `+def:` line, `additions: 1, deletions: 0`. It never removed the redundant occipital-lobe axiom. Verified that the redundant `relationship: part_of UBERON:0002021 {source="MA"} ! occipital lobe` is **still present in upstream `obophenotype/uberon` master as of 2026-05-16**, and that the redundancy is genuine (UBERON:0022232 `part_of` UBERON:0000411 visual cortex, and UBERON:0000411 has `relationship: part_of UBERON:0002021 ! occipital lobe`, so the direct axiom is entailed by `part_of` transitivity). No companion PR resolved the redundancy (`gh search prs` for "3471"/"UBERON:0022232"/"secondary visual cortex" returns only #3472 as issue-linked).

Consequence: the metadiff scores systematically **under-represent** quality. All 9 agent attempts correctly removed the redundant axiom — i.e., they did the issue-mandated work that gold omitted — and are penalized on recall for it (capping F1 at ~0.667 even for byte-clean attempts, and producing F1=0.000 for attempts that paraphrased the def or carried serialization churn). Attempts should be judged against the union of the issue's two asks, not against the partial gold #3472. Downstream scoring should down-weight or exclude this case.
