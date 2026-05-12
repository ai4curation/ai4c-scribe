---
ontology: go-ontology
issue_number: 31961
pr_number: 32015
eval_repo_pr: 37
agent: std_codex_g54
model: gpt-5.4
runtime: codex
agent_config_tag: v9
case_type: obsoletion
difficulty: simple
f1: 0.8
precision: 0.889
recall: 0.727
jaccard: 0.667
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
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/37
  Agent config: ai4curation/go-ontology-agent-config

  Quick reference:
    gh issue view 31961 --repo geneontology/go-ontology
    gh pr diff 32015 --repo geneontology/go-ontology
    gh pr diff 37 --repo ai4curation/eval-ont-agent-go
-->

## Summary

The agent correctly handled the central request from geneontology/go-ontology#31961: it obsoleted `GO:0008785 alkyl hydroperoxide reductase activity` and added `replaced_by: GO:0102039` for `NADH-dependent peroxiredoxin activity`. The metadiff `F1=0.8` is directionally fair: the core ontology edit matches the accepted PR, but the agent made two additional free-text comment changes that the human PR initially tried and then reverted after maintainer feedback. This is a partial success because the substantive obsoletion is right, but the PR would need scope cleanup before acceptance.


## Strengths

- Correctly targeted `GO:0008785` and changed the label to `obsolete alkyl hydroperoxide reductase activity`.
- Correctly applied the standard obsoletion mechanics to `GO:0008785`: prefixed the definition with `OBSOLETE.`, removed the asserted `is_a GO:0016668` parent, added `is_obsolete: true`, preserved the existing `term_tracker_item` links for issues `28261` and `28340`, added a tracker link for issue `31961`, and added `replaced_by: GO:0102039`.
- Chose the correct replacement term, `GO:0102039 NADH-dependent peroxiredoxin activity`, matching the issue's explanation that `GO:0008785` was a substrate-specific version of the broader EC 1.11.1.26-aligned activity.
- Added a reasonable obsoletion comment explaining that `GO:0008785` represents a substrate-specific instance of NADH-dependent peroxiredoxin activity.
- The extra edits show useful term-search behavior: the agent found remaining textual references to `GO:0008785` in `GO:0009321 alkyl hydroperoxide reductase complex` and `GO:0070937 CRD-mediated mRNA stability complex`.


## Issues

- The agent over-edited outside the final accepted scope by changing the free-text comment on `GO:0009321` from a see-also reference to `GO:0008785` to one pointing to `GO:0102039`. This cleanup is biologically understandable, but the maintainer explicitly asked the human PR not to change comments in other terms, and the accepted diff left `GO:0009321` unchanged.
- The agent also removed the stale `GO:0008785` see-also comment from `GO:0070937`. That comment appears unrelated to a CRD-mediated mRNA stability complex and may be a real pre-existing copy/paste artifact, but it was not requested by issue `31961` and was not retained in the human solution.
- The `GO:0008785` obsoletion comment is less informative than the accepted PR's wording. It captures the substrate-specific rationale, but omits the issue's more precise explanation that "alkyl hydroperoxide reductase" is listed as a synonym of EC `1.11.1.26`, which corresponds to `GO:0102039`.
