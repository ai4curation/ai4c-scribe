---
ontology: cell-ontology
issue_number: 3536
pr_number: 3537
eval_repo_pr: 521
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

gpt-5.4/opencode produced a diff byte-identical (blob `6735706`) to eval PR #584 — same
model, runtime, and result — and is one of the two top-scoring attempts for this case
(metadiff F1=0.613). It added the squamous epithelial cell `EquivalentClasses`
definition (`CL:0000076` ≡ `CL:0000066` and `RO:0000053` some `PATO:0002254`,
byte-for-byte matching gold), minted `cuboidal epithelial cell` (`CL:9900001`, same
temporary ID as gold) with `EquivalentClasses(... RO:0000053 some PATO:0001872 cuboid)`,
reparented `CL:0000241` under the new term, added both DOSDP YAMLs and the
`docs/patterns/*.md` companion pages plus `overview.md`, and extended
`relations_guide.md`. All four explicit asks of issue #3536 are met. F1=0.613
under-represents quality because the gold PR is internally inconsistent (docs/DOSDP cite
`PATO:0002312` = "segmented") and includes out-of-scope structural edits.

## Strengths

- **Squamous equivalence axiom matches gold exactly**:
  `EquivalentClasses(obo:CL_0000076 ObjectIntersectionOf(obo:CL_0000066
  ObjectSomeValuesFrom(obo:RO_0000053 obo:PATO_0002254)))` plus mirrored text
  definition — ask #2 satisfied.
- **Correct, consistently-applied PATO selection.** Used `PATO:0001872` (cuboid; exact
  synonym "cuboidal") uniformly across the equivalence axiom, per-cell axioms, DOSDP,
  and docs — avoiding the gold's `PATO:0002312` ("segmented") documentation error.
- **Met ask #1 structurally**: `CL:9900001` ≡ epithelial cell and has_characteristic
  some cuboid, with `CL:0000241` (stratified cuboidal epithelial cell) reparented from
  `CL:0000075` to `CL:9900001`. ID `CL:9900001` is from the idrange:82 "Temporary IDs"
  block — identical to gold.
- **Met ask #4 most completely**: produced both DOSDP YAMLs *and* the
  `docs/patterns/{squamous,cuboidal}EpithelialCell.md` pages and updated
  `overview.md` — matching the file set gold generated.
- **Disciplined per-cell axiom selection (ask #3)** with an explicit rationale in the
  PR comment for limiting to directly-relevant epithelial subtypes.
- **Validation**: ran `robot convert`; correctly attributed the reported
  `CL:4072022` structure error to a pre-existing, unrelated problem.

## Issues

- **Per-cell axiom set differs from gold (metadiff artifact).** The issue gives no
  exact term list; the agent's defensible reading produces a partially-overlapping but
  non-identical set, the main driver of recall < 1.0.
- **Did not reproduce gold's out-of-scope structural edits** (reparenting
  `CL:0000237`, `EquivalentClasses`/`part_of UBERON_0000486` on `CL:0000079`/`CL:0000240`,
  `CL:0002063` merge). Correct scoping for issue #3536; costs recall only because gold
  is over-scoped.
- **Minor**: trailing-newline removal in docs (no-op formatting).
- Exact duplicate of attempt #584; no independent signal. No correctness or syntax
  errors.
