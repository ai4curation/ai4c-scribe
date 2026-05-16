# PR #31968 — Reparent 49 EC:1.14.14.x terms from GO:0016709 to GO:0016712 (CYP450 reclassification)

- **Ontology**: go-ontology
- **Repo**: geneontology/go-ontology
- **Issue**: [#31967](https://github.com/geneontology/go-ontology/issues/31967)
- **PR**: [#31968](https://github.com/geneontology/go-ontology/pull/31968)
- **Author**: @sjm41
- **Merged**: 2026-04-24
- **task_type**: reclassification
- **difficulty**: medium
- **scoping**: tightly_scoped
- **scope**: structural_refactor
- **review_outcome**: approved_first_time
- **scoping_notes**: Every change is a reparent of an EC:1.14.14.x term from GO:0016709 to GO:0016712, plus term_tracker_item provenance additions. No unrelated edits.

## Context

All GO terms corresponding to EC:1.14.14.x (cytochrome P450 monooxygenases) were incorrectly classified under GO:0016709 ("oxidoreductase activity, acting on paired donors, with NAD(P)H as one donor"). These enzymes actually use a reduced flavin/flavoprotein as electron donor, so the correct parent is GO:0016712 ("oxidoreductase activity, acting on paired donors, with reduced flavin or flavoprotein as one donor").

The key insight: CYP450 enzymes receive electrons from NADPH *indirectly* via cytochrome P450 reductase (a flavoprotein). The GO hierarchy classifies by the *immediate* electron donor to the catalytic site, which is the flavoprotein, not NADPH itself.

## Changes Made

In `src/ontology/go-edit.obo` (56 additions, 7 deletions):

**Bulk reparent** of 49 terms, each following the same pattern:
```
-is_a: GO:0016709 ! ... NAD(P)H as one donor ...
+is_a: GO:0016712 ! ... reduced flavin or flavoprotein as one donor ...
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31967" xsd:anyURI
```

Example terms affected:
- GO:0004506 (squalene monooxygenase) — EC:1.14.14.17
- GO:0008398 (sterol 14-demethylase) — EC:1.14.14.154
- GO:0010283 (4-coumarate 3-hydroxylase) — EC:1.14.14.91
- GO:0016711 (flavonoid 3'-monooxygenase) — EC:1.14.14.82
- GO:0018664 (benzoate 4-monooxygenase) — EC:1.14.14.93
- Plus ~44 more CYP450-related terms

## Resolution

Medium difficulty: the reasoning (identify correct parent based on electron donor mechanism) requires enzyme biochemistry knowledge, but once determined, the edit is repetitive. An agent would need to:
1. Understand the EC:1.14.14 -> flavoprotein donor mapping
2. Identify all affected terms (those with EC:1.14.14.x xrefs currently under GO:0016709)
3. Apply the bulk reparent mechanically

Same-day turnaround (issue opened and PR merged on 2026-04-24). Approved without changes because the reasoning was clear and the edit was mechanical.

## Human Diff

```diff
diff --git a/src/ontology/go-edit.obo b/src/ontology/go-edit.obo
index 6dd226998..b2469c260 100644
--- a/src/ontology/go-edit.obo
+++ b/src/ontology/go-edit.obo
@@ -43251,8 +43251,9 @@ xref: EC:1.14.14.17 {source="skos:exactMatch"}
 xref: KEGG_REACTION:R02874
 xref: MetaCyc:SQUALENE-MONOOXYGENASE-RXN
 xref: RHEA:25282 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31967" xsd:anyURI
 
 [Term]
 id: GO:0004507
@@ -80692,10 +80693,11 @@ xref: RHEA:25286 {source="skos:narrowMatch"}
 xref: RHEA:45960 {source="skos:narrowMatch"}
 xref: RHEA:54028 {source="skos:exactMatch"}
 xref: RHEA:75439 {source="skos:narrowMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 is_a: GO:0032451 ! demethylase activity
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/22523" xsd:anyURI
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31967" xsd:anyURI
 
 [Term]
 id: GO:0008399
@@ -102582,8 +102584,9 @@ xref: EC:1.14.14.137 {source="skos:exactMatch"}
 xref: KEGG_REACTION:R07202
 xref: MetaCyc:1.14.13.93-RXN
 xref: RHEA:12897 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31967" xsd:anyURI
 
 [Term]
 id: GO:0010296
@@ -127768,8 +127771,9 @@ synonym: "trans-cinnamic acid 4-hydroxylase activity" RELATED [EC:1.14.14.91]
 xref: EC:1.14.14.91 {source="skos:exactMatch"}
 xref: MetaCyc:TRANS-CINNAMATE-4-MONOOXYGENASE-RXN
 xref: RHEA:10608 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31967" xsd:anyURI
 
 [Term]
 id: GO:0016711
@@ -127788,8 +127792,9 @@ xref: RHEA:61096 {source="skos:narrowMatch"}
 xref: RHEA:61112 {source="skos:narrowMatch"}
 xref: RHEA:61124 {source="skos:narrowMatch"}
 xref: RHEA:79895 {source="skos:narrowMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31967" xsd:anyURI
 
 [Term]
 id: GO:0016712
@@ -139312,8 +139317,9 @@ xref: KEGG_REACTION:R01295
 xref: MetaCyc:BENZOATE-4-MONOOXYGENASE-RXN
 xref: RHEA:18033 {source="skos:exactMatch"}
 xref: UM-BBD_reactionID:r0623
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31967" xsd:anyURI
 
 [Term]
 id: GO:0018665
@@ -201756,8 +201762,9 @@ xref: RHEA:55448 {source="skos:exactMatch"}
 xref: RHEA:61104 {source="skos:narrowMatch"}
 xref: RHEA:61108 {source="skos:narrowMatch"}
 xref: RHEA:61120 {source="skos:narrowMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/28526" xsd:anyURI
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31967" xsd:anyURI
 
 [Term]
 id: GO:0033773
@@ -201797,8 +201804,9 @@ xref: EC:1.14.14.136 {source="skos:exactMatch"}
 xref: KEGG_REACTION:R05828
 xref: MetaCyc:1.14.13.91-RXN
 xref: RHEA:14237 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31967" xsd:anyURI
 
 [Term]
 id: GO:0033776
@@ -201828,8 +201836,9 @@ xref: EC:1.14.14.138 {source="skos:exactMatch"}
 xref: KEGG_REACTION:R07203
 xref: MetaCyc:1.14.13.94-RXN
 xref: RHEA:18857 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31967" xsd:anyURI
 
 [Term]
 id: GO:0033778
@@ -201886,8 +201895,9 @@ xref: EC:1.14.14.25 {source="skos:exactMatch"}
 xref: KEGG_REACTION:R07207
 xref: MetaCyc:1.14.13.98-RXN
 xref: RHEA:22716 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31967" xsd:anyURI
 
 [Term]
 id: GO:0033782
@@ -228574,8 +228584,9 @@ xref: EC:1.14.14.144 {source="skos:exactMatch"}
 xref: KEGG_REACTION:R06351
 xref: MetaCyc:RXN-8507
 xref: RHEA:26217 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31967" xsd:anyURI
 created_by: bf
 creation_date: 2012-04-19T10:57:05Z
 
@@ -228735,8 +228746,9 @@ def: "Catalysis of the reaction: ent-isokaurene + O2 + NADPH + H+ = ent-2alpha-h
 xref: EC:1.14.14.76 {source="skos:exactMatch"}
 xref: KEGG_REACTION:R09861
 xref: RHEA:56336 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31967" xsd:anyURI
 created_by: bf
 creation_date: 2012-04-20T02:21:33Z
 
@@ -228749,8 +228761,9 @@ synonym: "ent-cassadiene C11alpha-hydroxylase activity" RELATED [EC:1.14.14.112]
 xref: EC:1.14.14.112 {source="skos:exactMatch"}
 xref: KEGG_REACTION:R09866
 xref: RHEA:31967 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31967" xsd:anyURI
 created_by: bf
 creation_date: 2012-04-20T02:34:13Z
 
@@ -228776,8 +228789,9 @@ xref: EC:1.14.14.145 {source="skos:exactMatch"}
 xref: KEGG_REACTION:R06354
 xref: MetaCyc:RXN-12799
 xref: RHEA:26221 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31967" xsd:anyURI
 created_by: bf
 creation_date: 2012-04-24T02:37:15Z
 
@@ -228848,9 +228862,10 @@ xref: EC:1.14.14.111 {source="skos:exactMatch"}
 xref: KEGG_REACTION:R09865
 xref: MetaCyc:RXN-15437
 xref: RHEA:31951 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/21412" xsd:anyURI
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31967" xsd:anyURI
 created_by: bf
 creation_date: 2012-04-25T11:11:55Z
 
@@ -291822,8 +291837,9 @@ xref: EC:1.14.14.93 {source="skos:exactMatch"}
 xref: KEGG_REACTION:R03452
 xref: MetaCyc:RXN-4505
 xref: RHEA:15321 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31967" xsd:anyURI
 
 [Term]
 id: GO:0047083
@@ -291836,8 +291852,9 @@ synonym: "trans-5-O-(4-coumaroyl)-D-quinate,NADPH:oxygen oxidoreductase (3'-hydr
 xref: EC:1.14.14.96 {source="skos:exactMatch"}
 xref: MetaCyc:1.14.13.36-RXN
 xref: RHEA:16265 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31967" xsd:anyURI
 
 [Term]
 id: GO:0047084
@@ -291851,8 +291868,9 @@ synonym: "methyltetrahydroprotoberberine 14-hydroxylase activity" EXACT []
 xref: EC:1.14.14.97 {source="skos:exactMatch"}
 xref: MetaCyc:1.14.13.37-RXN
 xref: RHEA:23684 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
... (348 more lines truncated)
```

## Agent Attempts (11)

### Attempt 1: gpt-5.5 / opencode

- **Eval PR**: [#98](https://github.com/ai4curation/eval-ont-agent-go/pull/98)
- **F1**: 1.000  **Precision**: 1.000  **Recall**: 1.000  **Jaccard**: 1.000
- **Trace**: [25615946252](https://github.com/ai4curation/eval-ont-agent-go/tree/master/traces/25615946252)
- **Workflow run**: [25615946252](https://github.com/ai4curation/eval-ont-agent-go/actions/runs/25615946252)

#### Agent PR Comment

## Summary

Addresses geneontology/go-ontology issue #31967.

Changes made in `src/ontology/go-edit.obo`:

- Reparented all 49 listed `EC:1.14.14.x` molecular function terms from:
  - `GO:0016709` oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen (`EC:1.14.13.-`)
- to:
  - `GO:0016712` oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen (`EC:1.14.14.-`)
- Added `property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31967" xsd:anyURI` to each edited term.

Rationale: the affected terms all carry exact EC xrefs in `EC:1.14.14.x`, while their asserted parent was the GO grouping term mapped to `EC:1.14.13.-`. Reparenting them to the existing `EC:1.14.14.-` GO grouping term aligns the GO asserted hierarchy with the EC hierarchy and existing GO precedent for other `EC:1.14.14.x` monooxygenase terms.

## Validation

- Pre-validation: `cd src/ontology && make travis_build` passed before edits.
- Post-edit validation: `cd src/ontology && make travis_build` passed after edits.
- Additional spot check: confirmed each of the 49 requested terms now has `is_a: GO:0016712`, no longer has direct `is_a: GO:0016709`, and has the issue #31967 term tracker entry.

## Checklist

- [x] PLAN: Issue context was reviewed; intent was clear: correct the EC hierarchy parent for 49 `EC:1.14.14.x` terms.
- [x] PRE-VALIDATION: Current ontology validated successfully before changes using `make travis_build`.
- [x] RESEARCH: N/A; no new biological claims, definitions, or references were introduced. The change follows the EC xrefs and existing GO EC grouping term.
- [x] TERM-SEARCH: Relevant GO parent terms and affected terms were checked in `src/ontology/go-edit.obo` using `obo-grep.pl`.
- [x] DESIGN-PATTERNS: Reviewed applicable pattern considerations for EC-organized molecular function catalytic activity terms; no logical definitions were added.
- [x] EDITS: Used `obo-checkout.pl` / term files under `terms/` / `obo-checkin.pl`; did not directly hand-edit the large ontology file.
- [x] RELATIONSHIPS: Replaced direct asserted `is_a: GO:0016709` with `is_a: GO:0016712` for each affected term; retained any other existing asserted parents.
  - [x] Logical definitions: N/A; no `intersection_of` axioms were added or changed.
  - [x] Relationships conform to similar `EC:1.14.14.x` terms already under `GO:0016712`.
  - [x] `is_a` was not over-asserted beyond the requested EC grouping correction.
- [x] SPECIALIZED-EDITS: Reaction/catalytic activity guidance was consulted because the terms are EC-linked molecular functions.
  - [x] Term obsoletion: N/A.
  - [x] Chemical entity: N/A; no CHEBI-linked content was edited.
  - [x] Reaction: Applied; EC hierarchy alignment checked.
  - [x] Taxon constraints: N/A.
- [x] METADATA: Added issue #31967 `term_tracker_item` metadata to edited terms; no `created_by` or `creation_date` added because these are existing terms.
- [x] AUTOMATED-VALIDATION: `make travis_build` passed after edits.
- [x] REFERENCE-VALIDATION: N/A; no new PMIDs or definition references were introduced.
- [x] CHANGES-COMMITTED: Changes committed locally.
  - [x] RELEVANT-FILES: Only `src/ontology/go-edit.obo` was committed.
  - [x] ACCURACY: Changes align exact EC `1.14.14.x` xrefs with the EC `1.14.14.-` GO parent.
  - [x] ISSUE-ALIGNMENT: The requested 49 terms were updated as specified.

---
🤖 **Generated by pi agent**
- Runtime: `pi`
- Model: `openai/gpt-5.5`
- Agent config: `ai4curation/go-ontology-agent-config@v9:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-go/actions/runs/25615946252)


#### Agent Issue Comment

Changes committed in PR #<NN>.

Summary: the 49 listed `EC:1.14.14.x` monooxygenase activity terms have been reparented from `GO:0016709` (`EC:1.14.13.-`) to `GO:0016712` (`EC:1.14.14.-`). I also added issue #31967 as term tracker metadata on the edited terms.

Validation completed with `cd src/ontology && make travis_build`.

---
🤖 **Generated by pi agent**
- Runtime: `pi`
- Model: `openai/gpt-5.5`
- Agent config: `ai4curation/go-ontology-agent-config@v9:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-go/actions/runs/25615946252)


#### Agent Diff

```diff
diff --git a/src/ontology/go-edit.obo b/src/ontology/go-edit.obo
index 6dd226998..b2469c260 100644
--- a/src/ontology/go-edit.obo
+++ b/src/ontology/go-edit.obo
@@ -43251,8 +43251,9 @@ xref: EC:1.14.14.17 {source="skos:exactMatch"}
 xref: KEGG_REACTION:R02874
 xref: MetaCyc:SQUALENE-MONOOXYGENASE-RXN
 xref: RHEA:25282 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31967" xsd:anyURI
 
 [Term]
 id: GO:0004507
@@ -80692,10 +80693,11 @@ xref: RHEA:25286 {source="skos:narrowMatch"}
 xref: RHEA:45960 {source="skos:narrowMatch"}
 xref: RHEA:54028 {source="skos:exactMatch"}
 xref: RHEA:75439 {source="skos:narrowMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 is_a: GO:0032451 ! demethylase activity
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/22523" xsd:anyURI
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31967" xsd:anyURI
 
 [Term]
 id: GO:0008399
@@ -102582,8 +102584,9 @@ xref: EC:1.14.14.137 {source="skos:exactMatch"}
 xref: KEGG_REACTION:R07202
 xref: MetaCyc:1.14.13.93-RXN
 xref: RHEA:12897 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31967" xsd:anyURI
 
 [Term]
 id: GO:0010296
@@ -127768,8 +127771,9 @@ synonym: "trans-cinnamic acid 4-hydroxylase activity" RELATED [EC:1.14.14.91]
 xref: EC:1.14.14.91 {source="skos:exactMatch"}
 xref: MetaCyc:TRANS-CINNAMATE-4-MONOOXYGENASE-RXN
 xref: RHEA:10608 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31967" xsd:anyURI
 
 [Term]
 id: GO:0016711
@@ -127788,8 +127792,9 @@ xref: RHEA:61096 {source="skos:narrowMatch"}
 xref: RHEA:61112 {source="skos:narrowMatch"}
 xref: RHEA:61124 {source="skos:narrowMatch"}
 xref: RHEA:79895 {source="skos:narrowMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31967" xsd:anyURI
 
 [Term]
 id: GO:0016712
@@ -139312,8 +139317,9 @@ xref: KEGG_REACTION:R01295
 xref: MetaCyc:BENZOATE-4-MONOOXYGENASE-RXN
 xref: RHEA:18033 {source="skos:exactMatch"}
 xref: UM-BBD_reactionID:r0623
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31967" xsd:anyURI
 
 [Term]
 id: GO:0018665
@@ -201756,8 +201762,9 @@ xref: RHEA:55448 {source="skos:exactMatch"}
 xref: RHEA:61104 {source="skos:narrowMatch"}
 xref: RHEA:61108 {source="skos:narrowMatch"}
 xref: RHEA:61120 {source="skos:narrowMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/28526" xsd:anyURI
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31967" xsd:anyURI
 
 [Term]
 id: GO:0033773
@@ -201797,8 +201804,9 @@ xref: EC:1.14.14.136 {source="skos:exactMatch"}
 xref: KEGG_REACTION:R05828
 xref: MetaCyc:1.14.13.91-RXN
 xref: RHEA:14237 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31967" xsd:anyURI
 
 [Term]
 id: GO:0033776
@@ -201828,8 +201836,9 @@ xref: EC:1.14.14.138 {source="skos:exactMatch"}
 xref: KEGG_REACTION:R07203
 xref: MetaCyc:1.14.13.94-RXN
 xref: RHEA:18857 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31967" xsd:anyURI
 
 [Term]
 id: GO:0033778
@@ -201886,8 +201895,9 @@ xref: EC:1.14.14.25 {source="skos:exactMatch"}
 xref: KEGG_REACTION:R07207
 xref: MetaCyc:1.14.13.98-RXN
 xref: RHEA:22716 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31967" xsd:anyURI
 
 [Term]
 id: GO:0033782
@@ -228574,8 +228584,9 @@ xref: EC:1.14.14.144 {source="skos:exactMatch"}
 xref: KEGG_REACTION:R06351
 xref: MetaCyc:RXN-8507
 xref: RHEA:26217 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31967" xsd:anyURI
 created_by: bf
 creation_date: 2012-04-19T10:57:05Z
 
@@ -228735,8 +228746,9 @@ def: "Catalysis of the reaction: ent-isokaurene + O2 + NADPH + H+ = ent-2alpha-h
 xref: EC:1.14.14.76 {source="skos:exactMatch"}
 xref: KEGG_REACTION:R09861
 xref: RHEA:56336 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31967" xsd:anyURI
 created_by: bf
 creation_date: 2012-04-20T02:21:33Z
 
@@ -228749,8 +228761,9 @@ synonym: "ent-cassadiene C11alpha-hydroxylase activity" RELATED [EC:1.14.14.112]
 xref: EC:1.14.14.112 {source="skos:exactMatch"}
 xref: KEGG_REACTION:R09866
 xref: RHEA:31967 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31967" xsd:anyURI
 created_by: bf
 creation_date: 2012-04-20T02:34:13Z
 
@@ -228776,8 +228789,9 @@ xref: EC:1.14.14.145 {source="skos:exactMatch"}
 xref: KEGG_REACTION:R06354
 xref: MetaCyc:RXN-12799
 xref: RHEA:26221 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31967" xsd:anyURI
 created_by: bf
 creation_date: 2012-04-24T02:37:15Z
 
@@ -228848,9 +228862,10 @@ xref: EC:1.14.14.111 {source="skos:exactMatch"}
 xref: KEGG_REACTION:R09865
 xref: MetaCyc:RXN-15437
 xref: RHEA:31951 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/21412" xsd:anyURI
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31967" xsd:anyURI
 created_by: bf
 creation_date: 2012-04-25T11:11:55Z
 
@@ -291822,8 +291837,9 @@ xref: EC:1.14.14.93 {source="skos:exactMatch"}
 xref: KEGG_REACTION:R03452
 xref: MetaCyc:RXN-4505
 xref: RHEA:15321 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31967" xsd:anyURI
 
 [Term]
 id: GO:0047083
@@ -291836,8 +291852,9 @@ synonym: "trans-5-O-(4-coumaroyl)-D-quinate,NADPH:oxygen oxidoreductase (3'-hydr
 xref: EC:1.14.14.96 {source="skos:exactMatch"}
 xref: MetaCyc:1.14.13.36-RXN
 xref: RHEA:16265 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31967" xsd:anyURI
 
 [Term]
 id: GO:0047084
@@ -291851,8 +291868,9 @@ synonym: "methyltetrahydroprotoberberine 14-hydroxylase activity" EXACT []
 xref: EC:1.14.14.97 {source="skos:exactMatch"}
 xref: MetaCyc:1.14.13.37-RXN
 xref: RHEA:23684 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
... (348 more lines truncated)
```

#### Review by gpt-5.5

**outcome**: success  **f1**: 1.0  **precision**: 1.0  **recall**: 1.0

<!-- Review this eval run following analysis/instructions/review-agent-eval.md

  Source issue: https://github.com/geneontology/go-ontology/issues/31967
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/31968
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/98
  Agent config: ai4curation/go-ontology-agent-config

  Quick reference:
    gh issue view 31967 --repo geneontology/go-ontology
    gh pr diff 31968 --repo geneontology/go-ontology
    gh pr diff 98 --repo ai4curation/eval-ont-agent-go
-->

## Summary

The agent successfully completed issue #31967 by reparenting the EC:1.14.14.x cytochrome-P450 monooxygenase activity terms from `GO:0016709` to `GO:0016712`, exactly matching the accepted human PR. The metadiff score (`F1=1.0`, precision `1.0`, recall `1.0`) accurately represents the quality here: the agent PR diff is identical to the human PR diff, including the provenance additions.


## Strengths

- Correctly applied the requested hierarchy fix: affected terms with EC:1.14.14.x xrefs now point to `GO:0016712` `oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen`, instead of the EC:1.14.13.- parent `GO:0016709`.
- Covered the representative early targets from the issue list, including `GO:0004506` squalene monooxygenase activity, `GO:0008398` sterol 14-demethylase activity, `GO:0010295` (+)-abscisic acid 8'-hydroxylase activity, `GO:0016710` trans-cinnamate 4-monooxygenase activity, and `GO:0016711` flavonoid 3'-monooxygenase activity.
- Covered later CYP450-related `GO:010*` targets as well, including `GO:0102001`, `GO:0102002`, `GO:0102320`, `GO:0102375`, `GO:0102556`, `GO:0102597`, `GO:0102684`, `GO:0102876`, `GO:0106144`, and `GO:0106149`.
- Preserved additional asserted parentage while changing the incorrect oxidoreductase grouping parent. For example, `GO:0008398` retains its separate `is_a: GO:0032451 ! demethylase activity`.
- Added `property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31967" xsd:anyURI` to each affected term, matching the human PR's traceability pattern.
- Maintained tight scope: the patch only changes `src/ontology/go-edit.obo` and consists of the intended parent swaps plus issue tracker annotations.


## Issues

No significant issues. The agent solution is substantively and line-for-line identical to the human PR diff for this task.

### Attempt 2: gpt-5.5 / opencode

- **Eval PR**: [#77](https://github.com/ai4curation/eval-ont-agent-go/pull/77)
- **F1**: 1.000  **Precision**: 1.000  **Recall**: 1.000  **Jaccard**: 1.000
- **Trace**: [25615902101](https://github.com/ai4curation/eval-ont-agent-go/tree/master/traces/25615902101)
- **Workflow run**: [25615902101](https://github.com/ai4curation/eval-ont-agent-go/actions/runs/25615902101)

#### Agent PR Comment

## Summary

Reparented the 49 affected EC:1.14.14.x cytochrome P450 monooxygenase activity terms from `GO:0016709` to `GO:0016712` in `src/ontology/go-edit.obo`.

This aligns the asserted GO hierarchy with the EC:1.14.14 reclassification noted in issue #31967. Existing EC/RHEA/MetaCyc xrefs, definitions, synonyms, tracker links, and any additional parents were left unchanged.

## Rationale

Each affected term has an `EC:1.14.14.x` exactMatch xref but was directly asserted under `GO:0016709`, whose exact EC grouping is `EC:1.14.13.-`. The target parent `GO:0016712` carries `EC:1.14.14.-`, making it the appropriate grouping parent for these terms.

## Validation

Pre-validation: `make travis_build` passed before edits.

Post-edit validation: `make travis_build` passed after edits.

The build emitted existing RHEA filter warnings for missing RHEA identifiers, but all reported SPARQL and reasoning checks passed.

## Checklist

- [x] PLAN: Issue #31967 context was reviewed; requested action was clear.
- [x] PRE-VALIDATION: Current ontology validated before changes.
- [x] RESEARCH: N/A; no new definitions, references, or literature-backed term content were introduced.
- [x] TERM-SEARCH: Confirmed source and target grouping terms and all 49 affected terms in `go-edit.obo`.
- [x] DESIGN-PATTERNS: N/A; no new terms or logical definitions were added.
- [x] EDITS: Used `obo-checkout.pl` / `obo-checkin.pl` workflow via `terms/`.
- [x] RELATIONSHIPS: Replaced only the incorrect `is_a: GO:0016709` parent with `is_a: GO:0016712`; preserved other parents and relationships.
- [x] SPECIALIZED-EDITS: Reaction-term guidance consulted because these are catalytic activity terms with EC xrefs.
- [x] METADATA: No new terms or metadata changes were needed.
- [x] AUTOMATED-VALIDATION: `make travis_build` passed after changes.
- [x] REFERENCE-VALIDATION: N/A; no references were added or changed.
- [x] CHANGES-COMMITTED: Local commit created for `src/ontology/go-edit.obo` only.

---
🤖 **Generated by opencode agent**
- Runtime: `opencode`
- Model: `openai/gpt-5.5`
- Agent config: `ai4curation/go-ontology-agent-config@v9:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-go/actions/runs/25615902101)


#### Agent Issue Comment

Implemented in PR #<NN>.

Reparented the 49 EC:1.14.14.x cytochrome P450 monooxygenase activity terms listed in the issue from GO:0016709 to GO:0016712, aligning their asserted parentage with their EC exactMatch classifications.

Validation passed with `make travis_build`.

---
🤖 **Generated by opencode agent**
- Runtime: `opencode`
- Model: `openai/gpt-5.5`
- Agent config: `ai4curation/go-ontology-agent-config@v9:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-go/actions/runs/25615902101)


#### Agent Diff

```diff
diff --git a/src/ontology/go-edit.obo b/src/ontology/go-edit.obo
index 6dd226998..b2469c260 100644
--- a/src/ontology/go-edit.obo
+++ b/src/ontology/go-edit.obo
@@ -43251,8 +43251,9 @@ xref: EC:1.14.14.17 {source="skos:exactMatch"}
 xref: KEGG_REACTION:R02874
 xref: MetaCyc:SQUALENE-MONOOXYGENASE-RXN
 xref: RHEA:25282 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31967" xsd:anyURI
 
 [Term]
 id: GO:0004507
@@ -80692,10 +80693,11 @@ xref: RHEA:25286 {source="skos:narrowMatch"}
 xref: RHEA:45960 {source="skos:narrowMatch"}
 xref: RHEA:54028 {source="skos:exactMatch"}
 xref: RHEA:75439 {source="skos:narrowMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 is_a: GO:0032451 ! demethylase activity
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/22523" xsd:anyURI
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31967" xsd:anyURI
 
 [Term]
 id: GO:0008399
@@ -102582,8 +102584,9 @@ xref: EC:1.14.14.137 {source="skos:exactMatch"}
 xref: KEGG_REACTION:R07202
 xref: MetaCyc:1.14.13.93-RXN
 xref: RHEA:12897 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31967" xsd:anyURI
 
 [Term]
 id: GO:0010296
@@ -127768,8 +127771,9 @@ synonym: "trans-cinnamic acid 4-hydroxylase activity" RELATED [EC:1.14.14.91]
 xref: EC:1.14.14.91 {source="skos:exactMatch"}
 xref: MetaCyc:TRANS-CINNAMATE-4-MONOOXYGENASE-RXN
 xref: RHEA:10608 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31967" xsd:anyURI
 
 [Term]
 id: GO:0016711
@@ -127788,8 +127792,9 @@ xref: RHEA:61096 {source="skos:narrowMatch"}
 xref: RHEA:61112 {source="skos:narrowMatch"}
 xref: RHEA:61124 {source="skos:narrowMatch"}
 xref: RHEA:79895 {source="skos:narrowMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31967" xsd:anyURI
 
 [Term]
 id: GO:0016712
@@ -139312,8 +139317,9 @@ xref: KEGG_REACTION:R01295
 xref: MetaCyc:BENZOATE-4-MONOOXYGENASE-RXN
 xref: RHEA:18033 {source="skos:exactMatch"}
 xref: UM-BBD_reactionID:r0623
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31967" xsd:anyURI
 
 [Term]
 id: GO:0018665
@@ -201756,8 +201762,9 @@ xref: RHEA:55448 {source="skos:exactMatch"}
 xref: RHEA:61104 {source="skos:narrowMatch"}
 xref: RHEA:61108 {source="skos:narrowMatch"}
 xref: RHEA:61120 {source="skos:narrowMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/28526" xsd:anyURI
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31967" xsd:anyURI
 
 [Term]
 id: GO:0033773
@@ -201797,8 +201804,9 @@ xref: EC:1.14.14.136 {source="skos:exactMatch"}
 xref: KEGG_REACTION:R05828
 xref: MetaCyc:1.14.13.91-RXN
 xref: RHEA:14237 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31967" xsd:anyURI
 
 [Term]
 id: GO:0033776
@@ -201828,8 +201836,9 @@ xref: EC:1.14.14.138 {source="skos:exactMatch"}
 xref: KEGG_REACTION:R07203
 xref: MetaCyc:1.14.13.94-RXN
 xref: RHEA:18857 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31967" xsd:anyURI
 
 [Term]
 id: GO:0033778
@@ -201886,8 +201895,9 @@ xref: EC:1.14.14.25 {source="skos:exactMatch"}
 xref: KEGG_REACTION:R07207
 xref: MetaCyc:1.14.13.98-RXN
 xref: RHEA:22716 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31967" xsd:anyURI
 
 [Term]
 id: GO:0033782
@@ -228574,8 +228584,9 @@ xref: EC:1.14.14.144 {source="skos:exactMatch"}
 xref: KEGG_REACTION:R06351
 xref: MetaCyc:RXN-8507
 xref: RHEA:26217 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31967" xsd:anyURI
 created_by: bf
 creation_date: 2012-04-19T10:57:05Z
 
@@ -228735,8 +228746,9 @@ def: "Catalysis of the reaction: ent-isokaurene + O2 + NADPH + H+ = ent-2alpha-h
 xref: EC:1.14.14.76 {source="skos:exactMatch"}
 xref: KEGG_REACTION:R09861
 xref: RHEA:56336 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31967" xsd:anyURI
 created_by: bf
 creation_date: 2012-04-20T02:21:33Z
 
@@ -228749,8 +228761,9 @@ synonym: "ent-cassadiene C11alpha-hydroxylase activity" RELATED [EC:1.14.14.112]
 xref: EC:1.14.14.112 {source="skos:exactMatch"}
 xref: KEGG_REACTION:R09866
 xref: RHEA:31967 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31967" xsd:anyURI
 created_by: bf
 creation_date: 2012-04-20T02:34:13Z
 
@@ -228776,8 +228789,9 @@ xref: EC:1.14.14.145 {source="skos:exactMatch"}
 xref: KEGG_REACTION:R06354
 xref: MetaCyc:RXN-12799
 xref: RHEA:26221 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31967" xsd:anyURI
 created_by: bf
 creation_date: 2012-04-24T02:37:15Z
 
@@ -228848,9 +228862,10 @@ xref: EC:1.14.14.111 {source="skos:exactMatch"}
 xref: KEGG_REACTION:R09865
 xref: MetaCyc:RXN-15437
 xref: RHEA:31951 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/21412" xsd:anyURI
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31967" xsd:anyURI
 created_by: bf
 creation_date: 2012-04-25T11:11:55Z
 
@@ -291822,8 +291837,9 @@ xref: EC:1.14.14.93 {source="skos:exactMatch"}
 xref: KEGG_REACTION:R03452
 xref: MetaCyc:RXN-4505
 xref: RHEA:15321 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31967" xsd:anyURI
 
 [Term]
 id: GO:0047083
@@ -291836,8 +291852,9 @@ synonym: "trans-5-O-(4-coumaroyl)-D-quinate,NADPH:oxygen oxidoreductase (3'-hydr
 xref: EC:1.14.14.96 {source="skos:exactMatch"}
 xref: MetaCyc:1.14.13.36-RXN
 xref: RHEA:16265 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31967" xsd:anyURI
 
 [Term]
 id: GO:0047084
@@ -291851,8 +291868,9 @@ synonym: "methyltetrahydroprotoberberine 14-hydroxylase activity" EXACT []
 xref: EC:1.14.14.97 {source="skos:exactMatch"}
 xref: MetaCyc:1.14.13.37-RXN
 xref: RHEA:23684 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
... (348 more lines truncated)
```

#### Review by gpt-5.5

**outcome**: success  **f1**: 1.0  **precision**: 1.0  **recall**: 1.0

<!-- Review this eval run following analysis/instructions/review-agent-eval.md

  Source issue: https://github.com/geneontology/go-ontology/issues/31967
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/31968
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/77
  Agent config: ai4curation/go-ontology-agent-config

  Quick reference:
    gh issue view 31967 --repo geneontology/go-ontology
    gh pr diff 31968 --repo geneontology/go-ontology
    gh pr diff 77 --repo ai4curation/eval-ont-agent-go
-->

## Summary

The agent successfully completed issue #31967 by reparenting all 49 listed EC:1.14.14.x cytochrome-P450 monooxygenase activity terms from `GO:0016709` to `GO:0016712`, matching the requested EC hierarchy correction. The metadiff score (`F1=1.0`, precision `1.0`, recall `1.0`) accurately reflects the review result: the cached agent PR diff is identical to the human PR diff, including the added `term_tracker_item` annotations for issue `31967`.


## Strengths

- Edited the correct superclass relationship throughout the target set: each affected term loses `is_a: GO:0016709` (EC:1.14.13.- parent) and gains `is_a: GO:0016712` (the existing EC:1.14.14.- grouping term).
- Covered the full requested set of 49 terms, including early/base entries such as `GO:0004506` squalene monooxygenase activity, `GO:0008398` sterol 14-demethylase activity, `GO:0010295` (+)-abscisic acid 8'-hydroxylase activity, `GO:0016710` trans-cinnamate 4-monooxygenase activity, and `GO:0016711` flavonoid 3'-monooxygenase activity.
- Covered the later `GO:010*` entries from the issue list, including `GO:0102001`, `GO:0102002`, `GO:0102320`, `GO:0102375`, `GO:0102556`, `GO:0102597`, `GO:0102684`, `GO:0102876`, `GO:0106144`, and `GO:0106149`.
- Preserved other asserted parents while changing only the EC-inconsistent oxidoreductase parent; notably, `GO:0008398` retains its additional `is_a: GO:0032451 ! demethylase activity`.
- Added `property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31967" xsd:anyURI` to each affected term, matching the human PR's traceability update.
- Maintained tight scope: the patch only changes `src/ontology/go-edit.obo` and consists of the intended relationship swaps plus the corresponding issue tracker annotations.


## Issues

No significant issues. The agent solution is substantively and line-for-line identical to the human PR diff for this task.

### Attempt 3: gemma-4-31b / opencode

- **Eval PR**: [#533](https://github.com/ai4curation/eval-ont-agent-go/pull/533)
- **F1**: 0.800  **Precision**: 0.667  **Recall**: 1.000  **Jaccard**: 0.667

#### Agent Diff

```diff
diff --git a/src/ontology/go-edit.obo b/src/ontology/go-edit.obo
index 6dd226998..c8cf8aed8 100644
--- a/src/ontology/go-edit.obo
+++ b/src/ontology/go-edit.obo
@@ -43251,7 +43251,7 @@ xref: EC:1.14.14.17 {source="skos:exactMatch"}
 xref: KEGG_REACTION:R02874
 xref: MetaCyc:SQUALENE-MONOOXYGENASE-RXN
 xref: RHEA:25282 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
 
 [Term]
@@ -80692,7 +80692,7 @@ xref: RHEA:25286 {source="skos:narrowMatch"}
 xref: RHEA:45960 {source="skos:narrowMatch"}
 xref: RHEA:54028 {source="skos:exactMatch"}
 xref: RHEA:75439 {source="skos:narrowMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 is_a: GO:0032451 ! demethylase activity
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/22523" xsd:anyURI
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
@@ -102582,7 +102582,7 @@ xref: EC:1.14.14.137 {source="skos:exactMatch"}
 xref: KEGG_REACTION:R07202
 xref: MetaCyc:1.14.13.93-RXN
 xref: RHEA:12897 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
 
 [Term]
@@ -127768,7 +127768,7 @@ synonym: "trans-cinnamic acid 4-hydroxylase activity" RELATED [EC:1.14.14.91]
 xref: EC:1.14.14.91 {source="skos:exactMatch"}
 xref: MetaCyc:TRANS-CINNAMATE-4-MONOOXYGENASE-RXN
 xref: RHEA:10608 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
 
 [Term]
@@ -127788,7 +127788,7 @@ xref: RHEA:61096 {source="skos:narrowMatch"}
 xref: RHEA:61112 {source="skos:narrowMatch"}
 xref: RHEA:61124 {source="skos:narrowMatch"}
 xref: RHEA:79895 {source="skos:narrowMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
 
 [Term]
@@ -139312,7 +139312,7 @@ xref: KEGG_REACTION:R01295
 xref: MetaCyc:BENZOATE-4-MONOOXYGENASE-RXN
 xref: RHEA:18033 {source="skos:exactMatch"}
 xref: UM-BBD_reactionID:r0623
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
 
 [Term]
@@ -201756,7 +201756,7 @@ xref: RHEA:55448 {source="skos:exactMatch"}
 xref: RHEA:61104 {source="skos:narrowMatch"}
 xref: RHEA:61108 {source="skos:narrowMatch"}
 xref: RHEA:61120 {source="skos:narrowMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/28526" xsd:anyURI
 
 [Term]
@@ -201797,7 +201797,7 @@ xref: EC:1.14.14.136 {source="skos:exactMatch"}
 xref: KEGG_REACTION:R05828
 xref: MetaCyc:1.14.13.91-RXN
 xref: RHEA:14237 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
 
 [Term]
@@ -201828,7 +201828,7 @@ xref: EC:1.14.14.138 {source="skos:exactMatch"}
 xref: KEGG_REACTION:R07203
 xref: MetaCyc:1.14.13.94-RXN
 xref: RHEA:18857 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
 
 [Term]
@@ -201886,7 +201886,7 @@ xref: EC:1.14.14.25 {source="skos:exactMatch"}
 xref: KEGG_REACTION:R07207
 xref: MetaCyc:1.14.13.98-RXN
 xref: RHEA:22716 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
 
 [Term]
@@ -228574,7 +228574,7 @@ xref: EC:1.14.14.144 {source="skos:exactMatch"}
 xref: KEGG_REACTION:R06351
 xref: MetaCyc:RXN-8507
 xref: RHEA:26217 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
 created_by: bf
 creation_date: 2012-04-19T10:57:05Z
@@ -228735,7 +228735,7 @@ def: "Catalysis of the reaction: ent-isokaurene + O2 + NADPH + H+ = ent-2alpha-h
 xref: EC:1.14.14.76 {source="skos:exactMatch"}
 xref: KEGG_REACTION:R09861
 xref: RHEA:56336 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
 created_by: bf
 creation_date: 2012-04-20T02:21:33Z
@@ -228749,7 +228749,7 @@ synonym: "ent-cassadiene C11alpha-hydroxylase activity" RELATED [EC:1.14.14.112]
 xref: EC:1.14.14.112 {source="skos:exactMatch"}
 xref: KEGG_REACTION:R09866
 xref: RHEA:31967 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
 created_by: bf
 creation_date: 2012-04-20T02:34:13Z
@@ -228776,7 +228776,7 @@ xref: EC:1.14.14.145 {source="skos:exactMatch"}
 xref: KEGG_REACTION:R06354
 xref: MetaCyc:RXN-12799
 xref: RHEA:26221 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
 created_by: bf
 creation_date: 2012-04-24T02:37:15Z
@@ -228848,7 +228848,7 @@ xref: EC:1.14.14.111 {source="skos:exactMatch"}
 xref: KEGG_REACTION:R09865
 xref: MetaCyc:RXN-15437
 xref: RHEA:31951 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/21412" xsd:anyURI
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
 created_by: bf
@@ -291822,7 +291822,7 @@ xref: EC:1.14.14.93 {source="skos:exactMatch"}
 xref: KEGG_REACTION:R03452
 xref: MetaCyc:RXN-4505
 xref: RHEA:15321 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
 
 [Term]
@@ -291836,7 +291836,7 @@ synonym: "trans-5-O-(4-coumaroyl)-D-quinate,NADPH:oxygen oxidoreductase (3'-hydr
 xref: EC:1.14.14.96 {source="skos:exactMatch"}
 xref: MetaCyc:1.14.13.36-RXN
 xref: RHEA:16265 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
 
 [Term]
@@ -291851,7 +291851,7 @@ synonym: "methyltetrahydroprotoberberine 14-hydroxylase activity" EXACT []
 xref: EC:1.14.14.97 {source="skos:exactMatch"}
 xref: MetaCyc:1.14.13.37-RXN
 xref: RHEA:23684 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
 
 [Term]
@@ -291894,7 +291894,7 @@ xref: EC:1.14.14.98 {source="skos:exactMatch"}
 xref: KEGG_REACTION:R04699
 xref: MetaCyc:1.14.13.55-RXN
 xref: RHEA:22644 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
 
 [Term]
@@ -291908,7 +291908,7 @@ xref: EC:1.14.14.100 {source="skos:exactMatch"}
 xref: KEGG_REACTION:R04702
 xref: MetaCyc:1.14.13.56-RXN
 xref: RHEA:10528 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
 
 [Term]
@@ -291922,7 +291922,7 @@ xref: EC:1.14.14.101 {source="skos:exactMatch"}
 xref: KEGG_REACTION:R04708
 xref: MetaCyc:1.14.13.57-RXN
 xref: RHEA:10156 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
 
 [Term]
@@ -305597,7 +305597,7 @@ synonym: "isoflavone 2'-monooxygenase activity" BROAD [EC:1.14.14.89]
 xref: EC:1.14.14.89 {source="skos:exactMatch"}
 xref: MetaCyc:ISOFLAVONE-2-HYDROXYLASE-RXN
 xref: RHEA:12388 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
... (246 more lines truncated)
```

### Attempt 4: gemma-4-31b / opencode

- **Eval PR**: [#510](https://github.com/ai4curation/eval-ont-agent-go/pull/510)
- **F1**: 0.800  **Precision**: 0.667  **Recall**: 1.000  **Jaccard**: 0.667

#### Agent Diff

```diff
diff --git a/src/ontology/go-edit.obo b/src/ontology/go-edit.obo
index 6dd226998..c8cf8aed8 100644
--- a/src/ontology/go-edit.obo
+++ b/src/ontology/go-edit.obo
@@ -43251,7 +43251,7 @@ xref: EC:1.14.14.17 {source="skos:exactMatch"}
 xref: KEGG_REACTION:R02874
 xref: MetaCyc:SQUALENE-MONOOXYGENASE-RXN
 xref: RHEA:25282 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
 
 [Term]
@@ -80692,7 +80692,7 @@ xref: RHEA:25286 {source="skos:narrowMatch"}
 xref: RHEA:45960 {source="skos:narrowMatch"}
 xref: RHEA:54028 {source="skos:exactMatch"}
 xref: RHEA:75439 {source="skos:narrowMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 is_a: GO:0032451 ! demethylase activity
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/22523" xsd:anyURI
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
@@ -102582,7 +102582,7 @@ xref: EC:1.14.14.137 {source="skos:exactMatch"}
 xref: KEGG_REACTION:R07202
 xref: MetaCyc:1.14.13.93-RXN
 xref: RHEA:12897 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
 
 [Term]
@@ -127768,7 +127768,7 @@ synonym: "trans-cinnamic acid 4-hydroxylase activity" RELATED [EC:1.14.14.91]
 xref: EC:1.14.14.91 {source="skos:exactMatch"}
 xref: MetaCyc:TRANS-CINNAMATE-4-MONOOXYGENASE-RXN
 xref: RHEA:10608 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
 
 [Term]
@@ -127788,7 +127788,7 @@ xref: RHEA:61096 {source="skos:narrowMatch"}
 xref: RHEA:61112 {source="skos:narrowMatch"}
 xref: RHEA:61124 {source="skos:narrowMatch"}
 xref: RHEA:79895 {source="skos:narrowMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
 
 [Term]
@@ -139312,7 +139312,7 @@ xref: KEGG_REACTION:R01295
 xref: MetaCyc:BENZOATE-4-MONOOXYGENASE-RXN
 xref: RHEA:18033 {source="skos:exactMatch"}
 xref: UM-BBD_reactionID:r0623
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
 
 [Term]
@@ -201756,7 +201756,7 @@ xref: RHEA:55448 {source="skos:exactMatch"}
 xref: RHEA:61104 {source="skos:narrowMatch"}
 xref: RHEA:61108 {source="skos:narrowMatch"}
 xref: RHEA:61120 {source="skos:narrowMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/28526" xsd:anyURI
 
 [Term]
@@ -201797,7 +201797,7 @@ xref: EC:1.14.14.136 {source="skos:exactMatch"}
 xref: KEGG_REACTION:R05828
 xref: MetaCyc:1.14.13.91-RXN
 xref: RHEA:14237 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
 
 [Term]
@@ -201828,7 +201828,7 @@ xref: EC:1.14.14.138 {source="skos:exactMatch"}
 xref: KEGG_REACTION:R07203
 xref: MetaCyc:1.14.13.94-RXN
 xref: RHEA:18857 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
 
 [Term]
@@ -201886,7 +201886,7 @@ xref: EC:1.14.14.25 {source="skos:exactMatch"}
 xref: KEGG_REACTION:R07207
 xref: MetaCyc:1.14.13.98-RXN
 xref: RHEA:22716 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
 
 [Term]
@@ -228574,7 +228574,7 @@ xref: EC:1.14.14.144 {source="skos:exactMatch"}
 xref: KEGG_REACTION:R06351
 xref: MetaCyc:RXN-8507
 xref: RHEA:26217 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
 created_by: bf
 creation_date: 2012-04-19T10:57:05Z
@@ -228735,7 +228735,7 @@ def: "Catalysis of the reaction: ent-isokaurene + O2 + NADPH + H+ = ent-2alpha-h
 xref: EC:1.14.14.76 {source="skos:exactMatch"}
 xref: KEGG_REACTION:R09861
 xref: RHEA:56336 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
 created_by: bf
 creation_date: 2012-04-20T02:21:33Z
@@ -228749,7 +228749,7 @@ synonym: "ent-cassadiene C11alpha-hydroxylase activity" RELATED [EC:1.14.14.112]
 xref: EC:1.14.14.112 {source="skos:exactMatch"}
 xref: KEGG_REACTION:R09866
 xref: RHEA:31967 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
 created_by: bf
 creation_date: 2012-04-20T02:34:13Z
@@ -228776,7 +228776,7 @@ xref: EC:1.14.14.145 {source="skos:exactMatch"}
 xref: KEGG_REACTION:R06354
 xref: MetaCyc:RXN-12799
 xref: RHEA:26221 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
 created_by: bf
 creation_date: 2012-04-24T02:37:15Z
@@ -228848,7 +228848,7 @@ xref: EC:1.14.14.111 {source="skos:exactMatch"}
 xref: KEGG_REACTION:R09865
 xref: MetaCyc:RXN-15437
 xref: RHEA:31951 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/21412" xsd:anyURI
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
 created_by: bf
@@ -291822,7 +291822,7 @@ xref: EC:1.14.14.93 {source="skos:exactMatch"}
 xref: KEGG_REACTION:R03452
 xref: MetaCyc:RXN-4505
 xref: RHEA:15321 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
 
 [Term]
@@ -291836,7 +291836,7 @@ synonym: "trans-5-O-(4-coumaroyl)-D-quinate,NADPH:oxygen oxidoreductase (3'-hydr
 xref: EC:1.14.14.96 {source="skos:exactMatch"}
 xref: MetaCyc:1.14.13.36-RXN
 xref: RHEA:16265 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
 
 [Term]
@@ -291851,7 +291851,7 @@ synonym: "methyltetrahydroprotoberberine 14-hydroxylase activity" EXACT []
 xref: EC:1.14.14.97 {source="skos:exactMatch"}
 xref: MetaCyc:1.14.13.37-RXN
 xref: RHEA:23684 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
 
 [Term]
@@ -291894,7 +291894,7 @@ xref: EC:1.14.14.98 {source="skos:exactMatch"}
 xref: KEGG_REACTION:R04699
 xref: MetaCyc:1.14.13.55-RXN
 xref: RHEA:22644 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
 
 [Term]
@@ -291908,7 +291908,7 @@ xref: EC:1.14.14.100 {source="skos:exactMatch"}
 xref: KEGG_REACTION:R04702
 xref: MetaCyc:1.14.13.56-RXN
 xref: RHEA:10528 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
 
 [Term]
@@ -291922,7 +291922,7 @@ xref: EC:1.14.14.101 {source="skos:exactMatch"}
 xref: KEGG_REACTION:R04708
 xref: MetaCyc:1.14.13.57-RXN
 xref: RHEA:10156 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
 
 [Term]
@@ -305597,7 +305597,7 @@ synonym: "isoflavone 2'-monooxygenase activity" BROAD [EC:1.14.14.89]
 xref: EC:1.14.14.89 {source="skos:exactMatch"}
 xref: MetaCyc:ISOFLAVONE-2-HYDROXYLASE-RXN
 xref: RHEA:12388 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
... (246 more lines truncated)
```

### Attempt 5: claude-sonnet-4.5 / copilot

- **Eval PR**: [#497](https://github.com/ai4curation/eval-ont-agent-go/pull/497)
- **F1**: 0.800  **Precision**: 0.667  **Recall**: 1.000  **Jaccard**: 0.667
- **Trace**: [25888553584](https://github.com/ai4curation/eval-ont-agent-go/tree/master/traces/25888553584)
- **Workflow run**: [25888553584](https://github.com/ai4curation/eval-ont-agent-go/actions/runs/25888553584)

#### Agent PR Comment

# Reparent 49 EC:1.14.14.x cytochrome P450 terms

## Summary
This PR addresses issue #31967 by systematically reparenting 49 cytochrome P450 monooxygenase activity terms to align with the IUBMB 2018 EC reclassification.

## Changes Made
- **Modified file**: `src/ontology/go-edit.obo`
- **Type of change**: Reparenting of existing terms
- **Number of terms affected**: 49

All 49 terms previously had `is_a: GO:0016709` (EC:1.14.13.-) and now have `is_a: GO:0016712` (EC:1.14.14.-).

## Rationale
The affected terms all have EC xrefs in sub-subclass 1.14.14, but their nearest EC-bearing is_a ancestor was GO:0016709 carrying EC:1.14.13.-, which is not an EC-class ancestor of 1.14.14.x. This inconsistency arose from the IUBMB 2018 reclassification of most cytochrome P450 enzymes from EC sub-subclass 1.14.13 to 1.14.14.

The target parent GO:0016712 appropriately carries `xref: EC:1.14.14.- {source="skos:exactMatch"}`, making it the correct parent for all these terms.

## Terms Modified (49 total)
GO:0004506 (squalene monooxygenase activity), GO:0008398 (sterol 14-demethylase activity), GO:0010295 ((+)-abscisic acid 8'-hydroxylase activity), GO:0016710 (trans-cinnamate 4-monooxygenase activity), GO:0016711 (flavonoid 3'-monooxygenase activity), GO:0018664 (benzoate 4-monooxygenase activity), GO:0033772 (flavonoid 3',5'-hydroxylase activity), GO:0033775 (deoxysarpagine hydroxylase activity), GO:0033777 (lithocholate 6beta-hydroxylase activity), GO:0033781 (cholesterol 24-hydroxylase activity), GO:0036189 (abieta-7,13-diene hydroxylase activity), GO:0036201 (ent-isokaurene C2-hydroxylase activity), GO:0036202 (ent-cassa-12,15-diene 11-hydroxylase activity), GO:0036204 (abieta-7,13-dien-18-ol hydroxylase activity), GO:0036209 (9beta-pimara-7,15-diene oxidase activity), GO:0047082 (3,9-dihydroxypterocarpan 6a-monooxygenase activity), GO:0047083 (5-O-(4-coumaroyl)-D-quinate 3'-monooxygenase activity), GO:0047084 (methyltetrahydroprotoberberine 14-monooxygenase activity), GO:0047087 (protopine 6-monooxygenase activity), GO:0047088 (dihydrosanguinarine 10-monooxygenase activity), GO:0047089 (dihydrochelirubine 12-monooxygenase activity), GO:0047957 (4'-methoxyisoflavone 2'-hydroxylase activity), GO:0048000 (isoflavone 3'-hydroxylase activity), GO:0050591 (quinine 3-monooxygenase activity), GO:0050592 (4-hydroxyphenylacetaldehyde oxime monooxygenase activity), GO:0050593 (N-methylcoclaurine 3'-monooxygenase activity), GO:0050594 (tabersonine 16-hydroxylase activity), GO:0050596 (vinorine hydroxylase activity), GO:0050597 (taxane 10-beta-hydroxylase activity), GO:0050598 (taxane 13-alpha-hydroxylase activity), GO:0102001 (isoleucine N-monooxygenase (oxime forming) activity), GO:0102002 (valine N-monooxygenase (oxime forming) activity), GO:0102068 (alpha-humulene 10-hydroxylase activity), GO:0102170 (5-epi-aristolochene-1,3-dihydroxylase activity), GO:0102289 (beta-amyrin 11-oxidase activity), GO:0102320 (1,8-cineole 2-exo-monooxygenase activity), GO:0102375 (11-oxo-beta-amyrin 30-oxidase activity), GO:0102556 (dammarenediol 12-hydroxylase activity), GO:0102557 (protopanaxadiol 6-hydroxylase activity), GO:0102596 (cytochrome P450 dependent ent-sandaracopimaradiene 3-hydroxylase activity), GO:0102597 (3alpha-hydroxy-ent-sandaracopimardiene 9-beta-monooxygenase activity), GO:0102598 (3alpha-hydroxy-ent-sandaracopimardiene 7-beta-monooxygenase activity), GO:0102684 (L-phenylalanine N-monooxygenase activity), GO:0102811 (geraniol 10-hydroxylase activity), GO:0102876 (psoralen synthase (NADPH) activity), GO:0102934 (costunolide synthase activity), GO:0102995 (angelicin synthase activity), GO:0106144 (fraxetin 5-hydroxylase activity), GO:0106149 (indole-3-carbonyl nitrile 4-hydroxylase activity)

## Verification Checklist
- [x] **PLAN**: Issue analyzed and plan created
- [x] **PRE-VALIDATION**: Baseline validation performed (build tools unavailable, manual checks passed)
- [x] **TERM-SEARCH**: All affected terms and parent terms verified
  - Confirmed GO:0016709 (old parent) has EC:1.14.13.- xref
  - Confirmed GO:0016712 (new parent) has EC:1.14.14.- xref
  - Verified sample terms have EC:1.14.14.x xrefs
- [x] **DESIGN-PATTERNS**: Design pattern compliance verified
  - Pattern is straightforward: reparent to match EC classification
  - No logical definitions involved, only is_a relationships
- [x] **EDITS**: Correct checkout/checkin procedure followed
  - Used obo-checkout.pl to extract all 49 terms
  - Modified is_a relationships in individual term files
  - Used obo-checkin.pl to reintegrate changes
- [x] **RELATIONSHIPS**: Relationships properly maintained
  - Changed only the GO:0016709 is_a relationship to GO:0016712
  - Preserved all other relationships (e.g., GO:0008398 retains its is_a to GO:0032451)
  - No logical definitions to update
- [x] **METADATA**: Metadata handling correct
  - No metadata changes needed (only editing existing terms, not creating new ones)
  - Preserved all existing metadata fields
- [x] **AUTOMATED-VALIDATION**: Validation performed
  - Full travis_build unavailable due to missing dependencies (amm, robot)
  - Manual verification: all 49 terms confirmed to have new parent GO:0016712
  - Manual verification: no terms retain old parent GO:0016709
  - Manual verification: sample terms confirmed to have matching EC:1.14.14.x xrefs
- [x] **CHANGES-COMMITTED**: Changes committed properly
  - Modified only src/ontology/go-edit.obo
  - Detailed commit message with full context
  - Includes issue reference and co-author signature

## Impact
This change resolves the largest cluster of EC/GO hierarchy inconsistencies in the GO:0016491 oxidoreductase subtree, ensuring that cytochrome P450 monooxygenase activities are correctly grouped under a parent that matches their EC classification.

---
🤖 **Generated by copilot agent**
- Runtime: `copilot`
- Model: `claude-sonnet-4.5`
- Agent config: `ai4curation/go-ontology-agent-config@v9:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-go/actions/runs/25888553584)


#### Agent Issue Comment

Changes committed in PR #<NN>.

All 49 cytochrome P450 monooxygenase activity terms with EC:1.14.14.x xrefs have been successfully reparented from GO:0016709 (EC:1.14.13.-) to GO:0016712 (EC:1.14.14.-), aligning the GO hierarchy with the IUBMB 2018 EC reclassification.

The changes have been verified and all affected terms now correctly reference GO:0016712 as their parent, ensuring consistency between GO and EC classifications.

---
🤖 **Generated by copilot agent**
- Runtime: `copilot`
- Model: `claude-sonnet-4.5`
- Agent config: `ai4curation/go-ontology-agent-config@v9:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-go/actions/runs/25888553584)


#### Agent Diff

```diff
diff --git a/src/ontology/go-edit.obo b/src/ontology/go-edit.obo
index 6dd226998..c8cf8aed8 100644
--- a/src/ontology/go-edit.obo
+++ b/src/ontology/go-edit.obo
@@ -43251,7 +43251,7 @@ xref: EC:1.14.14.17 {source="skos:exactMatch"}
 xref: KEGG_REACTION:R02874
 xref: MetaCyc:SQUALENE-MONOOXYGENASE-RXN
 xref: RHEA:25282 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
 
 [Term]
@@ -80692,7 +80692,7 @@ xref: RHEA:25286 {source="skos:narrowMatch"}
 xref: RHEA:45960 {source="skos:narrowMatch"}
 xref: RHEA:54028 {source="skos:exactMatch"}
 xref: RHEA:75439 {source="skos:narrowMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 is_a: GO:0032451 ! demethylase activity
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/22523" xsd:anyURI
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
@@ -102582,7 +102582,7 @@ xref: EC:1.14.14.137 {source="skos:exactMatch"}
 xref: KEGG_REACTION:R07202
 xref: MetaCyc:1.14.13.93-RXN
 xref: RHEA:12897 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
 
 [Term]
@@ -127768,7 +127768,7 @@ synonym: "trans-cinnamic acid 4-hydroxylase activity" RELATED [EC:1.14.14.91]
 xref: EC:1.14.14.91 {source="skos:exactMatch"}
 xref: MetaCyc:TRANS-CINNAMATE-4-MONOOXYGENASE-RXN
 xref: RHEA:10608 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
 
 [Term]
@@ -127788,7 +127788,7 @@ xref: RHEA:61096 {source="skos:narrowMatch"}
 xref: RHEA:61112 {source="skos:narrowMatch"}
 xref: RHEA:61124 {source="skos:narrowMatch"}
 xref: RHEA:79895 {source="skos:narrowMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
 
 [Term]
@@ -139312,7 +139312,7 @@ xref: KEGG_REACTION:R01295
 xref: MetaCyc:BENZOATE-4-MONOOXYGENASE-RXN
 xref: RHEA:18033 {source="skos:exactMatch"}
 xref: UM-BBD_reactionID:r0623
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
 
 [Term]
@@ -201756,7 +201756,7 @@ xref: RHEA:55448 {source="skos:exactMatch"}
 xref: RHEA:61104 {source="skos:narrowMatch"}
 xref: RHEA:61108 {source="skos:narrowMatch"}
 xref: RHEA:61120 {source="skos:narrowMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/28526" xsd:anyURI
 
 [Term]
@@ -201797,7 +201797,7 @@ xref: EC:1.14.14.136 {source="skos:exactMatch"}
 xref: KEGG_REACTION:R05828
 xref: MetaCyc:1.14.13.91-RXN
 xref: RHEA:14237 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
 
 [Term]
@@ -201828,7 +201828,7 @@ xref: EC:1.14.14.138 {source="skos:exactMatch"}
 xref: KEGG_REACTION:R07203
 xref: MetaCyc:1.14.13.94-RXN
 xref: RHEA:18857 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
 
 [Term]
@@ -201886,7 +201886,7 @@ xref: EC:1.14.14.25 {source="skos:exactMatch"}
 xref: KEGG_REACTION:R07207
 xref: MetaCyc:1.14.13.98-RXN
 xref: RHEA:22716 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
 
 [Term]
@@ -228574,7 +228574,7 @@ xref: EC:1.14.14.144 {source="skos:exactMatch"}
 xref: KEGG_REACTION:R06351
 xref: MetaCyc:RXN-8507
 xref: RHEA:26217 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
 created_by: bf
 creation_date: 2012-04-19T10:57:05Z
@@ -228735,7 +228735,7 @@ def: "Catalysis of the reaction: ent-isokaurene + O2 + NADPH + H+ = ent-2alpha-h
 xref: EC:1.14.14.76 {source="skos:exactMatch"}
 xref: KEGG_REACTION:R09861
 xref: RHEA:56336 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
 created_by: bf
 creation_date: 2012-04-20T02:21:33Z
@@ -228749,7 +228749,7 @@ synonym: "ent-cassadiene C11alpha-hydroxylase activity" RELATED [EC:1.14.14.112]
 xref: EC:1.14.14.112 {source="skos:exactMatch"}
 xref: KEGG_REACTION:R09866
 xref: RHEA:31967 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
 created_by: bf
 creation_date: 2012-04-20T02:34:13Z
@@ -228776,7 +228776,7 @@ xref: EC:1.14.14.145 {source="skos:exactMatch"}
 xref: KEGG_REACTION:R06354
 xref: MetaCyc:RXN-12799
 xref: RHEA:26221 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
 created_by: bf
 creation_date: 2012-04-24T02:37:15Z
@@ -228848,7 +228848,7 @@ xref: EC:1.14.14.111 {source="skos:exactMatch"}
 xref: KEGG_REACTION:R09865
 xref: MetaCyc:RXN-15437
 xref: RHEA:31951 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/21412" xsd:anyURI
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
 created_by: bf
@@ -291822,7 +291822,7 @@ xref: EC:1.14.14.93 {source="skos:exactMatch"}
 xref: KEGG_REACTION:R03452
 xref: MetaCyc:RXN-4505
 xref: RHEA:15321 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
 
 [Term]
@@ -291836,7 +291836,7 @@ synonym: "trans-5-O-(4-coumaroyl)-D-quinate,NADPH:oxygen oxidoreductase (3'-hydr
 xref: EC:1.14.14.96 {source="skos:exactMatch"}
 xref: MetaCyc:1.14.13.36-RXN
 xref: RHEA:16265 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
 
 [Term]
@@ -291851,7 +291851,7 @@ synonym: "methyltetrahydroprotoberberine 14-hydroxylase activity" EXACT []
 xref: EC:1.14.14.97 {source="skos:exactMatch"}
 xref: MetaCyc:1.14.13.37-RXN
 xref: RHEA:23684 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
 
 [Term]
@@ -291894,7 +291894,7 @@ xref: EC:1.14.14.98 {source="skos:exactMatch"}
 xref: KEGG_REACTION:R04699
 xref: MetaCyc:1.14.13.55-RXN
 xref: RHEA:22644 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
 
 [Term]
@@ -291908,7 +291908,7 @@ xref: EC:1.14.14.100 {source="skos:exactMatch"}
 xref: KEGG_REACTION:R04702
 xref: MetaCyc:1.14.13.56-RXN
 xref: RHEA:10528 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
 
 [Term]
@@ -291922,7 +291922,7 @@ xref: EC:1.14.14.101 {source="skos:exactMatch"}
 xref: KEGG_REACTION:R04708
 xref: MetaCyc:1.14.13.57-RXN
 xref: RHEA:10156 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
 
 [Term]
@@ -305597,7 +305597,7 @@ synonym: "isoflavone 2'-monooxygenase activity" BROAD [EC:1.14.14.89]
 xref: EC:1.14.14.89 {source="skos:exactMatch"}
 xref: MetaCyc:ISOFLAVONE-2-HYDROXYLASE-RXN
 xref: RHEA:12388 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
... (246 more lines truncated)
```

### Attempt 6: claude-sonnet-4.5 / claude

- **Eval PR**: [#476](https://github.com/ai4curation/eval-ont-agent-go/pull/476)
- **F1**: 0.800  **Precision**: 0.667  **Recall**: 1.000  **Jaccard**: 0.667
- **Trace**: [25847326548](https://github.com/ai4curation/eval-ont-agent-go/tree/master/traces/25847326548)
- **Workflow run**: [25847326548](https://github.com/ai4curation/eval-ont-agent-go/actions/runs/25847326548)

#### Agent PR Comment

# Reparent 49 EC:1.14.14.x cytochrome P450 terms to correct EC hierarchy

## Summary

This PR addresses issue #31967 by reparenting 49 cytochrome P450 monooxygenase activity terms from GO:0016709 to GO:0016712, aligning their GO hierarchy with the IUBMB 2018 EC classification update.

## Background

The affected terms carry EC:1.14.14.x xrefs (with skos:exactMatch mappings), indicating they belong to EC sub-subclass 1.14.14 (oxidoreductases acting on paired donors with reduced flavin/flavoprotein as one donor). However, they were previously classified under GO:0016709, which maps to EC:1.14.13.- (oxidoreductases with NAD(P)H as one donor). This created a hierarchy inconsistency where the terms' EC codes were not in the same sub-subclass as their GO parent's EC code.

## Changes Made

Replaced `is_a: GO:0016709` with `is_a: GO:0016712` for all 49 terms:

- **Old parent**: GO:0016709 "oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen" (EC:1.14.13.-)
- **New parent**: GO:0016712 "oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen" (EC:1.14.14.-)

For terms with multiple parent classes (e.g., GO:0008398 which is also a demethylase), only the specific is_a relationship to GO:0016709 was modified; all other relationships were preserved.

## Affected Terms (49)

GO:0004506, GO:0008398, GO:0010295, GO:0016710, GO:0016711, GO:0018664, GO:0033772, GO:0033775, GO:0033777, GO:0033781, GO:0036189, GO:0036201, GO:0036202, GO:0036204, GO:0036209, GO:0047082, GO:0047083, GO:0047084, GO:0047087, GO:0047088, GO:0047089, GO:0047957, GO:0048000, GO:0050591, GO:0050592, GO:0050593, GO:0050594, GO:0050596, GO:0050597, GO:0050598, GO:0102001, GO:0102002, GO:0102068, GO:0102170, GO:0102289, GO:0102320, GO:0102375, GO:0102556, GO:0102557, GO:0102596, GO:0102597, GO:0102598, GO:0102684, GO:0102811, GO:0102876, GO:0102934, GO:0102995, GO:0106144, GO:0106149

## Technical Details

### Procedure
1. Verified current state: all 49 terms had `is_a: GO:0016709` and EC:1.14.14.x xrefs
2. Confirmed target parent GO:0016712 exists with `xref: EC:1.14.14.-`
3. Used obo-checkout.pl to check out all 49 terms
4. Performed batch replacement of is_a relationships
5. Used obo-checkin.pl to update src/ontology/go-edit.obo
6. Verified changes: confirmed all terms now have GO:0016712 as parent

### Files Modified
- `src/ontology/go-edit.obo`: 49 is_a relationships updated (49 insertions, 49 deletions)

## Validation

Manual verification confirmed:
- All 49 terms now have `is_a: GO:0016712` 
- All 49 terms retain their EC:1.14.14.x xrefs
- Terms with multiple parents (e.g., GO:0008398) retained their other is_a relationships
- No terms still reference GO:0016709 as a parent

Note: Automated validation tools (robot, amm) were not available in the evaluation environment. Standard travis_build validation should be performed by reviewers.

## Checklist

- [x] PLAN: Issue analyzed, intent clear, plan created
- [x] PRE-VALIDATION: Ontology file accessible and in expected location
- [N/A] RESEARCH: Not required for this administrative reclassification
- [x] TERM-SEARCH: Verified current parent relationships and target parent structure
- [N/A] DESIGN-PATTERNS: Not applicable for simple reparenting
- [x] EDITS: Proper checkout/checkin procedure followed
  - [x] Used obo-checkout.pl to extract terms to terms/ folder
  - [x] Modified is_a relationships
  - [x] Used obo-checkin.pl to update go-edit.obo
- [x] RELATIONSHIPS: Appropriate relationships maintained
  - [x] Only the specific GO:0016709 is_a relationship was modified
  - [x] Other is_a relationships preserved for multi-parent terms
  - [x] No other relationships affected
- [N/A] SPECIALIZED-EDITS: Not required (no obsoletions, CHEBI terms, reactions, or taxon constraints)
- [N/A] METADATA: No metadata changes required (existing terms only)
- [x] AUTOMATED-VALIDATION: Manual verification performed
  - [x] All 49 terms confirmed to have new parent GO:0016712
  - [x] No terms retain old parent GO:0016709
  - [x] EC xrefs preserved
- [N/A] REFERENCE-VALIDATION: No new references introduced
- [x] CHANGES-COMMITTED
  - [x] RELEVANT-FILES: Only src/ontology/go-edit.obo committed
  - [x] ACCURACY: Changes align with IUBMB 2018 EC reclassification
  - [x] ISSUE-ALIGNMENT: Changes directly address issue #31967
  - [x] PR description includes detailed rationale and complete checklist
  - [x] Issue updated with status

## Rationale

This change corrects a systematic misalignment between GO and EC hierarchies that arose from the IUBMB's 2018 reclassification of most cytochrome P450 enzymes from EC 1.14.13 to EC 1.14.14. By ensuring GO parents match EC parents at the sub-subclass level, this improves ontology consistency and facilitates accurate cross-referencing between GO and EC classifications.

---
🤖 **Generated by claude agent**
- Runtime: `claude`
- Model: `claude-sonnet-4-5-20250929`
- Agent config: `ai4curation/go-ontology-agent-config@v9:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-go/actions/runs/25847326548)


#### Agent Issue Comment

Changes committed in PR #<NN>.

All 49 cytochrome P450 monooxygenase activity terms with EC:1.14.14.x xrefs have been successfully reparented from GO:0016709 (EC:1.14.13.-) to GO:0016712 (EC:1.14.14.-), aligning the GO hierarchy with the IUBMB 2018 EC reclassification.

The changes have been verified to ensure:
- All 49 terms now have GO:0016712 as their parent
- Terms with multiple parent classes retained their other relationships
- EC xrefs remain intact

This resolves the EC/GO hierarchy inconsistency identified in the issue.

---
🤖 **Generated by claude agent**
- Runtime: `claude`
- Model: `claude-sonnet-4-5-20250929`
- Agent config: `ai4curation/go-ontology-agent-config@v9:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-go/actions/runs/25847326548)


#### Agent Diff

```diff
diff --git a/src/ontology/go-edit.obo b/src/ontology/go-edit.obo
index 6dd226998..c8cf8aed8 100644
--- a/src/ontology/go-edit.obo
+++ b/src/ontology/go-edit.obo
@@ -43251,7 +43251,7 @@ xref: EC:1.14.14.17 {source="skos:exactMatch"}
 xref: KEGG_REACTION:R02874
 xref: MetaCyc:SQUALENE-MONOOXYGENASE-RXN
 xref: RHEA:25282 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
 
 [Term]
@@ -80692,7 +80692,7 @@ xref: RHEA:25286 {source="skos:narrowMatch"}
 xref: RHEA:45960 {source="skos:narrowMatch"}
 xref: RHEA:54028 {source="skos:exactMatch"}
 xref: RHEA:75439 {source="skos:narrowMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 is_a: GO:0032451 ! demethylase activity
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/22523" xsd:anyURI
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
@@ -102582,7 +102582,7 @@ xref: EC:1.14.14.137 {source="skos:exactMatch"}
 xref: KEGG_REACTION:R07202
 xref: MetaCyc:1.14.13.93-RXN
 xref: RHEA:12897 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
 
 [Term]
@@ -127768,7 +127768,7 @@ synonym: "trans-cinnamic acid 4-hydroxylase activity" RELATED [EC:1.14.14.91]
 xref: EC:1.14.14.91 {source="skos:exactMatch"}
 xref: MetaCyc:TRANS-CINNAMATE-4-MONOOXYGENASE-RXN
 xref: RHEA:10608 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
 
 [Term]
@@ -127788,7 +127788,7 @@ xref: RHEA:61096 {source="skos:narrowMatch"}
 xref: RHEA:61112 {source="skos:narrowMatch"}
 xref: RHEA:61124 {source="skos:narrowMatch"}
 xref: RHEA:79895 {source="skos:narrowMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
 
 [Term]
@@ -139312,7 +139312,7 @@ xref: KEGG_REACTION:R01295
 xref: MetaCyc:BENZOATE-4-MONOOXYGENASE-RXN
 xref: RHEA:18033 {source="skos:exactMatch"}
 xref: UM-BBD_reactionID:r0623
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
 
 [Term]
@@ -201756,7 +201756,7 @@ xref: RHEA:55448 {source="skos:exactMatch"}
 xref: RHEA:61104 {source="skos:narrowMatch"}
 xref: RHEA:61108 {source="skos:narrowMatch"}
 xref: RHEA:61120 {source="skos:narrowMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/28526" xsd:anyURI
 
 [Term]
@@ -201797,7 +201797,7 @@ xref: EC:1.14.14.136 {source="skos:exactMatch"}
 xref: KEGG_REACTION:R05828
 xref: MetaCyc:1.14.13.91-RXN
 xref: RHEA:14237 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
 
 [Term]
@@ -201828,7 +201828,7 @@ xref: EC:1.14.14.138 {source="skos:exactMatch"}
 xref: KEGG_REACTION:R07203
 xref: MetaCyc:1.14.13.94-RXN
 xref: RHEA:18857 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
 
 [Term]
@@ -201886,7 +201886,7 @@ xref: EC:1.14.14.25 {source="skos:exactMatch"}
 xref: KEGG_REACTION:R07207
 xref: MetaCyc:1.14.13.98-RXN
 xref: RHEA:22716 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
 
 [Term]
@@ -228574,7 +228574,7 @@ xref: EC:1.14.14.144 {source="skos:exactMatch"}
 xref: KEGG_REACTION:R06351
 xref: MetaCyc:RXN-8507
 xref: RHEA:26217 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
 created_by: bf
 creation_date: 2012-04-19T10:57:05Z
@@ -228735,7 +228735,7 @@ def: "Catalysis of the reaction: ent-isokaurene + O2 + NADPH + H+ = ent-2alpha-h
 xref: EC:1.14.14.76 {source="skos:exactMatch"}
 xref: KEGG_REACTION:R09861
 xref: RHEA:56336 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
 created_by: bf
 creation_date: 2012-04-20T02:21:33Z
@@ -228749,7 +228749,7 @@ synonym: "ent-cassadiene C11alpha-hydroxylase activity" RELATED [EC:1.14.14.112]
 xref: EC:1.14.14.112 {source="skos:exactMatch"}
 xref: KEGG_REACTION:R09866
 xref: RHEA:31967 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
 created_by: bf
 creation_date: 2012-04-20T02:34:13Z
@@ -228776,7 +228776,7 @@ xref: EC:1.14.14.145 {source="skos:exactMatch"}
 xref: KEGG_REACTION:R06354
 xref: MetaCyc:RXN-12799
 xref: RHEA:26221 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
 created_by: bf
 creation_date: 2012-04-24T02:37:15Z
@@ -228848,7 +228848,7 @@ xref: EC:1.14.14.111 {source="skos:exactMatch"}
 xref: KEGG_REACTION:R09865
 xref: MetaCyc:RXN-15437
 xref: RHEA:31951 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/21412" xsd:anyURI
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
 created_by: bf
@@ -291822,7 +291822,7 @@ xref: EC:1.14.14.93 {source="skos:exactMatch"}
 xref: KEGG_REACTION:R03452
 xref: MetaCyc:RXN-4505
 xref: RHEA:15321 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
 
 [Term]
@@ -291836,7 +291836,7 @@ synonym: "trans-5-O-(4-coumaroyl)-D-quinate,NADPH:oxygen oxidoreductase (3'-hydr
 xref: EC:1.14.14.96 {source="skos:exactMatch"}
 xref: MetaCyc:1.14.13.36-RXN
 xref: RHEA:16265 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
 
 [Term]
@@ -291851,7 +291851,7 @@ synonym: "methyltetrahydroprotoberberine 14-hydroxylase activity" EXACT []
 xref: EC:1.14.14.97 {source="skos:exactMatch"}
 xref: MetaCyc:1.14.13.37-RXN
 xref: RHEA:23684 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
 
 [Term]
@@ -291894,7 +291894,7 @@ xref: EC:1.14.14.98 {source="skos:exactMatch"}
 xref: KEGG_REACTION:R04699
 xref: MetaCyc:1.14.13.55-RXN
 xref: RHEA:22644 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
 
 [Term]
@@ -291908,7 +291908,7 @@ xref: EC:1.14.14.100 {source="skos:exactMatch"}
 xref: KEGG_REACTION:R04702
 xref: MetaCyc:1.14.13.56-RXN
 xref: RHEA:10528 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
 
 [Term]
@@ -291922,7 +291922,7 @@ xref: EC:1.14.14.101 {source="skos:exactMatch"}
 xref: KEGG_REACTION:R04708
 xref: MetaCyc:1.14.13.57-RXN
 xref: RHEA:10156 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
 
 [Term]
@@ -305597,7 +305597,7 @@ synonym: "isoflavone 2'-monooxygenase activity" BROAD [EC:1.14.14.89]
 xref: EC:1.14.14.89 {source="skos:exactMatch"}
 xref: MetaCyc:ISOFLAVONE-2-HYDROXYLASE-RXN
 xref: RHEA:12388 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
... (246 more lines truncated)
```

### Attempt 7: claude-sonnet-4.5 / copilot

- **Eval PR**: [#418](https://github.com/ai4curation/eval-ont-agent-go/pull/418)
- **F1**: 0.800  **Precision**: 0.667  **Recall**: 1.000  **Jaccard**: 0.667
- **Trace**: [25774724377](https://github.com/ai4curation/eval-ont-agent-go/tree/master/traces/25774724377)

#### Agent Diff

```diff
diff --git a/src/ontology/go-edit.obo b/src/ontology/go-edit.obo
index 6dd226998..c8cf8aed8 100644
--- a/src/ontology/go-edit.obo
+++ b/src/ontology/go-edit.obo
@@ -43251,7 +43251,7 @@ xref: EC:1.14.14.17 {source="skos:exactMatch"}
 xref: KEGG_REACTION:R02874
 xref: MetaCyc:SQUALENE-MONOOXYGENASE-RXN
 xref: RHEA:25282 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
 
 [Term]
@@ -80692,7 +80692,7 @@ xref: RHEA:25286 {source="skos:narrowMatch"}
 xref: RHEA:45960 {source="skos:narrowMatch"}
 xref: RHEA:54028 {source="skos:exactMatch"}
 xref: RHEA:75439 {source="skos:narrowMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 is_a: GO:0032451 ! demethylase activity
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/22523" xsd:anyURI
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
@@ -102582,7 +102582,7 @@ xref: EC:1.14.14.137 {source="skos:exactMatch"}
 xref: KEGG_REACTION:R07202
 xref: MetaCyc:1.14.13.93-RXN
 xref: RHEA:12897 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
 
 [Term]
@@ -127768,7 +127768,7 @@ synonym: "trans-cinnamic acid 4-hydroxylase activity" RELATED [EC:1.14.14.91]
 xref: EC:1.14.14.91 {source="skos:exactMatch"}
 xref: MetaCyc:TRANS-CINNAMATE-4-MONOOXYGENASE-RXN
 xref: RHEA:10608 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
 
 [Term]
@@ -127788,7 +127788,7 @@ xref: RHEA:61096 {source="skos:narrowMatch"}
 xref: RHEA:61112 {source="skos:narrowMatch"}
 xref: RHEA:61124 {source="skos:narrowMatch"}
 xref: RHEA:79895 {source="skos:narrowMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
 
 [Term]
@@ -139312,7 +139312,7 @@ xref: KEGG_REACTION:R01295
 xref: MetaCyc:BENZOATE-4-MONOOXYGENASE-RXN
 xref: RHEA:18033 {source="skos:exactMatch"}
 xref: UM-BBD_reactionID:r0623
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
 
 [Term]
@@ -201756,7 +201756,7 @@ xref: RHEA:55448 {source="skos:exactMatch"}
 xref: RHEA:61104 {source="skos:narrowMatch"}
 xref: RHEA:61108 {source="skos:narrowMatch"}
 xref: RHEA:61120 {source="skos:narrowMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/28526" xsd:anyURI
 
 [Term]
@@ -201797,7 +201797,7 @@ xref: EC:1.14.14.136 {source="skos:exactMatch"}
 xref: KEGG_REACTION:R05828
 xref: MetaCyc:1.14.13.91-RXN
 xref: RHEA:14237 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
 
 [Term]
@@ -201828,7 +201828,7 @@ xref: EC:1.14.14.138 {source="skos:exactMatch"}
 xref: KEGG_REACTION:R07203
 xref: MetaCyc:1.14.13.94-RXN
 xref: RHEA:18857 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
 
 [Term]
@@ -201886,7 +201886,7 @@ xref: EC:1.14.14.25 {source="skos:exactMatch"}
 xref: KEGG_REACTION:R07207
 xref: MetaCyc:1.14.13.98-RXN
 xref: RHEA:22716 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
 
 [Term]
@@ -228574,7 +228574,7 @@ xref: EC:1.14.14.144 {source="skos:exactMatch"}
 xref: KEGG_REACTION:R06351
 xref: MetaCyc:RXN-8507
 xref: RHEA:26217 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
 created_by: bf
 creation_date: 2012-04-19T10:57:05Z
@@ -228735,7 +228735,7 @@ def: "Catalysis of the reaction: ent-isokaurene + O2 + NADPH + H+ = ent-2alpha-h
 xref: EC:1.14.14.76 {source="skos:exactMatch"}
 xref: KEGG_REACTION:R09861
 xref: RHEA:56336 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
 created_by: bf
 creation_date: 2012-04-20T02:21:33Z
@@ -228749,7 +228749,7 @@ synonym: "ent-cassadiene C11alpha-hydroxylase activity" RELATED [EC:1.14.14.112]
 xref: EC:1.14.14.112 {source="skos:exactMatch"}
 xref: KEGG_REACTION:R09866
 xref: RHEA:31967 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
 created_by: bf
 creation_date: 2012-04-20T02:34:13Z
@@ -228776,7 +228776,7 @@ xref: EC:1.14.14.145 {source="skos:exactMatch"}
 xref: KEGG_REACTION:R06354
 xref: MetaCyc:RXN-12799
 xref: RHEA:26221 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
 created_by: bf
 creation_date: 2012-04-24T02:37:15Z
@@ -228848,7 +228848,7 @@ xref: EC:1.14.14.111 {source="skos:exactMatch"}
 xref: KEGG_REACTION:R09865
 xref: MetaCyc:RXN-15437
 xref: RHEA:31951 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/21412" xsd:anyURI
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
 created_by: bf
@@ -291822,7 +291822,7 @@ xref: EC:1.14.14.93 {source="skos:exactMatch"}
 xref: KEGG_REACTION:R03452
 xref: MetaCyc:RXN-4505
 xref: RHEA:15321 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
 
 [Term]
@@ -291836,7 +291836,7 @@ synonym: "trans-5-O-(4-coumaroyl)-D-quinate,NADPH:oxygen oxidoreductase (3'-hydr
 xref: EC:1.14.14.96 {source="skos:exactMatch"}
 xref: MetaCyc:1.14.13.36-RXN
 xref: RHEA:16265 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
 
 [Term]
@@ -291851,7 +291851,7 @@ synonym: "methyltetrahydroprotoberberine 14-hydroxylase activity" EXACT []
 xref: EC:1.14.14.97 {source="skos:exactMatch"}
 xref: MetaCyc:1.14.13.37-RXN
 xref: RHEA:23684 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
 
 [Term]
@@ -291894,7 +291894,7 @@ xref: EC:1.14.14.98 {source="skos:exactMatch"}
 xref: KEGG_REACTION:R04699
 xref: MetaCyc:1.14.13.55-RXN
 xref: RHEA:22644 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
 
 [Term]
@@ -291908,7 +291908,7 @@ xref: EC:1.14.14.100 {source="skos:exactMatch"}
 xref: KEGG_REACTION:R04702
 xref: MetaCyc:1.14.13.56-RXN
 xref: RHEA:10528 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
 
 [Term]
@@ -291922,7 +291922,7 @@ xref: EC:1.14.14.101 {source="skos:exactMatch"}
 xref: KEGG_REACTION:R04708
 xref: MetaCyc:1.14.13.57-RXN
 xref: RHEA:10156 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
 
 [Term]
@@ -305597,7 +305597,7 @@ synonym: "isoflavone 2'-monooxygenase activity" BROAD [EC:1.14.14.89]
 xref: EC:1.14.14.89 {source="skos:exactMatch"}
 xref: MetaCyc:ISOFLAVONE-2-HYDROXYLASE-RXN
 xref: RHEA:12388 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
... (246 more lines truncated)
```

### Attempt 8: claude-opus-4.7 / claude

- **Eval PR**: [#351](https://github.com/ai4curation/eval-ont-agent-go/pull/351)
- **F1**: 0.800  **Precision**: 0.667  **Recall**: 1.000  **Jaccard**: 0.667
- **Trace**: [25650704246](https://github.com/ai4curation/eval-ont-agent-go/tree/master/traces/25650704246)
- **Workflow run**: [25650704246](https://github.com/ai4curation/eval-ont-agent-go/actions/runs/25650704246)

#### Agent PR Comment

## Summary

Reparents 49 cytochrome P450 monooxygenase activity terms (all carrying `xref: EC:1.14.14.x {source="skos:exactMatch"}`) from GO:0016709 (EC:1.14.13.-) to GO:0016712 (EC:1.14.14.-).

This brings the GO `is_a` hierarchy into alignment with the IUBMB 2018 reclassification of most cytochrome P450 enzymes from sub-subclass 1.14.13 to 1.14.14, which the terms' EC xrefs already reflect.

## Changes

For each of the 49 terms listed in issue #31967, exactly one line was replaced:

```
- is_a: GO:0016709 ! oxidoreductase activity, ..., NAD(P)H as one donor, ...
+ is_a: GO:0016712 ! oxidoreductase activity, ..., reduced flavin or flavoprotein as one donor, ...
```

Diff stats: `1 file changed, 49 insertions(+), 49 deletions(-)`. Nothing else was modified — labels, definitions, synonyms, xrefs, other relationships, and metadata are untouched.

GO:0016712 already exists with `xref: EC:1.14.14.- {source="skos:exactMatch"}`, so no new term creation was needed. None of the 49 terms had a more-specific existing descendant of GO:0016712 that would have been a better fit, so all were reparented directly under GO:0016712.

## Rationale / design

- The `skos:exactMatch` EC xref on each term puts it unambiguously in EC sub-subclass 1.14.14, but the asserted `is_a` parent (GO:0016709) maps to EC sub-subclass 1.14.13. EC 1.14.13 and 1.14.14 are sibling sub-subclasses, not ancestor/descendant — so the previous `is_a` was inconsistent with the EC xref.
- This is a pure reparenting (`is_a` swap), not a logical-definition change. None of the affected terms had an `intersection_of` axiom referencing GO:0016709, so no logical-definition rewrites were required.
- Two of the 49 terms (e.g. GO:0008398 sterol 14-demethylase activity) retain a second `is_a` parent (GO:0032451 demethylase activity); only the GO:0016709 parent was swapped.

## Process / checklist

- [x] PLAN: issue analyzed, intent unambiguous (single bulk reparenting operation), plan recorded as todos
- [x] PRE-VALIDATION: `robot convert -i go-edit.obo -f obo` succeeded on the unmodified file
- [x] RESEARCH: not needed — issue body cites IUBMB 2018 EC reclassification and the target term GO:0016712 already exists with the correct EC xref
- [x] TERM-SEARCH: confirmed all 49 source terms and target term GO:0016712 exist; verified each source term currently has exactly one `is_a: GO:0016709`
- [x] DESIGN-PATTERNS: no new pattern instantiation; reparenting only
- [x] EDITS: used `obo-checkout.pl` → bulk edit in `terms/` → `obo-checkin.pl` workflow as required
- [x] RELATIONSHIPS: only the single inconsistent `is_a` parent was swapped; no logical definitions added or modified; secondary `is_a` parents (e.g. GO:0032451 on GO:0008398) preserved
- [x] SPECIALIZED-EDITS: N/A — no obsoletion, no CHEBI changes, no taxon constraints, no new RHEA/EC mappings
- [x] METADATA: no `created_by`/`creation_date` added (all terms pre-existing); no `term_tracker_item` added since these are mass-reparentings tracked under the umbrella issue and adding 49 new tracker links would be noise
- [x] AUTOMATED-VALIDATION:
  - ROBOT SPARQL-QC suite (16 rules): all PASS, 0 violations
  - ELK reasoning (`robot reason -r ELK`): completed successfully, no unsatisfiable classes
  - Note: `make travis_build` could not run end-to-end because `amm` (Ammonite Scala) is not installed in this sandbox; the underlying ROBOT checks were run individually
- [x] REFERENCE-VALIDATION: no new PMIDs or other references introduced
- [x] CHANGES-COMMITTED:
  - [x] only `src/ontology/go-edit.obo` modified and committed
  - [x] biologically correct (matches IUBMB EC classification)
  - [x] aligned with issue request — all 49 terms in the requested list, no additional scope
  - [x] PR description (this file) details rationale and validation
  - [x] short status comment prepared for the originating issue

---
🤖 **Generated by claude agent**
- Runtime: `claude`
- Model: `claude-opus-4-7`
- Agent config: `ai4curation/go-ontology-agent-config@v9:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-go/actions/runs/25650704246)


#### Agent Issue Comment

All 49 EC:1.14.14.x terms reparented from GO:0016709 (EC:1.14.13.-) to GO:0016712 (EC:1.14.14.-) in PR #<NN>, matching the IUBMB 2018 reclassification. No other axioms or metadata were touched.

Validation: ROBOT SPARQL-QC suite (16 rules) and ELK reasoning both pass with no new violations or unsatisfiable classes. The full `make travis_build` was not run because `amm` (Ammonite) is unavailable in this environment, but the rule and reasoner checks it normally drives are green.

---
🤖 **Generated by claude agent**
- Runtime: `claude`
- Model: `claude-opus-4-7`
- Agent config: `ai4curation/go-ontology-agent-config@v9:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-go/actions/runs/25650704246)


#### Agent Diff

```diff
diff --git a/src/ontology/go-edit.obo b/src/ontology/go-edit.obo
index 6dd226998..c8cf8aed8 100644
--- a/src/ontology/go-edit.obo
+++ b/src/ontology/go-edit.obo
@@ -43251,7 +43251,7 @@ xref: EC:1.14.14.17 {source="skos:exactMatch"}
 xref: KEGG_REACTION:R02874
 xref: MetaCyc:SQUALENE-MONOOXYGENASE-RXN
 xref: RHEA:25282 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
 
 [Term]
@@ -80692,7 +80692,7 @@ xref: RHEA:25286 {source="skos:narrowMatch"}
 xref: RHEA:45960 {source="skos:narrowMatch"}
 xref: RHEA:54028 {source="skos:exactMatch"}
 xref: RHEA:75439 {source="skos:narrowMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 is_a: GO:0032451 ! demethylase activity
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/22523" xsd:anyURI
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
@@ -102582,7 +102582,7 @@ xref: EC:1.14.14.137 {source="skos:exactMatch"}
 xref: KEGG_REACTION:R07202
 xref: MetaCyc:1.14.13.93-RXN
 xref: RHEA:12897 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
 
 [Term]
@@ -127768,7 +127768,7 @@ synonym: "trans-cinnamic acid 4-hydroxylase activity" RELATED [EC:1.14.14.91]
 xref: EC:1.14.14.91 {source="skos:exactMatch"}
 xref: MetaCyc:TRANS-CINNAMATE-4-MONOOXYGENASE-RXN
 xref: RHEA:10608 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
 
 [Term]
@@ -127788,7 +127788,7 @@ xref: RHEA:61096 {source="skos:narrowMatch"}
 xref: RHEA:61112 {source="skos:narrowMatch"}
 xref: RHEA:61124 {source="skos:narrowMatch"}
 xref: RHEA:79895 {source="skos:narrowMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
 
 [Term]
@@ -139312,7 +139312,7 @@ xref: KEGG_REACTION:R01295
 xref: MetaCyc:BENZOATE-4-MONOOXYGENASE-RXN
 xref: RHEA:18033 {source="skos:exactMatch"}
 xref: UM-BBD_reactionID:r0623
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
 
 [Term]
@@ -201756,7 +201756,7 @@ xref: RHEA:55448 {source="skos:exactMatch"}
 xref: RHEA:61104 {source="skos:narrowMatch"}
 xref: RHEA:61108 {source="skos:narrowMatch"}
 xref: RHEA:61120 {source="skos:narrowMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/28526" xsd:anyURI
 
 [Term]
@@ -201797,7 +201797,7 @@ xref: EC:1.14.14.136 {source="skos:exactMatch"}
 xref: KEGG_REACTION:R05828
 xref: MetaCyc:1.14.13.91-RXN
 xref: RHEA:14237 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
 
 [Term]
@@ -201828,7 +201828,7 @@ xref: EC:1.14.14.138 {source="skos:exactMatch"}
 xref: KEGG_REACTION:R07203
 xref: MetaCyc:1.14.13.94-RXN
 xref: RHEA:18857 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
 
 [Term]
@@ -201886,7 +201886,7 @@ xref: EC:1.14.14.25 {source="skos:exactMatch"}
 xref: KEGG_REACTION:R07207
 xref: MetaCyc:1.14.13.98-RXN
 xref: RHEA:22716 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
 
 [Term]
@@ -228574,7 +228574,7 @@ xref: EC:1.14.14.144 {source="skos:exactMatch"}
 xref: KEGG_REACTION:R06351
 xref: MetaCyc:RXN-8507
 xref: RHEA:26217 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
 created_by: bf
 creation_date: 2012-04-19T10:57:05Z
@@ -228735,7 +228735,7 @@ def: "Catalysis of the reaction: ent-isokaurene + O2 + NADPH + H+ = ent-2alpha-h
 xref: EC:1.14.14.76 {source="skos:exactMatch"}
 xref: KEGG_REACTION:R09861
 xref: RHEA:56336 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
 created_by: bf
 creation_date: 2012-04-20T02:21:33Z
@@ -228749,7 +228749,7 @@ synonym: "ent-cassadiene C11alpha-hydroxylase activity" RELATED [EC:1.14.14.112]
 xref: EC:1.14.14.112 {source="skos:exactMatch"}
 xref: KEGG_REACTION:R09866
 xref: RHEA:31967 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
 created_by: bf
 creation_date: 2012-04-20T02:34:13Z
@@ -228776,7 +228776,7 @@ xref: EC:1.14.14.145 {source="skos:exactMatch"}
 xref: KEGG_REACTION:R06354
 xref: MetaCyc:RXN-12799
 xref: RHEA:26221 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
 created_by: bf
 creation_date: 2012-04-24T02:37:15Z
@@ -228848,7 +228848,7 @@ xref: EC:1.14.14.111 {source="skos:exactMatch"}
 xref: KEGG_REACTION:R09865
 xref: MetaCyc:RXN-15437
 xref: RHEA:31951 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/21412" xsd:anyURI
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
 created_by: bf
@@ -291822,7 +291822,7 @@ xref: EC:1.14.14.93 {source="skos:exactMatch"}
 xref: KEGG_REACTION:R03452
 xref: MetaCyc:RXN-4505
 xref: RHEA:15321 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
 
 [Term]
@@ -291836,7 +291836,7 @@ synonym: "trans-5-O-(4-coumaroyl)-D-quinate,NADPH:oxygen oxidoreductase (3'-hydr
 xref: EC:1.14.14.96 {source="skos:exactMatch"}
 xref: MetaCyc:1.14.13.36-RXN
 xref: RHEA:16265 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
 
 [Term]
@@ -291851,7 +291851,7 @@ synonym: "methyltetrahydroprotoberberine 14-hydroxylase activity" EXACT []
 xref: EC:1.14.14.97 {source="skos:exactMatch"}
 xref: MetaCyc:1.14.13.37-RXN
 xref: RHEA:23684 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
 
 [Term]
@@ -291894,7 +291894,7 @@ xref: EC:1.14.14.98 {source="skos:exactMatch"}
 xref: KEGG_REACTION:R04699
 xref: MetaCyc:1.14.13.55-RXN
 xref: RHEA:22644 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
 
 [Term]
@@ -291908,7 +291908,7 @@ xref: EC:1.14.14.100 {source="skos:exactMatch"}
 xref: KEGG_REACTION:R04702
 xref: MetaCyc:1.14.13.56-RXN
 xref: RHEA:10528 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
 
 [Term]
@@ -291922,7 +291922,7 @@ xref: EC:1.14.14.101 {source="skos:exactMatch"}
 xref: KEGG_REACTION:R04708
 xref: MetaCyc:1.14.13.57-RXN
 xref: RHEA:10156 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
 
 [Term]
@@ -305597,7 +305597,7 @@ synonym: "isoflavone 2'-monooxygenase activity" BROAD [EC:1.14.14.89]
 xref: EC:1.14.14.89 {source="skos:exactMatch"}
 xref: MetaCyc:ISOFLAVONE-2-HYDROXYLASE-RXN
 xref: RHEA:12388 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
... (246 more lines truncated)
```

### Attempt 9: claude-haiku-4.5 / claude

- **Eval PR**: [#216](https://github.com/ai4curation/eval-ont-agent-go/pull/216)
- **F1**: 0.800  **Precision**: 0.667  **Recall**: 1.000  **Jaccard**: 0.667
- **Workflow run**: [25640388575](https://github.com/ai4curation/eval-ont-agent-go/actions/runs/25640388575)

#### Agent PR Comment

# PR Description: Reparent 49 EC:1.14.14.x terms from GO:0016709 to GO:0016712

## Summary

This PR addresses issue #31967 by reparenting 49 cytochrome P450 monooxygenase activity terms from GO:0016709 (EC:1.14.13.-) to GO:0016712 (EC:1.14.14.-), aligning with the IUBMB 2018 EC classification reclassification.

## Rationale

The affected terms all contain EC:1.14.14.x xrefs (exact matches to IUBMB EC sub-subclass 1.14.14), yet were previously classified under GO:0016709 which carries EC:1.14.13.- The reparenting establishes the correct EC hierarchy relationship: these terms now have a parent (GO:0016712) whose EC classification (1.14.14.-) properly encompasses their more specific EC numbers (1.14.14.x).

## Changes Made

### Updated is_a Relationships

For each of the 49 affected terms, the following change was made:
- **From:** `is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen`
- **To:** `is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen`

This correctly reflects that these cytochrome P450 monooxygenases use reduced flavin or flavoprotein as the electron donor, not NAD(P)H.

### Affected Terms (49)

GO:0004506, GO:0008398, GO:0010295, GO:0016710, GO:0016711, GO:0018664, GO:0033772, GO:0033775, GO:0033777, GO:0033781, GO:0036189, GO:0036201, GO:0036202, GO:0036204, GO:0036209, GO:0047082, GO:0047083, GO:0047084, GO:0047087, GO:0047088, GO:0047089, GO:0047957, GO:0048000, GO:0050591, GO:0050592, GO:0050593, GO:0050594, GO:0050596, GO:0050597, GO:0050598, GO:0102001, GO:0102002, GO:0102068, GO:0102170, GO:0102289, GO:0102320, GO:0102375, GO:0102556, GO:0102557, GO:0102596, GO:0102597, GO:0102598, GO:0102684, GO:0102811, GO:0102876, GO:0102934, GO:0102995, GO:0106144, GO:0106149

## Validation Checklist

- [x] PLAN: Issue analyzed and understood; reparenting approach is straightforward and low-risk
- [x] PRE-VALIDATION: Ontology validated before changes (file integrity confirmed)
- [x] RESEARCH: Not required - issue is based on documented IUBMB reclassification
- [x] TERM-SEARCH: All 49 affected terms located and verified to have EC:1.14.14.x xrefs
- [x] DESIGN-PATTERNS: Not applicable - simple reparenting, no new logical definitions
- [x] EDITS: Terms checked out, modified, and checked back in using standard ODK procedures
- [x] RELATIONSHIPS: All is_a relationships verified to correctly point to GO:0016712
- [x] SPECIALIZED-EDITS: No special edits required (no obsoletions, chemical entities, reactions, or taxon constraints)
- [x] METADATA: No new term metadata modifications required (existing metadata preserved)
- [x] AUTOMATED-VALIDATION: Syntax verified; file structure confirmed intact
- [x] REFERENCE-VALIDATION: No new references added (existing references preserved)
- [x] CHANGES-COMMITTED: Changes committed with detailed message

## Technical Details

### Procedure Used

1. Verified target terms (GO:0004506, etc.) contained EC:1.14.14.x xrefs
2. Confirmed GO:0016712 exists with EC:1.14.14.- classification
3. Checked out all 49 terms using `obo-checkout.pl`
4. Updated is_a relationships via sed pattern replacement
5. Checked terms back in using `obo-checkin.pl`
6. Verified all 49 terms now have GO:0016712 as parent
7. Committed changes to src/ontology/go-edit.obo

### Verification Results

- All 49 terms successfully modified (100% completion)
- No terms retained the old GO:0016709 parent (verified via grep)
- All terms confirmed to have GO:0016712 parent
- Ontology file integrity maintained

## Scope

This change is narrowly scoped to address the EC hierarchy inconsistency identified in issue #31967. No other modifications to these terms or related ontology content were made.

---
🤖 **Generated by claude agent**
- Runtime: `claude`
- Model: `claude-haiku-4-5-20251001`
- Agent config: `ai4curation/go-ontology-agent-config@v9:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-go/actions/runs/25640388575)


#### Agent Issue Comment

# Issue #31967 - Reparent 49 EC:1.14.14.x terms from GO:0016709 to GO:0016712

## Status: RESOLVED

Changes have been committed in PR #<NN>. All 49 cytochrome P450 monooxygenase activity terms with EC:1.14.14.x xrefs have been successfully reparented from GO:0016709 (EC:1.14.13.-) to GO:0016712 (EC:1.14.14.-), aligning the GO ontology with the IUBMB 2018 EC classification reclassification.

## Summary of Changes

- Reparented 49 terms from GO:0016709 to GO:0016712
- Updated is_a relationships for all affected terms
- EC classification hierarchy now correctly reflects the IUBMB reclassification

All affected terms have been verified to contain the correct parent relationship.

---
🤖 **Generated by claude agent**
- Runtime: `claude`
- Model: `claude-haiku-4-5-20251001`
- Agent config: `ai4curation/go-ontology-agent-config@v9:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-go/actions/runs/25640388575)


#### Agent Diff

```diff
diff --git a/src/ontology/go-edit.obo b/src/ontology/go-edit.obo
index 6dd226998..c8cf8aed8 100644
--- a/src/ontology/go-edit.obo
+++ b/src/ontology/go-edit.obo
@@ -43251,7 +43251,7 @@ xref: EC:1.14.14.17 {source="skos:exactMatch"}
 xref: KEGG_REACTION:R02874
 xref: MetaCyc:SQUALENE-MONOOXYGENASE-RXN
 xref: RHEA:25282 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
 
 [Term]
@@ -80692,7 +80692,7 @@ xref: RHEA:25286 {source="skos:narrowMatch"}
 xref: RHEA:45960 {source="skos:narrowMatch"}
 xref: RHEA:54028 {source="skos:exactMatch"}
 xref: RHEA:75439 {source="skos:narrowMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 is_a: GO:0032451 ! demethylase activity
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/22523" xsd:anyURI
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
@@ -102582,7 +102582,7 @@ xref: EC:1.14.14.137 {source="skos:exactMatch"}
 xref: KEGG_REACTION:R07202
 xref: MetaCyc:1.14.13.93-RXN
 xref: RHEA:12897 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
 
 [Term]
@@ -127768,7 +127768,7 @@ synonym: "trans-cinnamic acid 4-hydroxylase activity" RELATED [EC:1.14.14.91]
 xref: EC:1.14.14.91 {source="skos:exactMatch"}
 xref: MetaCyc:TRANS-CINNAMATE-4-MONOOXYGENASE-RXN
 xref: RHEA:10608 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
 
 [Term]
@@ -127788,7 +127788,7 @@ xref: RHEA:61096 {source="skos:narrowMatch"}
 xref: RHEA:61112 {source="skos:narrowMatch"}
 xref: RHEA:61124 {source="skos:narrowMatch"}
 xref: RHEA:79895 {source="skos:narrowMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
 
 [Term]
@@ -139312,7 +139312,7 @@ xref: KEGG_REACTION:R01295
 xref: MetaCyc:BENZOATE-4-MONOOXYGENASE-RXN
 xref: RHEA:18033 {source="skos:exactMatch"}
 xref: UM-BBD_reactionID:r0623
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
 
 [Term]
@@ -201756,7 +201756,7 @@ xref: RHEA:55448 {source="skos:exactMatch"}
 xref: RHEA:61104 {source="skos:narrowMatch"}
 xref: RHEA:61108 {source="skos:narrowMatch"}
 xref: RHEA:61120 {source="skos:narrowMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/28526" xsd:anyURI
 
 [Term]
@@ -201797,7 +201797,7 @@ xref: EC:1.14.14.136 {source="skos:exactMatch"}
 xref: KEGG_REACTION:R05828
 xref: MetaCyc:1.14.13.91-RXN
 xref: RHEA:14237 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
 
 [Term]
@@ -201828,7 +201828,7 @@ xref: EC:1.14.14.138 {source="skos:exactMatch"}
 xref: KEGG_REACTION:R07203
 xref: MetaCyc:1.14.13.94-RXN
 xref: RHEA:18857 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
 
 [Term]
@@ -201886,7 +201886,7 @@ xref: EC:1.14.14.25 {source="skos:exactMatch"}
 xref: KEGG_REACTION:R07207
 xref: MetaCyc:1.14.13.98-RXN
 xref: RHEA:22716 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
 
 [Term]
@@ -228574,7 +228574,7 @@ xref: EC:1.14.14.144 {source="skos:exactMatch"}
 xref: KEGG_REACTION:R06351
 xref: MetaCyc:RXN-8507
 xref: RHEA:26217 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
 created_by: bf
 creation_date: 2012-04-19T10:57:05Z
@@ -228735,7 +228735,7 @@ def: "Catalysis of the reaction: ent-isokaurene + O2 + NADPH + H+ = ent-2alpha-h
 xref: EC:1.14.14.76 {source="skos:exactMatch"}
 xref: KEGG_REACTION:R09861
 xref: RHEA:56336 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
 created_by: bf
 creation_date: 2012-04-20T02:21:33Z
@@ -228749,7 +228749,7 @@ synonym: "ent-cassadiene C11alpha-hydroxylase activity" RELATED [EC:1.14.14.112]
 xref: EC:1.14.14.112 {source="skos:exactMatch"}
 xref: KEGG_REACTION:R09866
 xref: RHEA:31967 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
 created_by: bf
 creation_date: 2012-04-20T02:34:13Z
@@ -228776,7 +228776,7 @@ xref: EC:1.14.14.145 {source="skos:exactMatch"}
 xref: KEGG_REACTION:R06354
 xref: MetaCyc:RXN-12799
 xref: RHEA:26221 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
 created_by: bf
 creation_date: 2012-04-24T02:37:15Z
@@ -228848,7 +228848,7 @@ xref: EC:1.14.14.111 {source="skos:exactMatch"}
 xref: KEGG_REACTION:R09865
 xref: MetaCyc:RXN-15437
 xref: RHEA:31951 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/21412" xsd:anyURI
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
 created_by: bf
@@ -291822,7 +291822,7 @@ xref: EC:1.14.14.93 {source="skos:exactMatch"}
 xref: KEGG_REACTION:R03452
 xref: MetaCyc:RXN-4505
 xref: RHEA:15321 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
 
 [Term]
@@ -291836,7 +291836,7 @@ synonym: "trans-5-O-(4-coumaroyl)-D-quinate,NADPH:oxygen oxidoreductase (3'-hydr
 xref: EC:1.14.14.96 {source="skos:exactMatch"}
 xref: MetaCyc:1.14.13.36-RXN
 xref: RHEA:16265 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
 
 [Term]
@@ -291851,7 +291851,7 @@ synonym: "methyltetrahydroprotoberberine 14-hydroxylase activity" EXACT []
 xref: EC:1.14.14.97 {source="skos:exactMatch"}
 xref: MetaCyc:1.14.13.37-RXN
 xref: RHEA:23684 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
 
 [Term]
@@ -291894,7 +291894,7 @@ xref: EC:1.14.14.98 {source="skos:exactMatch"}
 xref: KEGG_REACTION:R04699
 xref: MetaCyc:1.14.13.55-RXN
 xref: RHEA:22644 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
 
 [Term]
@@ -291908,7 +291908,7 @@ xref: EC:1.14.14.100 {source="skos:exactMatch"}
 xref: KEGG_REACTION:R04702
 xref: MetaCyc:1.14.13.56-RXN
 xref: RHEA:10528 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
 
 [Term]
@@ -291922,7 +291922,7 @@ xref: EC:1.14.14.101 {source="skos:exactMatch"}
 xref: KEGG_REACTION:R04708
 xref: MetaCyc:1.14.13.57-RXN
 xref: RHEA:10156 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
 
 [Term]
@@ -305597,7 +305597,7 @@ synonym: "isoflavone 2'-monooxygenase activity" BROAD [EC:1.14.14.89]
 xref: EC:1.14.14.89 {source="skos:exactMatch"}
 xref: MetaCyc:ISOFLAVONE-2-HYDROXYLASE-RXN
 xref: RHEA:12388 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
... (246 more lines truncated)
```

#### Review by gpt-5.5

**outcome**: success  **f1**: 0.8  **precision**: 0.667  **recall**: 1.0

<!-- Review this eval run following analysis/instructions/review-agent-eval.md

  Source issue: https://github.com/geneontology/go-ontology/issues/31967
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/31968
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/216
  Agent config: ai4curation/go-ontology-agent-config

  Quick reference:
    gh issue view 31967 --repo geneontology/go-ontology
    gh pr diff 31968 --repo geneontology/go-ontology
    gh pr diff 216 --repo ai4curation/eval-ont-agent-go
-->

## Summary

The agent correctly solved the core request in issue `#31967`: it reparented all 49 listed EC:1.14.14.x cytochrome-P450 monooxygenase activity terms from `GO:0016709` to `GO:0016712`, matching the human PR's substantive classification change. The metadiff F1 of 0.8 reflects a systematic metadata difference rather than a biomedical classification error: the human diff also added `term_tracker_item` provenance for issue `#31967` to each edited term, while the agent left existing metadata unchanged.


## Strengths

- Correctly identified `GO:0016712` as the target grouping term for EC:1.14.14.- activities: `oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen`.
- Replaced the incorrect `GO:0016709` parent on all 49 affected terms from the issue list, including `GO:0004506` `squalene monooxygenase activity`, `GO:0008398` `sterol 14-demethylase activity`, `GO:0016710` `trans-cinnamate 4-monooxygenase activity`, `GO:0036209` `9beta-pimara-7,15-diene oxidase activity`, `GO:0102375` `11-oxo-beta-amyrin 30-oxidase activity`, and `GO:0106149` `indole-3-carbonyl nitrile 4-hydroxylase activity`.
- Preserved other asserted parentage. In particular, `GO:0008398` kept its separate `is_a: GO:0032451 ! demethylase activity` while only the obsolete oxidoreductase grouping parent was swapped.
- Kept the edit narrowly scoped to the requested relationship changes in `src/ontology/go-edit.obo`; it did not alter labels, definitions, EC/RHEA xrefs, synonyms, or logical definitions.
- The PR notes show a reasonable process: the agent recognized the EC hierarchy mismatch, verified the 49 EC:1.14.14.x targets, confirmed `GO:0016712` as the existing EC:1.14.14.- grouping term, and reported validation of the parent replacements.


## Issues

- Minor provenance omission relative to the accepted human PR: the agent did not add `property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31967" xsd:anyURI` to the 49 edited term stanzas. The source issue asked for the reparenting, which the agent completed, but the human solution added these tracker links for traceability.
- No wrong terms, missed target terms, syntax problems, or unsupported parent choices were found. The agent chose the same direct parent `GO:0016712` as the human PR rather than an inappropriate more-specific descendant.

### Attempt 10: gpt-5.4 / codex

- **Eval PR**: [#191](https://github.com/ai4curation/eval-ont-agent-go/pull/191)
- **F1**: 0.800  **Precision**: 0.667  **Recall**: 1.000  **Jaccard**: 0.667
- **Workflow run**: [25640338516](https://github.com/ai4curation/eval-ont-agent-go/actions/runs/25640338516)

#### Agent PR Comment

# Summary

This change reparents the 49 terms listed in issue `#31967` from:

- `GO:0016709` oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen

to:

- `GO:0016712` oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen

The issue is an EC/GO hierarchy mismatch: each affected term already has `xref: EC:1.14.14.x {source="skos:exactMatch"}`, but was asserted under the `EC:1.14.13.-` grouping term. The reparenting aligns the GO asserted hierarchy with the current EC classification and with existing GO precedent for other `EC:1.14.14.x` catalytic activity terms.

# Rationale

I checked official IUBMB/ENZYME sources and documented them in `RESEARCH.md`. Representative entries such as `EC:1.14.14.91` and `EC:1.14.14.114` explicitly note transfer in 2018 from `EC:1.14.13.x` to `EC:1.14.14.x`. The `1.14.14.-` class page also includes many of the issue terms directly.

This was handled as an asserted-parent correction only:

- no new terms
- no definition changes
- no logical definition (`intersection_of`) changes
- no metadata changes beyond the hierarchy update

Additional asserted parents, such as substrate-specific hydroxylase or demethylase parents, were preserved unchanged.

# Validation

- Verified all 49 issue-listed GO IDs existed and were initially under `GO:0016709`.
- Checked GO precedent for existing `EC:1.14.14.x` terms already curated under `GO:0016712`.
- Edited via `obo-checkout.pl` / `obo-checkin.pl` using checked-out term stanzas in `terms/`.
- Confirmed all 49 targets now have `is_a: GO:0016712` and none retain `is_a: GO:0016709`.
- Ran `cd src/ontology && make travis_build` successfully after the change.

# Checklist

- [x] PLAN: The issue and its context were analyzed and the intent was clear.
- [x] PRE-VALIDATION: Local validation succeeded before the edit.
- [x] RESEARCH: Background research recorded in `RESEARCH.md`.
- [x] TERM-SEARCH: Relevant GO terms and branch precedent were checked.
- [x] DESIGN-PATTERNS: Relevant pattern constraints documented in `DESIGN_PATTERNS.md`.
- [x] EDITS: Used checkout/checkin workflow rather than direct editing of `go-edit.obo`.
- [x] RELATIONSHIPS: Updated asserted `is_a` relationships appropriately.
- [x] logical definitions are appropriate, and are not over-specified, and conform to DESIGN_PATTERNS.md doc
- [x] relationships conform to other similar terms in the ontology
- [x] is_a is not over-asserted
- [x] is_a, part_of, and other relationships specified appropriately
- [x] SPECIALIZED-EDITS: `/reaction` skill applied; no term obsoletion, CHEBI, mapping, or taxon-constraint edits were needed.
- [x] METADATA: No new terms were created; existing metadata was preserved.
- [x] AUTOMATED-VALIDATION: `make travis_build` passed after changes.
- [x] REFERENCE-VALIDATION: No new GO references were introduced; external classification evidence was checked in `RESEARCH.md`.
- [x] CHANGES-COMMITTED
- [x] RELEVANT-FILES: Only `src/ontology/go-edit.obo` was committed.
- [x] ACCURACY: Changes align with current EC classification and existing GO curation precedent.
- [x] ISSUE-ALIGNMENT: Changes match the requested 49-term reparenting.
- [x] PR is created or amended
- [x] Communicate high level summary of changes on original issue(s), and any requests for further info
- [x] Communicated on PR detailed description of changes made, and rationale. Include checklists.

---
🤖 **Generated by codex agent**
- Runtime: `codex`
- Model: `gpt-5.4`
- Agent config: `ai4curation/go-ontology-agent-config@v9:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-go/actions/runs/25640338516)

#### Agent Issue Comment

Reparenting changes for this issue have been committed in PR #<NN>.

I updated the 49 listed molecular function terms so their asserted parent now matches their exact EC `1.14.14.x` xrefs and the current IUBMB/ENZYME classification, moving them from `GO:0016709` (`EC:1.14.13.-`) to `GO:0016712` (`EC:1.14.14.-`).

Validation passed locally with `cd src/ontology && make travis_build`.

---
🤖 **Generated by codex agent**
- Runtime: `codex`
- Model: `gpt-5.4`
- Agent config: `ai4curation/go-ontology-agent-config@v9:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-go/actions/runs/25640338516)

#### Agent Diff

```diff
diff --git a/src/ontology/go-edit.obo b/src/ontology/go-edit.obo
index 6dd226998..c8cf8aed8 100644
--- a/src/ontology/go-edit.obo
+++ b/src/ontology/go-edit.obo
@@ -43251,7 +43251,7 @@ xref: EC:1.14.14.17 {source="skos:exactMatch"}
 xref: KEGG_REACTION:R02874
 xref: MetaCyc:SQUALENE-MONOOXYGENASE-RXN
 xref: RHEA:25282 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
 
 [Term]
@@ -80692,7 +80692,7 @@ xref: RHEA:25286 {source="skos:narrowMatch"}
 xref: RHEA:45960 {source="skos:narrowMatch"}
 xref: RHEA:54028 {source="skos:exactMatch"}
 xref: RHEA:75439 {source="skos:narrowMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 is_a: GO:0032451 ! demethylase activity
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/22523" xsd:anyURI
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
@@ -102582,7 +102582,7 @@ xref: EC:1.14.14.137 {source="skos:exactMatch"}
 xref: KEGG_REACTION:R07202
 xref: MetaCyc:1.14.13.93-RXN
 xref: RHEA:12897 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
 
 [Term]
@@ -127768,7 +127768,7 @@ synonym: "trans-cinnamic acid 4-hydroxylase activity" RELATED [EC:1.14.14.91]
 xref: EC:1.14.14.91 {source="skos:exactMatch"}
 xref: MetaCyc:TRANS-CINNAMATE-4-MONOOXYGENASE-RXN
 xref: RHEA:10608 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
 
 [Term]
@@ -127788,7 +127788,7 @@ xref: RHEA:61096 {source="skos:narrowMatch"}
 xref: RHEA:61112 {source="skos:narrowMatch"}
 xref: RHEA:61124 {source="skos:narrowMatch"}
 xref: RHEA:79895 {source="skos:narrowMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
 
 [Term]
@@ -139312,7 +139312,7 @@ xref: KEGG_REACTION:R01295
 xref: MetaCyc:BENZOATE-4-MONOOXYGENASE-RXN
 xref: RHEA:18033 {source="skos:exactMatch"}
 xref: UM-BBD_reactionID:r0623
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
 
 [Term]
@@ -201756,7 +201756,7 @@ xref: RHEA:55448 {source="skos:exactMatch"}
 xref: RHEA:61104 {source="skos:narrowMatch"}
 xref: RHEA:61108 {source="skos:narrowMatch"}
 xref: RHEA:61120 {source="skos:narrowMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/28526" xsd:anyURI
 
 [Term]
@@ -201797,7 +201797,7 @@ xref: EC:1.14.14.136 {source="skos:exactMatch"}
 xref: KEGG_REACTION:R05828
 xref: MetaCyc:1.14.13.91-RXN
 xref: RHEA:14237 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
 
 [Term]
@@ -201828,7 +201828,7 @@ xref: EC:1.14.14.138 {source="skos:exactMatch"}
 xref: KEGG_REACTION:R07203
 xref: MetaCyc:1.14.13.94-RXN
 xref: RHEA:18857 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
 
 [Term]
@@ -201886,7 +201886,7 @@ xref: EC:1.14.14.25 {source="skos:exactMatch"}
 xref: KEGG_REACTION:R07207
 xref: MetaCyc:1.14.13.98-RXN
 xref: RHEA:22716 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
 
 [Term]
@@ -228574,7 +228574,7 @@ xref: EC:1.14.14.144 {source="skos:exactMatch"}
 xref: KEGG_REACTION:R06351
 xref: MetaCyc:RXN-8507
 xref: RHEA:26217 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
 created_by: bf
 creation_date: 2012-04-19T10:57:05Z
@@ -228735,7 +228735,7 @@ def: "Catalysis of the reaction: ent-isokaurene + O2 + NADPH + H+ = ent-2alpha-h
 xref: EC:1.14.14.76 {source="skos:exactMatch"}
 xref: KEGG_REACTION:R09861
 xref: RHEA:56336 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
 created_by: bf
 creation_date: 2012-04-20T02:21:33Z
@@ -228749,7 +228749,7 @@ synonym: "ent-cassadiene C11alpha-hydroxylase activity" RELATED [EC:1.14.14.112]
 xref: EC:1.14.14.112 {source="skos:exactMatch"}
 xref: KEGG_REACTION:R09866
 xref: RHEA:31967 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
 created_by: bf
 creation_date: 2012-04-20T02:34:13Z
@@ -228776,7 +228776,7 @@ xref: EC:1.14.14.145 {source="skos:exactMatch"}
 xref: KEGG_REACTION:R06354
 xref: MetaCyc:RXN-12799
 xref: RHEA:26221 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
 created_by: bf
 creation_date: 2012-04-24T02:37:15Z
@@ -228848,7 +228848,7 @@ xref: EC:1.14.14.111 {source="skos:exactMatch"}
 xref: KEGG_REACTION:R09865
 xref: MetaCyc:RXN-15437
 xref: RHEA:31951 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/21412" xsd:anyURI
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
 created_by: bf
@@ -291822,7 +291822,7 @@ xref: EC:1.14.14.93 {source="skos:exactMatch"}
 xref: KEGG_REACTION:R03452
 xref: MetaCyc:RXN-4505
 xref: RHEA:15321 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
 
 [Term]
@@ -291836,7 +291836,7 @@ synonym: "trans-5-O-(4-coumaroyl)-D-quinate,NADPH:oxygen oxidoreductase (3'-hydr
 xref: EC:1.14.14.96 {source="skos:exactMatch"}
 xref: MetaCyc:1.14.13.36-RXN
 xref: RHEA:16265 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
 
 [Term]
@@ -291851,7 +291851,7 @@ synonym: "methyltetrahydroprotoberberine 14-hydroxylase activity" EXACT []
 xref: EC:1.14.14.97 {source="skos:exactMatch"}
 xref: MetaCyc:1.14.13.37-RXN
 xref: RHEA:23684 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
 
 [Term]
@@ -291894,7 +291894,7 @@ xref: EC:1.14.14.98 {source="skos:exactMatch"}
 xref: KEGG_REACTION:R04699
 xref: MetaCyc:1.14.13.55-RXN
 xref: RHEA:22644 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
 
 [Term]
@@ -291908,7 +291908,7 @@ xref: EC:1.14.14.100 {source="skos:exactMatch"}
 xref: KEGG_REACTION:R04702
 xref: MetaCyc:1.14.13.56-RXN
 xref: RHEA:10528 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
 
 [Term]
@@ -291922,7 +291922,7 @@ xref: EC:1.14.14.101 {source="skos:exactMatch"}
 xref: KEGG_REACTION:R04708
 xref: MetaCyc:1.14.13.57-RXN
 xref: RHEA:10156 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
 
 [Term]
@@ -305597,7 +305597,7 @@ synonym: "isoflavone 2'-monooxygenase activity" BROAD [EC:1.14.14.89]
 xref: EC:1.14.14.89 {source="skos:exactMatch"}
 xref: MetaCyc:ISOFLAVONE-2-HYDROXYLASE-RXN
 xref: RHEA:12388 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
... (246 more lines truncated)
```

#### Review by gpt-5.5

**outcome**: success  **f1**: 0.8  **precision**: 0.667  **recall**: 1.0

<!-- Review this eval run following analysis/instructions/review-agent-eval.md

  Source issue: https://github.com/geneontology/go-ontology/issues/31967
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/31968
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/191
  Agent config: ai4curation/go-ontology-agent-config

  Quick reference:
    gh issue view 31967 --repo geneontology/go-ontology
    gh pr diff 31968 --repo geneontology/go-ontology
    gh pr diff 191 --repo ai4curation/eval-ont-agent-go
-->

## Summary

The agent correctly addressed the core ontology request in issue `#31967`: all 49 EC:1.14.14.x cytochrome-P450 monooxygenase activity terms were reparented from `GO:0016709` to `GO:0016712`, matching the human PR's relationship changes. The metadiff F1 of 0.8 mostly reflects a systematic provenance difference rather than a wrong classification: the human PR also added `term_tracker_item` metadata for issue `#31967` on every edited term, while the agent left metadata unchanged.


## Strengths

- Correctly selected the target parent `GO:0016712` `oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen`, the existing grouping term with `EC:1.14.14.-`.
- Replaced the outdated `GO:0016709` parent on all 49 issue-listed EC:1.14.14.x terms, including representative targets `GO:0004506` `squalene monooxygenase activity`, `GO:0008398` `sterol 14-demethylase activity`, `GO:0016710` `trans-cinnamate 4-monooxygenase activity`, `GO:0036209` `9beta-pimara-7,15-diene oxidase activity`, `GO:0102375` `11-oxo-beta-amyrin 30-oxidase activity`, and `GO:0106149` `indole-3-carbonyl nitrile 4-hydroxylase activity`.
- Preserved additional asserted parents where present; for example, `GO:0008398` kept its separate `is_a: GO:0032451 ! demethylase activity` while only the oxidoreductase grouping parent changed.
- Kept the scope tight: the agent changed only `src/ontology/go-edit.obo`, made 49 parent replacements, and did not alter labels, definitions, EC/RHEA xrefs, synonyms, or logical definitions.
- The agent PR notes indicate a reasonable methodology: it recognized the EC hierarchy mismatch, checked `GO:0016712` as the existing EC:1.14.14.- grouping term, and reported post-edit validation.


## Issues

- Minor provenance omission relative to the human PR: the agent did not add `property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31967" xsd:anyURI` to the 49 edited terms. The issue itself asked for the reparenting and the agent completed that, but the accepted PR added these tracker links for traceability.
- No substantive classification errors or missed target terms were found. The agent used the same parent replacement as the human PR rather than choosing an unsupported more-specific descendant.

### Attempt 11: gpt-5.5 / codex

- **Eval PR**: [#58](https://github.com/ai4curation/eval-ont-agent-go/pull/58)
- **F1**: 0.800  **Precision**: 0.667  **Recall**: 1.000  **Jaccard**: 0.667
- **Trace**: [25615854862](https://github.com/ai4curation/eval-ont-agent-go/tree/master/traces/25615854862)
- **Workflow run**: [25615854862](https://github.com/ai4curation/eval-ont-agent-go/actions/runs/25615854862)

#### Agent PR Comment

## Summary

Addressed issue #31967 by reparenting the 49 listed EC:1.14.14.x monooxygenase/oxidoreductase molecular function terms from:

- `GO:0016709` oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen

to:

- `GO:0016712` oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen

This aligns the asserted GO hierarchy with the existing exact EC mappings on those terms and with the existing `GO:0016712` exact mapping to `EC:1.14.14.-`.

## Rationale

All 49 affected terms were confirmed to have exact `EC:1.14.14.*` xrefs and a direct asserted `is_a: GO:0016709` parent before editing. `GO:0016709` is mapped to `EC:1.14.13.-`, while the requested target parent `GO:0016712` is mapped to `EC:1.14.14.-`. Existing EC:1.14.14.* terms in this part of the ontology are already directly parented to `GO:0016712`, so the change follows existing ontology precedent.

No names, definitions, synonyms, xrefs, term tracker metadata, or logical definitions were changed. No new references were introduced.

## Validation

- Pre-validation before edits: `cd src/ontology && make travis_build` passed.
- Post-edit validation: `cd src/ontology && make travis_build` passed.
- Diff check: exactly 49 `GO:0016709` parent assertions removed and 49 `GO:0016712` parent assertions added.
- `git diff --check -- src/ontology/go-edit.obo` passed.

## Checklist

- [x] PLAN: Issue context analyzed; request was clear and actionable.
- [x] PRE-VALIDATION: Current ontology validated before edits with `make travis_build`.
- [x] RESEARCH: N/A; no new biological claims or references were introduced. The work is an EC hierarchy alignment based on existing GO and EC xrefs.
- [x] TERM-SEARCH: Affected GO terms, source parent, target parent, and existing EC:1.14.14.* precedent terms were checked with `obo-grep.pl`.
- [x] DESIGN-PATTERNS: Checked relevant design-pattern guidance; no DOSDP pattern applies to this parent-only MF EC hierarchy correction, and no logical definitions were added.
- [x] EDITS: Used `obo-checkout.pl`, edited checked-out term files, and checked changes back into `src/ontology/go-edit.obo` with `obo-checkin.pl`.
- [x] RELATIONSHIPS: Updated only the direct asserted `is_a` parent from `GO:0016709` to `GO:0016712`.
- [x] SPECIALIZED-EDITS: Reaction/mapping considerations checked because these are EC-backed catalytic activity terms. Obsoletion, taxon constraints, and CHEBI logical-definition work were N/A.
- [x] METADATA: N/A; no new terms or metadata changes.
- [x] AUTOMATED-VALIDATION: Post-edit `make travis_build` passed.
- [x] REFERENCE-VALIDATION: N/A; no references were added or changed.
- [x] CHANGES-COMMITTED: Ontology change committed locally.

---
🤖 **Generated by codex agent**
- Runtime: `codex`
- Model: `gpt-5.5`
- Agent config: `ai4curation/go-ontology-agent-config@v9:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-go/actions/runs/25615854862)


#### Agent Issue Comment

Implemented the requested EC hierarchy cleanup: the 49 EC:1.14.14.x monooxygenase activity terms listed in this issue now use `GO:0016712` as their asserted parent instead of `GO:0016709`.

The change is committed locally and validation passed with `cd src/ontology && make travis_build`. Changes committed in PR #<NN>.

---
🤖 **Generated by codex agent**
- Runtime: `codex`
- Model: `gpt-5.5`
- Agent config: `ai4curation/go-ontology-agent-config@v9:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-go/actions/runs/25615854862)


#### Agent Diff

```diff
diff --git a/src/ontology/go-edit.obo b/src/ontology/go-edit.obo
index 6dd226998..c8cf8aed8 100644
--- a/src/ontology/go-edit.obo
+++ b/src/ontology/go-edit.obo
@@ -43251,7 +43251,7 @@ xref: EC:1.14.14.17 {source="skos:exactMatch"}
 xref: KEGG_REACTION:R02874
 xref: MetaCyc:SQUALENE-MONOOXYGENASE-RXN
 xref: RHEA:25282 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
 
 [Term]
@@ -80692,7 +80692,7 @@ xref: RHEA:25286 {source="skos:narrowMatch"}
 xref: RHEA:45960 {source="skos:narrowMatch"}
 xref: RHEA:54028 {source="skos:exactMatch"}
 xref: RHEA:75439 {source="skos:narrowMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 is_a: GO:0032451 ! demethylase activity
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/22523" xsd:anyURI
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
@@ -102582,7 +102582,7 @@ xref: EC:1.14.14.137 {source="skos:exactMatch"}
 xref: KEGG_REACTION:R07202
 xref: MetaCyc:1.14.13.93-RXN
 xref: RHEA:12897 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
 
 [Term]
@@ -127768,7 +127768,7 @@ synonym: "trans-cinnamic acid 4-hydroxylase activity" RELATED [EC:1.14.14.91]
 xref: EC:1.14.14.91 {source="skos:exactMatch"}
 xref: MetaCyc:TRANS-CINNAMATE-4-MONOOXYGENASE-RXN
 xref: RHEA:10608 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
 
 [Term]
@@ -127788,7 +127788,7 @@ xref: RHEA:61096 {source="skos:narrowMatch"}
 xref: RHEA:61112 {source="skos:narrowMatch"}
 xref: RHEA:61124 {source="skos:narrowMatch"}
 xref: RHEA:79895 {source="skos:narrowMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
 
 [Term]
@@ -139312,7 +139312,7 @@ xref: KEGG_REACTION:R01295
 xref: MetaCyc:BENZOATE-4-MONOOXYGENASE-RXN
 xref: RHEA:18033 {source="skos:exactMatch"}
 xref: UM-BBD_reactionID:r0623
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
 
 [Term]
@@ -201756,7 +201756,7 @@ xref: RHEA:55448 {source="skos:exactMatch"}
 xref: RHEA:61104 {source="skos:narrowMatch"}
 xref: RHEA:61108 {source="skos:narrowMatch"}
 xref: RHEA:61120 {source="skos:narrowMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/28526" xsd:anyURI
 
 [Term]
@@ -201797,7 +201797,7 @@ xref: EC:1.14.14.136 {source="skos:exactMatch"}
 xref: KEGG_REACTION:R05828
 xref: MetaCyc:1.14.13.91-RXN
 xref: RHEA:14237 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
 
 [Term]
@@ -201828,7 +201828,7 @@ xref: EC:1.14.14.138 {source="skos:exactMatch"}
 xref: KEGG_REACTION:R07203
 xref: MetaCyc:1.14.13.94-RXN
 xref: RHEA:18857 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
 
 [Term]
@@ -201886,7 +201886,7 @@ xref: EC:1.14.14.25 {source="skos:exactMatch"}
 xref: KEGG_REACTION:R07207
 xref: MetaCyc:1.14.13.98-RXN
 xref: RHEA:22716 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
 
 [Term]
@@ -228574,7 +228574,7 @@ xref: EC:1.14.14.144 {source="skos:exactMatch"}
 xref: KEGG_REACTION:R06351
 xref: MetaCyc:RXN-8507
 xref: RHEA:26217 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
 created_by: bf
 creation_date: 2012-04-19T10:57:05Z
@@ -228735,7 +228735,7 @@ def: "Catalysis of the reaction: ent-isokaurene + O2 + NADPH + H+ = ent-2alpha-h
 xref: EC:1.14.14.76 {source="skos:exactMatch"}
 xref: KEGG_REACTION:R09861
 xref: RHEA:56336 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
 created_by: bf
 creation_date: 2012-04-20T02:21:33Z
@@ -228749,7 +228749,7 @@ synonym: "ent-cassadiene C11alpha-hydroxylase activity" RELATED [EC:1.14.14.112]
 xref: EC:1.14.14.112 {source="skos:exactMatch"}
 xref: KEGG_REACTION:R09866
 xref: RHEA:31967 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
 created_by: bf
 creation_date: 2012-04-20T02:34:13Z
@@ -228776,7 +228776,7 @@ xref: EC:1.14.14.145 {source="skos:exactMatch"}
 xref: KEGG_REACTION:R06354
 xref: MetaCyc:RXN-12799
 xref: RHEA:26221 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
 created_by: bf
 creation_date: 2012-04-24T02:37:15Z
@@ -228848,7 +228848,7 @@ xref: EC:1.14.14.111 {source="skos:exactMatch"}
 xref: KEGG_REACTION:R09865
 xref: MetaCyc:RXN-15437
 xref: RHEA:31951 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/21412" xsd:anyURI
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
 created_by: bf
@@ -291822,7 +291822,7 @@ xref: EC:1.14.14.93 {source="skos:exactMatch"}
 xref: KEGG_REACTION:R03452
 xref: MetaCyc:RXN-4505
 xref: RHEA:15321 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
 
 [Term]
@@ -291836,7 +291836,7 @@ synonym: "trans-5-O-(4-coumaroyl)-D-quinate,NADPH:oxygen oxidoreductase (3'-hydr
 xref: EC:1.14.14.96 {source="skos:exactMatch"}
 xref: MetaCyc:1.14.13.36-RXN
 xref: RHEA:16265 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
 
 [Term]
@@ -291851,7 +291851,7 @@ synonym: "methyltetrahydroprotoberberine 14-hydroxylase activity" EXACT []
 xref: EC:1.14.14.97 {source="skos:exactMatch"}
 xref: MetaCyc:1.14.13.37-RXN
 xref: RHEA:23684 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
 
 [Term]
@@ -291894,7 +291894,7 @@ xref: EC:1.14.14.98 {source="skos:exactMatch"}
 xref: KEGG_REACTION:R04699
 xref: MetaCyc:1.14.13.55-RXN
 xref: RHEA:22644 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
 
 [Term]
@@ -291908,7 +291908,7 @@ xref: EC:1.14.14.100 {source="skos:exactMatch"}
 xref: KEGG_REACTION:R04702
 xref: MetaCyc:1.14.13.56-RXN
 xref: RHEA:10528 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
 
 [Term]
@@ -291922,7 +291922,7 @@ xref: EC:1.14.14.101 {source="skos:exactMatch"}
 xref: KEGG_REACTION:R04708
 xref: MetaCyc:1.14.13.57-RXN
 xref: RHEA:10156 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
 
 [Term]
@@ -305597,7 +305597,7 @@ synonym: "isoflavone 2'-monooxygenase activity" BROAD [EC:1.14.14.89]
 xref: EC:1.14.14.89 {source="skos:exactMatch"}
 xref: MetaCyc:ISOFLAVONE-2-HYDROXYLASE-RXN
 xref: RHEA:12388 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
... (246 more lines truncated)
```

#### Review by gpt-5.5

**outcome**: success  **f1**: 0.8  **precision**: 0.667  **recall**: 1.0

<!-- Review this eval run following analysis/instructions/review-agent-eval.md

  Source issue: https://github.com/geneontology/go-ontology/issues/31967
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/31968
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/58
  Agent config: ai4curation/go-ontology-agent-config

  Quick reference:
    gh issue view 31967 --repo geneontology/go-ontology
    gh pr diff 31968 --repo geneontology/go-ontology
    gh pr diff 58 --repo ai4curation/eval-ont-agent-go
-->

## Summary

The agent correctly addressed the core ontology request in issue `#31967`: it reparented all 49 listed EC:1.14.14.x cytochrome-P450 monooxygenase activity terms from `GO:0016709` to `GO:0016712`, matching the human PR's substantive relationship changes. The metadiff F1 of 0.8 under-represents the biological quality of the edit: the mismatch is systematic provenance metadata, because the human PR also added `term_tracker_item` links for issue `#31967` to each changed term while the agent left metadata untouched.


## Strengths

- Correctly selected `GO:0016712` as the target parent, the existing EC:1.14.14.- grouping term for oxidoreductase activity using a reduced flavin or flavoprotein donor.
- Replaced the incorrect `GO:0016709` parent on all 49 issue-listed EC:1.14.14.x terms, including `GO:0004506` `squalene monooxygenase activity`, `GO:0008398` `sterol 14-demethylase activity`, `GO:0016710` `trans-cinnamate 4-monooxygenase activity`, `GO:0036209` `9beta-pimara-7,15-diene oxidase activity`, `GO:0102375` `11-oxo-beta-amyrin 30-oxidase activity`, and `GO:0106149` `indole-3-carbonyl nitrile 4-hydroxylase activity`.
- Preserved other asserted parentage. In particular, `GO:0008398` retained its separate `is_a: GO:0032451 ! demethylase activity` while only the oxidoreductase grouping parent was changed.
- Kept the edit tightly scoped to `src/ontology/go-edit.obo`: the agent changed the requested `is_a` assertions and did not alter labels, definitions, EC/RHEA xrefs, synonyms, or logical definitions.
- The agent's PR notes show a reasonable method: it recognized the EC hierarchy mismatch, identified `GO:0016712` as the existing EC:1.14.14.- grouping term, checked that each target no longer had `GO:0016709`, and reported local validation limits separately from content checks.


## Issues

- Minor provenance omission relative to the accepted human PR: the agent did not add `property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31967" xsd:anyURI` to the 49 edited term stanzas. The source issue asked for the reparenting, which the agent completed, but the human solution added these tracker links for traceability.
- No substantive classification errors, wrong-term edits, missed target terms, or syntax problems were found. The issue allowed `GO:0016712` or a more specific descendant where one exists; the agent chose the same direct parent as the accepted human PR.
