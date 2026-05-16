---
ontology: uberon
repo: obophenotype/uberon
issue_number: 3478
pr_number: 3479
issue_title: '''late embryo'' connected to effectively vertebrate-specific stages'
pr_author: gouttegd
pr_merged_at: '2025-02-13'
task_type: axiom_repair
difficulty: hard
scoping: tightly_scoped
scope: multi_term
review_outcome: approved_first_time
num_agent_attempts: 7
generated_at: '2026-05-15'
domain_area: developmental-anatomy
best_f1: 0.5
best_model: claude-haiku-4.5
---

# PR #3479 — 'late embryo' connected to effectively vertebrate-specific stages

**uberon** | [obophenotype/uberon](https://github.com/obophenotype/uberon) | [Issue #3478](https://github.com/obophenotype/uberon/issues/3478) | [PR #3479](https://github.com/obophenotype/uberon/pull/3479) | @gouttegd | merged 2025-02-13

`axiom_repair` `hard` `tightly_scoped` `approved_first_time`

## Context

Issue #3478 reported that UBERON:0007220 (late embryonic stage) was connected via a preceded_by axiom to UBERON:0004707 (pharyngula stage), a chordate-specific developmental stage. This made the late embryonic stage effectively vertebrate-specific, which is incorrect since many non-chordate organisms have a late embryonic stage. Additionally, the pharyngula and neurula stages had overly broad taxon restrictions (Eumetazoa) that needed tightening to Chordata.

## Changes Made

The PR made three changes in uberon-edit.obo: (1) narrowed the taxon restriction on pharyngula (UBERON:0004707) and neurula (UBERON:0000110) from Eumetazoa to Chordata; (2) replaced the direct SubClassOf preceded_by pharyngula axiom on late embryonic stage with a GCI (General Class Inclusion) axiom that applies only when the stage occurs in Chordata. This decouples the general late embryonic stage concept from chordate-specific developmental sequences.

## Resolution

Hard difficulty. An agent would need to understand GCI axiom patterns in OBO format, reason about taxon-appropriate developmental stage sequences, and recognize that a general stage concept should not be tied to taxon-specific precursors. The GCI pattern (class AND occurs_in some Taxon SubClassOf preceded_by some Stage) is an advanced OWL modeling technique. Same-day merge reflects the clear rationale provided in the issue.

## Human Diff

```diff
diff --git a/src/ontology/uberon-edit.obo b/src/ontology/uberon-edit.obo
index 36afa06edc..d41f07f57f 100644
--- a/src/ontology/uberon-edit.obo
+++ b/src/ontology/uberon-edit.obo
@@ -2883,13 +2883,13 @@ relationship: simultaneous_with GO:0007369 ! gastrulation
 [Term]
 id: UBERON:0000110
 name: neurula stage
-def: "Staged defined by the formation of a tube from the flat layer of ectodermal cells known as the neural plate. This will give rise to the central nervous system." [GO:0001841]
+def: "A chordate developmental stage defined by the formation of a tube from the flat layer of ectodermal cells known as the neural plate. This will give rise to the central nervous system." [GO:0001841]
 xref: BilaDO:0000009
 xref: BILS:0000110
 xref: XAO:1000006
 is_a: UBERON:0000105 ! life cycle stage
 relationship: dubious_for_taxon NCBITaxon:7955 ! Danio rerio
-relationship: in_taxon NCBITaxon:6072 ! Eumetazoa
+relationship: in_taxon NCBITaxon:7711 ! Chordata
 relationship: part_of UBERON:0000068 ! embryo stage
 relationship: preceded_by UBERON:0000109 ! gastrula stage
 relationship: simultaneous_with GO:0001841 ! neural tube formation
@@ -90615,7 +90615,7 @@ property_value: external_definition "A pear shaped chamber that functions as a c
 [Term]
 id: UBERON:0004707
 name: pharyngula stage
-def: "A stage that follows the blastula, gastrula and neurula stages. At the pharyngula stage, all vertebrate embryos show remarkable similarities." [Wikipedia:Pharyngula]
+def: "A chordate developmental stage that follows the blastula, gastrula and neurula stages. At the pharyngula stage, all vertebrate embryos show remarkable similarities." [Wikipedia:Pharyngula]
 subset: efo_slim
 synonym: "pharyngula" RELATED []
 synonym: "phylotypic stage" EXACT []
@@ -90625,7 +90625,7 @@ xref: OGES:000006
 xref: Wikipedia:Pharyngula
 xref: ZFS:0000050
 is_a: UBERON:0000105 ! life cycle stage
-relationship: in_taxon NCBITaxon:6072 ! Eumetazoa
+relationship: in_taxon NCBITaxon:7711 ! Chordata
 relationship: part_of UBERON:0000111 ! organogenesis stage
 relationship: preceded_by UBERON:0000110 ! neurula stage
 property_value: taxon_notes "Corresponds to E7-E11 in Mouse (Galis et al, TREE, 2001)" xsd:string
@@ -119536,7 +119536,7 @@ is_a: UBERON:0000105 ! life cycle stage
 relationship: part_of UBERON:0000068 ! embryo stage
 relationship: preceded_by RnorDv:0000010 {gci_relation="part_of", gci_filler="NCBITaxon:10116"}
 relationship: preceded_by UBERON:0000111 ! organogenesis stage
-relationship: preceded_by UBERON:0004707 ! pharyngula stage
+relationship: preceded_by UBERON:0004707 {gci_relation="BFO:0000066", gci_filler="NCBITaxon:7711"} ! pharyngula stage
 property_value: seeAlso "https://github.com/obophenotype/uberon/issues/355" xsd:anyURI
 property_value: seeAlso "https://github.com/obophenotype/uberon/issues/565" xsd:anyURI
 

```

## Agent Attempts (7)

| # | Model | Runtime | F1 | P | R | Blob | Eval PR | Detail |
|---|-------|---------|-----|-----|-----|------|---------|--------|
| 1 | claude-haiku-4.5 | claude | 0.500 | 0.375 | 0.750 | `0b7dbb4` | [#336](https://github.com/ai4curation/eval-ont-agent-uberon/pull/336) | [attempt](attempts/pr336.md) |
| 2 | claude-sonnet-4.5 | claude | 0.500 | 0.375 | 0.750 | `0f06ccb` | [#321](https://github.com/ai4curation/eval-ont-agent-uberon/pull/321) | [attempt](attempts/pr321.md) |
| 3 | claude-haiku-4.5 | claude | 0.500 | 0.375 | 0.750 | `0b7dbb4` | [#279](https://github.com/ai4curation/eval-ont-agent-uberon/pull/279) | [attempt](attempts/pr279.md) |
| 4 | gpt-5.5 | codex | 0.462 | 0.375 | 0.600 | `b0be143` | [#20](https://github.com/ai4curation/eval-ont-agent-uberon/pull/20) | [attempt](attempts/pr20.md) |
| 5 | gpt-5.5 | opencode | 0.308 | 0.250 | 0.400 | `be1ace0` | [#57](https://github.com/ai4curation/eval-ont-agent-uberon/pull/57) | [attempt](attempts/pr57.md) |
| 6 | gpt-5.5 | opencode | 0.308 | 0.250 | 0.400 | `be1ace0` | [#38](https://github.com/ai4curation/eval-ont-agent-uberon/pull/38) | [attempt](attempts/pr38.md) |
| 7 | claude-opus-4.7 | claude | 0.273 | 0.375 | 0.214 | `27aed99` | [#234](https://github.com/ai4curation/eval-ont-agent-uberon/pull/234) | [attempt](attempts/pr234.md) |
