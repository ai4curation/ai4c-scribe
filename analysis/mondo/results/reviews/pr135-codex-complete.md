---
ontology: mondo
issue_number: 9798
pr_number: 10106
eval_repo_pr: 135
agent: std_opencode_g55
model: gpt-5.5
runtime: opencode
agent_config_tag: v3
case_type: obsoletion
difficulty: medium
f1: 0.772
precision: 0.629
recall: 1.0
jaccard: 0.629
outcome: partial_success
failure_modes: [over_editing]
reviewed_by: gpt-5.5
reviewed_at: 2026-05-16
---

<!-- Review this eval run following .claude/skills/review-agent-pr/SKILL.md

  Source issue: https://github.com/monarch-initiative/mondo/issues/9798
  Human PR (ground truth): https://github.com/monarch-initiative/mondo/pull/10106
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-mondo/pull/135
  Agent config: ai4curation/mondo-agent-config

  Quick reference:
    gh issue view 9798 --repo monarch-initiative/mondo
    gh pr diff 10106 --repo monarch-initiative/mondo
    gh pr diff 135 --repo ai4curation/eval-ont-agent-mondo
-->

## Summary

Source PR #10106 addressed `obsoletion` for issue #9798: [Obsolete] glass-chapman-hockley syndrome.
Human resolution summary: The PR merged MONDO:0023243 into MONDO:0011274 (Muenke syndrome) in a
single commit. The 15 additions transfer metadata from the obsoleted term (synonyms including
"Glass-Chapman-Hockley syndrome", cross-references, replaced_by annotation) to the Muenke syndrome
entry. The 20 deletions remove the source term's active axioms and classification. The net reduction
reflects that the obsoleted term's stanza shrinks more t... This attempt changed
`src/ontology/mondo-edit.obo` and scored F1=0.772 (precision=0.629, recall=1.0). It matched 4/15
accepted additions and 18/20 accepted deletions.

## Strengths

- Matched 22 normalized human diff lines, showing direct overlap with the accepted curation.
- Matched accepted addition: `name: obsolete glass-chapman-hockley syndrome`
- Matched accepted addition: `property_value: IAO:0000231 MONDO:TermsMerged`
- Matched accepted addition: `is_obsolete: true`
- Matched accepted addition: `replaced_by: MONDO:0011274`
- Matched accepted deletion: `name: glass-chapman-hockley syndrome`
- Matched accepted deletion: `def: "The Glass-Chapman-Hockley syndrome is a very rare disease. To date, the syndrome has only been reported in one family with five members affec...`
- Matched accepted deletion: `comment: This term is scheduled for obsoletion based on the fact that it is a historical diseaseAfter obsoletion, this term will not have a replace...`
- High recall indicates the agent covered most accepted changes.

## Issues

- Missing accepted changes: 11 additions and 2 deletions from the human PR were not reproduced.
- Missing accepted addition: `subset: inferred_rare`
- Missing accepted addition: `synonym: "craniosynostosis - dysmorphism - brachydactyly" EXACT [GARD:0002479]`
- Missing accepted addition: `synonym: "craniosynostosis brachydactyly" EXACT [GARD:0002479]`
- Missing accepted addition: `synonym: "craniosynostosis with facial dysmorphism and brachydactyly syndrome" EXACT [Orphanet:1535]`
- Missing accepted addition: `synonym: "craniosynostosis-dysmorphism-brachydactyly syndrome" EXACT [GARD:0002479]`
- Missing accepted deletion: `synonym: "MNKES" RELATED ABBREVIATION [MONDO:Lexical]`
- Missing accepted deletion: `synonym: "Muenke nonsyndromic coronal craniosynostosis" RELATED []`
- Overall this is a partial success: the attempt captures some intended curation but would still need curator correction before merge.
