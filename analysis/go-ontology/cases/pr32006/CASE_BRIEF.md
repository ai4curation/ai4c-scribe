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
num_agent_attempts: 14
generated_at: '2026-05-17'
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

## Curation Note (data quality)

Issue #31963 is not a clean one-PR evaluation case. The human resolution was split across PR #32006, which updated the `GO:0102067` definition and definition xrefs, and PR #32009, which later obsoleted `GO:0045550` with `replaced_by: GO:0102067`.

This matters for agent scoring because the selected gold PR for this case is only the definition-update sub-step. At least eval PR #124 was run on a base where the #32006 `GO:0102067` definition/xref update was already present while `GO:0045550` was still active. For that attempt, the zero metadiff against #32006 is therefore partly a base-state artifact; the substantive failure is that the agent did not complete the remaining issue-level obsoletion handled by #32009.

### Task-type metadata is wrong (flagged 2026-05-15, claude-opus-4.7)

The frontmatter `task_type: synonym_update` is incorrect, and so is the implied "obsoletion" of the issue title for *this* gold PR. PR #32006 changes only the `def:` text and the bracketed definition xrefs of `GO:0102067` (`[EC:1.3.1.83, GOC:pz]` → `[EC:1.3.1.83, PMID:9492312, RHEA:26229]`). There is no synonym edit and no obsoletion in #32006. The accurate task_type for the #32006 sub-step is **definition_update**; the obsoletion described by the issue title is the separate companion PR #32009.

### Cross-attempt review finding (claude-opus-4.7, 2026-05-15)

All 10 attempts were reviewed. Two clusters explain the score distribution, and the metadiff is misleading in both:

1. **Base `55fadafbd` (gold not pre-applied): #474, #349, #210, #279, #186.** These performed the correct definition rewrite. F1 caps at 0.5 (or 0.4 when a defensible `term_tracker_item` is added) purely because this is a one-line `def:` change and attempts differ from gold only in the bracketed xref set and synonymous phrasing. #186 (gpt-5.4/codex) reproduced the gold xref set `[EC:1.3.1.83, PMID:9492312, RHEA:26229]` exactly and #279 reproduced the gold def text verbatim — both scored only 0.4. The metadiff materially **under-represents** quality for this cluster; these are effectively successes.
2. **Base `8262d5a8a` (gold pre-applied): #157, #140, #124.** F1=0.0 is largely base-state leakage, not a definition-task failure; the real shortfall is the un-done `GO:0045550` obsoletion (companion #32009).
3. **Copilot #442 / #431** are genuine failures unrelated to the case-quality issue: identical off-topic diffs obsoleting `GO:0018581`/`GO:0047074` (hydroxyquinol dioxygenase), never engaging the geranylgeranyl reductase terms.

Recommendation: for aggregate scoring, treat the cluster-1 attempts as successes on the definition sub-step and exclude/down-weight the cluster-2 metadiff; only the two copilot runs are unambiguous failures.

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

## Agent Attempts (14)

| # | Model | Runtime | F1 | P | R | Blob | Eval PR | Detail |
|---|-------|---------|-----|-----|-----|------|---------|--------|
| 1 | claude-sonnet-4.5 | claude | 0.500 | 0.500 | 0.500 | `ddff8f6` | [#474](https://github.com/ai4curation/eval-ont-agent-go/pull/474) | [attempt](attempts/pr474.md) |
| 2 | claude-opus-4.7 | claude | 0.500 | 0.500 | 0.500 | `adf8db6` | [#349](https://github.com/ai4curation/eval-ont-agent-go/pull/349) | [attempt](attempts/pr349.md) |
| 3 | claude-haiku-4.5 | claude | 0.500 | 0.500 | 0.500 | `fd44a39` | [#210](https://github.com/ai4curation/eval-ont-agent-go/pull/210) | [attempt](attempts/pr210.md) |
| 4 | kimi-k2.6 | opencode | 0.400 | 0.500 | 0.333 | `653640d` | [#279](https://github.com/ai4curation/eval-ont-agent-go/pull/279) | [attempt](attempts/pr279.md) |
| 5 | gpt-5.4 | codex | 0.400 | 0.500 | 0.333 | `4f0b1a8` | [#186](https://github.com/ai4curation/eval-ont-agent-go/pull/186) | [attempt](attempts/pr186.md) |
| 6 | gpt-5.4 | opencode | 0.000 | 0.000 | 0.000 | `7070a10` | [#666](https://github.com/ai4curation/eval-ont-agent-go/pull/666) | [attempt](attempts/pr666.md) |
| 7 | gpt-5.4 | opencode | 0.000 | 0.000 | 0.000 | `7070a10` | [#660](https://github.com/ai4curation/eval-ont-agent-go/pull/660) | [attempt](attempts/pr660.md) |
| 8 | gpt-5.4 | opencode | 0.000 | 0.000 | 0.000 | `4c1a6c4` | [#627](https://github.com/ai4curation/eval-ont-agent-go/pull/627) | [attempt](attempts/pr627.md) |
| 9 | gpt-5.4 | opencode | 0.000 | 0.000 | 0.000 | `4c1a6c4` | [#612](https://github.com/ai4curation/eval-ont-agent-go/pull/612) | [attempt](attempts/pr612.md) |
| 10 | claude-sonnet-4.5 | copilot | 0.000 | 0.000 | 0.000 | `4c1a6c4` | [#442](https://github.com/ai4curation/eval-ont-agent-go/pull/442) | [attempt](attempts/pr442.md) |
| 11 | claude-sonnet-4.5 | copilot | 0.000 | 0.000 | 0.000 | `4c1a6c4` | [#431](https://github.com/ai4curation/eval-ont-agent-go/pull/431) | [attempt](attempts/pr431.md) |
| 12 | gpt-5.5 | opencode | 0.000 | 0.000 | 0.000 | `74726b1` | [#157](https://github.com/ai4curation/eval-ont-agent-go/pull/157) | [attempt](attempts/pr157.md) |
| 13 | gpt-5.5 | opencode | 0.000 | 0.000 | 0.000 | `74726b1` | [#140](https://github.com/ai4curation/eval-ont-agent-go/pull/140) | [attempt](attempts/pr140.md) |
| 14 | gpt-5.5 | codex | 0.000 | 0.000 | 0.000 | `74726b1` | [#124](https://github.com/ai4curation/eval-ont-agent-go/pull/124) | [attempt](attempts/pr124.md) |
