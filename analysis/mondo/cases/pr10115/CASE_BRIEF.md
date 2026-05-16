---
ontology: mondo
repo: monarch-initiative/mondo
issue_number: 9855
pr_number: 10115
issue_title: Request for new term PADI6-related oocyte/zygote/embryo maturation arrest
  16 and maternal-effect disorder
pr_author: katiermullen
pr_merged_at: '2026-04-02'
task_type: new_term
difficulty: medium
scoping: tightly_scoped
scope: single_term
review_outcome: approved_first_time
num_agent_attempts: 6
generated_at: '2026-05-15'
best_f1: 0.348
best_model: claude-sonnet-4.5
---

# PR #10115 — Request for new term PADI6-related oocyte/zygote/embryo maturation arrest 16 and maternal-effect disorder

**mondo** | [monarch-initiative/mondo](https://github.com/monarch-initiative/mondo) | [Issue #9855](https://github.com/monarch-initiative/mondo/issues/9855) | [PR #10115](https://github.com/monarch-initiative/mondo/pull/10115) | @katiermullen | merged 2026-04-02

`new_term` `medium` `tightly_scoped` `approved_first_time`

## Context

Issue #9855 requested a new term for "PADI6-related oocyte/zygote/embryo maturation arrest 16 and maternal-effect disorder". The curator discovered that this concept overlapped with the previously obsoleted MONDO:0014978, which had been deprecated but contained relevant metadata (synonyms, xrefs, definitions) that should be preserved in the new term.

## Changes Made

The PR created the new term while incorporating metadata from obsoleted MONDO:0014978. The 19 additions include the new term stanza with label, definition, synonyms (including "oocyte/zygote/embryo maturation arrest 16" and "PREIMPLANTATION EMBRYONIC LETHALITY 2"), parent classification, and cross-references. The 11 deletions likely reflect updating the obsoleted term's replaced_by annotation to point to the new term.

## Resolution

Moderate difficulty because it requires recognizing the relationship between a new term request and an existing obsoleted term. The curator noted this overlap in the PR description and merged information appropriately. An agent would need to search for related obsoleted terms when creating new terms and reconcile their metadata, which requires understanding of the obsoletion/replacement workflow.

## Human Diff

```diff
diff --git a/src/ontology/mondo-edit.obo b/src/ontology/mondo-edit.obo
index 8fe17dbb40..db0b71d65b 100644
--- a/src/ontology/mondo-edit.obo
+++ b/src/ontology/mondo-edit.obo
@@ -388643,19 +388643,11 @@ property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/
 [Term]
 id: MONDO:0014978
 name: obsolete preimplantation embryonic lethality 2
-def: "OBSOLETE. Any preimplantation embryonic lethality in which the cause of the disease is a mutation in the PADI6 gene." [MONDO:patterns/disease_series_by_gene]
-synonym: "PADI6 preimplantation embryonic lethality" EXACT [MONDO:design_pattern, MONDO:patterns/disease_series_by_gene]
-synonym: "preimplantation embryonic lethality 2" EXACT []
-synonym: "preimplantation embryonic lethality 2; PREMBL2" EXACT []
-synonym: "preimplantation embryonic lethality caused by mutation in PADI6" EXACT [MONDO:design_pattern]
-synonym: "preimplantation embryonic lethality type 2" EXACT [MONDO:RULE_1]
-synonym: "PREMBL2" EXACT ABBREVIATION []
-xref: OMIM:617234 {source="MONDO:obsoleteEquivalent"}
-property_value: curated_content_resource "https://www.malacards.org/card/oocyte_zygote_embryo_maturation_arrest_16" xsd:anyURI {source="MONDO:MalaCards"}
-property_value: IAO:0000231 OMO:0001000 {source="MONDO:excludePhenotype"}
+comment: Term replaced by MONDO:1010200 based on user request.
 property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/5091" xsd:anyURI
+property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9855" xsd:anyURI
 is_obsolete: true
-consider: HP:0032479
+replaced_by: MONDO:1010200
 
 [Term]
 id: MONDO:0014979
@@ -636159,6 +636151,22 @@ is_a: MONDO:0005583 {source="OMIA:001081"} ! non-human animal disease
 intersection_of: MONDO:0005583 {source="OMIA:001081"} ! non-human animal disease
 intersection_of: MONDO:0700097 MONDO:0010679 {source="OMIA:001081"} ! cross-species analog Duchenne muscular dystrophy
 
+[Term]
+id: MONDO:1010200
+name: oocyte/zygote/embryo maturation arrest 16
+def: "Any inherited oocyte maturation defect marked by early embryonic arrest and female infertility due to a varition in the PADI6 gene." [https://clinicalgenome.org/affiliation/40106, PMID:27545678, PMID:29693651]
+synonym: "PADI6 preimplantation embryonic lethality" EXACT [MONDO:design_pattern, MONDO:patterns/disease_series_by_gene]
+synonym: "PADI6-related oocyte/zygote/embryo maturation arrest 16 and maternal-effect disorder" EXACT [https://clinicalgenome.org/affiliation/40106] {OMO:0002001="https://w3id.org/information-resource-registry/clingen"}
+synonym: "preimplantation embryonic lethality type 2" EXACT [OMIM:617234]
+synonym: "PREMBL2" EXACT ABBREVIATION [OMIM:617234]
+xref: OMIM:617234 {source="MONDO:equivalentTo"}
+is_a: MONDO:0014769 {source="https://clinicalgenome.org/affiliation/40106"} ! inherited oocyte maturation defect
+intersection_of: MONDO:0014769 ! inherited oocyte maturation defect
+intersection_of: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/20449 ! PADI6
+property_value: curated_content_resource "https://www.malacards.org/card/oocyte_zygote_embryo_maturation_arrest_16" xsd:anyURI {source="MONDO:MalaCards"}
+property_value: http://purl.org/dc/terms/creator https://orcid.org/0000-0002-5002-8648
+property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9855" xsd:anyURI
+
 [Term]
 id: MONDO:1010201
 name: congenital pseudomyotonia, non-human animal

```

## Agent Attempts (6)

| # | Model | Runtime | F1 | P | R | Blob | Eval PR | Detail |
|---|-------|---------|-----|-----|-----|------|---------|--------|
| 1 | claude-sonnet-4.5 | claude | 0.348 | 0.286 | 0.444 | `769001c` | [#467](https://github.com/ai4curation/eval-ont-agent-mondo/pull/467) | [attempt](attempts/pr467.md) |
| 2 | claude-sonnet-4.5 | claude | 0.348 | 0.286 | 0.444 | `769001c` | [#436](https://github.com/ai4curation/eval-ont-agent-mondo/pull/436) | [attempt](attempts/pr436.md) |
| 3 | claude-opus-4.7 | claude | 0.333 | 0.286 | 0.400 | `4f7f0f1` | [#384](https://github.com/ai4curation/eval-ont-agent-mondo/pull/384) | [attempt](attempts/pr384.md) |
| 4 | gpt-5.5 | codex | 0.286 | 0.214 | 0.429 | `59fa801` | [#561](https://github.com/ai4curation/eval-ont-agent-mondo/pull/561) | [attempt](attempts/pr561.md) |
| 5 | claude-sonnet-4.5 | copilot | 0.267 | 0.214 | 0.353 | `562167e` | [#533](https://github.com/ai4curation/eval-ont-agent-mondo/pull/533) | [attempt](attempts/pr533.md) |
| 6 | claude-sonnet-4.5 | copilot | 0.267 | 0.214 | 0.353 | `562167e` | [#493](https://github.com/ai4curation/eval-ont-agent-mondo/pull/493) | [attempt](attempts/pr493.md) |
