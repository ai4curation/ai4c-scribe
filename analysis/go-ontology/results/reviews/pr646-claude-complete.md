---
ontology: go-ontology
issue_number: 31965
pr_number: 31971
eval_repo_pr: 646
agent: std_opencode_gpt54
model: gpt-5.4
runtime: opencode
agent_config_tag: v9
case_type: reclassification
difficulty: hard
f1: 0.294
precision: 0.769
recall: 0.182
jaccard: 0.172
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

This attempt (gpt-5.4 / opencode, blob `791d76d2a`) solves the biochemical
core of issue #31965 correctly but, unlike #603/#617, it follows the issue
**comment thread** (@pgaudet's 2026-04-27 proposal) and applies the "X as
acceptor" renaming — relabelling GO:0070819 to "protoporphyrinogen oxidase
activity, quinone as acceptor" and GO:0004729 to "protoporphyrinogen oxidase
activity, oxygen as acceptor". This deviates from the scored gold label
("quinone-dependent…", PR #31971) and pulls in companion-PR #31979 work,
lowering precision/recall vs the single-PR target (F1 0.294). On top of this
the diff carries the same large base-state-contamination block as #603/#617.
A failure on the metadiff target, with a defensible (if differently scoped)
naming judgment.

## Strengths

- Biochemical content matches gold PR #31971: removed incorrect
  `EC:1.3.3.4 {source="skos:broadMatch"}` from GO:0070819; added `EC:1.3.5.3`
  and `RHEA:65032` as `skos:exactMatch`; rewrote both defs to the 3x RHEA forms
  with RHEA def provenance (PMID:19583219 retained); added `RHEA:62000` xref +
  def provenance to GO:0070818; added `term_tracker_item` #31965 to both terms.
- GO:0070819 synonym restructuring correct: menaquinone oxidoreductase synonym
  demoted EXACT→NARROW and old label preserved as a NARROW synonym.
- The "X as acceptor" rename is itself a *correct* curation outcome — it is
  exactly what @pgaudet proposed in the issue comments and what the human later
  applied in companion PR #31979 (GO:0004729 and GO:0070819). The agent
  reasonably extended the work by reading the issue thread; the GO:0004729
  rename is consistent with the oxidoreductase naming precedent.

## Issues

- Diverges from the scored gold-PR #31971 label: gold uses
  "quinone-dependent protoporphyrinogen oxidase activity" for GO:0070819,
  whereas this attempt uses "protoporphyrinogen oxidase activity, quinone as
  acceptor". Per the case METADATA, the "X as acceptor" convention stems from a
  post-hoc reviewer comment and #31971 is the scored target, so this lowers the
  metadiff (F1 0.294 vs 0.333 for the gold-label runs #603/#617) even though
  the rename is defensible curation. It also touches GO:0004729, which gold
  #31971 does not.
- Severe base-state contamination / scope creep (dominant problem, shared with
  #603/#617): obsoleting `GO:0019584`, `GO:0046180`, `GO:0046181` tagged with
  `term_tracker_item` for the unrelated issue **#31978**; CHEBI re-grounding on
  multiple unrelated terms (`CHEBI:37329`→`CHEBI:57795`,
  `CHEBI:24265`→`CHEBI:18391`, …); reordering `xref: EC:` lines on unrelated
  reaction terms; reordering `created_by`/`is_obsolete`/`creation_date` on
  GO:0140057; and editing `src/ontology/extensions/go-lego-edit.ofn` to swap
  `emapa#starts_at`/`emapa#ends_at` for `RO_0002489`/`RO_0002493`. None
  requested by issue #31965.
- The contamination collapses recall to 0.182 and renders the PR unmergeable as
  delivered. Net: scientifically sound core plus a defensible-but-off-target
  rename, all undone by the contamination block.
