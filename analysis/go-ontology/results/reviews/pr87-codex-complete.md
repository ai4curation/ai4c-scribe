---
ontology: go-ontology
issue_number: 31295
pr_number: 32040
eval_repo_pr: 87
agent: std_opencode_g55
model: gpt-5.5
runtime: opencode
agent_config_tag: v9
case_type: new_term
difficulty: medium
f1: 0.696
precision: 0.667
recall: 0.727
jaccard: 0.533
outcome: partial_success
failure_modes:
  - under_editing
  - over_editing
reviewed_by: gpt-5.5
reviewed_at: 2026-05-11
---

<!-- Review this eval run following analysis/instructions/review-agent-eval.md

  Source issue: https://github.com/geneontology/go-ontology/issues/31295
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/32040
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/87
  Agent config: ai4curation/go-ontology-agent-config

  Quick reference:
    gh issue view 31295 --repo geneontology/go-ontology
    gh pr diff 32040 --repo geneontology/go-ontology
    gh pr diff 87 --repo ai4curation/eval-ont-agent-go
-->

## Summary

The agent correctly added the requested new cellular component term `GO:7770070 ! p24 cargo receptor complex` under `GO:0062137 ! cargo receptor complex`, with tracker metadata and the key ER-to-Golgi transport relationship. The `F1=0.696` score is directionally fair: this is a useful partial solution, but it misses several accepted human-PR details and adds one extra modeling assertion that was not in the accepted solution.


## Strengths

- Created the correct term ID and label, `GO:7770070 ! p24 cargo receptor complex`, in the `cellular_component` namespace.
- Used the requested parent `is_a: GO:0062137 ! cargo receptor complex`, matching both the source issue and the human PR.
- Included the important process relationship from the accepted PR: `relationship: capable_of_part_of GO:0006888 ! endoplasmic reticulum to Golgi vesicle-mediated transport`.
- Added a reasonable definition grounded in the requested biology: a p24-family cargo receptor complex associated with the early secretory pathway and COPII-mediated export.
- Included the issue tracker link, `created_by`, and `creation_date` metadata, and retained most of the PMID support used by the human PR (`PMID:19566487`, `PMID:27569046`, `PMID:32456004`, `PMID:34647572`).


## Issues

- The definition is less complete than the accepted curator-refined definition. It omits the explicit "conserved, hetero-oligomeric (often tetrameric)" characterization, the GPI-anchored cargo specificity, the role in maintaining early secretory pathway organization, and the typical alpha/beta/gamma/delta p24 subfamily composition.
- The agent omitted `PMID:26224213`, which the accepted PR included as definition evidence for `GO:7770070`.
- The synonym set is under-edited relative to the accepted PR. It includes only `p24 complex` and adds `p24 protein complex` as EXACT, but misses the accepted RELATED synonyms `Emp24-Erv25 complex`, `p24 family complex`, and `TMED complex`.
- The extra assertion `relationship: capable_of GO:0097020 ! COPII receptor activity` is defensible biologically but goes beyond the accepted modeling. The human PR deliberately followed sibling complex precedent by asserting `capable_of_part_of GO:0006888` and did not add a direct molecular-function capability on this term.
