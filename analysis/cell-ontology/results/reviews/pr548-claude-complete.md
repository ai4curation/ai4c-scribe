---
ontology: cell-ontology
issue_number: 3536
pr_number: 3537
eval_repo_pr: 548
agent: std_opencode_gpt55
model: gpt-5.5
runtime: opencode
agent_config_tag: ai4curation/cl-agent-config@v3:.
case_type: axiom_repair
difficulty: hard
f1: 0.083
precision: 0.061
recall: 0.128
jaccard: 0.043
outcome: partial_success
failure_modes:
  - missed_requirement
  - over_editing
case_quality: poor
case_quality_reason: gold_internally_inconsistent_and_out_of_scope
companion_prs: []
scoring_caveat: "Gold PR #3537 uses PATO:0002312 (actually 'segmented', not 'cuboidal') in its docs/DOSDP/relations_guide while using the correct PATO:0001872 in the OWL axioms, and makes out-of-scope structural reparenting the issue never asked for. F1=0.083 is a floor partly inflated by the gold's defects, but this attempt also genuinely missed ask #4 (no DOSDP files) and bulk-axiomatized far more cells than gold."
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-17
---

## Summary

gpt-5.5/opencode got the two core logical definitions right but only partially resolved
issue #3536. It minted `cuboidal epithelial cell` (`CL:9900000`) with the correct
`EquivalentClasses(... RO:0000053 some PATO:0001872 cuboid)` and gave squamous
epithelial cell the requested `EquivalentClasses` with `PATO:0002254` (flattened,
matching gold). However it **skipped ask #4 entirely** — no DOSDP YAMLs and no
`docs/patterns/*.md` pages — explicitly declining on a misread of the agent config as
forbidding `src/patterns` edits, and it bulk-added `has characteristic` axioms to a
much larger set of cells than gold. The very low metadiff F1=0.083 is partly a
case-quality floor (the gold is internally inconsistent and over-scoped) but here it
also reflects genuine gaps: the missing DOSDPs and broad over-editing.

## Strengths

- **Squamous equivalence axiom matches gold exactly**:
  `EquivalentClasses(obo:CL_0000076 ObjectIntersectionOf(obo:CL_0000066
  ObjectSomeValuesFrom(obo:RO_0000053 obo:PATO_0002254)))` plus a text definition —
  ask #2 satisfied.
- **Cuboidal logical definition is correct**: `CL:9900000` ≡ epithelial cell and
  has_characteristic some `PATO:0001872` (cuboid; syn. "cuboidal"), used consistently
  with the docs — avoiding the gold's `PATO:0002312` ("segmented") error. `CL:9900000`
  is in the idrange:82 "Temporary IDs" block, so it is a valid (if off-by-one from
  gold's `CL:9900001`) temporary ID, not an invalid placeholder.
- **Added provenance** to the new term (IAO:0000233 → issue #3536, `terms:creator`,
  `terms:date`).
- **Verified PATO terms in OLS before use** (per PR comment) and ran `robot convert`
  as a parse check.

## Issues

- **Missed ask #4 (DOSDPs + pattern docs).** The PR comment states the agent
  deliberately did not add `src/patterns` files because it believed "the local
  repository instructions restrict edits to `src/ontology/cl-edit.owl` and `docs/`".
  This is a misread — issue #3536 explicitly asks "Add DOSDPs for both patterns under
  src/patterns" — and is a genuine `missed_requirement`. Gold and the gpt-5.4 attempts
  (#584/#521/#591) all produced the DOSDP files.
- **Over-editing (over_editing).** Bulk-added `has characteristic some PATO:0002254/
  PATO:0001872` `SubClassOf` axioms to a large set of cells well beyond gold's
  selection — e.g. `CL:0000312` (keratinocyte), `CL:0002244`, `CL:0009066`,
  `CL:0009096`, `CL:1001575`, `CL:1001576`, `CL:1001577`, plus reparenting
  `CL:0005009`/`CL:0005010` and `CL:0002063` under `CL:9900000`. Several of these (e.g.
  asserting flattened on the broad keratinocyte class) over-state defining morphology
  and would mostly be inferred rather than asserted; this is the main precision sink
  (P=0.061) and not purely a metadiff artifact.
- **Did not reparent `CL:0000241`** (stratified cuboidal epithelial cell) under the new
  cuboidal term, unlike gold and the gpt-5.4 attempts — a small completeness gap on the
  cuboidal hierarchy.
- Core squamous/cuboidal definitions are sound, so this is `partial_success`, not a
  failure, despite the very low metadiff.
