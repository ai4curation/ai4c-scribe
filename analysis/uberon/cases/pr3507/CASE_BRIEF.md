---
ontology: uberon
repo: obophenotype/uberon
issue_number: 3446
pr_number: 3507
issue_title: 'NTR: medial prefrontal cortex'
pr_author: cmungall
pr_merged_at: '2025-04-24'
task_type: new_term
difficulty: medium
scoping: tightly_scoped
scope: single_term
review_outcome: approved_first_time
num_agent_attempts: 11
generated_at: '2026-05-17'
domain_area: neuroanatomy
best_f1: 0.588
best_model: claude-sonnet-4.5
---

# PR #3507 — NTR: medial prefrontal cortex

**uberon** | [obophenotype/uberon](https://github.com/obophenotype/uberon) | [Issue #3446](https://github.com/obophenotype/uberon/issues/3446) | [PR #3507](https://github.com/obophenotype/uberon/pull/3507) | @cmungall | merged 2025-04-24

`new_term` `medium` `tightly_scoped` `approved_first_time`

## Context

Issue #3446 was a new term request for medial prefrontal cortex, a brain region important in neuroscience research for decision-making, social cognition, and emotional regulation. The request came as part of the SCORCH project's efforts to improve neuroanatomical coverage in Uberon.

## Changes Made

The PR added a new term stanza (11 lines) to src/ontology/uberon-edit.obo for medial prefrontal cortex, including a text definition, is_a placement under the prefrontal cortex hierarchy, appropriate cross-references, and contributor attribution. Four commits suggest iterative refinement of the term's definition or placement.

## Resolution

Medium difficulty. An agent would need to understand cortical neuroanatomy sufficiently to place the medial prefrontal cortex correctly in the hierarchy (as a subtype of prefrontal cortex, which is part of the frontal cortex), write an accurate definition that distinguishes it from adjacent regions, and include appropriate database cross-references.

## Curation Note (data quality)

Flagged `case_quality: poor` by claude-opus-4.7 on 2026-05-16 after reviewing all 5 attempts (eval PRs #241, #25, #64, #43, #77).

This is a single-PR resolution (no companion PRs — `gh search prs` for "3446" and "medial prefrontal cortex" returns only #3507), so the multi-PR partial-gold pattern does **not** apply. However the case is a poor metadiff reference for three independent reasons:

1. **Gold renegotiated in PR comments.** Gold PR #3507 was itself produced by an AI agent ("🤖 Generated with CBorg Code", `dragon-ai-agent`). The curator @cmungall left a PR review comment ("@dragon-ai-agent, fix the definition xref on the term you added. Also remove the `created_by`...") and the 4-commit history (`Fixed definition xref and removed created_by field`, `removed IAO property`) shows the final merged gold is a *curator-corrected* state. A replay agent sees only issue #3446 and cannot observe or anticipate this review loop, so its metadata conventions necessarily diverge from gold through no fault of its own. The gold's curator instruction to strip `created_by` is the one substantive item agents would still need a follow-up round to fix.

2. **Placeholder-vs-canonical UBERON ID artifact.** The canonical gold ID is `UBERON:4450000`, allocated by the curation infrastructure. The agent config (`ai4curation/uberon-agent-config@v3`, CLAUDE.md) explicitly instructs "New terms start UBERON:99xxxxx". Four of five attempts (#241 `9900001`, #64/#43 `9900000`) correctly followed that instruction with a placeholder that can never match gold's ID line, mechanically capping F1. Only attempt #25 reached the canonical `UBERON:4450000` (by checking an external UBERON view). Attempt #77's `UBERON:8480075` is outside even the recommended 99xxxxx range.

3. **robot-convert reserialization churn.** Every attempt's diff carries identical non-substantive `robot convert` artifacts — blank-line collapses at UBERON:0007182/0007185, def-xref re-sorting on UBERON:0013540 (BA9) and UBERON:0034891 (insular cortex), and (for #25/#77) a synonym reorder on UBERON:0003532 (hindlimb skin). Verified against eval base branch `eval-base-issue-3446`, which holds the un-collapsed/un-reordered state. Gold did a minimal manual OBO insert and has none of this, so the metadiff penalizes mechanical serialization, not curation quality.

Net: F1 0.40–0.57 substantially **under-represents** quality. Substantively, all five agents correctly created the term with the requested parentage (`is_a UBERON:0002616`, `part_of UBERON:0000451`), the `mPFC` `OMO:0003000` synonym, and both requester ORCIDs. They differ mainly in definition quality: #241 (best, clean genus–differentia preserving Brodmann composition) and #25 (closest to issue text, correct canonical ID) are substantively `success`; #64/#43 (thin one-line definition) and #77 (circular definition + out-of-scope rodent-term reparenting) are `partial_success`. Note #43's PR comment claims ID `UBERON:9903446` but its committed blob is byte-identical to #64 (`UBERON:9900000`) — a narrative/artifact inconsistency. Downstream scoring should down-weight or exclude this case and judge against issue #3446's explicit asks rather than the curator-corrected gold diff.

## Human Diff

```diff
diff --git a/src/ontology/uberon-edit.obo b/src/ontology/uberon-edit.obo
index b727e1726e..08cef2747b 100644
--- a/src/ontology/uberon-edit.obo
+++ b/src/ontology/uberon-edit.obo
@@ -217321,6 +217321,17 @@ intersection_of: UBERON:4000172 ! lepidotrichium
 intersection_of: part_of UBERON:0002534 ! paired fin
 relationship: part_of UBERON:0010713 ! paired fin skeleton
 
+[Term]
+id: UBERON:4450000
+name: medial prefrontal cortex
+def: "The medial prefrontal cortex (mPFC) is a subdivision of the prefrontal cortex composed of BA12, BA25, and anterior cingulate cortex: BA32, BA33, BA24. Within this region is the dorsal nexus, which interconnects multiple brain networks and plays a role in maintenance and manipulation of information (working memory), as well as supporting the control of cognitive functions such as emotion processing and regulation, memory, decision making, and conflict resolution." [Wikipedia:Prefrontal_cortex, https://orcid.org/0000-0001-7628-5565, https://orcid.org/0000-0002-4964-5083]
+synonym: "mPFC" EXACT OMO:0003000 []
+is_a: UBERON:0002616 ! regional part of brain
+relationship: part_of UBERON:0000451 ! prefrontal cortex
+property_value: dc-contributor https://orcid.org/0000-0001-7628-5565 
+property_value: dc-contributor https://orcid.org/0000-0002-4964-5083
+creation_date: 2025-04-23
+
 [Term]
 id: UBERON:4500002
 name: upper uroneural

```

## Agent Attempts (11)

| # | Model | Runtime | F1 | P | R | Blob | Eval PR | Detail |
|---|-------|---------|-----|-----|-----|------|---------|--------|
| 1 | claude-sonnet-4.5 | claude | 0.588 | 0.556 | 0.625 | `33beb1b` | [#503](https://github.com/ai4curation/eval-ont-agent-uberon/pull/503) | [attempt](attempts/pr503.md) |
| 2 | kimi-k2.6 | opencode | 0.588 | 0.556 | 0.625 | `d1bcab3` | [#463](https://github.com/ai4curation/eval-ont-agent-uberon/pull/463) | [attempt](attempts/pr463.md) |
| 3 | claude-opus-4.7 | claude | 0.571 | 0.667 | 0.500 | `97cb728` | [#241](https://github.com/ai4curation/eval-ont-agent-uberon/pull/241) | [attempt](attempts/pr241.md) |
| 4 | claude-haiku-4.5 | claude | 0.556 | 0.556 | 0.556 | `a4814a9` | [#565](https://github.com/ai4curation/eval-ont-agent-uberon/pull/565) | [attempt](attempts/pr565.md) |
| 5 | claude-haiku-4.5 | claude | 0.556 | 0.556 | 0.556 | `a4814a9` | [#505](https://github.com/ai4curation/eval-ont-agent-uberon/pull/505) | [attempt](attempts/pr505.md) |
| 6 | gpt-5.5 | codex | 0.500 | 0.667 | 0.400 | `2122eb5` | [#25](https://github.com/ai4curation/eval-ont-agent-uberon/pull/25) | [attempt](attempts/pr25.md) |
| 7 | gpt-5.4 | opencode | 0.476 | 0.556 | 0.417 | `0669647` | [#654](https://github.com/ai4curation/eval-ont-agent-uberon/pull/654) | [attempt](attempts/pr654.md) |
| 8 | gpt-5.4 | opencode | 0.476 | 0.556 | 0.417 | `0669647` | [#597](https://github.com/ai4curation/eval-ont-agent-uberon/pull/597) | [attempt](attempts/pr597.md) |
| 9 | gpt-5.5 | opencode | 0.476 | 0.556 | 0.417 | `76a602f` | [#64](https://github.com/ai4curation/eval-ont-agent-uberon/pull/64) | [attempt](attempts/pr64.md) |
| 10 | gpt-5.5 | opencode | 0.476 | 0.556 | 0.417 | `76a602f` | [#43](https://github.com/ai4curation/eval-ont-agent-uberon/pull/43) | [attempt](attempts/pr43.md) |
| 11 | gpt-5.4 | codex | 0.400 | 0.556 | 0.312 | `50f64a8` | [#77](https://github.com/ai4curation/eval-ont-agent-uberon/pull/77) | [attempt](attempts/pr77.md) |
