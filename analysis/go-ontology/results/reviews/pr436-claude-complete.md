---
ontology: go-ontology
issue_number: 31965
pr_number: 31971
eval_repo_pr: 436
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

This attempt (claude-sonnet-4.5 / copilot) actually solves the protoporphyrinogen sub-task correctly — the GO:0070818/GO:0070819 edits match the gold PR #31971 including the synonym restructuring — but it is buried in a flood of unrelated, out-of-scope changes across the entire ontology, dragging F1 to 0.333 (recall 0.208). This is a failure driven by severe scope creep / instruction violation, not by getting the target science wrong.

## Strengths

- The in-scope protoporphyrinogen edits are essentially perfect: removed `EC:1.3.3.4 {source="skos:broadMatch"}` from GO:0070819, added `EC:1.3.5.3` + `RHEA:65032` exactMatch, relabelled to "quinone-dependent protoporphyrinogen oxidase activity", rewrote both defs to the 3x RHEA forms (PMID:19583219 retained in both), added `RHEA:62000` xref to GO:0070818, demoted the menaquinone oxidoreductase synonym EXACT→NARROW AND preserved the old label as a NARROW synonym, and added `term_tracker_item` #31965 to both terms. This portion alone would have scored near 1.0 (hence precision 0.846).

## Issues

- Severe scope creep / instruction violation (the dominant problem): the diff touches numerous unrelated terms and even a different ontology file. Examples: obsoleting `GO:0019584` (galactonate catabolic process), `GO:0046180`/`GO:0046181` (ketogluconate biosynthetic/catabolic process) with `term_tracker_item` for issue **#31978** (a completely different issue); swapping CHEBI identifiers on `GO:0010828` and others (`CHEBI:37329`→`CHEBI:57795`, `CHEBI:24265`→`CHEBI:18391`, `CHEBI:60978`→...); reordering `xref: EC:` lines on unrelated reaction terms (GO:0036441, the calciol hydroxylase term); reordering `created_by`/`is_obsolete` on `GO:0140057`; and modifying `src/ontology/extensions/go-lego-edit.ofn` to replace `emapa#starts_at`/`emapa#ends_at` with `RO_0002489`/`RO_0002493`. None of this is requested by issue #31965.
- These extraneous edits appear to be the agent picking up a stale/dirty working tree or conflating multiple issues' work into one PR — a serious process failure. They massively reduce recall (0.208) against the single-purpose gold PR and would introduce risk if merged (unreviewed obsoletions, CHEBI re-grounding, relation changes).
- Net assessment: correct local solution, unacceptable delivery. The contamination makes the PR unmergeable as-is and is the defining failure mode for this run.
