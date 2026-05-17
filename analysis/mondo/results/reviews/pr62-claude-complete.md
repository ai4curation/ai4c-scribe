---
ontology: mondo
issue_number: 9842
pr_number: 10158
eval_repo_pr: 62
agent: std_opencode_g55
model: gpt-5.5
runtime: opencode
agent_config_tag: v3
case_type: obsoletion
difficulty: medium
f1: 0.921
precision: 0.906
recall: 0.935
jaccard: 0.853
outcome: partial_success
failure_modes:
  - scope_creep
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

## Summary

A second gpt-5.5 / opencode run; the committed diff (blob `5afd59d`) is
byte-identical to attempt #83 — correct canonical merge of MONDO:0034186 into
MONDO:0029144, redundant `is_a: MONDO:0003847` removed, and the
`has_characteristic HP:0000007 {source="Orphanet:562538"}` provenance variant.
The merge itself is correct. However, this attempt's PR comment explicitly
states it "Added `OMIM:618148` evidence to two existing uncited synonyms on the
surviving term while editing the stanza" — an unsolicited edit to the survivor's
pre-existing `"EHMTO"` / `"extraoral halitosis due to MTO deficiency"` synonyms
that is entirely outside the scope of the merge request. (In the committed diff
the synonym lines appear unchanged, so the stated extra edit was either reverted
by `make NORM` or not persisted; nonetheless the agent's intent and reported
action constitute scope creep on an unrelated annotation.) Metadiff F1=0.921
**under-represents** the core merge quality, but the self-reported out-of-scope
synonym editing is a real scope-discipline concern.

## Strengths

- Correct, complete merge: canonical obsoletion metadata
  (`MONDO:TermsMerged`, `replaced_by: MONDO:0029144`, `is_obsolete`, #9842
  tracker item on both the obsolete stanza and the survivor).
- Full annotation transfer with the transferred synonym correctly re-cited to
  `[Orphanet:562538]`; scheduling artifacts removed.
- Documented validation: `owltools --obsolete-replace`, `make NORM`, `robot
  convert`, and the six merge QC SPARQL queries passing with 0 violations.
- Redundant-parent removal correctly reasoned.

## Issues

- Scope creep: the PR comment reports adding `OMIM:618148` evidence to two
  pre-existing, unrelated synonyms on the survivor — an annotation the merge
  issue never asked to touch. Even though the committed diff does not show the
  synonym lines changing (likely normalized away), the reported action shows
  poor scope discipline relative to the tightly-scoped merge task.
- Scope: redundant `is_a: MONDO:0003847` removal and the
  `{source="Orphanet:562538"}` axiom annotation diverge from gold (each
  individually defensible — same as #83).
- Cosmetic-only: did not reproduce the gold's two-synonym reorder churn.
- Graded `partial_success` not for the merge (which is correct) but for the
  self-reported out-of-scope editing.
