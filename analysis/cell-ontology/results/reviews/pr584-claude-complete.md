---
ontology: cell-ontology
issue_number: 3536
pr_number: 3537
eval_repo_pr: 584
agent: std_opencode_gpt54
model: gpt-5.4
runtime: opencode
agent_config_tag: ai4curation/cl-agent-config@v3:.
case_type: axiom_repair
difficulty: hard
f1: 0.613
precision: 0.663
recall: 0.570
jaccard: 0.442
outcome: success
failure_modes: []
case_quality: poor
case_quality_reason: gold_internally_inconsistent_and_out_of_scope
companion_prs: []
scoring_caveat: "Gold PR #3537 uses PATO:0002312 (actually 'segmented', not 'cuboidal') in its docs/DOSDP/relations_guide while using the correct PATO:0001872 (cuboid, syn. cuboidal) in the OWL axioms; gold also makes out-of-scope structural reparenting (CL_0000237, CL_0000079, CL_0000240, CL_0002063) the issue never asked for. Metadiff F1=0.613 under-represents this attempt, which is internally consistent and arguably better than gold on the cuboidal term choice."
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-17
---

## Summary

gpt-5.4/opencode addressed all four explicit asks in issue #3536 and produced the
highest-scoring attempt for this case (metadiff F1=0.613, the best of the eight). It
added the `EquivalentClasses` logical definition for squamous epithelial cell
(`CL:0000076` ≡ `CL:0000066` and `RO:0000053` some `PATO:0002254` flattened, matching
gold byte-for-byte), minted the new term `cuboidal epithelial cell` (`CL:9900001`,
same temporary ID as gold) with `EquivalentClasses(... RO:0000053 some PATO:0001872
cuboid)`, reparented `CL:0000241` (stratified cuboidal epithelial cell) under the new
class, added both DOSDP YAMLs and the `docs/patterns/*.md` companion pages plus
`overview.md`, and extended `relations_guide.md`. The reported F1 still under-represents
quality because the gold PR is internally inconsistent (its docs/DOSDP cite
`PATO:0002312` = "segmented") and makes out-of-scope structural reparenting the issue
never requested.

## Strengths

- **Squamous equivalence axiom matches gold exactly**:
  `EquivalentClasses(obo:CL_0000076 ObjectIntersectionOf(obo:CL_0000066
  ObjectSomeValuesFrom(obo:RO_0000053 obo:PATO_0002254)))` plus a mirrored text
  definition — exactly ask #2.
- **Correct, consistently-applied PATO selection.** Used `PATO:0001872` (cuboid;
  exact synonym "cuboidal") — the same term gold used in its *OWL axioms* — across the
  equivalence axiom, the per-cell axioms, the DOSDP, and the docs/`relations_guide.md`.
  Gold's documentation and `cuboidalEpithelialCell.yaml` instead cite `PATO:0002312`
  ("segmented"), a gold error this attempt avoids entirely.
- **Met ask #1 structurally**: `CL:9900001` is `EquivalentClasses` epithelial cell and
  has_characteristic some cuboid, and is correctly slotted under the hierarchy via
  reparenting `CL:0000241` (stratified cuboidal epithelial cell) from `CL:0000075` to
  `CL:9900001`. The temporary ID `CL:9900001` is from the idrange:82 "Temporary IDs"
  block (>= 9900000) — identical to gold's choice.
- **Met ask #4 most completely of all attempts**: produced both
  `src/patterns/dosdp-patterns/{squamous,cuboidal}EpithelialCell.yaml` *and* the
  `docs/patterns/{squamous,cuboidal}EpithelialCell.md` companion pages and updated
  `docs/patterns/overview.md` — the only PRs in this set (with #521) to generate the
  doc/pattern pages the gold also produced.
- **Disciplined scope on per-cell axioms (ask #3).** Added flattened/cuboidal axioms
  only to directly relevant epithelial subtypes (e.g. `CL:0000240`, `CL:0000241`,
  `CL:0002062`) rather than bulk-annotating every textual mention, with an explicit,
  defensible rationale in the PR comment.
- **Good provenance + validation**: ran `robot convert` as a parse check and correctly
  identified the reported `CL:4072022` error as pre-existing and unrelated.

## Issues

- **Per-cell axiom set differs from gold (metadiff artifact, not an error).** The
  agent's selected set of cells receiving explicit `has characteristic` axioms
  partially overlaps but is not identical to gold's. The issue gives no exact list
  ("find all cell types with squamous/cuboidal in name or definition"), so both
  readings are defensible; this is the dominant driver of recall < 1.0 and is a
  case-quality artifact.
- **Did not reproduce gold's out-of-scope structural edits** (reparenting `CL:0000237`
  to `CL:0000066`, `EquivalentClasses`/`part_of UBERON_0000486` on `CL:0000079` and
  `CL:0000240`, `CL:0002063` axiom merge). Not doing these is correct scoping for issue
  #3536; it costs recall against the metadiff only because the gold is over-scoped.
- **Minor**: trailing newline removed from `relations_guide.md`/`overview.md` (a
  no-op formatting artifact, not a substantive change).
- No correctness errors, no syntax errors, no broken axioms.
