---
ontology: go-ontology
issue_number: 31295
pr_number: 32040
eval_repo_pr: 173
agent: std_codex_g54
model: gpt-5.4
runtime: codex
agent_config_tag: v9
case_type: new_term
difficulty: medium
f1: 0.7
precision: 0.583
recall: 0.875
jaccard: 0.538
outcome: partial_success
failure_modes:
  - under_editing
  - missed_requirement
reviewed_by: codex
reviewed_at: "2026-05-16"
---

<!-- Review this eval run following analysis/instructions/review-agent-eval.md

  Source issue: https://github.com/geneontology/go-ontology/issues/31295
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/32040
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/173
  Agent config: ai4curation/go-ontology-agent-config

  Quick reference:
    gh issue view 31295 --repo geneontology/go-ontology
    gh pr diff 32040 --repo geneontology/go-ontology
    gh pr diff 173 --repo ai4curation/eval-ont-agent-go
-->

## Summary

The agent correctly created the requested cellular component term `GO:7770070 ! p24 cargo receptor complex` under `GO:0062137 ! cargo receptor complex`, with a reasonable basic definition and issue-tracker metadata. However, compared with the accepted PR it under-edited the term: it omitted the transport-process relationship, most synonyms, and some literature support used in the human solution. The metadiff F1 of 0.700 is directionally fair, though the line-level score somewhat under-represents that the core ontology object was correct.


## Strengths

- Added the correct new term ID and label, `GO:7770070 ! p24 cargo receptor complex`, in the `cellular_component` namespace.
- Placed the term under the requested parent `GO:0062137 ! cargo receptor complex`, matching both the issue and the human PR.
- Wrote a biologically plausible definition that captures ER-Golgi cycling, cargo receptor function, selective secretory cargo export, GPI-anchored proteins, and COPII vesicles.
- Included the exact synonym `p24 complex`, which was also present in the accepted solution.
- Added standard metadata: `property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31295"`, `created_by: dragon-ai-agent`, and a `creation_date`.


## Issues

- Omitted the relationship added by the accepted PR: `relationship: capable_of_part_of GO:0006888 ! endoplasmic reticulum to Golgi vesicle-mediated transport`. This is the most important substantive gap because it connects `GO:7770070` to the vesicle-mediated transport process motivating the request.
- The definition is less complete than the human PR. It says "heteromeric membrane protein complex" but does not capture the accepted term's "conserved, hetero-oligomeric (often tetrameric)" characterization or the typical alpha, beta, gamma, and delta p24 subfamily composition.
- Omitted three related synonyms from the human PR: `Emp24-Erv25 complex`, `p24 family complex`, and `TMED complex`. These are useful search/access terms for yeast and human ortholog naming.
- Used fewer definition references than the accepted PR. The agent cited `PMID:32456004`, `PMID:19566487`, and `PMID:34647572`, but omitted `PMID:27569046` from the issue and `PMID:26224213` from the accepted definition.
