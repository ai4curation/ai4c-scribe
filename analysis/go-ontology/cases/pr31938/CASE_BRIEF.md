---
ontology: go-ontology
repo: geneontology/go-ontology
issue_number: 31923
pr_number: 31938
issue_title: 'Textual definition update: GO:0045022 early endosome to late endosome
  transport (minor)'
pr_author: dragon-ai-agent
pr_merged_at: '2026-04-21'
task_type: other
difficulty: simple
scoping: tightly_scoped
scope: single_term
review_outcome: approved_first_time
num_agent_attempts: 11
generated_at: '2026-05-15'
best_f1: 1.0
best_model: claude-sonnet-4.5
---

# PR #31938 — Textual definition update: GO:0045022 early endosome to late endosome transport (minor)

**go-ontology** | [geneontology/go-ontology](https://github.com/geneontology/go-ontology) | [Issue #31923](https://github.com/geneontology/go-ontology/issues/31923) | [PR #31938](https://github.com/geneontology/go-ontology/pull/31938) | @dragon-ai-agent | merged 2026-04-21

`other` `simple` `tightly_scoped` `approved_first_time`

## Context

The definition of GO:0045022 `early endosome to late endosome transport` stated that "transport occurs along microtubules and can be experimentally blocked with microtubule-depolymerizing drugs." While this is true in many mammalian cell types, it is not universally the case across all organisms, making the definition too restrictive for a species-neutral ontology term. ValWood flagged this as a minor textual definition update.

## Changes Made

The definition was updated in `go-edit.obo` to remove the microtubule-specific mechanistic detail. The revised definition retains the core description of directed movement of substances in membrane-bounded vesicles from early sorting endosomes to late sorting endosomes, without asserting a specific cytoskeletal mechanism. This makes the term applicable across organisms regardless of their endosomal transport mechanisms.

## Resolution

Easy difficulty because the change was a straightforward text edit removing an overly specific claim. The biological rationale was clear: not all endosome-to-endosome transport is microtubule-dependent (e.g., in organisms with different cytoskeletal organization), so the definition should describe the transport event without mandating a specific mechanism. The 2-commit history suggests a minor formatting correction after the initial edit.

## Human Diff

```diff
diff --git a/src/ontology/go-edit.obo b/src/ontology/go-edit.obo
index d657bb9e5..f2d6aa9bf 100644
--- a/src/ontology/go-edit.obo
+++ b/src/ontology/go-edit.obo
@@ -268909,13 +268909,14 @@ consider: GO:0070987
 id: GO:0045022
 name: early endosome to late endosome transport
 namespace: biological_process
-def: "The directed movement of substances, in membrane-bounded vesicles, from the early sorting endosomes to the late sorting endosomes; transport occurs along microtubules and can be experimentally blocked with microtubule-depolymerizing drugs." [ISBN:0815316194, PMID:29980602]
+def: "The directed movement of substances, in membrane-bounded vesicles, from the early sorting endosomes to the late sorting endosomes." [ISBN:0815316194, PMID:29980602]
 synonym: "endosome maturation" RELATED [PMID:21878991, PMID:29980602]
 intersection_of: GO:0016192 ! vesicle-mediated transport
 intersection_of: has_target_end_location GO:0005770 ! late endosome
 intersection_of: has_target_start_location GO:0005769 ! early endosome
 intersection_of: occurs_in GO:0005737 ! cytoplasm
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/26386" xsd:anyURI
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31923" xsd:anyURI
 
 [Term]
 id: GO:0045023

```

## Agent Attempts (11)

| # | Model | Runtime | F1 | P | R | Blob | Eval PR | Detail |
|---|-------|---------|-----|-----|-----|------|---------|--------|
| 1 | claude-sonnet-4.5 | copilot | 1.000 | 1.000 | 1.000 | `f2d6aa9` | [#414](https://github.com/ai4curation/eval-ont-agent-go/pull/414) | [attempt](attempts/pr414.md) |
| 2 | claude-sonnet-4.5 | copilot | 1.000 | 1.000 | 1.000 | `f2d6aa9` | [#373](https://github.com/ai4curation/eval-ont-agent-go/pull/373) | [attempt](attempts/pr373.md) |
| 3 | kimi-k2.6 | opencode | 1.000 | 1.000 | 1.000 | `f2d6aa9` | [#268](https://github.com/ai4curation/eval-ont-agent-go/pull/268) | [attempt](attempts/pr268.md) |
| 4 | gpt-5.5 | opencode | 1.000 | 1.000 | 1.000 | `f2d6aa9` | [#108](https://github.com/ai4curation/eval-ont-agent-go/pull/108) | [attempt](attempts/pr108.md) |
| 5 | gpt-5.5 | opencode | 1.000 | 1.000 | 1.000 | `f2d6aa9` | [#90](https://github.com/ai4curation/eval-ont-agent-go/pull/90) | [attempt](attempts/pr90.md) |
| 6 | claude-sonnet-4.5 | claude | 0.857 | 1.000 | 0.750 | `e9f0f16` | [#455](https://github.com/ai4curation/eval-ont-agent-go/pull/455) | [attempt](attempts/pr455.md) |
| 7 | claude-opus-4.7 | claude | 0.800 | 0.667 | 1.000 | `306c812` | [#339](https://github.com/ai4curation/eval-ont-agent-go/pull/339) | [attempt](attempts/pr339.md) |
| 8 | gemma-4-31b | opencode | 0.800 | 0.667 | 1.000 | `306c812` | [#240](https://github.com/ai4curation/eval-ont-agent-go/pull/240) | [attempt](attempts/pr240.md) |
| 9 | claude-haiku-4.5 | claude | 0.800 | 0.667 | 1.000 | `306c812` | [#203](https://github.com/ai4curation/eval-ont-agent-go/pull/203) | [attempt](attempts/pr203.md) |
| 10 | gpt-5.4 | codex | 0.800 | 0.667 | 1.000 | `306c812` | [#181](https://github.com/ai4curation/eval-ont-agent-go/pull/181) | [attempt](attempts/pr181.md) |
| 11 | gpt-5.5 | codex | 0.667 | 0.667 | 0.667 | `b76a791` | [#72](https://github.com/ai4curation/eval-ont-agent-go/pull/72) | [attempt](attempts/pr72.md) |
