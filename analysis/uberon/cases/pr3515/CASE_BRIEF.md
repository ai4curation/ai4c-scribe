---
ontology: uberon
repo: obophenotype/uberon
issue_number: 3509
pr_number: 3515
issue_title: Definition of common hepatic artery is truncated
pr_author: ar-ibrahim
pr_merged_at: '2025-05-08'
task_type: axiom_repair
difficulty: simple
scoping: tightly_scoped
scope: single_term
review_outcome: approved_first_time
num_agent_attempts: 12
generated_at: '2026-05-17'
domain_area: vascular-anatomy
best_f1: 0.5
best_model: gpt-5.4
---

# PR #3515 — Definition of common hepatic artery is truncated

**uberon** | [obophenotype/uberon](https://github.com/obophenotype/uberon) | [Issue #3509](https://github.com/obophenotype/uberon/issues/3509) | [PR #3515](https://github.com/obophenotype/uberon/pull/3515) | @ar-ibrahim | merged 2025-05-08

`axiom_repair` `simple` `tightly_scoped` `approved_first_time`

## Context

Issue #3509 reported that the text definition of the common hepatic artery was truncated, likely due to a data entry or import error. The definition was incomplete and needed to be restored to its full text.

## Changes Made

The PR made a single line change in src/ontology/uberon-edit.obo, replacing the truncated definition with the complete text for the common hepatic artery term. Despite the minimal change, three commits were needed, possibly due to formatting corrections during review.

## Resolution

Simple difficulty. This is a straightforward text correction requiring an agent to identify the truncated definition and supply the complete text. The main challenge is sourcing the correct full definition text, which could be obtained from anatomical references or the term's cross-references to other ontologies.

## Curation Note (data quality)

**Flagged `case_quality: poor` by claude-opus-4.7 on 2026-05-16.**

This is a poor evaluation reference because the issue's explicit instruction
and the gold PR's actual change point in **opposite directions**:

- **Issue #3509** quotes the truncated definition and says, verbatim:
  *"Just shorten this further so it's not trailing"* — i.e. remove/trim the
  dangling "and has the following branches:." fragment. (Issue has no comments.)
- **Gold PR #3515** (merged 2025-05-08 by ar-ibrahim; verified as current
  canonical text on `master`) did the **opposite**: it *expanded* the
  definition — added "and gall bladder" to the supply list, **enumerated the
  three branches** ("the hepatic artery proper, the gastroduodenal artery and
  the right gastric artery"), and added an Elsevier source xref
  (`https://www.elsevier.com/resources/anatomy/cardiovascular-system/arteries/common-hepatic-artery/22763`)
  alongside the existing `Wikipedia:Common_hepatic_artery`.

A faithful agent cannot satisfy both the issue text and the gold simultaneously.

**Companion PR #3510** (by cmungall/Claude Code) implemented the literal
issue request (remove the trailing fragment) but was closed unmerged after a
merge conflict; matentzn's comment that it was "implemented elsewhere (#3507)"
is a mistaken cross-reference — PR #3507 is "Added term: medial prefrontal
cortex" (fixes #3446) and does not touch UBERON:0005436. So #3515 is the
genuine, surviving canonical resolution; this is NOT a curator-repudiated or
partial-gold case — it is an underspecified-issue / gold-diverges-from-ask
case.

**Scoring consequence.** This is a single-line `def:` replacement. metadiff
gives every well-formed attempt P=R=F1=0.500 (the deleted line matches gold's
deleted line = 1 TP; the rewritten line is novel prose that cannot match
gold's divergent expansion = 0 TP on the addition). The two opencode/gpt-5.5
attempts (#63, #44) that correctly added a config-recommended
`term_tracker_item` link (which gold omitted) drop to F1=0.400 — penalized
for following uberon-agent-config best practice. The metadiff therefore
materially **under-represents** quality for all 8 attempts.

**Judging guidance.** Score attempts against the issue's actual ask (produce
a complete, non-trailing definition) — which all 8 attempts satisfied with
valid, anatomically accurate, tightly-scoped OBO. Best fidelity to the
surviving canonical text: opus #242 and gemma #113 (byte-identical, blob
`cf7f76d`), which removed *only* the trailing clause and preserved the
original preamble/glosses. Recommend down-weighting or excluding this case
from aggregate metadiff scoring.

## Human Diff

```diff
diff --git a/src/ontology/uberon-edit.obo b/src/ontology/uberon-edit.obo
index e3220d8bc9..887747153c 100644
--- a/src/ontology/uberon-edit.obo
+++ b/src/ontology/uberon-edit.obo
@@ -101453,7 +101453,7 @@ property_value: taxon_notes "In dogs, it is located to the left and often ventra
 [Term]
 id: UBERON:0005436
 name: common hepatic artery
-def: "In anatomy, the common hepatic artery is a short blood vessel that supplies oxygenated blood to the liver, pylorus (a part of the stomach), duodenum (a part of the small intestine) and pancreas. It arises from the celiac artery and has the following branches:." [Wikipedia:Common_hepatic_artery]
+def: "In anatomy, the common hepatic artery is a short blood vessel that supplies oxygenated blood to the liver, pylorus (a part of the stomach), duodenum (a part of the small intestine), pancreas, and gall bladder. It arises from the celiac artery and has the following branches: the hepatic artery proper, the gastroduodenal artery and the right gastric artery." [https://www.elsevier.com/resources/anatomy/cardiovascular-system/arteries/common-hepatic-artery/22763, Wikipedia:Common_hepatic_artery]
 synonym: "arteria hepatica communis" RELATED OMO:0003011 [Wikipedia:Common_hepatic_artery]
 synonym: "common hepatic" RELATED [Wikipedia:Common_hepatic_artery]
 xref: EHDAA2:0000308

```

## Agent Attempts (12)

| # | Model | Runtime | F1 | P | R | Blob | Eval PR | Detail |
|---|-------|---------|-----|-----|-----|------|---------|--------|
| 1 | gpt-5.4 | opencode | 0.500 | 0.500 | 0.500 | `cf7f76d` | [#659](https://github.com/ai4curation/eval-ont-agent-uberon/pull/659) | [attempt](attempts/pr659.md) |
| 2 | gpt-5.4 | opencode | 0.500 | 0.500 | 0.500 | `cf7f76d` | [#601](https://github.com/ai4curation/eval-ont-agent-uberon/pull/601) | [attempt](attempts/pr601.md) |
| 3 | kimi-k2.6 | opencode | 0.500 | 0.500 | 0.500 | `cf7f76d` | [#442](https://github.com/ai4curation/eval-ont-agent-uberon/pull/442) | [attempt](attempts/pr442.md) |
| 4 | gpt-5.4 | codex | 0.500 | 0.500 | 0.500 | `cf7f76d` | [#380](https://github.com/ai4curation/eval-ont-agent-uberon/pull/380) | [attempt](attempts/pr380.md) |
| 5 | claude-haiku-4.5 | claude | 0.500 | 0.500 | 0.500 | `6ae02a3` | [#327](https://github.com/ai4curation/eval-ont-agent-uberon/pull/327) | [attempt](attempts/pr327.md) |
| 6 | claude-sonnet-4.5 | claude | 0.500 | 0.500 | 0.500 | `139e07f` | [#288](https://github.com/ai4curation/eval-ont-agent-uberon/pull/288) | [attempt](attempts/pr288.md) |
| 7 | claude-haiku-4.5 | claude | 0.500 | 0.500 | 0.500 | `6ae02a3` | [#269](https://github.com/ai4curation/eval-ont-agent-uberon/pull/269) | [attempt](attempts/pr269.md) |
| 8 | claude-opus-4.7 | claude | 0.500 | 0.500 | 0.500 | `cf7f76d` | [#242](https://github.com/ai4curation/eval-ont-agent-uberon/pull/242) | [attempt](attempts/pr242.md) |
| 9 | gemma-4-31b | opencode | 0.500 | 0.500 | 0.500 | `cf7f76d` | [#113](https://github.com/ai4curation/eval-ont-agent-uberon/pull/113) | [attempt](attempts/pr113.md) |
| 10 | gpt-5.5 | codex | 0.500 | 0.500 | 0.500 | `4aca6c2` | [#28](https://github.com/ai4curation/eval-ont-agent-uberon/pull/28) | [attempt](attempts/pr28.md) |
| 11 | gpt-5.5 | opencode | 0.400 | 0.500 | 0.333 | `cc0a259` | [#63](https://github.com/ai4curation/eval-ont-agent-uberon/pull/63) | [attempt](attempts/pr63.md) |
| 12 | gpt-5.5 | opencode | 0.400 | 0.500 | 0.333 | `cc0a259` | [#44](https://github.com/ai4curation/eval-ont-agent-uberon/pull/44) | [attempt](attempts/pr44.md) |
