---
ontology: go-ontology
issue_number: 31965
pr_number: 31971
eval_repo_pr: 136
agent: std_opencode_g55
model: gpt-5.5
runtime: opencode
agent_config_tag: v9
case_type: reclassification
difficulty: hard
f1: 0.769
precision: 0.769
recall: 0.769
jaccard: 0.625
outcome: partial_success
failure_modes:
  - under_editing
  - scope_creep
reviewed_by: gpt-5.5
reviewed_at: 2026-05-11
---

<!-- Review this eval run following analysis/instructions/review-agent-eval.md

  Source issue: https://github.com/geneontology/go-ontology/issues/31965
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/31971
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/136
  Agent config: ai4curation/go-ontology-agent-config

  Quick reference:
    gh issue view 31965 --repo geneontology/go-ontology
    gh pr diff 31971 --repo geneontology/go-ontology
    gh pr diff 136 --repo ai4curation/eval-ont-agent-go
-->

## Summary

The agent substantially solved the requested reclassification for issue #31965: it updated `GO:0070818` and broadened `GO:0070819` from menaquinone-specific to quinone-dependent with the requested EC/RHEA mappings and reaction definitions. The metadiff score (`F1=0.769`, precision `0.769`, recall `0.769`) is a reasonable signal here: the core ontology meaning matches the human PR, but there are real synonym-level divergences.


## Strengths

- Correctly updated `GO:0070818` (`protoporphyrinogen oxidase activity`) to use the RHEA:62000 stoichiometry in the definition: `protoporphyrinogen IX + 3 acceptor = protoporphyrin IX + 3 reduced acceptor`.
- Correctly added `xref: RHEA:62000 {source="skos:exactMatch"}` to `GO:0070818` and replaced the definition's `GOC:mah` provenance with `RHEA:62000` while retaining `PMID:19583219`.
- Correctly broadened `GO:0070819` from `menaquinone-dependent protoporphyrinogen oxidase activity` to `quinone-dependent protoporphyrinogen oxidase activity`.
- Correctly removed the inappropriate `EC:1.3.3.4 {source="skos:broadMatch"}` xref from `GO:0070819`; the issue notes that EC:1.3.3.4 belongs with the oxygen-dependent term `GO:0004729`.
- Correctly added exact mappings from `GO:0070819` to `EC:1.3.5.3` and `RHEA:65032`, and changed the definition to the RHEA:65032 reaction: `protoporphyrinogen IX + 3 a quinone = protoporphyrin IX + 3 a quinol`.
- Correctly changed the existing `GO:0070819` synonym `protoporphyrinogen-IX:menaquinone oxidoreductase activity` from `EXACT` to `NARROW`, matching the broader new label.
- Added `term_tracker_item` annotations for issue #31965 to both edited terms, as in the human PR.


## Issues

- The agent did not preserve the old `GO:0070819` label, `menaquinone-dependent protoporphyrinogen oxidase activity`, as a `NARROW` synonym. The human PR did this, and it is the better ontology-editing pattern after broadening a term label because it preserves searchability and historical annotation intent.
- The agent added an extra exact synonym to `GO:0070819`: `protoporphyrinogen-IX:quinone oxidoreductase activity` with source `EC:1.3.5.3`. This may be defensible as a lexical synonym, but it was not requested in the issue and was not part of the human solution, so it is a small scope expansion.
- The definition xref order differs from the human PR (`[PMID:19583219, RHEA:65032]` versus `[RHEA:65032, PMID:19583219]`, similarly for `RHEA:62000`). This is stylistic rather than a semantic error.
