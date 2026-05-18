---
ontology: uberon
repo: obophenotype/uberon
issue_number: 3464
pr_number: 3646
issue_title: Positioning 'life cycle' and 'life cycle stage' under 'process'
pr_author: matentzn
pr_merged_at: '2026-01-12'
task_type: reclassification
difficulty: hard
scoping: tightly_scoped
scope: multi_term
review_outcome: approved_first_time
num_agent_attempts: 8
generated_at: '2026-05-17'
domain_area: upper-ontology
best_f1: 0.0
best_model: gpt-5.4
---

# PR #3646 — Positioning 'life cycle' and 'life cycle stage' under 'process'

**uberon** | [obophenotype/uberon](https://github.com/obophenotype/uberon) | [Issue #3464](https://github.com/obophenotype/uberon/issues/3464) | [PR #3646](https://github.com/obophenotype/uberon/pull/3646) | @matentzn | merged 2026-01-12

`reclassification` `hard` `tightly_scoped` `approved_first_time`

## Context

As part of aligning Uberon with the Core Ontology for Biology (COB), "life cycle stage" and "life cycle temporary boundary" needed to be repositioned as root classes. This was an intermediate step before deprecating the "processual entity" class in a subsequent PR. The issue was open for nearly a year, indicating significant deliberation about the structural change.

## Changes Made

Added two lines to uberon-edit.obo to establish life cycle stage and life cycle temporary boundary as top-level classes. This minimal change has significant structural implications because it sets up the subsequent deprecation of processual entity.

## Resolution

Hard difficulty because changes to root-level ontology structure have cascading effects on the entire class hierarchy. The agent must understand the COB alignment strategy, know that these classes will become true roots once processual entity is deprecated, and ensure the change does not break existing reasoning. Despite the tiny diff, this required a year of discussion.

## Curation Note (data quality)

**Flagged poor: `gold_pr_is_partial`.** This is a multi-PR human resolution and the
selected gold PR is only a deliberate sub-step, so every agent scores F1=0 by
construction regardless of correctness.

Issue #3464 asks to reposition `life cycle` (UBERON:0000104) and `life cycle stage`
(UBERON:0000105) from `processual entity` (UBERON:0000000) to `process`
(`BFO:0000015`) for COB compatibility; the comment thread additionally raises
obsoleting the 4 vestigial "life cycle temporal boundary" terms
(UBERON:0035943/0035944/0035945/0035946).

The human resolved this across **three** PRs:

- **#3532** (2025-05): added the COB-alignment `comment:` and `seeAlso` COB#51 to
  UBERON:0000000 (groundwork).
- **#3646** (gold, 2026-01-12): adds only two header lines —
  `has_ontology_root_term UBERON:0000105` and `... UBERON:0035943`. The PR body
  states verbatim: *"This is an intermediate step... I am breaking the task down...
  in the next PR, I am getting rid of processual entity, which will make it so."*
  It shares **zero substantive lines** with the issue's actual ask.
- **#3647** (2026-01-23): the real work — obsoletes UBERON:0000000
  ("obsolete processual entity", `is_obsolete: true`), reparents UBERON:0000104 and
  UBERON:0000105 to `is_a: BFO:0000015 ! process`, and moves
  `life cycle temporal boundary` (UBERON:0035943) to `is_a: BFO:0000001 ! entity`.

Consequently the metadiff vs #3646 is meaningless for this issue. Judged against
the issue and the union #3532+#3646+#3647:

- **pr177 (haiku-4.5)** — best attempt; its 2 hunks reparenting UBERON:0000104/0000105
  to `BFO:0000015 ! process` are byte-identical to the corresponding hunks in
  human PR #3647. Graded `success`.
- **pr303 (sonnet-4.5)** — valid alternative mechanism: renames UBERON:0000000 in
  place to "process" with `BFO:0000015` xref + retained synonym; achieves COB
  alignment, differs from the human's obsolete-and-reparent approach. `partial_success`.
- **pr263 (opus-4.7)** — obsoletes the 4 vestigial temporal-boundary terms with good
  obsoletion hygiene and explicit scope rationale; responsive to the issue
  discussion but skips the title's primary reparenting ask. `partial_success`.

Flagged by claude-opus-4.7 on 2026-05-16.

## Human Diff

```diff
diff --git a/src/ontology/uberon-edit.obo b/src/ontology/uberon-edit.obo
index 0239d1945..878789bf4 100644
--- a/src/ontology/uberon-edit.obo
+++ b/src/ontology/uberon-edit.obo
@@ -185,7 +185,9 @@ property_value: doap-mailing-list "https://lists.sourceforge.net/lists/listinfo/
 property_value: doap-SVNRepository "https://obo.svn.sourceforge.net/svnroot/obo/uberon/" xsd:anyURI
 property_value: foaf-homepage "http://uberon.org" xsd:anyURI
 property_value: has_ontology_root_term UBERON:0000104
+property_value: has_ontology_root_term UBERON:0000105
 property_value: has_ontology_root_term UBERON:0001062
+property_value: has_ontology_root_term UBERON:0035943
 treat-xrefs-as-has-subclass: EHDAA
 treat-xrefs-as-has-subclass: EV
 treat-xrefs-as-has-subclass: NCIT

```

## Agent Attempts (8)

| # | Model | Runtime | F1 | P | R | Blob | Eval PR | Detail |
|---|-------|---------|-----|-----|-----|------|---------|--------|
| 1 | gpt-5.4 | opencode | 0.000 | 0.000 | 0.000 | `bcb5fd4` | [#677](https://github.com/ai4curation/eval-ont-agent-uberon/pull/677) | [attempt](attempts/pr677.md) |
| 2 | gpt-5.5 | opencode | 0.000 | 0.000 | 0.000 | `4f7bca3` | [#641](https://github.com/ai4curation/eval-ont-agent-uberon/pull/641) | [attempt](attempts/pr641.md) |
| 3 | gpt-5.4 | codex | 0.000 | 0.000 | 0.000 | `4fc8ac1` | [#625](https://github.com/ai4curation/eval-ont-agent-uberon/pull/625) | [attempt](attempts/pr625.md) |
| 4 | gpt-5.4 | opencode | 0.000 | 0.000 | 0.000 | `bcb5fd4` | [#617](https://github.com/ai4curation/eval-ont-agent-uberon/pull/617) | [attempt](attempts/pr617.md) |
| 5 | gpt-5.5 | opencode | 0.000 | 0.000 | 0.000 | `4f7bca3` | [#583](https://github.com/ai4curation/eval-ont-agent-uberon/pull/583) | [attempt](attempts/pr583.md) |
| 6 | claude-sonnet-4.5 | claude | 0.000 | 0.000 | 0.000 | `0b80776` | [#303](https://github.com/ai4curation/eval-ont-agent-uberon/pull/303) | [attempt](attempts/pr303.md) |
| 7 | claude-opus-4.7 | claude | 0.000 | 0.000 | 0.000 | `b0f5f2c` | [#263](https://github.com/ai4curation/eval-ont-agent-uberon/pull/263) | [attempt](attempts/pr263.md) |
| 8 | claude-haiku-4.5 | claude | 0.000 | 0.000 | 0.000 | `bcb5fd4` | [#177](https://github.com/ai4curation/eval-ont-agent-uberon/pull/177) | [attempt](attempts/pr177.md) |
