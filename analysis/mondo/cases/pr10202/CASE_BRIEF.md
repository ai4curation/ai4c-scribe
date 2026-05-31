---
ontology: mondo
repo: monarch-initiative/mondo
issue_number: 9875
pr_number: 10202
issue_title: Typo for MONDO:0700039 bladder exstrophy-epispadias-cloacal extrophy
  complex
pr_author: MeeSiing
pr_merged_at: '2026-04-30'
task_type: other
difficulty: simple
scoping: tightly_scoped
scope: single_term
review_outcome: approved_first_time
num_agent_attempts: 13
generated_at: '2026-05-17'
best_f1: 1.0
best_model: gpt-5.5
---

# PR #10202 — Typo for MONDO:0700039 bladder exstrophy-epispadias-cloacal extrophy complex

**mondo** | [monarch-initiative/mondo](https://github.com/monarch-initiative/mondo) | [Issue #9875](https://github.com/monarch-initiative/mondo/issues/9875) | [PR #10202](https://github.com/monarch-initiative/mondo/pull/10202) | @MeeSiing | merged 2026-04-30

`other` `simple` `tightly_scoped` `approved_first_time`

## Context

Issue #9875 reported a typographical error in the label of MONDO:0700039 (bladder exstrophy-epispadias-cloacal extrophy complex). The term's display name contained a misspelling that was visible in OLS and other ontology browsers, affecting searchability and professional presentation.

## Changes Made

The PR corrected the typo in MONDO:0700039's label within mondo-edit.obo. The 2 additions and 1 deletion reflect the corrected label line replacing the erroneous one, plus potentially an additional annotation (e.g., updating a synonym to match the corrected label).

## Resolution

Trivial difficulty representing the simplest possible ontology maintenance task. The curator located the term stanza and corrected the character-level error. An agent should handle typo fixes with high confidence, needing only to identify the specific characters to change and verify the correction matches the issue report.

## Human Diff

```diff
diff --git a/src/ontology/mondo-edit.obo b/src/ontology/mondo-edit.obo
index 1d63d0424f..e6e017c643 100644
--- a/src/ontology/mondo-edit.obo
+++ b/src/ontology/mondo-edit.obo
@@ -589672,7 +589672,7 @@ property_value: http://purl.org/dc/terms/creator https://orcid.org/0000-0002-414
 
 [Term]
 id: MONDO:0700039
-name: bladder exstrophy-epispadias-cloacal extrophy complex
+name: bladder exstrophy-epispadias-cloacal exstrophy complex
 def: "An anterior midline defect with variable expression involving the infraumbilical abdominal wall including the pelvis, urinary tract, and external genitalia." [OMIM:600057]
 subset: gard_rare {source="GARD:0026333", source="MONDO:GARD"}
 subset: nord_rare {source="MONDO:NORD"}
@@ -589688,6 +589688,7 @@ relationship: excluded_from_qc_check http://purl.obolibrary.org/obo/mondo/sparql
 property_value: curated_content_resource "https://www.malacards.org/card/bladder_exstrophy_and_epispadias_complex" xsd:anyURI {source="MONDO:MalaCards"}
 property_value: http://purl.org/dc/terms/creator https://orcid.org/0000-0002-4142-7153
 property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/3650" xsd:anyURI
+property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9875" xsd:anyURI
 
 [Term]
 id: MONDO:0700040

```

## Agent Attempts (13)

| # | Model | Runtime | F1 | P | R | Blob | Eval PR | Detail |
|---|-------|---------|-----|-----|-----|------|---------|--------|
| 1 | gpt-5.5 | opencode | 1.000 | 1.000 | 1.000 | `e6e017c` | [#722](https://github.com/ai4curation/eval-ont-agent-mondo/pull/722) | [attempt](attempts/pr722.md) |
| 2 | gpt-5.5 | opencode | 1.000 | 1.000 | 1.000 | `e6e017c` | [#669](https://github.com/ai4curation/eval-ont-agent-mondo/pull/669) | [attempt](attempts/pr669.md) |
| 3 | gpt-5.4 | codex | 1.000 | 1.000 | 1.000 | `e6e017c` | [#574](https://github.com/ai4curation/eval-ont-agent-mondo/pull/574) | [attempt](attempts/pr574.md) |
| 4 | gpt-5.4 | opencode | 0.800 | 0.667 | 1.000 | `911990e` | [#751](https://github.com/ai4curation/eval-ont-agent-mondo/pull/751) | [attempt](attempts/pr751.md) |
| 5 | gpt-5.4 | opencode | 0.800 | 0.667 | 1.000 | `911990e` | [#700](https://github.com/ai4curation/eval-ont-agent-mondo/pull/700) | [attempt](attempts/pr700.md) |
| 6 | claude-sonnet-4.5 | claude | 0.800 | 0.667 | 1.000 | `911990e` | [#446](https://github.com/ai4curation/eval-ont-agent-mondo/pull/446) | [attempt](attempts/pr446.md) |
| 7 | claude-haiku-4.5 | claude | 0.800 | 0.667 | 1.000 | `911990e` | [#428](https://github.com/ai4curation/eval-ont-agent-mondo/pull/428) | [attempt](attempts/pr428.md) |
| 8 | claude-haiku-4.5 | claude | 0.800 | 0.667 | 1.000 | `911990e` | [#314](https://github.com/ai4curation/eval-ont-agent-mondo/pull/314) | [attempt](attempts/pr314.md) |
| 9 | gemma-4-31b | opencode | 0.800 | 0.667 | 1.000 | `911990e` | [#290](https://github.com/ai4curation/eval-ont-agent-mondo/pull/290) | [attempt](attempts/pr290.md) |
| 10 | kimi-k2.6 | opencode | 0.800 | 0.667 | 1.000 | `911990e` | [#269](https://github.com/ai4curation/eval-ont-agent-mondo/pull/269) | [attempt](attempts/pr269.md) |
| 11 | gemma-4-31b | opencode | 0.800 | 0.667 | 1.000 | `911990e` | [#205](https://github.com/ai4curation/eval-ont-agent-mondo/pull/205) | [attempt](attempts/pr205.md) |
| 12 | gpt-5.5 | codex | 0.750 | 1.000 | 0.600 | `ee922f2` | [#562](https://github.com/ai4curation/eval-ont-agent-mondo/pull/562) | [attempt](attempts/pr562.md) |
| 13 | claude-opus-4.7 | claude | 0.571 | 0.667 | 0.500 | `a5af3ce` | [#399](https://github.com/ai4curation/eval-ont-agent-mondo/pull/399) | [attempt](attempts/pr399.md) |
