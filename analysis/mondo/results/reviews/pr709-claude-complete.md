---
ontology: mondo
issue_number: 9938
pr_number: 10221
eval_repo_pr: 709
agent: std_opencode_g54
model: gpt-5.4
runtime: opencode
agent_config_tag: v3
case_type: synonym_update
difficulty: simple
case_quality: poor
case_quality_reason: issue_renegotiated_in_comments
companion_prs: []
scoring_caveat: "Issue #9938 used the relabel template ('Suggested new label'), but the curator (@MeeSiing) explicitly resolved it as a ClinGen-qualified synonym ADD with NO rename (gold PR #10221: +2 lines, primary label 'myofibrillar myopathy 4' kept). 7/8 attempts took the title literally and RENAMED the term. metadiff F1 systematically UNDER-penalizes this: the term_tracker line lifts attempts and precision=1.0 is a pure artifact of only 2 gold lines being reproducible. Judge against the curator's stated decision + the agent config 'ClinGen Label Handling' pattern, not the issue title."
f1: 0.571
precision: 1.0
recall: 0.400
jaccard: 0.400
outcome: failure
failure_modes: [wrong_pattern, instruction_violation, over_editing]
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-17
---

## Summary

This attempt produces a diff byte-identical (blob `79ab396`) to pr762 — same gpt-5.4/opencode
configuration, same result. Gold PR #10221 added only two lines (the ClinGen-qualified EXACT
synonym `"LDB3-related myofibrillar myopathy"` with the `{OMO:0002001=...clingen}` qualifier and
ORCID/affiliation, plus an `IAO:0000233` term_tracker) and **kept the primary label
`myofibrillar myopathy 4`**, per the curator's explicit narrowing in the issue thread. This
attempt **renamed** the term — the destructive change the curator deliberately avoided — and
demoted the original label to a fabricated `synonym: "myofibrillar myopathy 4" EXACT
[OMIM:609452]`. It did add the correct ClinGen synonym and term_tracker (the two lines shared
with gold, hence precision=1.0). F1=0.571 / precision=1.0 **over-represents** quality: the
headline action is the opposite of the gold deliverable.

## Strengths

- Added the requested synonym with the correct ClinGen qualifier, matching gold line-for-line:
  `synonym: "LDB3-related myofibrillar myopathy" EXACT [https://clinicalgenome.org/affiliation/40151/, https://orcid.org/0000-0002-2078-7280] {OMO:0002001="https://w3id.org/information-resource-registry/clingen"}`
- Added the correct term_tracker (`property_value: IAO:0000233 ".../issues/9938" xsd:anyURI`).
- Did not fabricate provenance on the other pre-existing `[]` synonyms (unlike pr728/pr674);
  scope damage limited to the rename plus one added synonym.
- Reproducible result vs. pr762 indicates stable behavior for this model/runtime on this case.

## Issues

- **Wrong pattern / instruction violation (critical)**: Renamed MONDO:0012277, contrary to the
  curator's explicit decision to add the string as a ClinGen Preferred-label *synonym* and to
  the agent config's "ClinGen Label Handling" guidance. The agent followed the issue *title*
  rather than the resolving curator comment present in the imported issue context.
- **Over-editing**: Added `synonym: "myofibrillar myopathy 4" EXACT [OMIM:609452]` not in gold;
  the OMIM source is asserted, not attested by the issue.
- F1=0.571 / precision=1.0 is a metadiff artifact (only 2 matchable gold lines exist), not a
  signal of a correct resolution.
