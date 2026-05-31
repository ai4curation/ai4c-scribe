---
ontology: go-ontology
issue_number: 31965
pr_number: 31971
eval_repo_pr: 603
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

This attempt (gpt-5.4 / opencode) correctly solves the in-scope protoporphyrinogen
sub-task — the GO:0070818 / GO:0070819 edits match gold PR #31971 including the
synonym restructuring — but the PR is buried in a large block of unrelated,
out-of-scope edits (the same base-state-contamination block seen in the
copilot runs #421/#436, blob `1be19e9`). Recall collapses to 0.208 and F1 to
0.333; the metadiff under-represents the science quality but correctly flags an
unmergeable, contaminated delivery. This is a failure driven by scope
creep / contamination, not by getting the target biochemistry wrong.

## Strengths

- The in-scope protoporphyrinogen edits are essentially perfect and match gold
  PR #31971: removed the incorrect `EC:1.3.3.4 {source="skos:broadMatch"}` from
  GO:0070819; added `EC:1.3.5.3` and `RHEA:65032` as `skos:exactMatch` xrefs;
  relabelled GO:0070819 to "quinone-dependent protoporphyrinogen oxidase
  activity" (the literal gold label); rewrote its def to "protoporphyrinogen IX
  + 3 a quinone = protoporphyrin IX + 3 a quinol." with `RHEA:65032` def
  provenance; added `RHEA:62000` xref + def provenance to GO:0070818 and
  rewrote its def to the 3x acceptor stoichiometry; retained PMID:19583219 in
  both defs; added `term_tracker_item` #31965 to both terms. This explains the
  high precision (0.846).
- The discriminating curation subtlety is handled correctly: the
  `protoporphyrinogen-IX:menaquinone oxidoreductase activity` synonym is demoted
  EXACT→NARROW and the old label "menaquinone-dependent protoporphyrinogen
  oxidase activity" is preserved as a NARROW synonym (synonym ordering differs
  from gold but both are present and metadiff-equivalent).
- Stayed with the gold-PR #31971 label ("quinone-dependent...") rather than
  prematurely applying the post-hoc @pgaudet "X as acceptor" convention
  (companion #31979) — correct given the scored target.

## Issues

- Severe base-state contamination / scope creep (dominant problem): the diff
  carries the same large foreign hunk as the copilot #421/#436 runs —
  obsoleting `GO:0019584` (galactonate catabolic process), `GO:0046180`,
  `GO:0046181` (ketogluconate biosynthetic/catabolic) tagged with
  `term_tracker_item` for the unrelated issue **#31978**; CHEBI re-grounding on
  multiple unrelated terms (`CHEBI:37329`→`CHEBI:57795`,
  `CHEBI:24265`→`CHEBI:18391`, `CHEBI:60978`→…); reordering `xref: EC:` lines on
  unrelated reaction terms (GO:0036441, the calciol 25-hydroxylase term);
  reordering `created_by`/`is_obsolete`/`creation_date` on the obsolete
  vacuole-mitochondria tethering term (GO:0140057); and editing
  `src/ontology/extensions/go-lego-edit.ofn` to swap `emapa#starts_at` /
  `emapa#ends_at` for `RO_0002489` / `RO_0002493`. None of this is requested by
  issue #31965.
- These extraneous edits collapse recall to 0.208 against the single-purpose
  gold PR and would introduce unreviewed obsoletions, CHEBI changes and
  relation edits if merged. The PR is unmergeable as delivered.
- Net: correct local solution, unacceptable delivery; the contamination is the
  defining failure mode, mirroring the copilot runs on this case.
