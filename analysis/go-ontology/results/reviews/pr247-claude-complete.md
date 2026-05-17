---
ontology: go-ontology
issue_number: 31945
pr_number: 32013
eval_repo_pr: 247
agent: std_opencode_gem4
model: gemma-4-31b
runtime: opencode
agent_config_tag: v9
case_type: reclassification
difficulty: medium
f1: 0.833
precision: 0.75
recall: 0.938
jaccard: 0.714
outcome: partial_success
failure_modes:
  - missed_requirement
  - under_editing
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

<!-- Review this eval run following analysis/instructions/review-agent-eval.md

  Source issue: https://github.com/geneontology/go-ontology/issues/31945
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/32013
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/247
  Agent config: ai4curation/go-ontology-agent-config

  Quick reference:
    gh issue view 31945 --repo geneontology/go-ontology
    gh pr diff 32013 --repo geneontology/go-ontology
    gh pr diff 247 --repo ai4curation/eval-ont-agent-go
-->

## Summary

A respectable result for a small open model (gemma-4-31b): the obsoletion is correct and both renames are applied. But the agent **deleted the old labels entirely instead of demoting them to synonyms** — `GO:0006901` loses its `vesicle coat assembly` BROAD synonym with nothing added back, and `GO:0048208` loses its `COPII vesicle coat assembly` EXACT synonym with no `COPII vesicle coating` synonym restored. This breaks the gold's (and standard GO practice's) searchability guarantee: after renaming, the *old* primary label must survive as a synonym so existing literature/tool references still resolve. The metadiff (`f1: 0.833`, `precision: 0.75`, `recall: 0.938`) modestly over-represents quality — high recall because the renames and obsoletion lines match, but the lost synonyms are a genuine data-loss defect not penalized proportionally.

## Strengths

- **Obsoletion is correct and complete:** `name: obsolete ...`, `def: "OBSOLETE. ..."` (original dbxrefs kept), both `intersection_of` removed, `comment`, `term_tracker_item`, `is_obsolete: true`, `replaced_by: GO:0048208`, and `created_by: dph`/`creation_date` retained — full provenance preserved. This is the part the model got fully right.
- **Both renames applied** to the correct primary labels (`GO:0006901` → `vesicle coat assembly`, `GO:0048208` → `COPII vesicle coat assembly`).
- Honest validation reporting: PR comment discloses `make travis_build` failed in-environment (missing `amm`/`robot`) and that it fell back to `obo-grep.pl` verification — appropriate transparency rather than a false "all checks passed".

## Issues

- **Old labels dropped, not preserved as synonyms (under-editing / data loss — the headline problem).** For `GO:0006901` the diff removes `synonym: "vesicle coat assembly" BROAD []` and adds *nothing* back, so the old label `vesicle coating` is lost entirely (it was the name, now neither name nor synonym). For `GO:0048208` it removes `synonym: "COPII vesicle coat assembly" EXACT [...]` and does *not* add `synonym: "COPII vesicle coating" EXACT [...]`. The gold (and the rename convention) requires the demoted label to be retained as a synonym for searchability and annotation-tool resolution. This is a genuine loss of lexical information.
- **Missed the stale-comment maintenance (omission).** No refresh of `is_a: GO:0006901 ! vesicle coating` → `! vesicle coat assembly` on `GO:0016183`/`GO:0048200`/`GO:0048208` self-edge.
- **Weak obsoletion comment** that also references the now-stale old label: "can be accurately described using GO:0048208 COPII vesicle coating" — should read "COPII vesicle coat assembly" after its own rename. Minor internal inconsistency.

Net: `partial_success` — obsoletion solid, but failing to preserve the old labels as synonyms is a real searchability/data-loss regression that the recall-heavy metadiff underweights.
