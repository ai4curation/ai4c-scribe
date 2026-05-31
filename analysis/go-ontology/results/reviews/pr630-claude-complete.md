---
ontology: go-ontology
issue_number: 32005
pr_number: 32026
eval_repo_pr: 630
agent: std_opencode_gpt54
model: gpt-5.4
runtime: opencode
agent_config_tag: v9
case_type: obsoletion
difficulty: medium
f1: 0.017
precision: 0.19
recall: 0.009
jaccard: 0.008
outcome: partial_success
failure_modes:
  - over_editing
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-17
case_quality: poor
case_quality_reason: eval_base_state_contamination
---

## Summary

The live eval PR #630 **correctly obsoletes GO:0009095** "aromatic amino acid biosynthetic process, prephenate pathway" and substantively matches the human gold (#32026): name prefixed `obsolete`, def prefixed `OBSOLETE.` (provenance retained), all logical axioms (is_a GO:0009073, the three `intersection_of` axioms) and all 5 synonyms removed, `xref: MetaCyc:PWY-3481` removed, `is_obsolete: true`, `term_tracker_item` updated #31091 → #32005 (exactly matching the gold), and both `consider: GO:0009094` and `consider: GO:0006571` added. The go-edit.obo diff for this eval PR is blob `ccb7aa216..a1039a71c` — **byte-identical to eval PR #672** (same opencode/gpt-5.4 run). The recorded F1 0.017 (recall 0.009) is meaningless here: the scored diff carries the documented ~311-line foreign contaminated block (GO:0000268, GO:0003400, GO:0005048, GO:0008785, GO:0008873/0008874/0008875, exocyst, from issues #31419/#31922/#31945/#31961/#31989) plus regenerated import/taxon-constraint files — all eval base-state contamination, not agent work.

**Correction to prior curation note:** the case METADATA (flagged 2026-05-15) classified #630 as `no_output`, citing stale attempt-file data with go-edit.obo blob `961e08a` that did not touch GO:0009095. The current live eval PR #630 diff in fact contains a correct, complete GO:0009095 obsoletion (blob `a1039a71c`), identical to #672. #630 is therefore a `partial_success` (correct core task, over_editing entirely attributable to base contamination), not `no_output`.

## Strengths

- GO:0009095 obsoletion is essentially a gold match on substance: tracker handling exactly matches the human gold (removes #31091, adds #32005), and it correctly strips `xref: MetaCyc:PWY-3481` from the obsoleted term (defensible OBO obsoletion convention; the gold retained it).
- Correct dual `consider` targets (GO:0009094, GO:0006571) with sound rationale: PWY-3481 superpathway = PWY-3462 (L-Phe biosynthesis II) + PWY-3461 (L-Tyr biosynthesis II), already mapped as narrowMatch to GO:0009094/GO:0006571 — exactly the issue author's reasoning.
- Obsoletion comment accurately captures the rationale (pre-composed combined L-Phe/L-Tyr superpathway, not a single GO BP). Wording differs from the gold's longer comment but is correct; this is a metadiff-tolerant free-text difference, not a defect.
- The diff structure (clean `is_obsolete: true` with `consider` and no leftover axioms) follows the obsolete-term design pattern correctly.

## Issues

- The scored eval PR is dominated by the large foreign contaminated block plus regenerated `go-catalytic-activities-participants.owl`, `go_taxon_constraints.owl`, `only_in_taxon.ofn/.tsv`. This is **base-state contamination** in the eval harness, not an agent error — the go-edit.obo blob is byte-identical to eval PR #672.
- `failure_modes: [over_editing]` reflects only the contaminated out-of-scope changes in the scored diff; it is an artifact of the contaminated base, not behavior attributable to gpt-5.4 / opencode. No genuine omission or error in the agent's obsoletion was found.
- The prior `no_output` classification for #630 in METADATA was based on stale data and is corrected here (see Curation Note update / new poor signal).
- Recommend scoring this attempt on the GO:0009095 stanza only (a gold match) or excluding/down-weighting; see the case-level Curation Note in METADATA.md.
