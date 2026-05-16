---
ontology: cell-ontology
repo: obophenotype/cell-ontology
issue_number: 3379
pr_number: 3444
issue_title: '[Class hierarchy] CD4+ CD11b+ dendritic cell [CL_0000999]: Change parent
  to CD11b+ DC'
pr_author: copilot-swe-agent
pr_merged_at: '2025-11-18'
task_type: reclassification
difficulty: simple
scoping: tightly_scoped
scope: single_term
review_outcome: approved_first_time
num_agent_attempts: 6
generated_at: '2026-05-15'
domain_area: immunology
best_f1: 0.8
best_model: claude-opus-4.7
---

# PR #3444 — [Class hierarchy] CD4+ CD11b+ dendritic cell [CL_0000999]: Change parent to CD11b+ DC

**cell-ontology** | [obophenotype/cell-ontology](https://github.com/obophenotype/cell-ontology) | [Issue #3379](https://github.com/obophenotype/cell-ontology/issues/3379) | [PR #3444](https://github.com/obophenotype/cell-ontology/pull/3444) | @copilot-swe-agent | merged 2025-11-18

`reclassification` `simple` `tightly_scoped` `approved_first_time`

## Context

CD4-positive CD11b-positive dendritic cell (CL:0000999) had its EquivalentClasses axiom using conventional dendritic cell (CL:0000990) as the genus class. Since this cell type is specifically a CD11b-positive subset, the more appropriate genus is CD11b-positive dendritic cell (CL:0002465), which is itself a subclass of conventional DC.

## Changes Made

Changed a single line in the EquivalentClasses axiom in `cl-edit.owl`: replaced the genus class from CL:0000990 (conventional dendritic cell) to CL:0002465 (CD11b-positive dendritic cell). This makes the logical definition more precise without changing the inferred classification.

## Resolution

Approved on first review. Simple difficulty because it is a single axiom change, but the 9 commits suggest the agent explored multiple approaches before settling on the correct fix. This case demonstrates how equivalence axiom genus classes should be as specific as possible in OWL ontologies.

## Human Diff

```diff
diff --git a/src/ontology/cl-edit.owl b/src/ontology/cl-edit.owl
index e5ccfa31d..f04c89078 100644
--- a/src/ontology/cl-edit.owl
+++ b/src/ontology/cl-edit.owl
@@ -13018,7 +13018,7 @@ AnnotationAssertion(Annotation(oboInOwl:hasDbXref "GOC:amm") Annotation(oboInOwl
 AnnotationAssertion(oboInOwl:hasExactSynonym obo:CL_0000999 "DC.4+")
 AnnotationAssertion(rdfs:comment obo:CL_0000999 "Defined as having a disposition to secreting anti-inflammatory cytokines. These markers are associated with mouse cells. Originally described in the dendritic cell ontology (DC_CL:0000012)(PMID:19243617).")
 AnnotationAssertion(rdfs:label obo:CL_0000999 "CD4-positive CD11b-positive dendritic cell")
-EquivalentClasses(obo:CL_0000999 ObjectIntersectionOf(obo:CL_0000990 ObjectSomeValuesFrom(obo:CL_4030046 obo:PR_000001026) ObjectSomeValuesFrom(obo:CL_4030046 obo:PR_000001084) ObjectSomeValuesFrom(obo:RO_0002104 obo:PR_000001004) ObjectSomeValuesFrom(obo:RO_0002215 obo:GO_0001816) ObjectSomeValuesFrom(obo:RO_0002215 obo:GO_0050728)))
+EquivalentClasses(obo:CL_0000999 ObjectIntersectionOf(obo:CL_0002465 ObjectSomeValuesFrom(obo:CL_4030046 obo:PR_000001026) ObjectSomeValuesFrom(obo:CL_4030046 obo:PR_000001084) ObjectSomeValuesFrom(obo:RO_0002104 obo:PR_000001004) ObjectSomeValuesFrom(obo:RO_0002215 obo:GO_0001816) ObjectSomeValuesFrom(obo:RO_0002215 obo:GO_0050728)))
 SubClassOf(obo:CL_0000999 obo:CL_0002465)
 SubClassOf(obo:CL_0000999 ObjectSomeValuesFrom(obo:RO_0002202 obo:CL_0002010))
 

```

## Agent Attempts (6)

| # | Model | Runtime | F1 | P | R | Eval PR | Detail |
|---|-------|---------|-----|-----|-----|---------|--------|
| 1 | claude-opus-4.7 | claude | 0.800 | 1.000 | 0.667 | [#276](https://github.com/ai4curation/eval-ont-agent-cl/pull/276) | [attempt](attempts/pr276.md) |
| 2 | gpt-5.5 | opencode | 0.800 | 1.000 | 0.667 | [#64](https://github.com/ai4curation/eval-ont-agent-cl/pull/64) | [attempt](attempts/pr64.md) |
| 3 | gpt-5.5 | opencode | 0.800 | 1.000 | 0.667 | [#44](https://github.com/ai4curation/eval-ont-agent-cl/pull/44) | [attempt](attempts/pr44.md) |
| 4 | claude-sonnet-4.5 | claude | 0.667 | 1.000 | 0.500 | [#218](https://github.com/ai4curation/eval-ont-agent-cl/pull/218) | [attempt](attempts/pr218.md) |
| 5 | gpt-5.5 | codex | 0.667 | 1.000 | 0.500 | [#24](https://github.com/ai4curation/eval-ont-agent-cl/pull/24) | [attempt](attempts/pr24.md) |
| 6 | claude-haiku-4.5 | claude | 0.500 | 0.500 | 0.500 | [#95](https://github.com/ai4curation/eval-ont-agent-cl/pull/95) | [attempt](attempts/pr95.md) |
