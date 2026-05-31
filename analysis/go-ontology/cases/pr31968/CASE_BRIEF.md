---
ontology: go-ontology
repo: geneontology/go-ontology
issue_number: 31967
pr_number: 31968
issue_title: Reparent 49 EC:1.14.14.x terms from GO:0016709 to GO:0016712 (CYP450
  reclassification)
pr_author: sjm41
pr_merged_at: '2026-04-24'
task_type: reclassification
difficulty: medium
scoping: tightly_scoped
scope: structural_refactor
review_outcome: approved_first_time
num_agent_attempts: 13
generated_at: '2026-05-17'
scoping_notes: Every change is a reparent of an EC:1.14.14.x term from GO:0016709
  to GO:0016712, plus term_tracker_item provenance additions. No unrelated edits.
domain_area: molecular_function
best_f1: 1.0
best_model: gpt-5.4
---

# PR #31968 — Reparent 49 EC:1.14.14.x terms from GO:0016709 to GO:0016712 (CYP450 reclassification)

**go-ontology** | [geneontology/go-ontology](https://github.com/geneontology/go-ontology) | [Issue #31967](https://github.com/geneontology/go-ontology/issues/31967) | [PR #31968](https://github.com/geneontology/go-ontology/pull/31968) | @sjm41 | merged 2026-04-24

`reclassification` `medium` `tightly_scoped` `approved_first_time`

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

## Agent Attempts (13)

| # | Model | Runtime | F1 | P | R | Blob | Eval PR | Detail |
|---|-------|---------|-----|-----|-----|------|---------|--------|
| 1 | gpt-5.4 | opencode | 1.000 | 1.000 | 1.000 | `b2469c2` | [#649](https://github.com/ai4curation/eval-ont-agent-go/pull/649) | [attempt](attempts/pr649.md) |
| 2 | gpt-5.4 | opencode | 1.000 | 1.000 | 1.000 | `b2469c2` | [#600](https://github.com/ai4curation/eval-ont-agent-go/pull/600) | [attempt](attempts/pr600.md) |
| 3 | gpt-5.5 | opencode | 1.000 | 1.000 | 1.000 | `b2469c2` | [#98](https://github.com/ai4curation/eval-ont-agent-go/pull/98) | [attempt](attempts/pr98.md) |
| 4 | gpt-5.5 | opencode | 1.000 | 1.000 | 1.000 | `b2469c2` | [#77](https://github.com/ai4curation/eval-ont-agent-go/pull/77) | [attempt](attempts/pr77.md) |
| 5 | gemma-4-31b | opencode | 0.800 | 0.667 | 1.000 | `c8cf8ae` | [#533](https://github.com/ai4curation/eval-ont-agent-go/pull/533) | [attempt](attempts/pr533.md) |
| 6 | gemma-4-31b | opencode | 0.800 | 0.667 | 1.000 | `c8cf8ae` | [#510](https://github.com/ai4curation/eval-ont-agent-go/pull/510) | [attempt](attempts/pr510.md) |
| 7 | claude-sonnet-4.5 | copilot | 0.800 | 0.667 | 1.000 | `c8cf8ae` | [#497](https://github.com/ai4curation/eval-ont-agent-go/pull/497) | [attempt](attempts/pr497.md) |
| 8 | claude-sonnet-4.5 | claude | 0.800 | 0.667 | 1.000 | `c8cf8ae` | [#476](https://github.com/ai4curation/eval-ont-agent-go/pull/476) | [attempt](attempts/pr476.md) |
| 9 | claude-sonnet-4.5 | copilot | 0.800 | 0.667 | 1.000 | `c8cf8ae` | [#418](https://github.com/ai4curation/eval-ont-agent-go/pull/418) | [attempt](attempts/pr418.md) |
| 10 | claude-opus-4.7 | claude | 0.800 | 0.667 | 1.000 | `c8cf8ae` | [#351](https://github.com/ai4curation/eval-ont-agent-go/pull/351) | [attempt](attempts/pr351.md) |
| 11 | claude-haiku-4.5 | claude | 0.800 | 0.667 | 1.000 | `c8cf8ae` | [#216](https://github.com/ai4curation/eval-ont-agent-go/pull/216) | [attempt](attempts/pr216.md) |
| 12 | gpt-5.4 | codex | 0.800 | 0.667 | 1.000 | `c8cf8ae` | [#191](https://github.com/ai4curation/eval-ont-agent-go/pull/191) | [attempt](attempts/pr191.md) |
| 13 | gpt-5.5 | codex | 0.800 | 0.667 | 1.000 | `c8cf8ae` | [#58](https://github.com/ai4curation/eval-ont-agent-go/pull/58) | [attempt](attempts/pr58.md) |
