---
ontology: cell-ontology
issue_number: 3010
pr_number: 3225
case_type: obsoletion
difficulty: hard
num_agent_attempts: 0
agent_coverage: none
gold_assessment: sound
case_quality: poor
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-16
---

## Status

This is a **case-level review**, not an agent-attempt review. The case has
`num_agent_attempts: 0` and there is no `attempts/` directory in
`analysis/cell-ontology/cases/pr3225/`. No eval PRs were generated in
`ai4curation/eval-ont-agent-cl` for this case.

The absence of attempts is an **eval-coverage gap, not an agent failure**.
Nothing can be scored here; the deliverable is an assessment of the source
issue, the human gold PR, and dataset readiness. (Note: the `CASE_BRIEF.md`
prose claims "All three agent attempts scored 0.0 F1" — that statement is
stale/inconsistent with `num_agent_attempts: 0` and the empty case directory;
treat it as a brief-generation artifact, not evidence that attempts exist.)

## Source Issue

Issue [#3010](https://github.com/obophenotype/cell-ontology/issues/3010)
"[Obsolete] structural cell" has an **empty body** and **no comments**. The
entire specification is the title line: *"Only has 2 subclasses! Some work
needed to find new homes for these."*

This is an extremely thin issue. It names no CL ID (the target is
CL:0000293 "structural cell"), does not say what the new parent for the
orphaned subclasses should be, and gives no obsoletion-reason text. A human
curator can infer the intent from CL conventions; an agent would have to
discover the target ID, enumerate the dependent classes (CL:0000347 scleral
cell, CL:0000348 choroidal cell of the eye, and downstream CL:2000070 optic
choroid fibroblast), and decide on a reparenting target with essentially no
guidance. This thin-issue + cascade-obsoletion combination is the source of
the `hard` rating.

## Gold PR Assessment

**Step 3a (whole vs partial):** Issue #3010 was resolved by a **single
merged PR, #3225**. A search of source-repo PRs for "3010" and "structural
cell" returns one closed predecessor, **#3222** ("obsoleted structural
cell", closed 2025-08-05, same author @Caroline-99), which was superseded by
#3225 (merged 2025-08-07). There is no companion PR splitting the work; the
gold is the whole human resolution.

**Step 3b (poor-case signatures):** This case carries a clear
**gold-misattribution / issue-mismatch** signature, already recorded as
`eval_suitability: unusable` in the brief:

- The PR #3225 description states the work was done *"by manually editing the
  cl-edit.owl file related to issue **#3224**"*, and GitHub auto-linked the
  PR to #3224 (a `skos:prefLabel` MBAO import bug). The actual driving issue
  is **#3010**, evidenced only by the `IAO:0000233` tracking annotation
  pointing at issue 3010 inside the diff. An agent prompted with #3224 cannot
  produce this diff; an agent prompted with the (near-empty) #3010 has almost
  no signal. Either way the metadiff target is unreachable by construction.

**Gold soundness (substance):** The gold edit itself is **sound and
exemplary** for a CL obsoletion cascade:

- CL:0000293 obsoleted correctly: `owl:deprecated true`, "OBSOLETE." prefix
  prepended to the IAO:0000115 definition, `rdfs:label` → "obsolete
  structural cell", `rdfs:comment` "Unsustainable grouping term.",
  `IAO:0000233` tracking link to issue 3010, and the `SubClassOf CL:0000000`
  parent axiom removed (dangling-parent cleanup is correct for an obsolete).
- Cascade repair: CL:0000347 (scleral cell) and CL:0000348 (choroidal cell
  of the eye) equivalence axioms rewired from `CL_0000293` to `CL_0000000`
  (cell); CL:0000348's textual definition edited from "A structural cell
  that is part of optic choroid" → "A cell that is part of optic choroid".
- The `#gogoeditdiff` classified-diff comment shows a further downstream
  effect on CL:2000070 (optic choroid fibroblast) reparenting — handled at
  the classified level, consistent and correct.

The edit is approved-first-time and ontologically clean. The problem is
**not** the gold's correctness but the issue/PR linkage, which makes this an
unreliable scoring reference.

## Recommendation

- Keep `agent_coverage: none` — eval-coverage gap, not agent failure. If this
  case is ever run, it must be run with the **correct driving issue (#3010)**,
  not the auto-linked #3224, and even then the near-empty issue body makes a
  faithful metadiff match against #3225 implausible. Recommend this case be
  **excluded or heavily down-weighted** in any agent aggregate (consistent
  with the existing `eval_suitability: unusable` flag).
- The gold itself is a good *example* of cascade obsoletion and could be
  retained for qualitative/pedagogical use, but not for quantitative scoring.
- Carrying `case_quality: poor` (issue-mismatch + thin near-empty issue +
  single-PR with unreachable metadiff target).
