---
ontology: go-ontology
issue_number: 31965
pr_number: 31971
eval_repo_pr: 656
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

This attempt (gpt-5.4 / opencode) produced a diff identical to attempt #646
(same blob `791d76d2a`, F1 0.294, precision 0.769, recall 0.182). The
biochemical core of issue #31965 is solved correctly, but the agent followed
the issue **comment thread** and applied the "X as acceptor" renaming
(GO:0070819 → "protoporphyrinogen oxidase activity, quinone as acceptor";
GO:0004729 → "protoporphyrinogen oxidase activity, oxygen as acceptor"),
diverging from the scored gold label in PR #31971 and pulling in companion-PR
#31979 work. The diff also carries the same large base-state-contamination
block as #603/#617/#646. A reproducible failure on the metadiff target with a
defensible naming judgment.

## Strengths

- Biochemical content matches gold PR #31971: incorrect
  `EC:1.3.3.4 {source="skos:broadMatch"}` removed from GO:0070819;
  `EC:1.3.5.3` and `RHEA:65032` added as `skos:exactMatch`; both defs rewritten
  to the 3x RHEA forms with RHEA def provenance (PMID:19583219 retained);
  `RHEA:62000` added to GO:0070818; `term_tracker_item` #31965 added to both
  terms; menaquinone oxidoreductase synonym demoted EXACT→NARROW with old label
  preserved as a NARROW synonym.
- The PR/issue comments show explicit, well-reasoned methodology: the agent
  noted the issue-body xref/def changes were already present in the eval
  checkout and that the remaining work was the agreed label rename, citing the
  oxidoreductase "X as acceptor" naming precedent — this matches @pgaudet's
  comment and the human's companion PR #31979 (correct curation in isolation).
- Reproducible with #646, indicating systematic behavior rather than a one-off.

## Issues

- Diverges from the scored gold-PR #31971 label (gold:
  "quinone-dependent protoporphyrinogen oxidase activity"; this attempt:
  "protoporphyrinogen oxidase activity, quinone as acceptor") and additionally
  edits GO:0004729, which #31971 does not. Per the case METADATA the "X as
  acceptor" convention is post-hoc (#31979) and #31971 is the scored target, so
  this lowers F1 to 0.294 versus 0.333 for the gold-label runs even though the
  rename is defensible.
- Severe base-state contamination / scope creep (dominant problem, shared with
  #603/#617/#646): obsoleting `GO:0019584`, `GO:0046180`, `GO:0046181` tagged
  with `term_tracker_item` for the unrelated issue **#31978**; CHEBI
  re-grounding on multiple unrelated terms (`CHEBI:37329`→`CHEBI:57795`,
  `CHEBI:24265`→`CHEBI:18391`, …); reordering `xref: EC:` lines on unrelated
  reaction terms; reordering `created_by`/`is_obsolete`/`creation_date` on
  GO:0140057; and editing `src/ontology/extensions/go-lego-edit.ofn` to swap
  `emapa#starts_at`/`emapa#ends_at` for `RO_0002489`/`RO_0002493`. None
  requested by issue #31965.
- The contamination collapses recall to 0.182 and renders the PR unmergeable as
  delivered. Net: scientifically sound core plus a defensible-but-off-target
  rename, undone by the reproducible contamination block.
