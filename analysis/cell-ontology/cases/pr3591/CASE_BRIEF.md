---
ontology: cell-ontology
repo: obophenotype/cell-ontology
issue_number: 3590
pr_number: 3591
issue_title: add subset tag 'add_by_HRA'
pr_author: nicolevasilevsky
pr_merged_at: '2026-03-20'
task_type: other
difficulty: simple
scoping: tightly_scoped
scope: single_term
review_outcome: changes_requested
num_agent_attempts: 10
generated_at: '2026-05-17'
domain_area: metadata
best_f1: 0.667
best_model: claude-sonnet-4.5
---

# PR #3591 — add subset tag 'add_by_HRA'

**cell-ontology** | [obophenotype/cell-ontology](https://github.com/obophenotype/cell-ontology) | [Issue #3590](https://github.com/obophenotype/cell-ontology/issues/3590) | [PR #3591](https://github.com/obophenotype/cell-ontology/pull/3591) | @nicolevasilevsky | merged 2026-03-20

`other` `simple` `tightly_scoped` `changes_requested`

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

## Human Diff

```diff
diff --git a/src/ontology/cl-edit.owl b/src/ontology/cl-edit.owl
index 054fb3842..0837f612e 100644
--- a/src/ontology/cl-edit.owl
+++ b/src/ontology/cl-edit.owl
@@ -3589,6 +3589,7 @@ Declaration(AnnotationProperty(obo:IAO_0000700))
 Declaration(AnnotationProperty(obo:IAO_0100001))
 Declaration(AnnotationProperty(obo:RO_0002161))
 Declaration(AnnotationProperty(cl:BDS_subset))
+Declaration(AnnotationProperty(cl:added_by_HRA))
 Declaration(AnnotationProperty(cl:added_for_HCA))
 Declaration(AnnotationProperty(cl:blood_and_immune_upper_slim))
 Declaration(AnnotationProperty(cl:eye_upper_slim))
@@ -3639,6 +3640,11 @@ AnnotationAssertion(rdfs:label obo:IAO_0000028 "symbol")
 
 SubAnnotationPropertyOf(cl:BDS_subset oboInOwl:SubsetProperty)
 
+# Annotation Property: cl:added_by_HRA (cl:added_by_HRA)
+
+AnnotationAssertion(rdfs:comment cl:added_by_HRA "Classes tagged with this subset property were added on request from HuBMAP to support the HuBMAP Human Reference Atlas (HRA).")
+SubAnnotationPropertyOf(cl:added_by_HRA oboInOwl:SubsetProperty)
+
 # Annotation Property: cl:added_for_HCA (cl:added_for_HCA)
 
 SubAnnotationPropertyOf(cl:added_for_HCA oboInOwl:SubsetProperty)

```

## Agent Attempts (10)

| # | Model | Runtime | F1 | P | R | Blob | Eval PR | Detail |
|---|-------|---------|-----|-----|-----|------|---------|--------|
| 1 | claude-sonnet-4.5 | copilot | 0.667 | 0.750 | 0.600 | `c85b53a` | [#250](https://github.com/ai4curation/eval-ont-agent-cl/pull/250) | [attempt](attempts/pr250.md) |
| 2 | claude-sonnet-4.5 | claude | 0.667 | 0.750 | 0.600 | `7b19931` | [#201](https://github.com/ai4curation/eval-ont-agent-cl/pull/201) | [attempt](attempts/pr201.md) |
| 3 | gpt-5.4 | opencode | 0.000 | 0.000 | 0.000 | `d74021b` | [#596](https://github.com/ai4curation/eval-ont-agent-cl/pull/596) | [attempt](attempts/pr596.md) |
| 4 | gpt-5.5 | opencode | 0.000 | 0.000 | 0.000 | `64f048b` | [#558](https://github.com/ai4curation/eval-ont-agent-cl/pull/558) | [attempt](attempts/pr558.md) |
| 5 | gpt-5.4 | opencode | 0.000 | 0.000 | 0.000 | `d74021b` | [#535](https://github.com/ai4curation/eval-ont-agent-cl/pull/535) | [attempt](attempts/pr535.md) |
| 6 | gpt-5.5 | opencode | 0.000 | 0.000 | 0.000 | `64f048b` | [#498](https://github.com/ai4curation/eval-ont-agent-cl/pull/498) | [attempt](attempts/pr498.md) |
| 7 | gpt-5.4 | codex | 0.000 | 0.000 | 0.000 | `cf4864e` | [#286](https://github.com/ai4curation/eval-ont-agent-cl/pull/286) | [attempt](attempts/pr286.md) |
| 8 | claude-opus-4.7 | claude | 0.000 | 0.000 | 0.000 | `1ee945f` | [#274](https://github.com/ai4curation/eval-ont-agent-cl/pull/274) | [attempt](attempts/pr274.md) |
| 9 | claude-haiku-4.5 | claude | 0.000 | 0.000 | 0.000 | `e440578` | [#146](https://github.com/ai4curation/eval-ont-agent-cl/pull/146) | [attempt](attempts/pr146.md) |
| 10 | gemma-4-31b | opencode | 0.000 | 0.000 | 0.000 | `1469b07` | [#125](https://github.com/ai4curation/eval-ont-agent-cl/pull/125) | [attempt](attempts/pr125.md) |
