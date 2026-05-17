---
ontology: go-ontology
issue_number: 31961
pr_number: 32015
eval_repo_pr: 348
agent: std_claude_op47
model: claude-opus-4.7
runtime: claude
agent_config_tag: v9
case_type: obsoletion
difficulty: simple
f1: 0.800
precision: 0.889
recall: 0.727
jaccard: 0.667
outcome: partial_success
failure_modes:
  - over_editing
reviewed_by: claude-opus-4.7
reviewed_at: "2026-05-15"
---

## Summary

claude-opus-4.7 produced the best-articulated obsoletion in the set: structurally identical to the human gold stanza, with the two defensible cross-reference cleanups and an obsoletion comment that, like the human's, explicitly cites the EC 1.11.1.26 / Expasy synonym linkage. F1=0.800 understates quality — the false positives are good hygiene and the comment quality matches or exceeds the human's. Blob `8a2018c`.

## Strengths

- Correct, complete obsoletion: obsolete name prefix, `OBSOLETE.` def prefix, `is_a: GO:0016668` removed, `is_obsolete: true`, `replaced_by: GO:0102039`, #31961 tracker item, historical tracker items (#28261, #28340) preserved.
- Obsoletion comment is the closest to the human's: "more specific than the specificity of any known gene product. It has been replaced by GO:0102039 ... of which 'alkyl hydroperoxide reductase activity' is an exact synonym (EC 1.11.1.26)" — captures the substance-specificity rationale *and* the EC linkage.
- GO:0009321 comment rewired to GO:0102039 with explicit reasoning that the CC complex term itself is correctly left in place (out of scope); GO:0070937 spurious comment removed with a precise biological justification.
- Excellent methodology transparency: PR comment documents obo-grep reference sweep, the 16-query SPARQL QC suite + ELK reasoning passing, honest note that full `make travis_build` was not run end-to-end (covered the obsoletion-specific QC subset), and correct out-of-scope handling of the 3 annotations (go-annotation#6396).
- Checklist distinguishes N/A vs done items with justification (RESEARCH N/A, DESIGN-PATTERNS N/A) — disciplined scoping.

## Issues

- Scope/over-editing (metadiff-only): GO:0009321/GO:0070937 hunks not in the human PR → recall 0.727. These are the only deviations and are defensible curation, not errors.
- No substantive issues; this is among the highest-quality attempts despite the identical 0.800 metadiff to weaker runs — a clear case where the score fails to discriminate quality within the cluster.
