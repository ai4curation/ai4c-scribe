---
ontology: cell-ontology
repo: obophenotype/cell-ontology
issue_number: 3454
pr_number: 3555
issue_title: '[Class hierarchy] Remove CD44-high and CD122-high from CD45RO-positive
  memory T cells'
pr_author: copilot-swe-agent
pr_merged_at: '2026-02-16'
task_type: axiom_repair
difficulty: medium
scoping: tightly_scoped
scope: single_term
review_outcome: approved_first_time
num_agent_attempts: 11
generated_at: '2026-05-15'
domain_area: immunology
best_f1: 0.75
best_model: gpt-5.5
---

# PR #3555 — [Class hierarchy] Remove CD44-high and CD122-high from CD45RO-positive memory T cells

**cell-ontology** | [obophenotype/cell-ontology](https://github.com/obophenotype/cell-ontology) | [Issue #3454](https://github.com/obophenotype/cell-ontology/issues/3454) | [PR #3555](https://github.com/obophenotype/cell-ontology/pull/3555) | @copilot-swe-agent | merged 2026-02-16

`axiom_repair` `medium` `tightly_scoped` `approved_first_time`

## Context

CD44-high and CD122-high markers were included in the definition of CD45RO-positive memory T cells, but these markers are mouse-specific and not defining characteristics of human memory T cells. CD44 is broadly expressed across human T cell subsets (not specific to memory), and CD122-high expression is specific to mouse memory T cells. Since CD45RO is a human-specific marker, the term definition should not include mouse-specific marker assertions.

## Changes Made

Removed CD44-high and CD122-high marker assertions from the CD45RO-positive memory T cell definition in `cl-edit.owl`, with 4 lines added and 4 removed. The equal line counts reflect removing incorrect marker axioms and updating the definition text accordingly.

## Resolution

Approved on first review. Medium difficulty because correctly identifying which markers are species-specific requires understanding of comparative immunology between mouse and human T cell biology. An agent would need to recognize that combining mouse markers (CD44-high, CD122-high) with a human marker (CD45RO) is biologically inconsistent.

## Human Diff

```diff
diff --git a/src/ontology/cl-edit.owl b/src/ontology/cl-edit.owl
index f08e6e234..48518dd27 100644
--- a/src/ontology/cl-edit.owl
+++ b/src/ontology/cl-edit.owl
@@ -13901,23 +13901,23 @@ SubClassOf(obo:CL_0001202 obo:CL_0000980)
 
 # Class: obo:CL_0001203 (CD8-positive, alpha-beta memory T cell, CD45RO-positive)
 
-AnnotationAssertion(Annotation(oboInOwl:hasDbXref "GOC:tfm") Annotation(oboInOwl:hasDbXref "GO_REF:0000031") Annotation(oboInOwl:hasDbXref "PMID:20146720") obo:IAO_0000115 obo:CL_0001203 "A CD8-positive, alpha-beta T cell with memory phenotype indicated by being CD45RO and CD127-positive. This cell type is also described as being CD25-negative, CD44-high, and CD122-high.")
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "GOC:tfm") Annotation(oboInOwl:hasDbXref "GO_REF:0000031") Annotation(oboInOwl:hasDbXref "PMID:20146720") Annotation(oboInOwl:hasDbXref "PMID:24258910") Annotation(oboInOwl:hasDbXref "PMID:21926977") obo:IAO_0000115 obo:CL_0001203 "A CD8-positive, alpha-beta T cell with memory phenotype indicated by being CD45RO and CD127-positive. This cell type is also described as being CD25-negative.")
 AnnotationAssertion(oboInOwl:hasExactSynonym obo:CL_0001203 "CD8-positive, alpha-beta memory T lymphocyte, CD45RO-positive")
 AnnotationAssertion(oboInOwl:hasExactSynonym obo:CL_0001203 "CD8-positive, alpha-beta memory T-cell, CD45RO-positive")
 AnnotationAssertion(oboInOwl:hasExactSynonym obo:CL_0001203 "CD8-positive, alpha-beta memory T-lymphocyte, CD45RO-positive")
 AnnotationAssertion(rdfs:label obo:CL_0001203 "CD8-positive, alpha-beta memory T cell, CD45RO-positive")
-EquivalentClasses(obo:CL_0001203 ObjectIntersectionOf(obo:CL_0000909 ObjectSomeValuesFrom(obo:CL_4030046 obo:PR_000001380) ObjectSomeValuesFrom(obo:RO_0002104 obo:PR_000001017) ObjectSomeValuesFrom(obo:RO_0002104 obo:PR_000001869) ObjectSomeValuesFrom(obo:RO_0002162 obo:NCBITaxon_9606) ObjectSomeValuesFrom(obo:RO_0002353 obo:GO_0043379) ObjectSomeValuesFrom(obo:RO_0015015 obo:PR_000001307) ObjectSomeValuesFrom(obo:RO_0015015 obo:PR_000001381)))
+EquivalentClasses(obo:CL_0001203 ObjectIntersectionOf(obo:CL_0000909 ObjectSomeValuesFrom(obo:CL_4030046 obo:PR_000001380) ObjectSomeValuesFrom(obo:RO_0002104 obo:PR_000001017) ObjectSomeValuesFrom(obo:RO_0002104 obo:PR_000001869) ObjectSomeValuesFrom(obo:RO_0002162 obo:NCBITaxon_9606) ObjectSomeValuesFrom(obo:RO_0002353 obo:GO_0043379)))
 SubClassOf(Annotation(oboInOwl:is_inferred "true") obo:CL_0001203 obo:CL_0000909)
 SubClassOf(obo:CL_0001203 ObjectSomeValuesFrom(obo:RO_0002202 obo:CL_0000906))
 
 # Class: obo:CL_0001204 (CD4-positive, alpha-beta memory T cell, CD45RO-positive)
 
-AnnotationAssertion(Annotation(oboInOwl:hasDbXref "GOC:add") Annotation(oboInOwl:hasDbXref "GOC:tfm") Annotation(oboInOwl:hasDbXref "GO_REF:0000031") Annotation(oboInOwl:hasDbXref "ISBN:0781735149") Annotation(oboInOwl:hasDbXref "http://www.immgen.org/index_content.html") obo:IAO_0000115 obo:CL_0001204 "CD4-positive, alpha-beta long-lived T cell with the phenotype CD45RO-positive and CD127-positive. This cell type is also described as being CD25-negative, CD44-high, and CD122-high.")
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "GOC:add") Annotation(oboInOwl:hasDbXref "GOC:tfm") Annotation(oboInOwl:hasDbXref "GO_REF:0000031") Annotation(oboInOwl:hasDbXref "ISBN:0781735149") Annotation(oboInOwl:hasDbXref "http://www.immgen.org/index_content.html") Annotation(oboInOwl:hasDbXref "PMID:24258910") Annotation(oboInOwl:hasDbXref "PMID:21926977") obo:IAO_0000115 obo:CL_0001204 "CD4-positive, alpha-beta long-lived T cell with the phenotype CD45RO-positive and CD127-positive. This cell type is also described as being CD25-negative.")
 AnnotationAssertion(oboInOwl:hasExactSynonym obo:CL_0001204 "CD4-positive, alpha-beta memory T lymphocyte, CD45RO-positive")
 AnnotationAssertion(oboInOwl:hasExactSynonym obo:CL_0001204 "CD4-positive, alpha-beta memory T-cell, CD45RO-positive")
 AnnotationAssertion(oboInOwl:hasExactSynonym obo:CL_0001204 "CD4-positive, alpha-beta memory T-lymphocyte, CD45RO-positive")
 AnnotationAssertion(rdfs:label obo:CL_0001204 "CD4-positive, alpha-beta memory T cell, CD45RO-positive")
-EquivalentClasses(obo:CL_0001204 ObjectIntersectionOf(obo:CL_0000897 ObjectSomeValuesFrom(obo:CL_4030046 obo:PR_000001380) ObjectSomeValuesFrom(obo:RO_0002104 obo:PR_000001017) ObjectSomeValuesFrom(obo:RO_0002104 obo:PR_000001869) ObjectSomeValuesFrom(obo:RO_0002162 obo:NCBITaxon_9606) ObjectSomeValuesFrom(obo:RO_0002353 obo:GO_0043379) ObjectSomeValuesFrom(obo:RO_0015015 obo:PR_000001307) ObjectSomeValuesFrom(obo:RO_0015015 obo:PR_000001381)))
+EquivalentClasses(obo:CL_0001204 ObjectIntersectionOf(obo:CL_0000897 ObjectSomeValuesFrom(obo:CL_4030046 obo:PR_000001380) ObjectSomeValuesFrom(obo:RO_0002104 obo:PR_000001017) ObjectSomeValuesFrom(obo:RO_0002104 obo:PR_000001869) ObjectSomeValuesFrom(obo:RO_0002162 obo:NCBITaxon_9606) ObjectSomeValuesFrom(obo:RO_0002353 obo:GO_0043379)))
 SubClassOf(Annotation(oboInOwl:is_inferred "true") obo:CL_0001204 obo:CL_0000897)
 SubClassOf(obo:CL_0001204 ObjectSomeValuesFrom(obo:RO_0002202 obo:CL_0000896))
 

```

## Agent Attempts (11)

| # | Model | Runtime | F1 | P | R | Eval PR | Detail |
|---|-------|---------|-----|-----|-----|---------|--------|
| 1 | gpt-5.5 | opencode | 0.750 | 0.750 | 0.750 | [#17](https://github.com/ai4curation/eval-ont-agent-cl/pull/17) | [attempt](attempts/pr17.md) |
| 2 | claude-sonnet-4.5 | claude | 0.750 | 0.750 | 0.750 | [#15](https://github.com/ai4curation/eval-ont-agent-cl/pull/15) | [attempt](attempts/pr15.md) |
| 3 | claude-haiku-4.5 | claude | 0.750 | 0.750 | 0.750 | [#7](https://github.com/ai4curation/eval-ont-agent-cl/pull/7) | [attempt](attempts/pr7.md) |
| 4 | claude-opus-4.7 | claude | 0.667 | 0.750 | 0.600 | [#187](https://github.com/ai4curation/eval-ont-agent-cl/pull/187) | [attempt](attempts/pr187.md) |
| 5 | gpt-5.5 | opencode | 0.667 | 0.750 | 0.600 | [#70](https://github.com/ai4curation/eval-ont-agent-cl/pull/70) | [attempt](attempts/pr70.md) |
| 6 | gpt-5.5 | opencode | 0.667 | 0.750 | 0.600 | [#50](https://github.com/ai4curation/eval-ont-agent-cl/pull/50) | [attempt](attempts/pr50.md) |
| 7 | gpt-5.5 | codex | 0.667 | 0.750 | 0.600 | [#33](https://github.com/ai4curation/eval-ont-agent-cl/pull/33) | [attempt](attempts/pr33.md) |
| 8 | gpt-5.5 | codex | 0.667 | 0.750 | 0.600 | [#19](https://github.com/ai4curation/eval-ont-agent-cl/pull/19) | [attempt](attempts/pr19.md) |
| 9 | gpt-5.4 | codex | 0.667 | 0.750 | 0.600 | [#4](https://github.com/ai4curation/eval-ont-agent-cl/pull/4) | [attempt](attempts/pr4.md) |
| 10 | gpt-5.5 | opencode | 0.600 | 0.750 | 0.500 | [#18](https://github.com/ai4curation/eval-ont-agent-cl/pull/18) | [attempt](attempts/pr18.md) |
| 11 | gpt-5.5 | codex | 0.600 | 0.750 | 0.500 | [#16](https://github.com/ai4curation/eval-ont-agent-cl/pull/16) | [attempt](attempts/pr16.md) |
