---
ontology: go-ontology
repo: geneontology/go-ontology
issue_number: 32018
pr_number: 32021
issue_title: 'Obsoletion request: ergothioneine biosynthetic process terms'
pr_author: edwong57
pr_merged_at: '2026-05-04'
task_type: obsoletion
difficulty: simple
scoping: tightly_scoped
scope: multi_term
review_outcome: approved_first_time
num_agent_attempts: 11
generated_at: '2026-05-15'
domain_area: biological_process
best_f1: 0.148
best_model: gpt-5.4
---

# PR #32021 — Obsoletion request: ergothioneine biosynthetic process terms

**go-ontology** | [geneontology/go-ontology](https://github.com/geneontology/go-ontology) | [Issue #32018](https://github.com/geneontology/go-ontology/issues/32018) | [PR #32021](https://github.com/geneontology/go-ontology/pull/32021) | @edwong57 | merged 2026-05-04

`obsoletion` `simple` `tightly_scoped` `approved_first_time`

## Context

Issue #32018 requested obsoletion of ergothioneine biosynthetic process terms (GO:0140479 and GO:0052704). Before these terms could be fully obsoleted, their taxon constraints in `only_in_taxon.tsv` needed to be removed. This PR handles that specific cleanup step.

## Changes Made

In `src/taxon_constraints/only_in_taxon.tsv`, two rows were removed:
- The entry for GO:0140479 (ergothioneine biosynthetic process)
- The entry for GO:0052704 (related ergothioneine term)

This is a pure deletion with no additions, reflecting the removal of constraints that are no longer meaningful for terms being obsoleted.

## Resolution

Merged directly. This is a routine cleanup step in the GO obsoletion workflow: when a term is obsoleted, its taxon constraints must also be removed since they no longer serve a purpose. The change is purely mechanical and low-risk.

## Curation Note (data quality)

**This is a poor evaluation case — the selected gold PR is only a sub-step of the human resolution.**

Issue #32018 asked for the full obsoletion of `GO:0052704` and `GO:0140479`, replacement by the parent `GO:0052699`, and addition of two MetaCyc pathway xrefs (`PWY-7255`, `PWY-7550`) as `skos:narrowMatch` to `GO:0052699`. The humans split this work across **three** PRs:

- **#32021** (the selected `pr_number`/gold) — only deletes the two `only_in_taxon.tsv` rows (the taxon-constraint precondition; obsoletion CI fails until these are removed).
- **#32023** — adds the MetaCyc narrowMatch xrefs to `GO:0052699`, obsoletes `GO:0140479`, rewires the dependent MF `part_of` link.
- **#32069** — obsoletes `GO:0052704`, fixes the `GO:0052707` `replaced_by` chain, rewires its dependent MF `part_of` link.

Because the metadiff compares each attempt only against #32021 (≈2 lines of a much larger change), 10/11 attempts score F1 = 0.000 and the "best" is 0.148 — even though agents that did the full, correct obsoletion in a single PR (e.g. Attempt 1 / eval PR #222) effectively reproduced the union of all three human PRs.

**For scoring/aggregation:** exclude or down-weight this case's metadiff. **For review:** judge attempts against the issue text and the union of #32021 + #32023 + #32069, not the single gold PR.

Flagged by claude-opus-4.7 on 2026-05-15 during a `review-agent-pr` session.

## Human Diff

```diff
diff --git a/src/taxon_constraints/only_in_taxon.tsv b/src/taxon_constraints/only_in_taxon.tsv
index e3ab62640..d6018154d 100644
--- a/src/taxon_constraints/only_in_taxon.tsv
+++ b/src/taxon_constraints/only_in_taxon.tsv
@@ -742,8 +742,6 @@ GO:0006836	neurotransmitter transport	NCBITaxon:33208	Metazoa
 GO:0140446	fumigermin biosynthetic process	NCBITaxon:4751	Fungi	
 GO:0036411	H-NS-Cnu complex	NCBITaxon:2	Bacteria	
 GO:1990198	ModE complex	NCBITaxon:2	Bacteria	
-GO:0052704	ergothioneine biosynthesis from histidine via gamma-glutamyl-hercynylcysteine sulfoxide	NCBITaxon:2	Bacteria	
-GO:0140479	ergothioneine biosynthesis from histidine via hercynylcysteine sulfoxide synthase	NCBITaxon:4751	Fungi	
 GO:0140495	migracytosis	NCBITaxon:7742	Vertebrata <Metazoa>	
 GO:0120259	7SK snRNP	NCBITaxon:33208	Metazoa	
 GO:0120260	ciliary microtubule quartet	NCBITaxon:5653	Kinetoplastida	

```

## Agent Attempts (11)

| # | Model | Runtime | F1 | P | R | Blob | Eval PR | Detail |
|---|-------|---------|-----|-----|-----|------|---------|--------|
| 1 | gpt-5.4 | codex | 0.148 | 1.000 | 0.080 | `9ea0cec` | [#222](https://github.com/ai4curation/eval-ont-agent-go/pull/222) | [attempt](attempts/pr222.md) |
| 2 | claude-sonnet-4.5 | copilot | 0.000 | 0.000 | 0.000 | `8b8ea8f` | [#499](https://github.com/ai4curation/eval-ont-agent-go/pull/499) | [attempt](attempts/pr499.md) |
| 3 | claude-sonnet-4.5 | claude | 0.000 | 0.000 | 0.000 | `dec6c36` | [#485](https://github.com/ai4curation/eval-ont-agent-go/pull/485) | [attempt](attempts/pr485.md) |
| 4 | claude-sonnet-4.5 | copilot | 0.000 | 0.000 | 0.000 | `8b8ea8f` | [#438](https://github.com/ai4curation/eval-ont-agent-go/pull/438) | [attempt](attempts/pr438.md) |
| 5 | claude-opus-4.7 | claude | 0.000 | 0.000 | 0.000 | `dae7ce4` | [#358](https://github.com/ai4curation/eval-ont-agent-go/pull/358) | [attempt](attempts/pr358.md) |
| 6 | kimi-k2.6 | opencode | 0.000 | 0.000 | 0.000 | `b67e170` | [#286](https://github.com/ai4curation/eval-ont-agent-go/pull/286) | [attempt](attempts/pr286.md) |
| 7 | gemma-4-31b | opencode | 0.000 | 0.000 | 0.000 | `8c7827d` | [#262](https://github.com/ai4curation/eval-ont-agent-go/pull/262) | [attempt](attempts/pr262.md) |
| 8 | claude-haiku-4.5 | claude | 0.000 | 0.000 | 0.000 | `5be511e` | [#218](https://github.com/ai4curation/eval-ont-agent-go/pull/218) | [attempt](attempts/pr218.md) |
| 9 | gpt-5.5 | opencode | 0.000 | 0.000 | 0.000 | `acf29bd` | [#171](https://github.com/ai4curation/eval-ont-agent-go/pull/171) | [attempt](attempts/pr171.md) |
| 10 | gpt-5.5 | opencode | 0.000 | 0.000 | 0.000 | `acf29bd` | [#153](https://github.com/ai4curation/eval-ont-agent-go/pull/153) | [attempt](attempts/pr153.md) |
| 11 | gpt-5.5 | codex | 0.000 | 0.000 | 0.000 | `6ac11d2` | [#138](https://github.com/ai4curation/eval-ont-agent-go/pull/138) | [attempt](attempts/pr138.md) |
