---
ontology: cell-ontology
issue_number: 3497
pr_number: 3574
eval_repo_pr: 153
agent: std_claude_haiku45
model: claude-haiku-4.5
runtime: claude
agent_config_tag: v3
case_type: new_term
difficulty: medium
f1: 0.113
precision: 0.060
recall: 1.000
jaccard: 0.060
outcome: partial_success
failure_modes: [under_editing]
case_quality: poor
case_quality_reason: odk_build_regenerated_file_domination
companion_prs: [3576]
scoring_caveat: "Gold PR #3574 is dominated by ODK release-build artifacts (merged_import.owl +78, cellxgene_subset.tsv 958/958 reordered, 5 component version-date bumps, an unrelated hra_subset.owl inSubset removal) that agents are explicitly told not to produce (config: ONLY EDIT cl-edit.owl). Judge against the 12-line cl-edit.owl gold hunk and the issue, not the whole-diff metadiff. F1=0.113 massively under-represents quality."
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-16
---

<!-- Review this eval run following .claude/skills/review-agent-pr/SKILL.md

  Source issue: https://github.com/obophenotype/cell-ontology/issues/3497
  Human PR (ground truth): https://github.com/obophenotype/cell-ontology/pull/3574
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-cl/pull/153
  Agent config: ai4curation/cl-agent-config
-->

## Summary

The agent correctly added the `fasciacyte` (CL_9900001) term to `cl-edit.owl` with the
exact definition, both PMIDs, the requested parent, ORCID contributor, and the issue
back-link — i.e. it satisfied essentially every explicit ask in issue #3497. The reported
F1=0.113 (precision 0.060, recall 1.000) badly **under-represents** quality: the gold PR
#3574 diff is dominated by ODK release-build regenerated files (a +78-line
`merged_import.owl` UBERON import expansion, a 958/958-line reordered
`cellxgene_subset.tsv`, five component version-date bumps, and an unrelated
`hra_subset.owl` `inSubset` removal) that the agent config explicitly forbids the agent
from touching ("ONLY EDIT `src/ontology/cl-edit.owl`"). Recall=1.0 confirms every line the
agent wrote matched gold; precision is crushed only by build artifacts the agent could not
and should not produce. This is a `case_quality: poor` evaluation case. Treated as a
substantive new-term task, this is a near-complete result with one modeling omission.

## Strengths

- Correct ID `CL_9900001` from the NTR `CL_99xxxxx` temporary range (idrange:81) — matches
  gold exactly.
- Definition string matches gold byte-for-byte, including the dual `hasDbXref`
  reification with `PMID:29575206` and `PMID:33573365` on the `IAO_0000115` axiom.
- Correct parent `SubClassOf(obo:CL_9900001 obo:CL_0000499)` (stromal cell), exactly as
  requested in the issue.
- `terms:contributor` ORCID `0000-0002-5507-2103` and `IAO_0000233` issue back-link both
  present and correct.
- `Declaration(Class(obo:CL_9900001))` placed in numerical order in the declarations block
  and the class block inserted at the same location as gold (after CL_7770006, before the
  obsolete CP_* block). Recall=1.0 reflects this byte-level alignment.
- Scope-disciplined: edited only `cl-edit.owl`, exactly per the agent config instruction.

## Issues

- **Omission (substantive):** did not add the genus-differentia
  `EquivalentClasses(obo:CL_9900001 ObjectIntersectionOf(obo:CL_0000499 ObjectSomeValuesFrom(obo:BFO_0000050 obo:UBERON_0011236)))`
  (part_of deep fascia, UBERON_0011236) that the human added. This is the one piece of
  real ontological modeling missing — the agent produced an asserted-parent-only term
  where gold added a logical definition anchored to deep fascia.
- **Omission (minor):** no `rdfs:comment` explaining the stromal-vs-fibroblast
  classification. The human only added this after a `CHANGES_REQUESTED` review by dosumis,
  so it was not derivable from the issue alone; reasonable to miss but worth noting.
- Used `terms:date "2026-05-12..."` (run date) rather than gold's `2026-02-20T14:27:58Z`;
  this is a normal provenance/timestamp difference, not a quality defect.
- Did not add `terms:creator "GitHub Copilot"` (gold #3574 itself omitted it too; the
  companion test PR #3576 included it) — immaterial.
- F1 is low almost entirely due to ODK build-artifact domination in the gold diff, not
  agent error; the only genuine substantive gap is the missing equivalent-class axiom.
