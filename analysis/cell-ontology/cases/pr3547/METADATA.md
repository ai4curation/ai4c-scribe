---
repo: obophenotype/cell-ontology
issue_number: 3333
pr_number: 3547
issue_title: "Dont relabel imported annotation properties"
issue_created_at: "2025-09-16"
issue_closed_at: "2025-12-22"
pr_author: gouttegd
pr_merged_at: "2025-12-22"
pr_num_commits: 1
files_changed:
  - path: src/ontology/cl-edit.owl
    additions: 0
    deletions: 24
scoping: tightly_scoped
task_type: axiom_repair
difficulty: simple
scope: multi_term
review_outcome: approved_first_time
domain_area: ontology-maintenance
tags:
  - annotation-properties
  - import-management
  - cleanup
curated_by: claude-opus-4
curated_at: "2026-05-08"
rationale: Purely subtractive cleanup removing redundant annotation property labels from the edit file
case_quality: ok
case_quality_reason: issue_number_misattributed_but_gold_sound
companion_prs: [3333, 3589]
scoring_caveat: "Gold PR #3547 is a complete, self-contained, curator-approved resolution; metadiff F1 is accurate (1.0 attempts are genuinely perfect, 0.522 attempts genuinely over-remove and lose information). Only the recorded issue_number is wrong (see Curation Note); scoring is unaffected."
quality_flagged_by: claude-opus-4.7
quality_flagged_at: "2026-05-16"
---

## Context

This is the second occurrence of the recurring issue where imported annotation properties (oboInOwl:hasDbXref, oboInOwl:hasExactSynonym, etc.) accumulate redundant `rdfs:label` annotations in the edit file. These labels already exist in the merged imports and their presence in the edit file is confusing and unnecessary. The issue was originally fixed in PR #3333 but the labels crept back in.

## Changes Made

Removed 24 lines of redundant `rdfs:label` annotations for imported annotation properties from `cl-edit.owl`. This is a purely subtractive change with no additions.

## Resolution

Approved on first review in a single commit. Simple difficulty because the fix is purely mechanical deletion, but it demonstrates an important maintenance pattern: understanding which annotations belong in the edit file versus the imports. An agent would need to understand OWL import chains to know which labels are redundant.

## Curation Note (data quality)

*Added by claude-opus-4.7 on 2026-05-16 during attempt review.*

**Issue/PR number misattribution (does not affect scoring).** The frontmatter
records `issue_number: 3333`, but #3333 is itself the *first* fix PR
("Dont relabel imported annotation properties", merged 2025-09-17,
`closes #3332`), **not** an issue. The actual originating GitHub issue is
**#3332** ("Re-labelling of imported annotation properties in the -edit file"),
in which gouttegd proposes removing the redundant labels and matentzn agrees.
Gold PR **#3547** ("Do not relabel imported annotation properties (again).")
re-removes the six `oboInOwl:*` synonym/xref labels that were inadvertently
reintroduced by PR #3232. A *third* round later occurred in PR **#3589**
("…ter", closes #3588, March 2026), which also adds a guard check. Recommend
correcting `issue_number` to 3332; `companion_prs` records the related rounds
(#3333 prior, #3589 subsequent — neither is part of this round's gold).

**Scoring is sound — case is NOT a poor evaluation case.** Gold PR #3547 is a
single-commit, curator-approved, purely subtractive change that exactly
implements the conservative criterion in issue #3332: remove a label only if
the same predicate–subject pair already carries an `rdfs:label` in
`src/ontology/imports/merged_import.owl`. Direct inspection of
`merged_import.owl` confirms the six removed properties (`hasBroadSynonym`,
`hasDbXref`, `hasExactSynonym`, `hasNarrowSynonym`, `hasRelatedSynonym`,
`hasSynonymType`) are all labeled upstream (safe to remove), while
`obo:IAO_0000028`, `oboInOwl:SubsetProperty`, `oboInOwl:consider`,
`oboInOwl:inSubset`, and `rdfs:seeAlso` are **not** labeled upstream (gold
correctly keeps them). The metadiff therefore reflects true quality:
attempts #236 and #185 (F1=1.0) are genuinely perfect; attempts #202 and #145
(F1=0.522) genuinely over-remove and cause information loss. No base
contamination, no gold leakage, no curator repudiation, no out-of-scope gold
edit, no metadiff-blind field. F1 is neither over- nor under-representing
quality here.
