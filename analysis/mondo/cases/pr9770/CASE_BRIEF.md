---
ontology: mondo
repo: monarch-initiative/mondo
issue_number: 9703
pr_number: 9770
issue_title: Updates to Gene-Disease Classifications and Inheritance Patterns for
  Porphyria Disease Entities - ClinGen EIM group
pr_author: sabrinatoro
pr_merged_at: '2025-11-20'
task_type: reclassification
difficulty: hard
scoping: tightly_scoped
scope: multi_term
review_outcome: changes_requested
num_agent_attempts: 10
generated_at: '2026-05-17'
scoping_notes: Changes focused on porphyria disease branch with minor supporting infrastructure
  changes.
domain_area: rare-disease
best_f1: 0.923
best_model: gpt-5.4
---

# PR #9770 — Updates to Gene-Disease Classifications and Inheritance Patterns for Porphyria Disease Entities - ClinGen EIM group

**mondo** | [monarch-initiative/mondo](https://github.com/monarch-initiative/mondo) | [Issue #9703](https://github.com/monarch-initiative/mondo/issues/9703) | [PR #9770](https://github.com/monarch-initiative/mondo/pull/9770) | @sabrinatoro | merged 2025-11-20

`reclassification` `hard` `tightly_scoped` `changes_requested`

## Context

The ClinGen Errors of Inborn Metabolism (EIM) group requested comprehensive updates to porphyria disease entities in Mondo. This included new gene-disease classifications, updated inheritance patterns, new labels, and new child terms. The changes were coordinated via a shared spreadsheet tracking all required updates across the porphyria disease branch.

Porphyrias are a group of metabolic disorders caused by enzyme deficiencies in the heme biosynthesis pathway. Accurate classification requires understanding both the biochemical pathway and the clinical presentations, which differ between acute and cutaneous forms.

## Changes Made

The PR made 60 additions and 9 deletions across `src/ontology/mondo-edit.obo`, involving new labels, new terms, updated inheritance annotations, and restructured classification for multiple porphyria entities. A minor Makefile update and a new SPARQL QC query for detecting underscores in definitions were also included. The 7 commits reflect an iterative curation process responding to expert review feedback.

## Resolution

Hard difficulty because the porphyria branch restructure required coordinating multiple types of changes (new terms, relabeling, inheritance updates, reclassification) across several related terms while maintaining consistency with ClinGen's expert classifications. An agent would need to interpret the spreadsheet-based requirements and apply domain-specific knowledge about porphyria subtypes.

## Curation Note (data quality)

Flagged `case_quality: poor` by claude-opus-4.7 on 2026-05-15.

**Single-PR resolution (no companion PRs).** Issue #9703 was resolved entirely by PR #9770
(`gh search prs "9703"` returns only #9770; the other porphyria PRs — #8394, #8206, #5151,
#2855 — are unrelated older work). Step 3a does not apply.

**Placeholder-vs-canonical MONDO ID artifact (primary reason).** The gold PR created three
new grouping terms with registered IDs:

- `MONDO:0700382` HMBS-related hepatic porphyria
- `MONDO:0700383` PPOX-related hepatic porphyria
- `MONDO:0700384` porphyria, acute intermittent, nonerythroid variant

The `ai4curation/mondo-agent-config` CLAUDE.md explicitly instructs agents: *"New terms
start MONDO:777xxxx"*. All four attempts correctly followed this and used
`MONDO:7770003/7770004/7770005`. OBO metadiff does not normalize new-term ID minting, so
every `id:`, `name:`, `def:`, `intersection_of:` line on the three new terms **and** every
lumping `is_a:` axiom that references a new ID (≈6 lines pointing existing porphyria
entities at the new HMBS/PPOX/UROD groupers) is scored as a miss by construction, in every
attempt — including the strongest run. This systematically caps F1 far below substantive
quality (best observed F1 = 0.441; substance is appreciably better). Downstream
scoring/aggregation should down-weight or exclude this case, and reviewers should judge
attempts on substance (correct gene-grouping equivalence axioms `hepatic porphyria` +
`has_material_basis_in_germline_mutation_in <gene>`, correct lumping targets, faithful
GCEP definitions, ClinGen-attributed synonyms, `term_tracker_item` provenance) rather than
the metadiff.

**Separate genuine error common to all attempts (NOT an artifact).** Every agent renamed
the primary `name:` of ~6 existing terms (MONDO:0008319, 0009902, 0010420, 0013000,
0100498, 0800180), demoting the original labels to synonyms. The curator deliberately did
**not** rename any existing term — the ClinGen names were added only as EXACT synonyms
(with the `OMO:0002001` ClinGen qualifier) while primary labels were preserved. This is a
legitimate quality finding scored in the individual reviews (`wrong_pattern`) and is not
covered by the ID-artifact caveat.

## Human Diff

```diff
diff --git a/src/ontology/Makefile b/src/ontology/Makefile
index 154b8442ee..46f666869d 100644
--- a/src/ontology/Makefile
+++ b/src/ontology/Makefile
@@ -860,7 +860,7 @@ SPARQL_EDIT_EXCLUDE=
 # the ontology begin looking like this: http://purl.obolibrary.org/obo/mondo/mondo-base#... This
 # will cause the query to fail because it expects the IRI  http://purl.obolibrary.org/obo/mondo#ABREVIATION
 # for the duplicate-exact-synonym-no-abbrev check.
-SPARQL_OBO_EXCLUDE=qc-single-child qc-omimps-should-be-inherited qc-omim-subsumption qc-permitted-properties qc-duplicate-exact-synonym-no-abbrev qc-multiple-gene-associations qc-subclass-relation-no-source
+SPARQL_OBO_EXCLUDE=qc-single-child qc-omimps-should-be-inherited qc-omim-subsumption qc-permitted-properties qc-duplicate-exact-synonym-no-abbrev qc-multiple-gene-associations qc-subclass-relation-no-source qc-definition-containing-underscore
 SPARQL_OWL_EXCLUDE=qc-permitted-properties
 SPARQL_GENERAL_QC_EDIT=$(filter-out $(SPARQL_EDIT_EXCLUDE),$(SPARQL_GENERAL_QC))
 SPARQL_GENERAL_QC_OWL=$(filter-out $(SPARQL_OWL_EXCLUDE),$(SPARQL_GENERAL_QC))
diff --git a/src/ontology/mondo-edit.obo b/src/ontology/mondo-edit.obo
index 1cb7a9c08b..960785b57e 100644
--- a/src/ontology/mondo-edit.obo
+++ b/src/ontology/mondo-edit.obo
@@ -179763,10 +179763,12 @@ xref: SCTID:90842001 {source="DOID:3890"}
 xref: UMLS:C0162565 {source="MONDO:equivalentTo", source="MONDO:MEDGEN", source="MEDGEN:56452"}
 is_a: MONDO:0002520 {source="DOID:3890", source="MESH:D017118", source="Orphanet:79276"} ! hepatic porphyria
 is_a: MONDO:0019142 {source="DOID:3890/inferred", source="MESH:D017118/inferred", source="MONDO:Redundant", source="NCIT:C84536", source="Orphanet:79276/inferred"} ! inherited porphyria
+is_a: MONDO:0700382 {source="https://clinicalgenome.org/affiliation/40097/"} ! HMBS-related hepatic porphyria
 relationship: curated_content_resource https://search.clinicalgenome.org/kb/conditions/MONDO:0008294 {source="MONDO:CLINGEN"}
 relationship: has_characteristic PATO:0000389 ! acute
 relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/4982 {source="OMIM:176000"} ! HMBS
 property_value: curated_content_resource "https://www.malacards.org/card/porphyria_acute_intermittent" xsd:anyURI {source="MONDO:MalaCards"}
+property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9703" xsd:anyURI
 
 [Term]
 id: MONDO:0008295
@@ -179834,8 +179836,7 @@ xref: Orphanet:95159 {source="OMIM:176100", source="MONDO:directSiblingOf"}
 xref: SCTID:59229005 {source="MONDO:equivalentTo"}
 xref: UMLS:C0268323 {source="MEDGEN:75669", source="MONDO:equivalentTo", source="MONDO:MEDGEN"}
 is_a: MONDO:0015104 {source="MONDO:Redundant", source="Orphanet:443062", source="icd11.foundation:1318287619"} ! porphyria cutanea tarda
-intersection_of: MONDO:0015104 ! porphyria cutanea tarda
-intersection_of: has_characteristic MONDO:0021152 ! inherited
+is_a: MONDO:0100498 {source="https://clinicalgenome.org/affiliation/40097/"} ! UROD-related inherited porphyria
 relationship: excluded_from_qc_check http://purl.obolibrary.org/obo/mondo/sparql/qc/general/qc-single-child.sparql
 relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/12591 {source="OMIM:176100"} ! UROD
 property_value: curated_content_resource "https://www.malacards.org/card/familial_porphyria_cutanea_tarda" xsd:anyURI {source="MONDO:MalaCards"}
@@ -179880,9 +179881,11 @@ xref: SCTID:58275005 {source="DOID:4346", source="MONDO:equivalentTo"}
 xref: UMLS:C0162532 {source="MONDO:equivalentTo", source="MONDO:MEDGEN", source="MEDGEN:58118"}
 is_a: MONDO:0002520 {source="DOID:4346", source="MESH:D046350", source="Orphanet:79473"} ! hepatic porphyria
 is_a: MONDO:0019142 {source="DOID:4346/inferred", source="MESH:D046350/inferred", source="MONDO:Redundant", source="NCIT:C85219", source="Orphanet:79473/inferred"} ! inherited porphyria
+is_a: MONDO:0700383 {source="https://clinicalgenome.org/affiliation/40097/"} ! PPOX-related hepatic porphyria
 relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/9280 {source="OMIM:176200"} ! PPOX
 property_value: curated_content_resource "https://www.malacards.org/card/variegate_porphyria" xsd:anyURI {source="MONDO:MalaCards"}
 property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/4521" xsd:anyURI
+property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9703" xsd:anyURI
 property_value: seeAlso "https://rarediseases.info.nih.gov/diseases/7848/variegate-porphyria" xsd:anyURI {source="GARD:0007848"}
 
 [Term]
@@ -180473,7 +180476,7 @@ property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/
 [Term]
 id: MONDO:0008319
 name: protoporphyria, erythropoietic, 1
-def: "Erythropoietic protoporphyria caused by a compound heterozygous or homozygous mutation in the gene encoding ferrochelatase (FECH) on chromosome 18q21." [OMIM:177000]
+def: "An erythropoietic protoporphyria caused by biallelic variants in FECH (an autosomal recessive inheritance pattern) and causing primarily accumulation of protoporphyrin IX. Symptoms include extremely painful photosensitivity in childhood, possible microcytic anemia, cholelithiasis, and ~5% of patients develop liver failure. The majority of individuals with FECH-related erythropoietic protoporphyria harbor a hypomorphic variant (NM_000140.5:c.315-48T>C), which reduces enzyme levels by ~35%, in trans to a second pathogenic variant. Clinically individuals with this form of porphyria cannot be distinguished from those with ALAS2-related erythropoietic protoporphyria." [https://clinicalgenome.org/affiliation/40097/]
 subset: clingen {source="MONDO:CLINGEN"}
 subset: gard_rare {source="MONDO:GARD"}
 subset: nord_rare {source="MONDO:NORD"}
@@ -180482,6 +180485,7 @@ synonym: "EPP" RELATED ABBREVIATION [GARD:0004527, MONDO:Lexical]
 synonym: "EPP1" EXACT ABBREVIATION [OMIM:177000]
 synonym: "erythrohepatic protoporphyria" RELATED [GARD:0004527]
 synonym: "erythropoietic protoporphyria" BROAD []
+synonym: "FECH-related erythropoietic protoporphyria" EXACT [https://clinicalgenome.org/affiliation/40097/] {OMO:0002001="https://w3id.org/information-resource-registry/clingen"}
 synonym: "ferrochelatase deficiency" EXACT [GARD:0004527, OMIM:177000]
 synonym: "heme synthetase deficiency" EXACT [GARD:0004527, OMIM:177000]
 synonym: "protoporphyria, erythropoietic" BROAD [MONDO:Lexical]
@@ -180496,7 +180500,9 @@ xref: UMLS:C4692546 {source="MEDGEN:1643471", source="MONDO:equivalentTo", sourc
 is_a: MONDO:0019142 {source="MONDO:Redundant", source="NCIT:C84698"} ! inherited porphyria
 is_a: MONDO:0019263 {source="DC-OMIM:177000", source="OMIM:177000"} ! autosomal erythropoietic protoporphyria
 relationship: curated_content_resource https://search.clinicalgenome.org/kb/conditions/MONDO:0008319 {source="MONDO:CLINGEN"}
+relationship: excluded_from_qc_check http://purl.obolibrary.org/obo/mondo/sparql/qc/general/qc-definition-containing-underscore.sparql
 relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/3647 {source="OMIM:177000"} ! FECH
+property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9703" xsd:anyURI
 
 [Term]
 id: MONDO:0008320
@@ -225910,7 +225916,7 @@ property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/
 [Term]
 id: MONDO:0009902
 name: cutaneous porphyria
-def: "Congenital erythropoietic porphyria, or Günther disease, is a form of erythropoietic porphyria characterized by very severe and mutilating photodermatosis." [Orphanet:79277]
+def: "An erythropoietic porphyria (massive accumulation of photoreactive porphyrins in the bone marrow erythroid cells and circulating erythrocytes, resulting in cutaneous photosensitivity) caused by biallelic variants in UROS (in an autosomal recessive inheritance pattern). Cases where biallelic variants reduce WT enzyme activity to <5% are characterized by photosensitivity, hemolytic anemia (often in utero), erythrodontia, splenomegaly, cutaneous blistering, scarring and disfigurement. Other cases where biallelic variants do not reduce enzyme activity as severely (5-12% of WT activity) have a later onset of photosensitivity and milder symptoms." [https://clinicalgenome.org/affiliation/40097/]
 subset: gard_rare {source="GARD:4446", source="MONDO:GARD"}
 subset: nord_rare {source="MONDO:NORD", source="NORD:1599"}
 subset: ordo_disorder {source="Orphanet:79277"}
@@ -225930,6 +225936,7 @@ synonym: "porphyria, congenital erythropoietic" RELATED []
 synonym: "uroporphyrinogen 3 synthase deficiency" RELATED []
 synonym: "uroporphyrinogen III synthase, deficiency of" RELATED [GARD:0004446]
 synonym: "Uros deficiency" RELATED []
+synonym: "UROS-related erythropoietic porphyria" EXACT [https://clinicalgenome.org/affiliation/40097/] {OMO:0002001="https://w3id.org/information-resource-registry/clingen"}
 xref: DOID:13271 {source="MONDO:equivalentTo"}
 xref: GARD:4446 {source="MONDO:GARD"}
 xref: ICD10CM:E80.0 {source="DOID:13271", source="Orphanet:79277/inclusion", source="Orphanet:79277/ntbt", source="Orphanet:79277"}
@@ -225950,6 +225957,7 @@ is_a: MONDO:0019142 {source="DC-OMIM:263700", source="DOID:13271", source="MESH:
 is_a: MONDO:0020585 {source="MONDO:0020104-obsoleted"} ! anemia due to erythrocyte enzyme disorder
 relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/12592 {source="OMIM:263700"} ! UROS
 property_value: curated_content_resource "https://www.malacards.org/card/porphyria_congenital_erythropoietic" xsd:anyURI {source="MONDO:MalaCards"}
+property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9703" xsd:anyURI
 
 [Term]
 id: MONDO:0009903
@@ -241099,13 +241107,14 @@ replaced_by: MONDO:0020721
 [Term]
 id: MONDO:0010420
 name: X-linked erythropoietic protoporphyria
-def: "X-linked form of erythropoietic protoporphyria." [MONDO:patterns/x_linked]
+def: "An erythropoietic protoporphyria in which the cause of the disease is a hemizygous, heterozygous, or homozygous (rare) gain-of-function (GOF) variant (X-linked inheritance pattern) in the terminal regulatory exon of ALAS2. GOF variants increase ALAS2 activity resulting in pathway upregulation and high levels of protoporphyrin IX (PPIX). Males with hemizygous variants frequently present in early childhood with severe cutaneous photosensitivity and laboratory markers of liver disease. Heterozygous females can present with symptoms ranging from as severe as affected males to asymptomatic due to random X-chromosome inactivation. This disease is clinically indistinguishable from FECH-related erythropoietic protoporphyria." [https://clinicalgenome.org/affiliation/40097/]
 subset: clingen {source="MONDO:CLINGEN"}
 subset: gard_rare {source="GARD:17755", source="MONDO:GARD"}
 subset: nord_rare {source="MONDO:NORD"}
 subset: ordo_disorder {source="Orphanet:443197"}
 subset: orphanet_rare {source="Orphanet:443197"}
 subset: rare
+synonym: "ALAS2-related erythropoietic protoporphyria" EXACT [https://clinicalgenome.org/affiliation/40097/] {OMO:0002001="https://w3id.org/information-resource-registry/clingen"}
 synonym: "Erythrohepatic protoporphyria, X-linked" RELATED []
 synonym: "erythropoietic protoporphyria, X-linked" EXACT [MONDO:patterns/x_linked]
 synonym: "protoporphyria, erythropoietic, X-linked" RELATED [MONDO:Lexical]
@@ -241132,6 +241141,7 @@ intersection_of: has_characteristic HP:0001417 ! X-linked inheritance
 relationship: curated_content_resource https://search.clinicalgenome.org/kb/conditions/MONDO:0010420 {source="MONDO:CLINGEN"}
 relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/397 {source="OMIM:300752"} ! ALAS2
 property_value: curated_content_resource "https://www.malacards.org/card/protoporphyria_erythropoietic_x_linked" xsd:anyURI {source="MONDO:MalaCards"}
+property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9703" xsd:anyURI
 
 [Term]
 id: MONDO:0010421
@@ -309739,7 +309749,7 @@ property_value: seeAlso "https://rarediseases.info.nih.gov/diseases/2578/guanidi
 [Term]
 id: MONDO:0013000
 name: porphyria due to ALA dehydratase deficiency
-def: "An extremely rare form of acute hepatic porphyria characterized by neuro-visceral attacks without cutaneous manifestations." [https://clinicalgenome.org/affiliation/40097/, https://orcid.org/0000-0002-0587-4693]
+def: "A hepatic porphyria caused by biallelic variants in ALAD (in an autosomal recessive inheritance pattern). This is an extremely rare form of hepatic porphyria characterized by neuro-visceral attacks, nausea, vomiting, diarrhea, neuropathy, and abdominal pain without cutaneous manifestations. Because the disease is so rare, inducible triggers are not well-documented." [https://clinicalgenome.org/affiliation/40097/]
 subset: clingen {source="MONDO:CLINGEN"}
 subset: gard_rare {source="GARD:16937", source="MONDO:GARD"}
 subset: nord_rare {source="NORD:747", source="MONDO:NORD"}
@@ -309754,7 +309764,8 @@ synonym: "ALA dehydratase deficiency pophyria" RELATED [GARD:0004445]
 synonym: "ALAD deficiency" RELATED []
 synonym: "ALAD Porphyria" EXACT [NORD:747, Orphanet:100924] {OMO:0002001="https://w3id.org/information-resource-registry/nord"}
 synonym: "ALAD porphyria" EXACT [Orphanet:100924]
-synonym: "ALAD-related porphyria" EXACT [https://clinicalgenome.org/affiliation/40097/] {OMO:0002001="https://w3id.org/information-resource-registry/clingen"}
+synonym: "ALAD-related hepatic porphyria" EXACT [https://clinicalgenome.org/affiliation/40097/] {OMO:0002001="https://w3id.org/information-resource-registry/clingen"}
+synonym: "ALAD-related porphyria" EXACT [https://clinicalgenome.org/affiliation/40097/]
 synonym: "aminolevulinate dehydratase deficiency porphyria" RELATED [GARD:0004445]
 synonym: "Delta-aminolevulinate dehydratase deficiency" RELATED []
 synonym: "Doss porphyria" RELATED []
@@ -309779,6 +309790,7 @@ relationship: curated_content_resource https://search.clinicalgenome.org/kb/cond
 relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/395 {source="OMIM:612740"} ! ALAD
 property_value: curated_content_resource "https://www.malacards.org/card/porphyria_acute_hepatic" xsd:anyURI {source="MONDO:MalaCards"}
 property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/8036" xsd:anyURI
+property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9703" xsd:anyURI
 property_value: seeAlso "https://rarediseases.info.nih.gov/diseases/4445/aminolevulinate-dehydratase-deficiency-porphyria" xsd:anyURI {source="GARD:0004445"}
 
 [Term]
@@ -467669,6 +467681,7 @@ xref: Orphanet:95159 {source="MONDO:equivalentTo"}
 xref: SCTID:111386004 {source="MONDO:equivalentTo", source="DOID:5230"}
 xref: UMLS:C0162569 {source="MONDO:equivalentTo", source="MONDO:MEDGEN", source="MEDGEN:57940"}
 is_a: MONDO:0015104 {source="NCIT:C84754"} ! porphyria cutanea tarda
+is_a: MONDO:0100498 {source="https://clinicalgenome.org/affiliation/40097/"} ! UROD-related inherited porphyria
 relationship: excluded_from_qc_check http://purl.obolibrary.org/obo/mondo/sparql/qc/general/qc-single-child.sparql
 relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/12591 {source="Orphanet:95159"} ! UROD
 property_value: curated_content_resource "https://www.malacards.org/card/hepatoerythropoietic_porphyria" xsd:anyURI {source="MONDO:MalaCards"}
@@ -566370,17 +566383,19 @@ property_value: http://purl.org/dc/terms/creator https://orcid.org/0000-0001-520
 [Term]
 id: MONDO:0100498
 name: UROD-related inherited porphyria
-def: "Any inherited porphyria in which the cause of the disease is monoallelic or biallelic variants in the UROD gene." [https://clinicalgenome.org/affiliation/40097/, MONDO:patterns/disease_series_by_gene]
+def: "Porphyria caused by monoallelic and biallelic variants in UROD and presenting as a spectrum of disease (a semidominant inheritance pattern). Additionally, environmental factors almost always play a role in the disease. Monoallelic variants when exacerbated by environmental factors can result in episodic adult onset of photosensitivity. Biallelic variants that reduce WT enzyme activity <20% cause childhood onset of photosensitivity and sometimes liver damage." [https://clinicalgenome.org/affiliation/40097/]
 subset: clingen {source="MONDO:CLINGEN"}
 subset: gard_rare {source="MONDO:GARD"}
 subset: otar {source="MONDO:OTAR"}
 subset: rare
+synonym: "UROD-related porphyria" EXACT [https://clinicalgenome.org/affiliation/40097/] {OMO:0002001="https://w3id.org/information-resource-registry/clingen"}
 is_a: MONDO:0019142 {source="https://clinicalgenome.org/affiliation/40097/"} ! inherited porphyria
 intersection_of: MONDO:0019142 ! inherited porphyria
 intersection_of: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/12591 ! UROD
 relationship: curated_content_resource https://search.clinicalgenome.org/kb/conditions/MONDO:0100498 {source="MONDO:CLINGEN"}
 property_value: http://purl.org/dc/terms/creator https://orcid.org/0000-0001-5208-3432
 property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/5128" xsd:anyURI
+property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9703" xsd:anyURI
 
 [Term]
 id: MONDO:0100499
@@ -572748,6 +572763,34 @@ intersection_of: MONDO:0031166 ! macular dystrophy, retinal
 intersection_of: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/14550 ! CDHR1
 property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/8986" xsd:anyURI
 
+[Term]
+id: MONDO:0700382
+name: HMBS-related hepatic porphyria
+def: "A hepatic porphyria caused by monoallelic and biallelic variants in HMBS and presenting as a spectrum of disease (a semidominant inheritance pattern). Monoallelic variants predispose to acute/episodic attacks in adulthood with abdominal pain, neuropathy, and neuropsychiatric symptoms (women are more often affected) without cutaneous manifestations. Triggers precipitating acute attacks include estrogen/progesterone, oral contraceptives, alcohol, drugs, stress, or infections. Biallelic variants cause severe disease in childhood presenting with neurological issues including developmental abnormalities, ataxia, dysarthria, leukoencephalopathy, cataracts and optic nerve hypoplasia." [https://clinicalgenome.org/affiliation/40097/]
+synonym: "HMBS-related hepatic porphyria" EXACT [https://clinicalgenome.org/affiliation/40097/] {OMO:0002001="https://w3id.org/information-resource-registry/clingen"}
+is_a: MONDO:0002520 {source="https://clinicalgenome.org/affiliation/40097/"} ! hepatic porphyria
+intersection_of: MONDO:0002520 ! hepatic porphyria
+intersection_of: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/4982 ! HMBS
+property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9703" xsd:anyURI
+
+[Term]
+id: MONDO:0700383
... (97 more lines truncated)
```

## Agent Attempts (10)

| # | Model | Runtime | F1 | P | R | Blob | Eval PR | Detail |
|---|-------|---------|-----|-----|-----|------|---------|--------|
| 1 | gpt-5.4 | codex | 0.923 | 0.857 | 1.000 | `960785b` | [#576](https://github.com/ai4curation/eval-ont-agent-mondo/pull/576) | [attempt](attempts/pr576.md) |
| 2 | gpt-5.4 | codex | 0.923 | 0.857 | 1.000 | `960785b` | [#156](https://github.com/ai4curation/eval-ont-agent-mondo/pull/156) | [attempt](attempts/pr156.md) |
| 3 | claude-opus-4.7 | claude | 0.441 | 0.531 | 0.377 | `45d5d9b` | [#409](https://github.com/ai4curation/eval-ont-agent-mondo/pull/409) | [attempt](attempts/pr409.md) |
| 4 | gpt-5.4 | opencode | 0.273 | 0.306 | 0.246 | `28c7285` | [#769](https://github.com/ai4curation/eval-ont-agent-mondo/pull/769) | [attempt](attempts/pr769.md) |
| 5 | gpt-5.4 | opencode | 0.273 | 0.306 | 0.246 | `28c7285` | [#714](https://github.com/ai4curation/eval-ont-agent-mondo/pull/714) | [attempt](attempts/pr714.md) |
| 6 | gpt-5.5 | opencode | 0.268 | 0.347 | 0.218 | `8b95d2a` | [#91](https://github.com/ai4curation/eval-ont-agent-mondo/pull/91) | [attempt](attempts/pr91.md) |
| 7 | gpt-5.5 | opencode | 0.268 | 0.347 | 0.218 | `8b95d2a` | [#74](https://github.com/ai4curation/eval-ont-agent-mondo/pull/74) | [attempt](attempts/pr74.md) |
| 8 | gpt-5.5 | codex | 0.252 | 0.286 | 0.226 | `b0039e3` | [#53](https://github.com/ai4curation/eval-ont-agent-mondo/pull/53) | [attempt](attempts/pr53.md) |
| 9 | claude-sonnet-4.5 | claude | 0.243 | 0.286 | 0.212 | `175d21f` | [#604](https://github.com/ai4curation/eval-ont-agent-mondo/pull/604) | [attempt](attempts/pr604.md) |
| 10 | claude-sonnet-4.5 | claude | 0.243 | 0.286 | 0.212 | `175d21f` | [#547](https://github.com/ai4curation/eval-ont-agent-mondo/pull/547) | [attempt](attempts/pr547.md) |
