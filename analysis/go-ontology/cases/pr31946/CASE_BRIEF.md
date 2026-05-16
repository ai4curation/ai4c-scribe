---
ontology: go-ontology
repo: geneontology/go-ontology
issue_number: 31935
pr_number: 31946
issue_title: 'Missing parent: GO:0061852 retrograde transporter complex, Golgi to
  ER (plus term label and definition)'
pr_author: dragon-ai-agent
pr_merged_at: '2026-04-22'
task_type: reclassification
difficulty: medium
scoping: tightly_scoped
scope: single_term
review_outcome: approved_first_time
num_agent_attempts: 9
generated_at: '2026-05-15'
best_f1: 0.952
best_model: claude-sonnet-4.5
---

# PR #31946 — Missing parent: GO:0061852 retrograde transporter complex, Golgi to ER (plus term label and definition)

**go-ontology** | [geneontology/go-ontology](https://github.com/geneontology/go-ontology) | [Issue #31935](https://github.com/geneontology/go-ontology/issues/31935) | [PR #31946](https://github.com/geneontology/go-ontology/pull/31946) | @dragon-ai-agent | merged 2026-04-22

`reclassification` `medium` `tightly_scoped` `approved_first_time`

## Context

GO:0061852 was originally classified as a transporter complex with the label "retrograde transporter complex, Golgi to ER". ValWood identified that the term should actually be classified under `cargo receptor complex` rather than `transporter complex`, since the KDEL receptor and related proteins function as cargo receptors that recognize ER-retention signals, not as transporters that provide the energy for vesicle movement.

## Changes Made

The PR reclassified GO:0061852 by changing its parent from `GO:1990351 transporter complex` to `GO:0062137 cargo receptor complex`, renamed the primary label to `retrograde cargo receptor complex, Golgi to ER`, and refined the definition from "Transporter complex that recognises" to "Cargo receptor complex that recognizes" ER-retention signals. The two old transporter-based names were demoted to BROAD synonyms, and a new EXACT synonym was added for the specific KDEL receptor complex.

## Resolution

Medium difficulty because the reclassification required understanding the semantic distinction between cargo receptors (which recognize and bind cargo) and transporters (which provide energy for movement). In vesicle-mediated transport, KDEL receptors are cargo receptors that cycle between Golgi and ER to retrieve escaped ER-resident proteins, not transporters in the molecular function sense. The 2-commit history suggests a minor correction was needed after initial review.

## Human Diff

```diff
diff --git a/src/ontology/go-edit.obo b/src/ontology/go-edit.obo
index f0596951e..b1c0cb0c3 100644
--- a/src/ontology/go-edit.obo
+++ b/src/ontology/go-edit.obo
@@ -371414,17 +371414,19 @@ intersection_of: part_of GO:0030027 ! lamellipodium
 
 [Term]
 id: GO:0061852
-name: retrograde transporter complex, Golgi to ER
+name: retrograde cargo receptor complex, Golgi to ER
 namespace: cellular_component
-def: "Transporter complex that recognises, binds and returns endoplasmic reticulum (ER) resident proteins that have trafficked to Golgi compartments. Targets proteins lacking the HDEL motif recognised by COPI-coated vesicles." [GOC:bhm, PMID:16093310]
+def: "Cargo receptor complex that recognizes, binds and returns endoplasmic reticulum (ER) resident proteins that have trafficked to Golgi compartments. Targets proteins lacking the HDEL motif recognised by COPI-coated vesicles." [GOC:bhm, PMID:16093310]
 comment: An example of this is ERV41 in Saccharomyces cerevisiae (Q04651) in PMID:16093310 (inferred from direct assay).
 synonym: "ERV41-ERV46 retrograde receptor complex" NARROW []
+synonym: "retrograde cargo receptor complex, Golgi to endoplasmic reticulum" EXACT []
 synonym: "retrograde receptor complex, Golgi to endoplasmic reticulum" EXACT []
 synonym: "retrograde receptor complex, Golgi to ER" EXACT []
-synonym: "retrograde transporter complex, Golgi to endoplasmic reticulum" EXACT []
-is_a: GO:1990351 ! transporter complex
+synonym: "retrograde transporter complex, Golgi to ER" BROAD []
+is_a: GO:0062137 ! cargo receptor complex
 relationship: capable_of_part_of GO:0006890 ! retrograde vesicle-mediated transport, Golgi to endoplasmic reticulum
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/24444" xsd:anyURI
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31935" xsd:anyURI
 created_by: dph
 creation_date: 2017-02-28T13:56:56Z
 

```

## Agent Attempts (9)

| # | Model | Runtime | F1 | P | R | Eval PR | Detail |
|---|-------|---------|-----|-----|-----|---------|--------|
| 1 | claude-sonnet-4.5 | copilot | 0.952 | 1.000 | 0.909 | [#378](https://github.com/ai4curation/eval-ont-agent-go/pull/378) | [attempt](attempts/pr378.md) |
| 2 | claude-opus-4.7 | claude | 0.870 | 1.000 | 0.769 | [#346](https://github.com/ai4curation/eval-ont-agent-go/pull/346) | [attempt](attempts/pr346.md) |
| 3 | gpt-5.5 | opencode | 0.857 | 0.900 | 0.818 | [#95](https://github.com/ai4curation/eval-ont-agent-go/pull/95) | [attempt](attempts/pr95.md) |
| 4 | gpt-5.5 | opencode | 0.857 | 0.900 | 0.818 | [#75](https://github.com/ai4curation/eval-ont-agent-go/pull/75) | [attempt](attempts/pr75.md) |
| 5 | claude-haiku-4.5 | claude | 0.824 | 0.700 | 1.000 | [#206](https://github.com/ai4curation/eval-ont-agent-go/pull/206) | [attempt](attempts/pr206.md) |
| 6 | claude-sonnet-4.5 | claude | 0.800 | 0.800 | 0.800 | [#459](https://github.com/ai4curation/eval-ont-agent-go/pull/459) | [attempt](attempts/pr459.md) |
| 7 | claude-sonnet-4.5 | copilot | 0.800 | 0.800 | 0.800 | [#415](https://github.com/ai4curation/eval-ont-agent-go/pull/415) | [attempt](attempts/pr415.md) |
| 8 | gpt-5.5 | codex | 0.800 | 0.800 | 0.800 | [#59](https://github.com/ai4curation/eval-ont-agent-go/pull/59) | [attempt](attempts/pr59.md) |
| 9 | gpt-5.4 | codex | 0.720 | 0.900 | 0.600 | [#45](https://github.com/ai4curation/eval-ont-agent-go/pull/45) | [attempt](attempts/pr45.md) |
