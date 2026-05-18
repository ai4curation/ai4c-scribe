---
ontology: uberon
repo: obophenotype/uberon
issue_number: 3475
pr_number: 3477
issue_title: Remove Thoracic dorsal root ganglion as a part of thoracic ganglion
pr_author: tgbugs
pr_merged_at: '2025-04-24'
task_type: axiom_repair
difficulty: medium
scoping: tightly_scoped
scope: single_term
review_outcome: approved_first_time
num_agent_attempts: 10
generated_at: '2026-05-17'
domain_area: neuroanatomy
best_f1: 0.667
best_model: claude-haiku-4.5
---

# PR #3477 — Remove Thoracic dorsal root ganglion as a part of thoracic ganglion

**uberon** | [obophenotype/uberon](https://github.com/obophenotype/uberon) | [Issue #3475](https://github.com/obophenotype/uberon/issues/3475) | [PR #3477](https://github.com/obophenotype/uberon/pull/3477) | @tgbugs | merged 2025-04-24

`axiom_repair` `medium` `tightly_scoped` `approved_first_time`

## Context

Issue #3475 reported that UBERON:0002835 (thoracic dorsal root ganglion) was incorrectly classified as a subclass of UBERON:0000961 (thoracic ganglion). The thoracic ganglion in Uberon refers to a paravertebral ganglion of the sympathetic trunk, while a dorsal root ganglion is a sensory ganglion. These are fundamentally different types of ganglia despite both being located in the thoracic region.

## Changes Made

The PR removed a single is_a line from uberon-edit.obo, deleting the incorrect SubClassOf axiom that placed thoracic dorsal root ganglion under thoracic ganglion. No replacement axiom was needed since the dorsal root ganglion already had correct classification through its other parent terms.

## Resolution

Medium difficulty. While the change is a single line deletion, an agent would need to understand the neuroanatomical distinction between dorsal root ganglia (sensory, spinal nerve associated) and paravertebral ganglia (autonomic, sympathetic trunk associated) to verify that the removal is correct and that no replacement axiom is needed. The two-month gap between issue and merge suggests the fix waited for a batch merge cycle.

## Curation Note (data quality)

**Flagged poor by claude-opus-4.7 on 2026-05-16. Reason: `gold_pr_is_partial`.**

Issue #3475 contains two explicit, numbered asks:

1. "remove thoracic dorsal root ganglion as a subclass of thoracic ganglion" — remove `is_a: UBERON:0000961` from UBERON:0002835.
2. "clarify the name of thoracic ganglion ... to thoracic paravertebral ganglion, since thoracic ganglion would more properly refer to ganglia that are within the thorax, including spinal, prevertebral and paravertebral ganglia" — **rename** UBERON:0000961.

Gold PR #3477 (`tgbugs`, title "remove incorrct subClassOf axiom on thoracic drg", 0 additions / 1 deletion) performed **only ask #1**. The rename (ask #2) was never carried out: the current Uberon HEAD `uberon-edit.obo` still has `name: thoracic ganglion` for UBERON:0000961, with "thoracic paravertebral ganglion" remaining only an `EXACT [MA:0001159]` synonym. A search of PRs referencing #3475 / "thoracic paravertebral ganglion" finds no companion PR that did the rename (the only related hit, #3592, is an unrelated import refresh). The PR thread contains no curator decision to decline the rename — it appears simply not done.

Consequences for scoring:

- The metadiff is computed against the **partial** gold (one-line deletion). The maximum achievable F1 for an answer that does *only* the deletion is 0.667 (attempt #96), and that attempt actually did the deletion *wrong* (re-asserted `is_a: UBERON:0000044` instead of removing the line). Metadiff thus *over-represents* #96.
- Attempts that correctly did **both** issue asks (#319, #232, #19, #56, #37) score 0.15–0.33 and are **under-represented** by metadiff. #319 (sonnet-4.5/claude) is the cleanest full resolution of the actual issue.
- Two attempts (#11 gpt-5.4/codex, #193 sonnet-4.5/copilot) additionally suffer **ODK build-regenerated-file domination**: their diffs contain a large block of unrelated CL term-label rewrites (e.g. `lung ciliated cell` → `lung multiciliated epithelial cell`, `glandular epithelial cell` → `glandular secretory epithelial cell`). Verified against eval base branch `eval-base-issue-3475` (which carries the *old* labels), this is **self-inflicted** file regeneration by those agents, not base contamination — a genuine scope failure on top of the poor-case scoring.

Recommendation: down-weight or exclude this case from aggregate metadiff scoring; when judging attempts, score against the issue's two explicit asks and treat #319/#232/#19/#56/#37 as substantively successful. Do not treat #96's high F1 as a quality signal.

## Human Diff

```diff
diff --git a/src/ontology/uberon-edit.obo b/src/ontology/uberon-edit.obo
index 36afa06edc..19c73a513d 100644
--- a/src/ontology/uberon-edit.obo
+++ b/src/ontology/uberon-edit.obo
@@ -60564,7 +60564,6 @@ xref: BIRNLEX:2600
 xref: FMA:6006
 xref: SCTID:278326009
 xref: UMLS:C0457467 {source="BIRNLEX:2600"}
-is_a: UBERON:0000961 ! thoracic ganglion
 intersection_of: UBERON:0000044 ! dorsal root ganglion
 intersection_of: extends_fibers_into UBERON:0009630 ! root of thoracic nerve
 

```

## Agent Attempts (10)

| # | Model | Runtime | F1 | P | R | Blob | Eval PR | Detail |
|---|-------|---------|-----|-----|-----|------|---------|--------|
| 1 | claude-haiku-4.5 | claude | 0.667 | 1.000 | 0.500 | `5f37082` | [#96](https://github.com/ai4curation/eval-ont-agent-uberon/pull/96) | [attempt](attempts/pr96.md) |
| 2 | claude-sonnet-4.5 | claude | 0.333 | 1.000 | 0.200 | `a908508` | [#319](https://github.com/ai4curation/eval-ont-agent-uberon/pull/319) | [attempt](attempts/pr319.md) |
| 3 | gpt-5.4 | opencode | 0.222 | 1.000 | 0.125 | `567d5d1` | [#650](https://github.com/ai4curation/eval-ont-agent-uberon/pull/650) | [attempt](attempts/pr650.md) |
| 4 | gpt-5.4 | opencode | 0.222 | 1.000 | 0.125 | `567d5d1` | [#591](https://github.com/ai4curation/eval-ont-agent-uberon/pull/591) | [attempt](attempts/pr591.md) |
| 5 | gpt-5.5 | codex | 0.182 | 1.000 | 0.100 | `d1e2ddc` | [#19](https://github.com/ai4curation/eval-ont-agent-uberon/pull/19) | [attempt](attempts/pr19.md) |
| 6 | claude-opus-4.7 | claude | 0.154 | 1.000 | 0.083 | `29396e1` | [#232](https://github.com/ai4curation/eval-ont-agent-uberon/pull/232) | [attempt](attempts/pr232.md) |
| 7 | gpt-5.5 | opencode | 0.154 | 1.000 | 0.083 | `f5512c1` | [#56](https://github.com/ai4curation/eval-ont-agent-uberon/pull/56) | [attempt](attempts/pr56.md) |
| 8 | gpt-5.5 | opencode | 0.154 | 1.000 | 0.083 | `f5512c1` | [#37](https://github.com/ai4curation/eval-ont-agent-uberon/pull/37) | [attempt](attempts/pr37.md) |
| 9 | claude-sonnet-4.5 | copilot | 0.100 | 1.000 | 0.053 | `b932d33` | [#193](https://github.com/ai4curation/eval-ont-agent-uberon/pull/193) | [attempt](attempts/pr193.md) |
| 10 | gpt-5.4 | codex | 0.100 | 1.000 | 0.053 | `a1348f6` | [#11](https://github.com/ai4curation/eval-ont-agent-uberon/pull/11) | [attempt](attempts/pr11.md) |
