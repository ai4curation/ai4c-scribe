---
repo: obophenotype/uberon
issue_number: 3490
pr_number: 3585
issue_title: "consider allowing some whole cells in a 'multi cell part structure'"
issue_labels:
  - textual definition
issue_created_at: "2025-03-14"
issue_closed_at: "2025-07-14"
pr_author: gouttegd
pr_merged_at: "2025-07-14"
pr_num_commits: 1
files_changed:
  - path: src/ontology/uberon-edit.obo
    additions: 2
    deletions: 1
scoping: tightly_scoped
task_type: axiom_repair
difficulty: hard
scope: single_term
review_outcome: approved_first_time
domain_area: neuroanatomy
tags:
  - definition-update
  - multi-cell-part-structure
  - gray-matter
  - white-matter
curated_by: claude-opus-4
curated_at: "2026-05-08"
rationale: Subtle definition change requiring deep understanding of how textual definitions constrain classification of nervous system structures
case_quality: ok
case_quality_reason: metadiff_tiny_freetext_def_ceiling
scoring_caveat: "Gold PR #3585 is the complete, single-PR human resolution of issue #3490 (verified: no companion PRs). But the gold diff is only 3 lines of free-text def/comment, so metadiff F1 is structurally capped near 0.40 even for semantically perfect, scope-clean resolutions. Gold's wording derives from FBbt issue #2008's canonical proposal ('A structure mainly consisting of cell components, rather than complete cells.' / 'May contain complete cells in addition to partial ones.'); attempts #135/#295/#249/#33 reproduced that canonical FBbt wording almost verbatim and are conceptually as correct as gold, yet are penalized on def word-order ('mainly consisting' vs gold 'consisting mainly') and comment phrasing. Judge on substance: scores under-represent quality for scope-clean attempts; scope creep (extra term_tracker_item / created_by / external_ontology_notes / CARO-xref deletion) is the real differentiator, not the def text."
quality_flagged_by: claude-opus-4.7
quality_flagged_at: "2026-05-16"
---

## Context

The term "multi cell part structure" (UBERON:0005162) had a definition that excluded any structure containing whole cells. However, structures like gray matter and white matter, which are classified under this term, do contain some whole cells (e.g., neuronal cell bodies in gray matter). The overly restrictive definition was inconsistent with biological reality.

## Changes Made

Broadened the textual definition of UBERON:0005162 to allow for the presence of some complete cells within a multi cell part structure, while maintaining the core concept that such structures are primarily composed of cell parts (e.g., axons, dendrites). A minimal 2-line addition, 1-line deletion.

## Resolution

Hard difficulty despite the small diff because this involves careful reasoning about how a definition change affects the semantics of an upper-level term. The agent must understand that gray matter contains neuronal cell bodies (whole cells) alongside axons and synapses (cell parts), and that the definition must accommodate this biological reality without making the term too broad. Four months elapsed between issue filing and resolution, indicating significant deliberation.

## Curation Note (data quality)

Reviewed by claude-opus-4.7 on 2026-05-16 (all 9 attempts).

This is a **valid, well-formed reference case** (`case_quality: ok`), not a poor case: gold PR #3585 is the complete single-PR human resolution of issue #3490 — `gh search prs` confirms no companion PRs, there is no base-state contamination of the issue-relevant hunk, no metadiff-ignored gold field, no curator repudiation, and no out-of-scope gold extra. The issue body is the explicit ask and gold matches it.

However, scoring must be interpreted with care:

- The gold diff is **3 lines** (1 deletion + 2 additions) of pure free text: a reworded `def:` plus a new `comment:`, `[CARO:0001000]` retained. With OBO metadiff treating the def line atomically, F1 is **structurally capped near 0.40** for even a semantically perfect, scope-clean resolution. The observed best F1 is exactly 0.40.
- Gold's wording is adapted from the upstream **FBbt issue #2008** canonical proposal: def "A structure mainly consisting of cell components, rather than complete cells." and comment "May contain complete cells in addition to partial ones." Gold reordered to "consisting mainly" and expanded the comment with a glia example.
- Attempts **#135 (gemma), #295 (sonnet), #249 (opus), #33 (gpt-5.5 codex)** reproduced the FBbt canonical wording almost verbatim — conceptually **as correct as gold**, since gold itself derives from the same source — yet metadiff penalizes them for word order and comment phrasing. F1 here **under-represents quality** for scope-clean attempts.
- The genuine quality differentiator across attempts is **scope discipline**, not the definition text:
  - Cleanest: #169/#98 (haiku, single line, CARO xref kept) and #249 (opus, one extra `term_tracker_item`, strongest methodology — surveyed actual children UBERON:0012337/0018687/6040007/0012453).
  - Mild scope creep (defensible `term_tracker_item`): #68/#51 (gpt-5.5 opencode), #295 (sonnet, also added `dcterms-date` + `created_by: dragon-ai-agent`).
  - Real over-reach: #81 (gpt-5.4 codex) rewrote the `external_ontology_notes` curator-rationale free text; #33 (gpt-5.5 codex) **deleted `xref: CARO:0001000`** and swapped the def source bracket to the issue URL on a speculative equivalence-mapping argument — both unrequested and contrary to gold, which deliberately kept the CARO xref.
  - Syntax defects: #135 dropped `[CARO:0001000]` from the def and double-quoted the `comment:` value (non-standard OBO).

Net: all attempts identified the correct target term and the correct semantic change; outcomes range success → partial_success. No failures, no no_output. Downstream aggregation should treat the compressed F1 spread (0.20–0.40) as dominated by tiny-free-text metadiff geometry plus scope-creep penalties, not by correctness differences in the core definition edit.
