---
ontology: cell-ontology
issue_number: 3454
pr_number: 3555
eval_repo_pr: 17
agent: std_opencode_g55
model: gpt-5.5
runtime: opencode
agent_config_tag: ai4curation/cl-agent-config@v3
case_type: axiom_repair
difficulty: medium
f1: 0.750
precision: 0.750
recall: 0.750
jaccard: 0.600
outcome: success
failure_modes: []
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-16
---

## Summary

The agent correctly performed the core ontological task: it removed the
`ObjectSomeValuesFrom(obo:RO_0015015 obo:PR_000001307)` (CD44-high) and
`ObjectSomeValuesFrom(obo:RO_0015015 obo:PR_000001381)` (CD122-high)
restrictions from the EquivalentClasses axioms of CL_0001203 and CL_0001204,
and stripped "CD44-high, and CD122-high" from both textual definitions. The
F1 of 0.750 **under-represents** quality here: the gold human PR (#3555)
added only 2 of the 3 PMIDs the issue explicitly requested, whereas this
attempt added all three (PMID:24258910, PMID:21926977, **PMID:41254224**),
making it arguably more issue-compliant than the gold. The "extra" third PMID
is precisely what depresses recall vs the gold.

## Strengths

- Both target axioms removed correctly and identically to gold for CL_0001203
  and CL_0001204 — the substantive immunology task is fully solved.
- Added all three issue-requested PMIDs (24258910, 21926977, 41254224); the
  issue's instruction was explicit: "do not replace existing references but add
  these along existing ones". The gold omitted PMID:41254224 ("Guidelines for
  T cell nomenclature", the paper the issue specifically flagged for its Table 4
  marker list), so this attempt is more faithful to the stated ask.
- Preserved all other defining axioms (parent CL_0000909/CL_0000897,
  CD25-negative via CL_4030046→PR_000001380, CD45RO/CD127 via RO_0002104,
  in-taxon NCBITaxon_9606, GO_0043379 differentiation).
- Validated functional syntax with `robot convert`.
- Did not add a `dc:creator` (correct: these are edits to existing terms).

## Issues

- Style/deviation: changed "indicated by being CD45RO and CD127-positive" to
  "CD45RO-positive and CD127-positive" for CL_0001203, and added a leading "A"
  to the CL_0001204 definition. Both gold and the issue text retained
  "CD45RO and CD127-positive" / no leading "A" for CL_0001204. These are
  reasonable copy-edits but diverge from the issue's verbatim definition text
  and slightly lower text-match precision.
- Reordered the `http://www.immgen.org/index_content.html` xref position
  within the CL_0001204 definition annotation (placed after the PMIDs rather
  than before). Cosmetic; no semantic effect.
- No `term_tracker_item` (IAO_0000233) added. The config CLAUDE.md says to
  "link back to the issue ... using the `term_tracker_item`"; omitting it is a
  minor process miss (though it happens to keep this attempt closer to gold,
  which also omitted it).
