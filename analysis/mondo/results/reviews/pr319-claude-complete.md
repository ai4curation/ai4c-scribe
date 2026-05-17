---
ontology: mondo
issue_number: 9854
pr_number: 10116
eval_repo_pr: 319
agent: std_claude_hai45
model: claude-haiku-4.5
runtime: claude
agent_config_tag: ai4curation/mondo-agent-config@v3
case_type: other
difficulty: medium
f1: 0.200
precision: 0.111
recall: 1.000
jaccard: 0.111
outcome: partial_success
failure_modes: [under_editing, missed_requirement]
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

## Summary

The smallest-scope attempt of the six: a bare two-line xref move and nothing
else. The agent removed `xref: Orphanet:2477 {source="MONDO:equivalentTo"}`
from MONDO:0016608 and added it to MONDO:0017089, but performed no subset
migration, no source-qualifier cleanup, and did not add the issue-tracker
links. F1 0.200 (P 0.111 / R 1.000) is an accurate reflection: the move is
correct (recall 1.000) but it is a tiny fraction of the curator-endorsed
resolution. Substantively a partial_success bordering on failure on
completeness — the literal ask is satisfied but the underlying
mis-attribution is left largely intact.

## Strengths

- Correct literal move: the one substantive change (Orphanet:2477 xref from
  the broad term to the isolated term) is exactly right and matches gold,
  including correct placement relative to the existing
  `Orphanet:268920 {source="MONDO:equivalentObsolete"}` line.
- No incorrect or spurious edits — everything done is in the gold diff
  (recall 1.000); precision loss is entirely from omission, not error.

## Issues

- Under-editing — by far the most incomplete attempt. Did NOT migrate the four
  Orphanet:2477-sourced subsets (`ordo_disorder`,
  `ordo_malformation_syndrome`, `orphanet`, `orphanet_rare`), which the gold
  and four of the other five attempts all moved. These subsets stay on the
  wrong term (MONDO:0016608), perpetuating the mis-attribution.
- Missed requirement: did not strip `Orphanet:2477` / `Orphanet:2477/e` from
  the `ICD10CM:Q04.5`, `icd11.foundation:368780653`, or `MedDRA:10050183`
  source qualifiers on MONDO:0016608; the MedDRA line was not touched at all.
- Missed requirement: did not add the
  `property_value: IAO:0000233 .../issues/9854` term-tracker link to either
  term, contrary to gold and the project CLAUDE.md instruction to link back to
  the issue.
- No PR-body rationale documenting the scope choice (unlike the opus-4.7
  attempt, which at least justified its conservatism). The thin output offers
  no evidence of provenance analysis.
- This low F1 is genuine signal, not a poor-case artifact — kimi-k2.6 reached
  0.941 against the identical gold.
