---
ontology: mondo
issue_number: 9938
pr_number: 10221
eval_repo_pr: 762
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

Gold PR #10221 added exactly two lines to the MONDO:0012277 stanza: the ClinGen-qualified
EXACT synonym `"LDB3-related myofibrillar myopathy"` (with the
`{OMO:0002001="https://w3id.org/information-resource-registry/clingen"}` qualifier and
ORCID/affiliation attribution) plus an `IAO:0000233` term_tracker, and **kept the primary
label `myofibrillar myopathy 4`** — the curator @MeeSiing explicitly narrowed the resolution
in the issue thread ("will be added ... as ClinGen Preferred label"). This attempt instead
**renamed** the term to `LDB3-related myofibrillar myopathy`, the destructive change the
curator deliberately avoided, then demoted the original label to a freshly invented
`synonym: "myofibrillar myopathy 4" EXACT [OMIM:609452]`. It did add the correct ClinGen
synonym line and the correct term_tracker (the only two lines shared with gold, hence
precision=1.0). The headline F1=0.571 with precision=1.0 badly **over-represents** quality:
the agent's headline action is the opposite of the gold deliverable.

## Strengths

- Added the requested synonym with the correct ClinGen qualifier, matching gold line-for-line:
  `synonym: "LDB3-related myofibrillar myopathy" EXACT [https://clinicalgenome.org/affiliation/40151/, https://orcid.org/0000-0002-2078-7280] {OMO:0002001="https://w3id.org/information-resource-registry/clingen"}`
- Added the correct term_tracker (`property_value: IAO:0000233 ".../issues/9938" xsd:anyURI`),
  matching gold.
- Did not delete or fabricate provenance on the other pre-existing `[]` synonyms (unlike the
  gpt-5.5 attempts pr728/pr674) — scope damage is limited to the rename plus one added synonym.
- Tightly scoped to the single target file; PR comment shows research (inspected the LDB3
  logical axiom and `disease_series_by_gene.yaml` pattern) and a `robot convert` syntax check.

## Issues

- **Wrong pattern / instruction violation (critical)**: Renamed MONDO:0012277, contrary to the
  curator's explicit decision to add the string as a ClinGen Preferred-label *synonym* and
  contrary to the agent config's documented "ClinGen Label Handling" guidance (use the
  `{OMO:0002001=...clingen}` qualifier on a synonym, not a rename). The agent's PR rationale
  ("promoting an explicit gene-based label") is a reasonable reading of the issue *title* but
  ignores the resolving curator comment that was in the imported issue context.
- **Over-editing**: Fabricated a new `synonym: "myofibrillar myopathy 4" EXACT [OMIM:609452]`
  that gold did not add; the OMIM source is asserted, not attested by the issue.
- The F1=0.571 / precision=1.0 is a metadiff artifact (only 2 gold lines exist to match, and
  it reproduced both); it does not indicate a correct resolution.
