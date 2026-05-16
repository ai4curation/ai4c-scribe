---
ontology: mondo
issue_number: 9861
pr_number: 10113
eval_repo_pr: 194
agent: std_claude_hai45
model: claude-haiku-4.5
runtime: claude
agent_config_tag: v3
case_type: other
difficulty: medium
f1: 0.188
precision: 0.158
recall: 0.231
jaccard: 0.103
outcome: failure
failure_modes: [under_editing, missed_requirement, over_editing, wrong_pattern]
reviewed_by: gpt-5.5
reviewed_at: 2026-05-16
---

<!-- Review this eval run following .claude/skills/review-agent-pr/SKILL.md

  Source issue: https://github.com/monarch-initiative/mondo/issues/9861
  Human PR (ground truth): https://github.com/monarch-initiative/mondo/pull/10113
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-mondo/pull/194
  Agent config: ai4curation/mondo-agent-config

  Quick reference:
    gh issue view 9861 --repo monarch-initiative/mondo
    gh pr diff 10113 --repo monarch-initiative/mondo
    gh pr diff 194 --repo ai4curation/eval-ont-agent-mondo
-->

## Summary

Source PR #10113 addressed `other` for issue #9861: [NTR/gene] Hyperinsulinemic hypoglycemia,
familial 3. Human resolution summary: The PR modified MONDO:0011236 in `src/ontology/mondo-edit.obo`
with 13 additions and 6 deletions across 6 commits. Changes included updating the rdfs:label to
"hyperinsulinemic hypoglycemia, familial, 3", adding "GCK-related hyperinsulinism" as an exact
synonym, and adjusting the classification under MONDO:0017182 "familial hyperinsulinism." The
multiple commits reflect both the review iteration (a CHANGES_REQUESTED ... This attempt changed
`src/ontology/mondo-edit.obo` and scored F1=0.188 (precision=0.158, recall=0.231). It matched 1/13
accepted additions and 2/6 accepted deletions.

## Strengths

- Matched 3 normalized human diff lines, showing direct overlap with the accepted curation.
- Matched accepted addition: `property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9861" xsd:anyURI`
- Matched accepted deletion: `name: hyperinsulinism due to glucokinase deficiency`
- Matched accepted deletion: `def: "Hyperinsulism due to glucokinase deficiency (HIGCK) is a form of diazoxide-sensitive diffuse hyperinsulinism, caused by a lowered threshold f...`

## Issues

- Missing accepted changes: 12 additions and 4 deletions from the human PR were not reproduced.
- Missing accepted addition: `name: hyperinsulinemic hypoglycemia, familial, 3`
- Missing accepted addition: `def: "A form of diffuse hyperinsulinism due to glucokinase hyperactivity associated with a variation in the GCK gene, and characterized by an exces...`
- Missing accepted addition: `synonym: "congenital glucokinase-related hyperinsulinism" EXACT [Orphanet:79299]`
- Missing accepted addition: `synonym: "GCK-related hyperinsulinism" EXACT [https://clinicalgenome.org/affiliation/40016/] {OMO:0002001="https://w3id.org/information-resource-re...`
- Missing accepted addition: `synonym: "glucokinase-related hyperinsulinemic hypoglycemia" EXACT [Orphanet:79299]`
- Missing accepted deletion: `synonym: "HHF3" RELATED ABBREVIATION [GARD:0009930, MONDO:Lexical]`
- Missing accepted deletion: `synonym: "hyperinsulinemic hypoglycemia familial 3" RELATED [GARD:0009930]`
- Missing accepted deletion: `synonym: "hyperinsulinemic hypoglycemia, familial, 3" RELATED [MONDO:Lexical]`
- Missing accepted deletion: `is_a: MONDO:0015624 {source="Orphanet:79299"} ! diazoxide-sensitive diffuse hyperinsulinism`
- Extra changes beyond the accepted PR: 8 additions and 2 deletions. These may be defensible only if independently justified by the issue discussion.
- Extra agent addition: `name: GCK-related hyperinsulinism`
- Extra agent addition: `def: "Any familial hyperinsulinism in which the cause of the disease is a gain-of-function mutation in the GCK gene. This condition is characterize...`
- Extra agent addition: `synonym: "hyperinsulinism due to glucokinase deficiency" RELATED [Orphanet:79299]`
- Extra agent addition: `is_a: MONDO:0017182 {source="PMID:15277402", source="PMID:34680961", source="PMID:24890200"} ! familial hyperinsulinism`
- Extra agent addition: `intersection_of: MONDO:0017182 ! familial hyperinsulinism`
- Extra agent deletion: `relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/4195 {source="OMIM:602485"} ! GCK`
- Extra agent deletion: `property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/4985" xsd:anyURI`
- Overall this is a failure because the accepted edit was largely missed or buried under substantial unrelated change.
