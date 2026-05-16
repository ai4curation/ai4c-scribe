---
ontology: mondo
issue_number: 9854
pr_number: 10116
eval_repo_pr: 228
agent: std_opencode_gem4
model: gemma-4-31b
runtime: opencode
agent_config_tag: v3
case_type: other
difficulty: medium
f1: 0.882
precision: 0.833
recall: 0.938
jaccard: 0.789
outcome: success
failure_modes: [over_editing]
reviewed_by: gpt-5.5
reviewed_at: 2026-05-16
---

<!-- Review this eval run following .claude/skills/review-agent-pr/SKILL.md

  Source issue: https://github.com/monarch-initiative/mondo/issues/9854
  Human PR (ground truth): https://github.com/monarch-initiative/mondo/pull/10116
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-mondo/pull/228
  Agent config: ai4curation/mondo-agent-config

  Quick reference:
    gh issue view 9854 --repo monarch-initiative/mondo
    gh pr diff 10116 --repo monarch-initiative/mondo
    gh pr diff 228 --repo ai4curation/eval-ont-agent-mondo
-->

## Summary

Source PR #10116 addressed `other` for issue #9854: Isolated megalencephaly Orphanet Xref. Human
resolution summary: The PR required 3 commits to complete. The first moved the Orphanet xref to the
correct term MONDO:0017089. The second removed a MedDRA xref (MedDRA:10050183) that was also
incorrectly placed on isolated megalencephaly. The third commit addressed the source annotation for
the MedDRA xref, as the curator was uncertain which source to assign after removing the Orphanet
provenance link. This attempt changed `src/ontology/mondo-edit.obo` and scored F1=0.882
(precision=0.833, recall=0.938). It matched 7/11 accepted additions and 8/8 accepted deletions.

## Strengths

- Matched 15 normalized human diff lines, showing direct overlap with the accepted curation.
- Matched accepted addition: `xref: ICD10CM:Q04.5 {source="https://orcid.org/0009-0001-6494-4831", source="MONDO:equivalentTo", source="https://orcid.org/0000-0002-5002-8648"}`
- Matched accepted addition: `xref: icd11.foundation:368780653 {source="MONDO:equivalentTo"}`
- Matched accepted addition: `subset: ordo_disorder {source="Orphanet:2477"}`
- Matched accepted addition: `subset: ordo_malformation_syndrome {source="Orphanet:2477"}`
- Matched accepted deletion: `subset: ordo_disorder {source="Orphanet:2477"}`
- Matched accepted deletion: `subset: ordo_malformation_syndrome {source="Orphanet:2477"}`
- Matched accepted deletion: `subset: orphanet {source="Orphanet:2477"}`
- High recall indicates the agent covered most accepted changes.

## Issues

- Missing accepted changes: 4 additions and 0 deletions from the human PR were not reproduced.
- Missing accepted addition: `xref: MedDRA:10050183 {source="MONDO:equivalentTo"}`
- Missing accepted addition: `property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9854" xsd:anyURI`
- Missing accepted addition: `xref: icd11.foundation:368780653 {source="Orphanet:2477"}`
- Extra changes beyond the accepted PR: 1 additions and 0 deletions. These may be defensible only if independently justified by the issue discussion.
- Extra agent addition: `xref: MedDRA:10050183 {}`
- Overall this is a successful attempt; any differences above are minor relative to the requested curation.
