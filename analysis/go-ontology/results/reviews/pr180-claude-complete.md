---
ontology: go-ontology
issue_number: 31916
pr_number: 32024
eval_repo_pr: 180
agent: std_codex_g54
model: gpt-5.4
runtime: codex
agent_config_tag: v9
case_type: obsoletion
difficulty: medium
f1: 0.965
precision: 0.965
recall: 0.965
jaccard: 0.932
outcome: success
failure_modes: []
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

<!-- Independent claude review.
  Source issue: https://github.com/geneontology/go-ontology/issues/31916
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/32024
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/180
-->

## Summary

The agent fully and correctly resolved issue #31916. It obsoleted the four Entner-Doudoroff variant terms with `replaced_by: GO:0061678`, obsoleted GO:0061688 with `replaced_by: GO:0006096`, and rewrote the GO:0061678 MetaCyc xrefs with the required `{source="skos:narrowMatch"}` qualifier. The substantive diff matches gold PR #32024. F1=0.965 slightly under-represents the result, since the only differences are comment wording and one extra harmless tracker line. The PR comment includes a thorough checklist documenting term-obsoletion skill consultation, design-pattern review (catabolic_process.md), and validation via `make travis_build`.

## Strengths

- Correct, complete obsoletion of GO:0009255, GO:0061679, GO:0061680, GO:0061681: obsolete name/def prefixes, `is_obsolete: true`, `replaced_by: GO:0061678`, issue #31916 tracker, and removal of all active logical axioms and term-level MetaCyc xrefs, plus the GO:0061679 RELATED synonym.
- GO:0061688 obsoleted with `replaced_by: GO:0006096`, correctly incorporating the curator decision from the issue thread (not just the issue body) and stripping its `is_a`/`intersection_of`/`starts_with` axioms.
- GO:0061678 mapping cleanup exactly correct: removed grouping-class `MetaCyc:Entner-Doudoroff-Pathways`; added ENTNER-DOUDOROFF-PWY, NPGLUCAT-PWY, PWY-2221, PWY-8004 each with `{source="skos:narrowMatch"}`. This is the hardest detail and it is done right.
- Preserved the unrelated issue #28392 tracker and `created_by`/`creation_date` lines on the obsoleted variants, matching the gold PR.
- Strong documented methodology: explicit term-obsoletion skill use, design-pattern doc consultation recorded in DESIGN_PATTERNS.md, pre/post validation, and an honest note that `runoak` was broken so annotation impact relied on curator-provided counts.

## Issues

- Style only: obsoletion comments ("this pathway variant is being merged into the broader Entner-Doudoroff pathway term") are less informative than the gold PR's text, which names GO:0061678 explicitly and cites MetaCyc's variant-pathway treatment / GO-CAM rationale. No semantic effect.
- Minor scope: extra `property_value: term_tracker_item ".../31916"` added to the still-active parent GO:0061678, which the human PR omitted. Harmless; the only reason F1 is below 1.0.
- No correctness, syntax, or completeness problems.
