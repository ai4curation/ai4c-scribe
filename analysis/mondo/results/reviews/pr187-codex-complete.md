---
ontology: mondo
issue_number: 9826
pr_number: 10142
eval_repo_pr: 187
agent: std_claude_hai45
model: claude-haiku-4.5
runtime: claude
agent_config_tag: v3
case_type: obsoletion
difficulty: simple
f1: 0.062
precision: 0.864
recall: 0.032
jaccard: 0.032
outcome: failure
failure_modes: [under_editing, missed_requirement, wrong_pattern]
reviewed_by: gpt-5.5
reviewed_at: 2026-05-16
---

<!-- Review this eval run following .claude/skills/review-agent-pr/SKILL.md

  Source issue: https://github.com/monarch-initiative/mondo/issues/9826
  Human PR (ground truth): https://github.com/monarch-initiative/mondo/pull/10142
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-mondo/pull/187
  Agent config: ai4curation/mondo-agent-config

  Quick reference:
    gh issue view 9826 --repo monarch-initiative/mondo
    gh pr diff 10142 --repo monarch-initiative/mondo
    gh pr diff 187 --repo ai4curation/eval-ont-agent-mondo
-->

## Summary

Source PR #10142 addressed `obsoletion` for issue #9826: [Merge] short-rib thoracic dysplasia 22
without polydactyly & thoracic dysostosis, isolated. Human resolution summary: The PR obsoleted
MONDO:0008549 and merged its metadata into MONDO:0979242. The 13 additions include obsoletion
annotations on the source term (replaced_by pointing to MONDO:0979242) and an added definition for
the surviving term. The 9 deletions remove the active classification axioms and synonyms from the
obsoleted term. All changes are confined to `src/ontology/mondo-edit.obo`. This attempt changed
`.agents/skills/analyse-issue/SKILL.md`, `.agents/skills/deep-research-specialist/SKILL.md`,
`.agents/skills/design-pattern-advisor/SKILL.md`, `.agents/skills/identifier-validator/SKILL.md`,
`.agents/skills/merge-terms/SKILL.md`, `.agents/skills/metadata-checker/SKILL.md`,
`.agents/skills/odk/SKILL.md`, `.agents/skills/ontology-reasoner/SKILL.md`,
`.agents/skills/release-announcement/SKILL.md`, `.agents/skills/task-coordinator/SKILL.md`,
`.claude/skills/deep-research-specialist/SKILL.md`,
`.claude/skills/design-pattern-advisor/SKILL.md`, `.claude/skills/identifier-validator/SKILL.md`,
`.claude/skills/merge-terms/SKILL.md`, `.claude/skills/metadata-checker/SKILL.md`,
`.claude/skills/odk/SKILL.md`, `.claude/skills/ontology-reasoner/SKILL.md`,
`.claude/skills/release-announcement/SKILL.md`, `.claude/skills/skills`,
`.claude/skills/task-coordinator/SKILL.md`, `.github/copilot-instructions.md`, `AGENTS.md`,
`__agent_config__`, `__agent_prompt__.md`, `__issue_context__.json`, `__pr_result__`, `obo-scripts`,
`src/ontology/mondo-edit.obo` and scored F1=0.062 (precision=0.864, recall=0.032). It matched 10/13
accepted additions and 9/9 accepted deletions.

## Strengths

- Matched 19 normalized human diff lines, showing direct overlap with the accepted curation.
- Matched accepted addition: `name: obsolete thoracic dysostosis, isolated`
- Matched accepted addition: `property_value: IAO:0000231 MONDO:TermsMerged`
- Matched accepted addition: `is_obsolete: true`
- Matched accepted addition: `replaced_by: MONDO:0979242`
- Matched accepted deletion: `name: thoracic dysostosis, isolated`
- Matched accepted deletion: `comment: This term is scheduled to be merged with MONDO:0979242 short-rib thoracic dysplasia 22 without polydactyly, based on the fact that the con...`
- Matched accepted deletion: `subset: obsoletion_candidate`
- High precision indicates the agent mostly edited within the accepted change surface.

## Issues

- Missing accepted changes: 3 additions and 0 deletions from the human PR were not reproduced.
- Missing accepted addition: `def: "Any Jeune syndrome in which the cause of the disease is a mutation in the FGF4 gene, characterized by a small thorax with short ribs, resulti...`
- Missing accepted addition: `intersection_of: MONDO:0018770 ! Jeune syndrome`
- Missing accepted addition: `intersection_of: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/3682 ! FGF4`
- Extra changes beyond the accepted PR: 893 additions and 1 deletions. These may be defensible only if independently justified by the issue discussion.
- Extra agent addition: `---`
- Extra agent addition: `name: analyse-issue`
- Extra agent addition: `description: Analyze MONDO GitHub issues for validity, suggest improvements, and generate structured`
- Extra agent addition: `reports with duplication checks and identifier validation`
- Extra agent addition: `# Analyze a GitHub issue for validity`
- Extra agent deletion: `../CLAUDE.md`
- Overall this is a failure because the accepted edit was largely missed or buried under substantial unrelated change.
