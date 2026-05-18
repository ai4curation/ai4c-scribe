---
ontology: cell-ontology
issue_number: 3500
pr_number: 3570
eval_repo_pr: 553
agent: gpt-5.5-opencode
model: gpt-5.5
runtime: opencode
agent_config_tag: ai4curation/cl-agent-config@v3
case_type: other
difficulty: simple
case_quality: ok
case_quality_reason: gold_renegotiated_term_tracker_in_pr_comments
f1: 0.000
precision: 0.000
recall: 0.000
jaccard: 0.000
outcome: partial_success
failure_modes: [over_editing]
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-17
---

## Summary

The agent added both required taxon constraints for CL_0002423 (DN2a
thymocyte) and CL_0002424 (DN2b thymocyte) — correct relation `RO_0002162`,
correct target `NCBITaxon_10090` (Mus musculus) — but wrapped each
`SubClassOf` axiom with an inline `Annotation(obo:IAO_0000233
"https://github.com/obophenotype/cell-ontology/issues/3500")` term-tracker
link. Because the gold axioms are *bare/unannotated*, every changed line
differs after normalization, yielding F1=0.0. The 0.0 **severely
over-penalizes** the work: the substance (in-taxon restriction to Mus
musculus) is biologically and logically correct and fully addresses issue
#3500. This is the same inline-annotation pattern as #190 (opus/claude); blob
`32de51a` is shared identically with sibling opencode runs #528, #589, #492.

## Strengths

- Correct, complete ontological resolution: both DN2 subtypes restricted to
  Mus musculus via `in taxon` (`RO_0002162` some `NCBITaxon_10090`), exactly
  the issue's explicit ask; valid OWL functional syntax.
- The `IAO_0000233`/term-tracker provenance is directly mandated by the
  agent's `cl-agent-config` `CLAUDE.md` ("Link back to the issue ... using the
  `term_tracker_item`"); the agent transparently documented this in its PR
  comment and cited the supporting PMIDs (20543111, 25060579).
- Good methodology surface: checked existing `RO_0002162`/`NCBITaxon_10090`
  patterns, checked for (absent) `human_subset` annotations, ran `robot
  convert` for syntax validation.

## Issues

- **Over-editing / form mismatch (decisive scoring factor):** the inline
  `Annotation(obo:IAO_0000233 ...)` on each axiom means no line matches gold,
  collapsing F1 to 0.0 despite correct content. The gold was explicitly
  renegotiated in PR comments (RiveraAndrea83: "@copilot please remove term
  tracker from the edits"), so the merged gold deliberately omits term-tracker
  provenance — a documented instruction-vs-curator-preference conflict, not a
  curation error.
- Minor serialization churn: the run also normalized the file's missing final
  newline (`\ No newline at end of file` → trailing `)`), a robot-convert-style
  artifact absent from the gold human diff. Secondary to the term-tracker
  mismatch.
- The conservative codex run #285 shows the bare-axiom form was achievable;
  this run took the least conservative (inline) variant.

Graded `partial_success` (not `failure`): core curation correct and complete;
F1=0.0 is a metadiff artifact of inline term-tracker annotation + gold
renegotiation, not evidence the issue was unresolved.
