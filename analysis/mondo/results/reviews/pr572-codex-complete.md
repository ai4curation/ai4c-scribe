---
ontology: mondo
issue_number: 9855
pr_number: 10115
eval_repo_pr: 572
agent: std_codex_g54
model: gpt-5.4
runtime: codex
agent_config_tag: v3
case_type: new_term
difficulty: medium
f1: 0.566
precision: 0.536
recall: 0.6
jaccard: 0.395
outcome: partial_success
failure_modes:
  - under_editing
  - missed_requirement
  - over_editing
reviewed_by: codex
reviewed_at: "2026-05-16"
---

<!-- Review this eval run following .claude/skills/review-agent-pr/SKILL.md

  Source issue: https://github.com/monarch-initiative/mondo/issues/9855
  Human PR (ground truth): https://github.com/monarch-initiative/mondo/pull/10115
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-mondo/pull/572
  Agent config: ai4curation/mondo-agent-config

  Quick reference:
    gh issue view 9855 --repo monarch-initiative/mondo
    gh pr diff 10115 --repo monarch-initiative/mondo
    gh pr diff 572 --repo ai4curation/eval-ont-agent-mondo
-->

## Summary

Source PR #10115 addressed `new_term` for issue #9855: Request for new term PADI6-related
oocyte/zygote/embryo maturation arrest 16 and maternal-effect disorder. Human resolution summary:
The PR created the new term while incorporating metadata from obsoleted MONDO:0014978. The 19
additions include the new term stanza with label, definition, synonyms (including
"oocyte/zygote/embryo maturation arrest 16" and "PREIMPLANTATION EMBRYONIC LETHALITY 2"), parent
classification, and cross-references. The 11 deletions likely reflect updating the obsoleted term's
replaced_by annotation to point to the new term... This attempt changed
`src/ontology/mondo-edit.obo` and scored F1=0.566 (precision=0.536, recall=0.6). It matched 6/18
accepted additions and 10/11 accepted deletions.

## Strengths

- Matched 16 normalized human diff lines, showing direct overlap with the accepted curation.
- Matched accepted addition: `property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9855" xsd:anyURI`
- Matched accepted addition: `synonym: "PREMBL2" EXACT ABBREVIATION [OMIM:617234]`
- Matched accepted addition: `xref: OMIM:617234 {source="MONDO:equivalentTo"}`
- Matched accepted addition: `intersection_of: MONDO:0014769 ! inherited oocyte maturation defect`
- Matched accepted deletion: `def: "OBSOLETE. Any preimplantation embryonic lethality in which the cause of the disease is a mutation in the PADI6 gene." [MONDO:patterns/disease...`
- Matched accepted deletion: `synonym: "PADI6 preimplantation embryonic lethality" EXACT [MONDO:design_pattern, MONDO:patterns/disease_series_by_gene]`
- Matched accepted deletion: `synonym: "preimplantation embryonic lethality 2" EXACT []`

## Issues

- Missing accepted changes: 12 additions and 1 deletions from the human PR were not reproduced.
- Missing accepted addition: `comment: Term replaced by MONDO:1010200 based on user request.`
- Missing accepted addition: `replaced_by: MONDO:1010200`
- Missing accepted addition: `[Term]`
- Missing accepted addition: `id: MONDO:1010200`
- Missing accepted addition: `name: oocyte/zygote/embryo maturation arrest 16`
- Missing accepted deletion: `property_value: curated_content_resource "https://www.malacards.org/card/oocyte_zygote_embryo_maturation_arrest_16" xsd:anyURI {source="MONDO:MalaC...`
- Extra changes beyond the accepted PR: 8 additions and 2 deletions. These may be defensible only if independently justified by the issue discussion.
- Extra agent addition: `name: PADI6-related oocyte/zygote/embryo maturation arrest 16 and maternal-effect disorder`
- Extra agent addition: `def: "Any inherited oocyte maturation defect in which the cause of the disease is a mutation in the PADI6 gene. It is characterized by female infer...`
- Extra agent addition: `subset: omim {source="OMIM:617234"}`
- Extra agent addition: `synonym: "early embryonic arrest" RELATED [PMID:27545678, PMID:29693651]`
- Extra agent addition: `synonym: "oocyte/zygote/embryo maturation arrest 16" EXACT [OMIM:617234]`
- Extra agent deletion: `name: obsolete preimplantation embryonic lethality 2`
- Extra agent deletion: `is_obsolete: true`
- Overall this is a partial success: the attempt captures some intended curation but would still need curator correction before merge.
