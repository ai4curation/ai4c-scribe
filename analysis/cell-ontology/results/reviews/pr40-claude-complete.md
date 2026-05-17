---
ontology: cell-ontology
issue_number: 3243
pr_number: 3251
eval_repo_pr: 40
agent: std_opencode_gpt55
model: openai/gpt-5.5
runtime: opencode
agent_config_tag: ai4curation/cl-agent-config@v3
case_type: axiom_repair
difficulty: medium
f1: 0.545
precision: 0.529
recall: 0.562
jaccard: 0.375
outcome: success
failure_modes: [wrong_pattern]
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-16
---

## Summary

This is a sibling run to eval PR #59 (same model/runtime, byte-identical diff blob `212aa91`). The agent correctly resolved issue #3243: renamed CL_0000135 to "circulating fibrocyte", replaced the definition, added "monocyte-derived fibrocyte" (narrow) and "fibrocyte" (exact) synonyms, refined the marker comment, rebuilt the logical definition, and removed the stale inferred `tendon cell SubClassOf fibrocyte` axiom (matching gold). F1 of 0.545 under-represents quality; suppression is dominated by the `EquivalentClasses`-vs-primitive-`SubClassOf` modeling-form difference and heavier comment editing than the human.

## Strengths

- Correct rename and synonyms (narrow "monocyte-derived fibrocyte"; exact "fibrocyte" preserving discoverability after the label change).
- Accurate, concise textual definition with appropriate PMID xrefs.
- Logical definition substantively captures curator intent: `CL_0000499` stromal cell + `CL_0011026` progenitor cell + `develops_from CL_0000839` + `capable_of` GO_0002495 / GO_0042060 / GO_0045766; all IDs and relations valid.
- Replaced the obsolete `develops_from some CL_0000057` (fibroblast) with `develops_from some CL_0000839`.
- Removed the stale `SubClassOf(is_inferred "true") CL_0000388 CL_0000135` — exactly matching the gold PR.

## Issues

- **Style/wrong_pattern**: genus + differentia expressed as one `EquivalentClasses(...)` axiom rather than the gold's primitive `SubClassOf` decomposition with the `EquivalentClasses` removed. Defensible modeling but the chief F1-suppressing divergence.
- Rewrote `rdfs:comment` into a short sentence; the issue explicitly deferred comment refinement and the gold left it untouched — minor divergence from the human's deliberate hold.
- Added an `IAO_0000233` issue-link annotation absent from gold (normal metadiff precision drag).
- Identical output to eval PR #59 — no independent signal; same wrong_pattern applies.
