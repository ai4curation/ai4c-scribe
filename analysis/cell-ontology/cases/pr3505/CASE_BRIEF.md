---
ontology: cell-ontology
repo: obophenotype/cell-ontology
issue_number: 3458
pr_number: 3505
issue_title: NTR Fibrochondrocyte progenitor cell (FCP)
pr_author: app/copilot-swe-agent
pr_merged_at: '2025-12-11'
task_type: new_term
difficulty: medium
scoping: tightly_scoped
scope: single_term
review_outcome: approved_first_time
num_agent_attempts: 6
generated_at: '2026-05-15'
domain_area: skeletal
best_f1: 0.696
best_model: claude-sonnet-4.5
---

# PR #3505 — NTR Fibrochondrocyte progenitor cell (FCP)

**cell-ontology** | [obophenotype/cell-ontology](https://github.com/obophenotype/cell-ontology) | [Issue #3458](https://github.com/obophenotype/cell-ontology/issues/3458) | [PR #3505](https://github.com/obophenotype/cell-ontology/pull/3505) | @app/copilot-swe-agent | merged 2025-12-11

`new_term` `medium` `tightly_scoped` `approved_first_time`

## Context

A new term request was filed for the fibrochondrocyte progenitor cell (FCP), a precursor cell that gives rise to fibrochondrocytes in fibrocartilaginous tissues such as the meniscus and temporomandibular joint disc. This term is part of a broader effort to populate the chondrocyte and cartilage cell branches of CL, complementing related terms like fibrochondrocyte (CL_4072104) added in PR #3467.

## Changes Made

Added 14 new lines to `cl-edit.owl` defining the FCP term with appropriate class declaration, label, textual definition referencing the progenitor-to-fibrochondrocyte differentiation pathway, parentage linking it to both progenitor cell and the chondrocyte lineage, and logical axioms capturing its developmental potential.

## Resolution

Approved on first review after 8 commits of iterative refinement. Medium difficulty because correctly modeling a progenitor cell requires establishing the develops_into relationship to the mature fibrochondrocyte and positioning the term appropriately within both the progenitor cell hierarchy and the cartilage cell lineage.

## Human Diff

```diff
diff --git a/src/ontology/cl-edit.owl b/src/ontology/cl-edit.owl
index 7bcf184f9..ead4ebcf5 100644
--- a/src/ontology/cl-edit.owl
+++ b/src/ontology/cl-edit.owl
@@ -3285,6 +3285,7 @@ Declaration(Class(obo:CL_7770003))
 Declaration(Class(obo:CL_7770004))
 Declaration(Class(obo:CL_7770005))
 Declaration(Class(obo:CL_7770006))
+Declaration(Class(obo:CL_9900000))
 Declaration(Class(obo:CP_0000000))
 Declaration(Class(obo:CP_0000025))
 Declaration(Class(obo:CP_0000027))
@@ -35330,6 +35331,7 @@ AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:31871141") Annotation(ob
 AnnotationAssertion(rdfs:label obo:CL_4072104 "fibrochondrocyte")
 EquivalentClasses(obo:CL_4072104 ObjectIntersectionOf(obo:CL_0000138 ObjectSomeValuesFrom(obo:BFO_0000050 obo:UBERON_0001995)))
 SubClassOf(obo:CL_4072104 obo:CL_0002320)
+SubClassOf(obo:CL_4072104 ObjectSomeValuesFrom(obo:RO_0002202 obo:CL_9900000))
 SubClassOf(obo:CL_4072104 ObjectSomeValuesFrom(obo:RO_0002292 obo:PR_000003264))
 SubClassOf(obo:CL_4072104 ObjectSomeValuesFrom(obo:RO_0002292 obo:PR_000003328))
 SubClassOf(obo:CL_4072104 ObjectSomeValuesFrom(obo:RO_0002292 obo:PR_000003353))
@@ -35385,6 +35387,18 @@ SubClassOf(obo:CL_7770006 obo:CL_0002367)
 SubClassOf(obo:CL_7770006 ObjectSomeValuesFrom(obo:RO_0002162 obo:NCBITaxon_9606))
 SubClassOf(obo:CL_7770006 ObjectSomeValuesFrom(obo:RO_0002292 obo:PR_Q9UIK5))
 
+# Class: obo:CL_9900000 (fibrochondrocyte progenitor cell)
+
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:31871141") Annotation(oboInOwl:hasDbXref "PMID:36338137") obo:IAO_0000115 obo:CL_9900000 "A mesenchymal progenitor cell located in fibrocartilaginous tissues, along the fibrochondrocytic differentiation pathway that co-expresses both fibrochondrocyte markers (COL1A1, COL3A1) and mesenchymal stem cell markers (MCAM/CD146, MYLK) in humans. This cell serves as a progenitor for mature fibrochondrocytes and other meniscal cell types, with differentiation regulated by TGF-β signaling, focal adhesion, and extracellular matrix-receptor interaction pathways.")
+AnnotationAssertion(terms:contributor obo:CL_9900000 <https://orcid.org/0009-0000-8480-9277>)
+AnnotationAssertion(terms:creator obo:CL_9900000 "GitHub Copilot")
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:31871141") Annotation(oboInOwl:hasSynonymType obo:OMO_0003000) oboInOwl:hasRelatedSynonym obo:CL_9900000 "FCP")
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:31871141") rdfs:comment obo:CL_9900000 "A fibrochondrocyte progenitor cell demonstrates colony-forming capacity and multi-lineage differentiation potential toward osteogenic and adipogenic lineages.")
+AnnotationAssertion(rdfs:label obo:CL_9900000 "fibrochondrocyte progenitor cell")
+SubClassOf(obo:CL_9900000 obo:CL_0008019)
+SubClassOf(obo:CL_9900000 obo:CL_0011026)
+SubClassOf(obo:CL_9900000 ObjectSomeValuesFrom(obo:BFO_0000050 obo:UBERON_0001995))
+
 # Class: obo:CP_0000000 (obsolete CP:0000000)
 
 AnnotationAssertion(obo:IAO_0100001 obo:CP_0000000 obo:CL_0017500)

```

## Agent Attempts (6)

### Attempt 1: claude-sonnet-4.5 / claude

- **Eval PR**: [#230](https://github.com/ai4curation/eval-ont-agent-cl/pull/230)
- **F1**: 0.696  **Precision**: 0.727  **Recall**: 0.667  **Jaccard**: 0.533
- **Trace**: [25877893188](https://github.com/ai4curation/eval-ont-agent-cl/tree/master/traces/25877893188)
- **Workflow run**: [25877893188](https://github.com/ai4curation/eval-ont-agent-cl/actions/runs/25877893188)

#### Agent PR Comment

## Summary

This PR adds a new term for **fibrochondrocyte progenitor cell (FCP)** in response to issue #3458.

## Changes Made

### New Term: CL_9900000 - fibrochondrocyte progenitor cell

**Term Details:**
- **ID:** CL_9900000 (from the temporary ID range as specified in cl-idranges.owl)
- **Label:** fibrochondrocyte progenitor cell
- **Synonym:** FCP (abbreviation, related synonym with PMID:31871141 reference)
- **Definition:** A mesenchymal progenitor cell located in fibrocartilaginous tissues, along the fibrochondrocytic differentiation pathway that co-expresses both fibrochondrocyte markers (COL1A1, COL3A1) and mesenchymal stem cell markers (MCAM/CD146, MYLK) in humans. FCP demonstrates colony-forming capacity and multi-lineage differentiation potential toward osteogenic and adipogenic lineages. This cell serves as a progenitor for mature fibrochondrocytes and other meniscal cell types, with differentiation regulated by TGF-β signaling, focal adhesion, and extracellular matrix-receptor interaction pathways.

**Logical Relationships:**
- SubClassOf: mesenchymal cell (CL_0008019)
- SubClassOf: progenitor cell (CL_0011026)
- SubClassOf: part_of some fibrocartilage (UBERON_0001995)
- SubClassOf: expresses some collagen alpha-1(I) chain (PR_000003264 / COL1A1)
- SubClassOf: expresses some collagen alpha-1(III) chain (PR_000003328 / COL3A1)

**Metadata:**
- Definition references: PMID:31871141, PMID:36338137
- Contributor ORCID: https://orcid.org/0009-0000-8480-9277
- Creator: GitHub Copilot
- Date: 2026-05-14
- Term tracker: https://github.com/obophenotype/cell-ontology/issues/3458

## Implementation Decisions

### Protein Markers
The issue requested four protein markers to be expressed:
1. ✅ COL1A1 (collagen alpha-1(I) chain) - Added as PR_000003264
2. ✅ COL3A1 (collagen alpha-1(III) chain) - Added as PR_000003328  
3. ⚠️ MCAM/CD146 (cell surface glycoprotein MUC18) - Mentioned in definition text only
4. ⚠️ MYLK (myosin light chain kinase, smooth muscle) - Mentioned in definition text only

I successfully added formal logical axioms for COL1A1 and COL3A1 using their PRO identifiers which are already used in the ontology for related cell types (fibrochondrocyte CL_4072104 and proliferative fibrochondrocyte CL_0020018).

For MCAM/CD146 and MYLK, I was unable to definitively identify the correct PRO identifiers used in this ontology. These markers are mentioned in the textual definition, which accurately reflects the biology described in the referenced publications. Future enhancements could add formal logical axioms for these markers once the appropriate PRO identifiers are confirmed.

### Parent Terms
Following the issue request, I assigned two parent classes:
- **mesenchymal cell (CL_0008019)** - Appropriate as FCP is described as a mesenchymal progenitor
- **progenitor cell (CL_0011026)** - Appropriate as FCP demonstrates progenitor characteristics including colony-forming capacity and multi-lineage differentiation potential

### Anatomical Location
- **part_of fibrocartilage (UBERON_0001995)** - Matches the issue request and the biological description of FCP being located in fibrocartilaginous tissues like the meniscus

## Validation

- ✅ Term ID follows OBO guidelines (CL_9900000 from temporary ID range)
- ✅ Definition includes inline references to PMIDs
- ✅ Synonym includes appropriate reference
- ✅ Parent terms are consistent with biology
- ✅ Anatomical location is specified
- ✅ Contributor ORCID added as requested
- ✅ Followed existing term patterns (see CL_0020018 proliferative fibrochondrocyte for similar structure)
- ✅ File syntax follows OWL functional syntax format (one axiom per line)
- ✅ All referenced classes (parent terms, proteins, anatomical structures) are already declared in the ontology

## Background Research

During implementation, I reviewed:
1. **PMID:31871141** - Referenced paper describing FCP characteristics and markers
2. **PMID:36338137** - Additional reference for FCP biology
3. **Existing related terms:**
   - CL_4072104 (fibrochondrocyte) - The differentiated cell type
   - CL_0020018 (proliferative fibrochondrocyte) - Related cell type that already mentions FCP in its definition
4. **Protein Ontology references** - To identify correct PRO identifiers for expressed proteins

The definition in CL_0020018 (proliferative fibrochondrocyte) explicitly mentions "fibrochondrocyte progenitors (FCP)" and describes them as being "positioned at the root of developmental trajectories," which aligns with and supports the creation of this new FCP term.

## Next Steps

As mentioned in the original issue, the requester plans to add a 'develops from' relationship to the fibrochondrocyte term (CL_4072104) to link it to this new progenitor cell. This would complete the lineage relationship:

```
fibrochondrocyte (CL_4072104) develops_from some fibrochondrocyte progenitor cell (CL_9900000)
```

This relationship should be added in a future update to establish the complete developmental hierarchy.

---
🤖 **Generated by claude agent**
- Runtime: `claude`
- Model: `claude-sonnet-4-5-20250929`
- Agent config: `ai4curation/cl-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-cl/actions/runs/25877893188)


#### Agent Issue Comment

Thank you for the detailed new term request! I've created the fibrochondrocyte progenitor cell (FCP) term as requested.

## Summary

**New Term ID:** CL_9900000  
**Term Label:** fibrochondrocyte progenitor cell  
**Synonym:** FCP (abbreviation)

The term has been added with:
- Parent classes: mesenchymal cell and progenitor cell
- Location: part of fibrocartilage
- Expression markers: COL1A1 and COL3A1
- Your ORCID has been added as a contributor
- References to PMID:31871141 and PMID:36338137

## Implementation Notes

I was able to add the collagen markers (COL1A1, COL3A1) as expression relationships. However, I encountered difficulty identifying the correct PRO (Protein Ontology) identifiers for MCAM/CD146 and MYLK to add them as formal logical axioms. The term definition mentions these markers in text form.

If you'd like to add formal logical axioms for MCAM/CD146 and MYLK expression in a future update, the PRO identifiers would need to be confirmed first.

As you mentioned in your request, you can now add the 'develops from' relationship to the fibrochondrocyte term (CL_4072104) to link it to this new progenitor cell.

Changes have been committed in PR #<NN>.

---
🤖 **Generated by claude agent**
- Runtime: `claude`
- Model: `claude-sonnet-4-5-20250929`
- Agent config: `ai4curation/cl-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-cl/actions/runs/25877893188)


#### Agent Diff

```diff
diff --git a/src/ontology/cl-edit.owl b/src/ontology/cl-edit.owl
index 7bcf184f9..92da4d45f 100644
--- a/src/ontology/cl-edit.owl
+++ b/src/ontology/cl-edit.owl
@@ -35385,6 +35385,22 @@ SubClassOf(obo:CL_7770006 obo:CL_0002367)
 SubClassOf(obo:CL_7770006 ObjectSomeValuesFrom(obo:RO_0002162 obo:NCBITaxon_9606))
 SubClassOf(obo:CL_7770006 ObjectSomeValuesFrom(obo:RO_0002292 obo:PR_Q9UIK5))
 
+# Class: obo:CL_9900000 (fibrochondrocyte progenitor cell)
+
+Declaration(Class(obo:CL_9900000))
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:31871141") Annotation(oboInOwl:hasDbXref "PMID:36338137") obo:IAO_0000115 obo:CL_9900000 "A mesenchymal progenitor cell located in fibrocartilaginous tissues, along the fibrochondrocytic differentiation pathway that co-expresses both fibrochondrocyte markers (COL1A1, COL3A1) and mesenchymal stem cell markers (MCAM/CD146, MYLK) in humans. FCP demonstrates colony-forming capacity and multi-lineage differentiation potential toward osteogenic and adipogenic lineages. This cell serves as a progenitor for mature fibrochondrocytes and other meniscal cell types, with differentiation regulated by TGF-β signaling, focal adhesion, and extracellular matrix-receptor interaction pathways.")
+AnnotationAssertion(terms:contributor obo:CL_9900000 <https://orcid.org/0009-0000-8480-9277>)
+AnnotationAssertion(terms:creator obo:CL_9900000 "GitHub Copilot")
+AnnotationAssertion(terms:date obo:CL_9900000 "2026-05-14T00:00:00Z"^^xsd:dateTime)
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:31871141") Annotation(oboInOwl:hasSynonymType obo:OMO_0003000) oboInOwl:hasRelatedSynonym obo:CL_9900000 "FCP")
+AnnotationAssertion(oboInOwl:hasDbXref obo:CL_9900000 "https://github.com/obophenotype/cell-ontology/issues/3458")
+AnnotationAssertion(rdfs:label obo:CL_9900000 "fibrochondrocyte progenitor cell")
+SubClassOf(obo:CL_9900000 obo:CL_0008019)
+SubClassOf(obo:CL_9900000 obo:CL_0011026)
+SubClassOf(obo:CL_9900000 ObjectSomeValuesFrom(obo:BFO_0000050 obo:UBERON_0001995))
+SubClassOf(obo:CL_9900000 ObjectSomeValuesFrom(obo:RO_0002292 obo:PR_000003264))
+SubClassOf(obo:CL_9900000 ObjectSomeValuesFrom(obo:RO_0002292 obo:PR_000003328))
+
 # Class: obo:CP_0000000 (obsolete CP:0000000)
 
 AnnotationAssertion(obo:IAO_0100001 obo:CP_0000000 obo:CL_0017500)

```

### Attempt 2: claude-opus-4.7 / claude

- **Eval PR**: [#280](https://github.com/ai4curation/eval-ont-agent-cl/pull/280)
- **F1**: 0.615  **Precision**: 0.727  **Recall**: 0.533  **Jaccard**: 0.444

#### Agent Diff

```diff
diff --git a/src/ontology/cl-edit.owl b/src/ontology/cl-edit.owl
index 7bcf184f9..960b14cfa 100644
--- a/src/ontology/cl-edit.owl
+++ b/src/ontology/cl-edit.owl
@@ -3285,6 +3285,7 @@ Declaration(Class(obo:CL_7770003))
 Declaration(Class(obo:CL_7770004))
 Declaration(Class(obo:CL_7770005))
 Declaration(Class(obo:CL_7770006))
+Declaration(Class(obo:CL_9900000))
 Declaration(Class(obo:CP_0000000))
 Declaration(Class(obo:CP_0000025))
 Declaration(Class(obo:CP_0000027))
@@ -35385,6 +35386,24 @@ SubClassOf(obo:CL_7770006 obo:CL_0002367)
 SubClassOf(obo:CL_7770006 ObjectSomeValuesFrom(obo:RO_0002162 obo:NCBITaxon_9606))
 SubClassOf(obo:CL_7770006 ObjectSomeValuesFrom(obo:RO_0002292 obo:PR_Q9UIK5))
 
+# Class: obo:CL_9900000 (fibrochondrocyte progenitor cell)
+
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:31871141") Annotation(oboInOwl:hasDbXref "PMID:36338137") obo:IAO_0000115 obo:CL_9900000 "A mesenchymal progenitor cell located in fibrocartilaginous tissues, along the fibrochondrocytic differentiation pathway that co-expresses both fibrochondrocyte markers (COL1A1, COL3A1) and mesenchymal stem cell markers (MCAM/CD146, MYLK) in humans. FCP demonstrates colony-forming capacity and multi-lineage differentiation potential toward osteogenic and adipogenic lineages. This cell serves as a progenitor for mature fibrochondrocytes and other meniscal cell types, with differentiation regulated by TGF-beta signaling, focal adhesion, and extracellular matrix-receptor interaction pathways.")
+AnnotationAssertion(terms:contributor obo:CL_9900000 <https://orcid.org/0009-0000-8480-9277>)
+AnnotationAssertion(terms:creator obo:CL_9900000 "GitHub Copilot")
+AnnotationAssertion(terms:date obo:CL_9900000 "2026-05-15T00:00:00Z"^^xsd:dateTime)
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:31871141") Annotation(oboInOwl:hasSynonymType obo:OMO_0003000) oboInOwl:hasRelatedSynonym obo:CL_9900000 "FCP")
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:31871141") oboInOwl:hasRelatedSynonym obo:CL_9900000 "fibrochondrocyte progenitor")
+AnnotationAssertion(rdfs:label obo:CL_9900000 "fibrochondrocyte progenitor cell")
+AnnotationAssertion(obo:IAO_0000233 obo:CL_9900000 <https://github.com/obophenotype/cell-ontology/issues/3458>)
+SubClassOf(obo:CL_9900000 obo:CL_0008019)
+SubClassOf(obo:CL_9900000 obo:CL_0011026)
+SubClassOf(obo:CL_9900000 ObjectSomeValuesFrom(obo:BFO_0000050 obo:UBERON_0001995))
+SubClassOf(obo:CL_9900000 ObjectSomeValuesFrom(obo:RO_0002292 obo:PR_000001127))
+SubClassOf(obo:CL_9900000 ObjectSomeValuesFrom(obo:RO_0002292 obo:PR_000003264))
+SubClassOf(obo:CL_9900000 ObjectSomeValuesFrom(obo:RO_0002292 obo:PR_000003328))
+SubClassOf(obo:CL_9900000 ObjectSomeValuesFrom(obo:RO_0002292 obo:PR_000010845))
+
 # Class: obo:CP_0000000 (obsolete CP:0000000)
 
 AnnotationAssertion(obo:IAO_0100001 obo:CP_0000000 obo:CL_0017500)

```

### Attempt 3: claude-haiku-4.5 / claude

- **Eval PR**: [#100](https://github.com/ai4curation/eval-ont-agent-cl/pull/100)
- **F1**: 0.000  **Precision**: 0.000  **Recall**: 0.000  **Jaccard**: 0.000
- **Workflow run**: [25640376309](https://github.com/ai4curation/eval-ont-agent-cl/actions/runs/25640376309)

#### Agent PR Comment

# PR: Add fibrochondrocyte progenitor cell (CL_9900001)

## Summary

This PR adds a new cell type term to the Cell Ontology: fibrochondrocyte progenitor cell (FCP). The term was requested in issue #3458 to represent a specific mesenchymal progenitor cell population located in fibrocartilaginous tissues.

## Changes Made

### Ontology Entry (src/ontology/cl-edit.owl)

**New Term:** CL_9900001 - fibrochondrocyte progenitor cell

**Key Features:**
- **ID Range:** CL_9900001 (temporary ID range for new terms)
- **Parent Classes:** 
  - Mesenchymal cell (CL_0008019)
  - Progenitor cell (CL_0011026)
- **Location:** Part of fibrocartilage (UBERON_0001995)

**Definition:**
"A mesenchymal progenitor cell located in fibrocartilaginous tissues that co-expresses both fibrochondrocyte markers (COL1A1, COL3A1) and mesenchymal stem cell markers (MCAM/CD146, MYLK) in humans. FCP demonstrates colony-forming capacity and multi-lineage differentiation potential toward osteogenic and adipogenic lineages. This cell serves as a progenitor for mature fibrochondrocytes and other meniscal cell types, with differentiation regulated by TGF-β signaling, focal adhesion, and extracellular matrix-receptor interaction pathways."

**References:**
- PMID:31871141 (primary reference for FCP characteristics)
- PMID:36338137 (secondary reference)

**Metadata:**
- **Abbreviation (Related Synonym):** FCP (with reference PMID:31871141)
- **Contributor:** https://orcid.org/0009-0000-8480-9277 (as specified in the issue)
- **Issue Reference:** https://github.com/obophenotype/cell-ontology/issues/3458
- **Date Created:** 2026-05-10

## Validation Checklist

- [x] Term ID follows correct format (CL_9900001 in temporary ID range)
- [x] Term does not already exist in the ontology
- [x] Parent terms verified to exist (CL_0008019, CL_0011026)
- [x] Anatomical location verified (UBERON_0001995 - fibrocartilage)
- [x] Definition includes proper references (PMIDs)
- [x] ORCID contributor added as requested
- [x] GitHub issue linked via IAO_0000233 annotation
- [x] Abbreviation included as related synonym with citation
- [x] Term appropriately positioned in ontology hierarchy

## Implementation Notes

The term was designed to represent a previously undescribed progenitor population that:
1. Resides in fibrocartilaginous tissues
2. Co-expresses markers from both fibrochondrocytes and mesenchymal stem cells
3. Has the capacity to differentiate into multiple lineages
4. Serves as a developmental precursor to mature fibrochondrocytes

The hierarchical placement under both "mesenchymal cell" and "progenitor cell" reflects its dual nature as a tissue-localized progenitor with mesenchymal characteristics. The inclusion of "part of fibrocartilage" via BFO:part_of relationship correctly captures its anatomical location.

---
🤖 **Generated by claude agent**
- Runtime: `claude`
- Model: `claude-haiku-4-5-20251001`
- Agent config: `ai4curation/cl-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-cl/actions/runs/25640376309)


#### Agent Issue Comment

# Issue #3458: NTR Fibrochondrocyte progenitor cell (FCP)

## Status: Completed

The new term for fibrochondrocyte progenitor cell has been added to the Cell Ontology with the following details:

**Term ID:** CL_9900001
**Label:** fibrochondrocyte progenitor cell
**Abbreviation:** FCP

The term has been integrated into the ontology hierarchy as a subclass of both mesenchymal cell (CL_0008019) and progenitor cell (CL_0011026), and is located in fibrocartilage (UBERON_0001995).

The definition comprehensively describes the cell as a mesenchymal progenitor with co-expression of fibrochondrocyte markers (COL1A1, COL3A1) and mesenchymal stem cell markers (MCAM/CD146, MYLK), with documented colony-forming capacity and multi-lineage differentiation potential.

The ORCID provided (https://orcid.org/0009-0000-8480-9277) has been added as a contributor.

Changes committed in PR #<NN>.

---
🤖 **Generated by claude agent**
- Runtime: `claude`
- Model: `claude-haiku-4-5-20251001`
- Agent config: `ai4curation/cl-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-cl/actions/runs/25640376309)


#### Agent Diff

```diff
diff --git a/src/ontology/cl-edit.owl b/src/ontology/cl-edit.owl
index 7bcf184f9..67c802e8d 100644
--- a/src/ontology/cl-edit.owl
+++ b/src/ontology/cl-edit.owl
@@ -3285,6 +3285,7 @@ Declaration(Class(obo:CL_7770003))
 Declaration(Class(obo:CL_7770004))
 Declaration(Class(obo:CL_7770005))
 Declaration(Class(obo:CL_7770006))
+Declaration(Class(obo:CL_9900001))
 Declaration(Class(obo:CP_0000000))
 Declaration(Class(obo:CP_0000025))
 Declaration(Class(obo:CP_0000027))
@@ -35385,6 +35386,18 @@ SubClassOf(obo:CL_7770006 obo:CL_0002367)
 SubClassOf(obo:CL_7770006 ObjectSomeValuesFrom(obo:RO_0002162 obo:NCBITaxon_9606))
 SubClassOf(obo:CL_7770006 ObjectSomeValuesFrom(obo:RO_0002292 obo:PR_Q9UIK5))
 
+# Class: obo:CL_9900001 (fibrochondrocyte progenitor cell)
+
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:31871141") Annotation(oboInOwl:hasDbXref "PMID:36338137") obo:IAO_0000115 obo:CL_9900001 "A mesenchymal progenitor cell located in fibrocartilaginous tissues that co-expresses both fibrochondrocyte markers (COL1A1, COL3A1) and mesenchymal stem cell markers (MCAM/CD146, MYLK) in humans. FCP demonstrates colony-forming capacity and multi-lineage differentiation potential toward osteogenic and adipogenic lineages. This cell serves as a progenitor for mature fibrochondrocytes and other meniscal cell types, with differentiation regulated by TGF-β signaling, focal adhesion, and extracellular matrix-receptor interaction pathways.")
+AnnotationAssertion(terms:contributor obo:CL_9900001 <https://orcid.org/0009-0000-8480-9277>)
+AnnotationAssertion(terms:date obo:CL_9900001 "2026-05-10T00:00:00Z"^^xsd:dateTime)
+AnnotationAssertion(rdfs:label obo:CL_9900001 "fibrochondrocyte progenitor cell")
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:31871141") Annotation(oboInOwl:hasSynonymType obo:OMO_0003000) oboInOwl:hasRelatedSynonym obo:CL_9900001 "FCP")
+AnnotationAssertion(obo:IAO_0000233 obo:CL_9900001 <https://github.com/obophenotype/cell-ontology/issues/3458>)
+SubClassOf(obo:CL_9900001 obo:CL_0008019)
+SubClassOf(obo:CL_9900001 obo:CL_0011026)
+SubClassOf(obo:CL_9900001 ObjectSomeValuesFrom(obo:BFO_0000050 obo:UBERON_0001995))
+
 # Class: obo:CP_0000000 (obsolete CP:0000000)
 
 AnnotationAssertion(obo:IAO_0100001 obo:CP_0000000 obo:CL_0017500)

```

### Attempt 4: gpt-5.5 / opencode

- **Eval PR**: [#66](https://github.com/ai4curation/eval-ont-agent-cl/pull/66)
- **F1**: 0.000  **Precision**: 0.000  **Recall**: 0.000  **Jaccard**: 0.000
- **Trace**: [25615959701](https://github.com/ai4curation/eval-ont-agent-cl/tree/master/traces/25615959701)
- **Workflow run**: [25615959701](https://github.com/ai4curation/eval-ont-agent-cl/actions/runs/25615959701)

#### Agent PR Comment

## Summary

Added `fibrochondrocyte progenitor cell` (`CL_0020021`) to `src/ontology/cl-edit.owl` for issue #3458.

## Changes made

- Added a new class declaration and term block for `fibrochondrocyte progenitor cell`.
- Added a PMID-supported definition based on the requested meniscus/fibrocartilage progenitor biology (`PMID:31871141`, `PMID:36338137`).
- Added the requested abbreviation synonym `FCP` as a related abbreviation synonym with `PMID:31871141`.
- Added contributor ORCID `https://orcid.org/0009-0000-8480-9277`, creator metadata, date metadata, and a tracker link to issue #3458.
- Placed the term logically as an intersection of:
  - `mesenchymal cell` (`CL_0008019`)
  - `progenitor cell` (`CL_0011026`)
  - `part of` some `fibrocartilage` (`UBERON_0001995`)
- Added a `develops into` relationship to `fibrochondrocyte` (`CL_4072104`).
- Added marker-expression axioms for:
  - MCAM/CD146 / cell surface glycoprotein MUC18 (`PR_000001127`)
  - COL1A1 / collagen alpha-1(I) chain (`PR_000003264`)
  - COL3A1 / collagen alpha-1(III) chain (`PR_000003328`)
  - MYLK / myosin light chain kinase, smooth muscle (`PR_000010845`)

## Checks completed

- Confirmed no local `fibrochondrocyte progenitor cell` term was present in `src/ontology/cl-edit.owl` before editing.
- Checked the requested parent terms in `src/ontology/cl-edit.owl`:
  - `mesenchymal cell` (`CL_0008019`)
  - `progenitor cell` (`CL_0011026`)
- Checked existing related local terms, including `fibrochondrocyte` and `proliferative fibrochondrocyte`, for consistency.
- Retrieved PubMed abstracts for `PMID:31871141` and `PMID:36338137` to verify the definition scope.
- Looked up PR identifiers for requested marker proteins via OLS.
- Validated syntax with:
  - `robot convert -i src/ontology/cl-edit.owl -o /tmp/cl-edit-check.ofn`
  - `robot reason -i src/ontology/cl-edit.owl --reasoner ELK --equivalent-classes-allowed all --exclude-duplicate-axioms true -o /tmp/cl-edit-reasoned.owl`

---
🤖 **Generated by pi agent**
- Runtime: `pi`
- Model: `openai/gpt-5.5`
- Agent config: `ai4curation/cl-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-cl/actions/runs/25615959701)


#### Agent Issue Comment

Changes committed in PR #<NN>.

---
🤖 **Generated by pi agent**
- Runtime: `pi`
- Model: `openai/gpt-5.5`
- Agent config: `ai4curation/cl-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-cl/actions/runs/25615959701)


#### Agent Diff

```diff
diff --git a/src/ontology/cl-edit.owl b/src/ontology/cl-edit.owl
index 7bcf184f9..8e94f3f50 100644
--- a/src/ontology/cl-edit.owl
+++ b/src/ontology/cl-edit.owl
@@ -2277,6 +2277,7 @@ Declaration(Class(obo:CL_0020017))
 Declaration(Class(obo:CL_0020018))
 Declaration(Class(obo:CL_0020019))
 Declaration(Class(obo:CL_0020020))
+Declaration(Class(obo:CL_0020021))
 Declaration(Class(obo:CL_0700009))
 Declaration(Class(obo:CL_1000001))
 Declaration(Class(obo:CL_1000022))
@@ -3362,6 +3363,7 @@ Declaration(Class(obo:PATO_0070031))
 Declaration(Class(obo:PATO_0070034))
 Declaration(Class(obo:PATO_0070062))
 Declaration(Class(obo:PATO_0070063))
+Declaration(Class(obo:PR_000001127))
 Declaration(Class(obo:PR_000001224))
 Declaration(Class(obo:PR_000001243))
 Declaration(Class(obo:PR_000001244))
@@ -3387,6 +3389,7 @@ Declaration(Class(obo:PR_000007498))
 Declaration(Class(obo:PR_000007785))
 Declaration(Class(obo:PR_000009981))
 Declaration(Class(obo:PR_000010529))
+Declaration(Class(obo:PR_000010845))
 Declaration(Class(obo:PR_000011241))
 Declaration(Class(obo:PR_000012318))
 Declaration(Class(obo:PR_000013015))
@@ -25629,6 +25632,22 @@ SubClassOf(obo:CL_0020020 obo:CL_0000138)
 SubClassOf(obo:CL_0020020 ObjectSomeValuesFrom(obo:RO_0002215 obo:GO_0070278))
 SubClassOf(obo:CL_0020020 ObjectSomeValuesFrom(obo:RO_0002215 obo:GO_1990079))
 
+# Class: obo:CL_0020021 (fibrochondrocyte progenitor cell)
+
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:31871141") Annotation(oboInOwl:hasDbXref "PMID:36338137") obo:IAO_0000115 obo:CL_0020021 "A mesenchymal progenitor cell that is part of fibrocartilage and lies on the fibrochondrocytic differentiation pathway. In human meniscus, fibrochondrocyte progenitor cells co-express fibrochondrocyte markers COL1A1 and COL3A1 and mesenchymal progenitor markers MCAM/CD146 and MYLK, form colonies, and can differentiate toward osteogenic and adipogenic lineages.")
+AnnotationAssertion(obo:IAO_0000233 obo:CL_0020021 "https://github.com/obophenotype/cell-ontology/issues/3458")
+AnnotationAssertion(terms:contributor obo:CL_0020021 <https://orcid.org/0009-0000-8480-9277>)
+AnnotationAssertion(terms:creator obo:CL_0020021 "GitHub Copilot")
+AnnotationAssertion(terms:date obo:CL_0020021 "2026-05-10T00:00:00Z"^^xsd:dateTime)
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:31871141") Annotation(oboInOwl:hasSynonymType obo:OMO_0003000) oboInOwl:hasRelatedSynonym obo:CL_0020021 "FCP")
+AnnotationAssertion(rdfs:label obo:CL_0020021 "fibrochondrocyte progenitor cell")
+EquivalentClasses(obo:CL_0020021 ObjectIntersectionOf(obo:CL_0008019 obo:CL_0011026 ObjectSomeValuesFrom(obo:BFO_0000050 obo:UBERON_0001995)))
+SubClassOf(obo:CL_0020021 ObjectSomeValuesFrom(obo:RO_0002203 obo:CL_4072104))
+SubClassOf(obo:CL_0020021 ObjectSomeValuesFrom(obo:RO_0002292 obo:PR_000001127))
+SubClassOf(obo:CL_0020021 ObjectSomeValuesFrom(obo:RO_0002292 obo:PR_000003264))
+SubClassOf(obo:CL_0020021 ObjectSomeValuesFrom(obo:RO_0002292 obo:PR_000003328))
+SubClassOf(obo:CL_0020021 ObjectSomeValuesFrom(obo:RO_0002292 obo:PR_000010845))
+
 # Class: obo:CL_0700009 (obsolete kidney collecting duct beta-intercalated cell)
 
 AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:24051376") Annotation(oboInOwl:hasDbXref "PMID:31300091") Annotation(oboInOwl:hasDbXref "PMID:32016094") obo:IAO_0000115 obo:CL_0700009 "OBSOLETE. A renal beta-intercalated cell that is part of the cortical collecting duct. The medullary collecting duct does not contain the renal beta-intercalated cell type.")

```

### Attempt 5: gpt-5.5 / opencode

- **Eval PR**: [#48](https://github.com/ai4curation/eval-ont-agent-cl/pull/48)
- **F1**: 0.000  **Precision**: 0.000  **Recall**: 0.000  **Jaccard**: 0.000
- **Trace**: [25615915819](https://github.com/ai4curation/eval-ont-agent-cl/tree/master/traces/25615915819)
- **Workflow run**: [25615915819](https://github.com/ai4curation/eval-ont-agent-cl/actions/runs/25615915819)

#### Agent PR Comment

## Summary

Added the new CL term `fibrochondrocyte progenitor cell` (`CL_9900001`) for issue #3458.

## Rationale

The issue requested a new fibrochondrocyte progenitor cell term with FCP as an abbreviation synonym, references to PMID:31871141 and PMID:36338137, fibrocartilage location, mesenchymal/progenitor parentage, and marker expression axioms. The new term is modeled as a mesenchymal progenitor cell that is part of fibrocartilage, develops into fibrochondrocyte, and expresses MCAM/CD146, COL1A1, COL3A1, and MYLK.

## Completed Checklist

- Checked `src/ontology/cl-edit.owl` for an existing fibrochondrocyte progenitor cell term.
- Checked existing parent and related terms: `mesenchymal cell`, `progenitor cell`, and `fibrochondrocyte`.
- Reused the existing fibrocartilage modeling from `fibrochondrocyte` (`UBERON_0001995`).
- Confirmed marker PR identifiers through OLS/PR lookups: `PR_000001127` for MCAM/CD146, `PR_000003264` for COL1A1, `PR_000003328` for COL3A1, and `PR_000010845` for MYLK.
- Read PubMed records for PMID:31871141 and PMID:36338137; `aurelian fulltext` was attempted but unavailable in this environment.
- Added contributor ORCID, creator, date, and term tracker metadata.
- Validated syntax with `robot convert -i src/ontology/cl-edit.owl -o /tmp/opencode/cl-edit-convert-check.owl`.

Signed-off-by: GitHub Copilot

---
🤖 **Generated by opencode agent**
- Runtime: `opencode`
- Model: `openai/gpt-5.5`
- Agent config: `ai4curation/cl-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-cl/actions/runs/25615915819)


#### Agent Issue Comment

Added `fibrochondrocyte progenitor cell` in the local PR branch. Changes committed in PR #<NN>.

---
🤖 **Generated by opencode agent**
- Runtime: `opencode`
- Model: `openai/gpt-5.5`
- Agent config: `ai4curation/cl-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-cl/actions/runs/25615915819)


#### Agent Diff

```diff
diff --git a/src/ontology/cl-edit.owl b/src/ontology/cl-edit.owl
index 7bcf184f9..8e94f3f50 100644
--- a/src/ontology/cl-edit.owl
+++ b/src/ontology/cl-edit.owl
@@ -2277,6 +2277,7 @@ Declaration(Class(obo:CL_0020017))
 Declaration(Class(obo:CL_0020018))
 Declaration(Class(obo:CL_0020019))
 Declaration(Class(obo:CL_0020020))
+Declaration(Class(obo:CL_0020021))
 Declaration(Class(obo:CL_0700009))
 Declaration(Class(obo:CL_1000001))
 Declaration(Class(obo:CL_1000022))
@@ -3362,6 +3363,7 @@ Declaration(Class(obo:PATO_0070031))
 Declaration(Class(obo:PATO_0070034))
 Declaration(Class(obo:PATO_0070062))
 Declaration(Class(obo:PATO_0070063))
+Declaration(Class(obo:PR_000001127))
 Declaration(Class(obo:PR_000001224))
 Declaration(Class(obo:PR_000001243))
 Declaration(Class(obo:PR_000001244))
@@ -3387,6 +3389,7 @@ Declaration(Class(obo:PR_000007498))
 Declaration(Class(obo:PR_000007785))
 Declaration(Class(obo:PR_000009981))
 Declaration(Class(obo:PR_000010529))
+Declaration(Class(obo:PR_000010845))
 Declaration(Class(obo:PR_000011241))
 Declaration(Class(obo:PR_000012318))
 Declaration(Class(obo:PR_000013015))
@@ -25629,6 +25632,22 @@ SubClassOf(obo:CL_0020020 obo:CL_0000138)
 SubClassOf(obo:CL_0020020 ObjectSomeValuesFrom(obo:RO_0002215 obo:GO_0070278))
 SubClassOf(obo:CL_0020020 ObjectSomeValuesFrom(obo:RO_0002215 obo:GO_1990079))
 
+# Class: obo:CL_0020021 (fibrochondrocyte progenitor cell)
+
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:31871141") Annotation(oboInOwl:hasDbXref "PMID:36338137") obo:IAO_0000115 obo:CL_0020021 "A mesenchymal progenitor cell that is part of fibrocartilage and lies on the fibrochondrocytic differentiation pathway. In human meniscus, fibrochondrocyte progenitor cells co-express fibrochondrocyte markers COL1A1 and COL3A1 and mesenchymal progenitor markers MCAM/CD146 and MYLK, form colonies, and can differentiate toward osteogenic and adipogenic lineages.")
+AnnotationAssertion(obo:IAO_0000233 obo:CL_0020021 "https://github.com/obophenotype/cell-ontology/issues/3458")
+AnnotationAssertion(terms:contributor obo:CL_0020021 <https://orcid.org/0009-0000-8480-9277>)
+AnnotationAssertion(terms:creator obo:CL_0020021 "GitHub Copilot")
+AnnotationAssertion(terms:date obo:CL_0020021 "2026-05-10T00:00:00Z"^^xsd:dateTime)
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:31871141") Annotation(oboInOwl:hasSynonymType obo:OMO_0003000) oboInOwl:hasRelatedSynonym obo:CL_0020021 "FCP")
+AnnotationAssertion(rdfs:label obo:CL_0020021 "fibrochondrocyte progenitor cell")
+EquivalentClasses(obo:CL_0020021 ObjectIntersectionOf(obo:CL_0008019 obo:CL_0011026 ObjectSomeValuesFrom(obo:BFO_0000050 obo:UBERON_0001995)))
+SubClassOf(obo:CL_0020021 ObjectSomeValuesFrom(obo:RO_0002203 obo:CL_4072104))
+SubClassOf(obo:CL_0020021 ObjectSomeValuesFrom(obo:RO_0002292 obo:PR_000001127))
+SubClassOf(obo:CL_0020021 ObjectSomeValuesFrom(obo:RO_0002292 obo:PR_000003264))
+SubClassOf(obo:CL_0020021 ObjectSomeValuesFrom(obo:RO_0002292 obo:PR_000003328))
+SubClassOf(obo:CL_0020021 ObjectSomeValuesFrom(obo:RO_0002292 obo:PR_000010845))
+
 # Class: obo:CL_0700009 (obsolete kidney collecting duct beta-intercalated cell)
 
 AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:24051376") Annotation(oboInOwl:hasDbXref "PMID:31300091") Annotation(oboInOwl:hasDbXref "PMID:32016094") obo:IAO_0000115 obo:CL_0700009 "OBSOLETE. A renal beta-intercalated cell that is part of the cortical collecting duct. The medullary collecting duct does not contain the renal beta-intercalated cell type.")

```

### Attempt 6: gpt-5.5 / codex

- **Eval PR**: [#29](https://github.com/ai4curation/eval-ont-agent-cl/pull/29)
- **F1**: 0.000  **Precision**: 0.000  **Recall**: 0.000  **Jaccard**: 0.000
- **Trace**: [25615880010](https://github.com/ai4curation/eval-ont-agent-cl/tree/master/traces/25615880010)
- **Workflow run**: [25615880010](https://github.com/ai4curation/eval-ont-agent-cl/actions/runs/25615880010)

#### Agent PR Comment

## Summary

Added a new CL term for `fibrochondrocyte progenitor cell` (`CL_9900001`) in `src/ontology/cl-edit.owl`.

The term includes:
- PMID-backed definition using PMID:31871141 and PMID:36338137.
- Related abbreviation synonym `FCP` with abbreviation synonym type.
- Contributor ORCID from the issue.
- `terms:creator`, `terms:date`, and issue tracker metadata.
- Logical placement as both a `mesenchymal cell` and `progenitor cell`.
- Fibrocartilage location and marker expression axioms for MCAM/CD146, COL1A1, COL3A1, and human MYLK.
- Homo sapiens taxon restriction, matching the human marker evidence in the request.

## Rationale

The requested label was not already present in `cl-edit.owl`. I modeled the term from the requested parentage and definition, using the existing `fibrochondrocyte` and `proliferative fibrochondrocyte` entries as local consistency checks for fibrocartilage and collagen marker modeling.

I used `UBERON_0001995` for fibrocartilage, following the existing `fibrochondrocyte` logical definition, and reused existing CL marker-expression practice with `RO_0002292`.

## Checklist

- [x] Read `__issue_context__.json`.
- [x] Checked `cl-edit.owl` for an existing `fibrochondrocyte progenitor cell` term and related fibrochondrocyte/progenitor terms.
- [x] Checked parent consistency for `mesenchymal cell` and `progenitor cell`.
- [x] Checked relevant DOSDP patterns for anatomical location and plasma membrane marker modeling.
- [x] Tried `aurelian fulltext` for both PMIDs; it was not installed in this environment.
- [x] Checked PubMed metadata via NCBI E-utilities for PMID:31871141 and PMID:36338137.
- [x] Checked Protein Ontology evidence for COL1A1, COL3A1, MCAM/CD146, and MYLK identifiers.
- [x] Validated syntax with `robot convert`.
- [x] Validated reasoning with `robot reason`.

---
🤖 **Generated by codex agent**
- Runtime: `codex`
- Model: `gpt-5.5`
- Agent config: `ai4curation/cl-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-cl/actions/runs/25615880010)


#### Agent Issue Comment

Added `fibrochondrocyte progenitor cell` as `CL_9900001`; changes committed in PR #<NN>.

---
🤖 **Generated by codex agent**
- Runtime: `codex`
- Model: `gpt-5.5`
- Agent config: `ai4curation/cl-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-cl/actions/runs/25615880010)


#### Agent Diff

```diff
diff --git a/src/ontology/cl-edit.owl b/src/ontology/cl-edit.owl
index 7bcf184f9..66a3b1b46 100644
--- a/src/ontology/cl-edit.owl
+++ b/src/ontology/cl-edit.owl
@@ -3285,6 +3285,7 @@ Declaration(Class(obo:CL_7770003))
 Declaration(Class(obo:CL_7770004))
 Declaration(Class(obo:CL_7770005))
 Declaration(Class(obo:CL_7770006))
+Declaration(Class(obo:CL_9900001))
 Declaration(Class(obo:CP_0000000))
 Declaration(Class(obo:CP_0000025))
 Declaration(Class(obo:CP_0000027))
@@ -35385,6 +35386,18 @@ SubClassOf(obo:CL_7770006 obo:CL_0002367)
 SubClassOf(obo:CL_7770006 ObjectSomeValuesFrom(obo:RO_0002162 obo:NCBITaxon_9606))
 SubClassOf(obo:CL_7770006 ObjectSomeValuesFrom(obo:RO_0002292 obo:PR_Q9UIK5))
 
+# Class: obo:CL_9900001 (fibrochondrocyte progenitor cell)
+
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:31871141") Annotation(oboInOwl:hasDbXref "PMID:36338137") obo:IAO_0000115 obo:CL_9900001 "A mesenchymal progenitor cell located in fibrocartilage that is along the fibrochondrocytic differentiation pathway. In humans, this cell co-expresses the fibrochondrocyte markers COL1A1 and COL3A1 with the mesenchymal stem cell markers MCAM/CD146 and MYLK, demonstrates colony-forming capacity, and has multi-lineage differentiation potential toward osteogenic and adipogenic lineages.")
+AnnotationAssertion(obo:IAO_0000233 obo:CL_9900001 <https://github.com/obophenotype/cell-ontology/issues/3458>)
+AnnotationAssertion(terms:contributor obo:CL_9900001 <https://orcid.org/0009-0000-8480-9277>)
+AnnotationAssertion(terms:creator obo:CL_9900001 "GitHub Copilot")
+AnnotationAssertion(terms:date obo:CL_9900001 "2026-05-10T00:57:19Z"^^xsd:dateTime)
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:31871141") Annotation(oboInOwl:hasSynonymType obo:OMO_0003000) oboInOwl:hasRelatedSynonym obo:CL_9900001 "FCP")
+AnnotationAssertion(rdfs:label obo:CL_9900001 "fibrochondrocyte progenitor cell")
+EquivalentClasses(obo:CL_9900001 ObjectIntersectionOf(obo:CL_0008019 obo:CL_0011026 ObjectSomeValuesFrom(obo:BFO_0000050 obo:UBERON_0001995) ObjectSomeValuesFrom(obo:RO_0002292 obo:PR_000001127) ObjectSomeValuesFrom(obo:RO_0002292 obo:PR_000003264) ObjectSomeValuesFrom(obo:RO_0002292 obo:PR_000003328) ObjectSomeValuesFrom(obo:RO_0002292 obo:PR_Q15746)))
+SubClassOf(obo:CL_9900001 ObjectSomeValuesFrom(obo:RO_0002162 obo:NCBITaxon_9606))
+
 # Class: obo:CP_0000000 (obsolete CP:0000000)
 
 AnnotationAssertion(obo:IAO_0100001 obo:CP_0000000 obo:CL_0017500)
@@ -35464,4 +35477,4 @@ SubClassOf(ObjectIntersectionOf(obo:CL_0000163 ObjectSomeValuesFrom(obo:BFO_0000
 SubClassOf(ObjectIntersectionOf(obo:CL_0000163 ObjectSomeValuesFrom(obo:BFO_0000050 obo:UBERON_0000945)) obo:CL_0000164)
 SubClassOf(ObjectIntersectionOf(obo:CL_0000163 ObjectSomeValuesFrom(obo:BFO_0000050 obo:UBERON_0001264)) obo:CL_0000164)
 SubClassOf(Annotation(oboInOwl:hasDbXref <https://github.com/obophenotype/cell-ontology/issues/757>) ObjectIntersectionOf(obo:CL_0000540 ObjectSomeValuesFrom(obo:RO_0002162 obo:NCBITaxon_7742)) ObjectSomeValuesFrom(obo:RO_0002202 obo:CL_0000031))
-)
\ No newline at end of file
+)

```
