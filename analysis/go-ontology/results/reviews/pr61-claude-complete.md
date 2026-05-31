---
ontology: go-ontology
issue_number: 31945
pr_number: 32013
eval_repo_pr: 61
agent: std_codex_g55
model: gpt-5.5
runtime: codex
agent_config_tag: v9
case_type: reclassification
difficulty: medium
f1: 0.826
precision: 0.95
recall: 0.731
jaccard: 0.704
outcome: partial_success
failure_modes:
  - over_editing
  - scope_creep
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

<!-- Review this eval run following analysis/instructions/review-agent-eval.md

  Source issue: https://github.com/geneontology/go-ontology/issues/31945
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/32013
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/61
  Agent config: ai4curation/go-ontology-agent-config

  Quick reference:
    gh issue view 31945 --repo geneontology/go-ontology
    gh pr diff 32013 --repo geneontology/go-ontology
    gh pr diff 61 --repo ai4curation/eval-ont-agent-go
-->

## Summary

The `go-edit.obo` portion of this run is among the most complete in the cohort — it is the only attempt besides pr344 to refresh **all** the stale `! vesicle coating` inline comments (incoming `is_a` edges from `GO:0016183`, `GO:0048200`, and the `GO:0048208` self-edge). However, the agent also hand-edited four **build-generated** files: `src/design_patterns/cc_assembly.tsv`, `regulation.tsv`, `regulation_by.tsv`, `docs/patterns/cc_assembly.md`, and `src/ontology/ld.txt`. These are derived artifacts regenerated from `go-edit.obo` by `make` (the merged repo confirms they were auto-updated, not hand-edited, in the gold). Editing them is unnecessary and risky. The metadiff (`f1: 0.826`, `precision: 0.95`, `recall: 0.731`) over-represents go-edit quality (high precision) but the recall hit reflects the *generated-file scope creep* being scored against a gold that didn't touch them.

## Strengths

- **Most complete `go-edit.obo` change of the non-opus attempts.** It is the only one besides pr344 to refresh every stale inline `! vesicle coating` → `! vesicle coat assembly` comment: incoming edges on `GO:0016183` (synaptic vesicle coating), `GO:0048200` (Golgi transport vesicle coating), and `GO:0048208`'s own `is_a: GO:0006901` line — exactly the set the gold updated.
- **Obsoletion is correct and complete:** `name: obsolete ...`, `def: "OBSOLETE. ..."` (original dbxrefs kept), both `intersection_of` removed, `comment`, `term_tracker_item`, `is_obsolete: true`, `replaced_by: GO:0048208`. Restored-synonym dbxrefs `[GOC:ascb_2009, GOC:dph, GOC:tb]` match the gold exactly.
- **Both renames correct** with old labels restored as EXACT synonyms.
- Rigorous validation: pre- and post-edit `make travis_build` both passing, with an honest note that the only warnings were pre-existing Rhea-filtering noise.

## Issues

- **Provenance loss on the obsoleted term (error).** The diff removes `created_by: dph` and `creation_date: 2009-12-17T08:38:14Z` from `GO:0003400`. The gold and the `term-obsoletion` skill both retain these. Same defect as pr278.
- **Editing build-generated files (scope creep — the headline problem).** The agent modified `src/design_patterns/cc_assembly.tsv`, `regulation.tsv`, `regulation_by.tsv`, `docs/patterns/cc_assembly.md`, and `src/ontology/ld.txt`. These are *derived* from `go-edit.obo` by the ontology build (the current merged repo shows them correctly regenerated without any manual edit in the gold PR). Hand-editing generated artifacts is non-standard, will be overwritten on the next build, and risks divergence if the edits are imperfect. `ld.txt` in particular is a machine-generated logical-definition dump; hand-removing the `intersection_of` lines there is exactly the kind of edit the pipeline should own.
- **Weak obsoletion comment:** "this term is equivalent to COPII vesicle coat assembly" — biologically imprecise (it is a regulation term, not equivalent to the process); the gold's part_of explanation is correct.

Net: `partial_success`. The ontology-source edit is excellent (rivaling pr344), but the provenance deletion plus hand-editing five generated/derived files is a clear scope-discipline failure that the high precision metric hides.
