---
ontology: cell-ontology
issue_number: 3536
pr_number: 3537
eval_repo_pr: 485
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

gpt-5.5/opencode produced a diff byte-identical (blob `0e0d3a6`) to eval PR #548 — same
model, runtime, and result. It got the two core logical definitions right —
`cuboidal epithelial cell` (`CL:9900000`) ≡ epithelial cell and has_characteristic some
`PATO:0001872` (cuboid), and squamous epithelial cell `EquivalentClasses` with
`PATO:0002254` (flattened, matching gold) — but **skipped ask #4 entirely** (no DOSDP
YAMLs, no `docs/patterns/*.md`), declining on a misread of the agent config, and
bulk-added `has characteristic` axioms to far more cells than gold. The very low
metadiff F1=0.083 is partly a case-quality floor (gold internally inconsistent and
over-scoped) but here also reflects the genuine missing DOSDPs and broad over-editing.

## Strengths

- **Squamous equivalence axiom matches gold exactly**:
  `EquivalentClasses(obo:CL_0000076 ObjectIntersectionOf(obo:CL_0000066
  ObjectSomeValuesFrom(obo:RO_0000053 obo:PATO_0002254)))` plus a text definition —
  ask #2 satisfied.
- **Cuboidal logical definition is correct**: `CL:9900000` ≡ epithelial cell and
  has_characteristic some `PATO:0001872` (cuboid; syn. "cuboidal"), consistent with the
  docs — avoiding the gold's `PATO:0002312` ("segmented") error. `CL:9900000` is a
  valid temporary ID from the idrange:82 "Temporary IDs" block (off-by-one from gold's
  `CL:9900001`, but not an invalid placeholder).
- **Added provenance** to the new term (IAO:0000233 → issue #3536, `terms:creator`,
  `terms:date`); ran `robot convert` as a parse check.

## Issues

- **Missed ask #4 (DOSDPs + pattern docs).** Same misread as #548: the agent
  deliberately omitted `src/patterns` files believing the config forbade them, despite
  issue #3536 explicitly asking for DOSDPs under `src/patterns`. Genuine
  `missed_requirement`; gold and the gpt-5.4 attempts produced these files.
- **Over-editing (over_editing).** Bulk-added shape `SubClassOf` axioms to a large set
  of cells beyond gold's selection (e.g. `CL:0000312` keratinocyte, `CL:0002244`,
  `CL:0009066`, `CL:0009096`, `CL:1001575/6/7`) and reparented `CL:0005009`,
  `CL:0005010`, `CL:0002063` under `CL:9900000`. Some assertions over-state defining
  morphology; main precision sink (P=0.061), not purely a metadiff artifact.
- **Did not reparent `CL:0000241`** under the new cuboidal term, unlike gold and the
  gpt-5.4 attempts — small cuboidal-hierarchy completeness gap.
- Exact duplicate of attempt #548; no independent signal. Core definitions are sound,
  so `partial_success` despite the very low metadiff.
