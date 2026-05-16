---
ontology: go-ontology
repo: geneontology/go-ontology
issue_number: 31636
pr_number: 31925
issue_title: rename GO:1990334 Bfa1-Bub2 complex to make it species agnostic
pr_author: dragon-ai-agent
pr_merged_at: '2026-04-20'
task_type: synonym_update
difficulty: simple
scoping: tightly_scoped
scope: single_term
review_outcome: approved_first_time
num_agent_attempts: 11
generated_at: '2026-05-15'
best_f1: 0.857
best_model: claude-sonnet-4.5
---

# PR #31925 — rename GO:1990334 Bfa1-Bub2 complex to make it species agnostic

**go-ontology** | [geneontology/go-ontology](https://github.com/geneontology/go-ontology) | [Issue #31636](https://github.com/geneontology/go-ontology/issues/31636) | [PR #31925](https://github.com/geneontology/go-ontology/pull/31925) | @dragon-ai-agent | merged 2026-04-20

`synonym_update` `simple` `tightly_scoped` `approved_first_time`

## Context

GO:1990334 was named `Bfa1-Bub2 complex` using S. cerevisiae-specific gene names. GO naming conventions prefer species-agnostic labels for complexes that are conserved across species. This complex functions as a two-component GTPase-activating protein (GAP) in both the mitotic exit network (MEN) in budding yeast and the septation initiation network (SIN) in fission yeast, where it is known as the Byr4-Cdc16 complex.

## Changes Made

The primary label was changed from `Bfa1-Bub2 complex` to `SIN/MEN two-component GAP complex`. The old S. cerevisiae name was retained as a NARROW synonym (`Bfa1-Bub2 complex`), and the S. pombe equivalent was added as another NARROW synonym (`Byr4-Cdc16 GAP complex`). The definition was updated to reference both the mitotic exit network (MEN, budding yeast) and septation initiation network (SIN, fission yeast) to support the species-agnostic label.

## Resolution

Easy difficulty because the naming convention is well-established in GO (species-agnostic primary labels with species-specific NARROW synonyms) and the biological equivalence of Bfa1-Bub2 and Byr4-Cdc16 complexes is well-documented. The main decision was the choice of species-agnostic label, which used the functional description (SIN/MEN two-component GAP complex) rather than any single species' nomenclature.

## Human Diff

```diff
diff --git a/src/ontology/go-edit.obo b/src/ontology/go-edit.obo
index abffd332f..859cb9e99 100644
--- a/src/ontology/go-edit.obo
+++ b/src/ontology/go-edit.obo
@@ -593152,11 +593152,14 @@ creation_date: 2014-03-17T14:11:35Z
 
 [Term]
 id: GO:1990334
-name: Bfa1-Bub2 complex
+name: SIN/MEN two-component GAP complex
 namespace: cellular_component
-def: "A protein complex that acts as a two-component GTPase-activating protein for Tem1 GTPase, thus regulating a signal transduction cascade, called the mitotic exit network (MEN), which is required for mitotic exit and cytokinesis. Bub2/Bfa1 keeps Tem1 inactive until the spindle is properly oriented, thus inhibiting MEN activation." [GOC:bhm, PMID:16449187]
+def: "A protein complex that acts as a two-component GTPase-activating protein for the Tem1/Spg1 GTPase, thus regulating a signal transduction cascade (the mitotic exit network, MEN, in budding yeast; the septation initiation network, SIN, in fission yeast), which is required for mitotic exit and cytokinesis. The complex keeps the GTPase inactive until the spindle is properly oriented, thus inhibiting MEN/SIN activation." [GOC:bhm, PMID:16449187]
+synonym: "Bfa1-Bub2 complex" NARROW []
+synonym: "Byr4-Cdc16 GAP complex" NARROW []
 is_a: GO:1902773 ! GTPase activator complex
 relationship: part_of GO:0005816 ! spindle pole body
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31636" xsd:anyURI
 created_by: bhm
 creation_date: 2014-03-17T14:34:21Z
 

```

## Agent Attempts (11)

| # | Model | Runtime | F1 | P | R | Eval PR | Detail |
|---|-------|---------|-----|-----|-----|---------|--------|
| 1 | claude-sonnet-4.5 | claude | 0.857 | 0.857 | 0.857 | [#457](https://github.com/ai4curation/eval-ont-agent-go/pull/457) | [attempt](attempts/pr457.md) |
| 2 | claude-sonnet-4.5 | copilot | 0.857 | 0.857 | 0.857 | [#416](https://github.com/ai4curation/eval-ont-agent-go/pull/416) | [attempt](attempts/pr416.md) |
| 3 | claude-sonnet-4.5 | copilot | 0.857 | 0.857 | 0.857 | [#370](https://github.com/ai4curation/eval-ont-agent-go/pull/370) | [attempt](attempts/pr370.md) |
| 4 | claude-opus-4.7 | claude | 0.857 | 0.857 | 0.857 | [#329](https://github.com/ai4curation/eval-ont-agent-go/pull/329) | [attempt](attempts/pr329.md) |
| 5 | gemma-4-31b | opencode | 0.857 | 0.857 | 0.857 | [#249](https://github.com/ai4curation/eval-ont-agent-go/pull/249) | [attempt](attempts/pr249.md) |
| 6 | gpt-5.4 | codex | 0.857 | 0.857 | 0.857 | [#172](https://github.com/ai4curation/eval-ont-agent-go/pull/172) | [attempt](attempts/pr172.md) |
| 7 | gpt-5.5 | codex | 0.857 | 0.857 | 0.857 | [#60](https://github.com/ai4curation/eval-ont-agent-go/pull/60) | [attempt](attempts/pr60.md) |
| 8 | kimi-k2.6 | opencode | 0.833 | 0.714 | 1.000 | [#264](https://github.com/ai4curation/eval-ont-agent-go/pull/264) | [attempt](attempts/pr264.md) |
| 9 | claude-haiku-4.5 | claude | 0.727 | 0.571 | 1.000 | [#193](https://github.com/ai4curation/eval-ont-agent-go/pull/193) | [attempt](attempts/pr193.md) |
| 10 | gpt-5.5 | opencode | 0.667 | 0.714 | 0.625 | [#94](https://github.com/ai4curation/eval-ont-agent-go/pull/94) | [attempt](attempts/pr94.md) |
| 11 | gpt-5.5 | opencode | 0.667 | 0.714 | 0.625 | [#76](https://github.com/ai4curation/eval-ont-agent-go/pull/76) | [attempt](attempts/pr76.md) |
