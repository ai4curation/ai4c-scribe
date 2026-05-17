---
ontology: mondo
issue_number: 9826
pr_number: 10142
eval_repo_pr: 164
agent: std_codex_g54
model: gpt-5.4
runtime: codex
agent_config_tag: v3
case_type: obsoletion
difficulty: simple
f1: 0.872
precision: 0.773
recall: 1.0
jaccard: 0.773
outcome: success
failure_modes: []
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

## Summary

gpt-5.4 via codex produced a final blob (`9e11f82`) byte-identical to the claude-opus-4.7 run (#393): F1 0.872, precision 0.773, recall 1.000. The merge of MONDO:0008549 into MONDO:0979242 is fully correct — obsoleted stanza reduced to the canonical gold six lines, survivor enriched with the corrected `[OMIM:187750]` synonym, both transferred xrefs with correct precision qualifiers, `is_a: MONDO:0003847`, and the MalaCards resource. The F1 gap from the top gpt-5.5 run is entirely the single duplicate `property_value: IAO:0000233 .../9826` line on the survivor that this run did not add, plus the human's out-of-scope `def:`/`intersection_of` enrichment. The metadiff under-represents quality; this is a correct merge.

## Strengths

- Obsoleted MONDO:0008549 stanza matches gold exactly: `IAO:0000231 MONDO:TermsMerged`, retained issue link, `is_obsolete: true`, `replaced_by: MONDO:0979242`; scheduling metadata (`obsoletion_candidate`, comment, `IAO:0006012`) correctly stripped.
- Synonym evidence correctly repaired to `[OMIM:187750]`, matching gold and avoiding the owltools `[MONDO:0008549]` self-citation.
- Xrefs `MESH:C566063 {source="MONDO:equivalentTo"}` and `OMIM:187750 {source="MONDO:equivalentObsolete"}` transferred with correct precision qualifiers, identical to gold.
- Retained `is_a: MONDO:0003847` "hereditary disease" on the survivor as gold did.
- Excellent documented methodology, the strongest of the claude/codex-style writeups here: `make NORM`, six targeted merge QC SPARQL queries via `robot verify` (qc-misused-replaced-by, qc-obsoletion-reason, qc-deprecated-class-reference, qc-xref-without-precision, qc-duplicate-exact-synonym-no-abbrev, qc-proxy-merge-missing-preferred) all 0 violations, plus an explicit verification checklist (no stray `alt_id`, no MONDO:0008549 references outside the obsolete stanza, no duplicate survivor synonym text).

## Issues

- Minor omission: did not add the survivor's duplicate `property_value: IAO:0000233 .../issues/9826` line — the sole difference from the gpt-5.5/codex top run. Redundant provenance (already on the obsoleted stanza); defensible and arguably cleaner, but costs metadiff precision.
- Omission of `def:` and `intersection_of` — the human's curatorial enrichment, out of scope for a merge request; correctly conservative.
- No errors, no scope creep, no syntax problems. Outcome set to `success`: a correct, well-validated merge whose only divergence from the best attempt is one redundant provenance line.
