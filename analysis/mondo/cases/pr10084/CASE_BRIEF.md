---
ontology: mondo
repo: monarch-initiative/mondo
issue_number: 9849
pr_number: 10084
issue_title: Request for new term 'reticular pseudodrusen'
pr_author: MeeSiing
pr_merged_at: '2026-03-30'
task_type: new_term
difficulty: medium
scoping: tightly_scoped
scope: single_term
review_outcome: approved_first_time
num_agent_attempts: 12
generated_at: '2026-05-17'
best_f1: 0.522
best_model: gpt-5.5
---

# PR #10084 — Request for new term 'reticular pseudodrusen'

**mondo** | [monarch-initiative/mondo](https://github.com/monarch-initiative/mondo) | [Issue #9849](https://github.com/monarch-initiative/mondo/issues/9849) | [PR #10084](https://github.com/monarch-initiative/mondo/pull/10084) | @MeeSiing | merged 2026-03-30

`new_term` `medium` `tightly_scoped` `approved_first_time`

## Context

Issue #9849 requested a new term for "reticular pseudodrusen" (also known as subretinal drusenoid deposits/SDD/RPD), which are subretinal deposits located internal to the retinal pigment epithelium. The request included exact synonyms and two abbreviations, a definition, and multiple PMIDs as evidence. The curator noted that one suggested PMID (34752962) was incorrect evidence and excluded it.

## Changes Made

The PR created MONDO:1060213 with 13 additions to mondo-edit.obo. The new term includes the label "reticular pseudodrusen", a revised definition based on the provided PMIDs, exact synonyms ("subretinal drusenoid deposits", "SDD", "RPD"), parent classification, and ORCID-attributed evidence annotations. The curator critically evaluated the suggested references and excluded one that did not support the term.

## Resolution

Moderate difficulty because new term creation requires evaluating evidence quality. The curator demonstrated critical assessment by rejecting an inappropriate PMID while accepting others. The synonym scope decisions (abbreviations as EXACT rather than RELATED) and parent term placement both require ophthalmology domain knowledge. An agent would need literature verification capabilities to replicate this evidence evaluation step.

## Curation Note (data quality)

`case_quality: ok` — this is **not** a poor evaluation case. PR #10084 is the
whole human resolution: a single commit, approved first time by @sabrinatoro,
issue #9849 closed by it, no companion PRs, no curator repudiation, no
post-merge renegotiation. Gold edits real semantic fields (not a
metadiff-ignored field).

A `scoring_caveat` is recorded in the frontmatter because the uniformly
compressed metadiff F1 across all 10 attempts (0.261–0.522) is **normal
metadiff under-representation**, not a poor-case signature, and downstream
aggregation should not treat the low absolute numbers as agent failure:

1. **ID range is structurally penalized.** The eval scores agents against the
   curator's post-merge canonical ID `MONDO:1060213`. The agent config
   (`ai4curation/mondo-agent-config@v3`, `CLAUDE.md`) explicitly instructs:
   "New terms start MONDO:777xxxx". Every well-formed attempt therefore used
   `MONDO:7770012` and mismatches gold on the ~6 of ~13 stanza lines that
   contain the ID — by construction, not by error. Agents that used the
   placeholder range were *following their instructions correctly*.
2. **`dcterms:creator` convention.** Gold uses the curator ORCID
   `0000-0002-7638-4659` (matching the config's own NTR template example).
   Most attempts used the requester ORCID `0000-0001-6677-8489` — a genuine
   (minor) convention deviation, but it compounds the metadiff gap.
3. **Definition/comment split + singular synonym.** Gold rewrote the genus
   ("A retinal drusen characterized by…"), moved the AMD-risk sentence to a
   separate `comment:` field, and used singular "subretinal drusenoid
   deposit". Most agents pasted the issue's raw definition and used the plural.
   Defensible authoring differences that further depress recall.

Recommended adjudication basis (used in the per-attempt reviews): substance
over line-match — correct parent (`MONDO:0006949`), correct synonym
types/qualifiers, correct `SCTID:` xref form, and especially whether the
attempt reproduced the curator's evidence judgment by **excluding the bogus
`PMID:34752962`** ("Monitoring Colonoscopy Quality", Clin Gastroenterol
Hepatol) that the issue body itself flags as wrong evidence. On that axis the
attempts split sharply: codex gpt-5.5 (#92), codex gpt-5.4 (#169) and
claude-opus-4.7 (#373) excluded it (success); copilot sonnet (#333) excluded
it but wrongly dropped the valid `PMID:41361163`; kimi (#272), the two
opencode gpt-5.5 runs (#110/#130), claude-sonnet/claude (#449) and both
haiku-4.5 runs (#479/#417) propagated the bogus PMID (partial_success). The
two haiku runs additionally used the wrong datatype `xsd:string` on the
`IAO:0000233` tracker annotation (should be `xsd:anyURI`).

Flagged by claude-opus-4.7, 2026-05-15.

## Human Diff

```diff
diff --git a/src/ontology/mondo-edit.obo b/src/ontology/mondo-edit.obo
index dcc3e5d075..a7ba7db4bd 100644
--- a/src/ontology/mondo-edit.obo
+++ b/src/ontology/mondo-edit.obo
@@ -672765,6 +672765,19 @@ relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/
 property_value: http://purl.org/dc/terms/creator https://orcid.org/0000-0002-7638-4659
 property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9774" xsd:anyURI
 
+[Term]
+id: MONDO:1060213
+name: reticular pseudodrusen
+def: "A retinal drusen characterized by subretinal deposits located internal to the retinal pigment epithelium, composed of material aggregations in the subretinal space between photoreceptors and the retinal pigment epithelium. These deposits have a bluish-white appearance by biomicroscopy and appear as hyperreflective lesions above the retinal pigment epithelium on optical coherence tomography." [https://orcid.org/0000-0001-6677-8489, PMID:29859199, PMID:38386332, PMID:41361163]
+comment: Reticular pseudodrusen are a strong independent risk factor for late age-related macular degeneration and are particularly associated with geographic atrophy and type 3 neovascularization.
+synonym: "RPD" EXACT ABBREVIATION [https://orcid.org/0000-0001-6677-8489, PMID:29859199]
+synonym: "SDD" EXACT ABBREVIATION [https://orcid.org/0000-0001-6677-8489, PMID:29859199]
+synonym: "subretinal drusenoid deposit" EXACT [https://orcid.org/0000-0001-6677-8489, PMID:29859199, PMID:38386332]
+xref: SCTID:762533006 {source="MONDO:equivalentTo"}
+is_a: MONDO:0006949 {source="PMID:29859199", source="https://orcid.org/0000-0001-6677-8489"} ! retinal drusen
+property_value: http://purl.org/dc/terms/creator https://orcid.org/0000-0002-7638-4659
+property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9849" xsd:anyURI
+
 [Term]
 id: MONDO:7770001
 name: equine juvenile spinocerebellar ataxia, FDXR-related, horse

```

## Agent Attempts (12)

| # | Model | Runtime | F1 | P | R | Blob | Eval PR | Detail |
|---|-------|---------|-----|-----|-----|------|---------|--------|
| 1 | gpt-5.5 | codex | 0.522 | 0.500 | 0.545 | `9363079` | [#92](https://github.com/ai4curation/eval-ont-agent-mondo/pull/92) | [attempt](attempts/pr92.md) |
| 2 | gpt-5.4 | opencode | 0.435 | 0.417 | 0.455 | `1f4ac96` | [#732](https://github.com/ai4curation/eval-ont-agent-mondo/pull/732) | [attempt](attempts/pr732.md) |
| 3 | gpt-5.4 | opencode | 0.435 | 0.417 | 0.455 | `1f4ac96` | [#679](https://github.com/ai4curation/eval-ont-agent-mondo/pull/679) | [attempt](attempts/pr679.md) |
| 4 | kimi-k2.6 | opencode | 0.435 | 0.417 | 0.455 | `691ecee` | [#272](https://github.com/ai4curation/eval-ont-agent-mondo/pull/272) | [attempt](attempts/pr272.md) |
| 5 | claude-sonnet-4.5 | copilot | 0.417 | 0.417 | 0.417 | `e05bf91` | [#333](https://github.com/ai4curation/eval-ont-agent-mondo/pull/333) | [attempt](attempts/pr333.md) |
| 6 | gpt-5.4 | codex | 0.417 | 0.417 | 0.417 | `95aff92` | [#169](https://github.com/ai4curation/eval-ont-agent-mondo/pull/169) | [attempt](attempts/pr169.md) |
| 7 | claude-opus-4.7 | claude | 0.348 | 0.333 | 0.364 | `9057ac2` | [#373](https://github.com/ai4curation/eval-ont-agent-mondo/pull/373) | [attempt](attempts/pr373.md) |
| 8 | gpt-5.5 | opencode | 0.348 | 0.333 | 0.364 | `f5b1ef9` | [#130](https://github.com/ai4curation/eval-ont-agent-mondo/pull/130) | [attempt](attempts/pr130.md) |
| 9 | gpt-5.5 | opencode | 0.348 | 0.333 | 0.364 | `f5b1ef9` | [#110](https://github.com/ai4curation/eval-ont-agent-mondo/pull/110) | [attempt](attempts/pr110.md) |
| 10 | claude-sonnet-4.5 | claude | 0.333 | 0.333 | 0.333 | `bcf6f27` | [#449](https://github.com/ai4curation/eval-ont-agent-mondo/pull/449) | [attempt](attempts/pr449.md) |
| 11 | claude-haiku-4.5 | claude | 0.261 | 0.250 | 0.273 | `56c6aed` | [#479](https://github.com/ai4curation/eval-ont-agent-mondo/pull/479) | [attempt](attempts/pr479.md) |
| 12 | claude-haiku-4.5 | claude | 0.261 | 0.250 | 0.273 | `56c6aed` | [#417](https://github.com/ai4curation/eval-ont-agent-mondo/pull/417) | [attempt](attempts/pr417.md) |
