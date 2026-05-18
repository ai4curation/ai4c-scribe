---
ontology: uberon
issue_number: 3602
pr_number: 3603
eval_repo_pr: 571
agent: std_opencode_gpt55
model: gpt-5.5
runtime: opencode
agent_config_tag: ai4curation/uberon-agent-config@v3
case_type: new_term
difficulty: simple
case_quality: good
f1: 0.769
precision: 0.833
recall: 0.714
jaccard: 0.625
outcome: success
failure_modes: []
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-17
---

## Summary

gpt-5.5/opencode added `UBERON:8600149` "occlusal surface of tooth" as a
subclass of `UBERON:8600148` "tooth surface structure" with the correct ID,
name, *both* definition cross-references (`dentaleducationhub.com` + HL7
`CodeSystem-FDI-surface.html`), EXACT synonym `"occlusal surface"` with the
dentaleducationhub reference, correct `is_a` parent, and wdduncan's requester
ORCID `0000-0001-9625-1899`. The only substantive divergence from the gold
is one extra word in the definition: "...molar or premolar **tooth**." vs the
gold's "...molar or premolar." Metadiff F1=0.769 (P=0.833, R=0.714)
**under-represents** quality: the gap is the def-wording variant plus the two
CLAUDE.md-mandated metadata lines and one trailing-newline reserialization
artifact. The trailing word is a defensible, arguably clearer phrasing and
not an error — `success`.

## Strengths

- **Correct term skeleton**: id `UBERON:8600149`, name `occlusal surface of
  tooth`, `is_a: UBERON:8600148 ! tooth surface structure` as requested by
  @wdduncan in the issue body.
- **Both definition xrefs preserved**: `dentaleducationhub.com` and the HL7
  `CodeSystem-FDI-surface.html` — matching the two cross-references in issue
  #3602 and the gold's two-xref def (haiku attempts #501/#373 dropped the
  HL7 one; gpt-5.5 kept it).
- **Correct synonym and ORCID**: EXACT synonym `"occlusal surface"` with the
  dentaleducationhub reference @aleixpuigb specified; `relationship:
  dc-contributor https://orcid.org/0000-0001-9625-1899` — the exact ORCID
  the gold uses.
- **Followed CLAUDE.md metadata guidance**: added `term_tracker_item`
  pointing at issue #3602 (absent from the minimal gold, hence part of the
  recall dip but correct practice).

## Issues

- **Definition wording variant (style, not error)**: "...biting or grinding
  surface of a molar or premolar **tooth**." adds "tooth" relative to the
  gold/issue-body definition "...of a molar or premolar." This is the main
  metadiff-divergent line. It is grammatically defensible and arguably
  clearer, but deviates from the verbatim wording supplied in issue #3602;
  an exact reproduction would have matched the gold. Minor style point, not
  scored as a failure mode.
- **robot-convert trailing-newline churn (artifact)**: one EOF blank-line
  removal in the typedef block from the mandated reserialization; benign.
- **No genuine ontological issues.** Substantively the term is correct and
  complete.
