---
ontology: uberon
repo: obophenotype/uberon
issue_number: 3522
pr_number: 3525
issue_title: relationship is reversed between Uberon and NCIT for foramen secundum
pr_author: rays22
pr_merged_at: '2025-05-27'
task_type: axiom_repair
difficulty: medium
scoping: tightly_scoped
scope: multi_term
review_outcome: approved_first_time
num_agent_attempts: 8
generated_at: '2026-05-15'
domain_area: cardiac-anatomy
best_f1: 0.364
best_model: claude-haiku-4.5
---

# PR #3525 — relationship is reversed between Uberon and NCIT for foramen secundum

**uberon** | [obophenotype/uberon](https://github.com/obophenotype/uberon) | [Issue #3522](https://github.com/obophenotype/uberon/issues/3522) | [PR #3525](https://github.com/obophenotype/uberon/pull/3525) | @rays22 | merged 2025-05-27

`axiom_repair` `medium` `tightly_scoped` `approved_first_time`

## Context

Issue #3522 reported that the logical definition (equivalence axiom) for foramen secundum (UBERON:0006678) was reversed relative to NCIT, and that foramen primum (UBERON:0009149) had a non-unique equivalence axiom that could cause reasoning errors. Both terms relate to openings in the interatrial septum during cardiac development.

## Changes Made

For UBERON:0009149 (foramen primum), the non-unique equivalence axiom was replaced with two explicit subclass assertions. For UBERON:0006678 (foramen secundum), the incorrect equivalence axiom was similarly replaced with subclass assertions, and the text definition was corrected. The changes totaled 5 additions and 5 deletions in uberon-edit.obo.

## Resolution

Medium difficulty. An agent would need to understand the difference between equivalence axioms and subclass assertions in OBO/OWL, recognize when an equivalence axiom is non-unique or incorrect, and have sufficient cardiac embryology knowledge to verify the corrected relationships between foramen primum, foramen secundum, and the interatrial septum. Merged after twelve days with no changes requested.

## Human Diff

```diff
diff --git a/src/ontology/uberon-edit.obo b/src/ontology/uberon-edit.obo
index d1d6c46d4a..61c8ce1465 100644
--- a/src/ontology/uberon-edit.obo
+++ b/src/ontology/uberon-edit.obo
@@ -114747,7 +114747,7 @@ intersection_of: bounding_layer_of UBERON:0000483 ! epithelium
 [Term]
 id: UBERON:0006678
 name: foramen secundum
-def: "A foramen in the septum secundum." [Wikipedia:Foramen_secundum]
+def: "The foramen secundum is an opening in the septum primum, a precursor to the interatrial septum of the human heart. It is formed at a later developmental stage than the foramen primum. Its location is also different relative to the site of the foramen primum in the septum primum." [Wikipedia:Foramen_secundum]
 synonym: "foramen secundum" RELATED OMO:0003011 [Wikipedia:Foramen_secundum]
 synonym: "ostium secundum" EXACT OMO:0003011 [VHOG:0001471]
 xref: EHDAA2:0001828
@@ -114758,8 +114758,8 @@ xref: SCTID:308854001
 xref: UMLS:C1517293 {source="ncithesaurus:Foramen_Secundum"}
 xref: VHOG:0001471
 xref: Wikipedia:Foramen_secundum
-intersection_of: UBERON:0004111 ! anatomical conduit
-intersection_of: part_of UBERON:0004155 ! atrial septum secundum
+is_a: UBERON:0004111 ! anatomical conduit
+relationship: part_of UBERON:0004154 ! atrial septum primum
 property_value: external_definition "Second of the two openings to perforate the septum primum between the two atria of the embryonic heart. [TFD][VHOG]" xsd:string {date_retrieved="2012-09-17", external_class="VHOG:0001471", ontology="VHOG", source="http://bgee.unil.ch/", source="http://medical-dictionary.thefreedictionary.com/foramen"}
 property_value: homology_notes "The tetrapod clade develops a complete atrial septum and loses the fifth aortic arch altogether. [ISBN:978-0030223693 Liem KF, Bemis WE, Walker WF, Grande L, Functional Anatomy of the Vertebrates: An Evolutionary Perspective (2001) p.620]; [about heart development] In the various tetrapod classes ontogenetic events essentially recapitulate the phylogenetic stages.[well established][VHOG]" xsd:string {date_retrieved="2012-09-17", external_class="VHOG:0001471", ontology="VHOG", source="ISBN:978-0721676678 p.433", source="http://bgee.unil.ch/"}
 
@@ -130525,8 +130525,8 @@ xref: SCTID:308852002
 xref: UMLS:C1517292 {source="ncithesaurus:Foramen_Primum"}
 xref: VHOG:0001470
 xref: Wikipedia:Primary_interatrial_foramen
-intersection_of: UBERON:0004111 ! anatomical conduit
-intersection_of: part_of UBERON:0004154 ! atrial septum primum
+is_a: UBERON:0004111 ! anatomical conduit
+relationship: part_of UBERON:0004154 ! atrial septum primum
 property_value: external_definition "First of the two openings to perforate the septum primum between the two atria of the embryonic heart. [TFD][VHOG]" xsd:string {date_retrieved="2012-09-17", external_class="VHOG:0001470", ontology="VHOG", source="http://bgee.unil.ch/", source="http://medical-dictionary.thefreedictionary.com/foramen"}
 property_value: homology_notes "The tetrapod clade develops a complete atrial septum and loses the fifth aortic arch altogether. [ISBN:978-0030223693 Liem KF, Bemis WE, Walker WF, Grande L, Functional Anatomy of the Vertebrates: An Evolutionary Perspective (2001) p.620]; [about heart development] In the various tetrapod classes ontogenetic events essentially recapitulate the phylogenetic stages.[well established][VHOG]" xsd:string {date_retrieved="2012-09-17", external_class="VHOG:0001470", ontology="VHOG", source="ISBN:978-0721676678 p.433", source="http://bgee.unil.ch/"}
 

```

## Agent Attempts (8)

| # | Model | Runtime | F1 | P | R | Eval PR | Detail |
|---|-------|---------|-----|-----|-----|---------|--------|
| 1 | claude-haiku-4.5 | claude | 0.364 | 0.286 | 0.500 | [#329](https://github.com/ai4curation/eval-ont-agent-uberon/pull/329) | [attempt](attempts/pr329.md) |
| 2 | claude-haiku-4.5 | claude | 0.364 | 0.286 | 0.500 | [#273](https://github.com/ai4curation/eval-ont-agent-uberon/pull/273) | [attempt](attempts/pr273.md) |
| 3 | gemma-4-31b | opencode | 0.364 | 0.286 | 0.500 | [#111](https://github.com/ai4curation/eval-ont-agent-uberon/pull/111) | [attempt](attempts/pr111.md) |
| 4 | claude-sonnet-4.5 | claude | 0.333 | 0.286 | 0.400 | [#294](https://github.com/ai4curation/eval-ont-agent-uberon/pull/294) | [attempt](attempts/pr294.md) |
| 5 | claude-opus-4.7 | claude | 0.286 | 0.286 | 0.286 | [#244](https://github.com/ai4curation/eval-ont-agent-uberon/pull/244) | [attempt](attempts/pr244.md) |
| 6 | gpt-5.5 | opencode | 0.286 | 0.286 | 0.286 | [#65](https://github.com/ai4curation/eval-ont-agent-uberon/pull/65) | [attempt](attempts/pr65.md) |
| 7 | gpt-5.5 | opencode | 0.286 | 0.286 | 0.286 | [#47](https://github.com/ai4curation/eval-ont-agent-uberon/pull/47) | [attempt](attempts/pr47.md) |
| 8 | gpt-5.5 | codex | 0.286 | 0.286 | 0.286 | [#26](https://github.com/ai4curation/eval-ont-agent-uberon/pull/26) | [attempt](attempts/pr26.md) |
