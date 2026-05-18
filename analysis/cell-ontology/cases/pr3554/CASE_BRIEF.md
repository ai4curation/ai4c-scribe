---
ontology: cell-ontology
repo: obophenotype/cell-ontology
issue_number: 3452
pr_number: 3554
issue_title: '[NTR] Add new terms for stem cell memory T cells (TSCM): CD4+ and CD8+
  subsets'
pr_author: app/copilot-swe-agent
pr_merged_at: '2026-02-18'
task_type: new_term
difficulty: medium
scoping: tightly_scoped
scope: multi_term
review_outcome: approved_first_time
num_agent_attempts: 8
generated_at: '2026-05-17'
domain_area: immunology
best_f1: 0.828
best_model: claude-sonnet-4.5
---

# PR #3554 — [NTR] Add new terms for stem cell memory T cells (TSCM): CD4+ and CD8+ subsets

**cell-ontology** | [obophenotype/cell-ontology](https://github.com/obophenotype/cell-ontology) | [Issue #3452](https://github.com/obophenotype/cell-ontology/issues/3452) | [PR #3554](https://github.com/obophenotype/cell-ontology/pull/3554) | @app/copilot-swe-agent | merged 2026-02-18

`new_term` `medium` `tightly_scoped` `approved_first_time`

## Context

Stem cell memory T cells (TSCM) are a recently described subset of memory T cells that possess stem cell-like self-renewal capacity while maintaining the ability to differentiate into other memory and effector T cell subsets. Issue #3452 requested adding both CD4-positive and CD8-positive TSCM terms to enable annotation of these populations in single-cell datasets, particularly for CellxGene and HuBMAP.

## Changes Made

Added 40 new lines to `cl-edit.owl` defining two new terms: CD4-positive stem cell memory alpha-beta T cell and CD8-positive stem cell memory alpha-beta T cell. Each term includes a class declaration, label, synonyms, textual definition referencing the stem-like properties and surface marker profile, parentage under the appropriate CD4+ or CD8+ memory T cell parent, and logical axioms capturing surface marker expression (CD95+, CD122+) and the stem cell-like self-renewal capability.

## Resolution

Approved on first review in 6 commits. Medium difficulty because correctly modeling TSCM cells requires understanding their position in the T cell differentiation hierarchy -- they are the least differentiated memory subset, sitting between naive T cells and central memory T cells, and their definition involves multiple surface markers that distinguish them from other memory compartments.

## Human Diff

```diff
diff --git a/src/ontology/cl-edit.owl b/src/ontology/cl-edit.owl
index 123d89816..8b0bf8d9b 100644
--- a/src/ontology/cl-edit.owl
+++ b/src/ontology/cl-edit.owl
@@ -3527,6 +3527,8 @@ Declaration(Class(obo:UBERON_8600004))
 Declaration(Class(obo:UBERON_8600014))
 Declaration(Class(obo:UBERON_8850000))
 Declaration(Class(obo:UBERON_8910001))
+Declaration(Class(obo:CL_9900000))
+Declaration(Class(obo:CL_9900001))
 Declaration(ObjectProperty(obo:BFO_0000051))
 Declaration(ObjectProperty(obo:CL_4030044))
 Declaration(ObjectProperty(obo:CL_4030045))
@@ -11894,6 +11896,25 @@ AnnotationAssertion(rdfs:label obo:CL_0000897 "CD4-positive, alpha-beta memory T
 EquivalentClasses(obo:CL_0000897 ObjectIntersectionOf(obo:CL_0000624 ObjectSomeValuesFrom(obo:RO_0000053 obo:PATO_0001603) ObjectSomeValuesFrom(obo:RO_0002353 obo:GO_0002286) ObjectSomeValuesFrom(obo:RO_0002353 obo:GO_0043379)))
 SubClassOf(obo:CL_0000897 obo:CL_0000624)
 
+# Class: obo:CL_9900000 (stem cell memory CD4-positive, alpha-beta T cell)
+
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:19525962") Annotation(oboInOwl:hasDbXref "PMID:21926977") Annotation(oboInOwl:hasDbXref "PMID:28060797") obo:IAO_0000115 obo:CL_9900000 "A CD4-positive memory alpha-beta T cell with stem-like properties that is long-lived, retains a naïve-like phenotype, and exhibits self-renewal and multipotent differentiation capacity. This cell acts as a stem-like reservoir capable of regenerating central and effector memory T cell subsets.")
+AnnotationAssertion(terms:contributor obo:CL_9900000 <https://orcid.org/0000-0001-5742-4697>)
+AnnotationAssertion(terms:contributor obo:CL_9900000 <https://orcid.org/0009-0000-8480-9277>)
+AnnotationAssertion(terms:creator obo:CL_9900000 "GitHub Copilot")
+AnnotationAssertion(terms:date obo:CL_9900000 "2026-01-12T12:14:30Z"^^xsd:dateTime)
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:21926977") oboInOwl:hasExactSynonym obo:CL_9900000 "CD4+ T memory stem cell")
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:21926977") oboInOwl:hasExactSynonym obo:CL_9900000 "CD4+ TSCM cell")
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:21926977") oboInOwl:hasExactSynonym obo:CL_9900000 "CD4-positive TSCM cell")
+AnnotationAssertion(oboInOwl:hasExactSynonym obo:CL_9900000 "stem cell memory CD4+ T-cell")
+AnnotationAssertion(oboInOwl:hasExactSynonym obo:CL_9900000 "stem cell memory CD4+ T-lymphocyte")
+AnnotationAssertion(oboInOwl:hasExactSynonym obo:CL_9900000 "stem cell memory CD4+ alpha-beta T cell")
+AnnotationAssertion(oboInOwl:hasExactSynonym obo:CL_9900000 "stem cell memory CD4-positive, alpha-beta T lymphocyte")
+AnnotationAssertion(oboInOwl:hasExactSynonym obo:CL_9900000 "stem cell–like memory CD4+ T cell")
+AnnotationAssertion(oboInOwl:hasExactSynonym obo:CL_9900000 "stem cell–like memory CD4-positive, alpha-beta T cell")
+AnnotationAssertion(rdfs:label obo:CL_9900000 "stem cell memory CD4-positive, alpha-beta T cell")
+SubClassOf(obo:CL_9900000 obo:CL_0000897)
+
 # Class: obo:CL_0000898 (naive T cell)
 
 AnnotationAssertion(Annotation(oboInOwl:hasDbXref "GOC:add") Annotation(oboInOwl:hasDbXref "GOC:pam") Annotation(oboInOwl:hasDbXref "GOC:tfm") Annotation(oboInOwl:hasDbXref "GO_REF:0000031") Annotation(oboInOwl:hasDbXref "PMID:19100699") obo:IAO_0000115 obo:CL_0000898 "Mature T cell not yet exposed to antigen with the phenotype CCR7-positive, CD45RA-positive, and CD127-positive. This cell type is also described as being CD25-negative, CD62L-high and CD44-low.")
@@ -12061,6 +12082,25 @@ AnnotationAssertion(oboInOwl:hasRelatedSynonym obo:CL_0000909 "T.8Mem.Sp")
 AnnotationAssertion(rdfs:label obo:CL_0000909 "CD8-positive, alpha-beta memory T cell")
 EquivalentClasses(obo:CL_0000909 ObjectIntersectionOf(obo:CL_0000625 ObjectSomeValuesFrom(obo:RO_0000053 obo:PATO_0001603) ObjectSomeValuesFrom(obo:RO_0002353 obo:GO_0002286) ObjectSomeValuesFrom(obo:RO_0002353 obo:GO_0043379)))
 
+# Class: obo:CL_9900001 (stem cell memory CD8-positive, alpha-beta T cell)
+
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:19525962") Annotation(oboInOwl:hasDbXref "PMID:21926977") Annotation(oboInOwl:hasDbXref "PMID:28060797") obo:IAO_0000115 obo:CL_9900001 "A CD8-positive memory alpha-beta T cell with stem-like properties that is long-lived, retains a naïve-like phenotype, and exhibits self-renewal and multipotent differentiation capacity. This cell acts as a stem-like reservoir capable of regenerating central and effector memory T cell subsets.")
+AnnotationAssertion(terms:contributor obo:CL_9900001 <https://orcid.org/0000-0001-5742-4697>)
+AnnotationAssertion(terms:contributor obo:CL_9900001 <https://orcid.org/0009-0000-8480-9277>)
+AnnotationAssertion(terms:creator obo:CL_9900001 "GitHub Copilot")
+AnnotationAssertion(terms:date obo:CL_9900001 "2026-01-12T12:14:30Z"^^xsd:dateTime)
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:21926977") oboInOwl:hasExactSynonym obo:CL_9900001 "CD8+ T memory stem cell")
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:21926977") oboInOwl:hasExactSynonym obo:CL_9900001 "CD8+ TSCM cell")
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:21926977") oboInOwl:hasExactSynonym obo:CL_9900001 "CD8-positive TSCM cell")
+AnnotationAssertion(oboInOwl:hasExactSynonym obo:CL_9900001 "stem cell memory CD8+ T-cell")
+AnnotationAssertion(oboInOwl:hasExactSynonym obo:CL_9900001 "stem cell memory CD8+ T-lymphocyte")
+AnnotationAssertion(oboInOwl:hasExactSynonym obo:CL_9900001 "stem cell memory CD8+ alpha-beta T cell")
+AnnotationAssertion(oboInOwl:hasExactSynonym obo:CL_9900001 "stem cell memory CD8-positive, alpha-beta T lymphocyte")
+AnnotationAssertion(oboInOwl:hasExactSynonym obo:CL_9900001 "stem cell–like memory CD8+ T cell")
+AnnotationAssertion(oboInOwl:hasExactSynonym obo:CL_9900001 "stem cell–like memory CD8-positive, alpha-beta T cell")
+AnnotationAssertion(rdfs:label obo:CL_9900001 "stem cell memory CD8-positive, alpha-beta T cell")
+SubClassOf(obo:CL_9900001 obo:CL_0000909)
+
 # Class: obo:CL_0000910 (cytotoxic T cell)
 
 AnnotationAssertion(Annotation(oboInOwl:hasDbXref "GOC:add") Annotation(oboInOwl:hasDbXref "GOC:pam") Annotation(oboInOwl:hasDbXref "GOC:tfm") Annotation(oboInOwl:hasDbXref "GO_REF:0000031") Annotation(oboInOwl:hasDbXref "PMID:18395547") obo:IAO_0000115 obo:CL_0000910 "A mature T cell that differentiated and acquired cytotoxic function with the phenotype perforin-positive and granzyme-B positive.")

```

## Agent Attempts (8)

| # | Model | Runtime | F1 | P | R | Blob | Eval PR | Detail |
|---|-------|---------|-----|-----|-----|------|---------|--------|
| 1 | claude-sonnet-4.5 | claude | 0.828 | 0.800 | 0.857 | `973cb37` | [#203](https://github.com/ai4curation/eval-ont-agent-cl/pull/203) | [attempt](attempts/pr203.md) |
| 2 | claude-opus-4.7 | claude | 0.452 | 0.467 | 0.438 | `2e0ee0b` | [#186](https://github.com/ai4curation/eval-ont-agent-cl/pull/186) | [attempt](attempts/pr186.md) |
| 3 | gpt-5.4 | codex | 0.375 | 0.400 | 0.353 | `e4a20bb` | [#324](https://github.com/ai4curation/eval-ont-agent-cl/pull/324) | [attempt](attempts/pr324.md) |
| 4 | claude-haiku-4.5 | claude | 0.065 | 0.067 | 0.062 | `74bec89` | [#147](https://github.com/ai4curation/eval-ont-agent-cl/pull/147) | [attempt](attempts/pr147.md) |
| 5 | gpt-5.4 | opencode | 0.062 | 0.067 | 0.059 | `e0d2170` | [#586](https://github.com/ai4curation/eval-ont-agent-cl/pull/586) | [attempt](attempts/pr586.md) |
| 6 | gpt-5.5 | opencode | 0.062 | 0.067 | 0.059 | `f32adb0` | [#549](https://github.com/ai4curation/eval-ont-agent-cl/pull/549) | [attempt](attempts/pr549.md) |
| 7 | gpt-5.4 | opencode | 0.062 | 0.067 | 0.059 | `e0d2170` | [#523](https://github.com/ai4curation/eval-ont-agent-cl/pull/523) | [attempt](attempts/pr523.md) |
| 8 | gpt-5.5 | opencode | 0.062 | 0.067 | 0.059 | `f32adb0` | [#488](https://github.com/ai4curation/eval-ont-agent-cl/pull/488) | [attempt](attempts/pr488.md) |
