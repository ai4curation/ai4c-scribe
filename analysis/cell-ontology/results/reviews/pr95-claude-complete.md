---
ontology: cell-ontology
issue_number: 3379
pr_number: 3444
eval_repo_pr: 95
agent: std_claude_haiku45
model: claude-haiku-4.5
runtime: claude
agent_config_tag: ai4curation/cl-agent-config@v3
case_type: reclassification
difficulty: simple
f1: 0.500
precision: 0.500
recall: 0.500
jaccard: 0.333
outcome: partial_success
failure_modes:
  - over_editing
  - wrong_pattern
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-16
---

## Summary

The agent got the headline change right — it replaced genus `obo:CL_0000990`
with `obo:CL_0002465` in the `EquivalentClasses` axiom for CL:0000999, as the
issue and gold PR #3444 require. However, in the same edit it **also deleted the
differentia restriction `ObjectSomeValuesFrom(obo:CL_4030046 obo:PR_000001084)`**
and justified this in the PR comment as removing a "redundant CD11b marker". That
rationale is factually wrong: in this axiom `CL_4030046` is `lacks_plasma_
membrane_part` and `PR_000001084` is "T-cell surface glycoprotein CD8 alpha
chain", so the deleted restriction means "lacks CD8-alpha", not CD11b. This is a
genuine semantic loss, and it is why precision drops to 0.500. The metadiff F1 of
0.500 here **accurately** reflects a real defect, unlike the other five attempts.

## Strengths

- The required genus substitution `CL_0000990` → `CL_0002465` was applied
  correctly in the equivalence axiom.
- Kept the asserted `SubClassOf(obo:CL_0000999 obo:CL_0002465)` line (matches
  gold) and did not touch any other class — scope was otherwise tight.
- The PR comment correctly identifies the `CL_0002454` precedent and that
  `CL_0002465` is a subclass of `CL_0000990`.

## Issues

- **Error (semantic loss):** deleted
  `ObjectSomeValuesFrom(obo:CL_4030046 obo:PR_000001084)` from the equivalence
  axiom. `CL_4030046` = `lacks_plasma_membrane_part`, `PR_000001084` =
  T-cell surface glycoprotein CD8 alpha chain. The agent removed the
  "lacks CD8-alpha-chain" differentia, weakening the necessary-and-sufficient
  definition of CD4+ CD11b+ DC. The gold PR preserved every differentia and
  changed only the genus.
- **Wrong rationale (hallucination):** the PR comment claims the removed
  conjunct is a "redundant CD11b marker" already encoded in `CL_0002465`. This
  misreads the axiom. The genuinely-redundant marker here is CD11b
  (`RO_0002104 some PR_000001012`), which is *not even present* in CL:0000999's
  axiom; the agent instead deleted an unrelated CD8-alpha restriction. The
  reasoning that motivated the edit is incorrect.
- **Over-editing:** even setting aside the bad rationale, removing a differentia
  was never requested by the issue (a pure genus swap) and was not done by any
  other attempt or the human. Precision/recall of 0.500/0.500 correctly captures
  that the diff both omits gold's exact line and adds an unwanted deletion.
