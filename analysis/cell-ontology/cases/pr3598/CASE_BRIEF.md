---
ontology: cell-ontology
repo: obophenotype/cell-ontology
issue_number: 3597
pr_number: 3598
issue_title: '[NTR] Add mouth terms for HubMap'
pr_author: app/copilot-swe-agent
pr_merged_at: '2026-03-26'
task_type: new_term
difficulty: hard
scoping: loosely_scoped
scope: multi_term
review_outcome: approved_first_time
num_agent_attempts: 3
generated_at: '2026-05-15'
domain_area: oral
best_f1: 0.697
best_model: claude-haiku-4.5
---

# PR #3598 — [NTR] Add mouth terms for HubMap

**cell-ontology** | [obophenotype/cell-ontology](https://github.com/obophenotype/cell-ontology) | [Issue #3597](https://github.com/obophenotype/cell-ontology/issues/3597) | [PR #3598](https://github.com/obophenotype/cell-ontology/pull/3598) | @app/copilot-swe-agent | merged 2026-03-26

`new_term` `hard` `loosely_scoped` `approved_first_time`

## Context

The HuBMAP consortium requested cell type terms for oral and salivary gland tissue annotation as part of the broader HuBMAP term request effort (#3471). Issue #3597 specified 8 new cell types including serous demilune cells, basal duct cells, periductal fibroblasts, junctional epithelial cells, tuft cells of specific glands, ionocytes, and myoepithelial cells of salivary glands. Each requires specific anatomical contextualization within oral and salivary gland structures.

## Changes Made

Added 113 new lines to `cl-edit.owl` defining 8 new cell types. Each term follows the standard compositional pattern with EquivalentClasses axioms using intersectionOf with a parent cell type and part_of an UBERON anatomical structure. Terms include capability axioms (capable_of GO processes like saliva secretion, ion homeostasis, smooth muscle contraction) and synonym annotations with PMID cross-references as specified in the issue.

## Resolution

Approved on first review in just 3 commits, reflecting efficient implementation. Hard difficulty because the 8 terms span diverse parent cell types (epithelial cells, fibroblasts, ionocytes, myoepithelial cells) each requiring different axiom patterns, and the salivary gland anatomy involves specific UBERON structures (parotid, sublingual, submandibular) that must be correctly referenced.

## Human Diff

```diff
diff --git a/src/ontology/cl-edit.owl b/src/ontology/cl-edit.owl
index 0837f612e..f42efb759 100644
--- a/src/ontology/cl-edit.owl
+++ b/src/ontology/cl-edit.owl
@@ -3323,6 +3323,14 @@ Declaration(Class(obo:CL_7770003))
 Declaration(Class(obo:CL_7770004))
 Declaration(Class(obo:CL_7770005))
 Declaration(Class(obo:CL_7770006))
+Declaration(Class(obo:CL_9900001))
+Declaration(Class(obo:CL_9900002))
+Declaration(Class(obo:CL_9900003))
+Declaration(Class(obo:CL_9900004))
+Declaration(Class(obo:CL_9900005))
+Declaration(Class(obo:CL_9900006))
+Declaration(Class(obo:CL_9900007))
+Declaration(Class(obo:CL_9900008))
 Declaration(Class(obo:CP_0000000))
 Declaration(Class(obo:CP_0000025))
 Declaration(Class(obo:CP_0000027))
@@ -35929,6 +35937,111 @@ SubClassOf(obo:CL_7770006 obo:CL_0002367)
 SubClassOf(obo:CL_7770006 ObjectSomeValuesFrom(obo:RO_0002162 obo:NCBITaxon_9606))
 SubClassOf(obo:CL_7770006 ObjectSomeValuesFrom(obo:RO_0002292 obo:PR_Q9UIK5))
 
+# Class: obo:CL_9900001 (serous demilune cell of salivary gland)
+
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:23209333") Annotation(oboInOwl:hasDbXref "PMID:41686279") obo:IAO_0000115 obo:CL_9900001 "A serous secreting cell that is part of a salivary gland, forming crescent-shaped (demilune) caps at the distal ends of mucous acini in mixed glands. Prominent in human submandibular and sublingual glands, this cell delivers its watery, enzyme-rich secretions including alpha-amylase through intercellular canaliculi that run between adjacent mucous cells to reach the acinar lumen (Amano et al., 2012). In rodents, these cells also express neuronal nitric oxide synthase (nNOS).")
+AnnotationAssertion(obo:IAO_0000233 obo:CL_9900001 <https://github.com/obophenotype/cell-ontology/issues/3597>)
+AnnotationAssertion(terms:contributor obo:CL_9900001 <https://orcid.org/0000-0002-5507-2103>)
+AnnotationAssertion(terms:date obo:CL_9900001 "2026-03-24T10:46:30Z"^^xsd:dateTime)
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:23209333") oboInOwl:hasExactSynonym obo:CL_9900001 "serous demilune cell")
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "https://en.wikipedia.org/wiki/Serous_demilune") oboInOwl:hasRelatedSynonym obo:CL_9900001 "Crescents of Giannuzzi")
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:23209333") oboInOwl:hasRelatedSynonym obo:CL_9900001 "demilune cell of salivary gland")
+AnnotationAssertion(oboInOwl:hasRelatedSynonym obo:CL_9900001 "serous crescent cell")
+AnnotationAssertion(rdfs:comment obo:CL_9900001 "The classic crescent-shaped morphology that gives demilune cells their name is a well-established histological feature, but must be caveated with the fixation artifact issue. Amano et al. (2012) describe how rapid-freeze fixation reveals a more tubular arrangement, suggesting the demilune shape is at least partly artifactual.")
+AnnotationAssertion(rdfs:label obo:CL_9900001 "serous demilune cell of salivary gland")
+EquivalentClasses(obo:CL_9900001 ObjectIntersectionOf(obo:CL_0000313 ObjectSomeValuesFrom(obo:BFO_0000050 obo:UBERON_0001044)))
+SubClassOf(obo:CL_9900001 obo:CL_0000313)
+SubClassOf(obo:CL_9900001 ObjectSomeValuesFrom(obo:RO_0002215 obo:GO_0046541))
+
+# Class: obo:CL_9900002 (basal duct cell of salivary gland)
+
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:37446355") Annotation(oboInOwl:hasDbXref "PMID:39346911") obo:IAO_0000115 obo:CL_9900002 "A basal cell that is part of the duct of a salivary gland, characterized by an undifferentiated phenotype, expression of KRT5, and a position surrounding the striated ductal epithelium. This cell is presumed to function as a salivary gland stem/progenitor cell capable of regenerating ductal and potentially acinar cell populations (Yura and Hamada, 2023). In mice, Lgr5-expressing cells within this compartment demonstrate tripotent capacity, able to generate acinar, ductal, and myoepithelial cell lineages.")
+AnnotationAssertion(obo:IAO_0000233 obo:CL_9900002 <https://github.com/obophenotype/cell-ontology/issues/3597>)
+AnnotationAssertion(terms:contributor obo:CL_9900002 <https://orcid.org/0000-0002-5507-2103>)
+AnnotationAssertion(terms:date obo:CL_9900002 "2026-03-24T10:46:30Z"^^xsd:dateTime)
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:37446355") oboInOwl:hasExactSynonym obo:CL_9900002 "basal ductal cell of salivary gland")
+AnnotationAssertion(rdfs:label obo:CL_9900002 "basal duct cell of salivary gland")
+SubClassOf(obo:CL_9900002 obo:CL_0000646)
+SubClassOf(obo:CL_9900002 ObjectSomeValuesFrom(obo:BFO_0000050 obo:UBERON_0001837))
+
+# Class: obo:CL_9900003 (periductal fibroblast of salivary gland)
+
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:31213547") Annotation(oboInOwl:hasDbXref "PMID:39346911") Annotation(oboInOwl:hasDbXref "PMID:41411773") obo:IAO_0000115 obo:CL_9900003 "A fibroblast that is part of the stroma of a salivary gland, positioned in the periductal connective tissue surrounding the ductal system. This cell maintains the extracellular matrix framework around salivary gland ducts and participates in immunomodulatory signaling. In the context of Sjögren's syndrome, periductal fibroblasts respond to IL-13 stimulation by upregulating VCAM-1, PDPN, and ICAM-1, contributing to the formation of tertiary lymphoid structures (Nayar et al., 2019).")
+AnnotationAssertion(obo:IAO_0000233 obo:CL_9900003 <https://github.com/obophenotype/cell-ontology/issues/3597>)
+AnnotationAssertion(terms:contributor obo:CL_9900003 <https://orcid.org/0000-0002-5507-2103>)
+AnnotationAssertion(terms:date obo:CL_9900003 "2026-03-24T10:46:30Z"^^xsd:dateTime)
+AnnotationAssertion(oboInOwl:hasBroadSynonym obo:CL_9900003 "salivary gland fibroblast")
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:31213547") oboInOwl:hasRelatedSynonym obo:CL_9900003 "immunofibroblast of salivary gland")
+AnnotationAssertion(rdfs:label obo:CL_9900003 "periductal fibroblast of salivary gland")
+SubClassOf(obo:CL_9900003 obo:CL_0000057)
+SubClassOf(obo:CL_9900003 ObjectSomeValuesFrom(obo:BFO_0000050 obo:UBERON_0001044))
+
+# Class: obo:CL_9900004 (junctional epithelial cell)
+
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:39590534") Annotation(oboInOwl:hasDbXref "PMID:40723411") Annotation(oboInOwl:hasDbXref "PMID:41143768") Annotation(oboInOwl:hasDbXref "PMID:41331699") obo:IAO_0000115 obo:CL_9900004 "An epithelial cell that is part of the junctional epithelium of the gingiva, forming a collar-like band around the cervix of the tooth. This cell attaches to the tooth surface via hemidesmosomes and an internal basal lamina rich in laminin-332 and ODAM (Gavriiloglou et al., 2024). The junctional epithelium is a stratified squamous non-keratinized epithelium ranging from 15-30 cell layers coronally to 1-3 cell layers apically. This cell expresses cytokeratin 19 (CK19) as a specific marker, along with ODAM and FDC-SP, and participates in innate immune defense by producing IL-8, IL-1alpha, and MMP-7, facilitating the transmigration of polymorphonuclear leukocytes through the epithelium (Gavriiloglou et al., 2024). This cell has a high turnover rate, with complete renewal occurring every 4-6 days (Lin et al., 2025), and develops from the reduced enamel epithelium during tooth eruption, although it can regenerate de novo without this precursor.")
+AnnotationAssertion(obo:IAO_0000233 obo:CL_9900004 <https://github.com/obophenotype/cell-ontology/issues/3597>)
+AnnotationAssertion(terms:contributor obo:CL_9900004 <https://orcid.org/0000-0002-5507-2103>)
+AnnotationAssertion(terms:date obo:CL_9900004 "2026-03-24T10:46:30Z"^^xsd:dateTime)
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:14756251") Annotation(oboInOwl:hasDbXref "PMID:39590534") Annotation(oboInOwl:hasDbXref "PMID:40723411") Annotation(oboInOwl:hasSynonymType obo:OMO_0003000) oboInOwl:hasExactSynonym obo:CL_9900004 "JE cell")
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:18973537") oboInOwl:hasExactSynonym obo:CL_9900004 "cell of junctional epithelium")
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:2480439") Annotation(oboInOwl:hasDbXref "PMID:7814753") Annotation(oboInOwl:hasSynonymType obo:OMO_0003000) oboInOwl:hasNarrowSynonym obo:CL_9900004 "DAT cell")
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:19646321") oboInOwl:hasRelatedSynonym obo:CL_9900004 "gingival junctional epithelial cell")
+AnnotationAssertion(rdfs:label obo:CL_9900004 "junctional epithelial cell")
+SubClassOf(obo:CL_9900004 obo:CL_0002077)
+SubClassOf(obo:CL_9900004 ObjectSomeValuesFrom(obo:BFO_0000050 obo:UBERON_0001949))
+SubClassOf(obo:CL_9900004 ObjectSomeValuesFrom(obo:RO_0002215 obo:GO_0002227))
+
+# Class: obo:CL_9900005 (tuft cell of parotid gland)
+
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:23209333") Annotation(oboInOwl:hasDbXref "PMID:35993302") Annotation(oboInOwl:hasDbXref "PMID:38098741") Annotation(oboInOwl:hasDbXref "PMID:38358561") obo:IAO_0000115 obo:CL_9900005 "A tuft cell that is part of the epithelium of the parotid gland, localized to the striated ducts and never observed in acini. This cell is characterized by expression of POU2F3 and is expected to possess chemosensory function consistent with tuft cells in other tissues. Immunohistochemical analysis of normal human parotid gland tissue detected POU2F3-positive cells as a very rare population within the ductal compartment, positioned on the luminal side (Hoki et al., 2024).")
+AnnotationAssertion(obo:IAO_0000233 obo:CL_9900005 <https://github.com/obophenotype/cell-ontology/issues/3597>)
+AnnotationAssertion(terms:contributor obo:CL_9900005 <https://orcid.org/0000-0002-5507-2103>)
+AnnotationAssertion(terms:date obo:CL_9900005 "2026-03-24T10:46:30Z"^^xsd:dateTime)
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:3284416") Annotation(oboInOwl:hasDbXref "PMID:38358561") oboInOwl:hasExactSynonym obo:CL_9900005 "parotid gland tuft cell")
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:18062147") Annotation(oboInOwl:hasDbXref "PMID:23209333") oboInOwl:hasRelatedSynonym obo:CL_9900005 "brush cell of parotid gland")
+AnnotationAssertion(rdfs:label obo:CL_9900005 "tuft cell of parotid gland")
+EquivalentClasses(obo:CL_9900005 ObjectIntersectionOf(obo:CL_0002204 ObjectSomeValuesFrom(obo:BFO_0000050 obo:UBERON_0001831)))
+SubClassOf(obo:CL_9900005 obo:CL_0002204)
+SubClassOf(obo:CL_9900005 ObjectSomeValuesFrom(obo:BFO_0000050 obo:UBERON_0001831))
+
+# Class: obo:CL_9900006 (tuft cell of sublingual gland)
+
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:23209333") Annotation(oboInOwl:hasDbXref "PMID:38358561") obo:IAO_0000115 obo:CL_9900006 "A tuft cell that is part of the epithelium of the sublingual gland, localized to the ductal compartment. This cell is characterized by expression of POU2F3, consistent with tuft cell identity. Immunohistochemical analysis detected POU2F3-positive cells in normal human sublingual gland tissue (Hoki et al., 2024).")
+AnnotationAssertion(obo:IAO_0000233 obo:CL_9900006 <https://github.com/obophenotype/cell-ontology/issues/3597>)
+AnnotationAssertion(terms:contributor obo:CL_9900006 <https://orcid.org/0000-0002-5507-2103>)
+AnnotationAssertion(terms:date obo:CL_9900006 "2026-03-24T10:46:30Z"^^xsd:dateTime)
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:38358561") Annotation(oboInOwl:hasDbXref "PMID:8874101") oboInOwl:hasExactSynonym obo:CL_9900006 "sublingual gland tuft cell")
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:18062147") Annotation(oboInOwl:hasDbXref "PMID:23209333") oboInOwl:hasRelatedSynonym obo:CL_9900006 "brush cell of sublingual gland")
+AnnotationAssertion(rdfs:label obo:CL_9900006 "tuft cell of sublingual gland")
+EquivalentClasses(obo:CL_9900006 ObjectIntersectionOf(obo:CL_0002204 ObjectSomeValuesFrom(obo:BFO_0000050 obo:UBERON_0001832)))
+SubClassOf(obo:CL_9900006 obo:CL_0002204)
+SubClassOf(obo:CL_9900006 obo:CL_0002251)
+
+# Class: obo:CL_9900007 (ionocyte of salivary gland)
+
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:30069044") Annotation(oboInOwl:hasDbXref "PMID:30069046") Annotation(oboInOwl:hasDbXref "PMID:38358561") Annotation(oboInOwl:hasDbXref "PMID:39346911") Annotation(oboInOwl:hasDbXref "PMID:41721487") obo:IAO_0000115 obo:CL_9900007 "An ionocyte that is part of a salivary gland, localized to the ductal compartment on the luminal side. This specialized epithelial cell is characterized by expression of FOXI1 and is involved in regulating and maintaining osmotic pressure within the glandular environment (Dong et al., 2024). In normal human salivary glands, FOXI1-positive cells constitute less than 5% of ductal epithelial cells and are found exclusively in ducts, never in acini, across all major gland types including parotid, submandibular, sublingual, and minor salivary glands (Hoki et al., 2024). Like ionocytes in other tissues, this cell is expected to express high levels of CFTR and possess abundant mitochondria and ion transporters.")
+AnnotationAssertion(obo:IAO_0000233 obo:CL_9900007 <https://github.com/obophenotype/cell-ontology/issues/3597>)
+AnnotationAssertion(terms:contributor obo:CL_9900007 <https://orcid.org/0000-0002-5507-2103>)
+AnnotationAssertion(terms:date obo:CL_9900007 "2026-03-24T10:46:30Z"^^xsd:dateTime)
+AnnotationAssertion(rdfs:label obo:CL_9900007 "ionocyte of salivary gland")
+EquivalentClasses(obo:CL_9900007 ObjectIntersectionOf(obo:CL_0005006 ObjectSomeValuesFrom(obo:BFO_0000050 obo:UBERON_0001044)))
+SubClassOf(obo:CL_9900007 obo:CL_0005006)
+SubClassOf(obo:CL_9900007 ObjectSomeValuesFrom(obo:RO_0002215 obo:GO_0050801))
+
+# Class: obo:CL_9900008 (myoepithelial cell of salivary gland)
+
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:23209333") Annotation(oboInOwl:hasDbXref "PMID:39346911") Annotation(oboInOwl:hasDbXref "PMID:40837863") Annotation(oboInOwl:hasDbXref "PMID:41271704") obo:IAO_0000115 obo:CL_9900008 "A myoepithelial cell that is part of a salivary gland, positioned between the basal lamina and the secretory or ductal epithelial cells surrounding acini and intercalated ducts. This cell adopts a stellate morphology with four to eight cellular processes around acini and an elongated form parallel to the ductal axis around intercalated ducts (Amano et al., 2012). It expresses alpha-smooth muscle actin (ACTA2/alpha-SMA) as a primary marker, along with p63 and aquaporin 1 (AQP1), and contracts rhythmically in response to neural stimulation to facilitate saliva expulsion from secretory acini into the ductal system (Amano et al., 2012). This cell also produces FGF7, which activates FGFR2b-dependent transcriptional programs essential for seromucous acinar cell differentiation (Aure et al., 2023). In mice, myoepithelial cells express SOX2 and possess regenerative capacity, contributing to acinar cell restoration during tissue repair after severe injury.")
+AnnotationAssertion(obo:IAO_0000233 obo:CL_9900008 <https://github.com/obophenotype/cell-ontology/issues/3597>)
+AnnotationAssertion(terms:contributor obo:CL_9900008 <https://orcid.org/0000-0002-5507-2103>)
+AnnotationAssertion(terms:date obo:CL_9900008 "2026-03-24T10:46:30Z"^^xsd:dateTime)
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:23209333") Annotation(oboInOwl:hasDbXref "PMID:39346911") Annotation(oboInOwl:hasDbXref "PMID:8155903") oboInOwl:hasExactSynonym obo:CL_9900008 "salivary gland myoepithelial cell")
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:40837863") oboInOwl:hasExactSynonym obo:CL_9900008 "salivary myoepithelial cell")
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:26015726") Annotation(oboInOwl:hasDbXref "PMID:27721614") Annotation(oboInOwl:hasDbXref "PMID:38273256") oboInOwl:hasRelatedSynonym obo:CL_9900008 "basket cell of salivary gland")
+AnnotationAssertion(rdfs:label obo:CL_9900008 "myoepithelial cell of salivary gland")
+EquivalentClasses(obo:CL_9900008 ObjectIntersectionOf(obo:CL_0000185 ObjectSomeValuesFrom(obo:BFO_0000050 obo:UBERON_0001044)))
+SubClassOf(obo:CL_9900008 obo:CL_0000185)
+SubClassOf(obo:CL_9900008 ObjectSomeValuesFrom(obo:RO_0002215 obo:GO_0006939))
+
 # Class: obo:CP_0000000 (obsolete CP:0000000)
 
 AnnotationAssertion(obo:IAO_0100001 obo:CP_0000000 obo:CL_0017500)

```

## Agent Attempts (3)

| # | Model | Runtime | F1 | P | R | Blob | Eval PR | Detail |
|---|-------|---------|-----|-----|-----|------|---------|--------|
| 1 | claude-haiku-4.5 | claude | 0.697 | 0.654 | 0.746 | `7e99c53` | [#233](https://github.com/ai4curation/eval-ont-agent-cl/pull/233) | [attempt](attempts/pr233.md) |
| 2 | claude-sonnet-4.5 | claude | 0.091 | 0.086 | 0.096 | `eec23b5` | [#213](https://github.com/ai4curation/eval-ont-agent-cl/pull/213) | [attempt](attempts/pr213.md) |
| 3 | claude-opus-4.7 | claude | 0.086 | 0.086 | 0.085 | `e7629bf` | [#196](https://github.com/ai4curation/eval-ont-agent-cl/pull/196) | [attempt](attempts/pr196.md) |
