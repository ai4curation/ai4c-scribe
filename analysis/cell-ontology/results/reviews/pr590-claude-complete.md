---
ontology: cell-ontology
issue_number: 3559
pr_number: 3564
eval_repo_pr: 590
agent: std_opencode_gpt54
model: gpt-5.4
runtime: opencode
agent_config_tag: ai4curation/cl-agent-config@v3:.
case_type: synonym_update
difficulty: simple
f1: 0.0
precision: 0.0
recall: 0.0
jaccard: 0.0
outcome: partial_success
failure_modes:
  - missed_requirement
case_quality: ok
case_quality_reason: metadiff_underrepresents_substance
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-17
---

## Summary

The agent added all three requested abbreviation synonyms — "WBC" to leukocyte
(CL:0000738), "RPE" to retinal pigment epithelial cell (CL:0002586), and "PBMC"
to peripheral blood mononuclear cell (CL:2000001) — each as a
`hasExactSynonym` carrying an `oboInOwl:hasSynonymType obo:OMO_0003000`
abbreviation annotation, with the issue URL as the xref. This is the closest
of the gpt-5.x attempts to the gold pattern: correct terms, correct
abbreviations, correct exact scope on all three, and the correct OMO_0003000
synonym type. The only substantive gap is provenance: gold uses literature
PMIDs (PMID:40794848 WBC, PMID:35835183 RPE, PMID:27696124 PBMC) as the xref
where this attempt used the GitHub issue URL. Metadiff F1=0.0 severely
under-represents quality — it is zero only because no agent line matches a
gold line byte-for-byte; substance is ~85% correct.

## Strengths

- Correctly identified all three target terms by CURIE and applied
  `oboInOwl:hasExactSynonym` scope to each, matching gold and curator
  consensus (addiehl: PBMC/WBC exact; scheuerm: RPE appropriate as a synonym
  for CL:0002586).
- Used the correct `oboInOwl:hasSynonymType obo:OMO_0003000` abbreviation
  synonym type on all three lines — the exact pattern gold uses and the one
  demonstrated in the cl-agent-config CLAUDE.md. This is the key axiom-shape
  detail that pr552/pr491 missed.
- Tightly scoped: the issue-relevant diff is exactly 3 added lines to
  `src/ontology/cl-edit.owl`, one per term, placed in the correct annotation
  block. No base contamination, no over-editing, no tracker-item noise.
- Strong methodology: PR comment documents reviewing issue context, checking
  existing synonym patterns, and running `robot convert` to confirm the
  edited ontology parses.

## Issues

- Omission (the real gap): the xref is the issue URL
  (`https://github.com/obophenotype/cell-ontology/issues/3559`) rather than
  the literature PMID gold attached to each synonym. The issue explicitly
  asked for "reference(s)" and gold sourced specific PMIDs. The issue URL is
  weaker provenance than a literature citation; this is an
  instructed-toward miss, not a stylistic choice.
- Trailing-newline artifact: the diff includes a no-newline-at-EOF →
  newline-at-EOF change at line 35597. Harmless and unrelated to the synonym
  request; likely a robot-convert/serialization side effect.
- F1/precision/recall of 0.0 does NOT mean the agent did nothing — the metric
  is all-or-nothing per line and every gold line carries the PMID +
  OMO_0003000 axiom annotations. Treat as partial_success, not failure.
