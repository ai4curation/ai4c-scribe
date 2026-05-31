---
ontology: cell-ontology
issue_number: 3453
pr_number: 3556
eval_repo_pr: 301
agent: std_codex_gpt54
model: gpt-5.4
runtime: codex
agent_config_tag: v3
case_type: new_term
difficulty: medium
f1: 0.125
precision: 0.125
recall: 0.125
jaccard: 0.067
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
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-cl/pull/301
  Agent config: ai4curation/cl-agent-config
-->

## Summary

This run (gpt-5.4 / codex, blob `02ec74a`) has correct biological content and, unlike the gpt-5.4 opencode runs, does incorporate `CL_0011025` (exhausted T cell) — but inside the `EquivalentClasses` intersection rather than as gold's separate `SubClassOf` parent. It still allocates the wrong CL IDs (`CL_9900001`/`CL_9900002` vs gold `CL_9900000`/`CL_9900001`), which dominates the F1=0.125 score. The metadiff under-represents conceptual correctness, but the off-by-one IDs and the non-gold equivalence pattern would require curator cleanup before merge. Not a poor case; gold #3556 is a clean single-PR reference (METADATA `case_quality: ok`).

## Strengths

- Both requested terms created with correct labels and definitions matching the issue text (including @scheuerm's "as a result of" wording, explicitly noted in the PR comment, and the CD4/CD8 transcription-factor distinctions).
- Correct PD-1 marker `PR_000001919` via `RO_0002104` (`has_plasma_membrane_part`), matching gold's protein.
- Correct lineage parents `CL_0000624` / `CL_0000625` (asserted `SubClassOf`).
- Recognized the dual lineage/state intent: `EquivalentClasses(CL_9900001 ObjectIntersectionOf(CL_0000624 CL_0011025 has-PD-1))` keeps the exhausted-T-cell concept in the logic, addressing what #526/#588 dropped (though via a different mechanism than gold).
- Full metadata: `IAO_0000233` to issue #3453 (IRI form, matching gold), both ORCID contributors, `terms:creator`, `terms:date`, 3 exact synonyms per term.
- Avoided the PMID:35880649 red herring; PR comment honestly reports that `aurelian` and `robot` were unavailable so PMID/parse validation could not be run.

## Issues

- **Wrong ID allocation (dominant scoring driver):** `CL_9900001`/`CL_9900002` instead of gold `CL_9900000`/`CL_9900001`; off-by-one propagates into every axiom line — the principal cause of F1=0.125.
- **Pattern divergence:** gold uses `EquivalentClasses(ObjectIntersectionOf(lineage-parent, has-PD-1))` (PD-1 the only differentia) + an `is_inferred "true"` SubClassOf to the lineage parent + a separate `SubClassOf CL_0011025`. This attempt instead folds `CL_0011025` *into* the equivalence intersection and adds only the lineage `SubClassOf`, with no explicit exhausted-T-cell parent axiom. Including `CL_0011025` as an equivalence conjunct over-constrains the defined class relative to both gold and the issue (PD-1 is the stated shared required marker).
- **Convention drift:** the three exact synonyms are PMID-annotated where gold leaves them bare; defensible but adds metadiff distance.
</content>
