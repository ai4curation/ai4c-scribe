---
ontology: cell-ontology
repo: obophenotype/cell-ontology
issue_number: 3536
pr_number: 3537
issue_title: Fix design patterns for columnar cuboidal and squamous epithelial cells
pr_author: app/copilot-swe-agent
pr_merged_at: '2026-02-12'
task_type: axiom_repair
difficulty: hard
scoping: loosely_scoped
scope: multi_term
review_outcome: approved_first_time
num_agent_attempts: 8
generated_at: '2026-05-17'
domain_area: epithelial
best_f1: 0.613
best_model: gpt-5.4
---

# PR #3537 — Fix design patterns for columnar cuboidal and squamous epithelial cells

**cell-ontology** | [obophenotype/cell-ontology](https://github.com/obophenotype/cell-ontology) | [Issue #3536](https://github.com/obophenotype/cell-ontology/issues/3536) | [PR #3537](https://github.com/obophenotype/cell-ontology/pull/3537) | @app/copilot-swe-agent | merged 2026-02-12

`axiom_repair` `hard` `loosely_scoped` `approved_first_time`

## Context

The logical definitions for squamous and cuboidal epithelial cell types had inconsistent or missing design patterns. Issue #3536 identified that these cell types lacked formal Dead Simple OWL Design Patterns (DOSDP) and that existing axioms did not follow a consistent compositional structure. This affected the ability to systematically generate and validate epithelial cell subtypes using standard tooling.

## Changes Made

Added new DOSDP pattern YAML files for both cuboidal and squamous epithelial cells under `src/patterns/dosdp-patterns/`, created corresponding documentation under `docs/patterns/`, updated the relations guide, and revised 31 lines in `cl-edit.owl` to align existing epithelial cell term axioms with the new patterns. The edit file changes refactored logical definitions for multiple epithelial cell types to use consistent has_quality/part_of compositional patterns.

## Resolution

Approved on first review in 10 commits. Hard difficulty because this required designing DOSDP patterns from scratch, understanding PATO quality terms for cell morphology (squamous, cuboidal), ensuring the patterns correctly compose with anatomical location, and updating multiple existing terms to conform to the new patterns while maintaining backward compatibility.

## Curation Note (data quality)

flagged_by: claude-opus-4.7 — flagged_at: 2026-05-16

This case is **`case_quality: poor`**. The gold PR #3537 should not be used as a
line-level metadiff reference; judge attempts against the issue's four explicit asks.

1. **Gold PR is internally inconsistent (gold error).** The issue asks for
   `cuboidal epithelial cell ≡ epithelial cell and has_characteristic some cuboidal`.
   PATO has no class literally labelled "cuboidal"; the correct term is
   **`PATO:0001872`** ("cuboid", with exact synonyms "cuboidal" and "block-like").
   The gold's OWL axioms correctly use `PATO:0001872` (for `CL_9900001`, `CL_0000634`,
   `CL_0002223`, `CL_0002662`, `CL_4033084`). However, the gold's **documentation and
   pattern files use `PATO:0002312`**, which is actually labelled **"segmented"**
   ("Consisting of segments… arranged in a longitudinal series") — a clear error in
   `docs/patterns/cuboidalEpithelialCell.md`, `docs/relations_guide.md`, and
   `src/patterns/dosdp-patterns/cuboidalEpithelialCell.yaml`. Agents that used
   `PATO:0001872` consistently everywhere (pr188 opus, pr151 haiku) are *more*
   internally consistent than the gold but are penalized by metadiff.

2. **Gold contains out-of-scope structural edits.** Beyond the issue's asks, the gold
   reparents `CL_0000237` (keratinizing barrier epithelial cell) from `CL_0000240` to
   `CL_0000066` and adds `part_of UBERON_0000486`; adds `EquivalentClasses` to
   `CL_0000079` (stratified epithelial cell) and rewrites the `CL_0000240` equivalence
   with `part_of UBERON_0000486`; and merges/reorders `CL_0002063` axioms. None of
   this is requested by issue #3536. Well-scoped agents that omit these are penalized
   on recall.

3. **Effect on scoring.** All three attempts scored F1 0.26–0.32. For pr188 (opus) and
   pr151 (haiku) the metadiff **substantially under-represents quality** — both met all
   four explicit asks with correct, reasoner-safe axioms. pr222 (sonnet) is a genuine
   partial: it correctly did the squamous half but abandoned the entire cuboidal half
   on the false premise that PATO has no cuboidal term, so its low score is only
   *partly* a case-quality artifact.

## Human Diff

```diff
diff --git a/docs/patterns/cuboidalEpithelialCell.md b/docs/patterns/cuboidalEpithelialCell.md
new file mode 100644
index 000000000..6ddbf32ad
--- /dev/null
+++ b/docs/patterns/cuboidalEpithelialCell.md
@@ -0,0 +1,29 @@
+# cuboidalEpithelialCell 
+
+[http://purl.obolibrary.org/obo/cl/cuboidalEpithelialCell](http://purl.obolibrary.org/obo/cl/cuboidalEpithelialCell)
+
+## Description 
+
+An epithelial cell type characterized by a cuboidal morphology.
+
+## Contributors 
+* [https://orcid.org/0000-0001-5208-3432](https://orcid.org/0000-0001-5208-3432) 
+* [https://orcid.org/0000-0002-6601-2165](https://orcid.org/0000-0002-6601-2165) 
+
+## Name 
+
+cuboidal {[cell](http://purl.obolibrary.org/obo/CL_0000000)}
+
+## Definition 
+
+A {[cell](http://purl.obolibrary.org/obo/CL_0000000)} that has a cuboidal morphology.
+
+## Equivalent to 
+
+{[cell](http://purl.obolibrary.org/obo/CL_0000000)} and ([bearer of](http://purl.obolibrary.org/obo/RO_0000053) some [cuboidal](http://purl.obolibrary.org/obo/PATO_0002312))
+
+## Data preview 
+| defined_class                             | defined_class_label   | cell                                      | cell_label           |
+|:------------------------------------------|:----------------------|:------------------------------------------|:---------------------|
+| [CL:9900001](http://purl.obolibrary.org/obo/CL_9900001) | cuboidal epithelial cell | [CL:0000066](http://purl.obolibrary.org/obo/CL_0000066) | epithelial cell |
+| [CL:4033084](http://purl.obolibrary.org/obo/CL_4033084) | cuboidal granulosa cell | [CL:0000501](http://purl.obolibrary.org/obo/CL_0000501) | granulosa cell |
diff --git a/docs/patterns/squamousEpithelialCell.md b/docs/patterns/squamousEpithelialCell.md
new file mode 100644
index 000000000..a31189d38
--- /dev/null
+++ b/docs/patterns/squamousEpithelialCell.md
@@ -0,0 +1,30 @@
+# squamousEpithelialCell 
+
+[http://purl.obolibrary.org/obo/cl/squamousEpithelialCell](http://purl.obolibrary.org/obo/cl/squamousEpithelialCell)
+
+## Description 
+
+An epithelial cell type characterized by a flattened (squamous) morphology.
+
+## Contributors 
+* [https://orcid.org/0000-0001-5208-3432](https://orcid.org/0000-0001-5208-3432) 
+* [https://orcid.org/0000-0002-6601-2165](https://orcid.org/0000-0002-6601-2165) 
+
+## Name 
+
+squamous {[cell](http://purl.obolibrary.org/obo/CL_0000000)}
+
+## Definition 
+
+A {[cell](http://purl.obolibrary.org/obo/CL_0000000)} that has a flattened morphology.
+
+## Equivalent to 
+
+{[cell](http://purl.obolibrary.org/obo/CL_0000000)} and ([bearer of](http://purl.obolibrary.org/obo/RO_0000053) some [flattened](http://purl.obolibrary.org/obo/PATO_0002254))
+
+## Data preview 
+| defined_class                             | defined_class_label   | cell                                      | cell_label           |
+|:------------------------------------------|:----------------------|:------------------------------------------|:---------------------|
+| [CL:0000076](http://purl.obolibrary.org/obo/CL_0000076) | squamous epithelial cell | [CL:0000066](http://purl.obolibrary.org/obo/CL_0000066) | epithelial cell |
+| [CL:0002653](http://purl.obolibrary.org/obo/CL_0002653) | squamous endothelial cell | [CL:0000115](http://purl.obolibrary.org/obo/CL_0000115) | endothelial cell |
+| [CL:0008040](http://purl.obolibrary.org/obo/CL_0008040) | squamous endothelial cell of venule | [CL:0002139](http://purl.obolibrary.org/obo/CL_0002139) | endothelial cell of venule |
diff --git a/docs/relations_guide.md b/docs/relations_guide.md
index 52cbb0f7b..a2ac0de9b 100644
--- a/docs/relations_guide.md
+++ b/docs/relations_guide.md
@@ -235,6 +235,19 @@ neuronal), e.g.
 
 ‘Betz cell’ subClassOf ‘has characteristic’ some ‘standard pyramidal morphology’
 
+
+### Recording cell shape
+
+Cell shape is an important characteristic for classifying certain cell types, particularly epithelial cells. Use the [**'has characteristic'**](http://purl.obolibrary.org/obo/RO_0000053) relation with appropriate PATO shape terms.
+
+For flattened (squamous) cells:
+
+['squamous epithelial cell'](http://purl.obolibrary.org/obo/CL_0000076) equivalentTo ['epithelial cell'](http://purl.obolibrary.org/obo/CL_0000066) and ([**'has characteristic'**](http://purl.obolibrary.org/obo/RO_0000053) *some* [flattened](http://purl.obolibrary.org/obo/PATO_0002254))
+
+For cuboidal cells:
+
+['cuboidal epithelial cell'](http://purl.obolibrary.org/obo/CL_9900001) equivalentTo ['epithelial cell'](http://purl.obolibrary.org/obo/CL_0000066) and ([**'has characteristic'**](http://purl.obolibrary.org/obo/RO_0000053) *some* [cuboidal](http://purl.obolibrary.org/obo/PATO_0002312))
+
 ### Recording nuclear number 
 
 To record the number of nuclei in a cell, use a PATO subclass
diff --git a/src/ontology/cl-edit.owl b/src/ontology/cl-edit.owl
index 876a6ef11..e80ee36b7 100644
--- a/src/ontology/cl-edit.owl
+++ b/src/ontology/cl-edit.owl
@@ -3293,6 +3293,7 @@ Declaration(Class(obo:CL_7770003))
 Declaration(Class(obo:CL_7770004))
 Declaration(Class(obo:CL_7770005))
 Declaration(Class(obo:CL_7770006))
+Declaration(Class(obo:CL_9900001))
 Declaration(Class(obo:CP_0000000))
 Declaration(Class(obo:CP_0000025))
 Declaration(Class(obo:CP_0000027))
@@ -3357,6 +3358,8 @@ Declaration(Class(obo:PATO_0001870))
 Declaration(Class(obo:PATO_0001872))
 Declaration(Class(obo:PATO_0001979))
 Declaration(Class(obo:PATO_0002064))
+Declaration(Class(obo:PATO_0002254))
+Declaration(Class(obo:PATO_0002312))
 Declaration(Class(obo:PATO_0010007))
 Declaration(Class(obo:PATO_0070002))
 Declaration(Class(obo:PATO_0070003))
@@ -4524,9 +4527,11 @@ SubClassOf(obo:CL_0000075 obo:CL_0000066)
 
 # Class: obo:CL_0000076 (squamous epithelial cell)
 
+AnnotationAssertion(obo:IAO_0000115 obo:CL_0000076 "An epithelial cell that has a flattened morphology.")
+AnnotationAssertion(terms:date obo:CL_0000076 "2025-12-16T15:56:39Z"^^xsd:dateTime)
 AnnotationAssertion(oboInOwl:hasDbXref obo:CL_0000076 "CALOHA:TS-1249")
 AnnotationAssertion(rdfs:label obo:CL_0000076 "squamous epithelial cell")
-SubClassOf(obo:CL_0000076 obo:CL_0000066)
+EquivalentClasses(obo:CL_0000076 ObjectIntersectionOf(obo:CL_0000066 ObjectSomeValuesFrom(obo:RO_0000053 obo:PATO_0002254)))
 
 # Class: obo:CL_0000077 (mesothelial cell)
 
@@ -4548,6 +4553,7 @@ EquivalentClasses(obo:CL_0000078 ObjectIntersectionOf(obo:CL_0000076 ObjectSomeV
 
 AnnotationAssertion(Annotation(oboInOwl:hasDbXref "Wikipedia:Epithelium") Annotation(oboInOwl:hasDbXref "doi:/10.1016/B978-0-12-410424-2.00003-2") Annotation(oboInOwl:hasDbXref "https://www.biologyonline.com/dictionary/stratified-epithelium") obo:IAO_0000115 obo:CL_0000079 "An epithelial cell, organized into multiple layers, with only the basal layer being in contact with the basement membrane.")
 AnnotationAssertion(rdfs:label obo:CL_0000079 "stratified epithelial cell")
+EquivalentClasses(obo:CL_0000079 ObjectIntersectionOf(obo:CL_0000066 ObjectSomeValuesFrom(obo:BFO_0000050 obo:UBERON_0000486)))
 SubClassOf(obo:CL_0000079 obo:CL_0000066)
 SubClassOf(obo:CL_0000079 ObjectSomeValuesFrom(obo:RO_0002202 obo:CL_0000357))
 
@@ -6071,8 +6077,9 @@ SubClassOf(obo:CL_0000236 ObjectSomeValuesFrom(obo:RO_0002202 obo:CL_0000826))
 # Class: obo:CL_0000237 (keratinizing barrier epithelial cell)
 
 AnnotationAssertion(rdfs:label obo:CL_0000237 "keratinizing barrier epithelial cell")
-SubClassOf(obo:CL_0000237 obo:CL_0000240)
+SubClassOf(obo:CL_0000237 obo:CL_0000066)
 SubClassOf(obo:CL_0000237 obo:CL_0000311)
+SubClassOf(obo:CL_0000237 ObjectSomeValuesFrom(obo:BFO_0000050 obo:UBERON_0000486))
 SubClassOf(obo:CL_0000237 ObjectSomeValuesFrom(obo:RO_0002202 obo:CL_0000114))
 
 # Class: obo:CL_0000238 (non keratinizing barrier epithelial cell)
@@ -6094,8 +6101,7 @@ SubClassOf(obo:CL_0000239 obo:CL_0000075)
 
 AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:30422572") Annotation(oboInOwl:hasDbXref "Wikipedia:Epithelium") Annotation(oboInOwl:hasDbXref "Wikipedia:Stratified_squamous_epithelium") obo:IAO_0000115 obo:CL_0000240 "A stratified epithelial cell that is part of squamous epithelium, characterized by multiple layers of cells. The basal layer is directly attached to the basement membrane and the apical layer consists of flattened squamous cells. This provides a protective barrier, commonly found in areas subject to abrasion, such as the skin, oral cavity, and esophagus.")
 AnnotationAssertion(rdfs:label obo:CL_0000240 "stratified squamous epithelial cell")
-EquivalentClasses(obo:CL_0000240 ObjectIntersectionOf(obo:CL_0000079 ObjectSomeValuesFrom(obo:BFO_0000050 obo:UBERON_0006915)))
-SubClassOf(obo:CL_0000240 obo:CL_0000076)
+EquivalentClasses(obo:CL_0000240 ObjectIntersectionOf(obo:CL_0000079 ObjectSomeValuesFrom(obo:BFO_0000050 obo:UBERON_0000486) ObjectSomeValuesFrom(obo:RO_0000053 obo:PATO_0002254)))
 
 # Class: obo:CL_0000241 (stratified cuboidal epithelial cell)
 
@@ -9277,6 +9283,7 @@ AnnotationAssertion(oboInOwl:hasExactSynonym obo:CL_0000634 "cell of Claudius")
 AnnotationAssertion(oboInOwl:hasRelatedSynonym obo:CL_0000634 "external supporting cell of Claudius")
 AnnotationAssertion(rdfs:label obo:CL_0000634 "Claudius cell")
 SubClassOf(obo:CL_0000634 obo:CL_0002315)
+SubClassOf(obo:CL_0000634 ObjectSomeValuesFrom(obo:RO_0000053 obo:PATO_0001872))
 
 # Class: obo:CL_0000635 (Deiter's cell)
 
@@ -14644,7 +14651,7 @@ AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:29463737") Annotation(ob
 AnnotationAssertion(Annotation(oboInOwl:hasSynonymType obo:OMO_0003000) oboInOwl:hasRelatedSynonym obo:CL_0002062 "ATI")
 AnnotationAssertion(rdfs:label obo:CL_0002062 "pulmonary alveolar type 1 cell")
 EquivalentClasses(obo:CL_0002062 ObjectIntersectionOf(obo:CL_0000322 ObjectSomeValuesFrom(obo:RO_0002215 obo:GO_0007585)))
-SubClassOf(obo:CL_0002062 obo:CL_0000076)
+SubClassOf(obo:CL_0002062 ObjectSomeValuesFrom(obo:RO_0000053 obo:PATO_0002254))
 
 # Class: obo:CL_0002063 (pulmonary alveolar type 2 cell)
 
@@ -14669,9 +14676,7 @@ AnnotationAssertion(Annotation(oboInOwl:hasSynonymType obo:OMO_0003000) oboInOwl
 AnnotationAssertion(oboInOwl:hasRelatedSynonym obo:CL_0002063 "TII")
 AnnotationAssertion(oboInOwl:hasRelatedSynonym obo:CL_0002063 "lung type II cell")
 AnnotationAssertion(rdfs:label obo:CL_0002063 "pulmonary alveolar type 2 cell")
-EquivalentClasses(obo:CL_0002063 ObjectIntersectionOf(obo:CL_0000322 ObjectSomeValuesFrom(obo:RO_0002215 obo:GO_0032940) ObjectSomeValuesFrom(obo:RO_0002215 obo:GO_0043129)))
-SubClassOf(obo:CL_0002063 ObjectSomeValuesFrom(obo:BFO_0000051 obo:GO_0097208))
-SubClassOf(obo:CL_0002063 ObjectSomeValuesFrom(obo:RO_0000053 obo:PATO_0001872))
+EquivalentClasses(obo:CL_0002063 ObjectIntersectionOf(obo:CL_0000322 ObjectSomeValuesFrom(obo:BFO_0000051 obo:GO_0097208) ObjectSomeValuesFrom(obo:RO_0000053 obo:PATO_0001872) ObjectSomeValuesFrom(obo:RO_0002215 obo:GO_0043129)))
 SubClassOf(obo:CL_0002063 ObjectSomeValuesFrom(obo:RO_0002202 obo:CL_4040003))
 
 # Class: obo:CL_0002064 (pancreatic acinar cell)
@@ -16052,6 +16057,7 @@ AnnotationAssertion(oboInOwl:hasDbXref obo:CL_0002190 "FMA:86925")
 AnnotationAssertion(rdfs:label obo:CL_0002190 "squamous cell of epidermis")
 SubClassOf(obo:CL_0002190 obo:CL_0000312)
 SubClassOf(obo:CL_0002190 ObjectSomeValuesFrom(obo:BFO_0000050 obo:UBERON_0001003))
+SubClassOf(obo:CL_0002190 ObjectSomeValuesFrom(obo:RO_0000053 obo:PATO_0002254))
 
 # Class: obo:CL_0002191 (granulocytopoietic cell)
 
@@ -16394,6 +16400,7 @@ AnnotationAssertion(rdfs:label obo:CL_0002221 "keratinized squamous cell of esop
 SubClassOf(obo:CL_0002221 obo:CL_0000237)
 SubClassOf(obo:CL_0002221 obo:CL_0002252)
 SubClassOf(obo:CL_0002221 ObjectSomeValuesFrom(obo:BFO_0000050 obo:UBERON_0001976))
+SubClassOf(obo:CL_0002221 ObjectSomeValuesFrom(obo:RO_0000053 obo:PATO_0002254))
 
... (150 more lines truncated)
```

## Agent Attempts (8)

| # | Model | Runtime | F1 | P | R | Blob | Eval PR | Detail |
|---|-------|---------|-----|-----|-----|------|---------|--------|
| 1 | gpt-5.4 | opencode | 0.613 | 0.663 | 0.570 | `6735706` | [#584](https://github.com/ai4curation/eval-ont-agent-cl/pull/584) | [attempt](attempts/pr584.md) |
| 2 | gpt-5.4 | opencode | 0.613 | 0.663 | 0.570 | `6735706` | [#521](https://github.com/ai4curation/eval-ont-agent-cl/pull/521) | [attempt](attempts/pr521.md) |
| 3 | gpt-5.4 | codex | 0.344 | 0.265 | 0.491 | `f932cec` | [#591](https://github.com/ai4curation/eval-ont-agent-cl/pull/591) | [attempt](attempts/pr591.md) |
| 4 | claude-opus-4.7 | claude | 0.320 | 0.286 | 0.364 | `4f63cf7` | [#188](https://github.com/ai4curation/eval-ont-agent-cl/pull/188) | [attempt](attempts/pr188.md) |
| 5 | claude-haiku-4.5 | claude | 0.292 | 0.255 | 0.342 | `7381859` | [#151](https://github.com/ai4curation/eval-ont-agent-cl/pull/151) | [attempt](attempts/pr151.md) |
| 6 | claude-sonnet-4.5 | claude | 0.260 | 0.194 | 0.396 | `ef01ecf` | [#222](https://github.com/ai4curation/eval-ont-agent-cl/pull/222) | [attempt](attempts/pr222.md) |
| 7 | gpt-5.5 | opencode | 0.083 | 0.061 | 0.128 | `0e0d3a6` | [#548](https://github.com/ai4curation/eval-ont-agent-cl/pull/548) | [attempt](attempts/pr548.md) |
| 8 | gpt-5.5 | opencode | 0.083 | 0.061 | 0.128 | `0e0d3a6` | [#485](https://github.com/ai4curation/eval-ont-agent-cl/pull/485) | [attempt](attempts/pr485.md) |
