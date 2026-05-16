---
ontology: uberon
repo: obophenotype/uberon
issue_number: 3473
pr_number: 3494
issue_title: Not all epithelia with squamous cells are squamous epithelium
pr_author: dosumis
pr_merged_at: '2025-03-19'
task_type: axiom_repair
difficulty: hard
scoping: tightly_scoped
scope: multi_term
review_outcome: approved_first_time
num_agent_attempts: 9
generated_at: '2026-05-15'
domain_area: epithelial-tissue
best_f1: 0.19
best_model: claude-opus-4.7
---

# PR #3494 — Not all epithelia with squamous cells are squamous epithelium

**uberon** | [obophenotype/uberon](https://github.com/obophenotype/uberon) | [Issue #3473](https://github.com/obophenotype/uberon/issues/3473) | [PR #3494](https://github.com/obophenotype/uberon/pull/3494) | @dosumis | merged 2025-03-19

`axiom_repair` `hard` `tightly_scoped` `approved_first_time`

## Context

Issue #3473 identified that the definition of squamous epithelium in Uberon was too broad: not all epithelia containing squamous cells qualify as squamous epithelium. The distinction is histologically significant because transitional epithelium and stratified epithelia may contain squamous cells in their superficial layers without being classified as squamous epithelium proper.

## Changes Made

The PR modified 15 lines and removed 18 lines in uberon-edit.obo, refining the definition and logical axioms for squamous epithelium and related terms. The changes tightened the classification criteria so that the presence of squamous cells alone is insufficient for classification as squamous epithelium, requiring instead that the epithelium be predominantly composed of squamous cells or classified as such by standard histological criteria.

## Resolution

Hard difficulty. An agent would need deep histological knowledge to understand why the original definition was too permissive, distinguish between squamous epithelium proper and epithelia that merely contain squamous cells, and craft logical axioms that correctly capture this distinction without breaking existing classification hierarchies. The three commits over six weeks suggest careful deliberation.

## Human Diff

```diff
diff --git a/src/ontology/uberon-edit.obo b/src/ontology/uberon-edit.obo
index bdb0f1896e..41228e1e77 100644
--- a/src/ontology/uberon-edit.obo
+++ b/src/ontology/uberon-edit.obo
@@ -7522,7 +7522,7 @@ xref: Wikipedia:Simple_squamous_epithelium
 xref: XAO:0004010
 xref: ZFA:0001498
 intersection_of: UBERON:0000490 ! unilaminar epithelium
-intersection_of: has_part CL:0000076 ! squamous epithelial cell
+intersection_of: composed_primarily_of CL:0000076 ! squamous epithelial cell
 property_value: depiction "https://upload.wikimedia.org/wikipedia/commons/8/8f/Illu_epithelium.jpg" xsd:anyURI
 property_value: external_definition "Unilaminar epithelium that consists of a single layer of squamous cells.[CARO]" xsd:string {date_retrieved="2012-06-20", external_class="CARO:0000070", ontology="CARO", source="FMA:45565", source="http://orcid.org/0000-0001-9114-8737"}
 
@@ -12476,7 +12476,6 @@ xref: SCTID:192172004
 xref: TAO:0002247
 xref: VHOG:0000607
 xref: ZFA:0001615
-is_a: UBERON:0000490 {source="EHDAA2-abduced"} ! unilaminar epithelium
 intersection_of: UBERON:0002165 ! endocardium
 intersection_of: part_of UBERON:0002082 ! cardiac ventricle
 relationship: contributes_to_morphology_of UBERON:0002082 ! cardiac ventricle
@@ -36854,7 +36853,7 @@ intersection_of: UBERON:0000483 ! epithelium
 intersection_of: part_of UBERON:0002187 ! terminal bronchiole
 relationship: dc-contributor https://orcid.org/0000-0001-6677-8489 ! Aleix Puig-Barbé
 relationship: has_part CL:0000158 {source="FMA"} ! club cell
-relationship: has_part CL:1000271 ! lung ciliated cell
+relationship: has_part CL:1000271 ! lung multiciliated epithelial cell
 property_value: taxon_notes "A pseudostratified epithelium, containing basal cells, stem cells of the airway, submucosal glands and cartilage rings, is limited to the trachea and large lobar airways in the mouse (Morrisey and Hogan, 2010). This more complex epithelium extends to terminal bronchioles in the human[DOI:10.1242/dev.115469]" xsd:string
 
 [Term]
@@ -38480,7 +38479,6 @@ xref: SCTID:361828005
 xref: UMLS:C0039099 {source="ncithesaurus:Synovial_Membrane"}
 xref: VHOG:0001282
 xref: Wikipedia:Synovial_membrane
-is_a: UBERON:0000486 {source="EHDAA2"} ! multilaminar epithelium
 is_a: UBERON:0007616 {source="FMA"} ! layer of synovial tissue
 relationship: attaches_to UBERON:0001484 {source="GAID"} ! articular capsule
 relationship: has_part CL:0000214 ! synovial cell
@@ -39642,8 +39640,8 @@ intersection_of: part_of UBERON:0002186 ! bronchiole
 relationship: contributes_to_morphology_of UBERON:0002186 ! bronchiole
 relationship: dc-contributor https://orcid.org/0000-0001-6677-8489 ! Aleix Puig-Barbé
 relationship: has_part CL:0000158 ! club cell
-relationship: has_part CL:0002145 {source="FMA"} ! ciliated columnar cell of tracheobronchial tree
-relationship: has_part CL:1000271 ! lung ciliated cell
+relationship: has_part CL:0002145 {source="FMA"} ! multiciliated columnar cell of tracheobronchial tree
+relationship: has_part CL:1000271 ! lung multiciliated epithelial cell
 relationship: part_of UBERON:0005039 ! mucosa of bronchiole
 
 [Term]
@@ -47866,7 +47864,7 @@ intersection_of: UBERON:0000483 ! epithelium
 intersection_of: part_of UBERON:0002183 ! lobar bronchus
 relationship: dc-contributor https://orcid.org/0000-0001-6677-8489 ! Aleix Puig-Barbé
 relationship: has_part CL:0002329 ! basal epithelial cell of tracheobronchial tree
-relationship: has_part CL:0002332 ! ciliated cell of the bronchus
+relationship: has_part CL:0002332 ! multiciliated epithelial cell of the bronchus
 relationship: has_part CL:0017000 ! pulmonary ionocyte
 
 [Term]
@@ -47923,10 +47921,10 @@ relationship: dc-contributor https://orcid.org/0000-0001-6677-8489 ! Aleix Puig-
 relationship: has_part CL:0000158 ! club cell
 relationship: has_part CL:0002208 ! brush cell of bronchus
 relationship: has_part CL:0002329 ! basal epithelial cell of tracheobronchial tree
-relationship: has_part CL:0002332 ! ciliated cell of the bronchus
+relationship: has_part CL:0002332 ! multiciliated epithelial cell of the bronchus
 relationship: has_part CL:0017000 ! pulmonary ionocyte
 relationship: has_part CL:1000143 ! lung goblet cell
-relationship: has_part CL:1000223 ! lung neuroendocrine cell
+relationship: has_part CL:1000223 ! pulmonary neuroendocrine cell
 relationship: part_of UBERON:0002184 ! segmental bronchus
 
 [Term]
@@ -72967,8 +72965,8 @@ id: UBERON:0003532
 name: hindlimb skin
 def: "A zone of skin that is part of a hindlimb [Automatically generated definition]." [OBOL:automatic]
 synonym: "hind limb skin" EXACT [OBOL:automatic]
-synonym: "lower limb skin" EXACT [FMA:23102]
 synonym: "lower limb skin" EXACT [https://orcid.org/0000-0002-0819-0473]
+synonym: "lower limb skin" EXACT [FMA:23102]
 synonym: "skin of hind limb" EXACT [OBOL:automatic]
 synonym: "skin of hindlimb" EXACT [OBOL:automatic]
 synonym: "skin of lower extremity" EXACT [OBOL:automatic]
@@ -96792,7 +96790,7 @@ id: UBERON:0005099
 name: short descending thin limb
 def: "The short descending thin limb is the descending thin limb of a short nephron that has a squamous epithelial morphology[GO]." [GO:0072063]
 is_a: UBERON:0000483 ! epithelium
-relationship: has_part CL:0000076 ! squamous epithelial cell
+relationship: composed_primarily_of CL:0000076 ! squamous epithelial cell
 relationship: part_of UBERON:0001285 ! nephron
 property_value: editor_note "TODO - epithelium types" xsd:string
 
@@ -116141,7 +116139,7 @@ xref: NCIT:C45715
 xref: UMLS:C0682578 {source="ncithesaurus:Glandular_Epithelium"}
 xref: UMLS:C1708242 {source="ncithesaurus:Glandular_Epithelial_Tissue"}
 intersection_of: UBERON:0000483 ! epithelium
-intersection_of: composed_primarily_of CL:0000150 ! glandular epithelial cell
+intersection_of: composed_primarily_of CL:0000150 ! glandular secretory epithelial cell
 disjoint_from: UBERON:0011952 ! non-glandular epithelium
 property_value: editor_note "consider splitting epithelium from epithelial tissue" xsd:string
 
@@ -117348,7 +117346,7 @@ xref: SCTID:40118003
 xref: UMLS:C0221909 {source="ncithesaurus:Squamous_Epithelium"}
 xref: Wikipedia:Squamous_epithelium
 intersection_of: UBERON:0000483 ! epithelium
-intersection_of: has_part CL:0000076 ! squamous epithelial cell
+intersection_of: composed_primarily_of CL:0000076 ! squamous epithelial cell
 property_value: external_ontology_notes "FBbt:00007028 (squamous epithelium) A type of epithelium that is made up of flattened cells which are arranged with their long axes in the plane of the epithelium" xsd:string {external_ontology="FBbt"}
 
 [Term]
@@ -117362,7 +117360,7 @@ xref: NCIT:C13180
 xref: UMLS:C0836131 {source="ncithesaurus:Stratified_Squamous_Epithelium"}
 xref: Wikipedia:Stratified_squamous_epithelium
 intersection_of: UBERON:0000486 ! multilaminar epithelium
-intersection_of: has_part CL:0000076 ! squamous epithelial cell
+intersection_of: composed_primarily_of CL:0000076 ! squamous epithelial cell
 
 [Term]
 id: UBERON:0006916
@@ -117484,14 +117482,14 @@ xref: FMA:64800
 xref: NCIT:C13182
 xref: UMLS:C0225337 {source="ncithesaurus:Columnar_Epithelium"}
 intersection_of: UBERON:0000485 ! simple columnar epithelium
-intersection_of: composed_primarily_of CL:0000150 ! glandular epithelial cell
+intersection_of: composed_primarily_of CL:0000150 ! glandular secretory epithelial cell
 
 [Term]
 id: UBERON:0006930
 name: glandular cuboidal epithelium
 xref: FMA:66809
 intersection_of: UBERON:0000484 ! simple cuboidal epithelium
-intersection_of: composed_primarily_of CL:0000150 ! glandular epithelial cell
+intersection_of: composed_primarily_of CL:0000150 ! glandular secretory epithelial cell
 
 [Term]
 id: UBERON:0006931
@@ -130372,7 +130370,6 @@ xref: FMA:7281
 xref: NCIT:C102339
 xref: SCTID:3194006
 xref: VHOG:0001228
-is_a: UBERON:0000490 {source="EHDAA2"} ! unilaminar epithelium
 intersection_of: UBERON:0002165 ! endocardium
 intersection_of: part_of UBERON:0002078 ! right cardiac atrium
 relationship: develops_from UBERON:0005092 {source="EHDAA2"} ! right horn of sinus venosus
@@ -134919,7 +134916,7 @@ synonym: "pulmonary neuroepithelial body" EXACT [MP:0010921]
 xref: EMAPA:37943 {source="MA:th"}
 is_a: UBERON:0000061 {source="MP"} ! anatomical structure
 relationship: contributes_to_morphology_of UBERON:0000115 ! lung epithelium
-relationship: has_part CL:1000223 ! lung neuroendocrine cell
+relationship: has_part CL:1000223 ! pulmonary neuroendocrine cell
 relationship: part_of UBERON:0000115 ! lung epithelium
 relationship: part_of UBERON:8600018 ! neuroendocrine system
 

```

## Agent Attempts (9)

| # | Model | Runtime | F1 | P | R | Eval PR | Detail |
|---|-------|---------|-----|-----|-----|---------|--------|
| 1 | claude-opus-4.7 | claude | 0.190 | 0.105 | 1.000 | [#238](https://github.com/ai4curation/eval-ont-agent-uberon/pull/238) | [attempt](attempts/pr238.md) |
| 2 | gemma-4-31b | opencode | 0.190 | 0.105 | 1.000 | [#110](https://github.com/ai4curation/eval-ont-agent-uberon/pull/110) | [attempt](attempts/pr110.md) |
| 3 | gpt-5.4 | codex | 0.182 | 0.105 | 0.667 | [#80](https://github.com/ai4curation/eval-ont-agent-uberon/pull/80) | [attempt](attempts/pr80.md) |
| 4 | gpt-5.5 | codex | 0.182 | 0.105 | 0.667 | [#73](https://github.com/ai4curation/eval-ont-agent-uberon/pull/73) | [attempt](attempts/pr73.md) |
| 5 | claude-haiku-4.5 | claude | 0.174 | 0.105 | 0.500 | [#375](https://github.com/ai4curation/eval-ont-agent-uberon/pull/375) | [attempt](attempts/pr375.md) |
| 6 | claude-haiku-4.5 | claude | 0.174 | 0.105 | 0.500 | [#325](https://github.com/ai4curation/eval-ont-agent-uberon/pull/325) | [attempt](attempts/pr325.md) |
| 7 | gpt-5.5 | opencode | 0.167 | 0.105 | 0.400 | [#59](https://github.com/ai4curation/eval-ont-agent-uberon/pull/59) | [attempt](attempts/pr59.md) |
| 8 | gpt-5.5 | opencode | 0.167 | 0.105 | 0.400 | [#41](https://github.com/ai4curation/eval-ont-agent-uberon/pull/41) | [attempt](attempts/pr41.md) |
| 9 | claude-sonnet-4.5 | claude | 0.160 | 0.105 | 0.333 | [#289](https://github.com/ai4curation/eval-ont-agent-uberon/pull/289) | [attempt](attempts/pr289.md) |
