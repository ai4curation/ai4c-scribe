---
ontology: mondo
repo: monarch-initiative/mondo
issue_number: 5726
pr_number: 10155
issue_title: Add non-human animal diseases from VeNom
pr_author: katiermullen
pr_merged_at: '2026-04-16'
task_type: new_term
difficulty: hard
scoping: loosely_scoped
scope: structural_refactor
review_outcome: approved_first_time
num_agent_attempts: 6
generated_at: '2026-05-15'
scoping_notes: Bulk addition of hundreds of non-human animal disease terms from the
  VeNom coding system.
domain_area: veterinary-disease
best_f1: 1.0
best_model: kimi-k2.6
---

# PR #10155 — Add non-human animal diseases from VeNom

**mondo** | [monarch-initiative/mondo](https://github.com/monarch-initiative/mondo) | [Issue #5726](https://github.com/monarch-initiative/mondo/issues/5726) | [PR #10155](https://github.com/monarch-initiative/mondo/pull/10155) | @katiermullen | merged 2026-04-16

`new_term` `hard` `loosely_scoped` `approved_first_time`

## Context

Issue #5726 was a long-running initiative (opened December 2022) to incorporate non-human animal diseases from the VeNom (Veterinary Nomenclature) coding system into Mondo. VeNom contains over 6,000 diagnosis entries spanning large animals, small animals, farm animals, equines, and exotics. This PR represents one tranche of that effort, adding curated veterinary disease terms with appropriate VeNom cross-references and classifications.

## Changes Made

The PR added 9,006 lines to `src/ontology/mondo-edit.obo` across 3 commits, with zero deletions. Each new term stanza includes a label, definition, VeNom cross-reference, and classification under the non-human animal disease hierarchy. The scale of this change required careful curation to map VeNom diagnoses to appropriate Mondo parent classes and to exclude entries that are phenotypes rather than diseases.

## Resolution

Complex difficulty due to the sheer volume of terms and the need for systematic curation decisions. Each VeNom entry required evaluation of whether it represents a true disease (vs. a phenotype or procedure), selection of an appropriate parent class, and construction of valid cross-references. This task is not well-suited to a single agent pass and instead required iterative human curation across multiple PRs addressing the same long-running issue.

## Human Diff

```diff
diff --git a/src/ontology/mondo-edit.obo b/src/ontology/mondo-edit.obo
index 27fc3d5620..569314b337 100644
--- a/src/ontology/mondo-edit.obo
+++ b/src/ontology/mondo-edit.obo
@@ -590480,6 +590480,7 @@ xref: VeNom:80727 {source="MONDO:equivalentTo"}
 is_a: MONDO:0700049 {source="https://orcid.org/0000-0001-5208-3432"} ! infectious disease, non-human animal
 intersection_of: MONDO:0005583 ! non-human animal disease
 intersection_of: MONDO:0700097 MONDO:0005939 ! cross-species analog Reoviridae infectious disease
+relationship: disease_has_infectious_agent NCBITaxon:10880 {source="https://orcid.org/0000-0002-5002-8648"}
 property_value: http://purl.org/dc/terms/creator https://orcid.org/0000-0002-4142-7153
 property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/5726" xsd:anyURI
 
@@ -591255,6 +591256,7 @@ is_a: MONDO:0700139 {source="NCIT:C132275"} ! canine neoplasm
 intersection_of: MONDO:0005583 ! non-human animal disease
 intersection_of: in_taxon NCBITaxon:9615 ! Canis lupus familiaris
 intersection_of: MONDO:0700097 MONDO:0024622 ! cross-species analog thyroid gland adenocarcinoma
+relationship: excluded_from_qc_check http://purl.obolibrary.org/obo/mondo/sparql/qc/general/qc-single-child.sparql
 property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/5252" xsd:anyURI
 
 [Term]
@@ -591865,6 +591867,7 @@ xref: VeNom:472 {source="MONDO:equivalentTo"}
 is_a: MONDO:0700049 {source="https://orcid.org/0000-0001-5208-3432"} ! infectious disease, non-human animal
 intersection_of: MONDO:0005583 ! non-human animal disease
 intersection_of: MONDO:0700097 MONDO:0005687 ! cross-species analog Caliciviridae infectious disease
+relationship: disease_has_infectious_agent NCBITaxon:11974 {source="https://orcid.org/0000-0002-5002-8648"} ! Caliciviridae
 property_value: http://purl.org/dc/terms/creator https://orcid.org/0000-0002-4142-7153
 property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/5726" xsd:anyURI
 
@@ -591904,6 +591907,7 @@ xref: VeNom:80500 {source="MONDO:equivalentTo"}
 is_a: MONDO:0700049 ! infectious disease, non-human animal
 intersection_of: MONDO:0005583 ! non-human animal disease
 intersection_of: MONDO:0700097 MONDO:0018076 ! cross-species analog tuberculosis
+relationship: excluded_from_qc_check http://purl.obolibrary.org/obo/mondo/sparql/qc/general/qc-single-child.sparql
 property_value: http://purl.org/dc/terms/creator https://orcid.org/0000-0002-4142-7153
 property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/5726" xsd:anyURI
 
@@ -591934,6 +591938,7 @@ xref: VeNom:982 {source="MONDO:equivalentTo"}
 is_a: MONDO:0700049 {source="https://orcid.org/0000-0001-5208-3432"} ! infectious disease, non-human animal
 intersection_of: MONDO:0005583 ! non-human animal disease
 intersection_of: MONDO:0700097 MONDO:0005794 ! cross-species analog Herpesviridae infectious disease
+relationship: disease_has_infectious_agent NCBITaxon:3044472 {source="https://orcid.org/0000-0002-5002-8648"} ! Orthoherpesviridae
 property_value: http://purl.org/dc/terms/creator https://orcid.org/0000-0002-4142-7153
 property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/5726" xsd:anyURI
 
@@ -617764,6 +617769,7 @@ xref: OMIA:000536 {source="MONDO:equivalentTo"}
 is_a: MONDO:0005583 {source="OMIA:000536"} ! non-human animal disease
 intersection_of: MONDO:0005583 {source="OMIA:000536"} ! non-human animal disease
 intersection_of: MONDO:0700097 MONDO:0018612 {source="OMIA:000536"} ! cross-species analog congenital hypothyroidism
+relationship: excluded_from_qc_check http://purl.obolibrary.org/obo/mondo/sparql/qc/general/qc-single-child.sparql
 
 [Term]
 id: MONDO:1010058
@@ -617904,6 +617910,7 @@ xref: OMIA:000185 {source="MONDO:equivalentTo"}
 is_a: MONDO:0005583 {source="OMIA:000185"} ! non-human animal disease
 intersection_of: MONDO:0005583 {source="OMIA:000185"} ! non-human animal disease
 intersection_of: MONDO:0700097 MONDO:0008963 {source="OMIA:000185"} ! cross-species analog Chediak-Higashi syndrome
+relationship: excluded_from_qc_check http://purl.obolibrary.org/obo/mondo/sparql/qc/general/qc-single-child.sparql
 
 [Term]
 id: MONDO:1010071
@@ -619451,6 +619458,19 @@ relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/
 property_value: http://purl.org/dc/terms/creator https://orcid.org/0000-0002-5002-8648
 property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9877" xsd:anyURI
 
+[Term]
+id: MONDO:1010206
+name: meningeal neoplasm, non-human animal
+def: "Meningeal neoplasm that occurs in non-human animals." [MONDO:patterns/nonhuman_disease]
+subset: venom_exotics {source="VeNom:1437"}
+subset: venom_small_animal {source="VeNom:1437"}
+xref: VeNom:1437 {source="MONDO:equivalentTo"}
+is_a: MONDO:0005583 ! non-human animal disease
+intersection_of: MONDO:0005583 ! non-human animal disease
+intersection_of: MONDO:0700097 MONDO:0016743 ! cross-species analog tumor of meninges
+property_value: http://purl.org/dc/terms/creator https://orcid.org/0000-0002-5002-8648
+property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/5726" xsd:anyURI
+
 [Term]
 id: MONDO:1010208
 name: myofibrillar myopathy, non-human animal
@@ -619605,6 +619625,7 @@ xref: OMIA:002369 {source="MONDO:equivalentTo"}
 is_a: MONDO:0005583 {source="OMIA:002369"} ! non-human animal disease
 intersection_of: MONDO:0005583 {source="https://orcid.org/0000-0002-5002-8648"} ! non-human animal disease
 intersection_of: MONDO:0700097 MONDO:0009761 {source="https://orcid.org/0000-0002-5002-8648"} ! cross-species analog cystic hygroma
+relationship: excluded_from_qc_check http://purl.obolibrary.org/obo/mondo/sparql/qc/general/qc-single-child.sparql
 
 [Term]
 id: MONDO:1010226
@@ -619853,6 +619874,7 @@ xref: OMIA:001867 {source="MONDO:equivalentTo"}
 is_a: MONDO:0005583 {source="OMIA:001867"} ! non-human animal disease
 intersection_of: MONDO:0005583 {source="OMIA:001867"} ! non-human animal disease
 intersection_of: MONDO:0700097 MONDO:0009760 {source="OMIA:001867"} ! cross-species analog Norman-Roberts syndrome
+relationship: excluded_from_qc_check http://purl.obolibrary.org/obo/mondo/sparql/qc/general/qc-single-child.sparql
 
 [Term]
 id: MONDO:1010249
@@ -619945,6 +619967,7 @@ xref: VeNom:1797 {source="MONDO:equivalentTo"}
 is_a: MONDO:0005583 {source="OMIA:000807"} ! non-human animal disease
 intersection_of: MONDO:0005583 {source="OMIA:000807"} ! non-human animal disease
 intersection_of: MONDO:0700097 MONDO:0020642 {source="OMIA:000807"} ! cross-species analog polycystic kidney disease
+relationship: excluded_from_qc_check http://purl.obolibrary.org/obo/mondo/sparql/qc/general/qc-single-child.sparql
 property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/5726" xsd:anyURI
 
 [Term]
@@ -620110,6 +620133,7 @@ xref: OMIA:001535 {source="MONDO:equivalentTo"}
 is_a: MONDO:0005583 {source="OMIA:001535"} ! non-human animal disease
 intersection_of: MONDO:0005583 {source="https://orcid.org/0000-0002-5002-8648"} ! non-human animal disease
 intersection_of: MONDO:0700097 MONDO:8000015 {source="https://orcid.org/0000-0002-5002-8648"} ! cross-species analog 46,XY sex reversal 11
+relationship: excluded_from_qc_check http://purl.obolibrary.org/obo/mondo/sparql/qc/general/qc-single-child.sparql
 
 [Term]
 id: MONDO:1010282
@@ -620618,6 +620642,7 @@ xref: OMIA:001914 {source="MONDO:equivalentTo"}
 is_a: MONDO:0005583 {source="OMIA:001914"} ! non-human animal disease
 intersection_of: MONDO:0005583 {source="https://orcid.org/0000-0002-5002-8648"} ! non-human animal disease
 intersection_of: MONDO:0700097 MONDO:0011414 {source="https://orcid.org/0000-0002-5002-8648"} ! cross-species analog Peters anomaly
+relationship: excluded_from_qc_check http://purl.obolibrary.org/obo/mondo/sparql/qc/general/qc-single-child.sparql
 
 [Term]
 id: MONDO:1010350
@@ -631786,6 +631811,7 @@ xref: OMIA:000041 {source="MONDO:equivalentTo"}
 is_a: MONDO:0005583 {source="OMIA:000041"} ! non-human animal disease
 intersection_of: MONDO:0005583 ! non-human animal disease
 intersection_of: MONDO:0700097 MONDO:0015253 ! cross-species analog Diamond-Blackfan anemia
+relationship: excluded_from_qc_check http://purl.obolibrary.org/obo/mondo/sparql/qc/general/qc-single-child.sparql
 property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/7225" xsd:anyURI
 
 [Term]
@@ -631849,10 +631875,17 @@ property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/
 id: MONDO:1011411
 name: Von Willebrand disease, non-human animal
 def: "Von Willebrand disease that occurs in non-human animals." [MONDO:patterns/nonhuman_disease]
+subset: venom_equine {source="VeNom:2090"}
+subset: venom_exotics {source="VeNom:2090"}
+subset: venom_farm_animal {source="VeNom:2090"}
+subset: venom_large_animal {source="VeNom:2090"}
+subset: venom_small_animal {source="VeNom:2090"}
 xref: OMIA:001056 {source="MONDO:equivalentTo"}
+xref: VeNom:2090 {source="MONDO:equivalentTo"}
 is_a: MONDO:0005583 {source="OMIA:001056"} ! non-human animal disease
 intersection_of: MONDO:0005583 ! non-human animal disease
 intersection_of: MONDO:0700097 MONDO:0024574 ! cross-species analog von Willebrand disease (hereditary or acquired)
+property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/5726" xsd:anyURI
 property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/7225" xsd:anyURI
 
 [Term]
@@ -631873,6 +631906,7 @@ xref: OMIA:002372 {source="MONDO:equivalentTo"}
 is_a: MONDO:0005583 {source="OMIA:002372"} ! non-human animal disease
 intersection_of: MONDO:0005583 ! non-human animal disease
 intersection_of: MONDO:0700097 MONDO:0100244 ! cross-species analog paroxysmal nocturnal hemoglobinuria
+relationship: excluded_from_qc_check http://purl.obolibrary.org/obo/mondo/sparql/qc/general/qc-single-child.sparql
 property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/7225" xsd:anyURI
 
 [Term]
@@ -632314,11 +632348,15 @@ property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/
 id: MONDO:1011451
 name: idiopathic pulmonary fibrosis, non-human animal
 def: "Idiopathic pulmonary fibrosis that occurs in non-human animals." [MONDO:patterns/nonhuman_disease]
+subset: venom_exotics {source="VeNom:1769"}
+subset: venom_small_animal {source="VeNom:1769"}
 xref: OMIA:001417 {source="MONDO:equivalentTo"}
+xref: VeNom:1769 {source="MONDO:equivalentTo"}
 is_a: MONDO:0005583 {source="OMIA:001417"} ! non-human animal disease
 intersection_of: MONDO:0005583 ! non-human animal disease
 intersection_of: MONDO:0700097 MONDO:0800504 ! cross-species analog idiopathic pulmonary fibrosis
 relationship: excluded_from_qc_check http://purl.obolibrary.org/obo/mondo/sparql/qc/general/qc-single-child.sparql
+property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/5726" xsd:anyURI
 property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/7225" xsd:anyURI
 
 [Term]
@@ -632339,10 +632377,14 @@ property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/
 id: MONDO:1011453
 name: Legg-Calvé-Perthes disease, non-human animal
 def: "Legg-Calvé-Perthes disease that occurs in non-human animals." [MONDO:patterns/nonhuman_disease]
+subset: venom_exotics {source="VeNom:420"}
+subset: venom_small_animal {source="VeNom:420"}
 xref: OMIA:000586 {source="MONDO:equivalentTo"}
+xref: VeNom:420 {source="MONDO:equivalentTo"}
 is_a: MONDO:0005583 {source="OMIA:000586"} ! non-human animal disease
 intersection_of: MONDO:0005583 ! non-human animal disease
 intersection_of: MONDO:0700097 MONDO:0007885 ! cross-species analog Legg-Calve-Perthes disease
+property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/5726" xsd:anyURI
 property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/7225" xsd:anyURI
 
 [Term]
@@ -635292,9 +635334,12 @@ property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/
 [Term]
 id: MONDO:1011724
 name: immunodeficiency disease, non-human animal
+subset: venom_equine {source="VeNom:81076"}
 xref: OMIA:000550 {source="MONDO:equivalentTo"}
+xref: VeNom:81076 {source="MONDO:equivalentTo"}
 is_a: MONDO:0005583 {source="OMIA:000550"} ! non-human animal disease
 is_a: MONDO:0700106 {source="OMIA:000550", source="https://orcid.org/0000-0002-5002-8648"} ! immune system disorder, non-human animal
+property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/5726" xsd:anyURI
 property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/7225" xsd:anyURI
 
 [Term]
@@ -646738,6 +646783,7 @@ def: "Amelogenesis imperfecta that occurs in non-human animals." [MONDO:patterns
 is_a: MONDO:0005583 {source="https://orcid.org/0000-0002-5002-8648"} ! non-human animal disease
... (8984 more lines truncated)
```

## Agent Attempts (6)

| # | Model | Runtime | F1 | P | R | Eval PR | Detail |
|---|-------|---------|-----|-----|-----|---------|--------|
| 1 | kimi-k2.6 | opencode | 1.000 | 1.000 | 1.000 | [#263](https://github.com/ai4curation/eval-ont-agent-mondo/pull/263) | [attempt](attempts/pr263.md) |
| 2 | gpt-5.5 | opencode | 1.000 | 1.000 | 1.000 | [#90](https://github.com/ai4curation/eval-ont-agent-mondo/pull/90) | [attempt](attempts/pr90.md) |
| 3 | gpt-5.5 | opencode | 1.000 | 1.000 | 1.000 | [#71](https://github.com/ai4curation/eval-ont-agent-mondo/pull/71) | [attempt](attempts/pr71.md) |
| 4 | gpt-5.5 | codex | 0.002 | 0.001 | 1.000 | [#153](https://github.com/ai4curation/eval-ont-agent-mondo/pull/153) | [attempt](attempts/pr153.md) |
| 5 | gpt-5.5 | codex | 0.002 | 0.001 | 1.000 | [#47](https://github.com/ai4curation/eval-ont-agent-mondo/pull/47) | [attempt](attempts/pr47.md) |
| 6 | gpt-5.4 | codex | 0.000 | 0.000 | 0.000 | [#158](https://github.com/ai4curation/eval-ont-agent-mondo/pull/158) | [attempt](attempts/pr158.md) |
