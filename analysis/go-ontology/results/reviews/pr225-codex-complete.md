---
ontology: go-ontology
issue_number: 31961
pr_number: 32015
eval_repo_pr: 225
agent: std_opencode_gem4
model: gemma-4-31b
runtime: opencode
agent_config_tag: v9
case_type: obsoletion
difficulty: simple
f1: 0.727
precision: 0.889
recall: 0.615
jaccard: 0.571
outcome: partial_success
failure_modes:
  - over_editing
  - scope_creep
  - missed_requirement
reviewed_by: codex
reviewed_at: "2026-05-16"
---

<!-- Review this eval run following analysis/instructions/review-agent-eval.md

  Source issue: https://github.com/geneontology/go-ontology/issues/31961
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/32015
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/225
  Agent config: ai4curation/go-ontology-agent-config

  Quick reference:
    gh issue view 31961 --repo geneontology/go-ontology
    gh pr diff 32015 --repo geneontology/go-ontology
    gh pr diff 225 --repo ai4curation/eval-ont-agent-go
-->

## Summary

The agent correctly handled the central request from geneontology/go-ontology#31961: `GO:0008785 alkyl hydroperoxide reductase activity` was made obsolete and given `replaced_by: GO:0102039` for `NADH-dependent peroxiredoxin activity`. The metadiff score (`f1: 0.727`, `precision: 0.889`, `recall: 0.615`) is directionally fair: the core ontology change is right, but the agent both missed retained metadata from the accepted PR and made extra edits outside the final human scope. This is a partial success rather than a failure because the biological target and obsoletion mechanics are substantially correct.


## Strengths

- Correctly identified `GO:0102039 NADH-dependent peroxiredoxin activity` as the replacement for `GO:0008785`, matching the issue's instruction that the more substrate-specific `GO:0008785` should be replaced by the EC 1.11.1.26-aligned term.
- Applied the main obsoletion pattern to `GO:0008785`: renamed it to `obsolete alkyl hydroperoxide reductase activity`, prefixed the definition with `OBSOLETE.`, removed the asserted `is_a GO:0016668` parent, added `is_obsolete: true`, and added `replaced_by: GO:0102039`.
- Added a `term_tracker_item` for issue `31961`, which matches the human PR's provenance addition.
- The added obsoletion comment captures the key reason from the issue: the old term was more specific than the specificity of any known gene product.
- The extra comment checks show that the agent searched for remaining references to `GO:0008785`, finding the free-text comments in `GO:0009321 alkyl hydroperoxide reductase complex` and `GO:0070937 CRD-mediated mRNA stability complex`.


## Issues

- The agent deleted two pre-existing `term_tracker_item` values from `GO:0008785`: issues `28261` and `28340`. The accepted human PR preserved both existing tracker links and added issue `31961`; removing existing provenance metadata is a real regression.
- The agent over-edited other terms. It changed the `GO:0009321` comment to point to `GO:0102039` and removed a stale `GO:0008785` comment from `GO:0070937`. These edits are understandable cleanup, especially because `GO:0070937` is clearly unrelated, but the accepted PR reverted the same comment changes after curator feedback asking not to change comments in other terms.
- The obsoletion comment on `GO:0008785` is less informative than the accepted PR's comment: it omits the issue's EC 1.11.1.26 / Expasy synonym rationale and does not name `GO:0102039`, though the `replaced_by` tag still carries the replacement formally.
- No wrong-term or syntax problem is evident. The main weaknesses are metadata loss and scope discipline, not misunderstanding of the requested obsoletion.
