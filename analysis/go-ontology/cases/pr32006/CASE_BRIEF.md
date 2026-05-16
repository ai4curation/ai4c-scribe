---
ontology: go-ontology
repo: geneontology/go-ontology
issue_number: 31963
pr_number: 32006
issue_title: Obsolete GO:0045550 geranylgeranyl reductase activity
pr_author: dragon-ai-agent
pr_merged_at: '2026-04-28'
task_type: synonym_update
difficulty: simple
scoping: tightly_scoped
scope: single_term
review_outcome: approved_first_time
num_agent_attempts: 10
generated_at: '2026-05-15'
domain_area: molecular_function
best_f1: 0.5
best_model: claude-sonnet-4.5
---

# PR #32006 — Obsolete GO:0045550 geranylgeranyl reductase activity

**go-ontology** | [geneontology/go-ontology](https://github.com/geneontology/go-ontology) | [Issue #31963](https://github.com/geneontology/go-ontology/issues/31963) | [PR #32006](https://github.com/geneontology/go-ontology/pull/32006) | @dragon-ai-agent | merged 2026-04-28

`synonym_update` `simple` `tightly_scoped` `approved_first_time`

## Context

Issue #31963 primarily requested obsoletion of GO:0045550, but discussion in the issue also identified that GO:0102067 (the replacement term) had an overly complex definition. After the obsoletion was merged in PR #32009, @sjm41 noted that the reaction description in GO:0102067's definition should be simplified to use "phytyl diphosphate" rather than spelling out the full IUPAC substrate name.

## Changes Made

In `src/ontology/go-edit.obo`, the `def:` field of GO:0102067 (geranylgeranyl diphosphate reductase activity) was updated to use simplified substrate naming, making the definition more readable while remaining biochemically accurate.

## Resolution

Merged directly. This single-line definition polish was a direct response to @sjm41's comment in the issue discussion. It demonstrates the common pattern of iterative refinement where obsoletion of one term prompts closer scrutiny of the replacement term's quality.

## Human Diff

```diff
diff --git a/src/ontology/go-edit.obo b/src/ontology/go-edit.obo
index 55fadafbd..ccb7aa216 100644
--- a/src/ontology/go-edit.obo
+++ b/src/ontology/go-edit.obo
@@ -440012,7 +440012,7 @@ is_obsolete: true
 id: GO:0102067
 name: geranylgeranyl diphosphate reductase activity
 namespace: molecular_function
-def: "Catalysis of the reaction: (E)-3,7,11,15-tetramethylhexadec-2-en-1-yl diphosphate + 3 NADP = 2-trans,6-trans,10-trans-geranylgeranyl diphosphate + 3 NADPH + 3 H+." [EC:1.3.1.83, GOC:pz]
+def: "Catalysis of the reaction: phytyl diphosphate + 3 NADP+ = geranylgeranyl diphosphate + 3 NADPH + 3 H+. This enzyme also catalyzes the reduction of geranylgeranyl-chlorophyll a into phytyl-chlorophyll a." [EC:1.3.1.83, PMID:9492312, RHEA:26229]
 xref: EC:1.3.1.83 {source="skos:exactMatch"}
 xref: MetaCyc:RXN-10625
 xref: RHEA:26229 {source="skos:exactMatch"}

```

## Agent Attempts (10)

| # | Model | Runtime | F1 | P | R | Eval PR | Detail |
|---|-------|---------|-----|-----|-----|---------|--------|
| 1 | claude-sonnet-4.5 | claude | 0.500 | 0.500 | 0.500 | [#474](https://github.com/ai4curation/eval-ont-agent-go/pull/474) | [attempt](attempts/pr474.md) |
| 2 | claude-opus-4.7 | claude | 0.500 | 0.500 | 0.500 | [#349](https://github.com/ai4curation/eval-ont-agent-go/pull/349) | [attempt](attempts/pr349.md) |
| 3 | claude-haiku-4.5 | claude | 0.500 | 0.500 | 0.500 | [#210](https://github.com/ai4curation/eval-ont-agent-go/pull/210) | [attempt](attempts/pr210.md) |
| 4 | kimi-k2.6 | opencode | 0.400 | 0.500 | 0.333 | [#279](https://github.com/ai4curation/eval-ont-agent-go/pull/279) | [attempt](attempts/pr279.md) |
| 5 | gpt-5.4 | codex | 0.400 | 0.500 | 0.333 | [#186](https://github.com/ai4curation/eval-ont-agent-go/pull/186) | [attempt](attempts/pr186.md) |
| 6 | claude-sonnet-4.5 | copilot | 0.000 | 0.000 | 0.000 | [#442](https://github.com/ai4curation/eval-ont-agent-go/pull/442) | [attempt](attempts/pr442.md) |
| 7 | claude-sonnet-4.5 | copilot | 0.000 | 0.000 | 0.000 | [#431](https://github.com/ai4curation/eval-ont-agent-go/pull/431) | [attempt](attempts/pr431.md) |
| 8 | gpt-5.5 | opencode | 0.000 | 0.000 | 0.000 | [#157](https://github.com/ai4curation/eval-ont-agent-go/pull/157) | [attempt](attempts/pr157.md) |
| 9 | gpt-5.5 | opencode | 0.000 | 0.000 | 0.000 | [#140](https://github.com/ai4curation/eval-ont-agent-go/pull/140) | [attempt](attempts/pr140.md) |
| 10 | gpt-5.5 | codex | 0.000 | 0.000 | 0.000 | [#124](https://github.com/ai4curation/eval-ont-agent-go/pull/124) | [attempt](attempts/pr124.md) |
