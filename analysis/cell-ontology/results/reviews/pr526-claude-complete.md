---
ontology: cell-ontology
issue_number: 3453
pr_number: 3556
eval_repo_pr: 526
agent: std_opencode_gpt54
model: gpt-5.4
runtime: opencode
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
  - missed_requirement
  - wrong_pattern
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-17
---

<!-- Review this eval run following .claude/skills/review-agent-pr/SKILL.md

  Source issue: https://github.com/obophenotype/cell-ontology/issues/3453
  Human PR (ground truth): https://github.com/obophenotype/cell-ontology/pull/3556
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-cl/pull/526
  Agent config: ai4curation/cl-agent-config
-->

## Summary

The agent (gpt-5.4 / opencode) added both requested terms with correct labels, definitions, synonyms, PMIDs, ORCID contributors and lineage placement, but allocated the wrong CL IDs (`CL_9900001`/`CL_9900002` instead of gold's `CL_9900000`/`CL_9900001`) and deliberately omitted the `CL_0011025` (exhausted T cell) parent that the issue's curator (Caroline-99) explicitly added. F1=0.125 substantially under-represents biological correctness — the content is largely right — but it does not over-represent it either: the off-by-one IDs propagate into every axiom line and the missing exhausted-T-cell link is a genuine requirement gap, so the patch would need real cleanup, not just renumbering. This is not a poor evaluation case; gold #3556 is a clean single-PR reference and the low score reflects the skill's expected metadiff sensitivity to ID allocation and convention drift (already recorded as `case_quality: ok` in METADATA).

## Strengths

- Both terms created with the requested labels (`CD4-positive exhausted alpha-beta T cell`, `CD8-positive exhausted alpha-beta T cell`).
- Definitions match the issue text including @scheuerm's "as a result of chronic antigenic stimulation" wording and the CD4/CD8 distinction (T-bet variability vs reduced T-bet / EOMES).
- Correct marker protein `PR_000001919` (PD-1 / PDCD1) via `RO_0002104` (`has_plasma_membrane_part`), matching gold's protein choice.
- Correct lineage parents `CL_0000624` (CD4+ alpha-beta T cell) and `CL_0000625` (CD8+ alpha-beta T cell).
- All metadata present: `IAO_0000233` term_tracker to issue #3453 (in IRI form, matching gold), both ORCID contributors, `terms:creator "GitHub Copilot"`, `terms:date`, 3 exact synonyms per term.
- Correctly avoided the PMID:35880649 red herring flagged by the curator (it never appears in the diff).

## Issues

- **Wrong ID allocation (dominant scoring driver):** uses `CL_9900001`/`CL_9900002` vs gold `CL_9900000`/`CL_9900001`. In CL functional-syntax OWL the ID appears on every declaration, annotation and axiom line, so the off-by-one shifts essentially every line of the new block — this is the primary cause of F1=0.125, not a harmless metadata mismatch.
- **Missed requirement:** omits the `SubClassOf(CL_9900001 CL_0011025)` / `SubClassOf(CL_9900002 CL_0011025)` exhausted-T-cell parent. Gold places both terms under the lineage parent *and* `CL_0011025`, following Caroline-99's explicit comment ("I have added a SubclassOF 'exhausted T cell' as I believe we should still link it to this term"). The agent's PR comment argues the opposite — that `CL_0011025` should not be used — which contradicts the curator's recorded decision in the issue thread. This is a genuine omission, not just style.
- **Pattern divergence:** gold defines each term with `EquivalentClasses(... ObjectIntersectionOf(lineage-parent, has-PD-1))` plus an `is_inferred "true"` SubClassOf to the lineage parent; this attempt uses two plain asserted `SubClassOf` axioms (lineage parent + PD-1 restriction) with no defined class.
- **Convention drift:** the three exact synonyms are each PMID-annotated (`Annotation(oboInOwl:hasDbXref "PMID:31390978") ...`) whereas gold leaves them unannotated; defensible but adds further metadiff distance.
</content>
</invoke>
