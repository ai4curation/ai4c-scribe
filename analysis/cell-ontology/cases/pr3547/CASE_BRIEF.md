---
ontology: cell-ontology
repo: obophenotype/cell-ontology
issue_number: 3333
pr_number: 3547
issue_title: Dont relabel imported annotation properties
pr_author: gouttegd
pr_merged_at: '2025-12-22'
task_type: axiom_repair
difficulty: simple
scoping: tightly_scoped
scope: multi_term
review_outcome: approved_first_time
num_agent_attempts: 9
generated_at: '2026-05-17'
domain_area: ontology-maintenance
best_f1: 1.0
best_model: claude-sonnet-4.5
---

# PR #3547 — Dont relabel imported annotation properties

**cell-ontology** | [obophenotype/cell-ontology](https://github.com/obophenotype/cell-ontology) | [Issue #3333](https://github.com/obophenotype/cell-ontology/issues/3333) | [PR #3547](https://github.com/obophenotype/cell-ontology/pull/3547) | @gouttegd | merged 2025-12-22

`axiom_repair` `simple` `tightly_scoped` `approved_first_time`

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

## Human Diff

```diff
diff --git a/src/ontology/cl-edit.owl b/src/ontology/cl-edit.owl
index 31e356a79..e61c1d874 100644
--- a/src/ontology/cl-edit.owl
+++ b/src/ontology/cl-edit.owl
@@ -3662,30 +3662,6 @@ AnnotationAssertion(rdfs:label oboInOwl:SubsetProperty "subset_property")
 
 AnnotationAssertion(rdfs:label oboInOwl:consider "consider")
 
-# Annotation Property: oboInOwl:hasBroadSynonym (has_broad_synonym)
-
-AnnotationAssertion(rdfs:label oboInOwl:hasBroadSynonym "has_broad_synonym")
-
-# Annotation Property: oboInOwl:hasDbXref (database_cross_reference)
-
-AnnotationAssertion(rdfs:label oboInOwl:hasDbXref "database_cross_reference")
-
-# Annotation Property: oboInOwl:hasExactSynonym (has exact synonym)
-
-AnnotationAssertion(rdfs:label oboInOwl:hasExactSynonym "has_exact_synonym")
-
-# Annotation Property: oboInOwl:hasNarrowSynonym (has narrow synonym)
-
-AnnotationAssertion(rdfs:label oboInOwl:hasNarrowSynonym "has_narrow_synonym")
-
-# Annotation Property: oboInOwl:hasRelatedSynonym (has_related_synonym)
-
-AnnotationAssertion(rdfs:label oboInOwl:hasRelatedSynonym "has_related_synonym")
-
-# Annotation Property: oboInOwl:hasSynonymType (has_synonym_type)
-
-AnnotationAssertion(rdfs:label oboInOwl:hasSynonymType "has_synonym_type")
-
 # Annotation Property: oboInOwl:inSubset (in_subset)
 
 AnnotationAssertion(rdfs:label oboInOwl:inSubset "in_subset")

```

## Agent Attempts (9)

| # | Model | Runtime | F1 | P | R | Blob | Eval PR | Detail |
|---|-------|---------|-----|-----|-----|------|---------|--------|
| 1 | claude-sonnet-4.5 | copilot | 1.000 | 1.000 | 1.000 | `e61c1d8` | [#236](https://github.com/ai4curation/eval-ont-agent-cl/pull/236) | [attempt](attempts/pr236.md) |
| 2 | claude-opus-4.7 | claude | 1.000 | 1.000 | 1.000 | `e61c1d8` | [#185](https://github.com/ai4curation/eval-ont-agent-cl/pull/185) | [attempt](attempts/pr185.md) |
| 3 | claude-sonnet-4.5 | claude | 0.522 | 0.500 | 0.545 | `17912f0` | [#202](https://github.com/ai4curation/eval-ont-agent-cl/pull/202) | [attempt](attempts/pr202.md) |
| 4 | claude-haiku-4.5 | claude | 0.522 | 0.500 | 0.545 | `17912f0` | [#145](https://github.com/ai4curation/eval-ont-agent-cl/pull/145) | [attempt](attempts/pr145.md) |
| 5 | gpt-5.4 | opencode | 0.480 | 0.500 | 0.462 | `b791e1e` | [#583](https://github.com/ai4curation/eval-ont-agent-cl/pull/583) | [attempt](attempts/pr583.md) |
| 6 | gpt-5.4 | opencode | 0.480 | 0.500 | 0.462 | `b791e1e` | [#522](https://github.com/ai4curation/eval-ont-agent-cl/pull/522) | [attempt](attempts/pr522.md) |
| 7 | gpt-5.5 | opencode | 0.429 | 0.500 | 0.375 | `5b0ac60` | [#546](https://github.com/ai4curation/eval-ont-agent-cl/pull/546) | [attempt](attempts/pr546.md) |
| 8 | gpt-5.5 | opencode | 0.429 | 0.500 | 0.375 | `5b0ac60` | [#486](https://github.com/ai4curation/eval-ont-agent-cl/pull/486) | [attempt](attempts/pr486.md) |
| 9 | gpt-5.4 | codex | 0.429 | 0.500 | 0.375 | `77f430a` | [#322](https://github.com/ai4curation/eval-ont-agent-cl/pull/322) | [attempt](attempts/pr322.md) |
