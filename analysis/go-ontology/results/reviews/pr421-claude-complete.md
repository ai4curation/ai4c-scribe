---
ontology: go-ontology
issue_number: 31965
pr_number: 31971
eval_repo_pr: 421
agent: std_copilot_son45
model: claude-sonnet-4.5
runtime: copilot
agent_config_tag: v9
case_type: reclassification
difficulty: hard
f1: 0.333
precision: 0.846
recall: 0.208
jaccard: 0.200
outcome: failure
failure_modes:
  - scope_creep
  - over_editing
  - instruction_violation
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

## Summary

This attempt (claude-sonnet-4.5 / copilot) produced a diff identical to attempt #436 (same blob `1be19e9`, F1 0.333, recall 0.208). The protoporphyrinogen sub-task is solved correctly and matches gold PR #31971 (including the synonym restructuring), but the PR is contaminated with a large set of unrelated, out-of-scope edits. This is a reproducible failure driven by scope creep / instruction violation, not by getting the target science wrong.

## Strengths

- The in-scope protoporphyrinogen edits are essentially perfect and match the gold: EC:1.3.3.4 removed from GO:0070819, EC:1.3.5.3 + RHEA:65032 added as exactMatch, label changed to "quinone-dependent protoporphyrinogen oxidase activity", both defs rewritten to the 3x RHEA forms (PMID:19583219 retained in both), RHEA:62000 added to GO:0070818, menaquinone oxidoreductase synonym demoted EXACT→NARROW and old label preserved as a NARROW synonym, term_tracker_item #31965 on both terms. This explains the high precision (0.846).
- Reproducible: identical to run #436, indicating the contamination is a systematic copilot-runtime/working-tree behavior on this case rather than a one-off.

## Issues

- Severe scope creep / instruction violation (dominant problem): same extraneous edits as #436 — obsoleting `GO:0019584`, `GO:0046180`, `GO:0046181` with `term_tracker_item` for the unrelated issue **#31978**; CHEBI re-grounding on multiple unrelated terms (`CHEBI:24265`→`CHEBI:18391`, `CHEBI:37329`→`CHEBI:57795`, etc.); reordering `xref: EC:` lines on unrelated reaction terms; reordering `created_by`/`is_obsolete` on `GO:0140057`; and editing `src/ontology/extensions/go-lego-edit.ofn` to swap `emapa#starts_at/ends_at` for `RO_0002489/RO_0002493`. None requested by issue #31965.
- The PR is unmergeable as delivered and would introduce unreviewed obsoletions, CHEBI changes, and relation edits if applied. Recall collapses to 0.208 against the single-purpose gold.
- Net: correct local solution, unacceptable delivery; the contamination is the defining failure mode and is reproducible across runs.
