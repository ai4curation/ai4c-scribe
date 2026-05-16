---
ontology: mondo
repo: monarch-initiative/mondo
issue_number: 9795
pr_number: 10110
issue_title: '[Obsolete] OMIM merges'
pr_author: MeeSiing
pr_merged_at: '2026-04-02'
task_type: obsoletion
difficulty: medium
scoping: tightly_scoped
scope: single_term
review_outcome: approved_first_time
num_agent_attempts: 16
generated_at: '2026-05-15'
scoping_notes: PR merges one obsolete term into a surviving term, transferring annotations.
domain_area: rare-disease
best_f1: 0.464
best_model: gpt-5.4
---

# PR #10110 — [Obsolete] OMIM merges

**mondo** | [monarch-initiative/mondo](https://github.com/monarch-initiative/mondo) | [Issue #9795](https://github.com/monarch-initiative/mondo/issues/9795) | [PR #10110](https://github.com/monarch-initiative/mondo/pull/10110) | @MeeSiing | merged 2026-04-02

`obsoletion` `medium` `tightly_scoped` `approved_first_time`

## Context

As part of a broader OMIM merge review (issue #9795), Usher syndrome type 1J was identified for merger into MONDO:0012273 (autosomal recessive nonsyndromic hearing loss 48). OMIM had consolidated these entries, and Mondo needed to follow suit. The decision required evaluating whether the syndromic (Usher) and nonsyndromic (hearing loss) presentations truly represent the same genetic entity.

Supporting documentation was maintained in a shared Google Doc tracking all OMIM merges for this batch.

## Changes Made

Merged Usher syndrome type 1J into MONDO:0012273 by obsoleting the Usher term and transferring its cross-references and annotations to the surviving hearing loss term. The 14 additions and 28 deletions reflect that more content was removed (obsoleted stanza) than added (transferred annotations plus obsoletion metadata).

## Resolution

Medium difficulty because the curator must evaluate whether merging a syndromic presentation (Usher syndrome, which includes retinal degeneration) with a nonsyndromic hearing loss term is scientifically justified. This requires understanding the genetic basis and phenotypic spectrum of the underlying mutation, not just following OMIM's lead blindly.

## Human Diff

```diff
diff --git a/src/ontology/mondo-edit.obo b/src/ontology/mondo-edit.obo
index 8fe17dbb40..655cff2e9c 100644
--- a/src/ontology/mondo-edit.obo
+++ b/src/ontology/mondo-edit.obo
@@ -312900,8 +312900,6 @@ subset: gard_rare {source="GARD:0022612", source="MONDO:GARD"}
 subset: nord_rare {source="MONDO:NORD"}
 subset: omim {source="OMIM:609439"}
 subset: rare
-synonym: "autosomal recessive deafness 48" NARROW []
-synonym: "autosomal recessive nonsyndromic deafness 48" NARROW []
 synonym: "autosomal recessive nonsyndromic deafness caused by mutation in CIB2" NARROW [MONDO:design_pattern]
 synonym: "autosomal recessive nonsyndromic deafness type 48" NARROW [MONDO:RULE_2]
 synonym: "autosomal recessive nonsyndromic hearing loss 48" EXACT [] {OMO:0002001="https://w3id.org/information-resource-registry/clingen"}
@@ -312909,13 +312907,20 @@ synonym: "CIB2 autosomal recessive nonsyndromic deafness" NARROW [MONDO:design_p
 synonym: "deafness, autosomal recessive 48" NARROW [MONDO:Lexical]
 synonym: "deafness, autosomal recessive type 48" NARROW [MONDO:RULE_2]
 synonym: "DFNB48" NARROW ABBREVIATION [MONDO:Lexical]
+synonym: "USH1J" EXACT ABBREVIATION [OMIM:609439]
+synonym: "Usher syndrome type 1J" EXACT [OMIM:609439]
 xref: DOID:0110505 {source="MONDO:equivalentTo"}
+xref: DOID:0110836 {source="MONDO:equivalentObsolete"}
+xref: GARD:0015863 {source="MONDO:GARD"}
 xref: GARD:0022612 {source="MONDO:GARD"}
 xref: ICD10CM:H90.3 {source="DOID:0110505"}
-xref: MEDGEN:332149 {source="MONDO:equivalentTo", source="MONDO:MEDGEN"}
+xref: MEDGEN:332149 {source="MONDO:equivalentTo", source="MONDO:MEDGEN", source="MONDO:preferredExternal"}
+xref: MEDGEN:766858 {source="MONDO:equivalentTo", source="MONDO:MEDGEN"}
 xref: MESH:C563720 {source="MONDO:equivalentTo"}
 xref: OMIM:609439 {source="DOID:0110505", source="MONDO:equivalentTo"}
-xref: UMLS:C1836199 {source="MONDO:equivalentTo", source="MONDO:MEDGEN", source="MEDGEN:332149"}
+xref: OMIM:614869 {source="MONDO:equivalentObsolete", source="DOID:0110836"}
+xref: UMLS:C1836199 {source="MONDO:equivalentTo", source="MONDO:MEDGEN", source="MEDGEN:332149", source="MONDO:preferredExternal"}
+xref: UMLS:C3553944 {source="MONDO:equivalentTo", source="MONDO:MEDGEN", source="MEDGEN:766858"}
 is_a: MONDO:0019588 {source="DC-OMIM:609439", source="DOID:0110505", source="MONDO:Redundant", source="OMIM:609439"} ! hearing loss, autosomal recessive
 intersection_of: MONDO:0019588 ! hearing loss, autosomal recessive
 intersection_of: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/24579 ! CIB2
@@ -312923,6 +312928,7 @@ relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/
 property_value: curated_content_resource "https://www.malacards.org/card/deafness_autosomal_recessive_48_2" xsd:anyURI {source="MONDO:MalaCards"}
 property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/4521" xsd:anyURI
 property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/551" xsd:anyURI
+property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9795" xsd:anyURI
 
 [Term]
 id: MONDO:0012274
@@ -358932,31 +358938,11 @@ property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/
 
 [Term]
 id: MONDO:0013935
-name: Usher syndrome type 1J
-def: "Any Usher syndrome in which the cause of the disease is a mutation in the CIB2 gene." [MONDO:patterns/disease_series_by_gene]
-comment: This term is scheduled for obsoletion based on the fact that it is a historical diseaseAfter obsoletion, this term will not have a replacement ID, but one could consider the following term: autosomal recessive nonsyndromic hearing loss 48-MONDO:0012273
-subset: gard_rare {source="GARD:0015863", source="MONDO:GARD"}
-subset: nord_rare {source="MONDO:NORD"}
-subset: obsoletion_candidate
-subset: rare
-synonym: "CIB2 Usher syndrome" EXACT [MONDO:design_pattern, MONDO:patterns/disease_series_by_gene]
-synonym: "USH1J" EXACT ABBREVIATION [MONDO:Lexical]
-synonym: "Usher syndrome caused by mutation in CIB2" EXACT [MONDO:design_pattern]
-synonym: "Usher syndrome type Ij" EXACT []
-synonym: "Usher syndrome, type 1J" RELATED []
-synonym: "USHER syndrome, type Ij" RELATED [MONDO:Lexical]
-xref: DOID:0110836 {source="MONDO:equivalentObsolete"}
-xref: GARD:0015863 {source="MONDO:GARD"}
-xref: MEDGEN:766858 {source="MONDO:equivalentTo", source="MONDO:MEDGEN"}
-xref: OMIM:614869 {source="MONDO:equivalentObsolete", source="DOID:0110836"}
-xref: UMLS:C3553944 {source="MONDO:equivalentTo", source="MONDO:MEDGEN", source="MEDGEN:766858"}
-is_a: MONDO:0010168 {source="DOID:0110836", source="Orphanet:231169"} ! Usher syndrome type 1
-is_a: MONDO:0019501 {source="DOID:0110836/inferred", source="MONDO:Redundant", source="OMIM:614869"} ! Usher syndrome
-relationship: has_characteristic HP:0000007 {source="MONDO:HPOA", source="OMIM:614869"} ! Autosomal recessive inheritance
-property_value: curated_content_resource "https://www.malacards.org/card/usher_syndrome_type_ij" xsd:anyURI {source="MONDO:MalaCards"}
-property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9778" xsd:anyURI
+name: obsolete Usher syndrome type 1J
+property_value: IAO:0000231 MONDO:TermsMerged
 property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9795" xsd:anyURI
-property_value: IAO:0006012 "2026-02-01" xsd:string
+is_obsolete: true
+replaced_by: MONDO:0012273
 
 [Term]
 id: MONDO:0013936

```

## Agent Attempts (16)

| # | Model | Runtime | F1 | P | R | Blob | Eval PR | Detail |
|---|-------|---------|-----|-----|-----|------|---------|--------|
| 1 | gpt-5.4 | codex | 0.464 | 0.707 | 0.345 | `875b11d` | [#163](https://github.com/ai4curation/eval-ont-agent-mondo/pull/163) | [attempt](attempts/pr163.md) |
| 2 | gpt-5.5 | opencode | 0.414 | 0.854 | 0.273 | `8a12406` | [#72](https://github.com/ai4curation/eval-ont-agent-mondo/pull/72) | [attempt](attempts/pr72.md) |
| 3 | gpt-5.5 | opencode | 0.414 | 0.854 | 0.273 | `8a12406` | [#57](https://github.com/ai4curation/eval-ont-agent-mondo/pull/57) | [attempt](attempts/pr57.md) |
| 4 | gpt-5.5 | codex | 0.412 | 0.854 | 0.271 | `4170e89` | [#34](https://github.com/ai4curation/eval-ont-agent-mondo/pull/34) | [attempt](attempts/pr34.md) |
| 5 | claude-opus-4.7 | claude | 0.402 | 0.854 | 0.263 | `5706df7` | [#380](https://github.com/ai4curation/eval-ont-agent-mondo/pull/380) | [attempt](attempts/pr380.md) |
| 6 | claude-opus-4.7 | claude | 0.402 | 0.854 | 0.263 | `5706df7` | [#379](https://github.com/ai4curation/eval-ont-agent-mondo/pull/379) | [attempt](attempts/pr379.md) |
| 7 | claude-opus-4.7 | claude | 0.402 | 0.854 | 0.263 | `5706df7` | [#377](https://github.com/ai4curation/eval-ont-agent-mondo/pull/377) | [attempt](attempts/pr377.md) |
| 8 | claude-opus-4.7 | claude | 0.402 | 0.854 | 0.263 | `5706df7` | [#376](https://github.com/ai4curation/eval-ont-agent-mondo/pull/376) | [attempt](attempts/pr376.md) |
| 9 | kimi-k2.6 | opencode | 0.398 | 0.854 | 0.259 | `3ac6778` | [#253](https://github.com/ai4curation/eval-ont-agent-mondo/pull/253) | [attempt](attempts/pr253.md) |
| 10 | claude-haiku-4.5 | claude | 0.392 | 0.488 | 0.328 | `f26acad` | [#296](https://github.com/ai4curation/eval-ont-agent-mondo/pull/296) | [attempt](attempts/pr296.md) |
| 11 | claude-haiku-4.5 | claude | 0.392 | 0.488 | 0.328 | `f26acad` | [#185](https://github.com/ai4curation/eval-ont-agent-mondo/pull/185) | [attempt](attempts/pr185.md) |
| 12 | claude-sonnet-4.5 | copilot | 0.352 | 0.463 | 0.284 | `3e2c892` | [#347](https://github.com/ai4curation/eval-ont-agent-mondo/pull/347) | [attempt](attempts/pr347.md) |
| 13 | claude-sonnet-4.5 | copilot | 0.352 | 0.463 | 0.284 | `3e2c892` | [#338](https://github.com/ai4curation/eval-ont-agent-mondo/pull/338) | [attempt](attempts/pr338.md) |
| 14 | claude-sonnet-4.5 | copilot | 0.352 | 0.463 | 0.284 | `3e2c892` | [#337](https://github.com/ai4curation/eval-ont-agent-mondo/pull/337) | [attempt](attempts/pr337.md) |
| 15 | claude-sonnet-4.5 | copilot | 0.343 | 0.415 | 0.293 | `495146a` | [#336](https://github.com/ai4curation/eval-ont-agent-mondo/pull/336) | [attempt](attempts/pr336.md) |
| 16 | claude-sonnet-4.5 | claude | 0.339 | 0.488 | 0.260 | `71e957f` | [#438](https://github.com/ai4curation/eval-ont-agent-mondo/pull/438) | [attempt](attempts/pr438.md) |
