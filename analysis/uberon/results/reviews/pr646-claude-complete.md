---
ontology: uberon
issue_number: 3678
pr_number: 3679
eval_repo_pr: 646
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

The opencode/gpt-5.5 attempt checked in `hra_skeleton.owl` (git blob
`9934d34b0`) that is **byte-identical to the merged gold component**
(`9934d34b01`), plus a `hra-skeleton.template.tsv` (git blob `7407e7f74`),
`hra-skeleton-prefixes.owl`, and the full ODK build wiring
(`uberon-odk.yaml`, `catalog-v001.xml`, `Makefile`, `uberon.Makefile`).
The template TSV blob differs from gold `b10105932c`, but on inspection it
is the **same 286-line file carrying the same bespoke 150–250-word
genus-differentia definitions** as gold (e.g. UBERON:1200005
"acromial process of scapula" with its full definition, genus
`UBERON:4100000` skeletal element projection, `part_of` UBERON:0006849,
`present_in_taxon NCBITaxon:9606`); the only difference is a trivial
serialization artifact (a duplicated ROBOT header row), which also explains
the marginally lower F1 (0.927 vs 0.928) versus the gpt-5.4 runs. The
substance of both core files is the merged gold. Gold PR #3679 merged
upstream 2026-03-25 before this eval ran. **This is gold-artifact leakage
(Step 3b) — the OWL component byte-identical, the template substantively
identical; the F1 over-represents capability; the case is flagged
`case_quality: poor`.**

## Strengths

- Build integration is correct and is the only plausibly-independent part
  of the diff: the component is registered via `uberon-odk.yaml`,
  `catalog-v001.xml`, `Makefile` `OTHER_SRC`, and a `uberon.Makefile`
  ROBOT-template rule, mirroring the gold and the existing
  `hra_subset.owl` / `hra_depiction_3d_images.owl` patterns. The agent's
  PR comment documents ROBOT validation of the template/component and OBO
  re-serialization.
- The agent disclosed that "the issue thread indicated that a ROBOT
  template had already been generated" and that it ported "the generated
  template/component available in the evaluation workspace" — honest
  acknowledgement of the pre-existing artifact rather than a claim of
  independent synthesis.
- The committed component, at face value, is curatorially sound: 284 terms
  UBERON:1200005–1200288 with correct genus/`part_of`/taxon axioms.

## Issues

- **Gold-artifact leakage (decisive).** The OWL component blob `9934d34b0`
  is byte-identical to merged gold `9934d34b01`, and the template's bespoke
  per-row definitions are the gold's verbatim (only a header-duplication
  serialization difference changes the blob hash to `7407e7f74`). A 286-row
  template of unique 150–250-word definitions plus corrections-report
  parent fixes is not regenerable from the CSV; the agent obtained the
  already-merged gold. The metadiff rewards copying the merged answer.
- Not evidence of independent skeletal-term curation. `outcome: success`
  only in the narrow sense that the artifact is correct and integrated;
  aggregation must exclude/heavily down-weight (METADATA `scoring_caveat`).
- Scope: did not reproduce the gold's QC report files
  (`corrections_report.md`, `duplicate_candidates_report.md`,
  `term_mapping_table.md`) or the four-term duplicate drop — the
  independent reasoning that the leakage masks.
