---
ontology: uberon
repo: obophenotype/uberon
issue_number: 3618
pr_number: 3620
issue_title: sixth lumbar dorsal root ganglion
pr_author: dragon-ai-agent
pr_merged_at: '2025-11-03'
task_type: new_term
difficulty: medium
scoping: tightly_scoped
scope: single_term
review_outcome: approved_first_time
num_agent_attempts: 4
generated_at: '2026-05-15'
domain_area: neuroanatomy
best_f1: 0.947
best_model: claude-opus-4.7
---

# PR #3620 — sixth lumbar dorsal root ganglion

**uberon** | [obophenotype/uberon](https://github.com/obophenotype/uberon) | [Issue #3618](https://github.com/obophenotype/uberon/issues/3618) | [PR #3620](https://github.com/obophenotype/uberon/pull/3620) | @dragon-ai-agent | merged 2025-11-03

`new_term` `medium` `tightly_scoped` `approved_first_time`

## Context

A new term was requested for the sixth lumbar dorsal root ganglion. Uberon already had terms for L1 through L5 dorsal root ganglia, so this request extended the series for species with six lumbar vertebrae.

## Changes Made

Added UBERON:9900001 for "sixth lumbar dorsal root ganglion" with synonyms (L6 dorsal root ganglion, sixth lumbar spinal ganglion), a definition, and relationships following the pattern established by the existing L1-L5 terms. The term was placed as part_of the appropriate spinal segment.

## Resolution

Medium difficulty because the agent must identify and follow the existing naming and axiom pattern for the L1-L5 series. It needs to understand that different species have different numbers of lumbar vertebrae and that the term must be modeled consistently with its siblings in the series.

## Human Diff

```diff
diff --git a/src/ontology/uberon-edit.obo b/src/ontology/uberon-edit.obo
index 45a291322..8b5f5a283 100644
--- a/src/ontology/uberon-edit.obo
+++ b/src/ontology/uberon-edit.obo
@@ -225622,6 +225622,19 @@ is_a: UBERON:0006914 ! squamous epithelium
 relationship: has_part CL:4030023 ! respiratory tract hillock cell
 relationship: part_of UBERON:0007196 ! tracheobronchial tree
 
+[Term]
+id: UBERON:9900001
+name: sixth lumbar dorsal root ganglion
+def: "The group of nerve cell bodies located on the dorsal spinal roots within the vertebral column at the level of the sixth lumbar vertebra." [PMID:18316160]
+subset: defined_by_ordinal_series
+synonym: "L6 dorsal root ganglion" EXACT []
+synonym: "sixth lumbar spinal ganglion" EXACT []
+is_a: UBERON:0002836 ! lumbar dorsal root ganglion
+created_by: dragon-ai-agent
+relationship: dc-contributor https://orcid.org/0000-0003-0289-8988 ! Stan Laulederkind
+property_value: dcterms-date "2025-11-03T00:00:00Z" xsd:dateTime
+property_value: term_tracker_item "https://github.com/obophenotype/uberon/issues/3618" xsd:anyURI
+
 [Typedef]
 id: aboral_to
 name: aboral to

```

## Agent Attempts (4)

| # | Model | Runtime | F1 | P | R | Eval PR | Detail |
|---|-------|---------|-----|-----|-----|---------|--------|
| 1 | claude-opus-4.7 | claude | 0.947 | 1.000 | 0.900 | [#376](https://github.com/ai4curation/eval-ont-agent-uberon/pull/376) | [attempt](attempts/pr376.md) |
| 2 | claude-haiku-4.5 | claude | 0.842 | 0.889 | 0.800 | [#374](https://github.com/ai4curation/eval-ont-agent-uberon/pull/374) | [attempt](attempts/pr374.md) |
| 3 | claude-haiku-4.5 | claude | 0.842 | 0.889 | 0.800 | [#334](https://github.com/ai4curation/eval-ont-agent-uberon/pull/334) | [attempt](attempts/pr334.md) |
| 4 | claude-sonnet-4.5 | claude | 0.842 | 0.889 | 0.800 | [#314](https://github.com/ai4curation/eval-ont-agent-uberon/pull/314) | [attempt](attempts/pr314.md) |
