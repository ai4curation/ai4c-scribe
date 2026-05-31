---
ontology: cell-ontology
issue_number: 3521
pr_number: 3583
eval_repo_pr: 298
agent: std_codex_g54
model: gpt-5.4
runtime: codex
agent_config_tag: ai4curation/cl-agent-config@v3
case_type: other
difficulty: simple
f1: 0.0
precision: 0.0
recall: 0.0
jaccard: 0.0
outcome: partial_success
failure_modes:
  - over_editing
  - scope_creep
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-17
---

## Summary

The agent added an `oboInOwl:hasDbXref` assertion annotated with
`Annotation(rdfs:label "reference transcriptomic data on Cell Annotation
Platform")` to all 13 listed bipolar neuron terms — the predicate precisely
following the curator's literal `database_cross_reference:` issue instruction
(and the original pre-renegotiation gold commit 0d637a1). However, it then
**heavily over-edited**: it rewrote all 13 `obo:IAO_0000115` textual
definitions to embed CAP prose, added 13 `obo:IAO_0000233` issue trackers, and
added per-term `rdfs:comment` annotations asserting specific NS-Forest marker
genes (MYO16, PRKCA, EBF1, COL5A1, DPP6, MEIS2, SCG2, SLC35F4, AGBL1, FEZF1,
etc.). The marker portion was explicitly blocked upstream (CellMark PR #56,
"PR needs fixing"), so injecting concrete marker-gene claims is unsourced
content the issue did not authorize. Metadiff F1=0.000 is partly the
documented poor-case artifact, but unlike the other attempts this one also has
genuine, caveat-independent quality problems.

## Strengths

- All 13 required terms identified and updated (CL_0000748, CL_0000751,
  CL_4033019, CL_4033027–CL_4033036) — complete coverage with correct CAP URL.
- The reference-link predicate `oboInOwl:hasDbXref` faithfully follows the
  curator's most explicit issue instruction (`database_cross_reference:`) and
  matches the *initial* gold commit before the in-thread renegotiation; the
  rdfs:label axiom annotation is verbatim correct.
- Transparent PR comment flagging two genuine CAP-to-CL mapping concerns
  (CL_0000748 ↔ CAP "diffuse bipolar 5"; CL_4033031 ↔ "diffuse bipolar 4"
  with DB4a/DB4b sub-distinction) — good curatorial judgment surfaced for
  review.

## Issues

- **Over-editing / scope creep (caveat-independent):** rewrote all 13
  IAO_0000115 definitions to append CAP-location prose. The issue does mention
  "extend definition text (standard pattern)", but with no pattern example, and
  the gold PR did not touch definitions — this is unilateral, large-scope text
  modification of canonical definitions.
- **Unsourced marker content:** added `rdfs:comment` marker-gene assertions
  (e.g. CL_0000751 → PRKCA, CL_4033027 → EBF1) for the NS-Forest portion that
  the issue explicitly deferred to a broken upstream CellMark PR ("@ubyndr to
  help with this bit"). Asserting specific marker genes the curators had not
  validated is a correctness risk, not just a scope issue.
- The duplicated reference link (both the embedded definition prose *and* a
  separate annotated `hasDbXref`) plus the IAO_0000233 trackers are further
  gold-absent extras.
- F1=0 reflects both the poor-case caveat and real over-editing; substantively
  this is the weakest of the five attempts reviewed — `partial_success`. See
  the case `METADATA.md` curation note for the scoring caveat.
