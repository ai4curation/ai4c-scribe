---
ontology: go-ontology
issue_number: 31961
pr_number: 32015
eval_repo_pr: 38
agent: std_codex_g55
model: gpt-5.5
runtime: codex
agent_config_tag: v9
case_type: obsoletion
difficulty: simple
f1: 0.762
precision: 0.889
recall: 0.667
jaccard: 0.615
outcome: partial_success
failure_modes:
  - over_editing
  - scope_creep
reviewed_by: gpt-5
reviewed_at: 2026-05-11
---

<!-- Review this eval run following analysis/instructions/review-agent-eval.md

  Source issue: https://github.com/geneontology/go-ontology/issues/31961
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/32015
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/38
  Agent config: ai4curation/go-ontology-agent-config

  Quick reference:
    gh issue view 31961 --repo geneontology/go-ontology
    gh pr diff 32015 --repo geneontology/go-ontology
    gh pr diff 38 --repo ai4curation/eval-ont-agent-go
-->

## Summary

The agent correctly solved the central request from geneontology/go-ontology#31961 by obsoleting `GO:0008785 alkyl hydroperoxide reductase activity` and replacing it with `GO:0102039 NADH-dependent peroxiredoxin activity`. The metadiff `F1=0.762` reflects a real mismatch: the `GO:0008785` obsoletion is substantively right, but the agent made additional edits to `GO:0009321`, `GO:0070937`, and `GO:0102039` that were outside the final accepted human PR. This is a partial success because the requested term was handled correctly, but the PR would need scope cleanup before it matched maintainer expectations.


## Strengths

- Correctly identified `GO:0008785` as the term to obsolete and renamed it to `obsolete alkyl hydroperoxide reductase activity`.
- Correctly applied the main obsoletion mechanics for `GO:0008785`: prefixed the definition with `OBSOLETE.`, removed the asserted `is_a GO:0016668` parent, added `is_obsolete: true`, preserved the existing tracker links for issues `28261` and `28340`, added the issue `31961` tracker, and added `replaced_by: GO:0102039`.
- Chose the correct replacement, `GO:0102039 NADH-dependent peroxiredoxin activity`, matching the issue's statement that `GO:0008785` was an over-specific substrate-specific version of the EC `1.11.1.26`-aligned activity.
- Added a valid obsoletion comment on `GO:0008785` explaining that the term was too substrate-specific for known gene products.
- Performed useful broader term search: it found textual references to `GO:0008785` in `GO:0009321 alkyl hydroperoxide reductase complex` and `GO:0070937 CRD-mediated mRNA stability complex`, and noticed that `GO:0102039` already carried closely related EC/RHEA/MetaCyc metadata.


## Issues

- The agent over-edited the ontology by changing the free-text comment on `GO:0009321` from a see-also reference to `GO:0008785` to one pointing to `GO:0102039`. This is biologically understandable, but it was not part of the accepted final PR; the maintainer explicitly asked the human PR not to change comments in other terms, and those comment edits were reverted.
- The agent also removed a stale `GO:0008785` see-also comment from `GO:0070937 CRD-mediated mRNA stability complex`. That comment looks unrelated and may be a genuine pre-existing copy/paste artifact, but issue `31961` asked only to obsolete `GO:0008785` and replace it with `GO:0102039`.
- The agent added `synonym: "alkyl hydroperoxide reductase activity" EXACT []` and a new issue `31961` tracker to `GO:0102039`. Adding the former label as a synonym is defensible for searchability, especially because the issue mentions the EC synonym, but it changes the replacement term itself and was not included in the human solution.
- The `GO:0008785` obsoletion comment is less complete than the accepted PR's wording. It captures the substrate-specific rationale but omits the explicit EC `1.11.1.26` synonym-to-`GO:0102039` connection that the human PR documented.
