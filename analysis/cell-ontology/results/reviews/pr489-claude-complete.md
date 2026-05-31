---
ontology: cell-ontology
issue_number: 3453
pr_number: 3556
eval_repo_pr: 489
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
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-cl/pull/489
  Agent config: ai4curation/cl-agent-config
-->

## Summary

This run (gpt-5.5 / opencode, blob `252ee7f`) is the strongest of the gpt-5.x opencode/codex attempts on biological substance: it reproduces gold's dual placement — both the lineage parent (`CL_0000624`/`CL_0000625`) **and** the `CL_0011025` exhausted-T-cell parent — which the gpt-5.4 opencode runs (#526/#588) dropped. It still allocates the wrong CL IDs (`CL_9900001`/`CL_9900002` vs gold `CL_9900000`/`CL_9900001`) and uses asserted `SubClassOf` axioms instead of gold's `EquivalentClasses` defined class. F1=0.120 (marginally below #526's 0.125, driven by extra PMID xrefs on the CD8 synonyms lowering recall) badly under-represents the actual quality — substantively this is the closest of the five to gold. Not a poor case; gold #3556 is a clean single-PR reference (METADATA `case_quality: ok`).

## Strengths

- **Correct dual placement:** both terms get `SubClassOf` to the lineage parent *and* `SubClassOf CL_0011025` (exhausted T cell), matching gold's structure and honoring curator Caroline-99's explicitly added exhausted-T-cell link. This is the key thing #526/#588 missed.
- Correct PD-1 marker `PR_000001919` via `RO_0002104` (`has_plasma_membrane_part`), matching gold's protein.
- Correct lineage parents `CL_0000624` / `CL_0000625`.
- Definitions match the issue text (with a minor punctuation paraphrase: "for example in chronic infection..." vs gold's "(e.g., chronic infection...)"), including @scheuerm's "as a result of" wording.
- Full metadata: term_tracker to issue #3453, both ORCID contributors, `terms:creator`, `terms:date`, 3 exact synonyms per term.
- Avoided the PMID:35880649 red herring.

## Issues

- **Wrong ID allocation (dominant scoring driver):** `CL_9900001`/`CL_9900002` instead of gold `CL_9900000`/`CL_9900001`; off-by-one propagates into every axiom line, the main cause of the ~0.12 F1.
- **Pattern divergence:** three plain asserted `SubClassOf` axioms (lineage parent + `CL_0011025` + PD-1 restriction) rather than gold's `EquivalentClasses(ObjectIntersectionOf(lineage-parent, has-PD-1))` defined class plus `is_inferred "true"` lineage SubClassOf. Semantically the asserted form lacks gold's defined-class equivalence, though it is arguably the more conservative modeling choice.
- **Convention drift / serialization:** `IAO_0000233` value is a quoted string literal (`"https://github.com/...issues/3453"`) rather than gold's IRI form (`<https://...>`); the CD8 synonyms carry two PMID xref annotations each (vs gold's bare synonyms), which lowers recall slightly below #526 (F1 0.120 vs 0.125).
</content>
