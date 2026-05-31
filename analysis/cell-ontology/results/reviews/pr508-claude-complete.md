---
ontology: cell-ontology
issue_number: 3382
pr_number: 3440
eval_repo_pr: 508
agent: std_opencode_g54
model: gpt-5.4
runtime: opencode
agent_config_tag: ai4curation/cl-agent-config@v3
case_type: axiom_repair
difficulty: simple
f1: 0.667
precision: 1.000
recall: 0.500
jaccard: 0.500
outcome: success
failure_modes: []
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-17
---

## Summary

gpt-5.4 (opencode) produced the exactly correct core fix for issue #3382:
`BFO_0000051` (has_part) → `RO_0002104` (has_plasma_membrane_part) for
`PR_000001207` (CXCR3) in the `EquivalentClasses` axiom of CL:0001041
(CD8-positive, CXCR3-positive, alpha-beta regulatory T cell). The issue-relevant
hunk is byte-identical to the gold human change. The metadiff F1=0.667
(precision=1.000, recall=0.500) **severely under-represents** quality: the only
divergence from gold is an end-of-file serialization artifact — the run
rewrote the file's terminal `)` to add a trailing newline (`\ No newline at
end of file` removed), producing a spurious second hunk on the unrelated
trailing axiom region (CL:0000164 / CL:0000031) with zero ontological effect.
This is the same EOF-normalization artifact seen in the codex sibling run
(#76) for this case.

## Strengths

- Correct, precisely scoped relation substitution on the CXCR3 conjunct: the
  genus `CL_0000795` and the three `RO_0002215` GO restrictions
  (GO:0032613, GO:0032689, GO:0042130) are untouched, exactly matching the
  gold edit on that line.
- Correctly treated the issue's "Additional Note" list of other PR terms
  (PR_000001858, PR_000001859, PR_000007597, PR_000010543, PR_000001944,
  PR_000003457, PR_000003460) as out of scope — the issue itself framed it
  as a question for consideration, and the human PR did not touch those
  terms. Good scope discipline.
- Tightly scoped to the single intended file (`src/ontology/cl-edit.owl`).

## Issues

- Serialization artifact (not substantive): the run added a trailing newline
  at the end of `cl-edit.owl`, producing a second diff hunk on unrelated
  trailing axioms. No ontological impact, but it is the entire reason
  F1 < 1.0 and recall = 0.500. Ideally the agent would preserve the file's
  existing (no terminal EOL) formatting to avoid spurious diff noise.
- This attempt (no PR comment captured) provides less methodology evidence
  than sibling run #568, but the resulting diff is identical and correct.
