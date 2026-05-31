---
ontology: cell-ontology
issue_number: 3497
pr_number: 3574
eval_repo_pr: 592
agent: std_opencode_gpt54
model: gpt-5.4
runtime: opencode
agent_config_tag: v3
case_type: new_term
difficulty: medium
f1: 0.073
precision: 0.040
recall: 0.400
jaccard: 0.038
outcome: partial_success
failure_modes: [under_editing]
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
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-cl/pull/592
  Agent config: ai4curation/cl-agent-config
-->

## Summary

The agent added the `fasciacyte` (CL_9900001) term to `cl-edit.owl` with the requested
ID, parent, both PMIDs, ORCID contributor and the issue back-link, and reproduced the
**fullest definition** of the gpt-5.x attempts — it retains gold's "mesenchymal" genus
plus the HAS2 mRNA / Alcian Blue / anti-HABP evidence clause nearly verbatim. The
reported F1=0.073 (precision 0.040, recall 0.400) badly **under-represents** quality:
gold PR #3574's diff is dominated by ODK release-build regenerated files (a +78-line
`merged_import.owl` UBERON expansion, a 958/958-line reordered `cellxgene_subset.tsv`,
five component version-date bumps, an unrelated `hra_subset.owl` `inSubset` removal) that
the config explicitly forbids the agent from touching ("ONLY EDIT
`src/ontology/cl-edit.owl`"). This is a `case_quality: poor` evaluation case. Treated as a
substantive new-term task this is a strong partial solution with one modeling omission.

## Strengths

- Correct ID `CL_9900001` from the NTR temporary range — matches gold exactly.
- `Declaration(Class(obo:CL_9900001))` placed in the declarations block (in this run's
  base ordering, before CL_7770002).
- Correct asserted parent `SubClassOf(obo:CL_9900001 obo:CL_0000499)` (stromal cell),
  exactly as requested.
- Definition is the closest of the gpt-5.x attempts to gold: keeps "A mesenchymal stromal
  cell of the deep fascia... vimentin-positive, CD68-negative, S-100A4-positive... HAS2
  mRNA expression, Alcian Blue staining, and anti-HABP immunoreactivity..." — only minor
  wording differences (e.g. "(e.g., fascia lata)" absent).
- Both definition xrefs `PMID:29575206` and `PMID:33573365` reified onto `IAO_0000115`
  in gold's dual-`hasDbXref` form.
- `terms:contributor` ORCID `0000-0002-5507-2103` and `IAO_0000233` issue link present
  and correct in value.
- Added a `fasciocyte` exact synonym (xref'd to PMID:29575206) — a defensible spelling
  variant capture not present in gold but a reasonable, harmless enrichment.
- Scope-disciplined: edited only `cl-edit.owl`. The agent's PR comment documents checking
  the parent term, checking for an existing term, and reviewing both PMIDs.

## Issues

- **Omission (substantive):** missing the genus-differentia
  `EquivalentClasses(obo:CL_9900001 ObjectIntersectionOf(obo:CL_0000499 ObjectSomeValuesFrom(obo:BFO_0000050 obo:UBERON_0011236)))`
  (part_of deep fascia) that the human added. This is the one piece of real ontological
  modeling missing — an asserted-parent-only term vs gold's logical definition anchored
  to deep fascia (UBERON_0011236).
- **Scope (very minor):** the extra `fasciocyte` synonym is not in gold; defensible but
  technically lowers precision against the gold hunk.
- `IAO_0000233` value written as a quoted string literal rather than gold's IRI form
  `<...>` — minor serialization deviation.
- No `rdfs:comment` on the stromal-vs-fibroblast distinction; the human only added this
  after a `CHANGES_REQUESTED` review, so it was not derivable from the issue alone —
  reasonable to miss.
- `terms:date` uses the run date and `terms:creator "GitHub Copilot"` was added (gold
  #3574 itself omitted creator); normal provenance differences, not quality defects.
- The agent's PR comment notes it did not run ROBOT validation this pass (only inspected
  the diff) — weaker validation methodology than #555's `robot convert` check.
- F1 is low almost entirely due to ODK build-artifact domination in the gold diff; the
  only genuine substantive gap is the missing equivalent-class axiom.
