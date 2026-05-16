---
ontology: mondo
repo: monarch-initiative/mondo
issue_number: 9826
pr_number: 10142
issue_title: '[Merge] short-rib thoracic dysplasia 22 without polydactyly & thoracic
  dysostosis, isolated'
pr_author: MeeSiing
pr_merged_at: '2026-04-08'
task_type: obsoletion
difficulty: simple
scoping: tightly_scoped
scope: single_term
review_outcome: approved_first_time
num_agent_attempts: 9
generated_at: '2026-05-15'
scoping_notes: PR merges one term into another with standard obsoletion of the source
  term.
domain_area: skeletal-disease
best_f1: 0.927
best_model: gpt-5.5
---

# PR #10142 — [Merge] short-rib thoracic dysplasia 22 without polydactyly & thoracic dysostosis, isolated

**mondo** | [monarch-initiative/mondo](https://github.com/monarch-initiative/mondo) | [Issue #9826](https://github.com/monarch-initiative/mondo/issues/9826) | [PR #10142](https://github.com/monarch-initiative/mondo/pull/10142) | @MeeSiing | merged 2026-04-08

`obsoletion` `simple` `tightly_scoped` `approved_first_time`

## Context

MONDO:0008549 "thoracic dysostosis, isolated" and MONDO:0979242 "short-rib thoracic dysplasia 22 without polydactyly" were identified as representing the same disease entity after OMIM merged entry 187750 into 621260. A user request (issue #9826) flagged this redundancy and provided the OMIM provenance for the merge. The task required consolidating the two Mondo terms and obsoleting the duplicate.

## Changes Made

The PR obsoleted MONDO:0008549 and merged its metadata into MONDO:0979242. The 13 additions include obsoletion annotations on the source term (replaced_by pointing to MONDO:0979242) and an added definition for the surviving term. The 9 deletions remove the active classification axioms and synonyms from the obsoleted term. All changes are confined to `src/ontology/mondo-edit.obo`.

## Resolution

Simple difficulty because term merges following OMIM consolidations are well-documented in the Mondo SOP. The curator needs to mark the source term as obsolete, transfer relevant metadata (synonyms, cross-references) to the target term, and add a replaced_by annotation. An agent should be able to handle this given the OMIM provenance and the standard merge pattern.

## Human Diff

```diff
diff --git a/src/ontology/mondo-edit.obo b/src/ontology/mondo-edit.obo
index 8f53dcf303..8d77ce255d 100644
--- a/src/ontology/mondo-edit.obo
+++ b/src/ontology/mondo-edit.obo
@@ -197648,16 +197648,11 @@ is_obsolete: true
 
 [Term]
 id: MONDO:0008549
-name: thoracic dysostosis, isolated
-comment: This term is scheduled to be merged with MONDO:0979242 short-rib thoracic dysplasia 22 without polydactyly, based on the fact that the concept of these 2 terms are the same. This ID will therefore be obsoleted and replaced with MONDO:0979242
-subset: obsoletion_candidate
-synonym: "thoracic dysostosis, isolated" EXACT []
-xref: MESH:C566063 {source="MONDO:equivalentTo"}
-xref: OMIM:187750 {source="MONDO:equivalentObsolete"}
-is_a: MONDO:0003847 {source="https://orcid.org/0000-0001-5208-3432"} ! hereditary disease
-property_value: curated_content_resource "https://www.malacards.org/card/thoracic_dysostosis_isolated" xsd:anyURI {source="MONDO:MalaCards"}
+name: obsolete thoracic dysostosis, isolated
+property_value: IAO:0000231 MONDO:TermsMerged
 property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9826" xsd:anyURI
-property_value: IAO:0006012 "2026-03-01" xsd:string
+is_obsolete: true
+replaced_by: MONDO:0979242
 
 [Term]
 id: MONDO:0008550
@@ -627194,13 +627189,22 @@ relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/
 [Term]
 id: MONDO:0979242
 name: short-rib thoracic dysplasia 22 without polydactyly
+def: "Any Jeune syndrome in which the cause of the disease is a mutation in the FGF4 gene, characterized by a small thorax with short ribs, resulting in pulmonary hypoplasia and respiratory insufficiency." [OMIM:621260]
 subset: gard_rare {source="GARD:0028115", source="MONDO:GARD"}
 subset: omim {source="OMIM:621260"}
 subset: rare
+synonym: "thoracic dysostosis, isolated" EXACT [OMIM:187750]
 xref: GARD:0028115 {source="MONDO:GARD"}
+xref: MESH:C566063 {source="MONDO:equivalentTo"}
+xref: OMIM:187750 {source="MONDO:equivalentObsolete"}
 xref: OMIM:621260 {source="MONDO:equivalentTo"}
+is_a: MONDO:0003847 {source="https://orcid.org/0000-0001-5208-3432"} ! hereditary disease
 is_a: MONDO:0018770 {source="OMIM:621260", source="https://orcid.org/0000-0002-4142-7153"} ! Jeune syndrome
+intersection_of: MONDO:0018770 ! Jeune syndrome
+intersection_of: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/3682 ! FGF4
 relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/3682 {source="OMIM:621260"} ! FGF4
+property_value: curated_content_resource "https://www.malacards.org/card/thoracic_dysostosis_isolated" xsd:anyURI {source="MONDO:MalaCards"}
+property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9826" xsd:anyURI
 
 [Term]
 id: MONDO:0979243

```

## Agent Attempts (9)

| # | Model | Runtime | F1 | P | R | Eval PR | Detail |
|---|-------|---------|-----|-----|-----|---------|--------|
| 1 | gpt-5.5 | codex | 0.927 | 0.864 | 1.000 | [#41](https://github.com/ai4curation/eval-ont-agent-mondo/pull/41) | [attempt](attempts/pr41.md) |
| 2 | gpt-5.5 | opencode | 0.900 | 0.818 | 1.000 | [#81](https://github.com/ai4curation/eval-ont-agent-mondo/pull/81) | [attempt](attempts/pr81.md) |
| 3 | gpt-5.5 | opencode | 0.900 | 0.818 | 1.000 | [#60](https://github.com/ai4curation/eval-ont-agent-mondo/pull/60) | [attempt](attempts/pr60.md) |
| 4 | claude-opus-4.7 | claude | 0.872 | 0.773 | 1.000 | [#393](https://github.com/ai4curation/eval-ont-agent-mondo/pull/393) | [attempt](attempts/pr393.md) |
| 5 | gpt-5.4 | codex | 0.872 | 0.773 | 1.000 | [#164](https://github.com/ai4curation/eval-ont-agent-mondo/pull/164) | [attempt](attempts/pr164.md) |
| 6 | claude-sonnet-4.5 | claude | 0.615 | 0.545 | 0.706 | [#456](https://github.com/ai4curation/eval-ont-agent-mondo/pull/456) | [attempt](attempts/pr456.md) |
| 7 | claude-haiku-4.5 | claude | 0.062 | 0.864 | 0.032 | [#321](https://github.com/ai4curation/eval-ont-agent-mondo/pull/321) | [attempt](attempts/pr321.md) |
| 8 | claude-haiku-4.5 | claude | 0.062 | 0.864 | 0.032 | [#187](https://github.com/ai4curation/eval-ont-agent-mondo/pull/187) | [attempt](attempts/pr187.md) |
| 9 | gemma-4-31b | opencode | 0.001 | 0.727 | 0.000 | [#235](https://github.com/ai4curation/eval-ont-agent-mondo/pull/235) | [attempt](attempts/pr235.md) |
