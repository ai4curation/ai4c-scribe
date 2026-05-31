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
outcome: success
failure_modes:
  - over_editing
  - under_editing
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

## Summary

This attempt (gpt-5.5 / opencode) produced a diff identical to attempt #155 (same blob `1d10e5e`, same F1 0.769). All six issue checkboxes are implemented correctly and the science is fully sound. As with #155, it demotes the menaquinone oxidoreductase synonym EXACT→NARROW (correct) but omits preserving the old label as a NARROW synonym (omission), and adds an extra IUBMB systematic-name synonym not in gold PR #31971 (defensible over-edit). The metadiff modestly under-represents quality.

## Strengths

- All six issue checkboxes implemented correctly: removed `EC:1.3.3.4` from GO:0070819, added `EC:1.3.5.3` + `RHEA:65032` exactMatch, relabelled to "quinone-dependent protoporphyrinogen oxidase activity", rewrote both defs to the RHEA stoichiometric forms, added `RHEA:62000` to GO:0070818 as xref + def provenance (PMID:19583219 retained), term_tracker_item #31965 on both terms.
- Demoted `protoporphyrinogen-IX:menaquinone oxidoreductase activity` EXACT→NARROW with correct rationale.
- Correctly scoped to GO:0070818/GO:0070819; GO:0004729 untouched.
- Consistent, reproducible result across two opencode runs (#136 == #155), indicating stable behavior for this model/runtime.

## Issues

- Omission (under_editing): old label `menaquinone-dependent protoporphyrinogen oxidase activity` not retained as a NARROW synonym (the human kept it for annotation/search continuity after broadening).
- Scope (over_editing, defensible): added `synonym: "protoporphyrinogen-IX:quinone oxidoreductase activity" EXACT [EC:1.3.5.3]` not present in the gold. This is the correct IUBMB systematic name for EC 1.3.5.3 — arguably an improvement, but beyond the issue's explicit asks, lowering precision vs gold. Not an error.
- The PR comment for this run is much terser than #155's (no validation detail), though the underlying diff is identical. The post-hoc "X as acceptor" naming (companion PR #31979) is correctly not attempted.
