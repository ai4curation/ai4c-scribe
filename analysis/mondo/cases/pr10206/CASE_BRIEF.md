---
ontology: mondo
repo: monarch-initiative/mondo
issue_number: 9892
pr_number: 10206
issue_title: chronic myelogenous leukemia, BCR-ABL1 positive
pr_author: MeeSiing
pr_merged_at: '2026-04-30'
task_type: synonym_update
difficulty: simple
scoping: tightly_scoped
scope: single_term
review_outcome: changes_requested
num_agent_attempts: 10
generated_at: '2026-05-15'
scoping_notes: Changes limited to relabeling one term and updating its synonyms.
domain_area: oncology
best_f1: 0.769
best_model: claude-sonnet-4.5
---

# PR #10206 — chronic myelogenous leukemia, BCR-ABL1 positive

**mondo** | [monarch-initiative/mondo](https://github.com/monarch-initiative/mondo) | [Issue #9892](https://github.com/monarch-initiative/mondo/issues/9892) | [PR #10206](https://github.com/monarch-initiative/mondo/pull/10206) | @MeeSiing | merged 2026-04-30

`synonym_update` `simple` `tightly_scoped` `changes_requested`

## Context

A request was made to relabel MONDO:0011996 to "chronic myeloid leukemia" to better align with OMIM's naming ("leukemia, chronic myeloid"). The existing label "chronic myelogenous leukemia, BCR-ABL1 positive" was considered overly specific for the primary label, as the BCR-ABL1 qualifier could be captured as a synonym instead.

The PR involved some discussion about how strictly Mondo should follow OMIM naming conventions, reflected in the 3 commits needed to finalize the label.

## Changes Made

Relabeled MONDO:0011996 from "chronic myelogenous leukemia, BCR-ABL1 positive" to "chronic myeloid leukemia" in `src/ontology/mondo-edit.obo`. The old label and variations were preserved as synonyms. The 7 additions and 8 deletions reflect the label change plus synonym adjustments across 3 commits.

## Resolution

Easy difficulty overall, though it required a minor judgment call about naming conventions. The multiple commits suggest some back-and-forth about the exact label wording. An agent would need to understand Mondo's relationship with OMIM naming and when to simplify versus preserve qualifier terms.

## Human Diff

```diff
diff --git a/src/ontology/mondo-edit.obo b/src/ontology/mondo-edit.obo
index 1d63d0424f..29e09aaed4 100644
--- a/src/ontology/mondo-edit.obo
+++ b/src/ontology/mondo-edit.obo
@@ -133431,7 +133431,7 @@ xref: SCTID:413656006 {source="MONDO:equivalentTo"}
 xref: UMLS:C0005699 {source="MONDO:equivalentTo", source="MONDO:MEDGEN", source="MEDGEN:2281"}
 is_a: MONDO:0005059 {source="EFO:1000131", source="MESH:D001752/inferred", source="NCIT:C9110/inferred"} ! leukemia
 is_a: MONDO:0005170 {source="EFO:1000131", source="NCIT:C9110/inferred"} ! myeloid neoplasm
-is_a: MONDO:0011996 {source="NCIT:C9110"} ! chronic myelogenous leukemia, BCR-ABL1 positive
+is_a: MONDO:0011996 {source="NCIT:C9110"} ! chronic myeloid leukemia
 
 [Term]
 id: MONDO:0006116
@@ -262021,7 +262021,7 @@ xref: MEDGEN:325075 {source="MONDO:equivalentTo", source="MONDO:MEDGEN"}
 xref: MESH:C536093 {source="MONDO:equivalentTo"}
 xref: OMIM:600080 {source="DOID:0060761", source="MONDO:equivalentTo"}
 xref: UMLS:C1838670 {source="MONDO:equivalentTo", source="MONDO:MEDGEN", source="MEDGEN:325075"}
-is_a: MONDO:0011996 {source="DOID:0060761"} ! chronic myelogenous leukemia, BCR-ABL1 positive
+is_a: MONDO:0011996 {source="DOID:0060761"} ! chronic myeloid leukemia
 property_value: curated_content_resource "https://www.malacards.org/card/myelocytic_leukemia_like_syndrome_familial_chronic" xsd:anyURI {source="MONDO:MalaCards"}
 property_value: seeAlso "https://rarediseases.info.nih.gov/diseases/10141/myelocytic-leukemia-like-syndrome-familial-chronic" xsd:anyURI {source="GARD:0010141"}
 
@@ -293841,7 +293841,7 @@ property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/
 
 [Term]
 id: MONDO:0011996
-name: chronic myelogenous leukemia, BCR-ABL1 positive
+name: chronic myeloid leukemia
 def: "A chronic myeloproliferative neoplasm characterized by the expression of the BCR-ABL1 fusion gene. It presents with neutrophilic leukocytosis. It can appear at any age, but it mostly affects middle aged and older individuals. Patients usually present with fatigue, weight loss, anemia, night sweats, and splenomegaly. If untreated, it follows a biphasic or triphasic natural course; an initial indolent chronic phase which is followed by an accelerated phase, a blast phase, or both. Allogeneic stem cell transplantation and tyrosine kinase inhibitors delay disease progression and prolong overall survival." [NCIT:C3174]
 subset: doid {source="DOID:0081088", source="DOID:8552"}
 subset: doid_rare {source="DOID:8552"}
@@ -293864,15 +293864,13 @@ synonym: "chronic myelogenous leukemia" EXACT [DOID:8552, NCIT:C3174, Orphanet:5
 synonym: "chronic myelogenous leukemia (CML)" EXACT [NCIT:C3174]
 synonym: "chronic myelogenous leukemia, BCR-ABL1 Positive" EXACT [DOID:0081088, NCIT:C3174]
 synonym: "chronic myelogenous leukemias" EXACT [NCIT:C3174]
-synonym: "chronic myeloid leukemia" EXACT [DOID:8552, NCIT:C3174, Orphanet:521]
+synonym: "chronic myeloid leukemia" EXACT [DOID:8552, https://medlineplus.gov/genetics/condition/chronic-myeloid-leukemia/#synonyms, https://orcid.org/0000-0001-9310-0163, https://www.cancer.gov/types/leukemia/patient/cml-treatment-pdq, https://www.cancer.org/cancer/types/chronic-myeloid-leukemia/about/what-is-cml.html, NCIT:C3174, Orphanet:521]
 synonym: "CML" EXACT ABBREVIATION [DOID:8552, NCIT:C3174, OMIM:608232, Orphanet:521]
 synonym: "CML - chronic myelogenous leukaemia" EXACT OMO:0003005 []
 synonym: "CML - chronic myelogenous leukemia" EXACT [DOID:8552, NCIT:C3174]
 synonym: "hematopoeitic - chronic myelocytic leukaemia (CML)" EXACT OMO:0003005 []
 synonym: "hematopoeitic - chronic myelocytic leukemia (CML)" EXACT [NCIT:C3174]
-synonym: "leukemia, chronic myeloid" RELATED []
-synonym: "leukemia, chronic myeloid, Philadelphia chromosome positive, somatic" EXACT []
-synonym: "leukemia, Philadelphia chromosome-positive, resistant to imatinib, Somatic mutation" EXACT []
+synonym: "leukimia, chronic myeloid" EXACT [OMIM:608232]
 synonym: "myeloid leukemia, chronic" EXACT [DOID:8552, MONDO:patterns/chronic, MTH:NOCODE]
 xref: DOID:0081088 {source="MONDO:equivalentTo", source="MONDO:preferredExternal"}
 xref: DOID:8552 {source="MONDO:equivalentTo", source="EFO:0000339"}
@@ -293903,6 +293901,7 @@ relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/
 property_value: curated_content_resource "https://www.malacards.org/card/chronic_myelogenous_leukemia_bcr_abl1_positive" xsd:anyURI {source="MONDO:MalaCards"}
 property_value: curated_content_resource "https://www.malacards.org/card/leukemia_chronic_myeloid" xsd:anyURI {source="MONDO:MalaCards"}
 property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/4521" xsd:anyURI
+property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9892" xsd:anyURI
 
 [Term]
 id: MONDO:0011997
@@ -512035,7 +512034,7 @@ xref: MESH:D015465 {source="UMLS:C0023472", source="MONDO:equivalentTo"}
 xref: NCIT:C3173 {source="UMLS:C0023472", source="MONDO:equivalentTo", source="https://orcid.org/0000-0002-5002-8648"}
 xref: SCTID:413389003 {source="UMLS:C0023472"}
 xref: UMLS:C0023472 {source="MEDGEN:6059", source="MONDO:equivalentTo", source="MONDO:MEDGEN"}
-is_a: MONDO:0011996 {source="UMLS:C0023472"} ! chronic myelogenous leukemia, BCR-ABL1 positive
+is_a: MONDO:0011996 {source="UMLS:C0023472"} ! chronic myeloid leukemia
 property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/8567" xsd:anyURI
 
 [Term]

```

## Agent Attempts (10)

| # | Model | Runtime | F1 | P | R | Blob | Eval PR | Detail |
|---|-------|---------|-----|-----|-----|------|---------|--------|
| 1 | claude-sonnet-4.5 | copilot | 0.769 | 0.667 | 0.909 | `e3e3dd9` | [#520](https://github.com/ai4curation/eval-ont-agent-mondo/pull/520) | [attempt](attempts/pr520.md) |
| 2 | claude-sonnet-4.5 | copilot | 0.769 | 0.667 | 0.909 | `e3e3dd9` | [#488](https://github.com/ai4curation/eval-ont-agent-mondo/pull/488) | [attempt](attempts/pr488.md) |
| 3 | claude-opus-4.7 | claude | 0.769 | 0.667 | 0.909 | `4514441` | [#397](https://github.com/ai4curation/eval-ont-agent-mondo/pull/397) | [attempt](attempts/pr397.md) |
| 4 | kimi-k2.6 | opencode | 0.769 | 0.667 | 0.909 | `c5db975` | [#251](https://github.com/ai4curation/eval-ont-agent-mondo/pull/251) | [attempt](attempts/pr251.md) |
| 5 | claude-sonnet-4.5 | claude | 0.741 | 0.667 | 0.833 | `65a5b11` | [#435](https://github.com/ai4curation/eval-ont-agent-mondo/pull/435) | [attempt](attempts/pr435.md) |
| 6 | gpt-5.5 | opencode | 0.741 | 0.667 | 0.833 | `65a5b11` | [#82](https://github.com/ai4curation/eval-ont-agent-mondo/pull/82) | [attempt](attempts/pr82.md) |
| 7 | gpt-5.5 | opencode | 0.741 | 0.667 | 0.833 | `65a5b11` | [#63](https://github.com/ai4curation/eval-ont-agent-mondo/pull/63) | [attempt](attempts/pr63.md) |
| 8 | gpt-5.5 | codex | 0.741 | 0.667 | 0.833 | `fc7a3ab` | [#44](https://github.com/ai4curation/eval-ont-agent-mondo/pull/44) | [attempt](attempts/pr44.md) |
| 9 | gemma-4-31b | opencode | 0.211 | 0.133 | 0.500 | `faea8f9` | [#291](https://github.com/ai4curation/eval-ont-agent-mondo/pull/291) | [attempt](attempts/pr291.md) |
| 10 | gemma-4-31b | opencode | 0.211 | 0.133 | 0.500 | `faea8f9` | [#206](https://github.com/ai4curation/eval-ont-agent-mondo/pull/206) | [attempt](attempts/pr206.md) |
