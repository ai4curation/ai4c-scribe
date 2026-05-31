---
ontology: mondo
issue_number: 9849
pr_number: 10084
eval_repo_pr: 272
agent: std_opencode_kimi
model: kimi-k2.6
runtime: opencode
agent_config_tag: v3
case_type: new_term
difficulty: medium
f1: 0.435
precision: 0.417
recall: 0.455
jaccard: 0.278
outcome: partial_success
failure_modes:
  - under_editing
  - missed_requirement
  - over_editing
reviewed_by: codex
reviewed_at: "2026-05-16"
---

<!-- Review this eval run following .claude/skills/review-agent-pr/SKILL.md

  Source issue: https://github.com/monarch-initiative/mondo/issues/9849
  Human PR (ground truth): https://github.com/monarch-initiative/mondo/pull/10084
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-mondo/pull/272
  Agent config: ai4curation/mondo-agent-config

  Quick reference:
    gh issue view 9849 --repo monarch-initiative/mondo
    gh pr diff 10084 --repo monarch-initiative/mondo
    gh pr diff 272 --repo ai4curation/eval-ont-agent-mondo
-->

## Summary

Source PR #10084 addressed `new_term` for issue #9849: Request for new term 'reticular
pseudodrusen'. Human resolution summary: The PR created MONDO:1060213 with 13 additions to
mondo-edit.obo. The new term includes the label "reticular pseudodrusen", a revised definition based
on the provided PMIDs, exact synonyms ("subretinal drusenoid deposits", "SDD", "RPD"), parent
classification, and ORCID-attributed evidence annotations. The curator critically evaluated the
suggested references and excluded one that did not support the term. This attempt changed
`src/ontology/mondo-edit.obo` and scored F1=0.435 (precision=0.417, recall=0.455). It matched 4/12
accepted additions and 0/0 accepted deletions.

## Strengths

- Matched 4 normalized human diff lines, showing direct overlap with the accepted curation.
- Matched accepted addition: `[Term]`
- Matched accepted addition: `name: reticular pseudodrusen`
- Matched accepted addition: `xref: SCTID:762533006 {source="MONDO:equivalentTo"}`
- Matched accepted addition: `property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9849" xsd:anyURI`

## Issues

- Missing accepted changes: 8 additions and 0 deletions from the human PR were not reproduced.
- Missing accepted addition: `id: MONDO:1060213`
- Missing accepted addition: `def: "A retinal drusen characterized by subretinal deposits located internal to the retinal pigment epithelium, composed of material aggregations i...`
- Missing accepted addition: `comment: Reticular pseudodrusen are a strong independent risk factor for late age-related macular degeneration and are particularly associated with...`
- Missing accepted addition: `synonym: "RPD" EXACT ABBREVIATION [https://orcid.org/0000-0001-6677-8489, PMID:29859199]`
- Missing accepted addition: `synonym: "SDD" EXACT ABBREVIATION [https://orcid.org/0000-0001-6677-8489, PMID:29859199]`
- Extra changes beyond the accepted PR: 7 additions and 0 deletions. These may be defensible only if independently justified by the issue discussion.
- Extra agent addition: `id: MONDO:7770012`
- Extra agent addition: `def: "Subretinal deposits located internal to the retinal pigment epithelium, composed of aggregations of material in the subretinal space between ...`
- Extra agent addition: `synonym: "RPD" EXACT ABBREVIATION [PMID:29859199, PMID:34752962, PMID:38386332, PMID:41361163]`
- Extra agent addition: `synonym: "SDD" EXACT ABBREVIATION [PMID:29859199, PMID:34752962, PMID:38386332, PMID:41361163]`
- Extra agent addition: `synonym: "subretinal drusenoid deposits" EXACT [PMID:29859199, PMID:34752962, PMID:38386332, PMID:41361163]`
- Overall this is a partial success: the attempt captures some intended curation but would still need curator correction before merge.
