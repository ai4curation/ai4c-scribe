---
ontology: go-ontology
issue_number: 32005
pr_number: 32026
eval_repo_pr: 487
agent: std_claude_son45
model: claude-sonnet-4.5
runtime: claude
agent_config_tag: v9
case_type: obsoletion
difficulty: medium
f1: 0.072
precision: 0.857
recall: 0.038
jaccard: 0.037
outcome: partial_success
failure_modes:
  - over_editing
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
case_quality: poor
case_quality_reason: eval_base_state_contamination
---

## Summary

A second claude-sonnet-4.5/claude run on the case, substantively equivalent to attempt #491 (same blob `318b009`): a correct GO:0009095 obsoletion (name/def prefixed, logical axioms + 5 synonyms removed, `is_obsolete: true`, both `consider: GO:0009094` and `consider: GO:0006571` with labels, tracker #32005 added, #31091 retained) with the same single sub-gold detail of **retaining `xref: MetaCyc:PWY-3481`** where the human gold removed it. The reported F1 of 0.072 is invalid as a quality measure due to **eval base-state contamination** — ~311 lines of unrelated foreign edits in the scored diff, byte-identical across all 9 low-scoring attempts on this case.

## Strengths

- Correct, well-formed obsoletion with the correct dual `consider` targets and accurate MetaCyc-decomposition rationale.
- Most thorough annotation analysis of any attempt: itemized all 4 EXP annotations by accession (UniProtKB:E9L7A5, AGI_LocusCode:AT2G22250 ×2, UniProtKB:P9WIC1) with per-annotation migrate/remove recommendations matching the issue author, plus noted the 3 computational (IEA/ISS) annotations — and correctly left annotation changes to the curation groups.
- Transparent about an environment limitation: full `make travis_build` could not complete (missing `amm` dependency); the agent disclosed this rather than over-claiming, and validated syntax with `obo-grep.pl` instead. Good calibration.

## Issues

- Same sub-gold detail as #491: `xref: MetaCyc:PWY-3481` retained on the obsolete stanza, where the gold and the top gpt-5.5 attempts removed it. The one genuine in-scope deviation; minor.
- Scored eval PR dominated by foreign, unrelated edits — **base-state contamination**, not an agent error (same block as #291/#224/#223/#491/#525/#450/#404/#324). F1/recall not a valid measure.
- `failure_modes: [over_editing]` is an artifact of contamination, not attributable to claude-sonnet-4.5. Recommend scoring on the GO:0009095 stanza only, or excluding/down-weighting; see Curation Note in METADATA.md.
