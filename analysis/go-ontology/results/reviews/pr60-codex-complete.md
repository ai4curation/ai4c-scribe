---
ontology: go-ontology
issue_number: 31636
pr_number: 31925
eval_repo_pr: 60
agent: std_codex_g55
model: gpt-5.5
runtime: codex
agent_config_tag: v9
case_type: synonym_update
difficulty: simple
f1: 0.857
precision: 0.857
recall: 0.857
jaccard: 0.75
outcome: success
failure_modes: []
reviewed_by: gpt-5.5
reviewed_at: 2026-05-11
---

<!-- Review this eval run following analysis/instructions/review-agent-eval.md

  Source issue: https://github.com/geneontology/go-ontology/issues/31636
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/31925
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/60
  Agent config: ai4curation/go-ontology-agent-config

  Quick reference:
    gh issue view 31636 --repo geneontology/go-ontology
    gh pr diff 31925 --repo geneontology/go-ontology
    gh pr diff 60 --repo ai4curation/eval-ont-agent-go
-->

## Summary

The agent correctly addressed issue #31636 for `GO:1990334` by replacing the species-specific label `Bfa1-Bub2 complex` with `SIN/MEN two-component GAP complex`, adding the requested narrow synonyms, broadening the definition, and adding the issue tracker metadata. The metadiff F1/precision/recall of 0.857 is a reasonable signal: the agent matches the core human solution, and the mismatch is mainly a different but defensible definition and xref list rather than a wrong ontology edit.


## Strengths

- Correctly edited the intended term, `GO:1990334`, and stayed scoped to `src/ontology/go-edit.obo`.
- Correctly changed the primary name from `Bfa1-Bub2 complex` to `SIN/MEN two-component GAP complex`, matching both the issue request and the human PR.
- Added both requested narrow synonyms on `GO:1990334`: `Bfa1-Bub2 complex` and `Byr4-Cdc16 GAP complex`.
- Revised the definition so it no longer describes only the budding yeast MEN/Tem1/Bfa1-Bub2 case. The agent's wording covers both SIN/MEN signaling and explicitly mentions Byr4-Cdc16/Spg1 in fission yeast and Bfa1-Bub2/Tem1 in budding yeast.
- Preserved the existing ontology placement: `is_a: GO:1902773 ! GTPase activator complex` and `relationship: part_of GO:0005816 ! spindle pole body`.
- Added `property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31636" xsd:anyURI`, matching the human PR metadata change.
- The PR notes indicate a reasonable method for a small synonym/definition update: term search, no unnecessary logical-definition change, and validation with `make travis_build`.


## Issues

- Minor definition/xref style divergence: the human PR preserved the existing `GOC:bhm` definition xref and `PMID:16449187`, while the agent replaced `GOC:bhm` with an additional literature xref, `PMID:9742395`. The added PMID is plausible support for the fission yeast Byr4-Cdc16/Spg1 example, but dropping the existing curator xref was unnecessary.
- The agent's definition is more example-driven than the human version. It says examples include Byr4-Cdc16 and Bfa1-Bub2, while the human PR more directly states the generalized Tem1/Spg1 GTPase role and preserves the original point that the complex keeps the GTPase inactive until spindle orientation is correct, inhibiting `MEN/SIN activation`. This is a stylistic and precision difference, not a failure to solve the issue.
