---
ontology: go-ontology
issue_number: 31965
pr_number: 31971
eval_repo_pr: 282
agent: std_opencode_kimi
model: kimi-k2.6
runtime: opencode
agent_config_tag: v9
case_type: reclassification
difficulty: hard
f1: 0.87
precision: 0.769
recall: 1.0
jaccard: 0.769
outcome: partial_success
failure_modes:
- wrong_pattern
- missed_requirement
reviewed_by: codex
reviewed_at: "2026-05-16"
---

<!-- Review this eval run following analysis/instructions/review-agent-eval.md

  Source issue: https://github.com/geneontology/go-ontology/issues/31965
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/31971
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/282
  Agent config: ai4curation/go-ontology-agent-config

  Quick reference:
    gh issue view 31965 --repo geneontology/go-ontology
    gh pr diff 31971 --repo geneontology/go-ontology
    gh pr diff 282 --repo ai4curation/eval-ont-agent-go
-->

## Summary

The agent correctly updated the EC/RHEA mappings and definitions for GO:0070818 and GO:0070819, including the broader `quinone-dependent` label and the exact EC:1.3.5.3/RHEA:65032 mappings. The result is incomplete because it did not restructure the GO:0070819 synonyms after broadening the term: the menaquinone-specific oxidoreductase synonym remained EXACT, and the old label was not preserved as a NARROW synonym.

## Strengths

- Correctly changed GO:0070818 to the 3-acceptor RHEA:62000 definition and added `xref: RHEA:62000 {source="skos:exactMatch"}`.
- Correctly renamed GO:0070819 from menaquinone-dependent to quinone-dependent protoporphyrinogen oxidase activity.
- Correctly replaced the inappropriate GO:0070819 `EC:1.3.3.4` broadMatch with exact matches to `EC:1.3.5.3` and `RHEA:65032`.
- Added issue tracker provenance to both edited terms.

## Issues

- Wrong synonym scope: `protoporphyrinogen-IX:menaquinone oxidoreductase activity` should be changed from EXACT to NARROW after GO:0070819 is broadened to quinone-dependent activity.
- Missing synonym: the previous GO:0070819 label, `menaquinone-dependent protoporphyrinogen oxidase activity`, should be retained as a NARROW synonym.
- These synonym details are not cosmetic in this case; they are the main curation safeguard preserving the old menaquinone-specific wording under a broader quinone class.
