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
num_agent_attempts: 10
generated_at: '2026-05-17'
domain_area: developmental-anatomy
best_f1: 0.5
best_model: gpt-5.4
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

## Curation Note (data quality)

Flagged by claude-opus-4.7 on 2026-05-16 after reviewing all 7 attempts.

This is a *genuine, sound* evaluation case — gold PR #3479 is the single, complete
human resolution: approved first time (cmungall APPROVED), merged same day, one
commit, one file, 5+/5-, no companion PRs, and not curator-repudiated. It is NOT
a poor case (not partial, not contaminated, not renegotiated). `case_quality: ok`.

However, two metadiff under-representation effects matter for downstream scoring and
should be applied when interpreting the F1 column:

1. **Issue-vs-PR scope gap (recall cap ~0.5 on top attempts).** Issue #3478's
   explicit proposal has exactly two items: (1) mark neurula stage (UBERON:0000110)
   and pharyngula stage (UBERON:0004707) as `in taxon` some Chordata
   (NCBITaxon:7711); (2) convert the `late embryonic stage` (UBERON:0007220)
   `preceded_by` pharyngula axiom to a GCI scoped to Chordata. The gold PR
   additionally rewrote the *textual definitions* of both neurula and pharyngula to
   begin "A chordate developmental stage ..." — an improvement the PR author added
   ("amend their definition accordingly") that the issue body never requested. All
   seven agents performed both explicit issue asks correctly but none made the
   unrequested def rewrites, so every well-scoped attempt is capped near F1=0.50 by
   two def lines that were not part of the stated task.

2. **GCI-relation surface penalty.** The gold encodes the GCI as
   `gci_relation="BFO:0000066"` (the IRI form of `occurs in`, exactly the issue's
   proposal). Attempts using the equivalent label form `occurs_in` (pr336/pr279) or
   the defensible same-stanza-consistent `part_of` (pr321/pr234, mirroring the
   pre-existing `RnorDv:0000010 {gci_relation="part_of"}` GCI on the very same term)
   are surface-penalized though semantically correct for the
   taxon-constraint-propagation goal the issue targets. (`in_taxon` as the GCI
   differentia in pr20/pr57/pr38 is a genuinely weaker/different model and a fair
   penalty.)

3. **pr234 robot-reserialization over-edit (not contamination).** The lowest-F1
   attempt (pr234, opus-4.7, F1 0.273) is the best-reasoned but was dragged down by
   ~10 unrelated CL label-refresh lines (CL:1000271, CL:0002145, CL:0002332,
   CL:1000223, CL:0000150) that `robot convert` re-synced from a newer merged CL
   import. Verified this hunk appears ONLY in pr234, not in the other six attempts —
   so it is an ODK/robot whole-file reserialization artifact specific to that run,
   NOT eval-base contamination and NOT a gold-leakage effect.

Recommendation: when aggregating, treat the top tier (pr336, pr279; then pr321) as
substantively successful on the issue's explicit asks despite F1≈0.50, and read the
F1 column as under-representing quality for the claude-runtime attempts.

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

## Agent Attempts (10)

| # | Model | Runtime | F1 | P | R | Blob | Eval PR | Detail |
|---|-------|---------|-----|-----|-----|------|---------|--------|
| 1 | gpt-5.4 | opencode | 0.500 | 0.375 | 0.750 | `d70acc6` | [#649](https://github.com/ai4curation/eval-ont-agent-uberon/pull/649) | [attempt](attempts/pr649.md) |
| 2 | gpt-5.4 | opencode | 0.500 | 0.375 | 0.750 | `d70acc6` | [#592](https://github.com/ai4curation/eval-ont-agent-uberon/pull/592) | [attempt](attempts/pr592.md) |
| 3 | claude-haiku-4.5 | claude | 0.500 | 0.375 | 0.750 | `0b7dbb4` | [#336](https://github.com/ai4curation/eval-ont-agent-uberon/pull/336) | [attempt](attempts/pr336.md) |
| 4 | claude-sonnet-4.5 | claude | 0.500 | 0.375 | 0.750 | `0f06ccb` | [#321](https://github.com/ai4curation/eval-ont-agent-uberon/pull/321) | [attempt](attempts/pr321.md) |
| 5 | claude-haiku-4.5 | claude | 0.500 | 0.375 | 0.750 | `0b7dbb4` | [#279](https://github.com/ai4curation/eval-ont-agent-uberon/pull/279) | [attempt](attempts/pr279.md) |
| 6 | gpt-5.4 | codex | 0.462 | 0.375 | 0.600 | `7802ace` | [#417](https://github.com/ai4curation/eval-ont-agent-uberon/pull/417) | [attempt](attempts/pr417.md) |
| 7 | gpt-5.5 | codex | 0.462 | 0.375 | 0.600 | `b0be143` | [#20](https://github.com/ai4curation/eval-ont-agent-uberon/pull/20) | [attempt](attempts/pr20.md) |
| 8 | gpt-5.5 | opencode | 0.308 | 0.250 | 0.400 | `be1ace0` | [#57](https://github.com/ai4curation/eval-ont-agent-uberon/pull/57) | [attempt](attempts/pr57.md) |
| 9 | gpt-5.5 | opencode | 0.308 | 0.250 | 0.400 | `be1ace0` | [#38](https://github.com/ai4curation/eval-ont-agent-uberon/pull/38) | [attempt](attempts/pr38.md) |
| 10 | claude-opus-4.7 | claude | 0.273 | 0.375 | 0.214 | `27aed99` | [#234](https://github.com/ai4curation/eval-ont-agent-uberon/pull/234) | [attempt](attempts/pr234.md) |
