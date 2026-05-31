---
ontology: mondo
issue_number: 9862
pr_number: 10103
eval_repo_pr: 111
agent: std_opencode_g55
model: gpt-5.5
runtime: opencode
agent_config_tag: v3
case_type: synonym_update
difficulty: simple
f1: 0.182
precision: 0.125
recall: 0.333
jaccard: 0.1
outcome: failure
failure_modes:
  - under_editing
  - missed_requirement
  - over_editing
  - wrong_pattern
reviewed_by: codex
reviewed_at: "2026-05-16"
---

<!-- Review this eval run following .claude/skills/review-agent-pr/SKILL.md

  Source issue: https://github.com/monarch-initiative/mondo/issues/9862
  Human PR (ground truth): https://github.com/monarch-initiative/mondo/pull/10103
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-mondo/pull/111
  Agent config: ai4curation/mondo-agent-config

  Quick reference:
    gh issue view 9862 --repo monarch-initiative/mondo
    gh pr diff 10103 --repo monarch-initiative/mondo
    gh pr diff 111 --repo ai4curation/eval-ont-agent-mondo
-->

## Summary

Source PR #10103 addressed `synonym_update` for issue #9862: Request for new synonym [Add
GEMIN5-related neurodevelopmental disorders and GEMIN5 disorders as new synonym for
Neurodevelopmental disorder with cerebellar atrophy and motor dysfunction]. Human resolution
summary: The PR added 8 lines to MONDO:0859152 in mondo-edit.obo with no deletions. Beyond the two
requested synonyms, the curator also added a definition and logical definition to the term, which
previously lacked both. This enrichment beyond the original request improves the term's utility for
both human users and automated reasoning. This attempt changed `src/ontology/mondo-edit.obo` and
scored F1=0.182 (precision=0.125, recall=0.333). It matched 1/8 accepted additions and 0/0 accepted
deletions.

## Strengths

- Matched 1 normalized human diff lines, showing direct overlap with the accepted curation.
- Matched accepted addition: `property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9862" xsd:anyURI`

## Issues

- Missing accepted changes: 7 additions and 0 deletions from the human PR were not reproduced.
- Missing accepted addition: `def: "A neurodevelopmental disorder caused by variation in the GEMIN5 gene, characterized by global developmental delay with prominent motor abnorm...`
- Missing accepted addition: `comment: Affected individuals have cognitive impairment and speech delay; brain imaging shows cerebellar atrophy. The severity is variable. Other s...`
- Missing accepted addition: `synonym: "GEMIN5 disorder" EXACT [https://orcid.org/0000-0001-9310-0163, PMID:38773790]`
- Missing accepted addition: `synonym: "GEMIN5-related neurodevelopmental disorder" EXACT [https://orcid.org/0000-0001-9310-0163, PMID:33963192]`
- Missing accepted addition: `synonym: "NEDCAM" EXACT ABBREVIATION [OMIM:619333]`
- Extra changes beyond the accepted PR: 2 additions and 0 deletions. These may be defensible only if independently justified by the issue discussion.
- Extra agent addition: `synonym: "GEMIN5 disorders" EXACT [PMID:38773790]`
- Extra agent addition: `synonym: "GEMIN5-related neurodevelopmental disorders" EXACT [PMID:38773790]`
- Overall this is a failure because the accepted edit was largely missed or buried under substantial unrelated change.
