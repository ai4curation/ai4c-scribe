---
ontology: go-ontology
issue_number: 31916
pr_number: 32024
eval_repo_pr: 668
agent: std_opencode_g54
model: gpt-5.4
runtime: opencode
agent_config_tag: v9
case_type: obsoletion
difficulty: medium
case_quality: good
f1: 0.948
precision: 0.965
recall: 0.932
jaccard: 0.902
outcome: success
failure_modes:
  - over_editing
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-17
---

<!-- Independent claude review.
  Source issue: https://github.com/geneontology/go-ontology/issues/31916
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/32024
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/668
-->

## Summary

The agent fully and correctly resolved issue #31916, producing a diff byte-identical to attempt #620 (same blob `2c6a89c`, F1=0.948, P=0.965, R=0.932). It obsoleted all five curator-requested terms (GO:0009255, GO:0061679, GO:0061680, GO:0061681 → `replaced_by: GO:0061678`; GO:0061688 → `replaced_by: GO:0006096`) and performed the GO:0061678 MetaCyc narrowMatch cleanup exactly as specified. The PR comment adds a thorough, accurate methodology checklist (pre/post `make travis_build`, annotation-impact review). The substantive result equals gold PR #32024; the recall gap is a single minor provenance regression.

## Strengths

- Complete, correct obsoletion of GO:0009255, GO:0061679, GO:0061680, GO:0061681 with `replaced_by: GO:0061678`, and GO:0061688 with `replaced_by: GO:0006096`: obsolete name/def prefixes, `is_obsolete: true`, issue #31916 tracker, all active `is_a`/`intersection_of` axioms and term-level MetaCyc xrefs/synonyms removed.
- Correctly incorporated the in-thread curator decision routing GO:0061688 to GO:0006096 (not the issue body, which only covered the four ED variants).
- GO:0061678 mapping cleanup exactly correct: grouping-class `MetaCyc:Entner-Doudoroff-Pathways` removed; ENTNER-DOUDOROFF-PWY, NPGLUCAT-PWY, PWY-2221, PWY-8004 each added with `{source="skos:narrowMatch"}` — the most error-prone part of the task, done right.
- Excellent documented methodology in the PR/issue comments: explicit obsoletion workflow, pre- and post-edit `make travis_build` validation, and an honest annotation-impact note (GO:0009255 has EXP annotations, GO:0061688 has 10 CGD IEAs) consistent with the issue discussion.
- Tightly scoped to `src/ontology/go-edit.obo`; no out-of-scope edits.

## Issues

- Over-deletion of provenance (the recall hit): the agent removed `created_by: dph` / `creation_date:` lines from GO:0061679, GO:0061680, GO:0061681 and GO:0061688, whereas gold PR #32024 retains them on obsoleted stanzas per standard GO practice. Cosmetic but a genuine regression versus gold.
- Also dropped the obsoletion-unrelated `property_value: term_tracker_item ".../28392"` on GO:0061680 that gold preserved — mildly over-aggressive cleanup of historical metadata.
- Style only: obsoletion `comment` wording is terser than gold's, which names MetaCyc's variant-pathway treatment and the GO-CAM rationale. No semantic effect.
- No correctness, syntax, or completeness problems; functionally equivalent to the merged human PR.
