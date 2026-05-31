---
ontology: cell-ontology
repo: obophenotype/cell-ontology
issue_number: 3453
pr_number: 3556
issue_title: '[NTR] CD4-positive exhausted alpha-beta T cell / CD8-positive exhausted
  alpha-beta T cell'
pr_author: app/copilot-swe-agent
pr_merged_at: '2026-02-16'
task_type: new_term
difficulty: medium
scoping: tightly_scoped
scope: multi_term
review_outcome: approved_first_time
num_agent_attempts: 8
generated_at: '2026-05-17'
domain_area: immunology
best_f1: 0.75
best_model: claude-opus-4.7
---

# PR #3556 — [NTR] CD4-positive exhausted alpha-beta T cell / CD8-positive exhausted alpha-beta T cell

**cell-ontology** | [obophenotype/cell-ontology](https://github.com/obophenotype/cell-ontology) | [Issue #3453](https://github.com/obophenotype/cell-ontology/issues/3453) | [PR #3556](https://github.com/obophenotype/cell-ontology/pull/3556) | @app/copilot-swe-agent | merged 2026-02-16

`new_term` `medium` `tightly_scoped` `approved_first_time`

## Context

T cell exhaustion is a state of progressive dysfunction that occurs during chronic viral infection and in the tumor microenvironment. Issue #3453 requested new terms for CD4-positive and CD8-positive exhausted alpha-beta T cells, which are characterized by high expression of inhibitory receptors (PD-1, LAG-3, TIM-3) and diminished effector function. These terms are important for annotating tumor-infiltrating lymphocyte populations in cancer immunology datasets.

## Changes Made

Added 34 new lines to `cl-edit.owl` defining CD4-positive exhausted alpha-beta T cell and CD8-positive exhausted alpha-beta T cell. Each term includes class declaration, label, textual definition describing the exhaustion phenotype, parentage under the appropriate CD4+ or CD8+ alpha-beta T cell parent, and logical axioms capturing the expression of inhibitory checkpoint receptors and the relationship to the exhaustion biological process via GO terms.

## Resolution

Approved on first review in 5 commits. Medium difficulty because the exhaustion state is defined by a combination of phenotypic markers and functional properties, and the ontological representation must capture both the surface marker profile (PD-1, LAG-3, TIM-3) and the diminished functional capacity without conflating exhaustion with other hyporesponsive states like anergy.

## Human Diff

```diff
diff --git a/src/ontology/cl-edit.owl b/src/ontology/cl-edit.owl
index f08e6e234..740d2b469 100644
--- a/src/ontology/cl-edit.owl
+++ b/src/ontology/cl-edit.owl
@@ -3294,6 +3294,8 @@ Declaration(Class(obo:CL_7770003))
 Declaration(Class(obo:CL_7770004))
 Declaration(Class(obo:CL_7770005))
 Declaration(Class(obo:CL_7770006))
+Declaration(Class(obo:CL_9900000))
+Declaration(Class(obo:CL_9900001))
 Declaration(Class(obo:CP_0000000))
 Declaration(Class(obo:CP_0000025))
 Declaration(Class(obo:CP_0000027))
@@ -35543,6 +35545,38 @@ SubClassOf(obo:CL_7770006 obo:CL_0002367)
 SubClassOf(obo:CL_7770006 ObjectSomeValuesFrom(obo:RO_0002162 obo:NCBITaxon_9606))
 SubClassOf(obo:CL_7770006 ObjectSomeValuesFrom(obo:RO_0002292 obo:PR_Q9UIK5))
 
+# Class: obo:CL_9900000 (CD4-positive exhausted alpha-beta T cell)
+
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:31207603") Annotation(oboInOwl:hasDbXref "PMID:31390978") Annotation(oboInOwl:hasDbXref "PMID:36907685") Annotation(oboInOwl:hasDbXref "PMID:38166256") obo:IAO_0000115 obo:CL_9900000 "A CD4-positive alpha-beta T cell that displays impaired function and altered differentiation as a result of chronic antigenic stimulation (e.g., chronic infection, tumors, or persistent inflammation). This state is characterised by sustained expression of PD-1 as a shared feature. Additional exhaustion-associated molecules, including the transcription factor TOX, and context- or stage-dependent changes in markers such as LAG-3, TIM-3, CD39, and T-bet, may also be observed; however, the expression levels of these molecules vary depending on exhaustion stage and tissue environment.")
+AnnotationAssertion(obo:IAO_0000233 obo:CL_9900000 <https://github.com/obophenotype/cell-ontology/issues/3453>)
+AnnotationAssertion(terms:contributor obo:CL_9900000 <https://orcid.org/0000-0001-5742-4697>)
+AnnotationAssertion(terms:contributor obo:CL_9900000 <https://orcid.org/0009-0000-8480-9277>)
+AnnotationAssertion(terms:creator obo:CL_9900000 "GitHub Copilot")
+AnnotationAssertion(terms:date obo:CL_9900000 "2026-01-13T15:30:05Z"^^xsd:dateTime)
+AnnotationAssertion(oboInOwl:hasExactSynonym obo:CL_9900000 "CD4+ exhausted T lymphocyte")
+AnnotationAssertion(oboInOwl:hasExactSynonym obo:CL_9900000 "exhausted CD4 T cell")
+AnnotationAssertion(oboInOwl:hasExactSynonym obo:CL_9900000 "exhausted CD4-positive T cell")
+AnnotationAssertion(rdfs:label obo:CL_9900000 "CD4-positive exhausted alpha-beta T cell")
+EquivalentClasses(obo:CL_9900000 ObjectIntersectionOf(obo:CL_0000624 ObjectSomeValuesFrom(obo:RO_0002104 obo:PR_000001919)))
+SubClassOf(Annotation(oboInOwl:is_inferred "true") obo:CL_9900000 obo:CL_0000624)
+SubClassOf(obo:CL_9900000 obo:CL_0011025)
+
+# Class: obo:CL_9900001 (CD8-positive exhausted alpha-beta T cell)
+
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:31207603") Annotation(oboInOwl:hasDbXref "PMID:36907685") Annotation(oboInOwl:hasDbXref "PMID:38166256") obo:IAO_0000115 obo:CL_9900001 "A CD8-positive alpha-beta T cell that displays impaired function and altered differentiation as a result of chronic antigenic stimulation (e.g., chronic infection, tumours, or persistent inflammation). This state is characterised by sustained expression of PD-1 as a shared feature. Additional exhaustion-associated molecules, including expression of the transcription factor TOX and reduced T-bet, and context- or stage-dependent changes in markers such as LAG-3, TIM-3, CD39, and EOMES, may also be observed; however, the expression levels of these molecules vary depending on exhaustion stage and disease context.")
+AnnotationAssertion(obo:IAO_0000233 obo:CL_9900001 <https://github.com/obophenotype/cell-ontology/issues/3453>)
+AnnotationAssertion(terms:contributor obo:CL_9900001 <https://orcid.org/0000-0001-5742-4697>)
+AnnotationAssertion(terms:contributor obo:CL_9900001 <https://orcid.org/0009-0000-8480-9277>)
+AnnotationAssertion(terms:creator obo:CL_9900001 "GitHub Copilot")
+AnnotationAssertion(terms:date obo:CL_9900001 "2026-01-13T15:30:05Z"^^xsd:dateTime)
+AnnotationAssertion(oboInOwl:hasExactSynonym obo:CL_9900001 "CD8+ exhausted T lymphocyte")
+AnnotationAssertion(oboInOwl:hasExactSynonym obo:CL_9900001 "exhausted CD8 T cell")
+AnnotationAssertion(oboInOwl:hasExactSynonym obo:CL_9900001 "exhausted CD8-positive T cell")
+AnnotationAssertion(rdfs:label obo:CL_9900001 "CD8-positive exhausted alpha-beta T cell")
+EquivalentClasses(obo:CL_9900001 ObjectIntersectionOf(obo:CL_0000625 ObjectSomeValuesFrom(obo:RO_0002104 obo:PR_000001919)))
+SubClassOf(Annotation(oboInOwl:is_inferred "true") obo:CL_9900001 obo:CL_0000625)
+SubClassOf(obo:CL_9900001 obo:CL_0011025)
+
 # Class: obo:CP_0000000 (obsolete CP:0000000)
 
 AnnotationAssertion(obo:IAO_0100001 obo:CP_0000000 obo:CL_0017500)

```

## Agent Attempts (8)

| # | Model | Runtime | F1 | P | R | Blob | Eval PR | Detail |
|---|-------|---------|-----|-----|-----|------|---------|--------|
| 1 | claude-opus-4.7 | claude | 0.750 | 0.750 | 0.750 | `8d8a7f0` | [#189](https://github.com/ai4curation/eval-ont-agent-cl/pull/189) | [attempt](attempts/pr189.md) |
| 2 | claude-sonnet-4.5 | claude | 0.696 | 0.667 | 0.727 | `5eda277` | [#226](https://github.com/ai4curation/eval-ont-agent-cl/pull/226) | [attempt](attempts/pr226.md) |
| 3 | claude-haiku-4.5 | claude | 0.130 | 0.125 | 0.136 | `c55910f` | [#156](https://github.com/ai4curation/eval-ont-agent-cl/pull/156) | [attempt](attempts/pr156.md) |
| 4 | gpt-5.4 | opencode | 0.125 | 0.125 | 0.125 | `b4b7a88` | [#588](https://github.com/ai4curation/eval-ont-agent-cl/pull/588) | [attempt](attempts/pr588.md) |
| 5 | gpt-5.4 | opencode | 0.125 | 0.125 | 0.125 | `b4b7a88` | [#526](https://github.com/ai4curation/eval-ont-agent-cl/pull/526) | [attempt](attempts/pr526.md) |
| 6 | gpt-5.4 | codex | 0.125 | 0.125 | 0.125 | `02ec74a` | [#301](https://github.com/ai4curation/eval-ont-agent-cl/pull/301) | [attempt](attempts/pr301.md) |
| 7 | gpt-5.5 | opencode | 0.120 | 0.125 | 0.115 | `252ee7f` | [#550](https://github.com/ai4curation/eval-ont-agent-cl/pull/550) | [attempt](attempts/pr550.md) |
| 8 | gpt-5.5 | opencode | 0.120 | 0.125 | 0.115 | `252ee7f` | [#489](https://github.com/ai4curation/eval-ont-agent-cl/pull/489) | [attempt](attempts/pr489.md) |
