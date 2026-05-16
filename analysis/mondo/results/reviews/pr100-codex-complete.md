---
ontology: mondo
issue_number: 9798
pr_number: 10106
eval_repo_pr: 100
agent: std_codex_g55
model: gpt-5.5
runtime: codex
agent_config_tag: v3
case_type: obsoletion
difficulty: medium
f1: 0.765
precision: 0.743
recall: 0.788
jaccard: 0.619
outcome: partial_success
failure_modes: [under_editing, missed_requirement, over_editing]
reviewed_by: gpt-5.5
reviewed_at: 2026-05-16
---

<!-- Review this eval run following .claude/skills/review-agent-pr/SKILL.md

  Source issue: https://github.com/monarch-initiative/mondo/issues/9798
  Human PR (ground truth): https://github.com/monarch-initiative/mondo/pull/10106
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-mondo/pull/100
  Agent config: ai4curation/mondo-agent-config

  Quick reference:
    gh issue view 9798 --repo monarch-initiative/mondo
    gh pr diff 10106 --repo monarch-initiative/mondo
    gh pr diff 100 --repo ai4curation/eval-ont-agent-mondo
-->

## Summary

Source PR #10106 addressed `obsoletion` for issue #9798: [Obsolete] glass-chapman-hockley syndrome.
Human resolution summary: The PR merged MONDO:0023243 into MONDO:0011274 (Muenke syndrome) in a
single commit. The 15 additions transfer metadata from the obsoleted term (synonyms including
"Glass-Chapman-Hockley syndrome", cross-references, replaced_by annotation) to the Muenke syndrome
entry. The 20 deletions remove the source term's active axioms and classification. The net reduction
reflects that the obsoleted term's stanza shrinks more t... This attempt changed
`src/ontology/mondo-edit.obo` and scored F1=0.765 (precision=0.743, recall=0.788). It matched 7/15
accepted additions and 19/20 accepted deletions.

## Strengths

- Matched 26 normalized human diff lines, showing direct overlap with the accepted curation.
- Matched accepted addition: `xref: Orphanet:1535 {source="GARD:0002479", source="MONDO:equivalentObsolete"}`
- Matched accepted addition: `xref: SCTID:720814001 {source="MONDO:equivalentObsolete"}`
- Matched accepted addition: `property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9798" xsd:anyURI`
- Matched accepted addition: `name: obsolete glass-chapman-hockley syndrome`
- Matched accepted deletion: `synonym: "Muenke nonsyndromic coronal craniosynostosis" RELATED []`
- Matched accepted deletion: `name: glass-chapman-hockley syndrome`
- Matched accepted deletion: `def: "The Glass-Chapman-Hockley syndrome is a very rare disease. To date, the syndrome has only been reported in one family with five members affec...`

## Issues

- Missing accepted changes: 8 additions and 1 deletions from the human PR were not reproduced.
- Missing accepted addition: `subset: inferred_rare`
- Missing accepted addition: `synonym: "craniosynostosis - dysmorphism - brachydactyly" EXACT [GARD:0002479]`
- Missing accepted addition: `synonym: "craniosynostosis brachydactyly" EXACT [GARD:0002479]`
- Missing accepted addition: `synonym: "craniosynostosis with facial dysmorphism and brachydactyly syndrome" EXACT [Orphanet:1535]`
- Missing accepted addition: `synonym: "craniosynostosis-dysmorphism-brachydactyly syndrome" EXACT [GARD:0002479]`
- Missing accepted deletion: `synonym: "MNKES" RELATED ABBREVIATION [MONDO:Lexical]`
- Extra changes beyond the accepted PR: 7 additions and 0 deletions. These may be defensible only if independently justified by the issue discussion.
- Extra agent addition: `synonym: "craniosynostosis - dysmorphism - brachydactyly" RELATED [GARD:0002479]`
- Extra agent addition: `synonym: "craniosynostosis brachydactyly" RELATED [GARD:0002479]`
- Extra agent addition: `synonym: "craniosynostosis with facial dysmorphism and brachydactyly syndrome" EXACT [GARD:0002479, PMID:20108486]`
- Extra agent addition: `synonym: "craniosynostosis-dysmorphism-brachydactyly syndrome" RELATED [GARD:0002479, PMID:20108486]`
- Extra agent addition: `synonym: "glass chapman hockley syndrome" RELATED [GARD:0002479, PMID:20108486]`
- Overall this is a partial success: the attempt captures some intended curation but would still need curator correction before merge.
