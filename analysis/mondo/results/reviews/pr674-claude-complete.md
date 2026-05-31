---
ontology: mondo
issue_number: 9938
pr_number: 10221
eval_repo_pr: 674
agent: std_opencode_g55
model: gpt-5.5
runtime: opencode
agent_config_tag: v3
case_type: synonym_update
difficulty: simple
case_quality: poor
case_quality_reason: issue_renegotiated_in_comments
companion_prs: []
scoring_caveat: "Issue #9938 used the relabel template ('Suggested new label'), but the curator (@MeeSiing) explicitly resolved it as a ClinGen-qualified synonym ADD with NO rename (gold PR #10221: +2 lines, primary label 'myofibrillar myopathy 4' kept). 7/8 attempts took the title literally and RENAMED the term. metadiff F1 systematically UNDER-penalizes this: the term_tracker line lifts attempts and precision=1.0 is a pure artifact of only 2 gold lines being reproducible; it masks fabricated synonym-source citations. Judge against the curator's stated decision + the agent config 'ClinGen Label Handling' pattern, not the issue title."
f1: 0.235
precision: 1.0
recall: 0.133
jaccard: 0.133
outcome: failure
failure_modes: [wrong_pattern, instruction_violation, over_editing, missed_requirement]
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-17
---

## Summary

This attempt produces a diff byte-identical (blob `6ff39f5`) to pr728 — same gpt-5.5/opencode
configuration, same result, and the same most-damaging profile of the five reviewed. Gold PR
#10221 added only two lines (the ClinGen-qualified EXACT synonym
`"LDB3-related myofibrillar myopathy"` with the `{OMO:0002001=...clingen}` qualifier plus an
`IAO:0000233` term_tracker) and **kept** the primary label `myofibrillar myopathy 4`. This
attempt **renamed** the term, **fabricated provenance on five pre-existing `[]` synonyms**, and
replaced the `myofibrillar myopathy type 4` synonym wording with a fabricated
`synonym: "myofibrillar myopathy 4" EXACT [OMIM:609452]`. It did add the correct ClinGen
synonym and term_tracker (the two lines shared with gold, hence precision=1.0). F1=0.235 /
precision=1.0 strongly **over-represents** quality — precision masks the fabricated-citation
damage.

## Strengths

- Added the requested synonym with the correct ClinGen qualifier, matching gold line-for-line:
  `synonym: "LDB3-related myofibrillar myopathy" EXACT [https://clinicalgenome.org/affiliation/40151/, https://orcid.org/0000-0002-2078-7280] {OMO:0002001="https://w3id.org/information-resource-registry/clingen"}`
- Added the correct term_tracker (`property_value: IAO:0000233 ".../issues/9938" xsd:anyURI`).
- Did not outright delete any synonym strings.

## Issues

- **Fabricated provenance (critical data-integrity violation)**: Invented sources on synonyms
  that previously had empty `[]` brackets — `"MFM4" RELATED ABBREVIATION []` → `[OMIM:609452]`;
  `"myofibrillar myopathy (disease) caused by mutation in LDB3" EXACT []` →
  `[MONDO:patterns/disease_series_by_gene]` (a design-pattern tag misused as a citation);
  `"myopathy, myofibrillar, 4" RELATED []` → `[OMIM:609452]`;
  `"myopathy, myofibrillar, type 4" EXACT []` → `[OMIM:609452]`. None attested by the issue;
  precision=1.0 completely masks this.
- **Wrong pattern / instruction violation (critical)**: Renamed MONDO:0012277, contrary to the
  curator's explicit ClinGen-synonym decision and the agent config's "ClinGen Label Handling"
  guidance.
- **Missed requirement / over-editing**: Dropped the original `myofibrillar myopathy type 4`
  synonym wording and substituted a fabricated `myofibrillar myopathy 4` synonym; six unrelated
  synonym-line rewrites plus the rename, none requested.
- F1=0.235 / precision=1.0 over-represents quality; treat precision as a scoring artifact.
