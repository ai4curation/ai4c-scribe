---
ontology: mondo
repo: monarch-initiative/mondo
issue_number: 9871
pr_number: 10201
issue_title: MONDO:0009106 diastematomyelia
pr_author: MeeSiing
pr_merged_at: '2026-05-04'
task_type: other
difficulty: medium
scoping: loosely_scoped
scope: multi_term
review_outcome: changes_requested
num_agent_attempts: 7
generated_at: '2026-05-15'
best_f1: 0.45
best_model: kimi-k2.6
---

# PR #10201 — MONDO:0009106 diastematomyelia

**mondo** | [monarch-initiative/mondo](https://github.com/monarch-initiative/mondo) | [Issue #9871](https://github.com/monarch-initiative/mondo/issues/9871) | [PR #10201](https://github.com/monarch-initiative/mondo/pull/10201) | @MeeSiing | merged 2026-05-04

`other` `medium` `loosely_scoped` `changes_requested`

## Context

Issue #9871 reported that MONDO:0009106 (diastematomyelia) had an incorrect Orphanet cross-reference (Orphanet:1671 for "Split cord malformation type I" rather than the broader concept). Investigation revealed that Orphanet:573278 correctly maps to the broader concept of diastematomyelia/split cord malformation, and that subtypes (type I with osseous spur, type II with fibrous septum) should be represented.

## Changes Made

The PR evolved from a simple xref correction into a multi-term edit across 5 commits. The initial commit updated the Orphanet xref from 1671 to 573278. A proxy merge was fixed in the second commit. The third commit added 3 new subtypes (MONDO:1060220-1060222) for split cord malformation classification. The fourth and fifth commits resolved merge conflicts with master. The 59 additions and 21 deletions reflect both the xref correction and the creation of new subtype terms with definitions, synonyms, and parent axioms.

## Resolution

Moderate difficulty because the scope expanded significantly from the original request. What began as a cross-reference correction required domain knowledge about split cord malformation types to realize that subtypes were needed. The merge conflicts and multiple commits show iterative development. An agent would need to recognize when an xref discrepancy indicates a deeper modeling issue requiring new terms.

## Human Diff

```diff
diff --git a/src/ontology/mondo-edit.obo b/src/ontology/mondo-edit.obo
index 3616a71b6a..027d104cae 100644
--- a/src/ontology/mondo-edit.obo
+++ b/src/ontology/mondo-edit.obo
@@ -210460,35 +210460,37 @@ subset: gard_rare {source="GARD:0001851", source="MONDO:GARD"}
 subset: ncit {source="NCIT:C98913"}
 subset: nord_rare {source="MONDO:NORD"}
 subset: omim {source="OMIM:222500"}
-subset: ordo_disorder {source="Orphanet:1671"}
+subset: ordo_disorder {source="Orphanet:573278"}
 subset: ordo_morphological_anomaly {source="Orphanet:1671"}
-subset: orphanet {source="Orphanet:1671"}
-subset: orphanet_rare {source="Orphanet:1671"}
+subset: orphanet {source="Orphanet:573278"}
+subset: orphanet_rare {source="Orphanet:573278"}
 subset: otar {source="MONDO:OTAR"}
 subset: rare
-synonym: "diastematomyelia" EXACT [ICD10CM:Q06.2, icd11.foundation:2070601288, NCIT:C98913, OMIM:222500, Orphanet:1671]
+synonym: "diastematomyelia" EXACT [ICD10CM:Q06.2, icd11.foundation:2070601288, NCIT:C98913, OMIM:222500, Orphanet:573278]
 synonym: "Dimyelia" RELATED [GARD:0001851]
 synonym: "diplomyelia" RELATED [GARD:0001851]
 synonym: "Pseudodiplomyelia" RELATED [GARD:0001851]
-synonym: "SCM type 1" EXACT [Orphanet:1671]
-synonym: "split cord malformation" RELATED [GARD:0001851]
-synonym: "split cord malformation type 1" EXACT [Orphanet:1671]
-synonym: "split spinal cord malformation" RELATED [GARD:0001851]
-synonym: "SSCM" RELATED ABBREVIATION [GARD:0001851]
+synonym: "SCM type 1" NARROW ABBREVIATION [Orphanet:1671]
+synonym: "split cord malformation" EXACT [GARD:0001851, Orphanet:573278]
+synonym: "split cord malformation type 1" NARROW [Orphanet:1671]
+synonym: "split spinal cord malformation" EXACT [GARD:0001851, Orphanet:573278]
+synonym: "SSCM" EXACT ABBREVIATION [GARD:0001851]
 xref: GARD:0001851 {source="MONDO:GARD"}
-xref: ICD10CM:Q06.2 {source="Orphanet:1671", source="MONDO:equivalentTo", source="Orphanet:1671/e", source="Orphanet:1671/specific"}
+xref: ICD10CM:Q06.2 {source="Orphanet:573278", source="MONDO:equivalentTo"}
 xref: icd11.foundation:2070601288 {source="MONDO:equivalentTo"}
 xref: ICD9:742.51 {source="MONDO:equivalentTo", source="MONDO:i2s"}
-xref: MedDRA:10012750 {source="Orphanet:1671", source="Orphanet:1671/e"}
+xref: MedDRA:10012750 {source="Orphanet:573278"}
 xref: MEDGEN:3801 {source="MONDO:equivalentTo", source="MONDO:MEDGEN"}
 xref: NCIT:C98913 {source="MONDO:equivalentTo"}
-xref: OMIM:222500 {source="Orphanet:1671", source="MONDO:equivalentTo", source="Orphanet:1671/e"}
-xref: Orphanet:1671 {source="MONDO:equivalentTo", source="OMIM:222500"}
+xref: OMIM:222500 {source="MONDO:equivalentTo"}
+xref: Orphanet:573278 {source="MONDO:equivalentTo"}
 xref: SCTID:49351009 {source="MONDO:equivalentTo"}
 xref: UMLS:C0011999 {source="MONDO:equivalentTo", source="MONDO:MEDGEN", source="MEDGEN:3801"}
 is_a: MONDO:0002320 {source="NCIT:C98913"} ! congenital nervous system disorder
 is_a: MONDO:0018075 {source="MONDO:0017085-obsoleted", source="https://github.com/monarch-initiative/mondo/pull/2571/"} ! neural tube defect
 property_value: curated_content_resource "https://www.malacards.org/card/diastematomyelia" xsd:anyURI {source="MONDO:MalaCards"}
+property_value: curated_content_resource "https://www.malacards.org/card/split_cord_malformation" xsd:anyURI {source="MONDO:MalaCards"}
+property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9871" xsd:anyURI
 
 [Term]
 id: MONDO:0009107
@@ -558641,23 +558643,21 @@ property_value: curated_content_resource "https://www.malacards.org/card/pheochr
 [Term]
 id: MONDO:0035541
 name: obsolete split cord malformation type II
-subset: ordo_disorder {source="Orphanet:573253"}
-xref: Orphanet:573253 {source="MONDO:obsoleteEquivalent"}
-property_value: curated_content_resource "https://www.malacards.org/card/split_cord_malformation_type_ii" xsd:anyURI {source="MONDO:MalaCards"}
-property_value: IAO:0000231 OMO:0001000 {source="MONDO:excludePhenotype"}
+property_value: IAO:0000231 MONDO:TermsMerged
 property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/4776" xsd:anyURI
 property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/7693" xsd:anyURI
+property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9871" xsd:anyURI
 is_obsolete: true
+replaced_by: MONDO:1060221
 
 [Term]
 id: MONDO:0035542
 name: obsolete split cord malformation
-subset: ordo_group_of_disorders {source="Orphanet:573278"}
-xref: Orphanet:573278 {source="MONDO:obsoleteEquivalent"}
-property_value: curated_content_resource "https://www.malacards.org/card/split_cord_malformation" xsd:anyURI {source="MONDO:MalaCards"}
-property_value: IAO:0000231 OMO:0001000 {source="MONDO:excludePhenotype"}
+property_value: IAO:0000231 MONDO:TermsMerged
 property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/4776" xsd:anyURI
+property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9871" xsd:anyURI
 is_obsolete: true
+replaced_by: MONDO:0009106
 
 [Term]
 id: MONDO:0035547
@@ -659109,6 +659109,44 @@ relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/
 property_value: http://purl.org/dc/terms/creator https://orcid.org/0000-0002-7638-4659
 property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9956" xsd:anyURI
 
+[Term]
+id: MONDO:1060220
+name: split cord malformation type I
+def: "A rare subtype of split cord malformation characterized by each hemicord contained in its own dural sac, typically with an intervening bony or cartilaginous septum." [https://orcid.org/0000-0002-7638-4659, Orphanet:1671]
+synonym: "SCM type 1" EXACT ABBREVIATION [Orphanet:1671]
+synonym: "SCM type I" EXACT ABBREVIATION [Orphanet:1671]
+synonym: "split cord malformation type 1" EXACT [Orphanet:1671]
+xref: Orphanet:1671 {source="MONDO:equivalentTo"}
+is_a: MONDO:0009106 {source="Orphanet:1671"} ! diastematomyelia
+property_value: http://purl.org/dc/terms/creator https://orcid.org/0000-0002-7638-4659
+property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9871" xsd:anyURI
+
+[Term]
+id: MONDO:1060221
+name: split cord malformation type II
+def: "A rare subtype of split cord malformation characterized by both hemicords included in the same single dural sac. An intradural intervening mesenchymal septum may be present." [https://orcid.org/0000-0002-7638-4659, Orphanet:573253]
+synonym: "diplomyelia" EXACT [Orphanet:573253]
+synonym: "SCM type 2" EXACT ABBREVIATION [Orphanet:573253]
+synonym: "SCM type II" EXACT ABBREVIATION [Orphanet:573253]
+synonym: "split cord malformation type 2" EXACT [Orphanet:573253]
+xref: Orphanet:573253 {source="MONDO:equivalentTo"}
+is_a: MONDO:0009106 {source="Orphanet:573253"} ! diastematomyelia
+property_value: curated_content_resource "https://www.malacards.org/card/split_cord_malformation_type_ii" xsd:anyURI {source="MONDO:MalaCards"}
+property_value: http://purl.org/dc/terms/creator https://orcid.org/0000-0002-7638-4659
+property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9871" xsd:anyURI
+
+[Term]
+id: MONDO:1060222
+name: split cord malformation, composite type
+def: "A rare intermediate form of split cord malformation characterized by both hemichords encapsulated in a single dural sac with presence of an incomplete ventral or dorsal bony spur." [https://orcid.org/0000-0002-7638-4659, Orphanet:633076, PMID:31557552]
+synonym: "split cord malformation type 1.5" EXACT [Orphanet:633076]
+synonym: "split cord malformation, intermediate type" EXACT [Orphanet:633076]
+synonym: "split cord malformation, mixed type" EXACT [Orphanet:633076]
+xref: Orphanet:633076 {source="MONDO:equivalentTo"}
+is_a: MONDO:0009106 {source="Orphanet:633076"} ! diastematomyelia
+property_value: http://purl.org/dc/terms/creator https://orcid.org/0000-0002-7638-4659
+property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9871" xsd:anyURI
+
 [Term]
 id: MONDO:1060223
 name: RNU12-related minor spliceopathy disorder

```

## Agent Attempts (7)

| # | Model | Runtime | F1 | P | R | Eval PR | Detail |
|---|-------|---------|-----|-----|-----|---------|--------|
| 1 | kimi-k2.6 | opencode | 0.450 | 0.321 | 0.750 | [#249](https://github.com/ai4curation/eval-ont-agent-mondo/pull/249) | [attempt](attempts/pr249.md) |
| 2 | gpt-5.5 | codex | 0.405 | 0.268 | 0.833 | [#563](https://github.com/ai4curation/eval-ont-agent-mondo/pull/563) | [attempt](attempts/pr563.md) |
| 3 | claude-opus-4.7 | claude | 0.405 | 0.286 | 0.696 | [#391](https://github.com/ai4curation/eval-ont-agent-mondo/pull/391) | [attempt](attempts/pr391.md) |
| 4 | claude-sonnet-4.5 | claude | 0.385 | 0.268 | 0.682 | [#432](https://github.com/ai4curation/eval-ont-agent-mondo/pull/432) | [attempt](attempts/pr432.md) |
| 5 | claude-sonnet-4.5 | copilot | 0.239 | 0.143 | 0.727 | [#524](https://github.com/ai4curation/eval-ont-agent-mondo/pull/524) | [attempt](attempts/pr524.md) |
| 6 | claude-sonnet-4.5 | copilot | 0.239 | 0.143 | 0.727 | [#489](https://github.com/ai4curation/eval-ont-agent-mondo/pull/489) | [attempt](attempts/pr489.md) |
| 7 | claude-haiku-4.5 | claude | 0.069 | 0.036 | 1.000 | [#307](https://github.com/ai4curation/eval-ont-agent-mondo/pull/307) | [attempt](attempts/pr307.md) |
