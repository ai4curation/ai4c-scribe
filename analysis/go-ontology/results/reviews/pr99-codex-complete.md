---
ontology: go-ontology
issue_number: 31984
pr_number: 31987
eval_repo_pr: 99
agent: std_opencode_g55
model: gpt-5.5
runtime: opencode
agent_config_tag: v9
case_type: axiom_repair
difficulty: hard
f1: 0.947
precision: 0.9
recall: 1.0
jaccard: 0.9
outcome: success
failure_modes: []
reviewed_by: codex
reviewed_at: "2026-05-16"
---

<!-- Review this eval run following analysis/instructions/review-agent-eval.md

  Source issue: https://github.com/geneontology/go-ontology/issues/31984
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/31987
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/99
  Agent config: ai4curation/go-ontology-agent-config

  Quick reference:
    gh issue view 31984 --repo geneontology/go-ontology
    gh pr diff 31987 --repo geneontology/go-ontology
    gh pr diff 99 --repo ai4curation/eval-ont-agent-go
-->

## Summary

The agent correctly addressed the core requirements from issue #31984: it renamed and redefined `GO:0008805`, reparented it under the quinone/similar-compound acceptor parent `GO:0052738`, and updated the `GO:0043885` anaerobic reaction definition. The high metadiff score (`f1=0.947`, precision `0.9`, recall `1.0`) is appropriate for a near-match, though it slightly overstates completeness because the agent missed one synonym-preservation line from the human PR.


## Strengths

- Correctly changed `GO:0008805` from `carbon-monoxide oxygenase activity` to `aerobic carbon monoxide dehydrogenase activity`, matching the issue request and the EC/RHEA framing.
- Correctly replaced the stale `GO:0008805` cytochrome b-561 definition with the quinone reaction `CO + a quinone + H2O = a quinol + CO2.` and used `RHEA:48880` as the definition xref, matching the human PR.
- Correctly reparented `GO:0008805` from `GO:0016622` (`cytochrome as acceptor`) to `GO:0052738` (`with a quinone or similar compound as acceptor`), which was the key axiom repair for EC:1.2.5.3.
- Correctly updated `GO:0043885` (`anaerobic carbon-monoxide dehydrogenase activity`) from the generic ferredoxin reaction to the precise RHEA/EC reaction with `2 oxidized [2Fe-2S]-[ferredoxin]`, `2 reduced [2Fe-2S]-[ferredoxin]`, and `2 H+`.
- Added `property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31984" xsd:anyURI` to both `GO:0008805` and `GO:0043885`, matching the human PR's provenance additions.
- Scope discipline was good: the agent left the existing xrefs and legacy synonyms untouched, and only changed the two terms named in the issue.


## Issues

- The agent did not preserve the exact previous `GO:0008805` label `carbon-monoxide oxygenase activity` as a new `BROAD` synonym. The human PR added that synonym, which is useful for searchability and distinguishes the old hyphenated label from the already-present `EXACT` synonym `carbon monoxide oxygenase activity`.
