---
ontology: mondo
issue_number: 9798
pr_number: 10106
eval_repo_pr: 375
agent: std_claude_op47
model: claude-opus-4.7
runtime: claude
agent_config_tag: v3
case_type: obsoletion
difficulty: medium
f1: 0.706
precision: 0.686
recall: 0.727
jaccard: 0.545
outcome: partial_success
failure_modes: [under_editing, missed_requirement, over_editing]
reviewed_by: gpt-5.5
reviewed_at: 2026-05-16
---

<!-- Review this eval run following .claude/skills/review-agent-pr/SKILL.md

  Source issue: https://github.com/monarch-initiative/mondo/issues/9798
  Human PR (ground truth): https://github.com/monarch-initiative/mondo/pull/10106
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-mondo/pull/375
  Agent config: ai4curation/mondo-agent-config

  Quick reference:
    gh issue view 9798 --repo monarch-initiative/mondo
    gh pr diff 10106 --repo monarch-initiative/mondo
    gh pr diff 375 --repo ai4curation/eval-ont-agent-mondo
-->

## Summary

Source PR #10106 addressed `obsoletion` for issue #9798: [Obsolete] glass-chapman-hockley syndrome.
Human resolution summary: The PR merged MONDO:0023243 into MONDO:0011274 (Muenke syndrome) in a
single commit. The 15 additions transfer metadata from the obsoleted term (synonyms including
"Glass-Chapman-Hockley syndrome", cross-references, replaced_by annotation) to the Muenke syndrome
entry. The 20 deletions remove the source term's active axioms and classification. The net reduction
reflects that the obsoleted term's stanza shrinks more t... This attempt changed
`src/ontology/mondo-edit.obo` and scored F1=0.706 (precision=0.686, recall=0.727). It matched 6/15
accepted additions and 18/20 accepted deletions.

## Strengths

- Matched 24 normalized human diff lines, showing direct overlap with the accepted curation.
- Matched accepted addition: `xref: Orphanet:1535 {source="GARD:0002479", source="MONDO:equivalentObsolete"}`
- Matched accepted addition: `property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9798" xsd:anyURI`
- Matched accepted addition: `name: obsolete glass-chapman-hockley syndrome`
- Matched accepted addition: `property_value: IAO:0000231 MONDO:TermsMerged`
- Matched accepted deletion: `name: glass-chapman-hockley syndrome`
- Matched accepted deletion: `def: "The Glass-Chapman-Hockley syndrome is a very rare disease. To date, the syndrome has only been reported in one family with five members affec...`
- Matched accepted deletion: `comment: This term is scheduled for obsoletion based on the fact that it is a historical diseaseAfter obsoletion, this term will not have a replace...`

## Issues

- Missing accepted changes: 9 additions and 2 deletions from the human PR were not reproduced.
- Missing accepted addition: `subset: inferred_rare`
- Missing accepted addition: `synonym: "craniosynostosis - dysmorphism - brachydactyly" EXACT [GARD:0002479]`
- Missing accepted addition: `synonym: "craniosynostosis brachydactyly" EXACT [GARD:0002479]`
- Missing accepted addition: `synonym: "craniosynostosis with facial dysmorphism and brachydactyly syndrome" EXACT [Orphanet:1535]`
- Missing accepted addition: `synonym: "craniosynostosis-dysmorphism-brachydactyly syndrome" EXACT [GARD:0002479]`
- Missing accepted deletion: `synonym: "MNKES" RELATED ABBREVIATION [MONDO:Lexical]`
- Missing accepted deletion: `synonym: "Muenke nonsyndromic coronal craniosynostosis" RELATED []`
- Extra changes beyond the accepted PR: 8 additions and 1 deletions. These may be defensible only if independently justified by the issue discussion.
- Extra agent addition: `synonym: "craniosynostosis - dysmorphism - brachydactyly" RELATED [GARD:0002479]`
- Extra agent addition: `synonym: "craniosynostosis brachydactyly" RELATED [GARD:0002479]`
- Extra agent addition: `synonym: "craniosynostosis with facial dysmorphism and brachydactyly syndrome" EXACT []`
- Extra agent addition: `synonym: "craniosynostosis-dysmorphism-brachydactyly syndrome" RELATED [GARD:0002479]`
- Extra agent addition: `synonym: "glass chapman hockley syndrome" RELATED []`
- Extra agent deletion: `is_a: MONDO:0015469 {source="https://orcid.org/0000-0002-4142-7153"} ! craniosynostosis`
- Overall this is a partial success: the attempt captures some intended curation but would still need curator correction before merge.
