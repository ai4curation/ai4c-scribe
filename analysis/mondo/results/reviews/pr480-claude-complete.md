---
ontology: mondo
issue_number: 9842
pr_number: 10158
eval_repo_pr: 480
agent: std_claude_hai45
model: claude-haiku-4.5
runtime: claude
agent_config_tag: v3
case_type: obsoletion
difficulty: medium
f1: 0.968
precision: 0.938
recall: 1.0
jaccard: 0.938
outcome: success
failure_modes: []
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

## Summary

The agent performed the requested merge of MONDO:0034186 (autosomal recessive
extra-oral halitosis) into MONDO:0029144 (extraoral halitosis due to methanethiol
oxidase deficiency) cleanly and correctly. The obsolete stanza is reduced to the
canonical merge form (`is_obsolete: true`, `replaced_by: MONDO:0029144`,
`IAO:0000231 MONDO:TermsMerged`, issue link), and all meaningful annotations
(subsets, GARD/Orphanet xrefs, the `autosomal recessive extra-oral halitosis`
synonym re-attributed to `Orphanet:562538`, the `MONDO:0019222` parent, and the
`has_characteristic HP:0000007` autosomal-recessive characteristic) were
transferred to the survivor. Metadiff F1=0.968 **under-represents** quality: the
"missed deletions" are the two pre-existing synonyms (`"EHMTO"` and `"extraoral
halitosis due to MTO deficiency"`) that the human PR deleted and re-added solely
to reposition them — the agent left them in place, producing a semantically
identical but cleaner, non-churning diff.

## Strengths

- Correct, complete merge following Mondo's obsoletion pattern; obsolete stanza
  contains exactly the canonical fields and the issue tracker link.
- All transfer targets handled: 6 rare-disease subsets, `xref: GARD:0017996`,
  `xref: Orphanet:562538 {source="MONDO:equivalentTo"}`, `is_a: MONDO:0019222`,
  `relationship: has_characteristic HP:0000007`, and the issue-9842 tracker item
  added to the survivor.
- Correctly re-cited the transferred synonym as `[Orphanet:562538]` rather than
  leaving stale `[MONDO:0034186]` evidence (a common QC trap).
- Removed the obsoletion-scheduling artifacts (`subset: obsoletion_candidate`,
  `property_value: IAO:0006012 "2026-03-01"`) that should not survive a merge.

## Issues

- The only divergence from gold is cosmetic: the human re-ordered the survivor's
  synonym block (delete + re-add of two unchanged synonyms); the agent kept them
  in original position. This is not an error — arguably the agent's diff is
  cleaner. No ontological difference.
- Kept `is_a: MONDO:0003847 ! hereditary disease` alongside the more specific
  transferred parent (matching gold). This is the conservative choice; redundant
  but consistent with the human PR.
- No substantive issues.
