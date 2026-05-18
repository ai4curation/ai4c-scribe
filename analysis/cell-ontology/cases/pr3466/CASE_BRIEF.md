---
ontology: cell-ontology
repo: obophenotype/cell-ontology
issue_number: 3457
pr_number: 3467
issue_title: Add fibrochondrocyte (CL_4072104) term
pr_author: copilot-swe-agent
pr_merged_at: '2025-11-27'
task_type: new_term
difficulty: medium
scoping: mostly_scoped
scope: single_term
review_outcome: approved_first_time
num_agent_attempts: 9
generated_at: '2026-05-17'
scoping_notes: Primary change is the new fibrochondrocyte term in cl-edit.owl, but
  component files were also regenerated as part of the build process.
domain_area: musculoskeletal
best_f1: 0.093
best_model: gpt-5.5
---

# PR #3467 — Add fibrochondrocyte (CL_4072104) term

**cell-ontology** | [obophenotype/cell-ontology](https://github.com/obophenotype/cell-ontology) | [Issue #3457](https://github.com/obophenotype/cell-ontology/issues/3457) | [PR #3467](https://github.com/obophenotype/cell-ontology/pull/3467) | @copilot-swe-agent | merged 2025-11-27

`new_term` `medium` `mostly_scoped` `approved_first_time`

## Context

A new term request was filed for fibrochondrocyte, a hybrid cell type found in fibrocartilaginous tissues (meniscus, intervertebral disc, TMJ disc) that exhibits characteristics of both chondrocytes and fibroblasts. This cell type produces both type I and type II collagen, distinguishing it from typical hyaline cartilage chondrocytes.

## Changes Made

Added the fibrochondrocyte term (CL:4072104) to `cl-edit.owl` with proper parentage under both chondrocyte and fibroblast lineages, a textual definition citing relevant literature, and synonyms. The term uses a permanent CL ID rather than a temporary one, indicating it was minted through the standard ID allocation process.

## Resolution

Approved on first review. Medium difficulty because properly modeling a hybrid cell type requires understanding dual-lineage classification, choosing appropriate parent classes, and writing a definition that captures the distinguishing features (collagen type production, anatomical location in fibrocartilage).

## Curation Note (data quality)

`case_quality: poor` — flagged 2026-05-16 by claude-opus-4.7 after reviewing all
7 attempts. **The metadiff scores are not usable as a quality signal for this
case** for two independent structural reasons:

1. **Placeholder-vs-canonical CL ID artifact.** The gold PR (#3467) uses the
   permanent ID `CL_4072104` assigned by the release reserialization pipeline.
   The agent config CLAUDE.md explicitly instructs agents to mint temporary IDs
   in the `CL_99xxxxx` range (idrange:81). Agents that *correctly followed this
   instruction* (sonnet #208, opus #180 → `CL_9900000`; haiku #99, codex #83/#36
   → `CL_9900001`) line-mismatch every axiom against gold and score **F1=0.000
   by construction**, despite producing substantively equivalent terms. The only
   non-zero attempts (#73, #54 = 0.093) are the two opencode runs that *violated*
   the instruction by scraping `CL_4072104` from OLS, so their declaration/header
   lines coincidentally line-matched gold. The metric thus rewards the
   instruction violation and zeros out the correct behavior.

2. **Build-regenerated-file domination.** Gold's 373-line diff is mostly
   ODK-regenerated artifacts: `merged_import.owl`, `bgo-cl-comp.owl`,
   `cellxgene_subset.owl`, `clm-cl.owl`, `wmbo-cl-comp.owl`, `pr_terms.txt`,
   release version IRIs, and downstream COL3A1 (`PR_000003328`) / COL6A1
   (`PR_000003353`) PR-class declarations. An edit-only agent that does not run
   the release pipeline cannot reproduce these, structurally capping recall.

Substantive assessment (judge against the issue, not metadiff): all 7 attempts
correctly added `fibrochondrocyte` under chondrocyte (`CL_0000138`) with
`part_of fibrocartilage` (`UBERON_0001995`), three correctly typed PMID-backed
synonyms, and contributor ORCID. Best: **opus #180** (clean genus-differentia
equivalence + separate COL1A1 marker SubClassOf, verbatim definition, correct
temp-ID handling and reasoning). Solid: sonnet #208, codex #36 (ran `robot
reason`), opencode #73/#54. Weaker: haiku #99 (used plain `SubClassOf` instead
of the `cellPartOfAnatomicalEntity` DOSDP equivalence axiom — wrong pattern);
codex #83 (gutted the definition to one sentence and dropped PMID:31871141).
Common gap across all: only COL1A1 `expresses` asserted, whereas gold also
asserts COL3A1 and COL6A1 (the issue's explicit "expresses some" line named only
collagen alpha-1(I) chain, so this is a defensible literal reading).

Note: the case directory is named `pr3466` but the gold PR for issue #3457 is
**#3467** (correct in frontmatter). Source PR #3466 is an unrelated change
("Generalize chondrocyte definition and add skeletogenic cell parent") and is
**not** a companion PR — `companion_prs: []`. Step 3a (multi-PR partial gold)
does not apply; this is a single-PR resolution.

## Human Diff

```diff
diff --git a/src/ontology/cl-edit.owl b/src/ontology/cl-edit.owl
index ed68a9183..03c722ffd 100644
--- a/src/ontology/cl-edit.owl
+++ b/src/ontology/cl-edit.owl
@@ -3273,6 +3273,7 @@ Declaration(Class(obo:CL_4072045))
 Declaration(Class(obo:CL_4072046))
 Declaration(Class(obo:CL_4072102))
 Declaration(Class(obo:CL_4072103))
+Declaration(Class(obo:CL_4072104))
 Declaration(Class(obo:CL_7770002))
 Declaration(Class(obo:CL_7770003))
 Declaration(Class(obo:CL_7770004))
@@ -3358,6 +3359,8 @@ Declaration(Class(obo:PR_000001432))
 Declaration(Class(obo:PR_000002030))
 Declaration(Class(obo:PR_000002123))
 Declaration(Class(obo:PR_000003264))
+Declaration(Class(obo:PR_000003328))
+Declaration(Class(obo:PR_000003353))
 Declaration(Class(obo:PR_000003472))
 Declaration(Class(obo:PR_000003490))
 Declaration(Class(obo:PR_000003675))
@@ -35232,6 +35235,20 @@ AnnotationAssertion(rdfs:label obo:CL_4072103 "hair follicle dermal stem cell")
 EquivalentClasses(obo:CL_4072103 ObjectIntersectionOf(obo:CL_0000134 ObjectSomeValuesFrom(obo:BFO_0000050 obo:UBERON_0002073)))
 SubClassOf(obo:CL_4072103 ObjectSomeValuesFrom(obo:RO_0002215 obo:GO_0042634))
 
+# Class: obo:CL_4072104 (fibrochondrocyte)
+
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:28939894") Annotation(oboInOwl:hasDbXref "PMID:31871141") Annotation(oboInOwl:hasDbXref "PMID:34608249") obo:IAO_0000115 obo:CL_4072104 "A chondrocyte with hybrid fibroblastic-chondrogenic characteristics found in fibrocartilage, particularly in the avascular inner zone and transitional middle zone of the meniscus. In humans, fibrochondrocytes are marked by predominant expression of type I collagen (COL1A1) and fibril-associated collagens (COL3A1, COL6A1), while retaining type II collagen (COL2A1) expression and exhibiting lower SOX9 than hyaline chondrocytes. This molecular profile underlies the synthesis of abundant type I collagen essential for fibrocartilage matrix and reflects an intermediate phenotype between fibroblast and chondrocyte.")
+AnnotationAssertion(terms:contributor obo:CL_4072104 <https://orcid.org/0009-0000-8480-9277>)
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:34608249") oboInOwl:hasExactSynonym obo:CL_4072104 "fibrocartilage chondrocyte")
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:28939894") oboInOwl:hasNarrowSynonym obo:CL_4072104 "meniscus fibrochondrocyte")
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:31871141") Annotation(oboInOwl:hasSynonymType obo:OMO_0003000) oboInOwl:hasRelatedSynonym obo:CL_4072104 "FC")
+AnnotationAssertion(rdfs:label obo:CL_4072104 "fibrochondrocyte")
+EquivalentClasses(obo:CL_4072104 ObjectIntersectionOf(obo:CL_0000138 ObjectSomeValuesFrom(obo:BFO_0000050 obo:UBERON_0001995)))
+SubClassOf(obo:CL_4072104 obo:CL_0002320)
+SubClassOf(obo:CL_4072104 ObjectSomeValuesFrom(obo:RO_0002292 obo:PR_000003264))
+SubClassOf(obo:CL_4072104 ObjectSomeValuesFrom(obo:RO_0002292 obo:PR_000003328))
+SubClassOf(obo:CL_4072104 ObjectSomeValuesFrom(obo:RO_0002292 obo:PR_000003353))
+
 # Class: obo:CL_7770002 (juxtacanalicular tissue cell)
 
 AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:25356439") Annotation(oboInOwl:hasDbXref "PMID:32341164") Annotation(oboInOwl:hasDbXref "PMID:39829808") obo:IAO_0000115 obo:CL_7770002 "A trabecular meshwork cell of the juxtacanalicular tissue (JCT), characterized by a spindle-shaped, fibroblast-like morphology within a loose extracellular matrix immediately adjacent to Schlemm's canal. It expresses CHI3L1 (human and mouse) and ANGPTL7 (human), as well as smooth muscle actin for contractility. Unlike other trabecular meshwork cells, it does not form monolayers but exists in a loose network, regulating aqueous humor outflow resistance through continuous ECM remodelling, mechanotransduction, and formation of intracellular pores historically called giant vacuoles.")
diff --git a/src/ontology/components/bgo-cl-comp.owl b/src/ontology/components/bgo-cl-comp.owl
index b5e04af0f..682f0b42a 100644
--- a/src/ontology/components/bgo-cl-comp.owl
+++ b/src/ontology/components/bgo-cl-comp.owl
@@ -11,8 +11,8 @@
      xmlns:oboInOwl="http://www.geneontology.org/formats/oboInOwl#"
      xmlns:CCN20230722="https://purl.brain-bican.org/taxonomy/CCN20230722#">
     <owl:Ontology rdf:about="http://purl.obolibrary.org/obo/cl/components/bgo-cl-comp.owl">
-        <owl:versionIRI rdf:resource="http://purl.obolibrary.org/obo/cl/releases/2025-11-25/components/bgo-cl-comp.owl"/>
-        <owl:versionInfo>2025-11-25</owl:versionInfo>
+        <owl:versionIRI rdf:resource="http://purl.obolibrary.org/obo/cl/releases/2025-11-27/components/bgo-cl-comp.owl"/>
+        <owl:versionInfo>2025-11-27</owl:versionInfo>
     </owl:Ontology>
     
 
diff --git a/src/ontology/components/cellxgene_subset.owl b/src/ontology/components/cellxgene_subset.owl
index 2ceac23d8..1166f7dc3 100644
--- a/src/ontology/components/cellxgene_subset.owl
+++ b/src/ontology/components/cellxgene_subset.owl
@@ -7,8 +7,8 @@ Prefix(rdfs:=<http://www.w3.org/2000/01/rdf-schema#>)
 
 
 Ontology(<http://purl.obolibrary.org/obo/cl/components/cellxgene_subset.owl>
-<http://purl.obolibrary.org/obo/cl/releases/2025-11-25/components/cellxgene_subset.owl>
-Annotation(owl:versionInfo "2025-11-25")
+<http://purl.obolibrary.org/obo/cl/releases/2025-11-27/components/cellxgene_subset.owl>
+Annotation(owl:versionInfo "2025-11-27")
 
 Declaration(Class(<http://purl.obolibrary.org/obo/CL_0000000>))
 Declaration(Class(<http://purl.obolibrary.org/obo/CL_0000001>))
diff --git a/src/ontology/components/clm-cl.owl b/src/ontology/components/clm-cl.owl
index 29aa1e72e..e189c1a07 100644
--- a/src/ontology/components/clm-cl.owl
+++ b/src/ontology/components/clm-cl.owl
@@ -11,13 +11,13 @@
      xmlns:dcterms="http://purl.org/dc/terms/"
      xmlns:oboInOwl="http://www.geneontology.org/formats/oboInOwl#">
     <owl:Ontology rdf:about="http://purl.obolibrary.org/obo/cl/components/clm-cl.owl">
-        <owl:versionIRI rdf:resource="http://purl.obolibrary.org/obo/cl/releases/2025-11-25/components/clm-cl.owl"/>
+        <owl:versionIRI rdf:resource="http://purl.obolibrary.org/obo/cl/releases/2025-11-27/components/clm-cl.owl"/>
         <dce:type rdf:resource="http://purl.obolibrary.org/obo/IAO_8000001"/>
         <dcterms:description>None</dcterms:description>
         <dcterms:license rdf:resource="https://creativecommons.org/licenses/unspecified"/>
         <dcterms:title>Cell Markers Ontology</dcterms:title>
         <owl:versionInfo>2025-09-14</owl:versionInfo>
-        <owl:versionInfo>2025-11-25</owl:versionInfo>
+        <owl:versionInfo>2025-11-27</owl:versionInfo>
     </owl:Ontology>
     
 
diff --git a/src/ontology/components/wmbo-cl-comp.owl b/src/ontology/components/wmbo-cl-comp.owl
index 2d14ec48a..6f1419710 100644
--- a/src/ontology/components/wmbo-cl-comp.owl
+++ b/src/ontology/components/wmbo-cl-comp.owl
@@ -11,8 +11,8 @@
      xmlns:oboInOwl="http://www.geneontology.org/formats/oboInOwl#"
      xmlns:CCN20230722="https://purl.brain-bican.org/taxonomy/CCN20230722#">
     <owl:Ontology rdf:about="http://purl.obolibrary.org/obo/cl/components/wmbo-cl-comp.owl">
-        <owl:versionIRI rdf:resource="http://purl.obolibrary.org/obo/cl/releases/2025-11-25/components/wmbo-cl-comp.owl"/>
-        <owl:versionInfo>2025-11-25</owl:versionInfo>
+        <owl:versionIRI rdf:resource="http://purl.obolibrary.org/obo/cl/releases/2025-11-27/components/wmbo-cl-comp.owl"/>
+        <owl:versionInfo>2025-11-27</owl:versionInfo>
     </owl:Ontology>
     
 
diff --git a/src/ontology/imports/merged_import.owl b/src/ontology/imports/merged_import.owl
index 10eee8aa9..bff45ad63 100644
--- a/src/ontology/imports/merged_import.owl
+++ b/src/ontology/imports/merged_import.owl
@@ -7,8 +7,8 @@ Prefix(rdfs:=<http://www.w3.org/2000/01/rdf-schema#>)
 
 
 Ontology(<http://purl.obolibrary.org/obo/cl/imports/merged_import.owl>
-<http://purl.obolibrary.org/obo/cl/releases/2025-11-25/imports/merged_import.owl>
-Annotation(owl:versionInfo "2025-11-25")
+<http://purl.obolibrary.org/obo/cl/releases/2025-11-27/imports/merged_import.owl>
+Annotation(owl:versionInfo "2025-11-27")
 
 Declaration(Class(<http://purl.obolibrary.org/obo/BFO_0000002>))
 Declaration(Class(<http://purl.obolibrary.org/obo/BFO_0000003>))
@@ -9290,6 +9290,9 @@ Declaration(Class(<http://purl.obolibrary.org/obo/PR_000002981>))
 Declaration(Class(<http://purl.obolibrary.org/obo/PR_000003262>))
 Declaration(Class(<http://purl.obolibrary.org/obo/PR_000003263>))
 Declaration(Class(<http://purl.obolibrary.org/obo/PR_000003264>))
+Declaration(Class(<http://purl.obolibrary.org/obo/PR_000003328>))
+Declaration(Class(<http://purl.obolibrary.org/obo/PR_000003353>))
+Declaration(Class(<http://purl.obolibrary.org/obo/PR_000003386>))
 Declaration(Class(<http://purl.obolibrary.org/obo/PR_000003450>))
 Declaration(Class(<http://purl.obolibrary.org/obo/PR_000003455>))
 Declaration(Class(<http://purl.obolibrary.org/obo/PR_000003457>))
@@ -9429,6 +9432,7 @@ Declaration(Class(<http://purl.obolibrary.org/obo/PR_000018603>))
 Declaration(Class(<http://purl.obolibrary.org/obo/PR_000018606>))
 Declaration(Class(<http://purl.obolibrary.org/obo/PR_000018732>))
 Declaration(Class(<http://purl.obolibrary.org/obo/PR_000018798>))
+Declaration(Class(<http://purl.obolibrary.org/obo/PR_000018809>))
 Declaration(Class(<http://purl.obolibrary.org/obo/PR_000018820>))
 Declaration(Class(<http://purl.obolibrary.org/obo/PR_000018835>))
 Declaration(Class(<http://purl.obolibrary.org/obo/PR_000018883>))
@@ -9466,6 +9470,7 @@ Declaration(Class(<http://purl.obolibrary.org/obo/PR_000025406>))
 Declaration(Class(<http://purl.obolibrary.org/obo/PR_000025407>))
 Declaration(Class(<http://purl.obolibrary.org/obo/PR_000025408>))
 Declaration(Class(<http://purl.obolibrary.org/obo/PR_000025409>))
+Declaration(Class(<http://purl.obolibrary.org/obo/PR_000025420>))
 Declaration(Class(<http://purl.obolibrary.org/obo/PR_000025455>))
 Declaration(Class(<http://purl.obolibrary.org/obo/PR_000025466>))
 Declaration(Class(<http://purl.obolibrary.org/obo/PR_000025670>))
@@ -9574,6 +9579,7 @@ Declaration(Class(<http://purl.obolibrary.org/obo/PR_P01903>))
 Declaration(Class(<http://purl.obolibrary.org/obo/PR_P02008>))
 Declaration(Class(<http://purl.obolibrary.org/obo/PR_P02088>))
 Declaration(Class(<http://purl.obolibrary.org/obo/PR_P02452>))
+Declaration(Class(<http://purl.obolibrary.org/obo/PR_P02461>))
 Declaration(Class(<http://purl.obolibrary.org/obo/PR_P02724>))
 Declaration(Class(<http://purl.obolibrary.org/obo/PR_P02786>))
 Declaration(Class(<http://purl.obolibrary.org/obo/PR_P02788>))
@@ -9611,6 +9617,7 @@ Declaration(Class(<http://purl.obolibrary.org/obo/PR_P07766>))
 Declaration(Class(<http://purl.obolibrary.org/obo/PR_P07949>))
 Declaration(Class(<http://purl.obolibrary.org/obo/PR_P08071>))
 Declaration(Class(<http://purl.obolibrary.org/obo/PR_P08101>))
+Declaration(Class(<http://purl.obolibrary.org/obo/PR_P08121>))
 Declaration(Class(<http://purl.obolibrary.org/obo/PR_P08152>))
 Declaration(Class(<http://purl.obolibrary.org/obo/PR_P08473>))
 Declaration(Class(<http://purl.obolibrary.org/obo/PR_P08508>))
@@ -9659,6 +9666,7 @@ Declaration(Class(<http://purl.obolibrary.org/obo/PR_P11836>))
 Declaration(Class(<http://purl.obolibrary.org/obo/PR_P12018>))
 Declaration(Class(<http://purl.obolibrary.org/obo/PR_P12036>))
 Declaration(Class(<http://purl.obolibrary.org/obo/PR_P12107>))
+Declaration(Class(<http://purl.obolibrary.org/obo/PR_P12109>))
 Declaration(Class(<http://purl.obolibrary.org/obo/PR_P12272>))
 Declaration(Class(<http://purl.obolibrary.org/obo/PR_P12314>))
 Declaration(Class(<http://purl.obolibrary.org/obo/PR_P12319>))
@@ -9890,6 +9898,7 @@ Declaration(Class(<http://purl.obolibrary.org/obo/PR_Q03059>))
 Declaration(Class(<http://purl.obolibrary.org/obo/PR_Q03347>))
 Declaration(Class(<http://purl.obolibrary.org/obo/PR_Q03405>))
 Declaration(Class(<http://purl.obolibrary.org/obo/PR_Q04683>))
+Declaration(Class(<http://purl.obolibrary.org/obo/PR_Q04857>))
 Declaration(Class(<http://purl.obolibrary.org/obo/PR_Q05117>))
 Declaration(Class(<http://purl.obolibrary.org/obo/PR_Q06318>))
 Declaration(Class(<http://purl.obolibrary.org/obo/PR_Q07075>))
@@ -148998,6 +149007,35 @@ AnnotationAssertion(rdfs:comment <http://purl.obolibrary.org/obo/PR_000003264> "
 AnnotationAssertion(rdfs:label <http://purl.obolibrary.org/obo/PR_000003264> "collagen alpha-1(I) chain")
 SubClassOf(<http://purl.obolibrary.org/obo/PR_000003264> <http://purl.obolibrary.org/obo/PR_000003263>)
 
+# Class: <http://purl.obolibrary.org/obo/PR_000003328> (collagen alpha-1(III) chain)
+
+AnnotationAssertion(Annotation(<http://www.geneontology.org/formats/oboInOwl#hasDbXref> "PRO:CNA") <http://purl.obolibrary.org/obo/IAO_0000115> <http://purl.obolibrary.org/obo/PR_000003328> "A collagen alpha chain that is a translation product of the human COL3A1 gene or a 1:1 ortholog thereof.")
+AnnotationAssertion(Annotation(<http://www.geneontology.org/formats/oboInOwl#hasDbXref> "PRO:DNx") Annotation(<http://www.geneontology.org/formats/oboInOwl#hasSynonymType> <http://purl.obolibrary.org/obo/pr#PRO-short-label>) <http://www.geneontology.org/formats/oboInOwl#hasExactSynonym> <http://purl.obolibrary.org/obo/PR_000003328> "COL3A1")
+AnnotationAssertion(<http://www.geneontology.org/formats/oboInOwl#hasOBONamespace> <http://purl.obolibrary.org/obo/PR_000003328> "protein")
+AnnotationAssertion(<http://www.geneontology.org/formats/oboInOwl#id> <http://purl.obolibrary.org/obo/PR_000003328> "PR:000003328")
+AnnotationAssertion(rdfs:comment <http://purl.obolibrary.org/obo/PR_000003328> "Category=gene.")
+AnnotationAssertion(rdfs:label <http://purl.obolibrary.org/obo/PR_000003328> "collagen alpha-1(III) chain")
+SubClassOf(<http://purl.obolibrary.org/obo/PR_000003328> <http://purl.obolibrary.org/obo/PR_000003262>)
+
+# Class: <http://purl.obolibrary.org/obo/PR_000003353> (collagen alpha-1(VI) chain)
+
+AnnotationAssertion(Annotation(<http://www.geneontology.org/formats/oboInOwl#hasDbXref> "PRO:CNA") <http://purl.obolibrary.org/obo/IAO_0000115> <http://purl.obolibrary.org/obo/PR_000003353> "A collagen type VI alpha chain that is a translation product of the human COL6A1 gene or a 1:1 ortholog thereof.")
+AnnotationAssertion(Annotation(<http://www.geneontology.org/formats/oboInOwl#hasDbXref> "PRO:DNx") Annotation(<http://www.geneontology.org/formats/oboInOwl#hasSynonymType> <http://purl.obolibrary.org/obo/pr#PRO-short-label>) <http://www.geneontology.org/formats/oboInOwl#hasExactSynonym> <http://purl.obolibrary.org/obo/PR_000003353> "COL6A1")
+AnnotationAssertion(<http://www.geneontology.org/formats/oboInOwl#hasOBONamespace> <http://purl.obolibrary.org/obo/PR_000003353> "protein")
+AnnotationAssertion(<http://www.geneontology.org/formats/oboInOwl#id> <http://purl.obolibrary.org/obo/PR_000003353> "PR:000003353")
... (174 more lines truncated)
```

## Agent Attempts (9)

| # | Model | Runtime | F1 | P | R | Blob | Eval PR | Detail |
|---|-------|---------|-----|-----|-----|------|---------|--------|
| 1 | gpt-5.5 | opencode | 0.093 | 0.050 | 0.583 | `ab81b79` | [#73](https://github.com/ai4curation/eval-ont-agent-cl/pull/73) | [attempt](attempts/pr73.md) |
| 2 | gpt-5.5 | opencode | 0.093 | 0.050 | 0.583 | `ab81b79` | [#54](https://github.com/ai4curation/eval-ont-agent-cl/pull/54) | [attempt](attempts/pr54.md) |
| 3 | gpt-5.4 | opencode | 0.080 | 0.043 | 0.545 | `3d76355` | [#575](https://github.com/ai4curation/eval-ont-agent-cl/pull/575) | [attempt](attempts/pr575.md) |
| 4 | gpt-5.4 | opencode | 0.080 | 0.043 | 0.545 | `3d76355` | [#513](https://github.com/ai4curation/eval-ont-agent-cl/pull/513) | [attempt](attempts/pr513.md) |
| 5 | claude-sonnet-4.5 | claude | 0.000 | 0.000 | 0.000 | `d4efc24` | [#208](https://github.com/ai4curation/eval-ont-agent-cl/pull/208) | [attempt](attempts/pr208.md) |
| 6 | claude-opus-4.7 | claude | 0.000 | 0.000 | 0.000 | `1b10d84` | [#180](https://github.com/ai4curation/eval-ont-agent-cl/pull/180) | [attempt](attempts/pr180.md) |
| 7 | claude-haiku-4.5 | claude | 0.000 | 0.000 | 0.000 | `d4628eb` | [#99](https://github.com/ai4curation/eval-ont-agent-cl/pull/99) | [attempt](attempts/pr99.md) |
| 8 | gpt-5.4 | codex | 0.000 | 0.000 | 0.000 | `3325b4c` | [#83](https://github.com/ai4curation/eval-ont-agent-cl/pull/83) | [attempt](attempts/pr83.md) |
| 9 | gpt-5.5 | codex | 0.000 | 0.000 | 0.000 | `cd27ef8` | [#36](https://github.com/ai4curation/eval-ont-agent-cl/pull/36) | [attempt](attempts/pr36.md) |
