---
ontology: cell-ontology
issue_number: 3408
pr_number: 3522
eval_repo_pr: 97
agent: std_claude_hai45
model: claude-haiku-4-5-20251001
runtime: claude
agent_config_tag: ai4curation/cl-agent-config@v3:.
case_type: other
difficulty: hard
f1: 0.481
precision: 0.338
recall: 0.839
jaccard: 0.317
outcome: partial_success
failure_modes: [instruction_violation, missed_requirement]
case_quality: poor
case_quality_reason: gold_dominated_by_odk_serialization_artifact_and_unrequested_style
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-16
---

## Summary

The agent did the nomenclature, broad-synonym, definition-text, `part of spiral ligament`, and type-III `tension fibroblast` parts of issue #3408, but **violated the issue's most emphatic instruction**: the issue bolded "DO NOT replace references, but instead add these to existing ones", yet the agent **deleted the existing `GOC:tfm` and `PMID:18353863` definition xrefs** on all five terms, keeping only the new PMIDs. It also omitted the type-I `adjacent to stria vascularis` axiom that the issue explicitly requested. F1=0.481 is the lowest of the six; while the gold is padded with serialization artifacts (which depress all attempts), this attempt also has genuine instruction-violation and omission defects.

## Strengths

- Correct relabelling of all five terms to "type I–V spiral ligament fibrocyte" with old Arabic labels added as `hasBroadSynonym`.
- Definition free text updated with the issue-supplied wording for all five types.
- `part of some spiral ligament` (UBERON_0006725) added correctly to all five terms.
- `tension fibroblast` exact synonym (xref PMID:33193034) added for type III, as requested.

## Issues

- **Instruction violation**: deleted the pre-existing definition cross-references `GOC:tfm` and `PMID:18353863` from all five terms (e.g. CL_0002666 def xrefs go from `GOC:tfm, PMID:18353863` to only `PMID:19080786, PMID:33193034`). The issue text bolded the opposite requirement; the gold and every other attempt retained these. This is a substantive provenance regression.
- **Missed requirement**: did not add `adjacent to (RO_0002220) some UBERON_0002282` (stria vascularis of cochlear duct) for type I, which the issue explicitly requested and the gold included.
- Did not reparent to CL_0020005 nor adopt gold's `EquivalentClasses` strategy (kept `SubClassOf CL_0002665`); no `term_tracker_item` provenance added.
- The very high recall (0.839) with low precision (0.338) is partly an artifact of the smaller, less-padded agent diff overlapping the substantive gold lines while the gold's serialization/style padding inflates the denominator — but the genuine defects above mean this attempt is correctly the weakest of the six.
