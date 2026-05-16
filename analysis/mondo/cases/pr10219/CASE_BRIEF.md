---
ontology: mondo
repo: monarch-initiative/mondo
issue_number: 9859
pr_number: 10219
issue_title: primary hypophysitis synonyms
pr_author: MeeSiing
pr_merged_at: '2026-05-04'
task_type: reclassification
difficulty: hard
scoping: tightly_scoped
scope: multi_term
review_outcome: changes_requested
num_agent_attempts: 10
generated_at: '2026-05-15'
scoping_notes: All changes are within the hypophysitis branch of the ontology, restructuring
  subtypes.
domain_area: rare-disease
best_f1: 0.259
best_model: claude-sonnet-4.5
---

# PR #10219 — primary hypophysitis synonyms

**mondo** | [monarch-initiative/mondo](https://github.com/monarch-initiative/mondo) | [Issue #9859](https://github.com/monarch-initiative/mondo/issues/9859) | [PR #10219](https://github.com/monarch-initiative/mondo/pull/10219) | @MeeSiing | merged 2026-05-04

`reclassification` `hard` `tightly_scoped` `changes_requested`

## Context

A user request was filed to update synonyms for primary hypophysitis. However, the resolution required a broader restructuring of the hypophysitis branch. The existing classification conflated primary vs secondary hypophysitis with histological subtypes (lymphocytic, granulomatous, etc.), making the hierarchy confusing.

The issue required domain expertise to determine that histological and anatomical subtypes should be classified as children of hypophysitis rather than maintaining the primary/secondary distinction, which is clinically less useful for classification purposes.

## Changes Made

The PR relabeled MONDO:0019835 to "lymphocytic hypophysitis" and restructured all histological and anatomical subtypes as child terms under the main hypophysitis term. With 6 commits, 45 additions and 18 deletions, this involved modifying multiple term stanzas to correct parent-child relationships and update labels.

## Resolution

This is a hard case because it requires understanding the clinical distinction between primary/secondary hypophysitis and histological subtypes, then making a judgment call about how best to restructure the hierarchy. An agent would need domain knowledge about hypophysitis classification and the ability to reorganize multiple related terms consistently while preserving cross-references.

## Human Diff

```diff
diff --git a/src/ontology/mondo-edit.obo b/src/ontology/mondo-edit.obo
index 027d104cae..c9dd4a3954 100644
--- a/src/ontology/mondo-edit.obo
+++ b/src/ontology/mondo-edit.obo
@@ -408807,6 +408807,7 @@ property_value: curated_content_resource "https://www.malacards.org/card/aapoaii
 [Term]
 id: MONDO:0016534
 name: infundibulo-neurohypophysitis
+def: "A hypophysitis characterized by an inflammation of the posterior pituitary and the stalk. The major clinical manifestation is diabetes insipidus with polyuria and polydipsia. Less frequent symptoms are headaches, adrenal insufficiency, hyperprolactinemia and hypogonadism." [https://orcid.org/0000-0002-7638-4659, Orphanet:238305]
 subset: gard_rare {source="GARD:0020632", source="MONDO:GARD"}
 subset: nord_rare {source="MONDO:NORD"}
 subset: ordo_disorder {source="Orphanet:238305"}
@@ -408818,8 +408819,9 @@ xref: ICD10CM:E23.6 {source="Orphanet:238305"}
 xref: MEDGEN:1683829 {source="MONDO:equivalentTo", source="MONDO:MEDGEN"}
 xref: Orphanet:238305 {source="MONDO:equivalentTo"}
 xref: UMLS:C5190834 {source="MONDO:equivalentTo", source="MONDO:MEDGEN", source="MEDGEN:1683829"}
-is_a: MONDO:0019835 {source="Orphanet:238305"} ! primary hypophysitis
+is_a: MONDO:0021156 {source="Orphanet:238305"} ! hypophysitis
 property_value: curated_content_resource "https://www.malacards.org/card/infundibulo_neurohypophysitis" xsd:anyURI {source="MONDO:MalaCards"}
+property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9859" xsd:anyURI
 
 [Term]
 id: MONDO:0016535
@@ -484699,16 +484701,13 @@ consider: MONDO:0015127
 
 [Term]
 id: MONDO:0019835
-name: primary hypophysitis
-def: "Immune-mediated inflammation of the pituitary gland often associated with other autoimmune diseases (e.g., hashimoto disease; graves disease; and addison disease)." [MESH:D000069281]
-subset: disease_grouping
+name: lymphocytic hypophysitis
+def: "An autoimmune condition affecting the pituitary gland, characterized by lymphocytic infiltration, commonly presenting with pituitary hormone deficiencies." [https://orcid.org/0000-0002-7638-4659, NCIT:C132055]
 subset: gard_rare {source="GARD:0019281", source="MONDO:GARD"}
 subset: ncit {source="NCIT:C132055"}
-subset: ordo_group_of_disorders {source="Orphanet:95506"}
-subset: orphanet {source="Orphanet:95506"}
 subset: rare
-synonym: "autoimmune hypophysitis" EXACT [NCIT:C132055, Orphanet:95506]
-synonym: "lymphocytic hypophysitis" EXACT [NCIT:C132055]
+synonym: "autoimmune hypophysitis" EXACT [NCIT:C132055]
+synonym: "primary hypophysitis" RELATED [PMID:34528683]
 xref: GARD:0019281 {source="MONDO:GARD"}
 xref: ICD10CM:E23.6 {source="Orphanet:95506"}
 xref: ICD9:253.8 {source="MONDO:relatedTo", source="MONDO:i2s"}
@@ -484716,14 +484715,14 @@ xref: ICD9:279.49 {source="MONDO:relatedTo", source="MONDO:i2s"}
 xref: MEDGEN:575013 {source="MONDO:equivalentTo", source="MONDO:MEDGEN"}
 xref: MESH:D000069281 {source="MONDO:equivalentTo"}
 xref: NCIT:C132055 {source="MONDO:equivalentTo"}
-xref: Orphanet:95506 {source="MONDO:equivalentTo"}
+xref: Orphanet:95506 {source="MONDO:mondoIsNarrowerThanSource"}
 xref: SCTID:237706000 {source="MONDO:equivalentTo"}
 xref: UMLS:C0342410 {source="MEDGEN:575013", source="MONDO:equivalentTo", source="MONDO:MEDGEN"}
 is_a: MONDO:0000569 {source="MONDO:Entailed"} ! autoimmune disorder of endocrine system
-is_a: MONDO:0019832 {source="Orphanet:95506"} ! acquired pituitary hormone deficiency
 is_a: MONDO:0021156 {source="MESH:D000069281", source="MONDO:Redundant"} ! hypophysitis
 relationship: disease_has_inflammation_site UBERON:0000007 ! pituitary gland
 property_value: curated_content_resource "https://www.malacards.org/card/primary_hypophysitis" xsd:anyURI {source="MONDO:MalaCards"}
+property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9859" xsd:anyURI
 
 [Term]
 id: MONDO:0019836
@@ -484766,7 +484765,7 @@ is_obsolete: true
 [Term]
 id: MONDO:0019838
 name: adenohypophysitis
-def: "An autoimmune disease of the pituitary gland which can present with varying degrees of pituitary hormonal impairment and/or with symptoms related to pituitary enlargement. It predominantly affects young women in pregnancy or the peripartum period." [PMID:21592417]
+def: "A rare, acquired pituitary hormone deficiency characterized by an inflammation of anterior pituitary with varying degrees of pituitary hormonal impairment and/or with symptoms related to pituitary enlargement. Clinical presentation is variable and includes headaches, visual disturbances, symptoms of adrenal insufficiency, hyperprolactinemia, hypothyroidism and hypogonadism. It most commonly affects young women during pregnancy or postpartum period." [https://orcid.org/0000-0002-7638-4659, Orphanet:95512, PMID:21592417]
 subset: gard_rare {source="GARD:0019284", source="MONDO:GARD"}
 subset: nord_rare {source="MONDO:NORD"}
 subset: ordo_disorder {source="Orphanet:95512"}
@@ -484775,21 +484774,21 @@ subset: orphanet_rare {source="Orphanet:95512"}
 subset: rare
 synonym: "adenohypophysis inflammation" EXACT [MONDO:patterns/inflammatory_disease_by_site]
 synonym: "anterior pituitary hypophysitis" EXACT [Orphanet:95512]
-synonym: "inflammation of adenohypophysis" EXACT []
-synonym: "lymphocytic adenohypophysitis" EXACT [PMID:21592417]
 xref: GARD:0019284 {source="MONDO:GARD"}
 xref: ICD10CM:E23.6 {source="Orphanet:95512"}
 xref: MEDGEN:1677203 {source="MONDO:equivalentTo", source="MONDO:MEDGEN"}
 xref: Orphanet:95512 {source="MONDO:equivalentTo"}
 xref: UMLS:C5190880 {source="MONDO:equivalentTo", source="MONDO:MEDGEN", source="MEDGEN:1677203"}
-is_a: MONDO:0019835 {source="Orphanet:95512"} ! primary hypophysitis
+is_a: MONDO:0021156 {source="Orphanet:95512"} ! hypophysitis
 intersection_of: MONDO:0000001 ! disease
 intersection_of: disease_has_inflammation_site UBERON:0002196 ! adenohypophysis
 property_value: curated_content_resource "https://www.malacards.org/card/adenohypophysitis" xsd:anyURI {source="MONDO:MalaCards"}
+property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9859" xsd:anyURI
 
 [Term]
 id: MONDO:0019839
 name: panhypophysitis
+def: "A hypophysitis characterized by an inflammation of the entire pituitary gland. Common clinical presentation is diabetes insipidus with polyuria and polydipsia and partial or panhypopituitarism. Other symptoms may include headaches, nausea/vomiting, visual disturbances and fatigue." [https://orcid.org/0000-0002-7638-4659, Orphanet:95513]
 subset: gard_rare {source="GARD:0019285", source="MONDO:GARD"}
 subset: nord_rare {source="MONDO:NORD"}
 subset: ordo_disorder {source="Orphanet:95513"}
@@ -484802,8 +484801,9 @@ xref: ICD10CM:E23.6 {source="Orphanet:95513"}
 xref: MEDGEN:1674527 {source="MONDO:equivalentTo", source="MONDO:MEDGEN"}
 xref: Orphanet:95513 {source="MONDO:equivalentTo"}
 xref: UMLS:C5190786 {source="MEDGEN:1674527", source="MONDO:equivalentTo", source="MONDO:MEDGEN"}
-is_a: MONDO:0019835 {source="Orphanet:95513"} ! primary hypophysitis
+is_a: MONDO:0021156 {source="Orphanet:95513"} ! hypophysitis
 property_value: curated_content_resource "https://www.malacards.org/card/panhypophysitis" xsd:anyURI {source="MONDO:MalaCards"}
+property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9859" xsd:anyURI
 
 [Term]
 id: MONDO:0019840
@@ -508215,13 +508215,10 @@ intersection_of: has_characteristic HP:0001417 ! X-linked inheritance
 id: MONDO:0021156
 name: hypophysitis
 def: "Inflammation of the pituitary gland." [MESH:D000072659]
-comment: Editor note: TODO - add all subtypes; Granulomatous hypophysitis is one of five types of inflammatory hypophysitis, which are (lymphocytic, granulomatous, xanthomatous, xanthogranulomatous, and necrotizing) https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5494403/
 subset: ncit {source="NCIT:C12399"}
-synonym: "gland, pituitary" EXACT []
 synonym: "hypophysis" EXACT [NCIT:C12399]
 synonym: "hypophysis cerebri" EXACT [NCIT:C12399]
 synonym: "hypophysitides" EXACT [MESH:D000072659]
-synonym: "inflammation of pituitary gland" EXACT []
 synonym: "nervous system, pituitary" EXACT [NCIT:C12399]
 synonym: "pituitary" EXACT [NCIT:C12399]
 synonym: "pituitary gland" EXACT [NCIT:C12399]
@@ -508236,6 +508233,7 @@ is_a: MONDO:0003381 {source="MESH:D000072659", source="MONDO:Redundant"} ! pitui
 is_a: MONDO:0021166 {source="MONDO:Redundant"} ! inflammatory disease
 intersection_of: MONDO:0000001 ! disease
 intersection_of: disease_has_inflammation_site UBERON:0000007 ! pituitary gland
+property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9859" xsd:anyURI
 
 [Term]
 id: MONDO:0021157
@@ -607281,6 +607279,7 @@ property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/
 [Term]
 id: MONDO:0957423
 name: immunotherapy induced hypophysitis
+def: "A rare acquired pituitary hormone deficieny characterized by inflammation of the pituitary gland secondary to immunotherapy for cancers treatments (such as monoclonal antibodies against cytotoxic T lymphocytes antigen, programmed cell death protein-1, and programmed cell death ligand molecules). Major clinical features include headache, fatigue, adrenal insufficiency and hypothyroidism. Patients may also have nausea and vomiting associated to the headache as well as dizziness and hot flashes. Enlargement of the pituitary gland is present in the brain imaging." [Orphanet:641350]
 subset: gard_rare {source="GARD:0026823", source="MONDO:GARD"}
 subset: ordo_disorder {source="Orphanet:641350"}
 subset: orphanet {source="Orphanet:641350"}
@@ -607292,6 +607291,7 @@ xref: Orphanet:641350 {source="MONDO:equivalentTo"}
 xref: UMLS:C5816794 {source="MONDO:equivalentTo", source="MONDO:MEDGEN", source="MEDGEN:1843401"}
 is_a: MONDO:0021156 {source="https://orcid.org/0000-0001-5208-3432"} ! hypophysitis
 property_value: curated_content_resource "https://www.malacards.org/card/immunotherapy_induced_hypophysitis" xsd:anyURI {source="MONDO:MalaCards"}
+property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9859" xsd:anyURI
 
 [Term]
 id: MONDO:0957426
@@ -659109,6 +659109,33 @@ relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/
 property_value: http://purl.org/dc/terms/creator https://orcid.org/0000-0002-7638-4659
 property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9956" xsd:anyURI
 
+[Term]
+id: MONDO:1060217
+name: xanthomatous hypophysitis
+def: "A rare hypophysitis characterized histologically by mixed inflammatory cell infiltrates consisting of foamy histiocytes, plasma cells, and small round mature lymphocytes infiltrating the anterior pituitary gland. The tissue often contains cystic-like areas of liquefaction filled with lipid-laden macrophages along with lymphocytes and plasma cells." [https://orcid.org/0000-0002-7638-4659, PMID:20671950, PMID:34528683]
+xref: MEDGEN:1800063 {source="MONDO:equivalentTo", source="MONDO:MEDGEN"}
+xref: SCTID:1186907003 {source="MONDO:equivalentTo"}
+xref: UMLS:C5568640 {source="MONDO:equivalentTo", source="MONDO:MEDGEN", source="MEDGEN:1800063"}
+is_a: MONDO:0021156 {source="PMID:20671950", source="PMID:34528683"} ! hypophysitis
+property_value: http://purl.org/dc/terms/creator https://orcid.org/0000-0002-7638-4659
+property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9859" xsd:anyURI
+
+[Term]
+id: MONDO:1060218
+name: xanthogranulomatous hypophysitis
+def: "A hypophysitis exhibiting histologic features of both xanthomatous and granulomatous hypophysitis, characterized by cholesterol clefts, haemosiderin deposits, multinucleated giant cells, macrophage accumulation and fibrous proliferation." [https://orcid.org/0000-0002-7638-4659, PMID:25759759]
+is_a: MONDO:0021156 {source="PMID:25759759"} ! hypophysitis
+property_value: http://purl.org/dc/terms/creator https://orcid.org/0000-0002-7638-4659
+property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9859" xsd:anyURI
+
+[Term]
+id: MONDO:1060219
+name: necrotizing hypophysitis
+def: "A rare hypophysitis defined histologically by extensive necrosis of pituitary tissue surrounded by lymphocytes, plasma cells, and eosinophils." [https://orcid.org/0000-0002-7638-4659, PMID:34528683]
+is_a: MONDO:0021156 {source="PMID:34528683"} ! hypophysitis
+property_value: http://purl.org/dc/terms/creator https://orcid.org/0000-0002-7638-4659
+property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9859" xsd:anyURI
+
 [Term]
 id: MONDO:1060220
 name: split cord malformation type I

```

## Agent Attempts (10)

| # | Model | Runtime | F1 | P | R | Eval PR | Detail |
|---|-------|---------|-----|-----|-----|---------|--------|
| 1 | claude-sonnet-4.5 | claude | 0.259 | 0.171 | 0.538 | [#459](https://github.com/ai4curation/eval-ont-agent-mondo/pull/459) | [attempt](attempts/pr459.md) |
| 2 | kimi-k2.6 | opencode | 0.235 | 0.146 | 0.600 | [#280](https://github.com/ai4curation/eval-ont-agent-mondo/pull/280) | [attempt](attempts/pr280.md) |
| 3 | gpt-5.5 | codex | 0.233 | 0.171 | 0.368 | [#45](https://github.com/ai4curation/eval-ont-agent-mondo/pull/45) | [attempt](attempts/pr45.md) |
| 4 | claude-opus-4.7 | claude | 0.128 | 0.073 | 0.500 | [#550](https://github.com/ai4curation/eval-ont-agent-mondo/pull/550) | [attempt](attempts/pr550.md) |
| 5 | claude-opus-4.7 | claude | 0.128 | 0.073 | 0.500 | [#401](https://github.com/ai4curation/eval-ont-agent-mondo/pull/401) | [attempt](attempts/pr401.md) |
| 6 | gpt-5.4 | codex | 0.093 | 0.049 | 1.000 | [#166](https://github.com/ai4curation/eval-ont-agent-mondo/pull/166) | [attempt](attempts/pr166.md) |
| 7 | gpt-5.5 | opencode | 0.091 | 0.049 | 0.667 | [#85](https://github.com/ai4curation/eval-ont-agent-mondo/pull/85) | [attempt](attempts/pr85.md) |
| 8 | gpt-5.5 | opencode | 0.091 | 0.049 | 0.667 | [#65](https://github.com/ai4curation/eval-ont-agent-mondo/pull/65) | [attempt](attempts/pr65.md) |
| 9 | claude-haiku-4.5 | claude | 0.048 | 0.024 | 1.000 | [#320](https://github.com/ai4curation/eval-ont-agent-mondo/pull/320) | [attempt](attempts/pr320.md) |
| 10 | claude-haiku-4.5 | claude | 0.048 | 0.024 | 1.000 | [#190](https://github.com/ai4curation/eval-ont-agent-mondo/pull/190) | [attempt](attempts/pr190.md) |
