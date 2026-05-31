---
ontology: go-ontology
issue_number: 31965
pr_number: 31971
eval_repo_pr: 617
agent: std_opencode_gpt54
model: gpt-5.4
runtime: opencode
agent_config_tag: v9
case_type: reclassification
difficulty: hard
f1: 0.333
precision: 0.846
recall: 0.208
jaccard: 0.200
case_quality: ok
outcome: failure
failure_modes:
  - scope_creep
  - over_editing
  - instruction_violation
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-17
---

## Summary

This attempt (gpt-5.4 / opencode) produced a diff identical to attempt #603
(same blob `1be19e9`, F1 0.333, precision 0.846, recall 0.208). The in-scope
protoporphyrinogen sub-task is solved correctly and matches gold PR #31971
(including the synonym restructuring), but the PR is contaminated with the same
large block of unrelated, out-of-scope edits. This is a reproducible failure
driven by base-state contamination / scope creep, not by getting the target
science wrong.

## Strengths

- The in-scope protoporphyrinogen edits are essentially perfect and match gold
  PR #31971: `EC:1.3.3.4 {source="skos:broadMatch"}` removed from GO:0070819;
  `EC:1.3.5.3` and `RHEA:65032` added as `skos:exactMatch`; GO:0070819
  relabelled to the literal gold label "quinone-dependent protoporphyrinogen
  oxidase activity"; both defs rewritten to the 3x RHEA forms with RHEA def
  provenance (PMID:19583219 retained in both); `RHEA:62000` added to GO:0070818;
  `term_tracker_item` #31965 added to both terms. This explains the high
  precision (0.846).
- The GO:0070819 synonym restructuring is correct: menaquinone oxidoreductase
  synonym demoted EXACT→NARROW and old label preserved as a NARROW synonym
  (ordering differs from gold but metadiff-equivalent).
- Reproducible with #603, indicating a systematic opencode/working-tree
  behavior on this case rather than a one-off.
- Did not prematurely apply the post-hoc @pgaudet "X as acceptor" rename
  (companion #31979), correctly tracking the scored gold-PR label.

## Issues

- Severe base-state contamination / scope creep (dominant problem): the same
  foreign hunk as #603 / copilot #421 / #436 — obsoleting `GO:0019584`,
  `GO:0046180`, `GO:0046181` tagged with `term_tracker_item` for the unrelated
  issue **#31978**; CHEBI re-grounding on multiple unrelated terms
  (`CHEBI:37329`→`CHEBI:57795`, `CHEBI:24265`→`CHEBI:18391`, …); reordering
  `xref: EC:` lines on unrelated reaction terms (GO:0036441, the calciol
  25-hydroxylase term); reordering `created_by`/`is_obsolete`/`creation_date`
  on the obsolete vacuole-mitochondria tethering term (GO:0140057); and editing
  `src/ontology/extensions/go-lego-edit.ofn` to swap `emapa#starts_at` /
  `emapa#ends_at` for `RO_0002489` / `RO_0002493`. None requested by issue
  #31965.
- The contamination collapses recall to 0.208 against the single-purpose gold
  and would introduce unreviewed obsoletions, CHEBI changes and relation edits
  if merged. The PR is unmergeable as delivered.
- Net: correct local solution, unacceptable delivery; the contamination is the
  defining and reproducible failure mode for this run.
