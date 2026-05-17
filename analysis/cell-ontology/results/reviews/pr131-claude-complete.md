---
ontology: cell-ontology
issue_number: 3239
pr_number: 3245
eval_repo_pr: 131
agent: std_opencode_gem4
model: togetherai/google/gemma-4-31B-it
runtime: opencode
agent_config_tag: ai4curation/cl-agent-config@v3
case_type: reclassification
difficulty: medium
f1: 0.333
precision: 0.227
recall: 0.625
jaccard: 0.200
outcome: partial_success
failure_modes:
  - under_editing
  - wrong_pattern
case_quality: poor
case_quality_reason: gold_incomplete_plus_serialization_noise
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-16
---

## Summary

gemma-4-31b/opencode got both reclassifications structurally right (tendon
cell → fibroblast CL_0000057 equivalence axiom; otic fibrocyte → mesenchymal
cell CL_0008019) and added both requested synonyms, but with several quality
defects: it left the stale inferred tendon cell SubClassOf pointing at the old
parent, mangled the tendon cell text definition, did not update the otic
fibrocyte definition text, and used a non-standard synonym-type annotation.
The F1 of 0.333 is in the same metadiff-depressed band as the others; here it
modestly **over-represents** relative to the cleaner Claude attempts because
the agent introduced real (not just stylistic) defects.

## Strengths

- Core ontological intent correct: `EquivalentClasses(CL_0000388
  ObjectIntersectionOf(CL_0000057 ...UBERON_0000043))` and
  `SubClassOf(CL_0002665 CL_0008019)` both match gold's substantive edits.
- Added both requested otic fibrocyte synonyms (cochlear fibrocyte
  PMID:31866825, spiral ligament fibrocyte PMID:33193034) addressing the
  issue ask the gold deferred.

## Issues

- **Wrong pattern**: synonyms added as `hasRelatedSynonym` with an extra
  `Annotation(oboInOwl:hasSynonymType obo:OMO_0003000)` (a previous-name
  synonym-type) — OMO_0003000 is not appropriate here and is not the CL
  convention for literature-attested synonyms; sibling attempts correctly
  used a plain `Annotation(hasDbXref PMID:...) hasExactSynonym/...`.
- **Under-editing**: did not update the otic fibrocyte text definition
  (left "A fibrocyte of the cochlea ..."); gold and most attempts changed
  "fibrocyte" → "mesenchymal cell". Also left the stale
  `SubClassOf(Annotation(is_inferred "true") CL_0000388 CL_0000135)` pointing
  at fibrocyte, inconsistent with the new fibroblast equivalence axiom.
- Tendon cell text definition degraded: "An elongated fibrocyte that is part
  of a tendon." → "A fibroblast that is part of a tendon." — dropped the
  "elongated" qualifier the gold and other agents preserved, a needless
  information loss.
- Did not add PMID:37720106 to the otic fibrocyte def xref despite it being
  the issue's cited reference for the reclassification.
- High recall (0.625) reflects fewer lines touched matching gold by accident,
  not superior completeness.
