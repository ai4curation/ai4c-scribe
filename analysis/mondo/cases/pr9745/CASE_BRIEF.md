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
num_agent_attempts: 13
generated_at: '2026-05-17'
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

## Curation Note (data quality)

Flagged `case_quality: poor` after reviewing all 11 attempts (claude-opus-4.7, 2026-05-15).

Two factors make the metadiff F1 a poor proxy for quality on this case:

1. **Placeholder-vs-canonical MONDO ID artifact.** The merged gold PR #9745 uses canonical IDs `MONDO:1010180` (cardiogenetic rhythm disorder) and `MONDO:1010181` (SCN5A-related cardiac rhythm disorder). Every agent used the eval base's auto-allocated placeholder range `MONDO:7770003`/`MONDO:7770004`. Since most of both diffs are `is_a:` lines that reference these IDs, OBO metadiff scores nearly every correct reparenting as a miss. F1 is structurally compressed (best 0.615, most ~0.31, lowest 0.216) even where agents attached the right child to the conceptually right parent.

2. **Out-of-scope gold cleanup.** The gold also reclassified `atrioventricular dissociation` (MONDO:0000465) from `MONDO:0003847` (hereditary disease) to `MONDO:0100042` (cardiac conduction defect) and added `excluded_subClassOf` plus two `excluded_from_qc_check` relationships. The issue (#9707) never requested this; it is incidental curator cleanup that no well-scoped agent would reproduce, accounting for the gold's single deletion and several additions and further depressing recall.

This issue was resolved by a single PR (#9745); no companion PRs exist. Recommended handling: down-weight or exclude this case from line-level F1 aggregation and judge attempts against the issue text and the gold's term-creation/reparenting substance. On that basis the best attempts (#261 kimi-k2.6/opencode F1=0.615; #407 claude-opus-4.7/claude F1=0.311; #89/#68 gpt-5.5/opencode F1=0.311) are substantively strong partial successes, far better than their raw F1 suggests.

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

## Agent Attempts (13)

| # | Model | Runtime | F1 | P | R | Blob | Eval PR | Detail |
|---|-------|---------|-----|-----|-----|------|---------|--------|
| 1 | kimi-k2.6 | opencode | 0.615 | 0.500 | 0.800 | `5b9c869` | [#261](https://github.com/ai4curation/eval-ont-agent-mondo/pull/261) | [attempt](attempts/pr261.md) |
| 2 | claude-sonnet-4.5 | copilot | 0.462 | 0.375 | 0.600 | `d65d819` | [#525](https://github.com/ai4curation/eval-ont-agent-mondo/pull/525) | [attempt](attempts/pr525.md) |
| 3 | claude-sonnet-4.5 | copilot | 0.462 | 0.375 | 0.600 | `d65d819` | [#490](https://github.com/ai4curation/eval-ont-agent-mondo/pull/490) | [attempt](attempts/pr490.md) |
| 4 | claude-sonnet-4.5 | claude | 0.432 | 0.333 | 0.615 | `e3d9937` | [#445](https://github.com/ai4curation/eval-ont-agent-mondo/pull/445) | [attempt](attempts/pr445.md) |
| 5 | claude-opus-4.7 | claude | 0.311 | 0.292 | 0.333 | `f773034` | [#407](https://github.com/ai4curation/eval-ont-agent-mondo/pull/407) | [attempt](attempts/pr407.md) |
| 6 | gpt-5.5 | opencode | 0.311 | 0.292 | 0.333 | `9617ce8` | [#89](https://github.com/ai4curation/eval-ont-agent-mondo/pull/89) | [attempt](attempts/pr89.md) |
| 7 | gpt-5.5 | opencode | 0.311 | 0.292 | 0.333 | `9617ce8` | [#68](https://github.com/ai4curation/eval-ont-agent-mondo/pull/68) | [attempt](attempts/pr68.md) |
| 8 | gpt-5.5 | codex | 0.308 | 0.250 | 0.400 | `dab7fd5` | [#48](https://github.com/ai4curation/eval-ont-agent-mondo/pull/48) | [attempt](attempts/pr48.md) |
| 9 | gpt-5.4 | codex | 0.270 | 0.208 | 0.385 | `895fb4a` | [#160](https://github.com/ai4curation/eval-ont-agent-mondo/pull/160) | [attempt](attempts/pr160.md) |
| 10 | gpt-5.4 | opencode | 0.256 | 0.208 | 0.333 | `a739698` | [#767](https://github.com/ai4curation/eval-ont-agent-mondo/pull/767) | [attempt](attempts/pr767.md) |
| 11 | gpt-5.4 | opencode | 0.256 | 0.208 | 0.333 | `a739698` | [#713](https://github.com/ai4curation/eval-ont-agent-mondo/pull/713) | [attempt](attempts/pr713.md) |
| 12 | claude-haiku-4.5 | claude | 0.216 | 0.167 | 0.308 | `391e147` | [#427](https://github.com/ai4curation/eval-ont-agent-mondo/pull/427) | [attempt](attempts/pr427.md) |
| 13 | claude-haiku-4.5 | claude | 0.216 | 0.167 | 0.308 | `391e147` | [#300](https://github.com/ai4curation/eval-ont-agent-mondo/pull/300) | [attempt](attempts/pr300.md) |
