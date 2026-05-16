---
ontology: mondo
issue_number: 9781
pr_number: 10111
eval_repo_pr: 214
agent: std_opencode_gem4
model: gemma-4-31b
runtime: opencode
agent_config_tag: ai4curation/mondo-agent-config@v3
case_type: new_term
difficulty: simple
f1: 0.533
precision: 0.571
recall: 0.500
jaccard: 0.364
outcome: partial_success
failure_modes: [over_editing, wrong_pattern]
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

## Summary

Gemma-4-31b, second run. The diff is byte-identical to eval PR #259 (same blob
`ebc0935`): the correct `is_a: MONDO:0021074 ! precancerous condition` term
with the issue's verbatim definition, but the same redundant
`synonym: "preneoplastic lesion" EXACT` (label-equals-synonym) and the same
malformed axiom source `source="MONDO:issue_9781"`. Core term correct; defects
reproduced exactly, so partial success. F1 of 0.533 roughly reflects the mixed
quality.

## Strengths

- **Correct parent.** `is_a: MONDO:0021074 ! precancerous condition`, matching
  gold and the requester's final preference in issue #9781.
- **Definition fidelity.** Issue's final refined definition text used verbatim,
  matching the gold `def` (same four PMIDs, order differs).
- Correct `IAO:0000233` link to #9781 with `xsd:anyURI`.
- Run-to-run determinism (identical to PR #259) — though here it also means the
  defects are reproduced.

## Issues

- **Redundant self-synonym (wrong pattern / over-editing).** Same as PR #259:
  `synonym: "preneoplastic lesion" EXACT` duplicates the `name`, is not
  standard MONDO practice, the gold has no synonym, and it contradicts the
  issue thread's explicit conclusion that the label should not be a synonym.
- **Malformed axiom source.** `{source="MONDO:issue_9781"}` is not a valid
  CURIE; gold uses proper PMID/ORCID source values.
- **Def xref omits requester ORCID.** Minor, secondary to the above.
- ID/creator-ORCID differences are sandbox artifacts; the substantive issues
  are the junk synonym and the invalid source value, reproduced across both
  gemma runs.
