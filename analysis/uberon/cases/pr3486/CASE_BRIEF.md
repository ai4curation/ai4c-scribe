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
num_agent_attempts: 11
generated_at: '2026-05-17'
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

## Curation Note (data quality)

`case_quality: poor` — flagged 2026-05-16 by claude-opus-4.7.

PR #3486 is the single, complete human resolution of issue #3354 (a `gh search prs`
for "3354" / "scale circulus" / "future brain vesicle" returns only #3486 — there are
**no companion PRs**, so this is *not* a partial-gold case). The CASE_BRIEF "Human Diff"
matches the true final `gh pr diff` exactly.

The poor-case signature is **gold renegotiated in PR comments**:

- The issue text for the uvea item explicitly says the fix is to remove
  `uvea part_of anterior segment of eyeball`, and that a replacement axiom
  "may not be needed since there is already axiom stating that uvea
  contributes to the morphology of some camera-type eye, which should be enough."
- 7 of 8 agents did exactly this minimal, issue-faithful fix.
- During review, @aleixpuigb noted this loses correct formal definitions for
  `canal of Schlemm` (UBERON:0004029) and `aqueous vein` (UBERON:0004030).
  gouttegd then added a **4th commit** converting
  `contributes_to_morphology_of camera-type eye` → `part_of camera-type eye`.
- Metadiff scores all attempts against this renegotiated final state, which was
  not derivable from the issue. This caps even perfect, issue-faithful attempts
  (sonnet #302, haiku #87) at F1≈0.727 with recall=1.0.

Secondary deflation: attempts #236 (opus), #21 (codex), #151 (gemma) pulled in a
large block of ODK/reserialization CL-import label normalizations (e.g.
`CL:1000271 lung ciliated cell` → `lung multiciliated epithelial cell`,
`CL:0002332`, `CL:1000223`, `CL:0000150`, FMA synonym reorderings) unrelated to
#3354 — the ODK-regenerated-file domination pattern — driving their F1 to 0.20–0.25
despite correct issue work.

Substance assessment (independent of metadiff): #302 and #87 fully and correctly
resolve all three items per the issue as written (success). #58 and #39 also
resolve all three but add unsolicited def/`term_tracker_item` (partial_success,
over-editing). #236 and #21 resolve all three but are dominated by reserialization
noise (partial_success). #151 omits the scale circulus fix entirely
(partial_success, missed requirement). #136 made no real fixes and emitted invalid
OBO (`term_tracker_item UBERON:0001768 3354`) — genuine failure.

Note also several agents' parent choices for `scale circulus` (`crest` UBERON:4200133,
or `anatomical projection` UBERON:0004529) are material projection terms that are
arguably *more informative* than gold's deliberately conservative
`anatomical structure` (UBERON:0000061) — not errors.

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

## Agent Attempts (11)

| # | Model | Runtime | F1 | P | R | Blob | Eval PR | Detail |
|---|-------|---------|-----|-----|-----|------|---------|--------|
| 1 | claude-sonnet-4.5 | claude | 0.727 | 0.571 | 1.000 | `3fd9e7b` | [#302](https://github.com/ai4curation/eval-ont-agent-uberon/pull/302) | [attempt](attempts/pr302.md) |
| 2 | claude-haiku-4.5 | claude | 0.727 | 0.571 | 1.000 | `3fd9e7b` | [#87](https://github.com/ai4curation/eval-ont-agent-uberon/pull/87) | [attempt](attempts/pr87.md) |
| 3 | gpt-5.4 | codex | 0.429 | 0.429 | 0.429 | `ae275d8` | [#388](https://github.com/ai4curation/eval-ont-agent-uberon/pull/388) | [attempt](attempts/pr388.md) |
| 4 | gpt-5.5 | opencode | 0.429 | 0.429 | 0.429 | `bb5e729` | [#58](https://github.com/ai4curation/eval-ont-agent-uberon/pull/58) | [attempt](attempts/pr58.md) |
| 5 | gpt-5.5 | opencode | 0.429 | 0.429 | 0.429 | `bb5e729` | [#39](https://github.com/ai4curation/eval-ont-agent-uberon/pull/39) | [attempt](attempts/pr39.md) |
| 6 | claude-opus-4.7 | claude | 0.250 | 0.429 | 0.176 | `72fa436` | [#236](https://github.com/ai4curation/eval-ont-agent-uberon/pull/236) | [attempt](attempts/pr236.md) |
| 7 | gpt-5.4 | opencode | 0.240 | 0.429 | 0.167 | `e5f6fc0` | [#655](https://github.com/ai4curation/eval-ont-agent-uberon/pull/655) | [attempt](attempts/pr655.md) |
| 8 | gpt-5.4 | opencode | 0.240 | 0.429 | 0.167 | `e5f6fc0` | [#593](https://github.com/ai4curation/eval-ont-agent-uberon/pull/593) | [attempt](attempts/pr593.md) |
| 9 | gpt-5.5 | codex | 0.231 | 0.429 | 0.158 | `12201aa` | [#21](https://github.com/ai4curation/eval-ont-agent-uberon/pull/21) | [attempt](attempts/pr21.md) |
| 10 | gemma-4-31b | opencode | 0.200 | 0.286 | 0.154 | `d3b3ab7` | [#151](https://github.com/ai4curation/eval-ont-agent-uberon/pull/151) | [attempt](attempts/pr151.md) |
| 11 | gemma-4-31b | opencode | 0.000 | 0.000 | 0.000 | `1404836` | [#136](https://github.com/ai4curation/eval-ont-agent-uberon/pull/136) | [attempt](attempts/pr136.md) |
