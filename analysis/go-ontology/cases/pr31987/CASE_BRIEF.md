---
ontology: go-ontology
repo: geneontology/go-ontology
issue_number: 31984
pr_number: 31987
issue_title: GO:0008805 (carbon-monoxide oxygenase activity) and GO:0043885 (anaerobic
  carbon-monoxide dehydrogenase activity)
pr_author: sjm41
pr_merged_at: '2026-04-27'
task_type: axiom_repair
difficulty: hard
scoping: tightly_scoped
scope: multi_term
review_outcome: approved_first_time
num_agent_attempts: 10
generated_at: '2026-05-15'
best_f1: 0.947
best_model: claude-opus-4.7
---

# PR #31987 — GO:0008805 (carbon-monoxide oxygenase activity) and GO:0043885 (anaerobic carbon-monoxide dehydrogenase activity)

**go-ontology** | [geneontology/go-ontology](https://github.com/geneontology/go-ontology) | [Issue #31984](https://github.com/geneontology/go-ontology/issues/31984) | [PR #31987](https://github.com/geneontology/go-ontology/pull/31987) | @sjm41 | merged 2026-04-27

`axiom_repair` `hard` `tightly_scoped` `approved_first_time`

## Context

Two carbon monoxide dehydrogenase terms in GO had incorrect names, definitions, and cross-references relative to their EC and RHEA entries. GO:0008805 was named "carbon-monoxide oxygenase activity" but actually corresponded to the aerobic CO dehydrogenase (using quinone as electron acceptor), while GO:0043885 (anaerobic variant) also needed alignment. The enzyme curator sjm41 identified the discrepancies during a systematic review of oxidoreductase terms.

## Changes Made

GO:0008805 was renamed from `carbon-monoxide oxygenase activity` to `aerobic carbon monoxide dehydrogenase activity`. The definition was corrected from a cytochrome-based reaction (`CO + H2O + ferrocytochrome b-561 = CO2 + 2 H+ + 2 ferricytochrome b-561`) to the quinone-based reaction (`CO + a quinone + H2O = a quinol + CO2`) matching RHEA:48880. The parent term was also changed from a cytochrome-dependent oxidoreductase class to the correct quinone-dependent class. Definition cross-references were updated accordingly.

## Resolution

Hard difficulty because the corrections required understanding the distinct biochemistry of aerobic vs. anaerobic CO dehydrogenases. Aerobic CoxMSL-type enzymes use molybdopterin cofactors with quinone electron acceptors, while anaerobic CODH uses nickel-iron centers. Misalignment between GO terms and EC/RHEA entries for these enzymes could lead to incorrect functional annotations. The curator resolved this within a single day, reflecting deep domain expertise.

## Human Diff

```diff
diff --git a/src/ontology/go-edit.obo b/src/ontology/go-edit.obo
index a76eab953..1c96f5771 100644
--- a/src/ontology/go-edit.obo
+++ b/src/ontology/go-edit.obo
@@ -85879,11 +85879,11 @@ property_value: term_tracker_item "https://github.com/geneontology/go-ontology/i
 
 [Term]
 id: GO:0008805
-name: carbon-monoxide oxygenase activity
+name: aerobic carbon monoxide dehydrogenase activity
 namespace: molecular_function
 alt_id: GO:0018999
 alt_id: GO:0047767
-def: "Catalysis of the reaction: CO + H2O + ferrocytochrome b-561 = CO2 + 2 H+ + 2 ferricytochrome b-561." [GOC:curators, RHEA:48880]
+def: "Catalysis of the reaction: CO + a quinone + H2O = a quinol + CO2." [RHEA:48880]
 synonym: "carbon monoxide oxidase activity" RELATED []
 synonym: "carbon monoxide oxygenase (cytochrome b-561) activity" NARROW []
 synonym: "carbon monoxide oxygenase activity" EXACT []
@@ -85891,13 +85891,15 @@ synonym: "carbon monoxide,water:cytochrome b-561 oxidoreductase activity" RELATE
 synonym: "carbon monoxide:methylene blue oxidoreductase activity" NARROW []
 synonym: "carbon-monoxide dehydrogenase (cytochrome b-561)" RELATED []
 synonym: "cytochrome b561" NARROW []
+synonym: "carbon-monoxide oxygenase activity" BROAD []
 xref: EC:1.2.5.3 {source="skos:exactMatch"}
 xref: MetaCyc:RXN-21452
 xref: RHEA:48880 {source="skos:exactMatch"}
 xref: UM-BBD_reactionID:r0650
 xref: Wikipedia:Carbon-monoxide_dehydrogenase_(cytochrome_b-561)
-is_a: GO:0016622 ! oxidoreductase activity, acting on the aldehyde or oxo group of donors, cytochrome as acceptor
+is_a: GO:0052738 ! oxidoreductase activity, acting on the aldehyde or oxo group of donors, with a quinone or similar compound as acceptor
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31984" xsd:anyURI
 
 [Term]
 id: GO:0008806
@@ -257958,7 +257960,7 @@ property_value: term_tracker_item "https://github.com/geneontology/go-ontology/i
 id: GO:0043885
 name: anaerobic carbon-monoxide dehydrogenase activity
 namespace: molecular_function
-def: "Catalysis of the reaction: CO + H2O + oxidized ferredoxin = CO2 + reduced ferredoxin." [RHEA:21040]
+def: "Catalysis of the reaction: CO + 2 oxidized [2Fe-2S]-[ferredoxin] + H2O = 2 reduced [2Fe-2S]-[ferredoxin] + CO2 + 2 H+." [RHEA:21040]
 synonym: "carbon monoxide dehydrogenase (ferredoxin) activity" EXACT []
 synonym: "carbon monoxide dehydrogenase activity" BROAD []
 synonym: "carbon-monoxide dehydrogenase (ferredoxin) activity" EXACT []
@@ -257976,6 +257978,7 @@ xref: UM-BBD_reactionID:r0652
 is_a: GO:0016625 ! oxidoreductase activity, acting on the aldehyde or oxo group of donors, iron-sulfur protein as acceptor
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/25872" xsd:anyURI
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31984" xsd:anyURI
 
 [Term]
 id: GO:0043886

```

## Agent Attempts (10)

| # | Model | Runtime | F1 | P | R | Eval PR | Detail |
|---|-------|---------|-----|-----|-----|---------|--------|
| 1 | claude-opus-4.7 | claude | 0.947 | 0.900 | 1.000 | [#355](https://github.com/ai4curation/eval-ont-agent-go/pull/355) | [attempt](attempts/pr355.md) |
| 2 | gpt-5.5 | opencode | 0.947 | 0.900 | 1.000 | [#99](https://github.com/ai4curation/eval-ont-agent-go/pull/99) | [attempt](attempts/pr99.md) |
| 3 | gpt-5.5 | opencode | 0.947 | 0.900 | 1.000 | [#79](https://github.com/ai4curation/eval-ont-agent-go/pull/79) | [attempt](attempts/pr79.md) |
| 4 | gpt-5.5 | codex | 0.857 | 0.900 | 0.818 | [#62](https://github.com/ai4curation/eval-ont-agent-go/pull/62) | [attempt](attempts/pr62.md) |
| 5 | claude-sonnet-4.5 | claude | 0.842 | 0.800 | 0.889 | [#482](https://github.com/ai4curation/eval-ont-agent-go/pull/482) | [attempt](attempts/pr482.md) |
| 6 | claude-haiku-4.5 | claude | 0.778 | 0.700 | 0.875 | [#217](https://github.com/ai4curation/eval-ont-agent-go/pull/217) | [attempt](attempts/pr217.md) |
| 7 | claude-sonnet-4.5 | copilot | 0.737 | 0.700 | 0.778 | [#496](https://github.com/ai4curation/eval-ont-agent-go/pull/496) | [attempt](attempts/pr496.md) |
| 8 | claude-sonnet-4.5 | copilot | 0.737 | 0.700 | 0.778 | [#426](https://github.com/ai4curation/eval-ont-agent-go/pull/426) | [attempt](attempts/pr426.md) |
| 9 | kimi-k2.6 | opencode | 0.700 | 0.700 | 0.700 | [#285](https://github.com/ai4curation/eval-ont-agent-go/pull/285) | [attempt](attempts/pr285.md) |
| 10 | gpt-5.4 | codex | 0.621 | 0.900 | 0.474 | [#200](https://github.com/ai4curation/eval-ont-agent-go/pull/200) | [attempt](attempts/pr200.md) |
