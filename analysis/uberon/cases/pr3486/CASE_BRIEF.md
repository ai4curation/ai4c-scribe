---
ontology: uberon
repo: obophenotype/uberon
issue_number: 3354
pr_number: 3486
issue_title: 'ZFA/Uberon issues: simple errors in Uberon'
pr_author: gouttegd
pr_merged_at: '2025-03-06'
task_type: axiom_repair
difficulty: hard
scoping: tightly_scoped
scope: multi_term
review_outcome: approved_first_time
num_agent_attempts: 8
generated_at: '2026-05-15'
domain_area: cross-species-anatomy
best_f1: 0.727
best_model: claude-sonnet-4.5
---

# PR #3486 — ZFA/Uberon issues: simple errors in Uberon

**uberon** | [obophenotype/uberon](https://github.com/obophenotype/uberon) | [Issue #3354](https://github.com/obophenotype/uberon/issues/3354) | [PR #3486](https://github.com/obophenotype/uberon/pull/3486) | @gouttegd | merged 2025-03-06

`axiom_repair` `hard` `tightly_scoped` `approved_first_time`

## Context

Issue #3354 reported three incompatibility issues between Uberon and ZFA (Zebrafish Anatomy Ontology). First, UBERON:0001768 (uvea) was incorrectly asserted as part_of the anterior segment of eyeball, but the uvea spans both anterior and posterior segments. Second, UBERON:0013150 (future brain vesicle) was incorrectly classified as an immaterial open anatomical space, inconsistent with its child terms (brain ventricles) being material structures. Third, UBERON:2002051 (scale circulus) was incorrectly classified as an immaterial anatomical line, when ZFA and published literature indicate circuli are material structures.

## Changes Made

The PR made three targeted corrections in uberon-edit.obo: removed the incorrect part_of axiom linking uvea to the anterior segment, reclassified future brain vesicle from immaterial to material entity, and reclassified scale circulus from anatomical line to a material structure. Each fix required independent anatomical reasoning supported by literature references.

## Resolution

Hard difficulty despite the small diff (3 additions, 4 deletions). An agent would need to reason about anatomical spatial relationships (uvea spanning anterior and posterior eye segments), ontological materiality distinctions (BFO material vs immaterial entities), and cross-species consistency with ZFA. Each of the three fixes requires independent domain knowledge and careful consideration of downstream inference impacts.

## Human Diff

```diff
diff --git a/src/ontology/uberon-edit.obo b/src/ontology/uberon-edit.obo
index d41f07f57f..bdb0f1896e 100644
--- a/src/ontology/uberon-edit.obo
+++ b/src/ontology/uberon-edit.obo
@@ -30590,11 +30590,10 @@ xref: SCTID:280648000
 xref: UMLS:C0042160 {source="ncithesaurus:Uvea"}
 xref: Wikipedia:Uvea
 is_a: UBERON:0004923 {source="FMA"} ! organ component layer
-relationship: contributes_to_morphology_of UBERON:0000019 ! camera-type eye
 relationship: has_part UBERON:0001769 ! iris
 relationship: has_part UBERON:0001775 ! ciliary body
 relationship: has_part UBERON:0001776 ! optic choroid
-relationship: part_of UBERON:0001801 ! anterior segment of eyeball
+relationship: part_of UBERON:0000019 ! camera-type eye
 relationship: present_in_taxon NCBITaxon:7955 {source="DOI:10.1177/0192623311409597"} ! Danio rerio
 property_value: depiction "http://upload.wikimedia.org/wikipedia/commons/e/eb/Gray869.png" xsd:anyURI
 property_value: editor_note "TODO - check child terms, isa vs partof. See also MA:0001284 ! tunica vasculosa plexus" xsd:string
@@ -154068,7 +154067,7 @@ synonym: "secondary brain vesicle" NARROW []
 xref: NCIT:C34259
 xref: neuronames:2499
 xref: SCTID:360409004
-is_a: UBERON:0010064 {source="EHDAA2"} ! open anatomical space
+is_a: UBERON:0010000 ! multicellular anatomical structure
 relationship: part_of UBERON:0000922 ! embryo
 relationship: part_of UBERON:0005281 {source="EHDAA2"} ! ventricular system of central nervous system
 relationship: part_of UBERON:0006238 ! future brain
@@ -201997,7 +201996,7 @@ def: "Fine ridge on surface of scale, often parallel to the circumference of sca
 synonym: "circuli" EXACT OMO:0003004 [TAO:0002051]
 synonym: "crétule" EXACT [PSPUB:0000149]
 xref: ZFA:0005499
-is_a: UBERON:0006800 ! anatomical line
+is_a: UBERON:0000061 ! anatomical structure
 relationship: part_of UBERON:0007380 ! dermal scale
 property_value: provenance_notes "This class was sourced from an external ontology (teleost_anatomy). Its definitions, naming conventions and relationships may need to be checked for compatibility with uberon" xsd:string {source="http://purl.obolibrary.org/obo/tao.owl"}
 

```

## Agent Attempts (8)

| # | Model | Runtime | F1 | P | R | Eval PR | Detail |
|---|-------|---------|-----|-----|-----|---------|--------|
| 1 | claude-sonnet-4.5 | claude | 0.727 | 0.571 | 1.000 | [#302](https://github.com/ai4curation/eval-ont-agent-uberon/pull/302) | [attempt](attempts/pr302.md) |
| 2 | claude-haiku-4.5 | claude | 0.727 | 0.571 | 1.000 | [#87](https://github.com/ai4curation/eval-ont-agent-uberon/pull/87) | [attempt](attempts/pr87.md) |
| 3 | gpt-5.5 | opencode | 0.429 | 0.429 | 0.429 | [#58](https://github.com/ai4curation/eval-ont-agent-uberon/pull/58) | [attempt](attempts/pr58.md) |
| 4 | gpt-5.5 | opencode | 0.429 | 0.429 | 0.429 | [#39](https://github.com/ai4curation/eval-ont-agent-uberon/pull/39) | [attempt](attempts/pr39.md) |
| 5 | claude-opus-4.7 | claude | 0.250 | 0.429 | 0.176 | [#236](https://github.com/ai4curation/eval-ont-agent-uberon/pull/236) | [attempt](attempts/pr236.md) |
| 6 | gpt-5.5 | codex | 0.231 | 0.429 | 0.158 | [#21](https://github.com/ai4curation/eval-ont-agent-uberon/pull/21) | [attempt](attempts/pr21.md) |
| 7 | gemma-4-31b | opencode | 0.200 | 0.286 | 0.154 | [#151](https://github.com/ai4curation/eval-ont-agent-uberon/pull/151) | [attempt](attempts/pr151.md) |
| 8 | gemma-4-31b | opencode | 0.000 | 0.000 | 0.000 | [#136](https://github.com/ai4curation/eval-ont-agent-uberon/pull/136) | [attempt](attempts/pr136.md) |
