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
failure_modes:
  - over_editing
  - under_editing
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

## Summary

This attempt (gpt-5.5 / opencode) correctly implements all six issue checkboxes and is biochemically sound (F1 0.769, balanced P=R). It diverges from gold PR #31971 in synonym handling: it demotes the menaquinone oxidoreductase synonym EXACT→NARROW (correct) but does NOT preserve the old label as a NARROW synonym (omission), and it ADDS a synonym not present in the gold — `protoporphyrinogen-IX:quinone oxidoreductase activity EXACT [EC:1.3.5.3]`. The added synonym is defensible (it is the IUBMB systematic name for EC 1.3.5.3) but is extra scope that lowers the metadiff. The score modestly under-represents quality: the core science is fully correct.

## Strengths

- All six issue checkboxes implemented correctly: EC:1.3.3.4 removed from GO:0070819, EC:1.3.5.3 + RHEA:65032 added as exactMatch, label changed to "quinone-dependent protoporphyrinogen oxidase activity", both defs rewritten to the RHEA stoichiometric forms, RHEA:62000 added to GO:0070818 as xref + def provenance (PMID:19583219 kept), term_tracker_item #31965 on both terms.
- Demoted `protoporphyrinogen-IX:menaquinone oxidoreductase activity` EXACT→NARROW with correct rationale.
- Validated RHEA IDs against the local `src/resources/rhea.rdf.gz` and ran `make travis_build` to a passing result both before and after edits — strong methodology.
- Clean scope on terms: GO:0004729 untouched.

## Issues

- Omission (under_editing): did not preserve the old label `menaquinone-dependent protoporphyrinogen oxidase activity` as a NARROW synonym, unlike the human. Broadening a term should retain the old name for annotation/search continuity.
- Scope (over_editing, defensible): added `synonym: "protoporphyrinogen-IX:quinone oxidoreductase activity" EXACT [EC:1.3.5.3]`, which the human did not. This is the correct IUBMB systematic name for EC 1.3.5.3 and is arguably an improvement, but it is beyond the issue's explicit asks and lowers precision against the gold. Defensible, not an error.
- The post-hoc "X as acceptor" naming (companion PR #31979) is correctly not attempted (not in the issue body).
