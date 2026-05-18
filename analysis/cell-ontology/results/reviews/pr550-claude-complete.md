---
ontology: cell-ontology
issue_number: 3453
pr_number: 3556
eval_repo_pr: 550
agent: std_opencode_gpt55
model: gpt-5.5
runtime: opencode
agent_config_tag: v3
case_type: new_term
difficulty: medium
f1: 0.120
precision: 0.125
recall: 0.115
jaccard: 0.064
outcome: partial_success
failure_modes:
  - wrong_term
  - wrong_pattern
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-17
---

<!-- Review this eval run following .claude/skills/review-agent-pr/SKILL.md

  Source issue: https://github.com/obophenotype/cell-ontology/issues/3453
  Human PR (ground truth): https://github.com/obophenotype/cell-ontology/pull/3556
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-cl/pull/550
  Agent config: ai4curation/cl-agent-config
-->

## Summary

This run (gpt-5.5 / opencode) produces an ontology diff byte-identical to eval PR #489 (same blob `252ee7f`, same `2026-05-17T00:02:24Z` timestamp), and the same assessment applies. It is the strongest of the gpt-5.x opencode/codex attempts on substance: it reproduces gold's dual placement — lineage parent (`CL_0000624`/`CL_0000625`) **and** `CL_0011025` exhausted T cell — which the gpt-5.4 opencode runs dropped, with the correct PD-1 marker and definitions. It still uses the wrong CL IDs (`CL_9900001`/`CL_9900002` vs gold `CL_9900000`/`CL_9900001`) and asserted `SubClassOf` axioms rather than gold's `EquivalentClasses` defined class. F1=0.120 badly under-represents quality; substantively this (with #489) is the closest of the five to gold. Not a poor case; gold #3556 is a clean single-PR reference (METADATA `case_quality: ok`). The PR comment additionally documents a successful `robot convert` parse check.

## Strengths

- **Correct dual placement:** `SubClassOf` to the lineage parent *and* `SubClassOf CL_0011025` (exhausted T cell), matching gold's structure and honoring curator Caroline-99's explicitly added exhausted-T-cell link — the requirement #526/#588 missed.
- Correct PD-1 marker `PR_000001919` via `RO_0002104` (`has_plasma_membrane_part`), matching gold's protein.
- Correct lineage parents `CL_0000624` / `CL_0000625`.
- Definitions match the issue text (minor "for example in..." paraphrase of gold's "(e.g., ...)"), including @scheuerm's "as a result of" wording; PR comment explicitly notes the curator's wording change and the PMID:35880649 exclusion.
- Full metadata: term_tracker to issue #3453, both ORCID contributors, `terms:creator`, `terms:date`, 3 exact synonyms per term.
- Methodology transparent: PR comment reports a successful `robot convert -i src/ontology/cl-edit.owl` parse validation and a conservative-marker rationale (PD-1 asserted, other markers left in text).

## Issues

- **Wrong ID allocation (dominant scoring driver):** `CL_9900001`/`CL_9900002` instead of gold `CL_9900000`/`CL_9900001`; off-by-one propagates into every axiom line — the main cause of the ~0.12 F1.
- **Pattern divergence:** three plain asserted `SubClassOf` axioms (lineage parent + `CL_0011025` + PD-1 restriction) instead of gold's `EquivalentClasses(ObjectIntersectionOf(lineage-parent, has-PD-1))` defined class plus `is_inferred "true"` lineage SubClassOf. Conservative but lacks gold's defined-class equivalence.
- **Convention drift / serialization:** `IAO_0000233` value serialized as a quoted string literal rather than gold's IRI form; CD8 exact synonyms carry two PMID xref annotations each (gold leaves synonyms bare), lowering recall slightly below #526 (F1 0.120 vs 0.125).
</content>
