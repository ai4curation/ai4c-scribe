---
ontology: mondo
repo: monarch-initiative/mondo
issue_number: 9987
pr_number: 10094
issue_title: 'Copy-paste error in inborn_metabolic_disrupts.yaml: definition says
  ''acquired'' instead of ''inherited'''
pr_author: sabrinatoro
pr_merged_at: '2026-03-31'
task_type: axiom_repair
difficulty: simple
scoping: tightly_scoped
scope: single_term
review_outcome: approved_first_time
num_agent_attempts: 10
generated_at: '2026-05-15'
best_f1: 1.0
best_model: claude-sonnet-4.5
---

# PR #10094 — Copy-paste error in inborn_metabolic_disrupts.yaml: definition says 'acquired' instead of 'inherited'

**mondo** | [monarch-initiative/mondo](https://github.com/monarch-initiative/mondo) | [Issue #9987](https://github.com/monarch-initiative/mondo/issues/9987) | [PR #10094](https://github.com/monarch-initiative/mondo/pull/10094) | @sabrinatoro | merged 2026-03-31

`axiom_repair` `simple` `tightly_scoped` `approved_first_time`

## Context

Issue #9987 reported a copy-paste error in the DOSDP pattern file `src/patterns/dosdp-patterns/inborn_metabolic_disrupts.yaml`. Line 46 of the definition template read "An acquired metabolic disease that is has its basis in the disruption of %s" when it should say "inherited" instead of "acquired". This error propagated incorrect definitions to all terms instantiated from this pattern.

## Changes Made

The PR made a single-character semantic fix in the DOSDP pattern file, changing "acquired" to "inherited" in the definition template text. This 1 addition and 1 deletion corrects the definition for all terms generated from the `inborn_metabolic_disrupts` pattern, which by definition describes inherited (not acquired) metabolic diseases.

## Resolution

Simple difficulty as a clear-cut word substitution fix. However, this case is notable because errors in DOSDP pattern files have multiplicative impact across all terms instantiated from that pattern. An agent should recognize that pattern file edits have broader implications than single-term edits and could potentially flag such inconsistencies proactively during quality control.

## Human Diff

```diff
diff --git a/src/patterns/dosdp-patterns/inborn_metabolic_disrupts.yaml b/src/patterns/dosdp-patterns/inborn_metabolic_disrupts.yaml
index bac19f0a39..a1b914908e 100644
--- a/src/patterns/dosdp-patterns/inborn_metabolic_disrupts.yaml
+++ b/src/patterns/dosdp-patterns/inborn_metabolic_disrupts.yaml
@@ -43,7 +43,7 @@ annotations:
   - process
 
 def:
-  text: An acquired metabolic disease that is has its basis in the disruption of %s.
+  text: An inherited metabolic disease that has its basis in the disruption of %s.
   vars:
   - process
 

```

## Agent Attempts (10)

| # | Model | Runtime | F1 | P | R | Eval PR | Detail |
|---|-------|---------|-----|-----|-----|---------|--------|
| 1 | claude-sonnet-4.5 | claude | 1.000 | 1.000 | 1.000 | [#430](https://github.com/ai4curation/eval-ont-agent-mondo/pull/430) | [attempt](attempts/pr430.md) |
| 2 | claude-opus-4.7 | claude | 1.000 | 1.000 | 1.000 | [#370](https://github.com/ai4curation/eval-ont-agent-mondo/pull/370) | [attempt](attempts/pr370.md) |
| 3 | claude-sonnet-4.5 | copilot | 1.000 | 1.000 | 1.000 | [#330](https://github.com/ai4curation/eval-ont-agent-mondo/pull/330) | [attempt](attempts/pr330.md) |
| 4 | kimi-k2.6 | opencode | 1.000 | 1.000 | 1.000 | [#244](https://github.com/ai4curation/eval-ont-agent-mondo/pull/244) | [attempt](attempts/pr244.md) |
| 5 | gemma-4-31b | opencode | 1.000 | 1.000 | 1.000 | [#212](https://github.com/ai4curation/eval-ont-agent-mondo/pull/212) | [attempt](attempts/pr212.md) |
| 6 | claude-haiku-4.5 | claude | 1.000 | 1.000 | 1.000 | [#201](https://github.com/ai4curation/eval-ont-agent-mondo/pull/201) | [attempt](attempts/pr201.md) |
| 7 | gpt-5.5 | opencode | 1.000 | 1.000 | 1.000 | [#129](https://github.com/ai4curation/eval-ont-agent-mondo/pull/129) | [attempt](attempts/pr129.md) |
| 8 | gpt-5.5 | opencode | 1.000 | 1.000 | 1.000 | [#109](https://github.com/ai4curation/eval-ont-agent-mondo/pull/109) | [attempt](attempts/pr109.md) |
| 9 | gpt-5.4 | codex | 0.857 | 1.000 | 0.750 | [#176](https://github.com/ai4curation/eval-ont-agent-mondo/pull/176) | [attempt](attempts/pr176.md) |
| 10 | gpt-5.5 | codex | 0.353 | 1.000 | 0.214 | [#93](https://github.com/ai4curation/eval-ont-agent-mondo/pull/93) | [attempt](attempts/pr93.md) |
