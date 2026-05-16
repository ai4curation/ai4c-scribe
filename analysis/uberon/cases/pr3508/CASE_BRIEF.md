---
ontology: uberon
repo: obophenotype/uberon
issue_number: 2911
pr_number: 3508
issue_title: 'relation error: conus arteriosus has_part *uterine tube'
pr_author: cmungall
pr_merged_at: '2025-04-23'
task_type: axiom_repair
difficulty: medium
scoping: tightly_scoped
scope: multi_term
review_outcome: approved_first_time
num_agent_attempts: 8
generated_at: '2026-05-15'
domain_area: cardiac-anatomy
best_f1: 1.0
best_model: claude-sonnet-4.5
---

# PR #3508 — relation error: conus arteriosus has_part *uterine tube

**uberon** | [obophenotype/uberon](https://github.com/obophenotype/uberon) | [Issue #2911](https://github.com/obophenotype/uberon/issues/2911) | [PR #3508](https://github.com/obophenotype/uberon/pull/3508) | @cmungall | merged 2025-04-23

`axiom_repair` `medium` `tightly_scoped` `approved_first_time`

## Context

Issue #2911 reported that UBERON:0007181 (serosa of infundibulum of uterine tube) and UBERON:0007182 (muscle layer of infundibulum of uterine tube) had erroneous part_of relationships to UBERON:0003983 (conus arteriosus), a cardiac structure. The error likely arose because "infundibulum" is used in both cardiac anatomy (infundibulum of the right ventricle / conus arteriosus) and reproductive anatomy (infundibulum of the uterine tube).

## Changes Made

The PR removed the incorrect part_of relationships linking the two uterine tube structures to the conus arteriosus. Two lines were replaced in uberon-edit.obo, correcting the relationship targets so that the uterine tube structures relate only to the uterine tube infundibulum, not the cardiac infundibulum.

## Resolution

Medium difficulty. An agent would need to recognize the homonym-based confusion between cardiac and reproductive uses of "infundibulum," identify which relationships are erroneous, and remove them without affecting the correct uterine tube hierarchy. The issue was open for nearly two years before resolution. Co-authored by the dragon-ai-agent.

## Human Diff

```diff
diff --git a/src/ontology/uberon-edit.obo b/src/ontology/uberon-edit.obo
index 82a8b281c3..92902c0f41 100644
--- a/src/ontology/uberon-edit.obo
+++ b/src/ontology/uberon-edit.obo
@@ -119281,7 +119281,7 @@ xref: EMAPA:29903
 xref: FMA:18324
 intersection_of: UBERON:0000042 ! serous membrane
 intersection_of: part_of UBERON:0003984 ! uterine tube infundibulum
-relationship: part_of UBERON:0003983 ! conus arteriosus
+
 
 [Term]
 id: UBERON:0007182
@@ -119294,7 +119294,7 @@ xref: EMAPA:31264
 xref: FMA:18336
 intersection_of: UBERON:0006660 ! muscular coat
 intersection_of: part_of UBERON:0003984 ! uterine tube infundibulum
-relationship: part_of UBERON:0003983 ! conus arteriosus
+
 
 [Term]
 id: UBERON:0007185

```

## Agent Attempts (8)

| # | Model | Runtime | F1 | P | R | Blob | Eval PR | Detail |
|---|-------|---------|-----|-----|-----|------|---------|--------|
| 1 | claude-sonnet-4.5 | claude | 1.000 | 1.000 | 1.000 | `1dec482` | [#296](https://github.com/ai4curation/eval-ont-agent-uberon/pull/296) | [attempt](attempts/pr296.md) |
| 2 | claude-haiku-4.5 | claude | 1.000 | 1.000 | 1.000 | `1dec482` | [#85](https://github.com/ai4curation/eval-ont-agent-uberon/pull/85) | [attempt](attempts/pr85.md) |
| 3 | gpt-5.4 | codex | 1.000 | 1.000 | 1.000 | `1dec482` | [#74](https://github.com/ai4curation/eval-ont-agent-uberon/pull/74) | [attempt](attempts/pr74.md) |
| 4 | gpt-5.5 | opencode | 1.000 | 1.000 | 1.000 | `1dec482` | [#61](https://github.com/ai4curation/eval-ont-agent-uberon/pull/61) | [attempt](attempts/pr61.md) |
| 5 | gpt-5.5 | opencode | 1.000 | 1.000 | 1.000 | `1dec482` | [#46](https://github.com/ai4curation/eval-ont-agent-uberon/pull/46) | [attempt](attempts/pr46.md) |
| 6 | claude-sonnet-4.5 | copilot | 0.333 | 1.000 | 0.200 | `6ce30bc` | [#197](https://github.com/ai4curation/eval-ont-agent-uberon/pull/197) | [attempt](attempts/pr197.md) |
| 7 | gpt-5.5 | codex | 0.333 | 1.000 | 0.200 | `6ce30bc` | [#24](https://github.com/ai4curation/eval-ont-agent-uberon/pull/24) | [attempt](attempts/pr24.md) |
| 8 | claude-opus-4.7 | claude | 0.250 | 1.000 | 0.143 | `011e530` | [#240](https://github.com/ai4curation/eval-ont-agent-uberon/pull/240) | [attempt](attempts/pr240.md) |
