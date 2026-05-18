---
ontology: uberon
repo: obophenotype/uberon
issue_number: 3003
pr_number: 3511
issue_title: review definition of cardiac septum and its child terms
pr_author: cmungall
pr_merged_at: '2025-04-24'
task_type: axiom_repair
difficulty: medium
scoping: tightly_scoped
scope: single_term
review_outcome: approved_first_time
num_agent_attempts: 13
generated_at: '2026-05-17'
domain_area: cardiac-anatomy
best_f1: 0.5
best_model: claude-haiku-4.5
---

# PR #3511 — review definition of cardiac septum and its child terms

**uberon** | [obophenotype/uberon](https://github.com/obophenotype/uberon) | [Issue #3003](https://github.com/obophenotype/uberon/issues/3003) | [PR #3511](https://github.com/obophenotype/uberon/pull/3511) | @cmungall | merged 2025-04-24

`axiom_repair` `medium` `tightly_scoped` `approved_first_time`

## Context

Issue #3003 noted that the definition of cardiac septum (UBERON:0002099) was too narrow, mentioning only septa between atria and ventricles. However, child terms in the hierarchy include atrioventricular septum and outflow tract septum, which the original definition did not accommodate. The issue had been open since August 2023.

## Changes Made

The PR updated the definition of UBERON:0002099 (cardiac septum) to include all septa between parts of the heart, specifically accommodating the outflow tract. This was a single line replacement in uberon-edit.obo, changing the def tag to a broader formulation that encompasses all child terms.

## Resolution

Medium difficulty. While the change is a single-line definition update, an agent would need to inspect the child terms of cardiac septum, understand that the outflow tract septum is a valid subtype, and craft a definition broad enough to cover all children without being overly vague. The nearly two-year gap between issue and resolution reflects the careful consideration needed for definitional changes to anatomical grouping terms.

## Curation Note (data quality)

Flagged `case_quality: poor` (reason `gold_verbatim_issue_text`) by claude-opus-4.7 on 2026-05-16 during detailed review of all 8 attempts.

**Why this is a poor metadiff reference:**

1. **Gold is a verbatim transcription of issue-supplied text.** Issue #3003's body contained an explicit "Suggested revision of textual definition": *"The thin membranous structure between parts of the heart, including the atria, ventricles, and outflow tract."* Gold PR #3511 (itself a dragon-ai-agent PR, merged 11 minutes after opening with no human review) copied this string byte-for-byte. Metadiff thus rewards copy-paste fidelity of the issue text, not curation reasoning. The single-line diff means the deletion of the old def matches for every attempt (→ precision/recall 0.5 each on that token) while any reworded — even improved — new def line never byte-matches gold, structurally **capping F1 at ≈0.5** for all eight attempts. Best F1 = 0.5; this ceiling is an artifact, not a quality signal.

2. **Gold violated the agent config's own mandates; attempts that complied are penalized.** `ai4curation/uberon-agent-config` CLAUDE.md instructs agents to add `term_tracker_item` linking the issue, to prefer a PMID definition xref, and to run `robot convert` reserialization before commit. Gold did none of these. Attempts that correctly followed these instructions (e.g. #307, #243, #27 adding `term_tracker_item`; #75 substituting a verified on-topic PMID:30795606) lose recall against the minimalist gold — they are punished by metadiff for instruction compliance.

3. **Reserialization churn artifact on two attempts.** #154 (gemma-4-31b/opencode, F1 0.25) and #199 (sonnet-4.5/copilot, F1 0.18) carry robot-convert reserialization churn on terms unrelated to the issue (UBERON:0003532 hindlimb skin synonym reorder, UBERON:0007182 blank lines, UBERON:0013540 Brodmann area 9 and UBERON:0034891 insular cortex xref reordering). This is the config-instructed reserialization applied to an eval base that was not pre-normalized — the precise serialization-glitch problem curator @gouttegd raised on source PR #3511. The churn conflates an environment artifact with agent quality.

**Net assessment:** All 8 attempts produced a substantively correct, semantically valid broadening of UBERON:0002099 covering the AV-septum and outflow-tract children. Six are clean successes on substance (the haiku runs #286/#182, gpt-5.4 #75, sonnet #307, opus #243, gpt-5.5 #27); two (#154, #199) are partial_success — correct core fix marred by reserialization scope creep. No attempt is a true failure. Downstream scoring/aggregation should down-weight or exclude this case; the metadiff F1 (best 0.5) does **not** represent agent performance here.

## Human Diff

```diff
diff --git a/src/ontology/uberon-edit.obo b/src/ontology/uberon-edit.obo
index 92902c0f41..3c8c5b7352 100644
--- a/src/ontology/uberon-edit.obo
+++ b/src/ontology/uberon-edit.obo
@@ -40925,7 +40925,7 @@ property_value: external_ontology_notes "FMA also has terms for the apical zone"
 [Term]
 id: UBERON:0002099
 name: cardiac septum
-def: "The thin membranous structure between the two heart atria or the thick muscular structure between the two heart ventricles." [MESH:A07.541.459]
+def: "The thin membranous structure between parts of the heart, including the atria, ventricles, and outflow tract." [MESH:A07.541.459]
 subset: pheno_slim
 subset: uberon_slim
 synonym: "cardiac septa" EXACT OMO:0003004 []

```

## Agent Attempts (13)

| # | Model | Runtime | F1 | P | R | Blob | Eval PR | Detail |
|---|-------|---------|-----|-----|-----|------|---------|--------|
| 1 | claude-haiku-4.5 | claude | 0.500 | 0.500 | 0.500 | `b7797d0` | [#286](https://github.com/ai4curation/eval-ont-agent-uberon/pull/286) | [attempt](attempts/pr286.md) |
| 2 | claude-haiku-4.5 | claude | 0.500 | 0.500 | 0.500 | `b7797d0` | [#182](https://github.com/ai4curation/eval-ont-agent-uberon/pull/182) | [attempt](attempts/pr182.md) |
| 3 | gpt-5.4 | codex | 0.500 | 0.500 | 0.500 | `ae2e557` | [#75](https://github.com/ai4curation/eval-ont-agent-uberon/pull/75) | [attempt](attempts/pr75.md) |
| 4 | gpt-5.4 | opencode | 0.400 | 0.500 | 0.333 | `0b8a5d4` | [#657](https://github.com/ai4curation/eval-ont-agent-uberon/pull/657) | [attempt](attempts/pr657.md) |
| 5 | gpt-5.5 | opencode | 0.400 | 0.500 | 0.333 | `66e3342` | [#627](https://github.com/ai4curation/eval-ont-agent-uberon/pull/627) | [attempt](attempts/pr627.md) |
| 6 | gpt-5.4 | opencode | 0.400 | 0.500 | 0.333 | `0b8a5d4` | [#599](https://github.com/ai4curation/eval-ont-agent-uberon/pull/599) | [attempt](attempts/pr599.md) |
| 7 | gpt-5.5 | opencode | 0.400 | 0.500 | 0.333 | `66e3342` | [#567](https://github.com/ai4curation/eval-ont-agent-uberon/pull/567) | [attempt](attempts/pr567.md) |
| 8 | kimi-k2.6 | opencode | 0.400 | 0.500 | 0.333 | `ebf0123` | [#455](https://github.com/ai4curation/eval-ont-agent-uberon/pull/455) | [attempt](attempts/pr455.md) |
| 9 | claude-sonnet-4.5 | claude | 0.400 | 0.500 | 0.333 | `5455704` | [#307](https://github.com/ai4curation/eval-ont-agent-uberon/pull/307) | [attempt](attempts/pr307.md) |
| 10 | claude-opus-4.7 | claude | 0.400 | 0.500 | 0.333 | `faea424` | [#243](https://github.com/ai4curation/eval-ont-agent-uberon/pull/243) | [attempt](attempts/pr243.md) |
| 11 | gpt-5.5 | codex | 0.400 | 0.500 | 0.333 | `4bd1afe` | [#27](https://github.com/ai4curation/eval-ont-agent-uberon/pull/27) | [attempt](attempts/pr27.md) |
| 12 | gemma-4-31b | opencode | 0.250 | 0.500 | 0.167 | `1dc38a1` | [#154](https://github.com/ai4curation/eval-ont-agent-uberon/pull/154) | [attempt](attempts/pr154.md) |
| 13 | claude-sonnet-4.5 | copilot | 0.182 | 0.500 | 0.111 | `b9ae65f` | [#199](https://github.com/ai4curation/eval-ont-agent-uberon/pull/199) | [attempt](attempts/pr199.md) |
