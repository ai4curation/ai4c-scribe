---
ontology: go-ontology
issue_number: 32005
pr_number: 32026
eval_repo_pr: 672
agent: std_opencode_gpt54
model: gpt-5.4
runtime: opencode
agent_config_tag: v9
case_type: obsoletion
difficulty: medium
f1: 0.08
precision: 0.952
recall: 0.042
jaccard: 0.042
outcome: partial_success
failure_modes:
  - over_editing
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-17
case_quality: poor
case_quality_reason: eval_base_state_contamination
---

## Summary

The agent's actual obsoletion of GO:0009095 "aromatic amino acid biosynthetic process, prephenate pathway" is **correct and substantively matches the human gold (#32026)**: name prefixed `obsolete`, def prefixed `OBSOLETE.` (provenance `[GOC:mah, ISBN:0471331309, MetaCyc:PWY-3481]` retained), all logical axioms (is_a GO:0009073, the three `intersection_of` axioms) and all 5 synonyms removed, `xref: MetaCyc:PWY-3481` removed, `is_obsolete: true`, `term_tracker_item` updated from #31091 → #32005 (exactly matching the gold), and both `consider: GO:0009094` (L-phenylalanine biosynthetic process) and `consider: GO:0006571` (L-tyrosine biosynthetic process) added. The reported F1 of 0.080 (recall 0.042) grossly under-represents quality: the scored eval-PR diff (go-edit.obo blob `ccb7aa216..a1039a71c`) also carries the documented ~311-line foreign block of unrelated edits (GO:0000268 peroxisome targeting, GO:0003400 COPII regulation, GO:0005048 signal sequence, GO:0008785 alkyl hydroperoxide reductase, GO:0008873/0008874/0008875 gluconate dehydrogenases, exocyst, etc., from issues #31419/#31922/#31945/#31961/#31989) plus knock-on regenerated import/taxon-constraint files. That block is **eval base-state contamination** present before the agent ran, not agent work — judged on the GO:0009095 stanza this is essentially a gold match.

## Strengths

- The GO:0009095 obsoletion is among the best on substance: tracker handling exactly matches the human gold (removes #31091, adds #32005), and it correctly strips the `xref: MetaCyc:PWY-3481` from the obsoleted term (the gold retained it; per OBO obsoletion convention removing it is defensible/arguably cleaner).
- Correct dual `consider` targets (GO:0009094, GO:0006571) with sound rationale: PWY-3481 is the superpathway = PWY-3462 (L-Phe biosynthesis II) + PWY-3461 (L-Tyr biosynthesis II), already narrowMatch-mapped to GO:0009094/GO:0006571 — exactly the issue author's reasoning.
- Obsoletion comment correctly states the rationale (pre-composed combined L-Phe/L-Tyr superpathway, not a single GO BP); shorter than the gold's verbose comment but accurate. Comment text is a metadiff-tolerant free-text difference, not a defect.
- Strong methodology documented in the PR/issue comments: pre/post `make travis_build` validation, AmiGO annotation-impact review of the 4 EXP annotations (PMID:21102469 → migrate Petunia PPA-AT to GO:0009094; PMID:20883697 / PMID:18727669 → likely removal), correctly deferring annotation migration to the annotation-review process rather than acting on it in the ontology PR. This mirrors the issue author's own annotation analysis.

## Issues

- The scored eval PR is dominated by a large foreign block of unrelated ontology edits plus regenerated `go-catalytic-activities-participants.owl`, `go_taxon_constraints.owl`, `only_in_taxon.ofn/.tsv`. This is **base-state contamination** in the eval harness, not an agent error — the same go-edit.obo blob (`a1039a71c`) is byte-identical to eval PR #630. The metadiff (F1 0.080, recall 0.042) is therefore not a valid measure of this agent's work.
- `failure_modes: [over_editing]` is recorded only because the scored diff is dominated by out-of-scope contaminated changes; this is an artifact of the contaminated base, not behavior attributable to gpt-5.4 / opencode. No genuine omission or error in the agent's obsoletion was found.
- Recommend scoring this attempt on the GO:0009095 stanza only (where it is a gold match) or excluding/down-weighting; see the case-level Curation Note in METADATA.md.
