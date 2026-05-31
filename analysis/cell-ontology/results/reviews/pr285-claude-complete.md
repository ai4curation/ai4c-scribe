---
ontology: cell-ontology
issue_number: 3500
pr_number: 3570
eval_repo_pr: 285
agent: gpt-5.4-codex
model: gpt-5.4
runtime: codex
agent_config_tag: ai4curation/cl-agent-config@v3
case_type: other
difficulty: simple
case_quality: ok
case_quality_reason: gold_renegotiated_term_tracker_in_pr_comments
f1: 0.667
precision: 1.000
recall: 0.500
jaccard: 0.500
outcome: success
failure_modes: []
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-17
---

## Summary

The agent added exactly the two bare, unannotated `SubClassOf` axioms the gold
PR landed — `SubClassOf(obo:CL_0002423 ObjectSomeValuesFrom(obo:RO_0002162
obo:NCBITaxon_10090))` and the equivalent for `CL_0002424` — fully and
correctly resolving issue #3500. This is the **best of the 5 reviewed attempts**:
it matches the merged gold's curator-renegotiated form (no `term_tracker_item`)
verbatim, and notably refrained from adding the `IAO_0000233`/term-tracker
provenance even though the agent config instructs it to. F1=0.667 (P=1.0,
R=0.5) **under-represents** the quality: the only recall loss is a
serialization artifact — the run also converted the file's missing final
newline (`\ No newline at end of file` → trailing `)` + newline), a
robot-convert-style churn line absent from the gold human diff.

## Strengths

- Ontological content is byte-identical to gold for both axioms: correct
  relation (`RO_0002162`, in taxon), correct target (`NCBITaxon_10090`, Mus
  musculus), both target terms (CL_0002423 DN2a, CL_0002424 DN2b), valid OWL
  functional syntax, conventional placement after the `is_inferred` SubClassOf.
- Precision 1.0 — every gold line reproduced; no spurious ontology edits.
- Correctly chose the *bare* axiom form, matching the gold curator preference
  (RiveraAndrea83 had the gold agent strip term-tracker annotations). It
  explicitly reasoned to "keep the issue-focused fix small," landing on the
  conservative form that #190/#199 and the four opencode runs missed.
- Transparent methodology: documented checklist, attempted `robot convert`
  syntax validation (robot unavailable in env), confirmed pattern against
  existing mouse-restricted CL terms.

## Issues

- Recall halved purely by the trailing-newline / serialization churn hunk at
  EOF (line ~35780). This is not an ontology error — it is a metadiff
  serialization artifact, not a curation defect. (Whether `robot convert`
  actually ran is unclear since the agent reported robot unavailable; the
  newline normalization nonetheless appears in the diff.)
- No substantive omissions, errors, scope creep, or wrong terms.

Net: substantively a perfect, complete, curator-aligned solution; F1=0.667
materially under-represents it (the gap is serialization-only, not content).
