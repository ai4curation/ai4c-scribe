---
ontology: go-ontology
repo: geneontology/go-ontology
issue_number: 31985
pr_number: 31986
issue_title: GO:0102177 24-methylenelophenol methyl oxidase activity
pr_author: sjm41
pr_merged_at: '2026-04-27'
task_type: reclassification
difficulty: hard
scoping: tightly_scoped
scope: single_term
review_outcome: approved_first_time
num_agent_attempts: 13
generated_at: '2026-05-17'
domain_area: molecular_function
best_f1: 0.96
best_model: claude-opus-4.7
---

# PR #31986 — GO:0102177 24-methylenelophenol methyl oxidase activity

**go-ontology** | [geneontology/go-ontology](https://github.com/geneontology/go-ontology) | [Issue #31985](https://github.com/geneontology/go-ontology/issues/31985) | [PR #31986](https://github.com/geneontology/go-ontology/pull/31986) | @sjm41 | merged 2026-04-27

`reclassification` `hard` `tightly_scoped` `approved_first_time`

## Context

Issue #31985 identified that GO:0102177 carried an `xref: EC:1.14.18.11` (plant 4-alpha-monomethylsterol monooxygenase) but its name, definition, RHEA cross-reference, MetaCyc cross-reference, and parent term all described a different reaction (an NADH-dependent partial reaction). All five fields needed realignment to match the actual EC:1.14.18.11 reaction.

## Changes Made

In `src/ontology/go-edit.obo`, GO:0102177 was comprehensively realigned:
- Name updated to match EC:1.14.18.11 nomenclature
- Definition rewritten to describe the correct reaction
- RHEA cross-reference corrected
- MetaCyc cross-reference corrected
- Parent `is_a` relationship changed to the appropriate oxidase parent
- Net +2 lines reflecting addition of previously missing xrefs

## Resolution

Merged same-day by the reporting curator (@sjm41). This is a technically demanding correction because it requires reconciling multiple external database identifiers (EC, RHEA, MetaCyc) with the GO term hierarchy to ensure all five aspects of the term (name, def, xrefs, parent) describe the same biochemical reaction.

## Human Diff

```diff
diff --git a/src/ontology/go-edit.obo b/src/ontology/go-edit.obo
index dd6593ace..a76eab953 100644
--- a/src/ontology/go-edit.obo
+++ b/src/ontology/go-edit.obo
@@ -440991,14 +440991,16 @@ replaced_by: GO:0000253
 
 [Term]
 id: GO:0102177
-name: 24-methylenelophenol methyl oxidase activity
+name: 4alpha-monomethylsterol monooxygenase activity
 namespace: molecular_function
-def: "Catalysis of the reaction: 24-methylenelophenol + O2 + NADH + H+ = 4alpha-hydroxymethyl-ergosta-7,24(241)-dien-3beta-ol + NAD + H2O." [GOC:pz, PMID:11707264, RHEA:58872]
+def: "Catalysis of the reaction: 24-methylidenelophenol + 6 Fe(II)-[cytochrome b5] + 3 O2 + 5 H+ = 4alpha-carboxy-ergosta-7,24(24(1))-dien-3beta-ol + 6 Fe(III)-[cytochrome b5] + 4 H2O." [PMID:11707264, RHEA:58868]
+synonym: "24-methylenelophenol methyl oxidase activity" EXACT []
 xref: EC:1.14.18.11 {source="skos:exactMatch"}
-xref: MetaCyc:RXN-11930
-xref: RHEA:58872 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+xref: MetaCyc:RXN-19724
+xref: RHEA:58868 {source="skos:exactMatch"}
+is_a: GO:0016716 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, another compound as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31985" xsd:anyURI
 
 [Term]
 id: GO:0102178

```

## Agent Attempts (13)

| # | Model | Runtime | F1 | P | R | Blob | Eval PR | Detail |
|---|-------|---------|-----|-----|-----|------|---------|--------|
| 1 | claude-opus-4.7 | claude | 0.960 | 1.000 | 0.923 | `30d280f` | [#352](https://github.com/ai4curation/eval-ont-agent-go/pull/352) | [attempt](attempts/pr352.md) |
| 2 | gpt-5.4 | opencode | 0.957 | 0.917 | 1.000 | `4a660c7` | [#652](https://github.com/ai4curation/eval-ont-agent-go/pull/652) | [attempt](attempts/pr652.md) |
| 3 | gpt-5.4 | opencode | 0.957 | 0.917 | 1.000 | `4a660c7` | [#605](https://github.com/ai4curation/eval-ont-agent-go/pull/605) | [attempt](attempts/pr605.md) |
| 4 | gpt-5.4 | codex | 0.957 | 0.917 | 1.000 | `4a660c7` | [#548](https://github.com/ai4curation/eval-ont-agent-go/pull/548) | [attempt](attempts/pr548.md) |
| 5 | claude-sonnet-4.5 | copilot | 0.957 | 0.917 | 1.000 | `4a660c7` | [#494](https://github.com/ai4curation/eval-ont-agent-go/pull/494) | [attempt](attempts/pr494.md) |
| 6 | claude-sonnet-4.5 | copilot | 0.957 | 0.917 | 1.000 | `4a660c7` | [#424](https://github.com/ai4curation/eval-ont-agent-go/pull/424) | [attempt](attempts/pr424.md) |
| 7 | kimi-k2.6 | opencode | 0.957 | 0.917 | 1.000 | `4a660c7` | [#283](https://github.com/ai4curation/eval-ont-agent-go/pull/283) | [attempt](attempts/pr283.md) |
| 8 | gpt-5.5 | opencode | 0.909 | 0.833 | 1.000 | `6ab6948` | [#637](https://github.com/ai4curation/eval-ont-agent-go/pull/637) | [attempt](attempts/pr637.md) |
| 9 | gpt-5.5 | opencode | 0.909 | 0.833 | 1.000 | `6ab6948` | [#588](https://github.com/ai4curation/eval-ont-agent-go/pull/588) | [attempt](attempts/pr588.md) |
| 10 | claude-sonnet-4.5 | claude | 0.909 | 0.833 | 1.000 | `6ab6948` | [#479](https://github.com/ai4curation/eval-ont-agent-go/pull/479) | [attempt](attempts/pr479.md) |
| 11 | claude-haiku-4.5 | claude | 0.909 | 0.833 | 1.000 | `6ab6948` | [#409](https://github.com/ai4curation/eval-ont-agent-go/pull/409) | [attempt](attempts/pr409.md) |
| 12 | gpt-5.5 | codex | 0.870 | 0.833 | 0.909 | `3c3c9c5` | [#544](https://github.com/ai4curation/eval-ont-agent-go/pull/544) | [attempt](attempts/pr544.md) |
| 13 | gemma-4-31b | opencode | 0.818 | 0.750 | 0.900 | `fd87377` | [#253](https://github.com/ai4curation/eval-ont-agent-go/pull/253) | [attempt](attempts/pr253.md) |
