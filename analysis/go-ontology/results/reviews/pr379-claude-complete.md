---
ontology: go-ontology
issue_number: 31916
pr_number: 32024
eval_repo_pr: 379
agent: std_copilot_son45
model: claude-sonnet-4.5
runtime: copilot
agent_config_tag: v9
case_type: obsoletion
difficulty: medium
f1: 0.852
precision: 0.860
recall: 0.845
jaccard: 0.742
outcome: partial_success
failure_modes:
  - wrong_pattern
  - missed_requirement
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

<!-- Review this eval run following analysis/instructions/review-agent-eval.md

  Source issue: https://github.com/geneontology/go-ontology/issues/31916
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/32024
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/379
  Agent config: ai4curation/go-ontology-agent-config
-->

## Summary

The agent obsoleted all five terms with the correct replacement targets, so the central obsoletion task of issue #31916 was achieved. But the execution has two real defects: the new MetaCyc mappings on `GO:0061678` use the wrong xref qualifier syntax, and obsolete-term synonyms were left in place on two terms (`GO:0061679`, `GO:0061688`). `F1=0.852` — the lowest of the non-codex attempts — fairly captures a result that is directionally correct but the most procedurally sloppy of the set.

## Strengths

- Obsoleted all four ED variant terms (`GO:0009255`, `GO:0061679`, `GO:0061680`, `GO:0061681`) with `replaced_by: GO:0061678`, and `GO:0061688` with `replaced_by: GO:0006096` — correct targets matching the human PR and the issue directive.
- Applied the core obsoletion mechanics: `obsolete ` name prefix, `OBSOLETE.` def prefix, `is_obsolete: true`, removal of `is_a`/`intersection_of`/`relationship` logical axioms, and a `term_tracker_item` for #31916 on each obsoleted term.
- Preserved `created_by`/`creation_date` on all obsoleted terms.
- Removed the grouping-class xref `MetaCyc:Entner-Doudoroff-Pathways` from `GO:0061678` and added the four requested variant pathway IDs, satisfying the issue's mapping request at the content level.
- PR documentation is thorough (per-term annotation-impact notes, rationale tied to #29539, checklist).

## Issues

- **Wrong mapping pattern (failure_mode: wrong_pattern):** the four new xrefs on `GO:0061678` are written as `xref: MetaCyc:PWY-8004 {skos:narrowMatch="MetaCyc:PWY-8004"}` etc. The GO-standard form used by the human PR and ~4600 existing xrefs in `go-edit.obo` is `{source="skos:narrowMatch"}`; the `{skos:narrowMatch="..."}` form is never used in the ontology and does not correctly encode the intended SKOS mapping.
- **Incomplete obsoletion (failure_mode: missed_requirement):** the `synonym: "gluconate pathway" RELATED []` line was retained on the obsoleted `GO:0061679` and on the obsoleted `GO:0061688`. Obsoletion should strip synonyms (the human PR removed them); leaving them risks the obsolete labels surfacing in synonym-based search and is a `synonym-label`/QC concern.
- Omission (minor): the pre-existing `property_value: term_tracker_item ".../issues/28392"` on `GO:0061680` was dropped; the human PR retained it.
- Style: `replaced_by: GO:0061678 ! Entner-Doudoroff pathway` includes a trailing `! label` comment where the human PR used the bare `replaced_by: GO:0061678`. Also the `is_obsolete`/`replaced_by`/`property_value` lines are ordered differently from convention. These are non-breaking but contribute to the lower metadiff and reflect less disciplined editing than the higher-scoring attempts.
