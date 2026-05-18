---
ontology: cell-ontology
issue_number: 3536
pr_number: 3537
eval_repo_pr: 591
agent: std_codex_gpt54
model: gpt-5.4
runtime: codex
agent_config_tag: ai4curation/cl-agent-config@v3:.
case_type: axiom_repair
difficulty: hard
f1: 0.344
precision: 0.265
recall: 0.491
jaccard: 0.208
outcome: success
failure_modes: []
case_quality: poor
case_quality_reason: gold_internally_inconsistent_and_out_of_scope
companion_prs: []
scoring_caveat: "Gold PR #3537 uses PATO:0002312 (actually 'segmented', not 'cuboidal') in its docs/DOSDP/relations_guide while using the correct PATO:0001872 (cuboid, syn. cuboidal) in the OWL axioms; gold also makes out-of-scope structural reparenting (CL_0000237, CL_0000079, CL_0000240, CL_0002063) the issue never asked for. Metadiff F1=0.344 substantially under-represents this attempt, which met all four explicit asks with internally-consistent, reasoner-safe axioms."
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-17
---

## Summary

gpt-5.4/codex met all four explicit asks of issue #3536 with internally consistent
axioms, but its metadiff F1 of 0.344 substantially under-represents the quality. It
minted `cuboidal epithelial cell` (`CL:9900001`, same temporary ID as gold) with
`EquivalentClasses(... RO:0000053 some PATO:0001872 cuboid)` and `SubClassOf CL:0000075`
(columnar/cuboidal epithelial cell), gave squamous epithelial cell the requested
`EquivalentClasses` definition with `PATO:0002254` (flattened, matching gold), added
per-cell shape axioms to a defensibly-selected set of squamous/cuboidal-named subtypes,
extended `relations_guide.md`, and added both DOSDP YAMLs. The low score reflects the
gold's internal inconsistency (docs/DOSDP cite `PATO:0002312` = "segmented") and
out-of-scope structural edits, not agent errors — though it did omit the
`docs/patterns/*.md` companion pages.

## Strengths

- **Squamous equivalence axiom matches gold exactly**:
  `EquivalentClasses(obo:CL_0000076 ObjectIntersectionOf(obo:CL_0000066
  ObjectSomeValuesFrom(obo:RO_0000053 obo:PATO_0002254)))` — ask #2 satisfied.
- **Met ask #1 correctly**: `CL:9900001` ≡ epithelial cell and has_characteristic some
  cuboid (`PATO:0001872`), plus `SubClassOf(obo:CL_9900001 obo:CL_0000075)` — exactly
  the parenting the issue specified. Provenance added (IAO:0000233 → issue #3536,
  `terms:creator`, `terms:date`, text definition). Temporary ID from idrange:82.
- **Correct, consistent PATO selection.** Used `PATO:0001872` (cuboid; syn. "cuboidal")
  everywhere — axioms, DOSDP, and `relations_guide.md` — avoiding the gold's
  `PATO:0002312` ("segmented") doc error. The DOSDP YAMLs correctly read
  `'epithelial cell' and ('has characteristic' some 'cuboid')`.
- **Disciplined, well-reasoned per-cell selection (ask #3).** Explicitly excluded
  variable/comparative morphology cells and declined to axiomatize the deliberately
  broader `CL:0000075` ("columnar/cuboidal epithelial cell") — sound ontological
  judgment. Overlaps with gold's set on `CL:0002653`, `CL:4033084`, `CL:0002662`,
  `CL:0002190`, `CL:0002221`, `CL:0002224`.
- **Met ask #4 (DOSDP half)**: added
  `src/patterns/dosdp-patterns/{squamous,cuboidal}EpithelialCell.yaml`.
- **Validation**: ran `robot convert` successfully and `yaml.safe_load` on both
  pattern files; also fixed the missing trailing newline / final `)` in
  `cl-edit.owl` cleanly.

## Issues

- **Omitted the `docs/patterns/*.md` companion pages** that the gold (and the
  opencode/gpt-5.4 attempts #584/#521) generated. The DOSDP YAMLs and
  `relations_guide.md` carry the equivalent guidance, so the substantive
  documentation ask is met, but this is a small completeness gap vs. gold and a
  contributor to lower recall.
- **Per-cell axiom set differs from gold (metadiff artifact).** Defensible reading of
  an under-specified ask; main driver of recall < 1.0 alongside the gold's
  out-of-scope structural edits, which the agent correctly did not reproduce.
- **Slightly terser `relations_guide.md` prose** than gold's dedicated "Recording
  cell shape" subsection (inlined into the existing morphology paragraph). Valid
  style difference.
- No correctness errors, no syntax errors, no broken axioms.
