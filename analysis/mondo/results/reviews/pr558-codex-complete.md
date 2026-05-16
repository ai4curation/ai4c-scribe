---
ontology: mondo
issue_number: 9938
pr_number: 10221
eval_repo_pr: 558
agent: std_codex_g55
model: gpt-5.5
runtime: codex
agent_config_tag: v3
case_type: synonym_update
difficulty: simple
f1: 0.235
precision: 1.0
recall: 0.133
jaccard: 0.133
outcome: failure
failure_modes: [under_editing, missed_requirement, wrong_pattern, missed_synonym]
reviewed_by: gpt-5.5
reviewed_at: 2026-05-16
---

<!-- Review this eval run following .claude/skills/review-agent-pr/SKILL.md

  Source issue: https://github.com/monarch-initiative/mondo/issues/9938
  Human PR (ground truth): https://github.com/monarch-initiative/mondo/pull/10221
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-mondo/pull/558
  Agent config: ai4curation/mondo-agent-config

  Quick reference:
    gh issue view 9938 --repo monarch-initiative/mondo
    gh pr diff 10221 --repo monarch-initiative/mondo
    gh pr diff 558 --repo ai4curation/eval-ont-agent-mondo
-->

## Summary

Source PR #10221 addressed `synonym_update` for issue #9938: request to relabel MONDO:0012277. Human
resolution summary: The PR added "LDB3-related myofibrillar myopathy" as an exact synonym to
MONDO:0012277 in the mondo-edit.obo file. This is a 2-line addition with no deletions, representing
the simplest possible ontology edit pattern: adding a synonym annotation to an existing term stanza.
This attempt changed `src/ontology/mondo-edit.obo` and scored F1=0.235 (precision=1.0,
recall=0.133). It matched 2/2 accepted additions and 0/0 accepted deletions.

## Strengths

- Matched 2 normalized human diff lines, showing direct overlap with the accepted curation.
- Matched accepted addition: `synonym: "LDB3-related myofibrillar myopathy" EXACT [https://clinicalgenome.org/affiliation/40151/, https://orcid.org/0000-0002-2078-7280] {OMO:000...`
- Matched accepted addition: `property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9938" xsd:anyURI`
- High precision indicates the agent mostly edited within the accepted change surface.

## Issues

- Extra changes beyond the accepted PR: 7 additions and 6 deletions. These may be defensible only if independently justified by the issue discussion.
- Extra agent addition: `name: LDB3-related myofibrillar myopathy`
- Extra agent addition: `synonym: "MFM4" RELATED ABBREVIATION [OMIM:609452]`
- Extra agent addition: `synonym: "myofibrillar myopathy (disease) caused by mutation in LDB3" EXACT [MONDO:patterns/disease_series_by_gene]`
- Extra agent addition: `synonym: "myofibrillar myopathy 4" EXACT [OMIM:609452]`
- Extra agent addition: `synonym: "myofibrillar myopathy type 4" EXACT [Orphanet:98912]`
- Extra agent deletion: `name: myofibrillar myopathy 4`
- Extra agent deletion: `synonym: "MFM4" RELATED ABBREVIATION []`
- Extra agent deletion: `synonym: "myofibrillar myopathy (disease) caused by mutation in LDB3" EXACT []`
- Extra agent deletion: `synonym: "myofibrillar myopathy type 4" EXACT []`
- Overall this is a failure because the accepted edit was largely missed or buried under substantial unrelated change.
