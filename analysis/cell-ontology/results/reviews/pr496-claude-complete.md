---
ontology: cell-ontology
issue_number: 3497
pr_number: 3574
eval_repo_pr: 496
agent: std_opencode_gpt55
model: gpt-5.5
runtime: opencode
agent_config_tag: v3
case_type: new_term
difficulty: medium
f1: 0.073
precision: 0.040
recall: 0.400
jaccard: 0.038
outcome: partial_success
failure_modes: [under_editing, wrong_pattern]
case_quality: poor
case_quality_reason: odk_build_regenerated_file_domination
companion_prs: [3576]
scoring_caveat: "Gold PR #3574 is dominated by ODK release-build artifacts (merged_import.owl +78, cellxgene_subset.tsv 958/958 reordered, 5 component version-date bumps, an unrelated hra_subset.owl inSubset removal) that agents are explicitly told not to produce (config: ONLY EDIT cl-edit.owl). Judge against the 12-line cl-edit.owl gold hunk and the issue, not the whole-diff metadiff. F1=0.073 massively under-represents quality."
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-17
---

<!-- Review this eval run following .claude/skills/review-agent-pr/SKILL.md

  Source issue: https://github.com/obophenotype/cell-ontology/issues/3497
  Human PR (ground truth): https://github.com/obophenotype/cell-ontology/pull/3574
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-cl/pull/496
  Agent config: ai4curation/cl-agent-config
-->

## Summary

The agent added the `fasciacyte` (CL_9900001) term to `cl-edit.owl` with the requested
ID, parent, both PMIDs, ORCID contributor and the issue back-link. The produced
`cl-edit.owl` blob (`823fcf4`) is **byte-identical** to attempt #555 (gpt-5.5/opencode),
so the substantive assessment is the same. The reported F1=0.073 (precision 0.040, recall
0.400) badly **under-represents** quality: gold PR #3574's diff is dominated by ODK
release-build regenerated files (a +78-line `merged_import.owl` UBERON expansion, a
958/958-line reordered `cellxgene_subset.tsv`, five component version-date bumps, an
unrelated `hra_subset.owl` `inSubset` removal) that the config explicitly forbids the
agent from touching ("ONLY EDIT `src/ontology/cl-edit.owl`"). This is a `case_quality:
poor` evaluation case. Treated as a substantive new-term task it is a recognizable
partial solution with a paraphrased definition and a missing logical definition.

## Strengths

- Correct ID `CL_9900001` from the NTR temporary range — matches gold exactly.
- `Declaration(Class(obo:CL_9900001))` correctly placed in the declarations block (after
  CL_7770006, before the CP_* block) — same location as gold.
- Correct asserted parent `SubClassOf(obo:CL_9900001 obo:CL_0000499)` (stromal cell),
  exactly as requested in the issue.
- Both definition xrefs `PMID:29575206` and `PMID:33573365` present and reified onto the
  `IAO_0000115` axiom in the same dual-`hasDbXref` form as gold.
- `terms:contributor` ORCID `0000-0002-5507-2103` and `IAO_0000233` issue back-link both
  present and correct in value.
- Scope-disciplined: edited only `cl-edit.owl`, exactly per the agent config instruction.

## Issues

- **Omission (substantive):** missing the genus-differentia
  `EquivalentClasses(obo:CL_9900001 ObjectIntersectionOf(obo:CL_0000499 ObjectSomeValuesFrom(obo:BFO_0000050 obo:UBERON_0011236)))`
  (part_of deep fascia) that the human added. The agent produced an asserted-parent-only
  term where gold added a logical definition anchored to deep fascia (UBERON_0011236).
- **Style/divergence:** definition is a paraphrase ("A stromal cell of the deep
  fascia...") that drops gold's "mesenchymal" genus qualifier and the HAS2 mRNA / Alcian
  Blue / anti-HABP evidence clause. Semantically faithful but not byte-aligned with the
  curator-supplied issue wording.
- **Scope (minor over-edit):** added `SubClassOf(obo:CL_9900001 ObjectSomeValuesFrom(obo:RO_0002215 obo:GO_0030213))`
  (capable_of hyaluronan biosynthetic process), not in gold; plausible but does not
  substitute for the missing anatomical logical definition.
- `IAO_0000233` value written as a quoted string literal rather than gold's IRI form —
  minor serialization deviation.
- `terms:date` uses the run date and `terms:creator "GitHub Copilot"` was added (gold
  #3574 itself omitted creator); normal provenance differences, not quality defects.
- This attempt has no PR/issue comment captured in the case file (only the diff), so
  methodology cannot be cross-checked; the diff itself is identical to #555 where the
  agent documented a `robot convert` validation pass.
- F1 is low almost entirely due to ODK build-artifact domination in the gold diff; the
  genuine substantive gaps are the missing equivalent-class axiom and the abridged
  definition wording.
