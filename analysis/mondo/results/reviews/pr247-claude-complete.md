---
ontology: mondo
issue_number: 9798
pr_number: 10106
eval_repo_pr: 247
agent: std_opencode_kimi
model: kimi-k2.6
runtime: opencode
agent_config_tag: v3
case_type: obsoletion
difficulty: medium
f1: 0.621
precision: 0.514
recall: 0.783
jaccard: 0.450
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
outcome: partial_success
failure_modes: [wrong_pattern, under_editing, missed_requirement]
---

## Summary

A hybrid that gets the merge intent partly right but botches the obsolete-stanza mechanics. The agent transferred three craniosynostosis synonyms onto MONDO:0011274 and added the issue link, which is the right direction — but it then **left the obsoleted MONDO:0023243 stanza fat** (kept all five original synonyms and both legacy xrefs *in place* on the obsolete term) instead of reducing it to the canonical merge skeleton, and it fabricated the non-existent xref qualifier `MONDO:obsoleteEquivalent`. F1=0.621. This is closer to the repudiated #10087 obsolete-only pattern than to the approved merge.

## Strengths

- Correct merge-specific obsoletion reason `IAO:0000231 MONDO:TermsMerged` (better than the `OMO:0001000` used by #293/#335/#424/#434).
- `is_obsolete: true` and `replaced_by: MONDO:0011274` present and correct.
- Did attempt the merge direction by transferring three synonyms onto Muenke with `[PMID:20108486]` evidence and adding the `IAO:0000233` issue link — partially addressing @sabrinatoro's data-preservation requirement.

## Issues

- **Wrong pattern (key error):** the obsoleted stanza was *not* reduced to the merge skeleton. It still carries `synonym:` lines and `xref: Orphanet:1535`/`xref: SCTID:720814001` on the obsolete term — gold removes all of these from MONDO:0023243 (they belong only on the surviving term). This leaves dangling synonyms/xrefs on an obsolete class, which Mondo merge SOP and QC forbid.
- **Fabricated qualifier:** `xref: ... {source="...", source="MONDO:obsoleteEquivalent"}` — `MONDO:obsoleteEquivalent` is not a valid Mondo qualifier; the correct token is `MONDO:equivalentObsolete` (which #100/#165/#375 used). This is the recurring lower-tier error flagged in the case METADATA.
- **Incomplete transfer:** only three synonyms moved to Muenke; the key historical label "glass-chapman-hockley syndrome" itself was *not* added to Muenke as a synonym, so the primary lexical bridge from the historical name to the surviving term is missing — the exact gap @sabrinatoro objected to in #10087.
- **Synonym evidence wrong:** transferred GARD-sourced synonyms re-cited as `[PMID:20108486]` only, dropping the GARD provenance gold keeps.

Net: partial success — right intent, wrong execution. Mixes a correct `TermsMerged`/`replaced_by` with a malformed fat obsolete stanza, a fabricated qualifier, and a missing primary synonym. Not mergeable as-is.
