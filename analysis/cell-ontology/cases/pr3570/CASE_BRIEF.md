---
ontology: cell-ontology
repo: obophenotype/cell-ontology
issue_number: 3500
pr_number: 3570
issue_title: Add taxon constraints to DN2a and DN2b thymocytes
pr_author: app/copilot-swe-agent
pr_merged_at: '2026-02-20'
task_type: other
difficulty: simple
scoping: tightly_scoped
scope: multi_term
review_outcome: approved_first_time
num_agent_attempts: 4
generated_at: '2026-05-15'
domain_area: immunology
best_f1: 1.0
best_model: claude-sonnet-4.5
---

# PR #3570 — Add taxon constraints to DN2a and DN2b thymocytes

**cell-ontology** | [obophenotype/cell-ontology](https://github.com/obophenotype/cell-ontology) | [Issue #3500](https://github.com/obophenotype/cell-ontology/issues/3500) | [PR #3570](https://github.com/obophenotype/cell-ontology/pull/3570) | @app/copilot-swe-agent | merged 2026-02-20

`other` `simple` `tightly_scoped` `approved_first_time`

## Context

The DN2a (CL_0002423) and DN2b (CL_0002424) thymocyte subtypes are defined based on mouse thymic development staging that does not directly translate to human T cell development. Issue #3500 requested adding taxon constraints to restrict these terms to Mus musculus, preventing their misuse in annotating human datasets where the DN2a/DN2b distinction is not applicable.

## Changes Made

Added 2 new lines to `cl-edit.owl`, one for each term, adding an `in_taxon some NCBITaxon:10090` (Mus musculus) constraint to CL_0002423 (DN2a thymocyte) and CL_0002424 (DN2b thymocyte). This is the standard CL pattern for species-restricted cell types.

## Resolution

Approved on first review in 4 commits. Simple difficulty because adding taxon constraints follows a well-established pattern in CL, and the biological rationale for restricting these terms to mouse is straightforward -- the DN2a/DN2b distinction is based on mouse-specific developmental staging.

## Human Diff

```diff
diff --git a/src/ontology/cl-edit.owl b/src/ontology/cl-edit.owl
index f91b7513c..12d47e7c3 100644
--- a/src/ontology/cl-edit.owl
+++ b/src/ontology/cl-edit.owl
@@ -18580,6 +18580,7 @@ AnnotationAssertion(rdfs:comment obo:CL_0002423 "Observed in mice. There is grow
 AnnotationAssertion(rdfs:label obo:CL_0002423 "DN2a thymocyte")
 EquivalentClasses(obo:CL_0002423 ObjectIntersectionOf(obo:CL_0000806 ObjectSomeValuesFrom(obo:RO_0015015 obo:PR_000002065)))
 SubClassOf(Annotation(oboInOwl:is_inferred "true") obo:CL_0002423 obo:CL_0000806)
+SubClassOf(obo:CL_0002423 ObjectSomeValuesFrom(obo:RO_0002162 obo:NCBITaxon_10090))
 
 # Class: obo:CL_0002424 (DN2b thymocyte)
 
@@ -18591,6 +18592,7 @@ AnnotationAssertion(rdfs:label obo:CL_0002424 "DN2b thymocyte")
 EquivalentClasses(obo:CL_0002424 ObjectIntersectionOf(obo:CL_0000806 ObjectSomeValuesFrom(obo:RO_0015016 obo:PR_000002065)))
 SubClassOf(Annotation(oboInOwl:is_inferred "true") obo:CL_0002424 obo:CL_0000806)
 SubClassOf(obo:CL_0002424 ObjectSomeValuesFrom(obo:RO_0002202 obo:CL_0002423))
+SubClassOf(obo:CL_0002424 ObjectSomeValuesFrom(obo:RO_0002162 obo:NCBITaxon_10090))
 
 # Class: obo:CL_0002425 (early T lineage precursor)
 

```

## Agent Attempts (4)

| # | Model | Runtime | F1 | P | R | Eval PR | Detail |
|---|-------|---------|-----|-----|-----|---------|--------|
| 1 | claude-sonnet-4.5 | copilot | 1.000 | 1.000 | 1.000 | [#235](https://github.com/ai4curation/eval-ont-agent-cl/pull/235) | [attempt](attempts/pr235.md) |
| 2 | claude-haiku-4.5 | claude | 1.000 | 1.000 | 1.000 | [#139](https://github.com/ai4curation/eval-ont-agent-cl/pull/139) | [attempt](attempts/pr139.md) |
| 3 | claude-sonnet-4.5 | claude | 0.667 | 1.000 | 0.500 | [#199](https://github.com/ai4curation/eval-ont-agent-cl/pull/199) | [attempt](attempts/pr199.md) |
| 4 | claude-opus-4.7 | claude | 0.000 | 0.000 | 0.000 | [#190](https://github.com/ai4curation/eval-ont-agent-cl/pull/190) | [attempt](attempts/pr190.md) |
