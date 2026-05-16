---
ontology: go-ontology
issue_number: 31967
pr_number: 31968
eval_repo_pr: 98
agent: std_opencode_g55
model: gpt-5.5
runtime: opencode
agent_config_tag: v9
case_type: reclassification
difficulty: medium
f1: 1.0
precision: 1.0
recall: 1.0
jaccard: 1.0
outcome: success
failure_modes: []
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

<!-- Review this eval run following analysis/instructions/review-agent-eval.md

  Source issue: https://github.com/geneontology/go-ontology/issues/31967
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/31968
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/98
  Agent config: ai4curation/go-ontology-agent-config
-->

## Summary

The agent fully and correctly resolved issue #31967: it reparented all 49 EC:1.14.14.x cytochrome-P450 monooxygenase activity terms from `GO:0016709` (EC:1.14.13.- grouping, NAD(P)H as one donor) to `GO:0016712` (EC:1.14.14.- grouping, reduced flavin or flavoprotein as one donor), and added a `term_tracker_item` provenance link to issue #31967 on every edited term. The diff is line-for-line identical to the accepted human PR #31968 (49 `is_a` swaps + 49 `term_tracker_item` additions), and the metadiff `F1=1.0` accurately represents this — there is no over- or under-statement of quality here.

## Strengths

- Correct ontological reasoning: selected `GO:0016712` as the target parent, the existing GO grouping term carrying `xref: EC:1.14.14.- {source="skos:exactMatch"}`, matching the IUBMB 2018 reclassification of cytochrome-P450 enzymes from EC sub-subclass 1.14.13 to 1.14.14. This is the substantively correct classification (the immediate electron donor to the catalytic site is the flavoprotein, not NADPH).
- Complete coverage: all 49 terms from the issue table were reparented, with no misses and no spurious extra reparents. The `is_a` change set is identical to the human PR (verified by normalized diff comparison).
- Preserved co-parentage where present: `GO:0008398` (sterol 14-demethylase activity) retained its separate `is_a: GO:0032451 ! demethylase activity`; only the incorrect oxidoreductase grouping parent was swapped.
- Followed the GO provenance convention from the agent config CLAUDE.md ("Link back to the issue you are dealing with using the `term_tracker_item`"): added `property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31967" xsd:anyURI` to all 49 stanzas in the correct format, preserving pre-existing tracker links (e.g. #30193, #22523, #28526, #21412).
- Tight scope: only `src/ontology/go-edit.obo` touched; no edits to labels, definitions, synonyms, EC/RHEA/MetaCyc xrefs, or logical definitions.
- Reported pre- and post-edit `make travis_build` validation and an explicit spot check that each of the 49 targets now has `is_a: GO:0016712` and no longer has `is_a: GO:0016709`.

## Issues

No significant issues. The agent's solution is substantively and line-for-line identical to the accepted human PR for this task.
