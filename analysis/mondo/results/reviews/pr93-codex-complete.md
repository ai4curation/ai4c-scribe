---
ontology: mondo
issue_number: 9987
pr_number: 10094
eval_repo_pr: 93
agent: std_codex_g55
model: gpt-5.5
runtime: codex
agent_config_tag: v3
case_type: axiom_repair
difficulty: simple
f1: 0.353
precision: 1.0
recall: 0.214
jaccard: 0.214
outcome: partial_success
failure_modes:
  - under_editing
  - missed_requirement
reviewed_by: codex
reviewed_at: "2026-05-16"
---

<!-- Review this eval run following .claude/skills/review-agent-pr/SKILL.md

  Source issue: https://github.com/monarch-initiative/mondo/issues/9987
  Human PR (ground truth): https://github.com/monarch-initiative/mondo/pull/10094
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-mondo/pull/93
  Agent config: ai4curation/mondo-agent-config

  Quick reference:
    gh issue view 9987 --repo monarch-initiative/mondo
    gh pr diff 10094 --repo monarch-initiative/mondo
    gh pr diff 93 --repo ai4curation/eval-ont-agent-mondo
-->

## Summary

Source PR #10094 addressed `axiom_repair` for issue #9987: Copy-paste error in
inborn_metabolic_disrupts.yaml: definition says 'acquired' instead of 'inherited'. Human resolution
summary: The PR made a single-character semantic fix in the DOSDP pattern file, changing "acquired"
to "inherited" in the definition template text. This 1 addition and 1 deletion corrects the
definition for all terms generated from the `inborn_metabolic_disrupts` pattern, which by definition
describes inherited (not acquired) metabolic diseases. This attempt changed
`src/patterns/dosdp-pattern.owl`, `src/patterns/dosdp-patterns/inborn_metabolic.yaml`,
`src/patterns/dosdp-patterns/inborn_metabolic_disrupts.yaml`, `src/patterns/pattern-merged.owl`,
`src/patterns/pattern-simple.owl`, `src/patterns/pattern-with-imports.owl`,
`src/patterns/pattern.owl` and scored F1=0.353 (precision=1.0, recall=0.214). It matched 1/1
accepted additions and 1/1 accepted deletions.

## Strengths

- Matched 2 normalized human diff lines, showing direct overlap with the accepted curation.
- Matched accepted addition: `text: An inherited metabolic disease that has its basis in the disruption of %s.`
- Matched accepted deletion: `text: An acquired metabolic disease that is has its basis in the disruption of %s.`
- High precision indicates the agent mostly edited within the accepted change surface.

## Issues

- Extra changes beyond the accepted PR: 11 additions and 12 deletions. These may be defensible only if independently justified by the issue discussion.
- Extra agent addition: `AnnotationAssertion(<http://purl.obolibrary.org/obo/IAO_0000115> <http://purl.obolibrary.org/obo/mondo/patterns/inborn_metabolic.yaml> "An inherite...`
- Extra agent addition: `AnnotationAssertion(<http://purl.obolibrary.org/obo/IAO_0000115> <http://purl.obolibrary.org/obo/mondo/patterns/inborn_metabolic_disrupts.yaml> "An...`
- Extra agent addition: `)`
- Extra agent addition: `<obo:IAO_0000115>An inherited metabolic disease that has its basis in the disruption of &apos;process&apos;.</obo:IAO_0000115>`
- Extra agent addition: `<obo:IAO_0000115>An inherited metabolic disease that has its basis in the disruption of &apos;owl_thing&apos;.</obo:IAO_0000115>`
- Extra agent deletion: `AnnotationAssertion(<http://purl.obolibrary.org/obo/IAO_0000115> <http://purl.obolibrary.org/obo/mondo/patterns/inborn_metabolic.yaml> "An inherite...`
- Extra agent deletion: `AnnotationAssertion(<http://purl.obolibrary.org/obo/IAO_0000115> <http://purl.obolibrary.org/obo/mondo/patterns/inborn_metabolic_disrupts.yaml> "An...`
- Extra agent deletion: `)`
- Extra agent deletion: `text: An inherited metabolic disease that is has its basis in the disruption of %s.`
- Overall this is a partial success: the attempt captures some intended curation but would still need curator correction before merge.
