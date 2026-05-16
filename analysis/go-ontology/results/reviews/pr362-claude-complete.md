---
ontology: go-ontology
issue_number: 31961
pr_number: 32015
eval_repo_pr: 362
agent: std_gemini_g25f
model: gemini-2.5-flash
runtime: gemini
agent_config_tag: v9
case_type: obsoletion
difficulty: simple
f1: 0.308
precision: 0.222
recall: 0.500
jaccard: 0.182
outcome: failure
failure_modes:
  - missed_requirement
  - wrong_pattern
  - syntax_error
reviewed_by: claude-opus-4.7
reviewed_at: "2026-05-15"
---

## Summary

gemini-2.5-flash / gemini produced an incomplete and malformed obsoletion that violates the standard GO obsoletion pattern in multiple ways and would fail ontology QC. It set `is_obsolete: true` while *retaining* the active `is_a: GO:0016668` axiom, did not prefix the name with "obsolete", did not prefix the definition with "OBSOLETE.", did not add the #31961 term_tracker_item, and used a non-reciprocal `consider:` on the replacement term instead of the requested `replaced_by`. F1=0.308 correctly reflects a genuine failure; this is the only failing attempt in the case. Blob `dddefb5`.

## Strengths

- Correctly identified GO:0102039 as the intended replacement target and recorded the rationale in a comment.
- Added `is_obsolete: true` and `replaced_by: GO:0102039` to GO:0008785 (the two edits that align with the gold and drive the partial recall of 0.500).

## Issues

- Syntax error / wrong pattern: the obsolete term retains `is_a: GO:0016668`. An obsolete term must have all logical axioms (is_a, relationships, intersection_of) removed; an obsolete class with an asserted superclass will trip the standard obsoletion QC and is logically incoherent. This is a hard error, not a style choice.
- Missed requirement: name not prefixed with "obsolete" (still `alkyl hydroperoxide reductase activity`) and definition not prefixed with `OBSOLETE.`. Both are mandatory in the GO obsoletion pattern and are checked by `obsolete-definition-violation` SPARQL QC; this PR would fail that check.
- Missed requirement: no `term_tracker_item` for issue #31961 added; the historical tracker items were left but the issue linkage required by the workflow is absent.
- Wrong pattern: added `consider: GO:0008785` to GO:0102039. `replaced_by`/`consider` are properties of the *obsolete* term, not the replacement; pointing an active term at an obsolete one via `consider` is backwards and not part of the requested change. This is the main driver of the very low precision (0.222).
- No reference cleanup: the spurious GO:0070937 comment and the GO:0009321 comment were left untouched (lesser issue given the larger structural failures).
- No validation evidence: the PR comment shows only a checklist with no `make travis_build`/SPARQL/reasoning run; given the structural errors, validation would have failed had it been run.
- Overall: not a viable obsoletion; would require substantial rework. Correctly scored as the worst attempt.
