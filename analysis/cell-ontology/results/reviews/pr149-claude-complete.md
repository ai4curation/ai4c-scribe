---
ontology: cell-ontology
issue_number: 3559
pr_number: 3564
eval_repo_pr: 149
agent: std_claude_haiku45
model: claude-haiku-4-5-20251001
runtime: claude
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
reviewed_at: 2026-05-16
---

## Summary

The agent added all three requested abbreviation synonyms — "WBC" to leukocyte
(CL:0000738), "RPE" to retinal pigment epithelial cell (CL:0002586), and "PBMC"
to peripheral blood mononuclear cell (CL:2000001) — each as a bare
`hasExactSynonym`, with placement matching the gold PR (WBC after the
"white blood cell" synonym line). This correctly identifies the right terms,
abbreviations, and synonym scope per the issue and curator consensus. The
metadiff F1=0.0 severely under-represents the quality: it is zero only because
the gold PR attached a `PMID` xref and `oboInOwl:hasSynonymType obo:OMO_0003000`
axiom annotation to every added line. The work is substantively ~70% correct
but genuinely incomplete on provenance.

## Strengths

- Correctly identified all three target terms by CURIE: CL:0000738
  (leukocyte), CL:0002586 (retinal pigment epithelial cell), CL:2000001
  (peripheral blood mononuclear cell), including RPE (which the CASE_BRIEF
  "Changes Made" text omits but the issue and gold both require).
- Used the correct predicate/scope `oboInOwl:hasExactSynonym`, consistent with
  curator guidance (addiehl, scheuerm) in the issue thread.
- Synonym placement matches the gold PR exactly (WBC inserted after
  `"white blood cell"`), slightly better positioned than the sonnet-4.5
  attempt, though still zero metadiff match due to the missing provenance
  annotations.
- Tightly scoped: 3 added lines, only `src/ontology/cl-edit.owl`, no base
  contamination, no over-editing.
- Clear, accurate issue/PR comment correctly enumerating the three
  term/abbreviation pairs.

## Issues

- Omission (the real gap): no literature reference or synonym type attached.
  Gold uses
  `AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:...") Annotation(oboInOwl:hasSynonymType obo:OMO_0003000) oboInOwl:hasExactSynonym ...)`
  on all three lines (PMID:40794848 WBC, PMID:35835183 RPE, PMID:27696124
  PBMC). The issue asked for "reference(s)" and the cl-agent-config CLAUDE.md
  shows this exact OMO_0003000 abbreviation pattern, so this is an
  instructed-against miss.
- The F1/precision/recall of 0.0 reflects all-or-nothing line matching against
  gold lines that all carry provenance; it does not mean the agent's output is
  wrong. Substance is largely correct; this is partial_success, not failure.
- Functionally near-identical to the sonnet-4.5 attempt (#210); the two diffs
  differ only in WBC line placement.
