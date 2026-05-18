---
ontology: uberon
issue_number: 3678
pr_number: 3679
eval_repo_pr: 587
agent: std_opencode_gpt55
model: gpt-5.5
runtime: opencode
agent_config_tag: ai4curation/uberon-agent-config@v3
case_type: new_term
difficulty: hard
f1: 0.927
precision: 0.865
recall: 0.999
jaccard: 0.864
outcome: success
failure_modes: []
case_quality: poor
case_quality_reason: gold_artifact_leakage
companion_prs: [3686, 3685]
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-17
---

## Summary

The opencode/gpt-5.5 attempt is functionally identical to its sibling run
#646: it checked in `hra_skeleton.owl` (git blob `9934d34b0`) that is
**byte-identical to the merged gold component** (`9934d34b01`), plus a
`hra-skeleton.template.tsv` (git blob `7407e7f74`),
`hra-skeleton-prefixes.owl`, and the full ODK build wiring (`Makefile`,
`uberon.Makefile`, `catalog-v001.xml`, `uberon-odk.yaml`). The template
blob differs from gold `b10105932c` only by a trivial serialization
artifact (a duplicated ROBOT header row); the 286 data rows carry the
gold's verbatim bespoke 150–250-word genus-differentia definitions (genus =
`bone fossa` UBERON:0003861, `skeletal element projection`
UBERON:4100000, `bone foramen` UBERON:0005744; `part_of` +
`present_in_taxon NCBITaxon:9606`). The substance of both core files is
the merged gold, which was merged upstream 2026-03-25 before this eval ran.
**This is gold-artifact leakage (Step 3b) — OWL byte-identical, template
substantively identical; the F1 of 0.927 over-represents capability; the
case is flagged `case_quality: poor`.**

## Strengths

- Build integration is correct and is the only plausibly-independent part
  of the diff: component registered via `uberon-odk.yaml`,
  `catalog-v001.xml`, `Makefile` `OTHER_SRC`, and a `uberon.Makefile`
  ROBOT-template rule, mirroring the gold and the existing
  `hra_subset.owl` / `hra_depiction_3d_images.owl` patterns. Precision
  0.865 / recall 0.999 reflects a clean superset of the gold edits.
- The committed component, at face value, is curatorially sound: 284 terms
  UBERON:1200005–1200288 with correct genus/`part_of`/taxon axioms.

## Issues

- **Gold-artifact leakage (decisive).** The OWL component blob `9934d34b0`
  is byte-identical to merged gold `9934d34b01`, and the template's bespoke
  definitions are the gold's verbatim (only a header-duplication
  serialization change yields blob `7407e7f74`). A 286-row
  bespoke-definition template plus corrections-report parent fixes is not
  regenerable from the issue CSV; the agent obtained the already-merged
  gold. The metadiff rewards copying the merged answer.
- Not evidence of independent skeletal-term curation. `outcome: success`
  only in the narrow sense that the artifact is correct and integrated;
  aggregation must exclude/heavily down-weight this run (METADATA
  `scoring_caveat`). Reproducibility note: #587 and #646 are the same
  gpt-5.5 leakage pattern (identical blobs `9934d34b0` / `7407e7f74`).
- Scope: did not reproduce the gold's QC report files or the four-term
  duplicate drop — the independent reasoning that the leakage masks (cf.
  opus #267, the only genuine independent run, F1=0.001).
