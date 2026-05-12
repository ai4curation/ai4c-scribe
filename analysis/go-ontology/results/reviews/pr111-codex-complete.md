---
ontology: go-ontology
issue_number: 31295
pr_number: 32040
eval_repo_pr: 111
agent: std_opencode_g55
model: gpt-5.5
runtime: opencode
agent_config_tag: v9
case_type: new_term
difficulty: medium
f1: 0.636
precision: 0.583
recall: 0.7
jaccard: 0.467
outcome: partial_success
failure_modes:
  - under_editing
  - missed_requirement
reviewed_by: gpt-5.5
reviewed_at: 2026-05-11
---

<!-- Review this eval run following analysis/instructions/review-agent-eval.md

  Source issue: https://github.com/geneontology/go-ontology/issues/31295
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/32040
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/111
  Agent config: ai4curation/go-ontology-agent-config

  Quick reference:
    gh issue view 31295 --repo geneontology/go-ontology
    gh pr diff 32040 --repo geneontology/go-ontology
    gh pr diff 111 --repo ai4curation/eval-ont-agent-go
-->

## Summary

The agent added the requested new cellular component term `GO:7770070 ! p24 cargo receptor complex` under `GO:0062137 ! cargo receptor complex`, with a reasonable literature-supported definition and basic metadata. However, it missed important content present in the accepted PR, especially the `capable_of_part_of GO:0006888 ! endoplasmic reticulum to Golgi vesicle-mediated transport` relationship and the final curator-refined definition/synonym set. The metadiff F1 of 0.636 is a fair signal: this is a partial success with the core term present, but it is under-edited relative to the human solution.


## Strengths

- Correctly created `GO:7770070` with the requested label `p24 cargo receptor complex` in the `cellular_component` namespace.
- Correctly placed the term as `is_a: GO:0062137 ! cargo receptor complex`, matching both the issue request and the human PR.
- Included the issue tracker metadata and normal creation metadata, including `property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31295" xsd:anyURI`.
- Used the three PMIDs supplied in the issue (`PMID:32456004`, `PMID:34647572`, `PMID:27569046`) and produced a definition that captures ER-to-Golgi cycling, COPII-mediated transport, and GPI-anchored protein cargo.
- Added `p24 complex` as an EXACT synonym, matching the human PR.


## Issues

- Omitted the relationship `relationship: capable_of_part_of GO:0006888 ! endoplasmic reticulum to Golgi vesicle-mediated transport`. The accepted PR added this axiom, following the precedent of other cargo receptor complex terms such as `GO:0061852 ! retrograde cargo receptor complex, Golgi to ER`; the agent only mentioned the process in the textual definition.
- Missed the final curator-refined definition used by the human PR. The accepted term defines the complex as a conserved, hetero-oligomeric cycling ER-Golgi protein complex, includes the early secretory pathway organization role, and states that a functional p24 complex typically contains one member of each p24 subfamily (alpha, beta, gamma, delta). The agent's definition is plausible but less complete.
- Used a narrower reference set than the human PR. The human solution retained the requested `PMID:27569046`, `PMID:32456004`, and `PMID:34647572` and added `PMID:19566487` and `PMID:26224213`; the agent omitted those added references.
- Missed useful related synonyms from the accepted PR: `Emp24-Erv25 complex`, `p24 family complex`, and `TMED complex`.
- Added extra EXACT synonyms, `p24 family protein complex` and `p24 protein complex`, that were not in the human PR. These may be defensible search synonyms, but EXACT scope is less well justified than the accepted PR's more conservative RELATED synonyms.
