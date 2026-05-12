---
ontology: go-ontology
issue_number: 31965
pr_number: 31971
eval_repo_pr: 155
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
outcome: success
failure_modes: []
reviewed_by: gpt-5
reviewed_at: 2026-05-11
---

<!-- Review this eval run following analysis/instructions/review-agent-eval.md

  Source issue: https://github.com/geneontology/go-ontology/issues/31965
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/31971
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/155
  Agent config: ai4curation/go-ontology-agent-config

  Quick reference:
    gh issue view 31965 --repo geneontology/go-ontology
    gh pr diff 31971 --repo geneontology/go-ontology
    gh pr diff 155 --repo ai4curation/eval-ont-agent-go
-->

## Summary

The agent correctly refactored the protoporphyrinogen oxidase terms requested in issue #31965, including the parent `GO:0070818` and the quinone-dependent child `GO:0070819`. The metadiff score of 0.769 is a reasonable line-level signal, but it slightly under-rates the substantive result: the agent hit all explicit EC/RHEA, label, and definition requirements, with only minor synonym/provenance differences from the human PR.


## Strengths

- Correctly updated `GO:0070818` protoporphyrinogen oxidase activity with the RHEA:62000 stoichiometry in the definition, replaced the GOC definition xref with `RHEA:62000` while retaining `PMID:19583219`, and added `xref: RHEA:62000 {source="skos:exactMatch"}`.
- Correctly added the issue tracker annotation for #31965 to both modified terms, `GO:0070818` and `GO:0070819`.
- Correctly generalized `GO:0070819` from "menaquinone-dependent protoporphyrinogen oxidase activity" to "quinone-dependent protoporphyrinogen oxidase activity".
- Correctly changed the `GO:0070819` definition to the RHEA:65032 reaction, `protoporphyrinogen IX + 3 a quinone = protoporphyrin IX + 3 a quinol`, and used `RHEA:65032` as the definition xref while retaining `PMID:19583219`.
- Correctly removed the inappropriate `EC:1.3.3.4 {source="skos:broadMatch"}` from `GO:0070819`, since that EC belongs to the oxygen-dependent child `GO:0004729`, and added exact mappings to `EC:1.3.5.3` and `RHEA:65032`.
- Correctly changed the existing menaquinone-specific synonym on `GO:0070819`, "protoporphyrinogen-IX:menaquinone oxidoreductase activity", from EXACT to NARROW after broadening the term to quinone-dependent activity.
- Appropriately left `GO:0004729` oxygen-dependent protoporphyrinogen oxidase activity untouched; it was mentioned in the issue only as context for why `EC:1.3.3.4` should not remain on `GO:0070819`.


## Issues

- Minor omission: the human PR preserved the old `GO:0070819` label, "menaquinone-dependent protoporphyrinogen oxidase activity", as a NARROW synonym with an empty source list. The agent did not add this old-label synonym, which slightly weakens searchability and label-change provenance, although it did retain the related menaquinone-specific oxidoreductase synonym as NARROW.
- Minor scope/style difference: the agent added an extra exact synonym on `GO:0070819`, "protoporphyrinogen-IX:quinone oxidoreductase activity" with source `EC:1.3.5.3`, whereas the human PR did not. This is plausible for the generalized EC mapping and does not conflict with the issue, but it is extra work beyond the requested edit.
- Insignificant diff-only difference: the agent ordered definition xrefs as `[PMID:19583219, RHEA:62000]` and `[PMID:19583219, RHEA:65032]`, while the human PR put RHEA first. This has no semantic impact.
