---
ontology: mondo
issue_number: 9909
pr_number: 10208
eval_repo_pr: 396
agent: std_claude_op47
model: claude-opus-4.7
runtime: claude
agent_config_tag: v3
case_type: synonym_update
difficulty: simple
f1: 0.2
precision: 0.125
recall: 0.5
jaccard: 0.111
outcome: partial_success
failure_modes: [under_editing, missed_requirement]
case_quality: poor
case_quality_reason: gold_uses_curator_orcid_source_and_expansive_reinterpretation
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

## Summary

The agent correctly identified MONDO:0015912, added the missing `MATINS` synonym, repaired the
empty-bracket citation on `MYH9-related disease`, and added the issue term tracker — three of the
nine line-changes the curator made. The metadiff F1=0.200 substantially **under-represents** the
quality here: the agent's edit is internally coherent, well-sourced, and faithfully implements the
maintainer's stated resolution; it cannot match gold partly because the gold PR also performed six
RELATED→EXACT scope promotions the issue did not literally ask for, and partly because the gold
sources MATINS and `MYH9-related disease` to the curator's personal ORCID
(`https://orcid.org/0000-0001-9310-0163`), a token no agent can guess. This is the best attempt
in the cohort and the only one that read and quoted MeeSiing's curator comment correctly.

## Strengths

- Read the issue thread carefully and explicitly grounded its plan in @MeeSiing's resolution
  comment ("keep the other synonyms since OMIM still lists them"), correctly declining to remove
  Epstein/Fechtner/May-Hegglin/Sebastian — matching the curator's actual decision against the
  requester's literal ask.
- Added `MATINS` — the single genuinely missing synonym — exactly as the gold did (the gold added
  the same `synonym: "MATINS"` line). Used a defensible source rationale (OMIM:155100, the entry
  whose title yields the acronym) plus the issue URL.
- Fixed the policy-violating empty `[]` citation on `synonym: "MYH9-related disease" EXACT []`,
  choosing `Orphanet:182050` by analogy to the sibling MYH9-related disorder/syndrome synonyms —
  a sound provenance heuristic (gold instead used the curator ORCID, an unguessable token).
- Added `property_value: IAO:0000233 ".../issues/9909"` term tracker, byte-identical to gold.
- Transparent PR comment: audited each requester-preferred synonym for presence, flagged the
  open sourcing question for reviewers, and honestly noted `make NORM` could not run (no ODK image).

## Issues

- Under-editing (the dominant gap): missed the six RELATED→EXACT scope promotions the curator
  made — `Alport syndrome with macrothrombocytopenia`, `FTNS`, `macrothrombocytopenia progressive
  deafness`, `MHA`, `MYH9 related disorders`, `SBS`. These reflect the curator's view that the
  historical names are *exact* synonyms of the unified MYH9-RD concept; the issue text did not
  request them, so missing them is defensible but is the reason recall is 0.5.
- Source divergence on MATINS / MYH9-related disease: agent used `OMIM:155100`/`Orphanet:182050`
  + issue URL; gold used the curator's ORCID. The agent's choice is arguably *better* practice
  (ORCID-as-synonym-source is unusual), but it guarantees a metadiff miss on those lines.
- Did not run normalization (environment limitation, honestly disclosed) — not an agent fault.
