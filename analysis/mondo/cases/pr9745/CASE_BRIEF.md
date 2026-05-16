---
ontology: mondo
repo: monarch-initiative/mondo
issue_number: 9707
pr_number: 9745
issue_title: Mondo request for SCN5A disease entity for ClinGen
pr_author: katiermullen
pr_merged_at: '2025-11-12'
task_type: new_term
difficulty: hard
scoping: tightly_scoped
scope: multi_term
review_outcome: approved_first_time
num_agent_attempts: 11
generated_at: '2026-05-15'
scoping_notes: Adds two new terms and reclassifies a related existing term.
domain_area: cardiac-disease
best_f1: 0.615
best_model: kimi-k2.6
---

# PR #9745 — Mondo request for SCN5A disease entity for ClinGen

**mondo** | [monarch-initiative/mondo](https://github.com/monarch-initiative/mondo) | [Issue #9707](https://github.com/monarch-initiative/mondo/issues/9707) | [PR #9745](https://github.com/monarch-initiative/mondo/pull/9745) | @katiermullen | merged 2025-11-12

`new_term` `hard` `tightly_scoped` `approved_first_time`

## Context

ClinGen requested new SCN5A-related disease entities for their gene curation workflow. SCN5A encodes a sodium channel subunit critical for cardiac conduction, and mutations cause a spectrum of cardiac rhythm disorders including Brugada syndrome, long QT syndrome type 3, and conduction defects. The request required creating two new gene-disease terms and adding child terms as specified in the detailed issue discussion.

Additionally, the existing term "atrioventricular dissociation" needed reclassification from its hereditary parent to "cardiac conduction defect" because the condition is not necessarily hereditary.

## Changes Made

Added two new SCN5A-related disease terms to `src/ontology/mondo-edit.obo` with associated child terms (40 additions), and reclassified "atrioventricular dissociation" by updating its parent (1 deletion to remove the old parent). The 2 commits reflect the new term additions and the parent reclassification as separate logical changes.

## Resolution

Hard difficulty because the PR involves multiple coordinated changes: creating two new gene-disease terms, adding their children, and correcting the classification of an existing term. An agent would need to understand the SCN5A channelopathy spectrum, determine correct parent classes for each new term, and recognize that the existing atrioventricular dissociation term was incorrectly classified as hereditary.

## Human Diff

```diff
diff --git a/src/ontology/mondo-edit.obo b/src/ontology/mondo-edit.obo
index f26e3f70a0..31deccd70c 100644
--- a/src/ontology/mondo-edit.obo
+++ b/src/ontology/mondo-edit.obo
@@ -5867,6 +5867,7 @@ xref: Orphanet:51083 {source="MONDO:equivalentTo", source="OMIM:609620"}
 xref: SCTID:698272007 {source="MONDO:equivalentTo"}
 xref: UMLS:C2348199 {source="MONDO:equivalentTo", source="MONDO:MEDGEN", source="MEDGEN:378835"}
 is_a: MONDO:0000992 {source="DOID:0050793"} ! heart conduction disease
+is_a: MONDO:1010180 {source="https://www.clinicalgenome.org/affiliation/40104/"} ! cardiogenetic rhythm disorder
 relationship: curated_content_resource https://search.clinicalgenome.org/kb/conditions/MONDO:0000453 {source="MONDO:CLINGEN"}
 relationship: has_characteristic MONDO:0021152 {source="OMIMPS:609620"} ! inherited
 property_value: curated_content_resource "https://www.malacards.org/card/familial_short_qt_syndrome" xsd:anyURI {source="MONDO:MalaCards"}
@@ -188782,6 +188783,7 @@ xref: OMIM:192605 {source="MONDO:equivalentTo"}
 xref: SCTID:233906007 {source="MONDO:equivalentTo"}
 xref: UMLS:C0340485 {source="MONDO:equivalentTo", source="MONDO:MEDGEN", source="MEDGEN:83309"}
 is_a: MONDO:0005477 {source="MONDO:Redundant", source="OMIM:192605"} ! ventricular tachycardia
+is_a: MONDO:1010180 {source="https://www.clinicalgenome.org/affiliation/40104/"} ! cardiogenetic rhythm disorder
 intersection_of: MONDO:0005477 ! ventricular tachycardia
 intersection_of: has_characteristic MONDO:0021152 ! inherited
 relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/4385 {source="OMIM:192605"} ! GNAI2
@@ -194742,7 +194744,10 @@ xref: MESH:D006327 {source="MONDO:equivalentTo"}
 xref: OMIM:209600 {source="MONDO:equivalentTo"}
 xref: SCTID:50799005 {source="MONDO:equivalentTo"}
 xref: UMLS:C0004331 {source="MEDGEN:2496", source="MONDO:equivalentTo", source="MONDO:MEDGEN"}
-is_a: MONDO:0003847 {source="https://orcid.org/0000-0001-5208-3432"} ! hereditary disease
+is_a: MONDO:0100042 {source="https://www.ncbi.nlm.nih.gov/books/NBK563205/"} ! cardiac conduction defect
+relationship: excluded_from_qc_check http://purl.obolibrary.org/obo/mondo/sparql/qc/general/qc-single-child.sparql
+relationship: excluded_from_qc_check http://purl.obolibrary.org/obo/mondo/sparql/qc/mondo/qc-omim-subsumption.sparql
+relationship: excluded_subClassOf MONDO:0003847 {source="https://orcid.org/0000-0001-5208-3432", source="https://orcid.org/0000-0002-5002-8648"} ! hereditary disease
 property_value: curated_content_resource "https://www.malacards.org/card/atrioventricular_dissociation" xsd:anyURI {source="MONDO:MalaCards"}
 property_value: IAO:0000589 "atrioventricular dissociation (disease)" xsd:string
 
@@ -257842,6 +257847,7 @@ xref: OMIM:601144 {source="DOID:0110218", source="MONDO:equivalentTo"}
 xref: Orphanet:130 {source="OMIM:601144"}
 xref: UMLS:C4551804 {source="MONDO:equivalentTo", source="MONDO:MEDGEN", source="MEDGEN:1646402"}
 is_a: MONDO:0015263 {source="DC-OMIM:601144", source="DOID:0110218", source="MONDO:Redundant", source="OMIM:601144"} ! Brugada syndrome
+is_a: MONDO:1010181 {source="https://www.clinicalgenome.org/affiliation/40104/"} ! SCN5A-related cardiac rhythm disorder
 intersection_of: MONDO:0015263 ! Brugada syndrome
 intersection_of: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/10593 ! SCN5A
 relationship: curated_content_resource https://search.clinicalgenome.org/kb/conditions/MONDO:0011001 {source="MONDO:CLINGEN"}
@@ -267530,6 +267536,7 @@ xref: Orphanet:228140 {source="OMIM:603829"}
 xref: SCTID:233915000 {source="MONDO:equivalentTo"}
 xref: UMLS:C2751898 {source="MEDGEN:414502", source="MONDO:equivalentTo", source="MONDO:MEDGEN"}
 is_a: MONDO:0100234 {source="DC-OMIM:603829", source="MESH:C567851"} ! paroxysmal familial ventricular fibrillation
+is_a: MONDO:1010181 {source="https://www.clinicalgenome.org/affiliation/40104/"} ! SCN5A-related cardiac rhythm disorder
 intersection_of: MONDO:0100234 ! paroxysmal familial ventricular fibrillation
 intersection_of: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/10593 ! SCN5A
 relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/10593 {source="OMIM:603829"} ! SCN5A
@@ -267562,6 +267569,7 @@ xref: Orphanet:101016 {source="OMIM:603830", source="MONDO:directSiblingOf"}
 xref: Orphanet:768 {source="OMIM:603830"}
 xref: UMLS:C1859062 {source="MONDO:equivalentTo", source="MONDO:MEDGEN", source="MEDGEN:349087"}
 is_a: MONDO:0019171 {source="OMIM:603830", source="Orphanet:101016-prototype"} ! familial long QT syndrome
+is_a: MONDO:1010181 {source="https://www.clinicalgenome.org/affiliation/40104/"} ! SCN5A-related cardiac rhythm disorder
 intersection_of: MONDO:0019171 ! familial long QT syndrome
 intersection_of: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/10593 ! SCN5A
 relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/10593 {source="OMIM:603830"} ! SCN5A
@@ -285573,6 +285581,7 @@ xref: Orphanet:166282 {source="MONDO:equivalentTo", source="OMIM:608567"}
 xref: SCTID:233913007 {source="MONDO:equivalentTo"}
 xref: UMLS:C0340491 {source="MONDO:equivalentTo", source="MONDO:MEDGEN", source="MEDGEN:573766"}
 is_a: MONDO:0001823 {source="DC-OMIM:608567", source="MESH:C563907", source="MONDO:Redundant", source="OMIM:608567"} ! sick sinus syndrome
+is_a: MONDO:1010180 {source="https://www.clinicalgenome.org/affiliation/40104/"} ! cardiogenetic rhythm disorder
 intersection_of: MONDO:0001823 ! sick sinus syndrome
 intersection_of: has_characteristic MONDO:0021152 ! inherited
 relationship: has_characteristic MONDO:0021152 {source="OMIMPS:608567"} ! inherited
@@ -323947,6 +323956,7 @@ xref: OMIM:614022 {source="MONDO:equivalentTo"}
 xref: Orphanet:334 {source="OMIM:614022"}
 xref: UMLS:C3151464 {source="MEDGEN:462814", source="MONDO:equivalentTo", source="MONDO:MEDGEN"}
 is_a: MONDO:0018054 {source="DC-OMIM:614022", source="MONDO:Redundant", source="OMIM:614022"} ! familial atrial fibrillation
+is_a: MONDO:1010181 {source="https://www.clinicalgenome.org/affiliation/40104/"} ! SCN5A-related cardiac rhythm disorder
 intersection_of: MONDO:0018054 ! familial atrial fibrillation
 intersection_of: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/10593 ! SCN5A
 relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/10593 {source="OMIM:614022"} ! SCN5A
@@ -349659,6 +349669,7 @@ xref: OMIM:616117 {source="Orphanet:436242/e", source="EFO:0005304", source="MON
 xref: Orphanet:436242 {source="MONDO:equivalentTo"}
 xref: UMLS:C4015285 {source="MEDGEN:863722", source="MONDO:equivalentTo", source="MONDO:MEDGEN"}
 is_a: MONDO:0005449 {source="EFO:0005304"} ! conduction system disorder
+is_a: MONDO:1010180 {source="https://www.clinicalgenome.org/affiliation/40104/"} ! cardiogenetic rhythm disorder
 relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/19661 {source="OMIM:616117"} ! TNNI3K
 property_value: curated_content_resource "https://www.malacards.org/card/cardiac_conduction_disease_with_or_without_dilated_cardiomyopathy" xsd:anyURI {source="MONDO:MalaCards"}
 
@@ -367967,6 +367978,7 @@ xref: SCTID:418818005 {source="DOID:0050451", source="MONDO:equivalentTo"}
 xref: UMLS:C1142166 {source="MONDO:equivalentTo", source="MONDO:MEDGEN", source="MEDGEN:222975"}
 is_a: MONDO:0000992 {source="DOID:0050451", source="MONDO:Redundant", source="MONDO:indirect"} ! heart conduction disease
 is_a: MONDO:0002254 {source="NCIT:C142891"} ! syndromic disease
+is_a: MONDO:1010180 {source="https://www.clinicalgenome.org/affiliation/40104/"} ! cardiogenetic rhythm disorder
 relationship: curated_content_resource https://search.clinicalgenome.org/kb/conditions/MONDO:0015263 {source="MONDO:CLINGEN"}
 relationship: has_characteristic MONDO:0021152 {source="OMIMPS:601144"} ! inherited
 property_value: curated_content_resource "https://www.malacards.org/card/brugada_syndrome" xsd:anyURI {source="MONDO:MalaCards"}
@@ -426972,6 +426984,7 @@ xref: Orphanet:334 {source="DOID:0050650", source="MONDO:equivalentTo"}
 xref: SCTID:715395008 {source="MONDO:equivalentTo"}
 xref: UMLS:C3468561 {source="MONDO:equivalentTo", source="MONDO:MEDGEN", source="MEDGEN:894635"}
 is_a: MONDO:0004981 {source="DOID:0050650", source="MONDO:DOID", source="MONDO:Redundant"} ! atrial fibrillation
+is_a: MONDO:1010180 {source="https://www.clinicalgenome.org/affiliation/40104/"} ! cardiogenetic rhythm disorder
 intersection_of: MONDO:0004981 ! atrial fibrillation
 intersection_of: has_characteristic MONDO:0021152 ! inherited
 relationship: has_characteristic MONDO:0021152 {source="OMIMPS:608583"} ! inherited
@@ -460880,6 +460893,7 @@ xref: Orphanet:871 {source="MONDO:equivalentTo", source="DOID:0111073"}
 xref: SCTID:698249005 {source="MONDO:equivalentTo"}
 xref: SCTID:93130009 {source="MONDO:equivalentObsolete"}
 is_a: MONDO:0000992 {source="DOID:0111073", source="MONDO:indirect"} ! heart conduction disease
+is_a: MONDO:1010180 {source="https://www.clinicalgenome.org/affiliation/40104/"} ! cardiogenetic rhythm disorder
 relationship: has_characteristic MONDO:0021152 {source="OMIMPS:113900"} ! inherited
 property_value: curated_content_resource "https://www.malacards.org/card/familial_progressive_cardiac_conduction_defect" xsd:anyURI {source="MONDO:MalaCards"}
 property_value: curated_content_resource "https://www.malacards.org/card/progressive_familial_heart_block" xsd:anyURI {source="MONDO:MalaCards"}
@@ -513327,6 +513341,7 @@ xref: OMIM:608567 {source="MONDO:equivalentTo"}
 xref: Orphanet:166282 {source="OMIM:608567"}
 xref: UMLS:C1837845 {source="MONDO:equivalentTo", source="MONDO:MEDGEN", source="MEDGEN:325270"}
 is_a: MONDO:0012061 {source="MONDO:0024562/inferred", source="MONDO:Redundant", source="OMIM:608567"} ! familial sick sinus syndrome
+is_a: MONDO:1010181 {source="https://www.clinicalgenome.org/affiliation/40104/"} ! SCN5A-related cardiac rhythm disorder
 intersection_of: MONDO:0012061 ! familial sick sinus syndrome
 intersection_of: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/10593 ! SCN5A
 relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/10593 {source="OMIM:608567"} ! SCN5A
@@ -561821,6 +561836,7 @@ xref: MEDGEN:83310 {source="MONDO:equivalentTo", source="MONDO:MEDGEN"}
 xref: Orphanet:228140 {source="MONDO:equivalentTo", source="OMIM:603829"}
 xref: UMLS:C0340493 {source="MEDGEN:83310", source="MONDO:equivalentTo", source="MONDO:MEDGEN"}
 is_a: MONDO:0000190 {source="https://orcid.org/0000-0001-5208-3432"} ! ventricular fibrillation
+is_a: MONDO:1010180 {source="https://www.clinicalgenome.org/affiliation/40104/"} ! cardiogenetic rhythm disorder
 property_value: curated_content_resource "https://www.malacards.org/card/paroxysmal_familial_ventricular_fibrillation" xsd:anyURI {source="MONDO:MalaCards"}
 property_value: http://purl.org/dc/terms/creator https://orcid.org/0000-0001-5208-3432
 property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/2524" xsd:anyURI
@@ -592442,6 +592458,29 @@ is_a: MONDO:0005015 {source="https://idf.org/about-diabetes/types-of-diabetes/ty
 property_value: http://purl.org/dc/terms/creator https://orcid.org/0000-0002-5002-8648
 property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9614" xsd:anyURI
 
+[Term]
+id: MONDO:1010180
+name: cardiogenetic rhythm disorder
+def: "Any cardiac rhythm disorder with a monogenic etiology that includes, but is not limited to, atrial fibrillation, sick sinus syndrome, progressive cardiac conduction disease, ventricular fibrillation, Brugada syndrome, long QT syndrome, short QT syndrome, tachycardia with fibrillation." [https://www.clinicalgenome.org/affiliation/40104/]
+synonym: "cardiogenetic rhythm disorder" EXACT [https://www.clinicalgenome.org/affiliation/40104/] {OMO:0002001="https://w3id.org/information-resource-registry/clingen"}
+is_a: MONDO:0007263 {source="https://www.clinicalgenome.org/affiliation/40104/"} ! cardiac rhythm disease
+is_a: MONDO:0100547 {source="https://www.clinicalgenome.org/affiliation/40104/"} ! cardiogenetic disease
+property_value: http://purl.org/dc/terms/creator https://orcid.org/0000-0002-5002-8648
+property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9707" xsd:anyURI
+
+[Term]
+id: MONDO:1010181
+name: SCN5A-related cardiac rhythm disorder
+def: "A heterogeneous collection of cardiac rhythm disorders caused by genetic variations in the SCN5A gene with autosomal dominant inheritance. Affected individuals are commonly reported to have unremarkable cardiac morphology and at least one cardiac rhythm phenotype that includes, but is not limited to, atrial fibrillation, sick sinus syndrome, progressive cardiac conduction disease, ventricular fibrillation, long QT syndrome, and Brugada syndrome." [https://www.clinicalgenome.org/affiliation/40104/]
+comment: Individuals with pathogenic variants in SCN5A may also exhibit overlapping or mixed cardiac rhythm phenotypes and intrafamilial variability.
+synonym: "SCN5A-related cardiac rhythm disorder" EXACT [https://www.clinicalgenome.org/affiliation/40104/] {OMO:0002001="https://w3id.org/information-resource-registry/clingen"}
+is_a: MONDO:1010180 {source="https://www.clinicalgenome.org/affiliation/40104/"} ! cardiogenetic rhythm disorder
+intersection_of: MONDO:1010180 ! cardiogenetic rhythm disorder
+intersection_of: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/10593 ! SCN5A
+relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/10593 {source="https://www.clinicalgenome.org/affiliation/40104/"} ! SCN5A
+property_value: http://purl.org/dc/terms/creator https://orcid.org/0000-0002-5002-8648
+property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9707" xsd:string
+
 [Term]
 id: MONDO:1010191
 name: deficiency of uridine monophosphate synthase, non-human animal

```

## Agent Attempts (11)

### Attempt 1: kimi-k2.6 / opencode

- **Eval PR**: [#261](https://github.com/ai4curation/eval-ont-agent-mondo/pull/261)
- **F1**: 0.615  **Precision**: 0.500  **Recall**: 0.800  **Jaccard**: 0.444
- **Trace**: [25755512671](https://github.com/ai4curation/eval-ont-agent-mondo/tree/master/traces/25755512671)
- **Workflow run**: [25755512671](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25755512671)

#### Agent PR Comment

PR Description: Add SCN5A-related cardiac rhythm disorder and cardiogenetic rhythm disorder terms

## Overview
This PR addresses monarch-initiative/mondo#9707, a request from the ClinGen Hereditary Cardiovascular Disease Gene Curation Expert Panel (GCEP) to create two new MONDO terms and reorganize existing cardiac rhythm disorder terms.

## Changes Made

### New Terms Created
1. **MONDO:7770003 - cardiogenetic rhythm disorder**
   - Parents: `cardiac rhythm disease` (MONDO:0007263), `cardiogenetic disease` (MONDO:0100547)
   - Definition: "A heterogeneous group of cardiac rhythm phenotypes with a monogenic etiology that include, but are not limited to, atrial fibrillation, sick sinus syndrome, progressive cardiac conduction disease, ventricular fibrillation, Brugada syndrome, long QT syndrome, short QT syndrome, tachycardia with fibrillation, etc."
   - Source: https://www.clinicalgenome.org/affiliation/40104/

2. **MONDO:7770004 - SCN5A-related cardiac rhythm disorder**
   - Parents: `cardiogenetic rhythm disorder` (MONDO:7770003), `cardiac rhythm disease` (MONDO:0007263), `cardiogenetic disease` (MONDO:0100547)
   - Definition: "A heterogeneous collection of cardiac rhythm disorders caused by genetic variation in the SCN5A gene with autosomal dominant inheritance. Affected individuals are commonly reported to have unremarkable cardiac morphology and at least one cardiac rhythm phenotype that includes, but is not limited to, atrial fibrillation, sick sinus syndrome, progressive cardiac conduction disease, ventricular fibrillation, long QT syndrome, and Brugada syndrome. Individuals with pathogenic variants in SCN5A may also exhibit overlapping or mixed cardiac rhythm phenotypes and intrafamilial variability."
   - Logical definition: `cardiac rhythm disease` AND `has_material_basis_in_germline_mutation_in` SCN5A (HGNC:10593)
   - Source: https://www.clinicalgenome.org/affiliation/40104/

### Existing Terms Reorganized (new is_a parents added, existing parents retained)

**Children of MONDO:7770004 (SCN5A-related cardiac rhythm disorder):**
- MONDO:0013530 - atrial fibrillation, familial, 10
- MONDO:0024562 - sick sinus syndrome 1
- MONDO:0011376 - ventricular fibrillation, paroxysmal familial, type 1
- MONDO:0011377 - long QT syndrome 3
- MONDO:0011001 - Brugada syndrome 1

**Children of MONDO:7770003 (cardiogenetic rhythm disorder):**
- MONDO:0014500 - atrial conduction disease
- MONDO:0015263 - Brugada syndrome
- MONDO:0018054 - familial atrial fibrillation
- MONDO:0012061 - familial sick sinus syndrome
- MONDO:0019490 - progressive familial heart block
- MONDO:0000453 - short QT syndrome
- MONDO:0008648 - ventricular tachycardia, familial
- MONDO:0011376 - ventricular fibrillation, paroxysmal familial, type 1

**Note:** atrioventricular block (MONDO:0000465) was explicitly excluded as a child of `cardiogenetic rhythm disorder` per curator feedback from @katiermullen, as this condition does not necessarily have a monogenic etiology.

### Definitions Used
The definitions were taken from the revised versions provided in the issue comments (removing "multifocal ectopic Purkinje-related premature contractions" as requested by the ClinGen submitter in a follow-up comment).

## Validation & Quality Control
- [x] Verified all referenced MONDO IDs exist in `mondo-edit.obo`
- [x] Verified HGNC ID for SCN5A (http://identifiers.org/hgnc/10593)
- [x] Checked out all 12 affected existing terms and 2 new terms via `obo-checkout.pl`
- [x] Added new `is_a` relationships without removing any existing parents
- [x] Syntax validated with `robot convert` (passed)
- [x] Normalized with ODK `make NORM` and moved to `mondo-edit.obo`
- [x] Logical consistency checked with `robot reason` using ELK reasoner - **no unsatisfiable classes found**
- [x] Checked that the new MONDO:777xxxx IDs do not clash with existing terms

## Rationale for Decisions
- **Monogenic requirement:** Only terms with established monogenic etiology were added as children of `cardiogenetic rhythm disorder`. This aligns with the term's definition and with @katiermullen's feedback about excluding atrioventricular block.
- **Logical definition for SCN5A term:** Used `intersection_of` with `cardiac rhythm disease` and `has_material_basis_in_germline_mutation_in SCN5A` to follow the `disease_series_by_gene` pattern established in MONDO, while also asserting dual `is_a` parents to capture the full semantic context (cardiogenetic disease lineage).
- **Plural vs singular naming:** Although the ClinGen request used "cardiogenetic rhythm disorders" (plural), the ontology term label uses singular "cardiogenetic rhythm disorder" to maintain consistency with MONDO conventions (e.g., "cardiogenetic disease", "cardiac rhythm disease").

## Files Changed
- `src/ontology/mondo-edit.obo` only

---
🤖 **Generated by opencode agent**
- Runtime: `opencode`
- Model: `togetherai/moonshotai/Kimi-K2.6`
- Agent config: `ai4curation/mondo-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25755512671)


#### Agent Issue Comment

Thank you @LengUNC and the ClinGen Hereditary Cardiovascular Disease Gene Curation Expert Panel for this detailed request. The requested changes have been implemented and committed in PR #<NN>.

Summary of changes:
- Added **MONDO:7770003 cardiogenetic rhythm disorder** as a new grouping term under `cardiac rhythm disease` and `cardiogenetic disease`.
- Added **MONDO:7770004 SCN5A-related cardiac rhythm disorder** as a new term under `cardiogenetic rhythm disorder`, `cardiac rhythm disease`, and `cardiogenetic disease`.
- Reorganized the five SCN5A-specific phenotypes as children of `SCN5A-related cardiac rhythm disorder`:
  - atrial fibrillation, familial, 10 (MONDO:0013530)
  - sick sinus syndrome 1 (MONDO:0024562)
  - ventricular fibrillation, paroxysmal familial, type 1 (MONDO:0011376)
  - long QT syndrome 3 (MONDO:0011377)
  - Brugada syndrome 1 (MONDO:0011001)
- Added the requested monogenic rhythm disorder categories as children of `cardiogenetic rhythm disorder`:
  - atrial conduction disease (MONDO:0014500)
  - Brugada syndrome (MONDO:0015263)
  - familial atrial fibrillation (MONDO:0018054)
  - familial sick sinus syndrome (MONDO:0012061)
  - progressive familial heart block (MONDO:0019490)
  - short QT syndrome (MONDO:0000453)
  - ventricular tachycardia, familial (MONDO:0008648)
  - ventricular fibrillation, paroxysmal familial, type 1 (MONDO:0011376)
- Per @katiermullen's comment, **atrioventricular block (MONDO:0000465) was excluded** from children of `cardiogenetic rhythm disorder` because it does not necessarily have a monogenic etiology.
- The revised definitions provided in the issue comments were used (with "multifocal ectopic Purkinje-related premature contractions" removed as requested).
- Full validation performed: OBO syntax checked with `robot convert`, normalized with `make NORM`, and logical consistency verified with `robot reason` (no unsatisfiable classes found).

Please let us know if any further adjustments are needed.

---
🤖 **Generated by opencode agent**
- Runtime: `opencode`
- Model: `togetherai/moonshotai/Kimi-K2.6`
- Agent config: `ai4curation/mondo-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25755512671)


#### Agent Diff

```diff
diff --git a/src/ontology/mondo-edit.obo b/src/ontology/mondo-edit.obo
index 8aaf2a57d..5b9c869ed 100644
--- a/src/ontology/mondo-edit.obo
+++ b/src/ontology/mondo-edit.obo
@@ -5867,6 +5867,7 @@ xref: Orphanet:51083 {source="MONDO:equivalentTo", source="OMIM:609620"}
 xref: SCTID:698272007 {source="MONDO:equivalentTo"}
 xref: UMLS:C2348199 {source="MONDO:equivalentTo", source="MONDO:MEDGEN", source="MEDGEN:378835"}
 is_a: MONDO:0000992 {source="DOID:0050793"} ! heart conduction disease
+is_a: MONDO:7770003 {source="https://www.clinicalgenome.org/affiliation/40104/"} ! cardiogenetic rhythm disorder
 relationship: curated_content_resource https://search.clinicalgenome.org/kb/conditions/MONDO:0000453 {source="MONDO:CLINGEN"}
 relationship: has_characteristic MONDO:0021152 {source="OMIMPS:609620"} ! inherited
 property_value: curated_content_resource "https://www.malacards.org/card/familial_short_qt_syndrome" xsd:anyURI {source="MONDO:MalaCards"}
@@ -188784,6 +188785,7 @@ xref: OMIM:192605 {source="MONDO:equivalentTo"}
 xref: SCTID:233906007 {source="MONDO:equivalentTo"}
 xref: UMLS:C0340485 {source="MONDO:equivalentTo", source="MONDO:MEDGEN", source="MEDGEN:83309"}
 is_a: MONDO:0005477 {source="MONDO:Redundant", source="OMIM:192605"} ! ventricular tachycardia
+is_a: MONDO:7770003 {source="https://www.clinicalgenome.org/affiliation/40104/"} ! cardiogenetic rhythm disorder
 intersection_of: MONDO:0005477 ! ventricular tachycardia
 intersection_of: has_characteristic MONDO:0021152 ! inherited
 relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/4385 {source="OMIM:192605"} ! GNAI2
@@ -257842,6 +257844,7 @@ xref: OMIM:601144 {source="DOID:0110218", source="MONDO:equivalentTo"}
 xref: Orphanet:130 {source="OMIM:601144"}
 xref: UMLS:C4551804 {source="MONDO:equivalentTo", source="MONDO:MEDGEN", source="MEDGEN:1646402"}
 is_a: MONDO:0015263 {source="DC-OMIM:601144", source="DOID:0110218", source="MONDO:Redundant", source="OMIM:601144"} ! Brugada syndrome
+is_a: MONDO:7770004 {source="https://www.clinicalgenome.org/affiliation/40104/"} ! SCN5A-related cardiac rhythm disorder
 intersection_of: MONDO:0015263 ! Brugada syndrome
 intersection_of: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/10593 ! SCN5A
 relationship: curated_content_resource https://search.clinicalgenome.org/kb/conditions/MONDO:0011001 {source="MONDO:CLINGEN"}
@@ -267530,6 +267533,8 @@ xref: Orphanet:228140 {source="OMIM:603829"}
 xref: SCTID:233915000 {source="MONDO:equivalentTo"}
 xref: UMLS:C2751898 {source="MEDGEN:414502", source="MONDO:equivalentTo", source="MONDO:MEDGEN"}
 is_a: MONDO:0100234 {source="DC-OMIM:603829", source="MESH:C567851"} ! paroxysmal familial ventricular fibrillation
+is_a: MONDO:7770003 {source="https://www.clinicalgenome.org/affiliation/40104/"} ! cardiogenetic rhythm disorder
+is_a: MONDO:7770004 {source="https://www.clinicalgenome.org/affiliation/40104/"} ! SCN5A-related cardiac rhythm disorder
 intersection_of: MONDO:0100234 ! paroxysmal familial ventricular fibrillation
 intersection_of: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/10593 ! SCN5A
 relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/10593 {source="OMIM:603829"} ! SCN5A
@@ -267562,6 +267567,7 @@ xref: Orphanet:101016 {source="OMIM:603830", source="MONDO:directSiblingOf"}
 xref: Orphanet:768 {source="OMIM:603830"}
 xref: UMLS:C1859062 {source="MONDO:equivalentTo", source="MONDO:MEDGEN", source="MEDGEN:349087"}
 is_a: MONDO:0019171 {source="OMIM:603830", source="Orphanet:101016-prototype"} ! familial long QT syndrome
+is_a: MONDO:7770004 {source="https://www.clinicalgenome.org/affiliation/40104/"} ! SCN5A-related cardiac rhythm disorder
 intersection_of: MONDO:0019171 ! familial long QT syndrome
 intersection_of: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/10593 ! SCN5A
 relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/10593 {source="OMIM:603830"} ! SCN5A
@@ -285573,6 +285579,7 @@ xref: Orphanet:166282 {source="MONDO:equivalentTo", source="OMIM:608567"}
 xref: SCTID:233913007 {source="MONDO:equivalentTo"}
 xref: UMLS:C0340491 {source="MONDO:equivalentTo", source="MONDO:MEDGEN", source="MEDGEN:573766"}
 is_a: MONDO:0001823 {source="DC-OMIM:608567", source="MESH:C563907", source="MONDO:Redundant", source="OMIM:608567"} ! sick sinus syndrome
+is_a: MONDO:7770003 {source="https://www.clinicalgenome.org/affiliation/40104/"} ! cardiogenetic rhythm disorder
 intersection_of: MONDO:0001823 ! sick sinus syndrome
 intersection_of: has_characteristic MONDO:0021152 ! inherited
 relationship: has_characteristic MONDO:0021152 {source="OMIMPS:608567"} ! inherited
@@ -323947,6 +323954,7 @@ xref: OMIM:614022 {source="MONDO:equivalentTo"}
 xref: Orphanet:334 {source="OMIM:614022"}
 xref: UMLS:C3151464 {source="MEDGEN:462814", source="MONDO:equivalentTo", source="MONDO:MEDGEN"}
 is_a: MONDO:0018054 {source="DC-OMIM:614022", source="MONDO:Redundant", source="OMIM:614022"} ! familial atrial fibrillation
+is_a: MONDO:7770004 {source="https://www.clinicalgenome.org/affiliation/40104/"} ! SCN5A-related cardiac rhythm disorder
 intersection_of: MONDO:0018054 ! familial atrial fibrillation
 intersection_of: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/10593 ! SCN5A
 relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/10593 {source="OMIM:614022"} ! SCN5A
@@ -349658,6 +349666,7 @@ xref: OMIM:616117 {source="Orphanet:436242/e", source="EFO:0005304", source="MON
 xref: Orphanet:436242 {source="MONDO:equivalentTo"}
 xref: UMLS:C4015285 {source="MEDGEN:863722", source="MONDO:equivalentTo", source="MONDO:MEDGEN"}
 is_a: MONDO:0005449 {source="EFO:0005304"} ! conduction system disorder
+is_a: MONDO:7770003 {source="https://www.clinicalgenome.org/affiliation/40104/"} ! cardiogenetic rhythm disorder
 relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/19661 {source="OMIM:616117"} ! TNNI3K
 property_value: curated_content_resource "https://www.malacards.org/card/cardiac_conduction_disease_with_or_without_dilated_cardiomyopathy" xsd:anyURI {source="MONDO:MalaCards"}
 
@@ -367966,6 +367975,7 @@ xref: SCTID:418818005 {source="DOID:0050451", source="MONDO:equivalentTo"}
 xref: UMLS:C1142166 {source="MONDO:equivalentTo", source="MONDO:MEDGEN", source="MEDGEN:222975"}
 is_a: MONDO:0000992 {source="DOID:0050451", source="MONDO:Redundant", source="MONDO:indirect"} ! heart conduction disease
 is_a: MONDO:0002254 {source="NCIT:C142891"} ! syndromic disease
+is_a: MONDO:7770003 {source="https://www.clinicalgenome.org/affiliation/40104/"} ! cardiogenetic rhythm disorder
 relationship: curated_content_resource https://search.clinicalgenome.org/kb/conditions/MONDO:0015263 {source="MONDO:CLINGEN"}
 relationship: has_characteristic MONDO:0021152 {source="OMIMPS:601144"} ! inherited
 property_value: curated_content_resource "https://www.malacards.org/card/brugada_syndrome" xsd:anyURI {source="MONDO:MalaCards"}
@@ -426973,6 +426983,7 @@ xref: Orphanet:334 {source="DOID:0050650", source="MONDO:equivalentTo"}
 xref: SCTID:715395008 {source="MONDO:equivalentTo"}
 xref: UMLS:C3468561 {source="MONDO:equivalentTo", source="MONDO:MEDGEN", source="MEDGEN:894635"}
 is_a: MONDO:0004981 {source="DOID:0050650", source="MONDO:DOID", source="MONDO:Redundant"} ! atrial fibrillation
+is_a: MONDO:7770003 {source="https://www.clinicalgenome.org/affiliation/40104/"} ! cardiogenetic rhythm disorder
 intersection_of: MONDO:0004981 ! atrial fibrillation
 intersection_of: has_characteristic MONDO:0021152 ! inherited
 relationship: has_characteristic MONDO:0021152 {source="OMIMPS:608583"} ! inherited
@@ -460887,6 +460898,7 @@ xref: Orphanet:871 {source="MONDO:equivalentTo", source="DOID:0111073"}
 xref: SCTID:698249005 {source="MONDO:equivalentTo"}
 xref: SCTID:93130009 {source="MONDO:equivalentObsolete"}
 is_a: MONDO:0000992 {source="DOID:0111073", source="MONDO:indirect"} ! heart conduction disease
+is_a: MONDO:7770003 {source="https://www.clinicalgenome.org/affiliation/40104/"} ! cardiogenetic rhythm disorder
 relationship: has_characteristic MONDO:0021152 {source="OMIMPS:113900"} ! inherited
 property_value: curated_content_resource "https://www.malacards.org/card/familial_progressive_cardiac_conduction_defect" xsd:anyURI {source="MONDO:MalaCards"}
 property_value: curated_content_resource "https://www.malacards.org/card/progressive_familial_heart_block" xsd:anyURI {source="MONDO:MalaCards"}
@@ -513335,6 +513347,7 @@ xref: OMIM:608567 {source="MONDO:equivalentTo"}
 xref: Orphanet:166282 {source="OMIM:608567"}
 xref: UMLS:C1837845 {source="MONDO:equivalentTo", source="MONDO:MEDGEN", source="MEDGEN:325270"}
 is_a: MONDO:0012061 {source="MONDO:0024562/inferred", source="MONDO:Redundant", source="OMIM:608567"} ! familial sick sinus syndrome
+is_a: MONDO:7770004 {source="https://www.clinicalgenome.org/affiliation/40104/"} ! SCN5A-related cardiac rhythm disorder
 intersection_of: MONDO:0012061 ! familial sick sinus syndrome
 intersection_of: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/10593 ! SCN5A
 relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/10593 {source="OMIM:608567"} ! SCN5A
@@ -621534,6 +621547,28 @@ is_a: MONDO:0005451 {source="PMID:38849953"} ! eating disorder
 property_value: http://purl.org/dc/terms/creator https://orcid.org/0000-0003-3311-7320
 property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9408" xsd:anyURI
 
+[Term]
+id: MONDO:7770003
+name: cardiogenetic rhythm disorder
+def: "A heterogeneous group of cardiac rhythm phenotypes with a monogenic etiology that include, but are not limited to, atrial fibrillation, sick sinus syndrome, progressive cardiac conduction disease, ventricular fibrillation, Brugada syndrome, long QT syndrome, short QT syndrome, tachycardia with fibrillation, etc." [https://www.clinicalgenome.org/affiliation/40104/]
+is_a: MONDO:0007263 {source="https://www.clinicalgenome.org/affiliation/40104/"} ! cardiac rhythm disease
+is_a: MONDO:0100547 {source="https://www.clinicalgenome.org/affiliation/40104/"} ! cardiogenetic disease
+property_value: http://purl.org/dc/terms/creator https://orcid.org/0000-0002-5002-8648
+property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9707" xsd:anyURI
+
+[Term]
+id: MONDO:7770004
+name: SCN5A-related cardiac rhythm disorder
+def: "A heterogeneous collection of cardiac rhythm disorders caused by genetic variation in the SCN5A gene with autosomal dominant inheritance. Affected individuals are commonly reported to have unremarkable cardiac morphology and at least one cardiac rhythm phenotype that includes, but is not limited to, atrial fibrillation, sick sinus syndrome, progressive cardiac conduction disease, ventricular fibrillation, long QT syndrome, and Brugada syndrome. Individuals with pathogenic variants in SCN5A may also exhibit overlapping or mixed cardiac rhythm phenotypes and intrafamilial variability." [https://www.clinicalgenome.org/affiliation/40104/]
+is_a: MONDO:0007263 {source="https://www.clinicalgenome.org/affiliation/40104/"} ! cardiac rhythm disease
+is_a: MONDO:0100547 {source="https://www.clinicalgenome.org/affiliation/40104/"} ! cardiogenetic disease
+is_a: MONDO:7770003 {source="https://www.clinicalgenome.org/affiliation/40104/"} ! cardiogenetic rhythm disorder
+intersection_of: MONDO:0007263 ! cardiac rhythm disease
+intersection_of: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/10593 ! SCN5A
+relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/10593 {source="https://www.clinicalgenome.org/affiliation/40104/"} ! SCN5A
+property_value: http://purl.org/dc/terms/creator https://orcid.org/0000-0002-5002-8648
+property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9707" xsd:anyURI
+
 [Term]
 id: MONDO:8000000
 name: infectious discitis

```

### Attempt 2: claude-sonnet-4.5 / copilot

- **Eval PR**: [#525](https://github.com/ai4curation/eval-ont-agent-mondo/pull/525)
- **F1**: 0.462  **Precision**: 0.375  **Recall**: 0.600  **Jaccard**: 0.300

#### Agent Diff

```diff
diff --git a/src/ontology/mondo-edit.obo b/src/ontology/mondo-edit.obo
index 8aaf2a57d..d65d81944 100644
--- a/src/ontology/mondo-edit.obo
+++ b/src/ontology/mondo-edit.obo
@@ -5867,6 +5867,7 @@ xref: Orphanet:51083 {source="MONDO:equivalentTo", source="OMIM:609620"}
 xref: SCTID:698272007 {source="MONDO:equivalentTo"}
 xref: UMLS:C2348199 {source="MONDO:equivalentTo", source="MONDO:MEDGEN", source="MEDGEN:378835"}
 is_a: MONDO:0000992 {source="DOID:0050793"} ! heart conduction disease
+is_a: MONDO:7770003 {source="https://www.clinicalgenome.org/affiliation/40104/"} ! cardiogenetic rhythm disorders
 relationship: curated_content_resource https://search.clinicalgenome.org/kb/conditions/MONDO:0000453 {source="MONDO:CLINGEN"}
 relationship: has_characteristic MONDO:0021152 {source="OMIMPS:609620"} ! inherited
 property_value: curated_content_resource "https://www.malacards.org/card/familial_short_qt_syndrome" xsd:anyURI {source="MONDO:MalaCards"}
@@ -188784,6 +188785,7 @@ xref: OMIM:192605 {source="MONDO:equivalentTo"}
 xref: SCTID:233906007 {source="MONDO:equivalentTo"}
 xref: UMLS:C0340485 {source="MONDO:equivalentTo", source="MONDO:MEDGEN", source="MEDGEN:83309"}
 is_a: MONDO:0005477 {source="MONDO:Redundant", source="OMIM:192605"} ! ventricular tachycardia
+is_a: MONDO:7770003 {source="https://www.clinicalgenome.org/affiliation/40104/"} ! cardiogenetic rhythm disorders
 intersection_of: MONDO:0005477 ! ventricular tachycardia
 intersection_of: has_characteristic MONDO:0021152 ! inherited
 relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/4385 {source="OMIM:192605"} ! GNAI2
@@ -257842,6 +257844,7 @@ xref: OMIM:601144 {source="DOID:0110218", source="MONDO:equivalentTo"}
 xref: Orphanet:130 {source="OMIM:601144"}
 xref: UMLS:C4551804 {source="MONDO:equivalentTo", source="MONDO:MEDGEN", source="MEDGEN:1646402"}
 is_a: MONDO:0015263 {source="DC-OMIM:601144", source="DOID:0110218", source="MONDO:Redundant", source="OMIM:601144"} ! Brugada syndrome
+is_a: MONDO:7770004 {source="https://www.clinicalgenome.org/affiliation/40104/"} ! SCN5A-related cardiac rhythm disorder
 intersection_of: MONDO:0015263 ! Brugada syndrome
 intersection_of: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/10593 ! SCN5A
 relationship: curated_content_resource https://search.clinicalgenome.org/kb/conditions/MONDO:0011001 {source="MONDO:CLINGEN"}
@@ -267530,6 +267533,7 @@ xref: Orphanet:228140 {source="OMIM:603829"}
 xref: SCTID:233915000 {source="MONDO:equivalentTo"}
 xref: UMLS:C2751898 {source="MEDGEN:414502", source="MONDO:equivalentTo", source="MONDO:MEDGEN"}
 is_a: MONDO:0100234 {source="DC-OMIM:603829", source="MESH:C567851"} ! paroxysmal familial ventricular fibrillation
+is_a: MONDO:7770004 {source="https://www.clinicalgenome.org/affiliation/40104/"} ! SCN5A-related cardiac rhythm disorder
 intersection_of: MONDO:0100234 ! paroxysmal familial ventricular fibrillation
 intersection_of: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/10593 ! SCN5A
 relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/10593 {source="OMIM:603829"} ! SCN5A
@@ -267562,6 +267566,7 @@ xref: Orphanet:101016 {source="OMIM:603830", source="MONDO:directSiblingOf"}
 xref: Orphanet:768 {source="OMIM:603830"}
 xref: UMLS:C1859062 {source="MONDO:equivalentTo", source="MONDO:MEDGEN", source="MEDGEN:349087"}
 is_a: MONDO:0019171 {source="OMIM:603830", source="Orphanet:101016-prototype"} ! familial long QT syndrome
+is_a: MONDO:7770004 {source="https://www.clinicalgenome.org/affiliation/40104/"} ! SCN5A-related cardiac rhythm disorder
 intersection_of: MONDO:0019171 ! familial long QT syndrome
 intersection_of: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/10593 ! SCN5A
 relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/10593 {source="OMIM:603830"} ! SCN5A
@@ -285573,6 +285578,7 @@ xref: Orphanet:166282 {source="MONDO:equivalentTo", source="OMIM:608567"}
 xref: SCTID:233913007 {source="MONDO:equivalentTo"}
 xref: UMLS:C0340491 {source="MONDO:equivalentTo", source="MONDO:MEDGEN", source="MEDGEN:573766"}
 is_a: MONDO:0001823 {source="DC-OMIM:608567", source="MESH:C563907", source="MONDO:Redundant", source="OMIM:608567"} ! sick sinus syndrome
+is_a: MONDO:7770003 {source="https://www.clinicalgenome.org/affiliation/40104/"} ! cardiogenetic rhythm disorders
 intersection_of: MONDO:0001823 ! sick sinus syndrome
 intersection_of: has_characteristic MONDO:0021152 ! inherited
 relationship: has_characteristic MONDO:0021152 {source="OMIMPS:608567"} ! inherited
@@ -323947,6 +323953,7 @@ xref: OMIM:614022 {source="MONDO:equivalentTo"}
 xref: Orphanet:334 {source="OMIM:614022"}
 xref: UMLS:C3151464 {source="MEDGEN:462814", source="MONDO:equivalentTo", source="MONDO:MEDGEN"}
 is_a: MONDO:0018054 {source="DC-OMIM:614022", source="MONDO:Redundant", source="OMIM:614022"} ! familial atrial fibrillation
+is_a: MONDO:7770004 {source="https://www.clinicalgenome.org/affiliation/40104/"} ! SCN5A-related cardiac rhythm disorder
 intersection_of: MONDO:0018054 ! familial atrial fibrillation
 intersection_of: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/10593 ! SCN5A
 relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/10593 {source="OMIM:614022"} ! SCN5A
@@ -349658,6 +349665,7 @@ xref: OMIM:616117 {source="Orphanet:436242/e", source="EFO:0005304", source="MON
 xref: Orphanet:436242 {source="MONDO:equivalentTo"}
 xref: UMLS:C4015285 {source="MEDGEN:863722", source="MONDO:equivalentTo", source="MONDO:MEDGEN"}
 is_a: MONDO:0005449 {source="EFO:0005304"} ! conduction system disorder
+is_a: MONDO:7770003 {source="https://www.clinicalgenome.org/affiliation/40104/"} ! cardiogenetic rhythm disorders
 relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/19661 {source="OMIM:616117"} ! TNNI3K
 property_value: curated_content_resource "https://www.malacards.org/card/cardiac_conduction_disease_with_or_without_dilated_cardiomyopathy" xsd:anyURI {source="MONDO:MalaCards"}
 
@@ -367966,6 +367974,7 @@ xref: SCTID:418818005 {source="DOID:0050451", source="MONDO:equivalentTo"}
 xref: UMLS:C1142166 {source="MONDO:equivalentTo", source="MONDO:MEDGEN", source="MEDGEN:222975"}
 is_a: MONDO:0000992 {source="DOID:0050451", source="MONDO:Redundant", source="MONDO:indirect"} ! heart conduction disease
 is_a: MONDO:0002254 {source="NCIT:C142891"} ! syndromic disease
+is_a: MONDO:7770003 {source="https://www.clinicalgenome.org/affiliation/40104/"} ! cardiogenetic rhythm disorders
 relationship: curated_content_resource https://search.clinicalgenome.org/kb/conditions/MONDO:0015263 {source="MONDO:CLINGEN"}
 relationship: has_characteristic MONDO:0021152 {source="OMIMPS:601144"} ! inherited
 property_value: curated_content_resource "https://www.malacards.org/card/brugada_syndrome" xsd:anyURI {source="MONDO:MalaCards"}
@@ -426973,6 +426982,7 @@ xref: Orphanet:334 {source="DOID:0050650", source="MONDO:equivalentTo"}
 xref: SCTID:715395008 {source="MONDO:equivalentTo"}
 xref: UMLS:C3468561 {source="MONDO:equivalentTo", source="MONDO:MEDGEN", source="MEDGEN:894635"}
 is_a: MONDO:0004981 {source="DOID:0050650", source="MONDO:DOID", source="MONDO:Redundant"} ! atrial fibrillation
+is_a: MONDO:7770003 {source="https://www.clinicalgenome.org/affiliation/40104/"} ! cardiogenetic rhythm disorders
 intersection_of: MONDO:0004981 ! atrial fibrillation
 intersection_of: has_characteristic MONDO:0021152 ! inherited
 relationship: has_characteristic MONDO:0021152 {source="OMIMPS:608583"} ! inherited
@@ -460887,6 +460897,7 @@ xref: Orphanet:871 {source="MONDO:equivalentTo", source="DOID:0111073"}
 xref: SCTID:698249005 {source="MONDO:equivalentTo"}
 xref: SCTID:93130009 {source="MONDO:equivalentObsolete"}
 is_a: MONDO:0000992 {source="DOID:0111073", source="MONDO:indirect"} ! heart conduction disease
+is_a: MONDO:7770003 {source="https://www.clinicalgenome.org/affiliation/40104/"} ! cardiogenetic rhythm disorders
 relationship: has_characteristic MONDO:0021152 {source="OMIMPS:113900"} ! inherited
 property_value: curated_content_resource "https://www.malacards.org/card/familial_progressive_cardiac_conduction_defect" xsd:anyURI {source="MONDO:MalaCards"}
 property_value: curated_content_resource "https://www.malacards.org/card/progressive_familial_heart_block" xsd:anyURI {source="MONDO:MalaCards"}
@@ -513335,6 +513346,7 @@ xref: OMIM:608567 {source="MONDO:equivalentTo"}
 xref: Orphanet:166282 {source="OMIM:608567"}
 xref: UMLS:C1837845 {source="MONDO:equivalentTo", source="MONDO:MEDGEN", source="MEDGEN:325270"}
 is_a: MONDO:0012061 {source="MONDO:0024562/inferred", source="MONDO:Redundant", source="OMIM:608567"} ! familial sick sinus syndrome
+is_a: MONDO:7770004 {source="https://www.clinicalgenome.org/affiliation/40104/"} ! SCN5A-related cardiac rhythm disorder
 intersection_of: MONDO:0012061 ! familial sick sinus syndrome
 intersection_of: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/10593 ! SCN5A
 relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/10593 {source="OMIM:608567"} ! SCN5A
@@ -561829,6 +561841,7 @@ xref: MEDGEN:83310 {source="MONDO:equivalentTo", source="MONDO:MEDGEN"}
 xref: Orphanet:228140 {source="MONDO:equivalentTo", source="OMIM:603829"}
 xref: UMLS:C0340493 {source="MEDGEN:83310", source="MONDO:equivalentTo", source="MONDO:MEDGEN"}
 is_a: MONDO:0000190 {source="https://orcid.org/0000-0001-5208-3432"} ! ventricular fibrillation
+is_a: MONDO:7770003 {source="https://www.clinicalgenome.org/affiliation/40104/"} ! cardiogenetic rhythm disorders
 property_value: curated_content_resource "https://www.malacards.org/card/paroxysmal_familial_ventricular_fibrillation" xsd:anyURI {source="MONDO:MalaCards"}
 property_value: http://purl.org/dc/terms/creator https://orcid.org/0000-0001-5208-3432
 property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/2524" xsd:anyURI
@@ -621534,6 +621547,26 @@ is_a: MONDO:0005451 {source="PMID:38849953"} ! eating disorder
 property_value: http://purl.org/dc/terms/creator https://orcid.org/0000-0003-3311-7320
 property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9408" xsd:anyURI
 
+[Term]
+id: MONDO:7770003
+name: cardiogenetic rhythm disorders
+def: "A heterogeneous group of cardiac rhythm phenotypes with a monogenic etiology that include, but are not limited to, atrial fibrillation, sick sinus syndrome, progressive cardiac conduction disease, ventricular fibrillation, Brugada syndrome, long QT syndrome, short QT syndrome, tachycardia with fibrillation, etc." [https://www.clinicalgenome.org/affiliation/40104/]
+is_a: MONDO:0100547 {source="https://www.clinicalgenome.org/affiliation/40104/"} ! cardiogenetic disease
+property_value: http://purl.org/dc/terms/creator doi:10.1186/s13326-024-00320-3
+property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9707" xsd:anyURI
+
+[Term]
+id: MONDO:7770004
+name: SCN5A-related cardiac rhythm disorder
+def: "A heterogeneous collection of cardiac rhythm disorders caused by genetic variation in the SCN5A gene with autosomal dominant inheritance. Affected individuals are commonly reported to have unremarkable cardiac morphology and at least one cardiac rhythm phenotype that includes, but is not limited to, atrial fibrillation, sick sinus syndrome, progressive cardiac conduction disease, ventricular fibrillation, long QT syndrome, and Brugada syndrome. Individuals with pathogenic variants in SCN5A may also exhibit overlapping or mixed cardiac rhythm phenotypes and intrafamilial variability." [https://www.clinicalgenome.org/affiliation/40104/]
+is_a: MONDO:0007263 {source="https://www.clinicalgenome.org/affiliation/40104/"} ! cardiac rhythm disease
+is_a: MONDO:0100547 {source="https://www.clinicalgenome.org/affiliation/40104/"} ! cardiogenetic disease
+intersection_of: MONDO:0007263 ! cardiac rhythm disease
+intersection_of: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/10593 ! SCN5A
+relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/10593 {source="https://www.clinicalgenome.org/affiliation/40104/"} ! SCN5A
+property_value: http://purl.org/dc/terms/creator doi:10.1186/s13326-024-00320-3
+property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9707" xsd:anyURI
+
 [Term]
 id: MONDO:8000000
 name: infectious discitis

```

### Attempt 3: claude-sonnet-4.5 / copilot

- **Eval PR**: [#490](https://github.com/ai4curation/eval-ont-agent-mondo/pull/490)
- **F1**: 0.462  **Precision**: 0.375  **Recall**: 0.600  **Jaccard**: 0.300

#### Agent Diff

```diff
diff --git a/src/ontology/mondo-edit.obo b/src/ontology/mondo-edit.obo
index 8aaf2a57d..d65d81944 100644
--- a/src/ontology/mondo-edit.obo
+++ b/src/ontology/mondo-edit.obo
@@ -5867,6 +5867,7 @@ xref: Orphanet:51083 {source="MONDO:equivalentTo", source="OMIM:609620"}
 xref: SCTID:698272007 {source="MONDO:equivalentTo"}
 xref: UMLS:C2348199 {source="MONDO:equivalentTo", source="MONDO:MEDGEN", source="MEDGEN:378835"}
 is_a: MONDO:0000992 {source="DOID:0050793"} ! heart conduction disease
+is_a: MONDO:7770003 {source="https://www.clinicalgenome.org/affiliation/40104/"} ! cardiogenetic rhythm disorders
 relationship: curated_content_resource https://search.clinicalgenome.org/kb/conditions/MONDO:0000453 {source="MONDO:CLINGEN"}
 relationship: has_characteristic MONDO:0021152 {source="OMIMPS:609620"} ! inherited
 property_value: curated_content_resource "https://www.malacards.org/card/familial_short_qt_syndrome" xsd:anyURI {source="MONDO:MalaCards"}
@@ -188784,6 +188785,7 @@ xref: OMIM:192605 {source="MONDO:equivalentTo"}
 xref: SCTID:233906007 {source="MONDO:equivalentTo"}
 xref: UMLS:C0340485 {source="MONDO:equivalentTo", source="MONDO:MEDGEN", source="MEDGEN:83309"}
 is_a: MONDO:0005477 {source="MONDO:Redundant", source="OMIM:192605"} ! ventricular tachycardia
+is_a: MONDO:7770003 {source="https://www.clinicalgenome.org/affiliation/40104/"} ! cardiogenetic rhythm disorders
 intersection_of: MONDO:0005477 ! ventricular tachycardia
 intersection_of: has_characteristic MONDO:0021152 ! inherited
 relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/4385 {source="OMIM:192605"} ! GNAI2
@@ -257842,6 +257844,7 @@ xref: OMIM:601144 {source="DOID:0110218", source="MONDO:equivalentTo"}
 xref: Orphanet:130 {source="OMIM:601144"}
 xref: UMLS:C4551804 {source="MONDO:equivalentTo", source="MONDO:MEDGEN", source="MEDGEN:1646402"}
 is_a: MONDO:0015263 {source="DC-OMIM:601144", source="DOID:0110218", source="MONDO:Redundant", source="OMIM:601144"} ! Brugada syndrome
+is_a: MONDO:7770004 {source="https://www.clinicalgenome.org/affiliation/40104/"} ! SCN5A-related cardiac rhythm disorder
 intersection_of: MONDO:0015263 ! Brugada syndrome
 intersection_of: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/10593 ! SCN5A
 relationship: curated_content_resource https://search.clinicalgenome.org/kb/conditions/MONDO:0011001 {source="MONDO:CLINGEN"}
@@ -267530,6 +267533,7 @@ xref: Orphanet:228140 {source="OMIM:603829"}
 xref: SCTID:233915000 {source="MONDO:equivalentTo"}
 xref: UMLS:C2751898 {source="MEDGEN:414502", source="MONDO:equivalentTo", source="MONDO:MEDGEN"}
 is_a: MONDO:0100234 {source="DC-OMIM:603829", source="MESH:C567851"} ! paroxysmal familial ventricular fibrillation
+is_a: MONDO:7770004 {source="https://www.clinicalgenome.org/affiliation/40104/"} ! SCN5A-related cardiac rhythm disorder
 intersection_of: MONDO:0100234 ! paroxysmal familial ventricular fibrillation
 intersection_of: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/10593 ! SCN5A
 relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/10593 {source="OMIM:603829"} ! SCN5A
@@ -267562,6 +267566,7 @@ xref: Orphanet:101016 {source="OMIM:603830", source="MONDO:directSiblingOf"}
 xref: Orphanet:768 {source="OMIM:603830"}
 xref: UMLS:C1859062 {source="MONDO:equivalentTo", source="MONDO:MEDGEN", source="MEDGEN:349087"}
 is_a: MONDO:0019171 {source="OMIM:603830", source="Orphanet:101016-prototype"} ! familial long QT syndrome
+is_a: MONDO:7770004 {source="https://www.clinicalgenome.org/affiliation/40104/"} ! SCN5A-related cardiac rhythm disorder
 intersection_of: MONDO:0019171 ! familial long QT syndrome
 intersection_of: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/10593 ! SCN5A
 relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/10593 {source="OMIM:603830"} ! SCN5A
@@ -285573,6 +285578,7 @@ xref: Orphanet:166282 {source="MONDO:equivalentTo", source="OMIM:608567"}
 xref: SCTID:233913007 {source="MONDO:equivalentTo"}
 xref: UMLS:C0340491 {source="MONDO:equivalentTo", source="MONDO:MEDGEN", source="MEDGEN:573766"}
 is_a: MONDO:0001823 {source="DC-OMIM:608567", source="MESH:C563907", source="MONDO:Redundant", source="OMIM:608567"} ! sick sinus syndrome
+is_a: MONDO:7770003 {source="https://www.clinicalgenome.org/affiliation/40104/"} ! cardiogenetic rhythm disorders
 intersection_of: MONDO:0001823 ! sick sinus syndrome
 intersection_of: has_characteristic MONDO:0021152 ! inherited
 relationship: has_characteristic MONDO:0021152 {source="OMIMPS:608567"} ! inherited
@@ -323947,6 +323953,7 @@ xref: OMIM:614022 {source="MONDO:equivalentTo"}
 xref: Orphanet:334 {source="OMIM:614022"}
 xref: UMLS:C3151464 {source="MEDGEN:462814", source="MONDO:equivalentTo", source="MONDO:MEDGEN"}
 is_a: MONDO:0018054 {source="DC-OMIM:614022", source="MONDO:Redundant", source="OMIM:614022"} ! familial atrial fibrillation
+is_a: MONDO:7770004 {source="https://www.clinicalgenome.org/affiliation/40104/"} ! SCN5A-related cardiac rhythm disorder
 intersection_of: MONDO:0018054 ! familial atrial fibrillation
 intersection_of: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/10593 ! SCN5A
 relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/10593 {source="OMIM:614022"} ! SCN5A
@@ -349658,6 +349665,7 @@ xref: OMIM:616117 {source="Orphanet:436242/e", source="EFO:0005304", source="MON
 xref: Orphanet:436242 {source="MONDO:equivalentTo"}
 xref: UMLS:C4015285 {source="MEDGEN:863722", source="MONDO:equivalentTo", source="MONDO:MEDGEN"}
 is_a: MONDO:0005449 {source="EFO:0005304"} ! conduction system disorder
+is_a: MONDO:7770003 {source="https://www.clinicalgenome.org/affiliation/40104/"} ! cardiogenetic rhythm disorders
 relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/19661 {source="OMIM:616117"} ! TNNI3K
 property_value: curated_content_resource "https://www.malacards.org/card/cardiac_conduction_disease_with_or_without_dilated_cardiomyopathy" xsd:anyURI {source="MONDO:MalaCards"}
 
@@ -367966,6 +367974,7 @@ xref: SCTID:418818005 {source="DOID:0050451", source="MONDO:equivalentTo"}
 xref: UMLS:C1142166 {source="MONDO:equivalentTo", source="MONDO:MEDGEN", source="MEDGEN:222975"}
 is_a: MONDO:0000992 {source="DOID:0050451", source="MONDO:Redundant", source="MONDO:indirect"} ! heart conduction disease
 is_a: MONDO:0002254 {source="NCIT:C142891"} ! syndromic disease
+is_a: MONDO:7770003 {source="https://www.clinicalgenome.org/affiliation/40104/"} ! cardiogenetic rhythm disorders
 relationship: curated_content_resource https://search.clinicalgenome.org/kb/conditions/MONDO:0015263 {source="MONDO:CLINGEN"}
 relationship: has_characteristic MONDO:0021152 {source="OMIMPS:601144"} ! inherited
 property_value: curated_content_resource "https://www.malacards.org/card/brugada_syndrome" xsd:anyURI {source="MONDO:MalaCards"}
@@ -426973,6 +426982,7 @@ xref: Orphanet:334 {source="DOID:0050650", source="MONDO:equivalentTo"}
 xref: SCTID:715395008 {source="MONDO:equivalentTo"}
 xref: UMLS:C3468561 {source="MONDO:equivalentTo", source="MONDO:MEDGEN", source="MEDGEN:894635"}
 is_a: MONDO:0004981 {source="DOID:0050650", source="MONDO:DOID", source="MONDO:Redundant"} ! atrial fibrillation
+is_a: MONDO:7770003 {source="https://www.clinicalgenome.org/affiliation/40104/"} ! cardiogenetic rhythm disorders
 intersection_of: MONDO:0004981 ! atrial fibrillation
 intersection_of: has_characteristic MONDO:0021152 ! inherited
 relationship: has_characteristic MONDO:0021152 {source="OMIMPS:608583"} ! inherited
@@ -460887,6 +460897,7 @@ xref: Orphanet:871 {source="MONDO:equivalentTo", source="DOID:0111073"}
 xref: SCTID:698249005 {source="MONDO:equivalentTo"}
 xref: SCTID:93130009 {source="MONDO:equivalentObsolete"}
 is_a: MONDO:0000992 {source="DOID:0111073", source="MONDO:indirect"} ! heart conduction disease
+is_a: MONDO:7770003 {source="https://www.clinicalgenome.org/affiliation/40104/"} ! cardiogenetic rhythm disorders
 relationship: has_characteristic MONDO:0021152 {source="OMIMPS:113900"} ! inherited
 property_value: curated_content_resource "https://www.malacards.org/card/familial_progressive_cardiac_conduction_defect" xsd:anyURI {source="MONDO:MalaCards"}
 property_value: curated_content_resource "https://www.malacards.org/card/progressive_familial_heart_block" xsd:anyURI {source="MONDO:MalaCards"}
@@ -513335,6 +513346,7 @@ xref: OMIM:608567 {source="MONDO:equivalentTo"}
 xref: Orphanet:166282 {source="OMIM:608567"}
 xref: UMLS:C1837845 {source="MONDO:equivalentTo", source="MONDO:MEDGEN", source="MEDGEN:325270"}
 is_a: MONDO:0012061 {source="MONDO:0024562/inferred", source="MONDO:Redundant", source="OMIM:608567"} ! familial sick sinus syndrome
+is_a: MONDO:7770004 {source="https://www.clinicalgenome.org/affiliation/40104/"} ! SCN5A-related cardiac rhythm disorder
 intersection_of: MONDO:0012061 ! familial sick sinus syndrome
 intersection_of: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/10593 ! SCN5A
 relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/10593 {source="OMIM:608567"} ! SCN5A
@@ -561829,6 +561841,7 @@ xref: MEDGEN:83310 {source="MONDO:equivalentTo", source="MONDO:MEDGEN"}
 xref: Orphanet:228140 {source="MONDO:equivalentTo", source="OMIM:603829"}
 xref: UMLS:C0340493 {source="MEDGEN:83310", source="MONDO:equivalentTo", source="MONDO:MEDGEN"}
 is_a: MONDO:0000190 {source="https://orcid.org/0000-0001-5208-3432"} ! ventricular fibrillation
+is_a: MONDO:7770003 {source="https://www.clinicalgenome.org/affiliation/40104/"} ! cardiogenetic rhythm disorders
 property_value: curated_content_resource "https://www.malacards.org/card/paroxysmal_familial_ventricular_fibrillation" xsd:anyURI {source="MONDO:MalaCards"}
 property_value: http://purl.org/dc/terms/creator https://orcid.org/0000-0001-5208-3432
 property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/2524" xsd:anyURI
@@ -621534,6 +621547,26 @@ is_a: MONDO:0005451 {source="PMID:38849953"} ! eating disorder
 property_value: http://purl.org/dc/terms/creator https://orcid.org/0000-0003-3311-7320
 property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9408" xsd:anyURI
 
+[Term]
+id: MONDO:7770003
+name: cardiogenetic rhythm disorders
+def: "A heterogeneous group of cardiac rhythm phenotypes with a monogenic etiology that include, but are not limited to, atrial fibrillation, sick sinus syndrome, progressive cardiac conduction disease, ventricular fibrillation, Brugada syndrome, long QT syndrome, short QT syndrome, tachycardia with fibrillation, etc." [https://www.clinicalgenome.org/affiliation/40104/]
+is_a: MONDO:0100547 {source="https://www.clinicalgenome.org/affiliation/40104/"} ! cardiogenetic disease
+property_value: http://purl.org/dc/terms/creator doi:10.1186/s13326-024-00320-3
+property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9707" xsd:anyURI
+
+[Term]
+id: MONDO:7770004
+name: SCN5A-related cardiac rhythm disorder
+def: "A heterogeneous collection of cardiac rhythm disorders caused by genetic variation in the SCN5A gene with autosomal dominant inheritance. Affected individuals are commonly reported to have unremarkable cardiac morphology and at least one cardiac rhythm phenotype that includes, but is not limited to, atrial fibrillation, sick sinus syndrome, progressive cardiac conduction disease, ventricular fibrillation, long QT syndrome, and Brugada syndrome. Individuals with pathogenic variants in SCN5A may also exhibit overlapping or mixed cardiac rhythm phenotypes and intrafamilial variability." [https://www.clinicalgenome.org/affiliation/40104/]
+is_a: MONDO:0007263 {source="https://www.clinicalgenome.org/affiliation/40104/"} ! cardiac rhythm disease
+is_a: MONDO:0100547 {source="https://www.clinicalgenome.org/affiliation/40104/"} ! cardiogenetic disease
+intersection_of: MONDO:0007263 ! cardiac rhythm disease
+intersection_of: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/10593 ! SCN5A
+relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/10593 {source="https://www.clinicalgenome.org/affiliation/40104/"} ! SCN5A
+property_value: http://purl.org/dc/terms/creator doi:10.1186/s13326-024-00320-3
+property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9707" xsd:anyURI
+
 [Term]
 id: MONDO:8000000
 name: infectious discitis

```

### Attempt 4: claude-sonnet-4.5 / claude

- **Eval PR**: [#445](https://github.com/ai4curation/eval-ont-agent-mondo/pull/445)
- **F1**: 0.432  **Precision**: 0.333  **Recall**: 0.615  **Jaccard**: 0.276
- **Trace**: [25867698890](https://github.com/ai4curation/eval-ont-agent-mondo/tree/master/traces/25867698890)
- **Workflow run**: [25867698890](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25867698890)

#### Agent PR Comment

# PR: Add cardiogenetic rhythm disorders and SCN5A-related cardiac rhythm disorder terms

#### Agent Issue Comment

Thank you for this request from the ClinGen Hereditary Cardiovascular Disease Gene Curation Expert Panel!

I have successfully created both new terms as requested:

1. **MONDO:7770003** - cardiogenetic rhythm disorders
2. **MONDO:7770004** - SCN5A-related cardiac rhythm disorder

The hierarchical relationships have been established with all the child terms you specified, using the revised definitions from your comment on October 31st (which removed the multifocal ectopic Purkinje-related premature contractions).

Following the previous discussion, I have excluded atrioventricular block (MONDO:0000465) from the children of cardiogenetic rhythm disorders, as it does not necessarily have a monogenic etiology.

All changes have been committed in PR #<NN>.

Please review the changes and let me know if you have any questions or if any adjustments are needed.

---
🤖 **Generated by claude agent**
- Runtime: `claude`
- Model: `claude-sonnet-4-5-20250929`
- Agent config: `ai4curation/mondo-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25867698890)

#### Agent Diff

```diff
diff --git a/src/ontology/mondo-edit.obo b/src/ontology/mondo-edit.obo
index 8aaf2a57d..e3d9937d5 100644
--- a/src/ontology/mondo-edit.obo
+++ b/src/ontology/mondo-edit.obo
@@ -5867,6 +5867,7 @@ xref: Orphanet:51083 {source="MONDO:equivalentTo", source="OMIM:609620"}
 xref: SCTID:698272007 {source="MONDO:equivalentTo"}
 xref: UMLS:C2348199 {source="MONDO:equivalentTo", source="MONDO:MEDGEN", source="MEDGEN:378835"}
 is_a: MONDO:0000992 {source="DOID:0050793"} ! heart conduction disease
+is_a: MONDO:7770003 {source="https://www.clinicalgenome.org/affiliation/40104/"} ! cardiogenetic rhythm disorders
 relationship: curated_content_resource https://search.clinicalgenome.org/kb/conditions/MONDO:0000453 {source="MONDO:CLINGEN"}
 relationship: has_characteristic MONDO:0021152 {source="OMIMPS:609620"} ! inherited
 property_value: curated_content_resource "https://www.malacards.org/card/familial_short_qt_syndrome" xsd:anyURI {source="MONDO:MalaCards"}
@@ -188784,6 +188785,7 @@ xref: OMIM:192605 {source="MONDO:equivalentTo"}
 xref: SCTID:233906007 {source="MONDO:equivalentTo"}
 xref: UMLS:C0340485 {source="MONDO:equivalentTo", source="MONDO:MEDGEN", source="MEDGEN:83309"}
 is_a: MONDO:0005477 {source="MONDO:Redundant", source="OMIM:192605"} ! ventricular tachycardia
+is_a: MONDO:7770003 {source="https://www.clinicalgenome.org/affiliation/40104/"} ! cardiogenetic rhythm disorders
 intersection_of: MONDO:0005477 ! ventricular tachycardia
 intersection_of: has_characteristic MONDO:0021152 ! inherited
 relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/4385 {source="OMIM:192605"} ! GNAI2
@@ -257842,6 +257844,7 @@ xref: OMIM:601144 {source="DOID:0110218", source="MONDO:equivalentTo"}
 xref: Orphanet:130 {source="OMIM:601144"}
 xref: UMLS:C4551804 {source="MONDO:equivalentTo", source="MONDO:MEDGEN", source="MEDGEN:1646402"}
 is_a: MONDO:0015263 {source="DC-OMIM:601144", source="DOID:0110218", source="MONDO:Redundant", source="OMIM:601144"} ! Brugada syndrome
+is_a: MONDO:7770004 {source="https://www.clinicalgenome.org/affiliation/40104/"} ! SCN5A-related cardiac rhythm disorder
 intersection_of: MONDO:0015263 ! Brugada syndrome
 intersection_of: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/10593 ! SCN5A
 relationship: curated_content_resource https://search.clinicalgenome.org/kb/conditions/MONDO:0011001 {source="MONDO:CLINGEN"}
@@ -267530,6 +267533,8 @@ xref: Orphanet:228140 {source="OMIM:603829"}
 xref: SCTID:233915000 {source="MONDO:equivalentTo"}
 xref: UMLS:C2751898 {source="MEDGEN:414502", source="MONDO:equivalentTo", source="MONDO:MEDGEN"}
 is_a: MONDO:0100234 {source="DC-OMIM:603829", source="MESH:C567851"} ! paroxysmal familial ventricular fibrillation
+is_a: MONDO:7770003 {source="https://www.clinicalgenome.org/affiliation/40104/"} ! cardiogenetic rhythm disorders
+is_a: MONDO:7770004 {source="https://www.clinicalgenome.org/affiliation/40104/"} ! SCN5A-related cardiac rhythm disorder
 intersection_of: MONDO:0100234 ! paroxysmal familial ventricular fibrillation
 intersection_of: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/10593 ! SCN5A
 relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/10593 {source="OMIM:603829"} ! SCN5A
@@ -267562,6 +267567,7 @@ xref: Orphanet:101016 {source="OMIM:603830", source="MONDO:directSiblingOf"}
 xref: Orphanet:768 {source="OMIM:603830"}
 xref: UMLS:C1859062 {source="MONDO:equivalentTo", source="MONDO:MEDGEN", source="MEDGEN:349087"}
 is_a: MONDO:0019171 {source="OMIM:603830", source="Orphanet:101016-prototype"} ! familial long QT syndrome
+is_a: MONDO:7770004 {source="https://www.clinicalgenome.org/affiliation/40104/"} ! SCN5A-related cardiac rhythm disorder
 intersection_of: MONDO:0019171 ! familial long QT syndrome
 intersection_of: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/10593 ! SCN5A
 relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/10593 {source="OMIM:603830"} ! SCN5A
@@ -285573,6 +285579,7 @@ xref: Orphanet:166282 {source="MONDO:equivalentTo", source="OMIM:608567"}
 xref: SCTID:233913007 {source="MONDO:equivalentTo"}
 xref: UMLS:C0340491 {source="MONDO:equivalentTo", source="MONDO:MEDGEN", source="MEDGEN:573766"}
 is_a: MONDO:0001823 {source="DC-OMIM:608567", source="MESH:C563907", source="MONDO:Redundant", source="OMIM:608567"} ! sick sinus syndrome
+is_a: MONDO:7770003 {source="https://www.clinicalgenome.org/affiliation/40104/"} ! cardiogenetic rhythm disorders
 intersection_of: MONDO:0001823 ! sick sinus syndrome
 intersection_of: has_characteristic MONDO:0021152 ! inherited
 relationship: has_characteristic MONDO:0021152 {source="OMIMPS:608567"} ! inherited
@@ -323947,6 +323954,7 @@ xref: OMIM:614022 {source="MONDO:equivalentTo"}
 xref: Orphanet:334 {source="OMIM:614022"}
 xref: UMLS:C3151464 {source="MEDGEN:462814", source="MONDO:equivalentTo", source="MONDO:MEDGEN"}
 is_a: MONDO:0018054 {source="DC-OMIM:614022", source="MONDO:Redundant", source="OMIM:614022"} ! familial atrial fibrillation
+is_a: MONDO:7770004 {source="https://www.clinicalgenome.org/affiliation/40104/"} ! SCN5A-related cardiac rhythm disorder
 intersection_of: MONDO:0018054 ! familial atrial fibrillation
 intersection_of: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/10593 ! SCN5A
 relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/10593 {source="OMIM:614022"} ! SCN5A
@@ -349658,6 +349666,7 @@ xref: OMIM:616117 {source="Orphanet:436242/e", source="EFO:0005304", source="MON
 xref: Orphanet:436242 {source="MONDO:equivalentTo"}
 xref: UMLS:C4015285 {source="MEDGEN:863722", source="MONDO:equivalentTo", source="MONDO:MEDGEN"}
 is_a: MONDO:0005449 {source="EFO:0005304"} ! conduction system disorder
+is_a: MONDO:7770003 {source="https://www.clinicalgenome.org/affiliation/40104/"} ! cardiogenetic rhythm disorders
 relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/19661 {source="OMIM:616117"} ! TNNI3K
 property_value: curated_content_resource "https://www.malacards.org/card/cardiac_conduction_disease_with_or_without_dilated_cardiomyopathy" xsd:anyURI {source="MONDO:MalaCards"}
 
@@ -367966,6 +367975,7 @@ xref: SCTID:418818005 {source="DOID:0050451", source="MONDO:equivalentTo"}
 xref: UMLS:C1142166 {source="MONDO:equivalentTo", source="MONDO:MEDGEN", source="MEDGEN:222975"}
 is_a: MONDO:0000992 {source="DOID:0050451", source="MONDO:Redundant", source="MONDO:indirect"} ! heart conduction disease
 is_a: MONDO:0002254 {source="NCIT:C142891"} ! syndromic disease
+is_a: MONDO:7770003 {source="https://www.clinicalgenome.org/affiliation/40104/"} ! cardiogenetic rhythm disorders
 relationship: curated_content_resource https://search.clinicalgenome.org/kb/conditions/MONDO:0015263 {source="MONDO:CLINGEN"}
 relationship: has_characteristic MONDO:0021152 {source="OMIMPS:601144"} ! inherited
 property_value: curated_content_resource "https://www.malacards.org/card/brugada_syndrome" xsd:anyURI {source="MONDO:MalaCards"}
@@ -426973,6 +426983,7 @@ xref: Orphanet:334 {source="DOID:0050650", source="MONDO:equivalentTo"}
 xref: SCTID:715395008 {source="MONDO:equivalentTo"}
 xref: UMLS:C3468561 {source="MONDO:equivalentTo", source="MONDO:MEDGEN", source="MEDGEN:894635"}
 is_a: MONDO:0004981 {source="DOID:0050650", source="MONDO:DOID", source="MONDO:Redundant"} ! atrial fibrillation
+is_a: MONDO:7770003 {source="https://www.clinicalgenome.org/affiliation/40104/"} ! cardiogenetic rhythm disorders
 intersection_of: MONDO:0004981 ! atrial fibrillation
 intersection_of: has_characteristic MONDO:0021152 ! inherited
 relationship: has_characteristic MONDO:0021152 {source="OMIMPS:608583"} ! inherited
@@ -460887,6 +460898,7 @@ xref: Orphanet:871 {source="MONDO:equivalentTo", source="DOID:0111073"}
 xref: SCTID:698249005 {source="MONDO:equivalentTo"}
 xref: SCTID:93130009 {source="MONDO:equivalentObsolete"}
 is_a: MONDO:0000992 {source="DOID:0111073", source="MONDO:indirect"} ! heart conduction disease
+is_a: MONDO:7770003 {source="https://www.clinicalgenome.org/affiliation/40104/"} ! cardiogenetic rhythm disorders
 relationship: has_characteristic MONDO:0021152 {source="OMIMPS:113900"} ! inherited
 property_value: curated_content_resource "https://www.malacards.org/card/familial_progressive_cardiac_conduction_defect" xsd:anyURI {source="MONDO:MalaCards"}
 property_value: curated_content_resource "https://www.malacards.org/card/progressive_familial_heart_block" xsd:anyURI {source="MONDO:MalaCards"}
@@ -513335,6 +513347,7 @@ xref: OMIM:608567 {source="MONDO:equivalentTo"}
 xref: Orphanet:166282 {source="OMIM:608567"}
 xref: UMLS:C1837845 {source="MONDO:equivalentTo", source="MONDO:MEDGEN", source="MEDGEN:325270"}
 is_a: MONDO:0012061 {source="MONDO:0024562/inferred", source="MONDO:Redundant", source="OMIM:608567"} ! familial sick sinus syndrome
+is_a: MONDO:7770004 {source="https://www.clinicalgenome.org/affiliation/40104/"} ! SCN5A-related cardiac rhythm disorder
 intersection_of: MONDO:0012061 ! familial sick sinus syndrome
 intersection_of: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/10593 ! SCN5A
 relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/10593 {source="OMIM:608567"} ! SCN5A
@@ -621534,6 +621547,25 @@ is_a: MONDO:0005451 {source="PMID:38849953"} ! eating disorder
 property_value: http://purl.org/dc/terms/creator https://orcid.org/0000-0003-3311-7320
 property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9408" xsd:anyURI
 
+[Term]
+id: MONDO:7770003
+name: cardiogenetic rhythm disorders
+def: "A heterogeneous group of cardiac rhythm phenotypes with a monogenic etiology that include, but are not limited to, atrial fibrillation, sick sinus syndrome, progressive cardiac conduction disease, ventricular fibrillation, Brugada syndrome, long QT syndrome, short QT syndrome, tachycardia with fibrillation, etc." [https://www.clinicalgenome.org/affiliation/40104/]
+is_a: MONDO:0100547 {source="https://www.clinicalgenome.org/affiliation/40104/"} ! cardiogenetic disease
+property_value: http://purl.org/dc/terms/creator https://orcid.org/0000-0002-7638-4659
+property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9707" xsd:anyURI
+
+[Term]
+id: MONDO:7770004
+name: SCN5A-related cardiac rhythm disorder
+def: "A heterogeneous collection of cardiac rhythm disorders caused by genetic variation in the SCN5A gene with autosomal dominant inheritance. Affected individuals are commonly reported to have unremarkable cardiac morphology and at least one cardiac rhythm phenotype that includes, but is not limited to, atrial fibrillation, sick sinus syndrome, progressive cardiac conduction disease, ventricular fibrillation, long QT syndrome, and Brugada syndrome. Individuals with pathogenic variants in SCN5A may also exhibit overlapping or mixed cardiac rhythm phenotypes and intrafamilial variability." [https://www.clinicalgenome.org/affiliation/40104/]
+is_a: MONDO:0100547 {source="https://www.clinicalgenome.org/affiliation/40104/"} ! cardiogenetic disease
+is_a: MONDO:0007263 {source="https://www.clinicalgenome.org/affiliation/40104/"} ! cardiac rhythm disease
+is_a: MONDO:7770003 {source="https://www.clinicalgenome.org/affiliation/40104/"} ! cardiogenetic rhythm disorders
+relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/10593 {source="https://www.clinicalgenome.org/affiliation/40104/"} ! SCN5A
+property_value: http://purl.org/dc/terms/creator https://orcid.org/0000-0002-7638-4659
+property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9707" xsd:anyURI
+
 [Term]
 id: MONDO:8000000
 name: infectious discitis

```

### Attempt 5: claude-opus-4.7 / claude

- **Eval PR**: [#407](https://github.com/ai4curation/eval-ont-agent-mondo/pull/407)
- **F1**: 0.311  **Precision**: 0.292  **Recall**: 0.333  **Jaccard**: 0.184
- **Trace**: [25819422715](https://github.com/ai4curation/eval-ont-agent-mondo/tree/master/traces/25819422715)
- **Workflow run**: [25819422715](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25819422715)

#### Agent PR Comment

# SCN5A-related cardiac rhythm disorder and cardiogenetic rhythm disorder (issue #9707)

Implements the ClinGen Hereditary Cardiovascular Disease GCEP request (affiliation 40104) to add an SCN5A umbrella disease term and a new monogenic-rhythm-disease parent, and to reorganize the affected children.

## New terms

### MONDO:7770003 — cardiogenetic rhythm disorder
- **def**: "A heterogeneous group of cardiac rhythm phenotypes with a monogenic etiology that include, but are not limited to, atrial fibrillation, sick sinus syndrome, progressive cardiac conduction disease, ventricular fibrillation, Brugada syndrome, long QT syndrome, short QT syndrome, tachycardia with fibrillation, etc." (sourced to ClinGen affiliation 40104; uses the revised wording from @LengUNC's follow-up comment).
- **parents**: `cardiac rhythm disease` (MONDO:0007263), `cardiogenetic disease` (MONDO:0100547).
- **logical definition**: `cardiac rhythm disease` and `has_characteristic` some `inherited` (MONDO:0021152). This mirrors the equivalence axiom for `cardiogenetic disease` so the new term sits cleanly underneath both parents.
- **term_tracker_item**: github.com/monarch-initiative/mondo/issues/9707.

### MONDO:7770004 — SCN5A-related cardiac rhythm disorder
- **def**: revised definition from @LengUNC's follow-up comment (multifocal ectopic Purkinje-related premature contractions removed).
- **parent**: `cardiogenetic rhythm disorder` (MONDO:7770003) only. The two other parents listed in the request (`cardiogenetic disease`, `cardiac rhythm disease`) are entailed via MONDO:7770003 and were left for the reasoner.
- **logical definition** (disease_series_by_gene pattern): `cardiogenetic rhythm disorder` and `has_material_basis_in_germline_mutation_in` some `SCN5A` (`http://identifiers.org/hgnc/10593`). The HGNC ID for SCN5A was verified against existing SCN5A-related MONDO terms.
- **term_tracker_item**: github.com/monarch-initiative/mondo/issues/9707.

## Reparented existing terms

Added `is_a: MONDO:7770004 ! SCN5A-related cardiac rhythm disorder` to the five SCN5A-specific phenotypes:
- MONDO:0013530 atrial fibrillation, familial, 10
- MONDO:0024562 sick sinus syndrome 1
- MONDO:0011376 ventricular fibrillation, paroxysmal familial, type 1
- MONDO:0011377 long QT syndrome 3
- MONDO:0011001 Brugada syndrome 1

Added `is_a: MONDO:7770003 ! cardiogenetic rhythm disorder` to the family-level rhythm terms:
- MONDO:0014500 atrial conduction disease
- MONDO:0015263 Brugada syndrome
- MONDO:0018054 familial atrial fibrillation
- MONDO:0012061 familial sick sinus syndrome
- MONDO:0019490 progressive familial heart block
- MONDO:0000453 short QT syndrome
- MONDO:0008648 ventricular tachycardia, familial
- MONDO:0100234 paroxysmal familial ventricular fibrillation

Existing parents were preserved (per the project's policy of not removing parents unless explicitly requested). The reasoner will mark anything redundant.

## Excluded children

- **atrioventricular block (MONDO:0000465)** — not added under cardiogenetic rhythm disorder, following @katiermullen's curator note that this term does not necessarily have a monogenic etiology.
- The four "Phenotypes EXCLUDED but still associated with SCN5A" listed in the issue (sudden infant death syndrome susceptibility, heart block nonprogressive, heart block progressive type IA, dilated cardiomyopathy 1E) were not added as children of MONDO:7770004.

## Decisions and clarifications

- **"ventricular fibrillation, familial (MONDO:0011376)" in the request**: MONDO:0011376 is actually the SCN5A-specific subtype ("ventricular fibrillation, paroxysmal familial, type 1"); the only generic family-level term is MONDO:0100234 ("paroxysmal familial ventricular fibrillation"). Other entries in the same list (e.g., familial atrial fibrillation MONDO:0018054) are generic family-level terms, so MONDO:0100234 was attached as the direct child of MONDO:7770003. MONDO:0011376 still inherits cardiogenetic rhythm disorder transitively via MONDO:7770004. Flagged in the issue comment for confirmation.
- **Inheritance not in the logical definition for SCN5A-related term**: the request mentions autosomal dominant inheritance, but several SCN5A children include autosomal-recessive forms (e.g., SSS1 / OMIM:608567 has an autosomal-recessive synonym). Inheritance is retained in the textual definition but not in the equivalence axiom, so the term covers all reported SCN5A rhythm phenotypes.
- **Creator/source**: ClinGen affiliation URL (`https://clinicalgenome.org/affiliation/40104/`) used as the source on the new term, on the new parents, and on the new is_a relationships of reparented children, consistent with similar GCEP-attributed terms (e.g., MONDO:0700349 ACTN2-related cardiac and skeletal myopathy). No `dc:creator` ORCID was added since no individual curator ORCID was identified in the issue.

## Validation

- Verified all referenced MONDO IDs (parents and children) by lookup in `src/ontology/mondo-edit.obo`.
- Verified the HGNC identifier for SCN5A (10593) by cross-referencing existing SCN5A-related terms.
- Followed the `disease_series_by_gene` DOSDP pattern for MONDO:7770004 (`src/patterns/dosdp-patterns/disease_series_by_gene.yaml`).
- ROBOT/owltools were not available in this environment, so the standard `robot convert` validation and `make NORM` normalization could not be executed. The file passes basic OBO structural checks (every `[Term]` stanza has an id; new stanza placement preserved by `obo-checkin.pl`). A NORM step is expected to run in CI.

## Checklist
- [x] New term IDs do not clash (greppd `MONDO:777`)
- [x] All references and IDs verified against `mondo-edit.obo`
- [x] Definitions match the corrected wording from @LengUNC's follow-up comment
- [x] Existing parents of reparented children left intact
- [x] term_tracker_item points to the originating issue
- [x] Curator note about atrioventricular block respected

---
🤖 **Generated by claude agent**
- Runtime: `claude`
- Model: `claude-opus-4-7`
- Agent config: `ai4curation/mondo-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25819422715)


#### Agent Issue Comment

Thanks @LengUNC — both terms have been added per the revised definitions in PR #<NN>:

- **MONDO:7770003** cardiogenetic rhythm disorder (parents: cardiac rhythm disease, cardiogenetic disease)
- **MONDO:7770004** SCN5A-related cardiac rhythm disorder (parented to cardiogenetic rhythm disorder; logical def via SCN5A / HGNC:10593)

The five SCN5A child phenotypes (atrial fibrillation, familial, 10; sick sinus syndrome 1; ventricular fibrillation, paroxysmal familial, type 1; long QT syndrome 3; Brugada syndrome 1) have been reparented under the new SCN5A-related term, and the broader family-level rhythm terms have been added as children of cardiogenetic rhythm disorder.

Per @katiermullen's earlier comment, atrioventricular block (MONDO:0000465) was not included as a child of cardiogenetic rhythm disorder because that condition does not necessarily have a monogenic etiology. If a specific monogenic AV block term is needed, please open a follow-up with a source.

One small note: the request listed "ventricular fibrillation, familial (MONDO:0011376)" as a child of cardiogenetic rhythm disorder, but MONDO:0011376 is the SCN5A-specific subtype. Following the family/generic-term pattern used for the other entries in that list, MONDO:0100234 (paroxysmal familial ventricular fibrillation) was added as a direct child of cardiogenetic rhythm disorder; MONDO:0011376 is now a child of SCN5A-related cardiac rhythm disorder and inherits transitively. Please flag if a different mapping is preferred.

---
🤖 **Generated by claude agent**
- Runtime: `claude`
- Model: `claude-opus-4-7`
- Agent config: `ai4curation/mondo-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25819422715)


#### Agent Diff

```diff
diff --git a/src/ontology/mondo-edit.obo b/src/ontology/mondo-edit.obo
index 8aaf2a57d..f773034cb 100644
--- a/src/ontology/mondo-edit.obo
+++ b/src/ontology/mondo-edit.obo
@@ -5867,6 +5867,7 @@ xref: Orphanet:51083 {source="MONDO:equivalentTo", source="OMIM:609620"}
 xref: SCTID:698272007 {source="MONDO:equivalentTo"}
 xref: UMLS:C2348199 {source="MONDO:equivalentTo", source="MONDO:MEDGEN", source="MEDGEN:378835"}
 is_a: MONDO:0000992 {source="DOID:0050793"} ! heart conduction disease
+is_a: MONDO:7770003 {source="https://clinicalgenome.org/affiliation/40104/"} ! cardiogenetic rhythm disorder
 relationship: curated_content_resource https://search.clinicalgenome.org/kb/conditions/MONDO:0000453 {source="MONDO:CLINGEN"}
 relationship: has_characteristic MONDO:0021152 {source="OMIMPS:609620"} ! inherited
 property_value: curated_content_resource "https://www.malacards.org/card/familial_short_qt_syndrome" xsd:anyURI {source="MONDO:MalaCards"}
@@ -188784,6 +188785,7 @@ xref: OMIM:192605 {source="MONDO:equivalentTo"}
 xref: SCTID:233906007 {source="MONDO:equivalentTo"}
 xref: UMLS:C0340485 {source="MONDO:equivalentTo", source="MONDO:MEDGEN", source="MEDGEN:83309"}
 is_a: MONDO:0005477 {source="MONDO:Redundant", source="OMIM:192605"} ! ventricular tachycardia
+is_a: MONDO:7770003 {source="https://clinicalgenome.org/affiliation/40104/"} ! cardiogenetic rhythm disorder
 intersection_of: MONDO:0005477 ! ventricular tachycardia
 intersection_of: has_characteristic MONDO:0021152 ! inherited
 relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/4385 {source="OMIM:192605"} ! GNAI2
@@ -257842,6 +257844,7 @@ xref: OMIM:601144 {source="DOID:0110218", source="MONDO:equivalentTo"}
 xref: Orphanet:130 {source="OMIM:601144"}
 xref: UMLS:C4551804 {source="MONDO:equivalentTo", source="MONDO:MEDGEN", source="MEDGEN:1646402"}
 is_a: MONDO:0015263 {source="DC-OMIM:601144", source="DOID:0110218", source="MONDO:Redundant", source="OMIM:601144"} ! Brugada syndrome
+is_a: MONDO:7770004 {source="https://clinicalgenome.org/affiliation/40104/"} ! SCN5A-related cardiac rhythm disorder
 intersection_of: MONDO:0015263 ! Brugada syndrome
 intersection_of: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/10593 ! SCN5A
 relationship: curated_content_resource https://search.clinicalgenome.org/kb/conditions/MONDO:0011001 {source="MONDO:CLINGEN"}
@@ -267530,6 +267533,7 @@ xref: Orphanet:228140 {source="OMIM:603829"}
 xref: SCTID:233915000 {source="MONDO:equivalentTo"}
 xref: UMLS:C2751898 {source="MEDGEN:414502", source="MONDO:equivalentTo", source="MONDO:MEDGEN"}
 is_a: MONDO:0100234 {source="DC-OMIM:603829", source="MESH:C567851"} ! paroxysmal familial ventricular fibrillation
+is_a: MONDO:7770004 {source="https://clinicalgenome.org/affiliation/40104/"} ! SCN5A-related cardiac rhythm disorder
 intersection_of: MONDO:0100234 ! paroxysmal familial ventricular fibrillation
 intersection_of: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/10593 ! SCN5A
 relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/10593 {source="OMIM:603829"} ! SCN5A
@@ -267562,6 +267566,7 @@ xref: Orphanet:101016 {source="OMIM:603830", source="MONDO:directSiblingOf"}
 xref: Orphanet:768 {source="OMIM:603830"}
 xref: UMLS:C1859062 {source="MONDO:equivalentTo", source="MONDO:MEDGEN", source="MEDGEN:349087"}
 is_a: MONDO:0019171 {source="OMIM:603830", source="Orphanet:101016-prototype"} ! familial long QT syndrome
+is_a: MONDO:7770004 {source="https://clinicalgenome.org/affiliation/40104/"} ! SCN5A-related cardiac rhythm disorder
 intersection_of: MONDO:0019171 ! familial long QT syndrome
 intersection_of: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/10593 ! SCN5A
 relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/10593 {source="OMIM:603830"} ! SCN5A
@@ -285573,6 +285578,7 @@ xref: Orphanet:166282 {source="MONDO:equivalentTo", source="OMIM:608567"}
 xref: SCTID:233913007 {source="MONDO:equivalentTo"}
 xref: UMLS:C0340491 {source="MONDO:equivalentTo", source="MONDO:MEDGEN", source="MEDGEN:573766"}
 is_a: MONDO:0001823 {source="DC-OMIM:608567", source="MESH:C563907", source="MONDO:Redundant", source="OMIM:608567"} ! sick sinus syndrome
+is_a: MONDO:7770003 {source="https://clinicalgenome.org/affiliation/40104/"} ! cardiogenetic rhythm disorder
 intersection_of: MONDO:0001823 ! sick sinus syndrome
 intersection_of: has_characteristic MONDO:0021152 ! inherited
 relationship: has_characteristic MONDO:0021152 {source="OMIMPS:608567"} ! inherited
@@ -323947,6 +323953,7 @@ xref: OMIM:614022 {source="MONDO:equivalentTo"}
 xref: Orphanet:334 {source="OMIM:614022"}
 xref: UMLS:C3151464 {source="MEDGEN:462814", source="MONDO:equivalentTo", source="MONDO:MEDGEN"}
 is_a: MONDO:0018054 {source="DC-OMIM:614022", source="MONDO:Redundant", source="OMIM:614022"} ! familial atrial fibrillation
+is_a: MONDO:7770004 {source="https://clinicalgenome.org/affiliation/40104/"} ! SCN5A-related cardiac rhythm disorder
 intersection_of: MONDO:0018054 ! familial atrial fibrillation
 intersection_of: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/10593 ! SCN5A
 relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/10593 {source="OMIM:614022"} ! SCN5A
@@ -349658,6 +349665,7 @@ xref: OMIM:616117 {source="Orphanet:436242/e", source="EFO:0005304", source="MON
 xref: Orphanet:436242 {source="MONDO:equivalentTo"}
 xref: UMLS:C4015285 {source="MEDGEN:863722", source="MONDO:equivalentTo", source="MONDO:MEDGEN"}
 is_a: MONDO:0005449 {source="EFO:0005304"} ! conduction system disorder
+is_a: MONDO:7770003 {source="https://clinicalgenome.org/affiliation/40104/"} ! cardiogenetic rhythm disorder
 relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/19661 {source="OMIM:616117"} ! TNNI3K
 property_value: curated_content_resource "https://www.malacards.org/card/cardiac_conduction_disease_with_or_without_dilated_cardiomyopathy" xsd:anyURI {source="MONDO:MalaCards"}
 
@@ -367966,6 +367974,7 @@ xref: SCTID:418818005 {source="DOID:0050451", source="MONDO:equivalentTo"}
 xref: UMLS:C1142166 {source="MONDO:equivalentTo", source="MONDO:MEDGEN", source="MEDGEN:222975"}
 is_a: MONDO:0000992 {source="DOID:0050451", source="MONDO:Redundant", source="MONDO:indirect"} ! heart conduction disease
 is_a: MONDO:0002254 {source="NCIT:C142891"} ! syndromic disease
+is_a: MONDO:7770003 {source="https://clinicalgenome.org/affiliation/40104/"} ! cardiogenetic rhythm disorder
 relationship: curated_content_resource https://search.clinicalgenome.org/kb/conditions/MONDO:0015263 {source="MONDO:CLINGEN"}
 relationship: has_characteristic MONDO:0021152 {source="OMIMPS:601144"} ! inherited
 property_value: curated_content_resource "https://www.malacards.org/card/brugada_syndrome" xsd:anyURI {source="MONDO:MalaCards"}
@@ -426973,6 +426982,7 @@ xref: Orphanet:334 {source="DOID:0050650", source="MONDO:equivalentTo"}
 xref: SCTID:715395008 {source="MONDO:equivalentTo"}
 xref: UMLS:C3468561 {source="MONDO:equivalentTo", source="MONDO:MEDGEN", source="MEDGEN:894635"}
 is_a: MONDO:0004981 {source="DOID:0050650", source="MONDO:DOID", source="MONDO:Redundant"} ! atrial fibrillation
+is_a: MONDO:7770003 {source="https://clinicalgenome.org/affiliation/40104/"} ! cardiogenetic rhythm disorder
 intersection_of: MONDO:0004981 ! atrial fibrillation
 intersection_of: has_characteristic MONDO:0021152 ! inherited
 relationship: has_characteristic MONDO:0021152 {source="OMIMPS:608583"} ! inherited
@@ -460887,6 +460897,7 @@ xref: Orphanet:871 {source="MONDO:equivalentTo", source="DOID:0111073"}
 xref: SCTID:698249005 {source="MONDO:equivalentTo"}
 xref: SCTID:93130009 {source="MONDO:equivalentObsolete"}
 is_a: MONDO:0000992 {source="DOID:0111073", source="MONDO:indirect"} ! heart conduction disease
+is_a: MONDO:7770003 {source="https://clinicalgenome.org/affiliation/40104/"} ! cardiogenetic rhythm disorder
 relationship: has_characteristic MONDO:0021152 {source="OMIMPS:113900"} ! inherited
 property_value: curated_content_resource "https://www.malacards.org/card/familial_progressive_cardiac_conduction_defect" xsd:anyURI {source="MONDO:MalaCards"}
 property_value: curated_content_resource "https://www.malacards.org/card/progressive_familial_heart_block" xsd:anyURI {source="MONDO:MalaCards"}
@@ -513335,6 +513346,7 @@ xref: OMIM:608567 {source="MONDO:equivalentTo"}
 xref: Orphanet:166282 {source="OMIM:608567"}
 xref: UMLS:C1837845 {source="MONDO:equivalentTo", source="MONDO:MEDGEN", source="MEDGEN:325270"}
 is_a: MONDO:0012061 {source="MONDO:0024562/inferred", source="MONDO:Redundant", source="OMIM:608567"} ! familial sick sinus syndrome
+is_a: MONDO:7770004 {source="https://clinicalgenome.org/affiliation/40104/"} ! SCN5A-related cardiac rhythm disorder
 intersection_of: MONDO:0012061 ! familial sick sinus syndrome
 intersection_of: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/10593 ! SCN5A
 relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/10593 {source="OMIM:608567"} ! SCN5A
@@ -561829,6 +561841,7 @@ xref: MEDGEN:83310 {source="MONDO:equivalentTo", source="MONDO:MEDGEN"}
 xref: Orphanet:228140 {source="MONDO:equivalentTo", source="OMIM:603829"}
 xref: UMLS:C0340493 {source="MEDGEN:83310", source="MONDO:equivalentTo", source="MONDO:MEDGEN"}
 is_a: MONDO:0000190 {source="https://orcid.org/0000-0001-5208-3432"} ! ventricular fibrillation
+is_a: MONDO:7770003 {source="https://clinicalgenome.org/affiliation/40104/"} ! cardiogenetic rhythm disorder
 property_value: curated_content_resource "https://www.malacards.org/card/paroxysmal_familial_ventricular_fibrillation" xsd:anyURI {source="MONDO:MalaCards"}
 property_value: http://purl.org/dc/terms/creator https://orcid.org/0000-0001-5208-3432
 property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/2524" xsd:anyURI
@@ -621534,6 +621547,31 @@ is_a: MONDO:0005451 {source="PMID:38849953"} ! eating disorder
 property_value: http://purl.org/dc/terms/creator https://orcid.org/0000-0003-3311-7320
 property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9408" xsd:anyURI
 
+[Term]
+id: MONDO:7770003
+name: cardiogenetic rhythm disorder
+def: "A heterogeneous group of cardiac rhythm phenotypes with a monogenic etiology that include, but are not limited to, atrial fibrillation, sick sinus syndrome, progressive cardiac conduction disease, ventricular fibrillation, Brugada syndrome, long QT syndrome, short QT syndrome, tachycardia with fibrillation, etc." [https://clinicalgenome.org/affiliation/40104/]
+synonym: "cardiogenetic rhythm disorders" EXACT [https://clinicalgenome.org/affiliation/40104/]
+synonym: "hereditary cardiac rhythm disease" EXACT [https://clinicalgenome.org/affiliation/40104/]
+is_a: MONDO:0007263 {source="https://clinicalgenome.org/affiliation/40104/"} ! cardiac rhythm disease
+is_a: MONDO:0100547 {source="https://clinicalgenome.org/affiliation/40104/"} ! cardiogenetic disease
+intersection_of: MONDO:0007263 ! cardiac rhythm disease
+intersection_of: has_characteristic MONDO:0021152 ! inherited
+relationship: has_characteristic MONDO:0021152 {source="https://clinicalgenome.org/affiliation/40104/"} ! inherited
+property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9707" xsd:anyURI
+
+[Term]
+id: MONDO:7770004
+name: SCN5A-related cardiac rhythm disorder
+def: "A heterogeneous collection of cardiac rhythm disorders caused by genetic variation in the SCN5A gene with autosomal dominant inheritance. Affected individuals are commonly reported to have unremarkable cardiac morphology and at least one cardiac rhythm phenotype that includes, but is not limited to, atrial fibrillation, sick sinus syndrome, progressive cardiac conduction disease, ventricular fibrillation, long QT syndrome, and Brugada syndrome. Individuals with pathogenic variants in SCN5A may also exhibit overlapping or mixed cardiac rhythm phenotypes and intrafamilial variability." [https://clinicalgenome.org/affiliation/40104/]
+synonym: "SCN5A cardiac rhythm disorder" EXACT [https://clinicalgenome.org/affiliation/40104/]
+synonym: "SCN5A-related cardiac arrhythmia" RELATED [https://clinicalgenome.org/affiliation/40104/]
+is_a: MONDO:7770003 {source="https://clinicalgenome.org/affiliation/40104/"} ! cardiogenetic rhythm disorder
+intersection_of: MONDO:7770003 ! cardiogenetic rhythm disorder
+intersection_of: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/10593 ! SCN5A
+relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/10593 {source="https://clinicalgenome.org/affiliation/40104/"} ! SCN5A
+property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9707" xsd:anyURI
+
 [Term]
 id: MONDO:8000000
 name: infectious discitis

```

### Attempt 6: gpt-5.5 / opencode

- **Eval PR**: [#89](https://github.com/ai4curation/eval-ont-agent-mondo/pull/89)
- **F1**: 0.311  **Precision**: 0.292  **Recall**: 0.333  **Jaccard**: 0.184
- **Trace**: [25615981305](https://github.com/ai4curation/eval-ont-agent-mondo/tree/master/traces/25615981305)
- **Workflow run**: [25615981305](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25615981305)

#### Agent PR Comment

## Summary

Addressed issue #9707 by adding two new MONDO terms requested by the ClinGen Hereditary Cardiovascular Disease GCEP:

- `MONDO:7770003` cardiogenetic rhythm disorder
- `MONDO:7770004` SCN5A-related cardiac rhythm disorder

#### Agent Issue Comment

Changes committed in PR #<NN>.

Implemented the two requested terms using the revised definitions, and omitted atrioventricular block from the new cardiogenetic rhythm disorder hierarchy because it is not necessarily monogenic.

---
🤖 **Generated by pi agent**
- Runtime: `pi`
- Model: `openai/gpt-5.5`
- Agent config: `ai4curation/mondo-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25615981305)

#### Agent Diff

```diff
diff --git a/src/ontology/mondo-edit.obo b/src/ontology/mondo-edit.obo
index 8aaf2a57d..9617ce88b 100644
--- a/src/ontology/mondo-edit.obo
+++ b/src/ontology/mondo-edit.obo
@@ -5867,6 +5867,7 @@ xref: Orphanet:51083 {source="MONDO:equivalentTo", source="OMIM:609620"}
 xref: SCTID:698272007 {source="MONDO:equivalentTo"}
 xref: UMLS:C2348199 {source="MONDO:equivalentTo", source="MONDO:MEDGEN", source="MEDGEN:378835"}
 is_a: MONDO:0000992 {source="DOID:0050793"} ! heart conduction disease
+is_a: MONDO:7770003 {source="https://clinicalgenome.org/affiliation/40104/"} ! cardiogenetic rhythm disorder
 relationship: curated_content_resource https://search.clinicalgenome.org/kb/conditions/MONDO:0000453 {source="MONDO:CLINGEN"}
 relationship: has_characteristic MONDO:0021152 {source="OMIMPS:609620"} ! inherited
 property_value: curated_content_resource "https://www.malacards.org/card/familial_short_qt_syndrome" xsd:anyURI {source="MONDO:MalaCards"}
@@ -188784,6 +188785,7 @@ xref: OMIM:192605 {source="MONDO:equivalentTo"}
 xref: SCTID:233906007 {source="MONDO:equivalentTo"}
 xref: UMLS:C0340485 {source="MONDO:equivalentTo", source="MONDO:MEDGEN", source="MEDGEN:83309"}
 is_a: MONDO:0005477 {source="MONDO:Redundant", source="OMIM:192605"} ! ventricular tachycardia
+is_a: MONDO:7770003 {source="https://clinicalgenome.org/affiliation/40104/"} ! cardiogenetic rhythm disorder
 intersection_of: MONDO:0005477 ! ventricular tachycardia
 intersection_of: has_characteristic MONDO:0021152 ! inherited
 relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/4385 {source="OMIM:192605"} ! GNAI2
@@ -257842,6 +257844,7 @@ xref: OMIM:601144 {source="DOID:0110218", source="MONDO:equivalentTo"}
 xref: Orphanet:130 {source="OMIM:601144"}
 xref: UMLS:C4551804 {source="MONDO:equivalentTo", source="MONDO:MEDGEN", source="MEDGEN:1646402"}
 is_a: MONDO:0015263 {source="DC-OMIM:601144", source="DOID:0110218", source="MONDO:Redundant", source="OMIM:601144"} ! Brugada syndrome
+is_a: MONDO:7770004 {source="https://clinicalgenome.org/affiliation/40104/"} ! SCN5A-related cardiac rhythm disorder
 intersection_of: MONDO:0015263 ! Brugada syndrome
 intersection_of: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/10593 ! SCN5A
 relationship: curated_content_resource https://search.clinicalgenome.org/kb/conditions/MONDO:0011001 {source="MONDO:CLINGEN"}
@@ -267530,6 +267533,8 @@ xref: Orphanet:228140 {source="OMIM:603829"}
 xref: SCTID:233915000 {source="MONDO:equivalentTo"}
 xref: UMLS:C2751898 {source="MEDGEN:414502", source="MONDO:equivalentTo", source="MONDO:MEDGEN"}
 is_a: MONDO:0100234 {source="DC-OMIM:603829", source="MESH:C567851"} ! paroxysmal familial ventricular fibrillation
+is_a: MONDO:7770003 {source="https://clinicalgenome.org/affiliation/40104/"} ! cardiogenetic rhythm disorder
+is_a: MONDO:7770004 {source="https://clinicalgenome.org/affiliation/40104/"} ! SCN5A-related cardiac rhythm disorder
 intersection_of: MONDO:0100234 ! paroxysmal familial ventricular fibrillation
 intersection_of: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/10593 ! SCN5A
 relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/10593 {source="OMIM:603829"} ! SCN5A
@@ -267562,6 +267567,7 @@ xref: Orphanet:101016 {source="OMIM:603830", source="MONDO:directSiblingOf"}
 xref: Orphanet:768 {source="OMIM:603830"}
 xref: UMLS:C1859062 {source="MONDO:equivalentTo", source="MONDO:MEDGEN", source="MEDGEN:349087"}
 is_a: MONDO:0019171 {source="OMIM:603830", source="Orphanet:101016-prototype"} ! familial long QT syndrome
+is_a: MONDO:7770004 {source="https://clinicalgenome.org/affiliation/40104/"} ! SCN5A-related cardiac rhythm disorder
 intersection_of: MONDO:0019171 ! familial long QT syndrome
 intersection_of: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/10593 ! SCN5A
 relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/10593 {source="OMIM:603830"} ! SCN5A
@@ -285573,6 +285579,7 @@ xref: Orphanet:166282 {source="MONDO:equivalentTo", source="OMIM:608567"}
 xref: SCTID:233913007 {source="MONDO:equivalentTo"}
 xref: UMLS:C0340491 {source="MONDO:equivalentTo", source="MONDO:MEDGEN", source="MEDGEN:573766"}
 is_a: MONDO:0001823 {source="DC-OMIM:608567", source="MESH:C563907", source="MONDO:Redundant", source="OMIM:608567"} ! sick sinus syndrome
+is_a: MONDO:7770003 {source="https://clinicalgenome.org/affiliation/40104/"} ! cardiogenetic rhythm disorder
 intersection_of: MONDO:0001823 ! sick sinus syndrome
 intersection_of: has_characteristic MONDO:0021152 ! inherited
 relationship: has_characteristic MONDO:0021152 {source="OMIMPS:608567"} ! inherited
@@ -323947,6 +323954,7 @@ xref: OMIM:614022 {source="MONDO:equivalentTo"}
 xref: Orphanet:334 {source="OMIM:614022"}
 xref: UMLS:C3151464 {source="MEDGEN:462814", source="MONDO:equivalentTo", source="MONDO:MEDGEN"}
 is_a: MONDO:0018054 {source="DC-OMIM:614022", source="MONDO:Redundant", source="OMIM:614022"} ! familial atrial fibrillation
+is_a: MONDO:7770004 {source="https://clinicalgenome.org/affiliation/40104/"} ! SCN5A-related cardiac rhythm disorder
 intersection_of: MONDO:0018054 ! familial atrial fibrillation
 intersection_of: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/10593 ! SCN5A
 relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/10593 {source="OMIM:614022"} ! SCN5A
@@ -349658,6 +349666,7 @@ xref: OMIM:616117 {source="Orphanet:436242/e", source="EFO:0005304", source="MON
 xref: Orphanet:436242 {source="MONDO:equivalentTo"}
 xref: UMLS:C4015285 {source="MEDGEN:863722", source="MONDO:equivalentTo", source="MONDO:MEDGEN"}
 is_a: MONDO:0005449 {source="EFO:0005304"} ! conduction system disorder
+is_a: MONDO:7770003 {source="https://clinicalgenome.org/affiliation/40104/"} ! cardiogenetic rhythm disorder
 relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/19661 {source="OMIM:616117"} ! TNNI3K
 property_value: curated_content_resource "https://www.malacards.org/card/cardiac_conduction_disease_with_or_without_dilated_cardiomyopathy" xsd:anyURI {source="MONDO:MalaCards"}
 
@@ -367966,6 +367975,7 @@ xref: SCTID:418818005 {source="DOID:0050451", source="MONDO:equivalentTo"}
 xref: UMLS:C1142166 {source="MONDO:equivalentTo", source="MONDO:MEDGEN", source="MEDGEN:222975"}
 is_a: MONDO:0000992 {source="DOID:0050451", source="MONDO:Redundant", source="MONDO:indirect"} ! heart conduction disease
 is_a: MONDO:0002254 {source="NCIT:C142891"} ! syndromic disease
+is_a: MONDO:7770003 {source="https://clinicalgenome.org/affiliation/40104/"} ! cardiogenetic rhythm disorder
 relationship: curated_content_resource https://search.clinicalgenome.org/kb/conditions/MONDO:0015263 {source="MONDO:CLINGEN"}
 relationship: has_characteristic MONDO:0021152 {source="OMIMPS:601144"} ! inherited
 property_value: curated_content_resource "https://www.malacards.org/card/brugada_syndrome" xsd:anyURI {source="MONDO:MalaCards"}
@@ -426973,6 +426983,7 @@ xref: Orphanet:334 {source="DOID:0050650", source="MONDO:equivalentTo"}
 xref: SCTID:715395008 {source="MONDO:equivalentTo"}
 xref: UMLS:C3468561 {source="MONDO:equivalentTo", source="MONDO:MEDGEN", source="MEDGEN:894635"}
 is_a: MONDO:0004981 {source="DOID:0050650", source="MONDO:DOID", source="MONDO:Redundant"} ! atrial fibrillation
+is_a: MONDO:7770003 {source="https://clinicalgenome.org/affiliation/40104/"} ! cardiogenetic rhythm disorder
 intersection_of: MONDO:0004981 ! atrial fibrillation
 intersection_of: has_characteristic MONDO:0021152 ! inherited
 relationship: has_characteristic MONDO:0021152 {source="OMIMPS:608583"} ! inherited
@@ -460887,6 +460898,7 @@ xref: Orphanet:871 {source="MONDO:equivalentTo", source="DOID:0111073"}
 xref: SCTID:698249005 {source="MONDO:equivalentTo"}
 xref: SCTID:93130009 {source="MONDO:equivalentObsolete"}
 is_a: MONDO:0000992 {source="DOID:0111073", source="MONDO:indirect"} ! heart conduction disease
+is_a: MONDO:7770003 {source="https://clinicalgenome.org/affiliation/40104/"} ! cardiogenetic rhythm disorder
 relationship: has_characteristic MONDO:0021152 {source="OMIMPS:113900"} ! inherited
 property_value: curated_content_resource "https://www.malacards.org/card/familial_progressive_cardiac_conduction_defect" xsd:anyURI {source="MONDO:MalaCards"}
 property_value: curated_content_resource "https://www.malacards.org/card/progressive_familial_heart_block" xsd:anyURI {source="MONDO:MalaCards"}
@@ -513335,6 +513347,7 @@ xref: OMIM:608567 {source="MONDO:equivalentTo"}
 xref: Orphanet:166282 {source="OMIM:608567"}
 xref: UMLS:C1837845 {source="MONDO:equivalentTo", source="MONDO:MEDGEN", source="MEDGEN:325270"}
 is_a: MONDO:0012061 {source="MONDO:0024562/inferred", source="MONDO:Redundant", source="OMIM:608567"} ! familial sick sinus syndrome
+is_a: MONDO:7770004 {source="https://clinicalgenome.org/affiliation/40104/"} ! SCN5A-related cardiac rhythm disorder
 intersection_of: MONDO:0012061 ! familial sick sinus syndrome
 intersection_of: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/10593 ! SCN5A
 relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/10593 {source="OMIM:608567"} ! SCN5A
@@ -621534,6 +621547,33 @@ is_a: MONDO:0005451 {source="PMID:38849953"} ! eating disorder
 property_value: http://purl.org/dc/terms/creator https://orcid.org/0000-0003-3311-7320
 property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9408" xsd:anyURI
 
+[Term]
+id: MONDO:7770003
+name: cardiogenetic rhythm disorder
+def: "A heterogeneous group of cardiac rhythm phenotypes with a monogenic etiology that include, but are not limited to, atrial fibrillation, sick sinus syndrome, progressive cardiac conduction disease, ventricular fibrillation, Brugada syndrome, long QT syndrome, short QT syndrome, and tachycardia with fibrillation." [https://clinicalgenome.org/affiliation/40104/]
+synonym: "cardiogenetic rhythm disorders" EXACT [https://clinicalgenome.org/affiliation/40104/]
+is_a: MONDO:0007263 {source="https://clinicalgenome.org/affiliation/40104/"} ! cardiac rhythm disease
+is_a: MONDO:0100547 {source="https://clinicalgenome.org/affiliation/40104/"} ! cardiogenetic disease
+intersection_of: MONDO:0007263 ! cardiac rhythm disease
+intersection_of: has_characteristic MONDO:0021152 ! inherited
+relationship: has_characteristic MONDO:0021152 {source="https://clinicalgenome.org/affiliation/40104/"} ! inherited
+property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9707" xsd:anyURI
+
+[Term]
+id: MONDO:7770004
+name: SCN5A-related cardiac rhythm disorder
+def: "A heterogeneous collection of cardiac rhythm disorders caused by genetic variation in the SCN5A gene with autosomal dominant inheritance. Affected individuals are commonly reported to have unremarkable cardiac morphology and at least one cardiac rhythm phenotype that includes, but is not limited to, atrial fibrillation, sick sinus syndrome, progressive cardiac conduction disease, ventricular fibrillation, long QT syndrome, and Brugada syndrome. Individuals with pathogenic variants in SCN5A may also exhibit overlapping or mixed cardiac rhythm phenotypes and intrafamilial variability." [https://clinicalgenome.org/affiliation/40104/]
+synonym: "SCN5A cardiac rhythm disorder" EXACT [https://clinicalgenome.org/affiliation/40104/, MONDO:patterns/disease_series_by_gene]
+synonym: "SCN5A related cardiac rhythm disorder" EXACT [https://clinicalgenome.org/affiliation/40104/, MONDO:patterns/disease_series_by_gene]
+synonym: "SCN5A-related cardiac rhythm disorders" EXACT [https://clinicalgenome.org/affiliation/40104/]
+is_a: MONDO:0007263 {source="https://clinicalgenome.org/affiliation/40104/"} ! cardiac rhythm disease
+is_a: MONDO:0100547 {source="https://clinicalgenome.org/affiliation/40104/"} ! cardiogenetic disease
+is_a: MONDO:7770003 {source="https://clinicalgenome.org/affiliation/40104/"} ! cardiogenetic rhythm disorder
+intersection_of: MONDO:7770003 ! cardiogenetic rhythm disorder
+intersection_of: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/10593 ! SCN5A
+relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/10593 {source="https://clinicalgenome.org/affiliation/40104/"} ! SCN5A
+property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9707" xsd:anyURI
+
 [Term]
 id: MONDO:8000000
 name: infectious discitis

```

### Attempt 7: gpt-5.5 / opencode

- **Eval PR**: [#68](https://github.com/ai4curation/eval-ont-agent-mondo/pull/68)
- **F1**: 0.311  **Precision**: 0.292  **Recall**: 0.333  **Jaccard**: 0.184
- **Trace**: [25615939651](https://github.com/ai4curation/eval-ont-agent-mondo/tree/master/traces/25615939651)
- **Workflow run**: [25615939651](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25615939651)

#### Agent PR Comment

## Summary

Added two new MONDO terms requested by the ClinGen Hereditary Cardiovascular Disease GCEP:

- `MONDO:7770003` cardiogenetic rhythm disorder
- `MONDO:7770004` SCN5A-related cardiac rhythm disorder

## Rationale

The issue requested a new SCN5A-related disease entity grouping several SCN5A-associated cardiac rhythm phenotypes, plus a new cardiogenetic rhythm disorder parent. I used the revised definitions from the issue comment that removed multifocal ectopic Purkinje-related premature contractions.

I added source-attributed parentage for the requested included child terms. For cardiogenetic rhythm disorder, I included all requested children except `MONDO:0000465` atrioventricular block, following the issue discussion that atrioventricular block does not necessarily have a monogenic etiology.

## Completed Checklist

- Read imported issue title, body, and comments from `__issue_context__.json`.
- Verified that the requested new terms were not already present locally.
- Checked available `MONDO:777` identifiers and used `MONDO:7770003` and `MONDO:7770004`.
- Checked relevant existing parent and child terms with `obo-grep.pl`.
- Verified the SCN5A HGNC identifier `HGNC:10593` via the HGNC REST endpoint.
- Verified the ClinGen Hereditary Cardiovascular Disease GCEP source URL resolves and describes affiliation `40104`.
- Added definitions, logical axioms, source-attributed `is_a` relationships, creator metadata, and issue tracker metadata.
- Used the `terms/` checkout/checkin workflow to update `src/ontology/mondo-edit.obo`.

## Validation

- `robot convert --catalog src/ontology/catalog-v001.xml -i src/ontology/mondo-edit.obo -f obo -o mondo-edit.TMP.obo` passed.
- `robot reason --catalog src/ontology/catalog-v001.xml --reasoner ELK --input src/ontology/mondo-edit.obo --output reasoned.owl` passed.
- `git diff --check -- src/ontology/mondo-edit.obo` passed.
- ODK `make NORM` was attempted but could not run because Docker is not installed in this evaluation environment.

---
🤖 **Generated by opencode agent**
- Runtime: `opencode`
- Model: `openai/gpt-5.5`
- Agent config: `ai4curation/mondo-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25615939651)


#### Agent Issue Comment

Changes committed in PR #<NN>.

Implemented the requested ClinGen Hereditary Cardiovascular Disease GCEP additions, using the revised definitions from the issue comments and excluding atrioventricular block from the cardiogenetic rhythm disorder children as discussed.

---
🤖 **Generated by opencode agent**
- Runtime: `opencode`
- Model: `openai/gpt-5.5`
- Agent config: `ai4curation/mondo-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25615939651)


#### Agent Diff

```diff
diff --git a/src/ontology/mondo-edit.obo b/src/ontology/mondo-edit.obo
index 8aaf2a57d..9617ce88b 100644
--- a/src/ontology/mondo-edit.obo
+++ b/src/ontology/mondo-edit.obo
@@ -5867,6 +5867,7 @@ xref: Orphanet:51083 {source="MONDO:equivalentTo", source="OMIM:609620"}
 xref: SCTID:698272007 {source="MONDO:equivalentTo"}
 xref: UMLS:C2348199 {source="MONDO:equivalentTo", source="MONDO:MEDGEN", source="MEDGEN:378835"}
 is_a: MONDO:0000992 {source="DOID:0050793"} ! heart conduction disease
+is_a: MONDO:7770003 {source="https://clinicalgenome.org/affiliation/40104/"} ! cardiogenetic rhythm disorder
 relationship: curated_content_resource https://search.clinicalgenome.org/kb/conditions/MONDO:0000453 {source="MONDO:CLINGEN"}
 relationship: has_characteristic MONDO:0021152 {source="OMIMPS:609620"} ! inherited
 property_value: curated_content_resource "https://www.malacards.org/card/familial_short_qt_syndrome" xsd:anyURI {source="MONDO:MalaCards"}
@@ -188784,6 +188785,7 @@ xref: OMIM:192605 {source="MONDO:equivalentTo"}
 xref: SCTID:233906007 {source="MONDO:equivalentTo"}
 xref: UMLS:C0340485 {source="MONDO:equivalentTo", source="MONDO:MEDGEN", source="MEDGEN:83309"}
 is_a: MONDO:0005477 {source="MONDO:Redundant", source="OMIM:192605"} ! ventricular tachycardia
+is_a: MONDO:7770003 {source="https://clinicalgenome.org/affiliation/40104/"} ! cardiogenetic rhythm disorder
 intersection_of: MONDO:0005477 ! ventricular tachycardia
 intersection_of: has_characteristic MONDO:0021152 ! inherited
 relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/4385 {source="OMIM:192605"} ! GNAI2
@@ -257842,6 +257844,7 @@ xref: OMIM:601144 {source="DOID:0110218", source="MONDO:equivalentTo"}
 xref: Orphanet:130 {source="OMIM:601144"}
 xref: UMLS:C4551804 {source="MONDO:equivalentTo", source="MONDO:MEDGEN", source="MEDGEN:1646402"}
 is_a: MONDO:0015263 {source="DC-OMIM:601144", source="DOID:0110218", source="MONDO:Redundant", source="OMIM:601144"} ! Brugada syndrome
+is_a: MONDO:7770004 {source="https://clinicalgenome.org/affiliation/40104/"} ! SCN5A-related cardiac rhythm disorder
 intersection_of: MONDO:0015263 ! Brugada syndrome
 intersection_of: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/10593 ! SCN5A
 relationship: curated_content_resource https://search.clinicalgenome.org/kb/conditions/MONDO:0011001 {source="MONDO:CLINGEN"}
@@ -267530,6 +267533,8 @@ xref: Orphanet:228140 {source="OMIM:603829"}
 xref: SCTID:233915000 {source="MONDO:equivalentTo"}
 xref: UMLS:C2751898 {source="MEDGEN:414502", source="MONDO:equivalentTo", source="MONDO:MEDGEN"}
 is_a: MONDO:0100234 {source="DC-OMIM:603829", source="MESH:C567851"} ! paroxysmal familial ventricular fibrillation
+is_a: MONDO:7770003 {source="https://clinicalgenome.org/affiliation/40104/"} ! cardiogenetic rhythm disorder
+is_a: MONDO:7770004 {source="https://clinicalgenome.org/affiliation/40104/"} ! SCN5A-related cardiac rhythm disorder
 intersection_of: MONDO:0100234 ! paroxysmal familial ventricular fibrillation
 intersection_of: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/10593 ! SCN5A
 relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/10593 {source="OMIM:603829"} ! SCN5A
@@ -267562,6 +267567,7 @@ xref: Orphanet:101016 {source="OMIM:603830", source="MONDO:directSiblingOf"}
 xref: Orphanet:768 {source="OMIM:603830"}
 xref: UMLS:C1859062 {source="MONDO:equivalentTo", source="MONDO:MEDGEN", source="MEDGEN:349087"}
 is_a: MONDO:0019171 {source="OMIM:603830", source="Orphanet:101016-prototype"} ! familial long QT syndrome
+is_a: MONDO:7770004 {source="https://clinicalgenome.org/affiliation/40104/"} ! SCN5A-related cardiac rhythm disorder
 intersection_of: MONDO:0019171 ! familial long QT syndrome
 intersection_of: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/10593 ! SCN5A
 relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/10593 {source="OMIM:603830"} ! SCN5A
@@ -285573,6 +285579,7 @@ xref: Orphanet:166282 {source="MONDO:equivalentTo", source="OMIM:608567"}
 xref: SCTID:233913007 {source="MONDO:equivalentTo"}
 xref: UMLS:C0340491 {source="MONDO:equivalentTo", source="MONDO:MEDGEN", source="MEDGEN:573766"}
 is_a: MONDO:0001823 {source="DC-OMIM:608567", source="MESH:C563907", source="MONDO:Redundant", source="OMIM:608567"} ! sick sinus syndrome
+is_a: MONDO:7770003 {source="https://clinicalgenome.org/affiliation/40104/"} ! cardiogenetic rhythm disorder
 intersection_of: MONDO:0001823 ! sick sinus syndrome
 intersection_of: has_characteristic MONDO:0021152 ! inherited
 relationship: has_characteristic MONDO:0021152 {source="OMIMPS:608567"} ! inherited
@@ -323947,6 +323954,7 @@ xref: OMIM:614022 {source="MONDO:equivalentTo"}
 xref: Orphanet:334 {source="OMIM:614022"}
 xref: UMLS:C3151464 {source="MEDGEN:462814", source="MONDO:equivalentTo", source="MONDO:MEDGEN"}
 is_a: MONDO:0018054 {source="DC-OMIM:614022", source="MONDO:Redundant", source="OMIM:614022"} ! familial atrial fibrillation
+is_a: MONDO:7770004 {source="https://clinicalgenome.org/affiliation/40104/"} ! SCN5A-related cardiac rhythm disorder
 intersection_of: MONDO:0018054 ! familial atrial fibrillation
 intersection_of: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/10593 ! SCN5A
 relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/10593 {source="OMIM:614022"} ! SCN5A
@@ -349658,6 +349666,7 @@ xref: OMIM:616117 {source="Orphanet:436242/e", source="EFO:0005304", source="MON
 xref: Orphanet:436242 {source="MONDO:equivalentTo"}
 xref: UMLS:C4015285 {source="MEDGEN:863722", source="MONDO:equivalentTo", source="MONDO:MEDGEN"}
 is_a: MONDO:0005449 {source="EFO:0005304"} ! conduction system disorder
+is_a: MONDO:7770003 {source="https://clinicalgenome.org/affiliation/40104/"} ! cardiogenetic rhythm disorder
 relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/19661 {source="OMIM:616117"} ! TNNI3K
 property_value: curated_content_resource "https://www.malacards.org/card/cardiac_conduction_disease_with_or_without_dilated_cardiomyopathy" xsd:anyURI {source="MONDO:MalaCards"}
 
@@ -367966,6 +367975,7 @@ xref: SCTID:418818005 {source="DOID:0050451", source="MONDO:equivalentTo"}
 xref: UMLS:C1142166 {source="MONDO:equivalentTo", source="MONDO:MEDGEN", source="MEDGEN:222975"}
 is_a: MONDO:0000992 {source="DOID:0050451", source="MONDO:Redundant", source="MONDO:indirect"} ! heart conduction disease
 is_a: MONDO:0002254 {source="NCIT:C142891"} ! syndromic disease
+is_a: MONDO:7770003 {source="https://clinicalgenome.org/affiliation/40104/"} ! cardiogenetic rhythm disorder
 relationship: curated_content_resource https://search.clinicalgenome.org/kb/conditions/MONDO:0015263 {source="MONDO:CLINGEN"}
 relationship: has_characteristic MONDO:0021152 {source="OMIMPS:601144"} ! inherited
 property_value: curated_content_resource "https://www.malacards.org/card/brugada_syndrome" xsd:anyURI {source="MONDO:MalaCards"}
@@ -426973,6 +426983,7 @@ xref: Orphanet:334 {source="DOID:0050650", source="MONDO:equivalentTo"}
 xref: SCTID:715395008 {source="MONDO:equivalentTo"}
 xref: UMLS:C3468561 {source="MONDO:equivalentTo", source="MONDO:MEDGEN", source="MEDGEN:894635"}
 is_a: MONDO:0004981 {source="DOID:0050650", source="MONDO:DOID", source="MONDO:Redundant"} ! atrial fibrillation
+is_a: MONDO:7770003 {source="https://clinicalgenome.org/affiliation/40104/"} ! cardiogenetic rhythm disorder
 intersection_of: MONDO:0004981 ! atrial fibrillation
 intersection_of: has_characteristic MONDO:0021152 ! inherited
 relationship: has_characteristic MONDO:0021152 {source="OMIMPS:608583"} ! inherited
@@ -460887,6 +460898,7 @@ xref: Orphanet:871 {source="MONDO:equivalentTo", source="DOID:0111073"}
 xref: SCTID:698249005 {source="MONDO:equivalentTo"}
 xref: SCTID:93130009 {source="MONDO:equivalentObsolete"}
 is_a: MONDO:0000992 {source="DOID:0111073", source="MONDO:indirect"} ! heart conduction disease
+is_a: MONDO:7770003 {source="https://clinicalgenome.org/affiliation/40104/"} ! cardiogenetic rhythm disorder
 relationship: has_characteristic MONDO:0021152 {source="OMIMPS:113900"} ! inherited
 property_value: curated_content_resource "https://www.malacards.org/card/familial_progressive_cardiac_conduction_defect" xsd:anyURI {source="MONDO:MalaCards"}
 property_value: curated_content_resource "https://www.malacards.org/card/progressive_familial_heart_block" xsd:anyURI {source="MONDO:MalaCards"}
@@ -513335,6 +513347,7 @@ xref: OMIM:608567 {source="MONDO:equivalentTo"}
 xref: Orphanet:166282 {source="OMIM:608567"}
 xref: UMLS:C1837845 {source="MONDO:equivalentTo", source="MONDO:MEDGEN", source="MEDGEN:325270"}
 is_a: MONDO:0012061 {source="MONDO:0024562/inferred", source="MONDO:Redundant", source="OMIM:608567"} ! familial sick sinus syndrome
+is_a: MONDO:7770004 {source="https://clinicalgenome.org/affiliation/40104/"} ! SCN5A-related cardiac rhythm disorder
 intersection_of: MONDO:0012061 ! familial sick sinus syndrome
 intersection_of: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/10593 ! SCN5A
 relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/10593 {source="OMIM:608567"} ! SCN5A
@@ -621534,6 +621547,33 @@ is_a: MONDO:0005451 {source="PMID:38849953"} ! eating disorder
 property_value: http://purl.org/dc/terms/creator https://orcid.org/0000-0003-3311-7320
 property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9408" xsd:anyURI
 
+[Term]
+id: MONDO:7770003
+name: cardiogenetic rhythm disorder
+def: "A heterogeneous group of cardiac rhythm phenotypes with a monogenic etiology that include, but are not limited to, atrial fibrillation, sick sinus syndrome, progressive cardiac conduction disease, ventricular fibrillation, Brugada syndrome, long QT syndrome, short QT syndrome, and tachycardia with fibrillation." [https://clinicalgenome.org/affiliation/40104/]
+synonym: "cardiogenetic rhythm disorders" EXACT [https://clinicalgenome.org/affiliation/40104/]
+is_a: MONDO:0007263 {source="https://clinicalgenome.org/affiliation/40104/"} ! cardiac rhythm disease
+is_a: MONDO:0100547 {source="https://clinicalgenome.org/affiliation/40104/"} ! cardiogenetic disease
+intersection_of: MONDO:0007263 ! cardiac rhythm disease
+intersection_of: has_characteristic MONDO:0021152 ! inherited
+relationship: has_characteristic MONDO:0021152 {source="https://clinicalgenome.org/affiliation/40104/"} ! inherited
+property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9707" xsd:anyURI
+
+[Term]
+id: MONDO:7770004
+name: SCN5A-related cardiac rhythm disorder
+def: "A heterogeneous collection of cardiac rhythm disorders caused by genetic variation in the SCN5A gene with autosomal dominant inheritance. Affected individuals are commonly reported to have unremarkable cardiac morphology and at least one cardiac rhythm phenotype that includes, but is not limited to, atrial fibrillation, sick sinus syndrome, progressive cardiac conduction disease, ventricular fibrillation, long QT syndrome, and Brugada syndrome. Individuals with pathogenic variants in SCN5A may also exhibit overlapping or mixed cardiac rhythm phenotypes and intrafamilial variability." [https://clinicalgenome.org/affiliation/40104/]
+synonym: "SCN5A cardiac rhythm disorder" EXACT [https://clinicalgenome.org/affiliation/40104/, MONDO:patterns/disease_series_by_gene]
+synonym: "SCN5A related cardiac rhythm disorder" EXACT [https://clinicalgenome.org/affiliation/40104/, MONDO:patterns/disease_series_by_gene]
+synonym: "SCN5A-related cardiac rhythm disorders" EXACT [https://clinicalgenome.org/affiliation/40104/]
+is_a: MONDO:0007263 {source="https://clinicalgenome.org/affiliation/40104/"} ! cardiac rhythm disease
+is_a: MONDO:0100547 {source="https://clinicalgenome.org/affiliation/40104/"} ! cardiogenetic disease
+is_a: MONDO:7770003 {source="https://clinicalgenome.org/affiliation/40104/"} ! cardiogenetic rhythm disorder
+intersection_of: MONDO:7770003 ! cardiogenetic rhythm disorder
+intersection_of: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/10593 ! SCN5A
+relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/10593 {source="https://clinicalgenome.org/affiliation/40104/"} ! SCN5A
+property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9707" xsd:anyURI
+
 [Term]
 id: MONDO:8000000
 name: infectious discitis

```

### Attempt 8: gpt-5.5 / codex

- **Eval PR**: [#48](https://github.com/ai4curation/eval-ont-agent-mondo/pull/48)
- **F1**: 0.308  **Precision**: 0.250  **Recall**: 0.400  **Jaccard**: 0.182
- **Trace**: [25615892734](https://github.com/ai4curation/eval-ont-agent-mondo/tree/master/traces/25615892734)
- **Workflow run**: [25615892734](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25615892734)

#### Agent PR Comment

## Summary

Addressed issue #9707 by adding two new MONDO terms:

- MONDO:7770003 cardiogenetic rhythm disorder
- MONDO:7770004 SCN5A-related cardiac rhythm disorder

The new terms include the revised definitions from the issue comments, with provenance to the ClinGen Hereditary Cardiovascular Disease GCEP page and the issue tracker item. I verified SCN5A as HGNC:10593 using the HGNC service before adding the gene relationship.

## Hierarchy Updates

Added `cardiogenetic rhythm disorder` as an additional parent for the requested monogenic rhythm disorder classes:

- atrial conduction disease
- Brugada syndrome
- familial atrial fibrillation
- familial sick sinus syndrome
- progressive familial heart block
- short QT syndrome
- ventricular tachycardia, familial
- ventricular fibrillation, paroxysmal familial, type 1

Added `SCN5A-related cardiac rhythm disorder` as an additional parent for the requested included SCN5A phenotypes:

- atrial fibrillation, familial, 10
- sick sinus syndrome 1
- ventricular fibrillation, paroxysmal familial, type 1
- long QT syndrome 3
- Brugada syndrome 1

I did not add atrioventricular block under cardiogenetic rhythm disorder, following the issue comment noting that it is not necessarily monogenic.

## Checklist

- Read the imported issue context and comments.
- Checked the disease series by gene pattern.
- Verified SCN5A gene identifier as HGNC:10593.
- Checked proposed parents and affected existing terms for consistency.
- Made edits through `terms/` checkout/checkin workflow.
- Ran normalization with `make NORM && mv NORM mondo-edit.obo` using the local toolchain because Docker is unavailable in this environment.
- Ran syntax validation with `robot convert --catalog src/ontology/catalog-v001.xml -i src/ontology/mondo-edit.obo -f obo -o mondo-edit.TMP.obo`.

---
🤖 **Generated by codex agent**
- Runtime: `codex`
- Model: `gpt-5.5`
- Agent config: `ai4curation/mondo-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25615892734)


#### Agent Issue Comment

Changes committed in PR #<NN>.

I added the requested SCN5A-related cardiac rhythm disorder term and the cardiogenetic rhythm disorder parent term. The requested hierarchy was added with provenance, excluding atrioventricular block per the curator note that it is not necessarily monogenic.

---
🤖 **Generated by codex agent**
- Runtime: `codex`
- Model: `gpt-5.5`
- Agent config: `ai4curation/mondo-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25615892734)


#### Agent Diff

```diff
diff --git a/src/ontology/mondo-edit.obo b/src/ontology/mondo-edit.obo
index 8aaf2a57d..dab7fd5f0 100644
--- a/src/ontology/mondo-edit.obo
+++ b/src/ontology/mondo-edit.obo
@@ -5867,6 +5867,7 @@ xref: Orphanet:51083 {source="MONDO:equivalentTo", source="OMIM:609620"}
 xref: SCTID:698272007 {source="MONDO:equivalentTo"}
 xref: UMLS:C2348199 {source="MONDO:equivalentTo", source="MONDO:MEDGEN", source="MEDGEN:378835"}
 is_a: MONDO:0000992 {source="DOID:0050793"} ! heart conduction disease
+is_a: MONDO:7770003 {source="https://clinicalgenome.org/affiliation/40104/", source="https://github.com/monarch-initiative/mondo/issues/9707"} ! cardiogenetic rhythm disorder
 relationship: curated_content_resource https://search.clinicalgenome.org/kb/conditions/MONDO:0000453 {source="MONDO:CLINGEN"}
 relationship: has_characteristic MONDO:0021152 {source="OMIMPS:609620"} ! inherited
 property_value: curated_content_resource "https://www.malacards.org/card/familial_short_qt_syndrome" xsd:anyURI {source="MONDO:MalaCards"}
@@ -188784,6 +188785,7 @@ xref: OMIM:192605 {source="MONDO:equivalentTo"}
 xref: SCTID:233906007 {source="MONDO:equivalentTo"}
 xref: UMLS:C0340485 {source="MONDO:equivalentTo", source="MONDO:MEDGEN", source="MEDGEN:83309"}
 is_a: MONDO:0005477 {source="MONDO:Redundant", source="OMIM:192605"} ! ventricular tachycardia
+is_a: MONDO:7770003 {source="https://clinicalgenome.org/affiliation/40104/", source="https://github.com/monarch-initiative/mondo/issues/9707"} ! cardiogenetic rhythm disorder
 intersection_of: MONDO:0005477 ! ventricular tachycardia
 intersection_of: has_characteristic MONDO:0021152 ! inherited
 relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/4385 {source="OMIM:192605"} ! GNAI2
@@ -257842,6 +257844,7 @@ xref: OMIM:601144 {source="DOID:0110218", source="MONDO:equivalentTo"}
 xref: Orphanet:130 {source="OMIM:601144"}
 xref: UMLS:C4551804 {source="MONDO:equivalentTo", source="MONDO:MEDGEN", source="MEDGEN:1646402"}
 is_a: MONDO:0015263 {source="DC-OMIM:601144", source="DOID:0110218", source="MONDO:Redundant", source="OMIM:601144"} ! Brugada syndrome
+is_a: MONDO:7770004 {source="https://clinicalgenome.org/affiliation/40104/", source="https://github.com/monarch-initiative/mondo/issues/9707"} ! SCN5A-related cardiac rhythm disorder
 intersection_of: MONDO:0015263 ! Brugada syndrome
 intersection_of: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/10593 ! SCN5A
 relationship: curated_content_resource https://search.clinicalgenome.org/kb/conditions/MONDO:0011001 {source="MONDO:CLINGEN"}
@@ -267530,6 +267533,8 @@ xref: Orphanet:228140 {source="OMIM:603829"}
 xref: SCTID:233915000 {source="MONDO:equivalentTo"}
 xref: UMLS:C2751898 {source="MEDGEN:414502", source="MONDO:equivalentTo", source="MONDO:MEDGEN"}
 is_a: MONDO:0100234 {source="DC-OMIM:603829", source="MESH:C567851"} ! paroxysmal familial ventricular fibrillation
+is_a: MONDO:7770003 {source="https://clinicalgenome.org/affiliation/40104/", source="https://github.com/monarch-initiative/mondo/issues/9707"} ! cardiogenetic rhythm disorder
+is_a: MONDO:7770004 {source="https://clinicalgenome.org/affiliation/40104/", source="https://github.com/monarch-initiative/mondo/issues/9707"} ! SCN5A-related cardiac rhythm disorder
 intersection_of: MONDO:0100234 ! paroxysmal familial ventricular fibrillation
 intersection_of: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/10593 ! SCN5A
 relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/10593 {source="OMIM:603829"} ! SCN5A
@@ -267562,6 +267567,7 @@ xref: Orphanet:101016 {source="OMIM:603830", source="MONDO:directSiblingOf"}
 xref: Orphanet:768 {source="OMIM:603830"}
 xref: UMLS:C1859062 {source="MONDO:equivalentTo", source="MONDO:MEDGEN", source="MEDGEN:349087"}
 is_a: MONDO:0019171 {source="OMIM:603830", source="Orphanet:101016-prototype"} ! familial long QT syndrome
+is_a: MONDO:7770004 {source="https://clinicalgenome.org/affiliation/40104/", source="https://github.com/monarch-initiative/mondo/issues/9707"} ! SCN5A-related cardiac rhythm disorder
 intersection_of: MONDO:0019171 ! familial long QT syndrome
 intersection_of: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/10593 ! SCN5A
 relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/10593 {source="OMIM:603830"} ! SCN5A
@@ -285573,6 +285579,7 @@ xref: Orphanet:166282 {source="MONDO:equivalentTo", source="OMIM:608567"}
 xref: SCTID:233913007 {source="MONDO:equivalentTo"}
 xref: UMLS:C0340491 {source="MONDO:equivalentTo", source="MONDO:MEDGEN", source="MEDGEN:573766"}
 is_a: MONDO:0001823 {source="DC-OMIM:608567", source="MESH:C563907", source="MONDO:Redundant", source="OMIM:608567"} ! sick sinus syndrome
+is_a: MONDO:7770003 {source="https://clinicalgenome.org/affiliation/40104/", source="https://github.com/monarch-initiative/mondo/issues/9707"} ! cardiogenetic rhythm disorder
 intersection_of: MONDO:0001823 ! sick sinus syndrome
 intersection_of: has_characteristic MONDO:0021152 ! inherited
 relationship: has_characteristic MONDO:0021152 {source="OMIMPS:608567"} ! inherited
@@ -323947,6 +323954,7 @@ xref: OMIM:614022 {source="MONDO:equivalentTo"}
 xref: Orphanet:334 {source="OMIM:614022"}
 xref: UMLS:C3151464 {source="MEDGEN:462814", source="MONDO:equivalentTo", source="MONDO:MEDGEN"}
 is_a: MONDO:0018054 {source="DC-OMIM:614022", source="MONDO:Redundant", source="OMIM:614022"} ! familial atrial fibrillation
+is_a: MONDO:7770004 {source="https://clinicalgenome.org/affiliation/40104/", source="https://github.com/monarch-initiative/mondo/issues/9707"} ! SCN5A-related cardiac rhythm disorder
 intersection_of: MONDO:0018054 ! familial atrial fibrillation
 intersection_of: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/10593 ! SCN5A
 relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/10593 {source="OMIM:614022"} ! SCN5A
@@ -349658,6 +349666,7 @@ xref: OMIM:616117 {source="Orphanet:436242/e", source="EFO:0005304", source="MON
 xref: Orphanet:436242 {source="MONDO:equivalentTo"}
 xref: UMLS:C4015285 {source="MEDGEN:863722", source="MONDO:equivalentTo", source="MONDO:MEDGEN"}
 is_a: MONDO:0005449 {source="EFO:0005304"} ! conduction system disorder
+is_a: MONDO:7770003 {source="https://clinicalgenome.org/affiliation/40104/", source="https://github.com/monarch-initiative/mondo/issues/9707"} ! cardiogenetic rhythm disorder
 relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/19661 {source="OMIM:616117"} ! TNNI3K
 property_value: curated_content_resource "https://www.malacards.org/card/cardiac_conduction_disease_with_or_without_dilated_cardiomyopathy" xsd:anyURI {source="MONDO:MalaCards"}
 
@@ -367966,6 +367975,7 @@ xref: SCTID:418818005 {source="DOID:0050451", source="MONDO:equivalentTo"}
 xref: UMLS:C1142166 {source="MONDO:equivalentTo", source="MONDO:MEDGEN", source="MEDGEN:222975"}
 is_a: MONDO:0000992 {source="DOID:0050451", source="MONDO:Redundant", source="MONDO:indirect"} ! heart conduction disease
 is_a: MONDO:0002254 {source="NCIT:C142891"} ! syndromic disease
+is_a: MONDO:7770003 {source="https://clinicalgenome.org/affiliation/40104/", source="https://github.com/monarch-initiative/mondo/issues/9707"} ! cardiogenetic rhythm disorder
 relationship: curated_content_resource https://search.clinicalgenome.org/kb/conditions/MONDO:0015263 {source="MONDO:CLINGEN"}
 relationship: has_characteristic MONDO:0021152 {source="OMIMPS:601144"} ! inherited
 property_value: curated_content_resource "https://www.malacards.org/card/brugada_syndrome" xsd:anyURI {source="MONDO:MalaCards"}
@@ -426973,6 +426983,7 @@ xref: Orphanet:334 {source="DOID:0050650", source="MONDO:equivalentTo"}
 xref: SCTID:715395008 {source="MONDO:equivalentTo"}
 xref: UMLS:C3468561 {source="MONDO:equivalentTo", source="MONDO:MEDGEN", source="MEDGEN:894635"}
 is_a: MONDO:0004981 {source="DOID:0050650", source="MONDO:DOID", source="MONDO:Redundant"} ! atrial fibrillation
+is_a: MONDO:7770003 {source="https://clinicalgenome.org/affiliation/40104/", source="https://github.com/monarch-initiative/mondo/issues/9707"} ! cardiogenetic rhythm disorder
 intersection_of: MONDO:0004981 ! atrial fibrillation
 intersection_of: has_characteristic MONDO:0021152 ! inherited
 relationship: has_characteristic MONDO:0021152 {source="OMIMPS:608583"} ! inherited
@@ -460887,6 +460898,7 @@ xref: Orphanet:871 {source="MONDO:equivalentTo", source="DOID:0111073"}
 xref: SCTID:698249005 {source="MONDO:equivalentTo"}
 xref: SCTID:93130009 {source="MONDO:equivalentObsolete"}
 is_a: MONDO:0000992 {source="DOID:0111073", source="MONDO:indirect"} ! heart conduction disease
+is_a: MONDO:7770003 {source="https://clinicalgenome.org/affiliation/40104/", source="https://github.com/monarch-initiative/mondo/issues/9707"} ! cardiogenetic rhythm disorder
 relationship: has_characteristic MONDO:0021152 {source="OMIMPS:113900"} ! inherited
 property_value: curated_content_resource "https://www.malacards.org/card/familial_progressive_cardiac_conduction_defect" xsd:anyURI {source="MONDO:MalaCards"}
 property_value: curated_content_resource "https://www.malacards.org/card/progressive_familial_heart_block" xsd:anyURI {source="MONDO:MalaCards"}
@@ -513335,6 +513347,7 @@ xref: OMIM:608567 {source="MONDO:equivalentTo"}
 xref: Orphanet:166282 {source="OMIM:608567"}
 xref: UMLS:C1837845 {source="MONDO:equivalentTo", source="MONDO:MEDGEN", source="MEDGEN:325270"}
 is_a: MONDO:0012061 {source="MONDO:0024562/inferred", source="MONDO:Redundant", source="OMIM:608567"} ! familial sick sinus syndrome
+is_a: MONDO:7770004 {source="https://clinicalgenome.org/affiliation/40104/", source="https://github.com/monarch-initiative/mondo/issues/9707"} ! SCN5A-related cardiac rhythm disorder
 intersection_of: MONDO:0012061 ! familial sick sinus syndrome
 intersection_of: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/10593 ! SCN5A
 relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/10593 {source="OMIM:608567"} ! SCN5A
@@ -621534,6 +621547,27 @@ is_a: MONDO:0005451 {source="PMID:38849953"} ! eating disorder
 property_value: http://purl.org/dc/terms/creator https://orcid.org/0000-0003-3311-7320
 property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9408" xsd:anyURI
 
+[Term]
+id: MONDO:7770003
+name: cardiogenetic rhythm disorder
+def: "A heterogeneous group of cardiac rhythm phenotypes with a monogenic etiology that include, but are not limited to, atrial fibrillation, sick sinus syndrome, progressive cardiac conduction disease, ventricular fibrillation, Brugada syndrome, long QT syndrome, short QT syndrome, and tachycardia with fibrillation." [https://clinicalgenome.org/affiliation/40104/, https://github.com/monarch-initiative/mondo/issues/9707]
+synonym: "cardiogenetic rhythm disorders" EXACT [https://clinicalgenome.org/affiliation/40104/, https://github.com/monarch-initiative/mondo/issues/9707]
+is_a: MONDO:0007263 {source="https://clinicalgenome.org/affiliation/40104/", source="https://github.com/monarch-initiative/mondo/issues/9707"} ! cardiac rhythm disease
+is_a: MONDO:0100547 {source="https://clinicalgenome.org/affiliation/40104/", source="https://github.com/monarch-initiative/mondo/issues/9707"} ! cardiogenetic disease
+property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9707" xsd:anyURI
+
+[Term]
+id: MONDO:7770004
+name: SCN5A-related cardiac rhythm disorder
+def: "A heterogeneous collection of cardiac rhythm disorders caused by genetic variation in the SCN5A gene with autosomal dominant inheritance. Affected individuals are commonly reported to have unremarkable cardiac morphology and at least one cardiac rhythm phenotype that includes, but is not limited to, atrial fibrillation, sick sinus syndrome, progressive cardiac conduction disease, ventricular fibrillation, long QT syndrome, and Brugada syndrome. Individuals with pathogenic variants in SCN5A may also exhibit overlapping or mixed cardiac rhythm phenotypes and intrafamilial variability." [https://clinicalgenome.org/affiliation/40104/, https://github.com/monarch-initiative/mondo/issues/9707]
+is_a: MONDO:0007263 {source="https://clinicalgenome.org/affiliation/40104/", source="https://github.com/monarch-initiative/mondo/issues/9707"} ! cardiac rhythm disease
+is_a: MONDO:0100547 {source="https://clinicalgenome.org/affiliation/40104/", source="https://github.com/monarch-initiative/mondo/issues/9707"} ! cardiogenetic disease
+is_a: MONDO:7770003 {source="https://clinicalgenome.org/affiliation/40104/", source="https://github.com/monarch-initiative/mondo/issues/9707"} ! cardiogenetic rhythm disorder
+intersection_of: MONDO:0007263 ! cardiac rhythm disease
+intersection_of: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/10593 ! SCN5A
+relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/10593 {source="https://clinicalgenome.org/affiliation/40104/", source="https://github.com/monarch-initiative/mondo/issues/9707"} ! SCN5A
+property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9707" xsd:anyURI
+
 [Term]
 id: MONDO:8000000
 name: infectious discitis

```

### Attempt 9: gpt-5.4 / codex

- **Eval PR**: [#160](https://github.com/ai4curation/eval-ont-agent-mondo/pull/160)
- **F1**: 0.270  **Precision**: 0.208  **Recall**: 0.385  **Jaccard**: 0.156
- **Workflow run**: [25640345470](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25640345470)

#### Agent PR Comment

Implemented the `#9707` request by adding two new umbrella terms and wiring the requested existing disease terms under them.

Changes made:
- Added `MONDO:7770003` `cardiogenetic rhythm disorder` as a child of `MONDO:0007263` cardiac rhythm disease and `MONDO:0100547` cardiogenetic disease.
- Added `MONDO:7770004` `SCN5A-related cardiac rhythm disorder` as a child of `MONDO:7770003`, with asserted `SCN5A` gene basis and autosomal dominant inheritance.
- Added the requested parentage from `MONDO:7770003` to:
  - `MONDO:0014500` atrial conduction disease
  - `MONDO:0015263` Brugada syndrome
  - `MONDO:0018054` familial atrial fibrillation
  - `MONDO:0012061` familial sick sinus syndrome
  - `MONDO:0019490` progressive familial heart block
  - `MONDO:0000453` short QT syndrome
  - `MONDO:0008648` ventricular tachycardia, familial
  - `MONDO:0011376` ventricular fibrillation, paroxysmal familial, type 1
- Added the requested parentage from `MONDO:7770004` to:
  - `MONDO:0013530` atrial fibrillation, familial, 10
  - `MONDO:0024562` sick sinus syndrome 1
  - `MONDO:0011376` ventricular fibrillation, paroxysmal familial, type 1
  - `MONDO:0011377` long QT syndrome 3
  - `MONDO:0011001` Brugada syndrome 1
- Added `IAO:0000233` issue provenance for each touched stanza.

Rationale:
- Used the revised definitions from the issue comment on 2025-10-31.
- Treated the explicit include/exclude lists in the issue as authoritative for asserted hierarchy.
- Kept `MONDO:0000465` atrioventricular block out of `cardiogenetic rhythm disorder`, matching the issue-thread decision that the class is not necessarily monogenic.
- Kept the excluded SCN5A-associated phenotypes out of the new SCN5A umbrella term, despite the broader descriptive text mentioning conduction phenotypes.

Validation checklist:
- [x] Read the imported issue title, body, and comments from `__issue_context__.json`
- [x] Verified existing relevant MONDO terms and current SCN5A children in `src/ontology/mondo-edit.obo`
- [x] Checked the HGNC identifier for `SCN5A` against existing MONDO usage (`HGNC:10593`)
- [x] Checked terms out to `terms/`, edited, and checked them back in
- [x] Ran `make NORM` in `src/ontology` and replaced `mondo-edit.obo` with the normalized output
- [x] Ran `robot convert --catalog catalog-v001.xml -i mondo-edit.obo -f obo -o mondo-edit.TMP.obo`

Notes:
- `docker` was not available in this environment, so normalization was run directly through the local repo toolchain (`make NORM`) rather than through `run.sh`.
- Local commit created: `21cded2` (`Add SCN5A-related cardiac rhythm umbrella terms`)

---
🤖 **Generated by codex agent**
- Runtime: `codex`
- Model: `gpt-5.4`
- Agent config: `ai4curation/mondo-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25640345470)

#### Agent Issue Comment

Implemented locally and committed for PR #<NN>.

Summary:
- added `MONDO:7770003` `cardiogenetic rhythm disorder`
- added `MONDO:7770004` `SCN5A-related cardiac rhythm disorder`
- reparented the requested existing rhythm terms under the new umbrella terms
- followed the thread update to use the revised definitions
- did not place `MONDO:0000465` atrioventricular block under `cardiogenetic rhythm disorder`, consistent with the existing issue discussion

---
🤖 **Generated by codex agent**
- Runtime: `codex`
- Model: `gpt-5.4`
- Agent config: `ai4curation/mondo-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25640345470)

#### Agent Diff

```diff
diff --git a/src/ontology/mondo-edit.obo b/src/ontology/mondo-edit.obo
index 8aaf2a57d..895fb4a8c 100644
--- a/src/ontology/mondo-edit.obo
+++ b/src/ontology/mondo-edit.obo
@@ -5867,10 +5867,12 @@ xref: Orphanet:51083 {source="MONDO:equivalentTo", source="OMIM:609620"}
 xref: SCTID:698272007 {source="MONDO:equivalentTo"}
 xref: UMLS:C2348199 {source="MONDO:equivalentTo", source="MONDO:MEDGEN", source="MEDGEN:378835"}
 is_a: MONDO:0000992 {source="DOID:0050793"} ! heart conduction disease
+is_a: MONDO:7770003 {source="https://clinicalgenome.org/affiliation/40104/"} ! cardiogenetic rhythm disorder
 relationship: curated_content_resource https://search.clinicalgenome.org/kb/conditions/MONDO:0000453 {source="MONDO:CLINGEN"}
 relationship: has_characteristic MONDO:0021152 {source="OMIMPS:609620"} ! inherited
 property_value: curated_content_resource "https://www.malacards.org/card/familial_short_qt_syndrome" xsd:anyURI {source="MONDO:MalaCards"}
 property_value: curated_content_resource "https://www.malacards.org/card/short_qt_syndrome" xsd:anyURI {source="MONDO:MalaCards"}
+property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9707" xsd:anyURI
 
 [Term]
 id: MONDO:0000454
@@ -188784,11 +188786,13 @@ xref: OMIM:192605 {source="MONDO:equivalentTo"}
 xref: SCTID:233906007 {source="MONDO:equivalentTo"}
 xref: UMLS:C0340485 {source="MONDO:equivalentTo", source="MONDO:MEDGEN", source="MEDGEN:83309"}
 is_a: MONDO:0005477 {source="MONDO:Redundant", source="OMIM:192605"} ! ventricular tachycardia
+is_a: MONDO:7770003 {source="https://clinicalgenome.org/affiliation/40104/"} ! cardiogenetic rhythm disorder
 intersection_of: MONDO:0005477 ! ventricular tachycardia
 intersection_of: has_characteristic MONDO:0021152 ! inherited
 relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/4385 {source="OMIM:192605"} ! GNAI2
 property_value: curated_content_resource "https://www.malacards.org/card/ventricular_tachycardia_familial" xsd:anyURI {source="MONDO:MalaCards"}
 property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/4521" xsd:anyURI
+property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9707" xsd:anyURI
 
 [Term]
 id: MONDO:0008649
@@ -257842,11 +257846,13 @@ xref: OMIM:601144 {source="DOID:0110218", source="MONDO:equivalentTo"}
 xref: Orphanet:130 {source="OMIM:601144"}
 xref: UMLS:C4551804 {source="MONDO:equivalentTo", source="MONDO:MEDGEN", source="MEDGEN:1646402"}
 is_a: MONDO:0015263 {source="DC-OMIM:601144", source="DOID:0110218", source="MONDO:Redundant", source="OMIM:601144"} ! Brugada syndrome
+is_a: MONDO:7770004 {source="https://clinicalgenome.org/affiliation/40104/"} ! SCN5A-related cardiac rhythm disorder
 intersection_of: MONDO:0015263 ! Brugada syndrome
 intersection_of: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/10593 ! SCN5A
 relationship: curated_content_resource https://search.clinicalgenome.org/kb/conditions/MONDO:0011001 {source="MONDO:CLINGEN"}
 relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/10593 {source="OMIM:601144"} ! SCN5A
 property_value: curated_content_resource "https://www.malacards.org/card/brugada_syndrome_1" xsd:anyURI {source="MONDO:MalaCards"}
+property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9707" xsd:anyURI
 
 [Term]
 id: MONDO:0011002
@@ -267530,11 +267536,14 @@ xref: Orphanet:228140 {source="OMIM:603829"}
 xref: SCTID:233915000 {source="MONDO:equivalentTo"}
 xref: UMLS:C2751898 {source="MEDGEN:414502", source="MONDO:equivalentTo", source="MONDO:MEDGEN"}
 is_a: MONDO:0100234 {source="DC-OMIM:603829", source="MESH:C567851"} ! paroxysmal familial ventricular fibrillation
+is_a: MONDO:7770003 {source="https://clinicalgenome.org/affiliation/40104/"} ! cardiogenetic rhythm disorder
+is_a: MONDO:7770004 {source="https://clinicalgenome.org/affiliation/40104/"} ! SCN5A-related cardiac rhythm disorder
 intersection_of: MONDO:0100234 ! paroxysmal familial ventricular fibrillation
 intersection_of: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/10593 ! SCN5A
 relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/10593 {source="OMIM:603829"} ! SCN5A
 property_value: curated_content_resource "https://www.malacards.org/card/ventricular_fibrillation_paroxysmal_familial_1" xsd:anyURI {source="MONDO:MalaCards"}
 property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/4521" xsd:anyURI
+property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9707" xsd:anyURI
 
 [Term]
 id: MONDO:0011377
@@ -267562,11 +267571,13 @@ xref: Orphanet:101016 {source="OMIM:603830", source="MONDO:directSiblingOf"}
 xref: Orphanet:768 {source="OMIM:603830"}
 xref: UMLS:C1859062 {source="MONDO:equivalentTo", source="MONDO:MEDGEN", source="MEDGEN:349087"}
 is_a: MONDO:0019171 {source="OMIM:603830", source="Orphanet:101016-prototype"} ! familial long QT syndrome
+is_a: MONDO:7770004 {source="https://clinicalgenome.org/affiliation/40104/"} ! SCN5A-related cardiac rhythm disorder
 intersection_of: MONDO:0019171 ! familial long QT syndrome
 intersection_of: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/10593 ! SCN5A
 relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/10593 {source="OMIM:603830"} ! SCN5A
 property_value: curated_content_resource "https://www.malacards.org/card/long_qt_syndrome_3" xsd:anyURI {source="MONDO:MalaCards"}
 property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9285" xsd:anyURI
+property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9707" xsd:anyURI
 property_value: seeAlso "https://rarediseases.info.nih.gov/diseases/3286/long-qt-syndrome-3" xsd:anyURI {source="GARD:0003286"}
 
 [Term]
@@ -285573,10 +285584,12 @@ xref: Orphanet:166282 {source="MONDO:equivalentTo", source="OMIM:608567"}
 xref: SCTID:233913007 {source="MONDO:equivalentTo"}
 xref: UMLS:C0340491 {source="MONDO:equivalentTo", source="MONDO:MEDGEN", source="MEDGEN:573766"}
 is_a: MONDO:0001823 {source="DC-OMIM:608567", source="MESH:C563907", source="MONDO:Redundant", source="OMIM:608567"} ! sick sinus syndrome
+is_a: MONDO:7770003 {source="https://clinicalgenome.org/affiliation/40104/"} ! cardiogenetic rhythm disorder
 intersection_of: MONDO:0001823 ! sick sinus syndrome
 intersection_of: has_characteristic MONDO:0021152 ! inherited
 relationship: has_characteristic MONDO:0021152 {source="OMIMPS:608567"} ! inherited
 property_value: curated_content_resource "https://www.malacards.org/card/familial_sick_sinus_syndrome" xsd:anyURI {source="MONDO:MalaCards"}
+property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9707" xsd:anyURI
 
 [Term]
 id: MONDO:0012062
@@ -323947,10 +323960,12 @@ xref: OMIM:614022 {source="MONDO:equivalentTo"}
 xref: Orphanet:334 {source="OMIM:614022"}
 xref: UMLS:C3151464 {source="MEDGEN:462814", source="MONDO:equivalentTo", source="MONDO:MEDGEN"}
 is_a: MONDO:0018054 {source="DC-OMIM:614022", source="MONDO:Redundant", source="OMIM:614022"} ! familial atrial fibrillation
+is_a: MONDO:7770004 {source="https://clinicalgenome.org/affiliation/40104/"} ! SCN5A-related cardiac rhythm disorder
 intersection_of: MONDO:0018054 ! familial atrial fibrillation
 intersection_of: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/10593 ! SCN5A
 relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/10593 {source="OMIM:614022"} ! SCN5A
 property_value: curated_content_resource "https://www.malacards.org/card/atrial_fibrillation_familial_10" xsd:anyURI {source="MONDO:MalaCards"}
+property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9707" xsd:anyURI
 
 [Term]
 id: MONDO:0013531
@@ -349658,8 +349673,10 @@ xref: OMIM:616117 {source="Orphanet:436242/e", source="EFO:0005304", source="MON
 xref: Orphanet:436242 {source="MONDO:equivalentTo"}
 xref: UMLS:C4015285 {source="MEDGEN:863722", source="MONDO:equivalentTo", source="MONDO:MEDGEN"}
 is_a: MONDO:0005449 {source="EFO:0005304"} ! conduction system disorder
+is_a: MONDO:7770003 {source="https://clinicalgenome.org/affiliation/40104/"} ! cardiogenetic rhythm disorder
 relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/19661 {source="OMIM:616117"} ! TNNI3K
 property_value: curated_content_resource "https://www.malacards.org/card/cardiac_conduction_disease_with_or_without_dilated_cardiomyopathy" xsd:anyURI {source="MONDO:MalaCards"}
+property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9707" xsd:anyURI
 
 [Term]
 id: MONDO:0014501
@@ -367966,9 +367983,11 @@ xref: SCTID:418818005 {source="DOID:0050451", source="MONDO:equivalentTo"}
 xref: UMLS:C1142166 {source="MONDO:equivalentTo", source="MONDO:MEDGEN", source="MEDGEN:222975"}
 is_a: MONDO:0000992 {source="DOID:0050451", source="MONDO:Redundant", source="MONDO:indirect"} ! heart conduction disease
 is_a: MONDO:0002254 {source="NCIT:C142891"} ! syndromic disease
+is_a: MONDO:7770003 {source="https://clinicalgenome.org/affiliation/40104/"} ! cardiogenetic rhythm disorder
 relationship: curated_content_resource https://search.clinicalgenome.org/kb/conditions/MONDO:0015263 {source="MONDO:CLINGEN"}
 relationship: has_characteristic MONDO:0021152 {source="OMIMPS:601144"} ! inherited
 property_value: curated_content_resource "https://www.malacards.org/card/brugada_syndrome" xsd:anyURI {source="MONDO:MalaCards"}
+property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9707" xsd:anyURI
 
 [Term]
 id: MONDO:0015264
@@ -426973,10 +426992,12 @@ xref: Orphanet:334 {source="DOID:0050650", source="MONDO:equivalentTo"}
 xref: SCTID:715395008 {source="MONDO:equivalentTo"}
 xref: UMLS:C3468561 {source="MONDO:equivalentTo", source="MONDO:MEDGEN", source="MEDGEN:894635"}
 is_a: MONDO:0004981 {source="DOID:0050650", source="MONDO:DOID", source="MONDO:Redundant"} ! atrial fibrillation
+is_a: MONDO:7770003 {source="https://clinicalgenome.org/affiliation/40104/"} ! cardiogenetic rhythm disorder
 intersection_of: MONDO:0004981 ! atrial fibrillation
 intersection_of: has_characteristic MONDO:0021152 ! inherited
 relationship: has_characteristic MONDO:0021152 {source="OMIMPS:608583"} ! inherited
 property_value: curated_content_resource "https://www.malacards.org/card/familial_atrial_fibrillation" xsd:anyURI {source="MONDO:MalaCards"}
+property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9707" xsd:anyURI
 
 [Term]
 id: MONDO:0018055
@@ -460887,9 +460908,11 @@ xref: Orphanet:871 {source="MONDO:equivalentTo", source="DOID:0111073"}
 xref: SCTID:698249005 {source="MONDO:equivalentTo"}
 xref: SCTID:93130009 {source="MONDO:equivalentObsolete"}
 is_a: MONDO:0000992 {source="DOID:0111073", source="MONDO:indirect"} ! heart conduction disease
+is_a: MONDO:7770003 {source="https://clinicalgenome.org/affiliation/40104/"} ! cardiogenetic rhythm disorder
 relationship: has_characteristic MONDO:0021152 {source="OMIMPS:113900"} ! inherited
 property_value: curated_content_resource "https://www.malacards.org/card/familial_progressive_cardiac_conduction_defect" xsd:anyURI {source="MONDO:MalaCards"}
 property_value: curated_content_resource "https://www.malacards.org/card/progressive_familial_heart_block" xsd:anyURI {source="MONDO:MalaCards"}
+property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9707" xsd:anyURI
 
 [Term]
 id: MONDO:0019491
@@ -513335,10 +513358,12 @@ xref: OMIM:608567 {source="MONDO:equivalentTo"}
 xref: Orphanet:166282 {source="OMIM:608567"}
 xref: UMLS:C1837845 {source="MONDO:equivalentTo", source="MONDO:MEDGEN", source="MEDGEN:325270"}
 is_a: MONDO:0012061 {source="MONDO:0024562/inferred", source="MONDO:Redundant", source="OMIM:608567"} ! familial sick sinus syndrome
+is_a: MONDO:7770004 {source="https://clinicalgenome.org/affiliation/40104/"} ! SCN5A-related cardiac rhythm disorder
 intersection_of: MONDO:0012061 ! familial sick sinus syndrome
 intersection_of: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/10593 ! SCN5A
 relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/10593 {source="OMIM:608567"} ! SCN5A
 property_value: curated_content_resource "https://www.malacards.org/card/sick_sinus_syndrome_1" xsd:anyURI {source="MONDO:MalaCards"}
+property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9707" xsd:anyURI
 
 [Term]
 id: MONDO:0024563
@@ -621534,6 +621559,23 @@ is_a: MONDO:0005451 {source="PMID:38849953"} ! eating disorder
 property_value: http://purl.org/dc/terms/creator https://orcid.org/0000-0003-3311-7320
 property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9408" xsd:anyURI
 
+[Term]
+id: MONDO:7770003
+name: cardiogenetic rhythm disorder
+def: "A heterogeneous group of cardiac rhythm phenotypes with a monogenic etiology that include, but are not limited to, atrial fibrillation, sick sinus syndrome, progressive cardiac conduction disease, ventricular fibrillation, Brugada syndrome, long QT syndrome, short QT syndrome, tachycardia with fibrillation, etc." [https://clinicalgenome.org/affiliation/40104/, https://github.com/monarch-initiative/mondo/issues/9707#issuecomment-3473275647]
+is_a: MONDO:0007263 {source="https://clinicalgenome.org/affiliation/40104/"} ! cardiac rhythm disease
+is_a: MONDO:0100547 {source="https://clinicalgenome.org/affiliation/40104/"} ! cardiogenetic disease
+property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9707" xsd:anyURI
+
+[Term]
+id: MONDO:7770004
+name: SCN5A-related cardiac rhythm disorder
+def: "A heterogeneous collection of cardiac rhythm disorders caused by genetic variation in the SCN5A gene with autosomal dominant inheritance. Affected individuals are commonly reported to have unremarkable cardiac morphology and at least one cardiac rhythm phenotype that includes, but is not limited to, atrial fibrillation, sick sinus syndrome, progressive cardiac conduction disease, ventricular fibrillation, long QT syndrome, and Brugada syndrome. Individuals with pathogenic variants in SCN5A may also exhibit overlapping or mixed cardiac rhythm phenotypes and intrafamilial variability." [https://clinicalgenome.org/affiliation/40104/, https://github.com/monarch-initiative/mondo/issues/9707#issuecomment-3473275647]
+is_a: MONDO:7770003 {source="https://clinicalgenome.org/affiliation/40104/"} ! cardiogenetic rhythm disorder
+relationship: has_characteristic HP:0000006 {source="https://clinicalgenome.org/affiliation/40104/"} ! Autosomal dominant inheritance
+relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/10593 {source="https://clinicalgenome.org/affiliation/40104/"} ! SCN5A
+property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9707" xsd:anyURI
+
 [Term]
 id: MONDO:8000000
 name: infectious discitis

```

### Attempt 10: claude-haiku-4.5 / claude

- **Eval PR**: [#427](https://github.com/ai4curation/eval-ont-agent-mondo/pull/427)
- **F1**: 0.216  **Precision**: 0.167  **Recall**: 0.308  **Jaccard**: 0.121
- **Trace**: [25844234243](https://github.com/ai4curation/eval-ont-agent-mondo/tree/master/traces/25844234243)
- **Workflow run**: [25844234243](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25844234243)

#### Agent PR Comment

# PR Summary: SCN5A-Related Cardiac Rhythm Disorder Terms

## Overview
This PR implements issue #9707 from the ClinGen Hereditary Cardiovascular Disease Gene Curation Expert Panel (GCEP), creating a new parent term and a gene-specific term to organize SCN5A-related cardiac rhythm phenotypes in MONDO.

## Changes Made

### 1. New Parent Term: `cardiogenetic rhythm disorders` (MONDO:7770003)
- **Parent**: MONDO:0100547 (cardiogenetic disease)
- **Purpose**: Groups monogenic cardiac rhythm phenotypes with various genetic etiologies
- **Definition**: "A heterogeneous group of cardiac rhythm phenotypes with a monogenic etiology that include, but are not limited to, atrial fibrillation, sick sinus syndrome, progressive cardiac conduction disease, ventricular fibrillation, Brugada syndrome, long QT syndrome, short QT syndrome, tachycardia with fibrillation, etc."
- **Source**: ClinGen GCEP (https://www.clinicalgenome.org/affiliation/40104/)

### 2. New Gene-Specific Term: `SCN5A-related cardiac rhythm disorder` (MONDO:7770004)
- **Parents**:
  1. MONDO:0100547 (cardiogenetic disease)
  2. MONDO:0007263 (cardiac rhythm disease)
  3. MONDO:7770003 (cardiogenetic rhythm disorders)
- **Logical Relationship**: `has_material_basis_in_germline_mutation_in` SCN5A (HGNC:10593)
- **Definition**: "A heterogeneous collection of cardiac rhythm disorders caused by genetic variation in the SCN5A gene with autosomal dominant inheritance. Affected individuals are commonly reported to have unremarkable cardiac morphology and at least one cardiac rhythm phenotype that includes, but is not limited to, atrial fibrillation, sick sinus syndrome, progressive cardiac conduction disease, ventricular fibrillation, long QT syndrome, and Brugada syndrome. Individuals with pathogenic variants in SCN5A may also exhibit overlapping or mixed cardiac rhythm phenotypes and intrafamilial variability."
- **Source**: ClinGen GCEP (https://www.clinicalgenome.org/affiliation/40104/)

### 3. Updated Existing Terms
Five existing SCN5A-related phenotype terms were updated to include MONDO:7770004 as a parent:

| Term ID | Term Name | Previous Parent(s) | New Parent Added |
|---------|-----------|-------------------|------------------|
| MONDO:0011001 | Brugada syndrome 1 | MONDO:0015263 | MONDO:7770004 |
| MONDO:0011376 | Ventricular fibrillation, paroxysmal familial, type 1 | MONDO:0100234 | MONDO:7770004 |
| MONDO:0011377 | Long QT syndrome 3 | MONDO:0019171 | MONDO:7770004 |
| MONDO:0013530 | Atrial fibrillation, familial, 10 | MONDO:0018054 | MONDO:7770004 |
| MONDO:0024562 | Sick sinus syndrome 1 | MONDO:0012061 | MONDO:7770004 |

## Implementation Details

### Methodology
1. Created batch file with two new terms following MONDO term creation conventions
2. Checked out existing SCN5A phenotype terms and added new parent relationships
3. Used `obo-checkin.pl` to integrate changes into the main ontology file
4. Verified all changes are present in `src/ontology/mondo-edit.obo`

### Quality Assurance
- ✅ All new terms have proper IDs from the 777xxxx NTR range
- ✅ All terms include definitions with ClinGen GCEP source attribution
- ✅ All terms include `term_tracker_item` pointing to GitHub issue #9707
- ✅ Gene identifier (SCN5A/HGNC:10593) is properly referenced in MONDO:7770004
- ✅ Existing term relationships maintained; only new parent relationships added
- ✅ No terms were removed; existing parents preserved for existing phenotype terms

### Checklist
- [x] Created new parent term (MONDO:7770003)
- [x] Created gene-specific term (MONDO:7770004)
- [x] Updated existing phenotype terms with new parent relationships
- [x] Verified all changes in mondo-edit.obo
- [x] Committed changes with appropriate commit message
- [x] Source attribution properly documented

## Notes
- The definitions use the revised version provided in the issue follow-up comment (removed "multifocal ectopic Purkinje-related premature contractions" as noted by @LengUNC)
- This change creates a hierarchical grouping that allows MONDO users to query all SCN5A-related cardiac rhythm phenotypes through MONDO:7770004
- The new parent term MONDO:7770003 (cardiogenetic rhythm disorders) can be expanded in the future with other gene-specific cardiac rhythm disorder terms

---
🤖 **Generated by claude agent**
- Runtime: `claude`
- Model: `claude-haiku-4-5-20251001`
- Agent config: `ai4curation/mondo-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25844234243)


#### Agent Issue Comment

# Issue #9707 Resolution

The requested ClinGen terms for SCN5A-related cardiac rhythm disorders have been successfully created and integrated into MONDO.

## Changes Completed

✅ Created two new MONDO terms as requested:
- **MONDO:7770003** - `cardiogenetic rhythm disorders` (parent term)
- **MONDO:7770004** - `SCN5A-related cardiac rhythm disorder` (gene-specific term)

✅ Updated five existing SCN5A-related phenotype terms with the new parent relationship to MONDO:7770004:
- MONDO:0011001 (Brugada syndrome 1)
- MONDO:0011376 (Ventricular fibrillation, paroxysmal familial, type 1)
- MONDO:0011377 (Long QT syndrome 3)
- MONDO:0013530 (Atrial fibrillation, familial, 10)
- MONDO:0024562 (Sick sinus syndrome 1)

## Implementation Notes

- Definitions were taken directly from the ClinGen GCEP specification (updated version without "multifocal ectopic Purkinje-related premature contractions" as requested in the follow-up comment by @LengUNC)
- Source attribution: https://www.clinicalgenome.org/affiliation/40104/
- Terms follow MONDO ontology conventions with proper parent-child relationships and SCN5A gene identifier linkage

Changes committed in PR #<NN>

---
🤖 **Generated by claude agent**
- Runtime: `claude`
- Model: `claude-haiku-4-5-20251001`
- Agent config: `ai4curation/mondo-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25844234243)


#### Agent Diff

```diff
diff --git a/src/ontology/mondo-edit.obo b/src/ontology/mondo-edit.obo
index 8aaf2a57d..391e147b1 100644
--- a/src/ontology/mondo-edit.obo
+++ b/src/ontology/mondo-edit.obo
@@ -257842,6 +257842,7 @@ xref: OMIM:601144 {source="DOID:0110218", source="MONDO:equivalentTo"}
 xref: Orphanet:130 {source="OMIM:601144"}
 xref: UMLS:C4551804 {source="MONDO:equivalentTo", source="MONDO:MEDGEN", source="MEDGEN:1646402"}
 is_a: MONDO:0015263 {source="DC-OMIM:601144", source="DOID:0110218", source="MONDO:Redundant", source="OMIM:601144"} ! Brugada syndrome
+is_a: MONDO:7770004 ! SCN5A-related cardiac rhythm disorder
 intersection_of: MONDO:0015263 ! Brugada syndrome
 intersection_of: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/10593 ! SCN5A
 relationship: curated_content_resource https://search.clinicalgenome.org/kb/conditions/MONDO:0011001 {source="MONDO:CLINGEN"}
@@ -267530,6 +267531,7 @@ xref: Orphanet:228140 {source="OMIM:603829"}
 xref: SCTID:233915000 {source="MONDO:equivalentTo"}
 xref: UMLS:C2751898 {source="MEDGEN:414502", source="MONDO:equivalentTo", source="MONDO:MEDGEN"}
 is_a: MONDO:0100234 {source="DC-OMIM:603829", source="MESH:C567851"} ! paroxysmal familial ventricular fibrillation
+is_a: MONDO:7770004 ! SCN5A-related cardiac rhythm disorder
 intersection_of: MONDO:0100234 ! paroxysmal familial ventricular fibrillation
 intersection_of: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/10593 ! SCN5A
 relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/10593 {source="OMIM:603829"} ! SCN5A
@@ -267562,6 +267564,7 @@ xref: Orphanet:101016 {source="OMIM:603830", source="MONDO:directSiblingOf"}
 xref: Orphanet:768 {source="OMIM:603830"}
 xref: UMLS:C1859062 {source="MONDO:equivalentTo", source="MONDO:MEDGEN", source="MEDGEN:349087"}
 is_a: MONDO:0019171 {source="OMIM:603830", source="Orphanet:101016-prototype"} ! familial long QT syndrome
+is_a: MONDO:7770004 ! SCN5A-related cardiac rhythm disorder
 intersection_of: MONDO:0019171 ! familial long QT syndrome
 intersection_of: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/10593 ! SCN5A
 relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/10593 {source="OMIM:603830"} ! SCN5A
@@ -323947,6 +323950,7 @@ xref: OMIM:614022 {source="MONDO:equivalentTo"}
 xref: Orphanet:334 {source="OMIM:614022"}
 xref: UMLS:C3151464 {source="MEDGEN:462814", source="MONDO:equivalentTo", source="MONDO:MEDGEN"}
 is_a: MONDO:0018054 {source="DC-OMIM:614022", source="MONDO:Redundant", source="OMIM:614022"} ! familial atrial fibrillation
+is_a: MONDO:7770004 ! SCN5A-related cardiac rhythm disorder
 intersection_of: MONDO:0018054 ! familial atrial fibrillation
 intersection_of: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/10593 ! SCN5A
 relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/10593 {source="OMIM:614022"} ! SCN5A
@@ -513335,6 +513339,7 @@ xref: OMIM:608567 {source="MONDO:equivalentTo"}
 xref: Orphanet:166282 {source="OMIM:608567"}
 xref: UMLS:C1837845 {source="MONDO:equivalentTo", source="MONDO:MEDGEN", source="MEDGEN:325270"}
 is_a: MONDO:0012061 {source="MONDO:0024562/inferred", source="MONDO:Redundant", source="OMIM:608567"} ! familial sick sinus syndrome
+is_a: MONDO:7770004 ! SCN5A-related cardiac rhythm disorder
 intersection_of: MONDO:0012061 ! familial sick sinus syndrome
 intersection_of: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/10593 ! SCN5A
 relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/10593 {source="OMIM:608567"} ! SCN5A
@@ -621534,6 +621539,25 @@ is_a: MONDO:0005451 {source="PMID:38849953"} ! eating disorder
 property_value: http://purl.org/dc/terms/creator https://orcid.org/0000-0003-3311-7320
 property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9408" xsd:anyURI
 
+[Term]
+id: MONDO:7770003
+name: cardiogenetic rhythm disorders
+def: "A heterogeneous group of cardiac rhythm phenotypes with a monogenic etiology that include, but are not limited to, atrial fibrillation, sick sinus syndrome, progressive cardiac conduction disease, ventricular fibrillation, Brugada syndrome, long QT syndrome, short QT syndrome, tachycardia with fibrillation, etc." [https://www.clinicalgenome.org/affiliation/40104/]
+is_a: MONDO:0100547 ! cardiogenetic disease
+property_value: http://purl.org/dc/terms/creator https://orcid.org/0000-0002-0736-9199
+property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9707" xsd:anyURI
+
+[Term]
+id: MONDO:7770004
+name: SCN5A-related cardiac rhythm disorder
+def: "A heterogeneous collection of cardiac rhythm disorders caused by genetic variation in the SCN5A gene with autosomal dominant inheritance. Affected individuals are commonly reported to have unremarkable cardiac morphology and at least one cardiac rhythm phenotype that includes, but is not limited to, atrial fibrillation, sick sinus syndrome, progressive cardiac conduction disease, ventricular fibrillation, long QT syndrome, and Brugada syndrome. Individuals with pathogenic variants in SCN5A may also exhibit overlapping or mixed cardiac rhythm phenotypes and intrafamilial variability." [https://www.clinicalgenome.org/affiliation/40104/]
+is_a: MONDO:0100547 ! cardiogenetic disease
+is_a: MONDO:0007263 ! cardiac rhythm disease
+is_a: MONDO:7770003 ! cardiogenetic rhythm disorders
+relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/10593 ! SCN5A
+property_value: http://purl.org/dc/terms/creator https://orcid.org/0000-0002-0736-9199
+property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9707" xsd:anyURI
+
 [Term]
 id: MONDO:8000000
 name: infectious discitis

```

### Attempt 11: claude-haiku-4.5 / claude

- **Eval PR**: [#300](https://github.com/ai4curation/eval-ont-agent-mondo/pull/300)
- **F1**: 0.216  **Precision**: 0.167  **Recall**: 0.308  **Jaccard**: 0.121
- **Trace**: [25762192649](https://github.com/ai4curation/eval-ont-agent-mondo/tree/master/traces/25762192649)

#### Agent Diff

```diff
diff --git a/src/ontology/mondo-edit.obo b/src/ontology/mondo-edit.obo
index 8aaf2a57d..391e147b1 100644
--- a/src/ontology/mondo-edit.obo
+++ b/src/ontology/mondo-edit.obo
@@ -257842,6 +257842,7 @@ xref: OMIM:601144 {source="DOID:0110218", source="MONDO:equivalentTo"}
 xref: Orphanet:130 {source="OMIM:601144"}
 xref: UMLS:C4551804 {source="MONDO:equivalentTo", source="MONDO:MEDGEN", source="MEDGEN:1646402"}
 is_a: MONDO:0015263 {source="DC-OMIM:601144", source="DOID:0110218", source="MONDO:Redundant", source="OMIM:601144"} ! Brugada syndrome
+is_a: MONDO:7770004 ! SCN5A-related cardiac rhythm disorder
 intersection_of: MONDO:0015263 ! Brugada syndrome
 intersection_of: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/10593 ! SCN5A
 relationship: curated_content_resource https://search.clinicalgenome.org/kb/conditions/MONDO:0011001 {source="MONDO:CLINGEN"}
@@ -267530,6 +267531,7 @@ xref: Orphanet:228140 {source="OMIM:603829"}
 xref: SCTID:233915000 {source="MONDO:equivalentTo"}
 xref: UMLS:C2751898 {source="MEDGEN:414502", source="MONDO:equivalentTo", source="MONDO:MEDGEN"}
 is_a: MONDO:0100234 {source="DC-OMIM:603829", source="MESH:C567851"} ! paroxysmal familial ventricular fibrillation
+is_a: MONDO:7770004 ! SCN5A-related cardiac rhythm disorder
 intersection_of: MONDO:0100234 ! paroxysmal familial ventricular fibrillation
 intersection_of: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/10593 ! SCN5A
 relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/10593 {source="OMIM:603829"} ! SCN5A
@@ -267562,6 +267564,7 @@ xref: Orphanet:101016 {source="OMIM:603830", source="MONDO:directSiblingOf"}
 xref: Orphanet:768 {source="OMIM:603830"}
 xref: UMLS:C1859062 {source="MONDO:equivalentTo", source="MONDO:MEDGEN", source="MEDGEN:349087"}
 is_a: MONDO:0019171 {source="OMIM:603830", source="Orphanet:101016-prototype"} ! familial long QT syndrome
+is_a: MONDO:7770004 ! SCN5A-related cardiac rhythm disorder
 intersection_of: MONDO:0019171 ! familial long QT syndrome
 intersection_of: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/10593 ! SCN5A
 relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/10593 {source="OMIM:603830"} ! SCN5A
@@ -323947,6 +323950,7 @@ xref: OMIM:614022 {source="MONDO:equivalentTo"}
 xref: Orphanet:334 {source="OMIM:614022"}
 xref: UMLS:C3151464 {source="MEDGEN:462814", source="MONDO:equivalentTo", source="MONDO:MEDGEN"}
 is_a: MONDO:0018054 {source="DC-OMIM:614022", source="MONDO:Redundant", source="OMIM:614022"} ! familial atrial fibrillation
+is_a: MONDO:7770004 ! SCN5A-related cardiac rhythm disorder
 intersection_of: MONDO:0018054 ! familial atrial fibrillation
 intersection_of: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/10593 ! SCN5A
 relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/10593 {source="OMIM:614022"} ! SCN5A
@@ -513335,6 +513339,7 @@ xref: OMIM:608567 {source="MONDO:equivalentTo"}
 xref: Orphanet:166282 {source="OMIM:608567"}
 xref: UMLS:C1837845 {source="MONDO:equivalentTo", source="MONDO:MEDGEN", source="MEDGEN:325270"}
 is_a: MONDO:0012061 {source="MONDO:0024562/inferred", source="MONDO:Redundant", source="OMIM:608567"} ! familial sick sinus syndrome
+is_a: MONDO:7770004 ! SCN5A-related cardiac rhythm disorder
 intersection_of: MONDO:0012061 ! familial sick sinus syndrome
 intersection_of: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/10593 ! SCN5A
 relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/10593 {source="OMIM:608567"} ! SCN5A
@@ -621534,6 +621539,25 @@ is_a: MONDO:0005451 {source="PMID:38849953"} ! eating disorder
 property_value: http://purl.org/dc/terms/creator https://orcid.org/0000-0003-3311-7320
 property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9408" xsd:anyURI
 
+[Term]
+id: MONDO:7770003
+name: cardiogenetic rhythm disorders
+def: "A heterogeneous group of cardiac rhythm phenotypes with a monogenic etiology that include, but are not limited to, atrial fibrillation, sick sinus syndrome, progressive cardiac conduction disease, ventricular fibrillation, Brugada syndrome, long QT syndrome, short QT syndrome, tachycardia with fibrillation, etc." [https://www.clinicalgenome.org/affiliation/40104/]
+is_a: MONDO:0100547 ! cardiogenetic disease
+property_value: http://purl.org/dc/terms/creator https://orcid.org/0000-0002-0736-9199
+property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9707" xsd:anyURI
+
+[Term]
+id: MONDO:7770004
+name: SCN5A-related cardiac rhythm disorder
+def: "A heterogeneous collection of cardiac rhythm disorders caused by genetic variation in the SCN5A gene with autosomal dominant inheritance. Affected individuals are commonly reported to have unremarkable cardiac morphology and at least one cardiac rhythm phenotype that includes, but is not limited to, atrial fibrillation, sick sinus syndrome, progressive cardiac conduction disease, ventricular fibrillation, long QT syndrome, and Brugada syndrome. Individuals with pathogenic variants in SCN5A may also exhibit overlapping or mixed cardiac rhythm phenotypes and intrafamilial variability." [https://www.clinicalgenome.org/affiliation/40104/]
+is_a: MONDO:0100547 ! cardiogenetic disease
+is_a: MONDO:0007263 ! cardiac rhythm disease
+is_a: MONDO:7770003 ! cardiogenetic rhythm disorders
+relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/10593 ! SCN5A
+property_value: http://purl.org/dc/terms/creator https://orcid.org/0000-0002-0736-9199
+property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9707" xsd:anyURI
+
 [Term]
 id: MONDO:8000000
 name: infectious discitis

```
