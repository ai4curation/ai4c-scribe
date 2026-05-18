---
ontology: uberon
repo: obophenotype/uberon
issue_number: 3414
pr_number: 3499
issue_title: 'NTR: broad ligament regions supporting fallopian tube & tissue layer
  addition'
pr_author: aleixpuigb
pr_merged_at: '2025-04-04'
task_type: new_term
difficulty: hard
scoping: tightly_scoped
scope: multi_term
review_outcome: changes_requested
num_agent_attempts: 13
generated_at: '2026-05-17'
domain_area: reproductive-anatomy
best_f1: 0.226
best_model: gpt-5.4
---

# PR #3499 — NTR: broad ligament regions supporting fallopian tube & tissue layer addition

**uberon** | [obophenotype/uberon](https://github.com/obophenotype/uberon) | [Issue #3414](https://github.com/obophenotype/uberon/issues/3414) | [PR #3499](https://github.com/obophenotype/uberon/pull/3499) | @aleixpuigb | merged 2025-04-04

`new_term` `hard` `tightly_scoped` `changes_requested`

## Context

Issue #3414 requested new terms for the myosalpinx (muscle layer of the fallopian tube), fallopian tube epithelium, and four cardinal regional subdivisions (superior, inferior, mesosalpinx-proximal, antimesosalpinx-proximal) for each tissue layer. This systematic decomposition supports detailed anatomical mapping of the fallopian tube.

## Changes Made

The PR added 83 lines to uberon-edit.obo, creating terms for myosalpinx, fallopian tube epithelium, and eight regional subdivision terms (four regions for each of the two tissue layers). Each term includes a definition, is_a classification, part_of relationships to the parent fallopian tube structure, and appropriate cross-references. Six commits indicate iterative development with review feedback.

## Resolution

Hard difficulty. An agent would need to understand the systematic naming convention for cardinal regions of tubular organs, correctly model the part_of relationships between tissue layers and their regional subdivisions, and ensure consistency across the set of ten new terms. The six commits and five-month timeline from issue to merge suggest substantive review feedback was incorporated.

## Curation Note (data quality)

**Flagged poor by claude-opus-4.7 on 2026-05-16.** This is a poor evaluation case for two compounding reasons; the metadiff F1 (best 0.169, most attempts < 0.12) **drastically under-represents** attempt quality.

1. **Multi-PR human resolution (Step 3a).** Issue #3414 was resolved by two human PRs:
   - **PR #3420** (merged 2024-11-22) added `antimesosalpinx` (UBERON:8600117) and explicitly deferred the layer terms ("not well supported by literature for now").
   - **PR #3499** (the gold, merged 2025-04-04) added `fallopian tube epithelium` plus 8 regional subdivision terms.
   The metadiff scores attempts against #3499 only. #3499 holds most of the 8-term request, so this is not the dominant problem, but it does mean the antimesosalpinx component (already merged via #3420) is invisible to scoring.

2. **Gold renegotiated the spec outside the issue thread (primary).** The issue's authoritative final spec (the 2025-02-13 comment from @aleixpuigb) requested 8 terms with labels like "mesosalpinx epithelium" / "superior muscularus", placed (per the forwarded SME guidance) under `mucosa of fallopian tube` (UBERON:0005048) and `muscle layer of oviduct` (UBERON:0006642), and **explicitly not** `part_of` (anti)mesosalpinx. The gold PR #3499 instead:
   - used different labels ("mesosalpinx-proximal fallopian tube epithelium", "superior fallopian tube epithelium", etc.);
   - introduced a new intermediate parent `fallopian tube epithelium` (UBERON:8600124) that the issue never requested;
   - modeled every regional term as `is_a UBERON:0000064 ! organ part` + `part_of` the layer, rather than under the expert-named mucosa/muscle-layer parents;
   - dropped the "myosalpinx" term that the PR title advertised (commit "Remove repeated term myosalpinx").
   These choices were negotiated in review/commits, not recorded in the issue the agents were given. Agents that faithfully followed the written issue (especially the gpt-5.5/codex #22 and gpt-5.5/opencode #60/#40 runs, with correct `oviduct epithelium` genus and `adjacent_to` polarity modeling) produced ontologically sound, issue-compliant terms but score near-zero against the divergent gold.

**Scoring guidance:** treat attempts on their substantive fidelity to issue #3414's explicit requirements (8 regional layer terms; expert layer placement; polarity-not-partonomy), not the line-level gold. Companion PR: #3420. Best-substance attempts: eval PR #60/#40 (gpt-5.5/opencode, logical defs + adjacent_to) and #22 (gpt-5.5/codex); most curatorially mature: eval PR #239 (claude-opus-4.7, correct 4 terms + targeted clarification request). Genuine failures independent of the poor case: eval PR #285/#179 (claude-haiku-4.5) injected malformed `! Curation contributor !` double-labels into ~20 unrelated dc-contributor lines (agent-introduced corruption; verified absent from source uberon-edit.obo).

## Human Diff

```diff
diff --git a/src/ontology/uberon-edit.obo b/src/ontology/uberon-edit.obo
index 218542b971..d32bd11801 100644
--- a/src/ontology/uberon-edit.obo
+++ b/src/ontology/uberon-edit.obo
@@ -224744,6 +224744,89 @@ intersection_of: part_of UBERON:0001558 ! lower respiratory tract
 relationship: dc-contributor https://orcid.org/0000-0001-6677-8489 ! Aleix Puig-Barbé
 property_value: dcterms-date "2025-02-24T14:15:29Z" xsd:dateTime
 
+[Term]
+id: UBERON:8600124
+name: fallopian tube epithelium
+def: "A simple columnar epithelium that is part of the fallopian tube." [PMID:7714136, Wikipedia:Fallopian_tube]
+is_a: UBERON:0012274 ! columnar epithelium
+intersection_of: UBERON:0000483 ! epithelium
+intersection_of: part_of UBERON:0003889 ! fallopian tube
+relationship: dc-contributor https://orcid.org/0000-0001-6677-8489 ! Aleix Puig-Barbé
+relationship: dc-contributor https://orcid.org/0000-0001-7655-4833 ! Ellen Quardokus
+property_value: dcterms-date "2025-03-04T14:24:07Z" xsd:dateTime
+
+[Term]
+id: UBERON:8600125
+name: superior fallopian tube epithelium
+def: "The superior region of the fallopian tube epithelium." [https://orcid.org/0000-0001-6677-8489]
+is_a: UBERON:0000064 ! organ part
+relationship: dc-contributor https://orcid.org/0000-0001-6677-8489 ! Aleix Puig-Barbé
+relationship: part_of UBERON:8600124 ! fallopian tube epithelium
+property_value: dcterms-date "2025-03-04T14:25:21Z" xsd:dateTime
+
+[Term]
+id: UBERON:8600126
+name: inferior fallopian tube epithelium
+def: "The inferior region of the fallopian tube epithelium." [https://orcid.org/0000-0001-6677-8489]
+is_a: UBERON:0000064 ! organ part
+relationship: dc-contributor https://orcid.org/0000-0001-6677-8489 ! Aleix Puig-Barbé
+relationship: part_of UBERON:8600124 ! fallopian tube epithelium
+property_value: dcterms-date "2025-03-04T14:26:37Z" xsd:dateTime
+
+[Term]
+id: UBERON:8600127
+name: mesosalpinx-proximal fallopian tube epithelium
+def: "The most proximal region to the mesosalpinx of the fallopian tube epithelium." [https://orcid.org/0000-0001-6677-8489]
+is_a: UBERON:0000064 ! organ part
+relationship: dc-contributor https://orcid.org/0000-0001-6677-8489 ! Aleix Puig-Barbé
+relationship: part_of UBERON:8600124 ! fallopian tube epithelium
+property_value: dcterms-date "2025-03-04T14:27:25Z" xsd:dateTime
+
+[Term]
+id: UBERON:8600128
+name: antimesosalpinx-proximal fallopian tube epithelium
+def: "The most proximal region to the antimesosalpinx of the fallopian tube epithelium." [https://orcid.org/0000-0001-6677-8489]
+is_a: UBERON:0000064 ! organ part
+relationship: dc-contributor https://orcid.org/0000-0001-6677-8489 ! Aleix Puig-Barbé
+relationship: part_of UBERON:8600124 ! fallopian tube epithelium
+property_value: dcterms-date "2025-03-04T14:27:50Z" xsd:dateTime
+
+[Term]
+id: UBERON:8600130
+name: superior muscular layer of fallopian tube
+def: "The most superior region of the muscularis layer of the fallopian tube." [https://orcid.org/0000-0001-6677-8489]
+is_a: UBERON:0000064 ! organ part
+relationship: dc-contributor https://orcid.org/0000-0001-6677-8489 ! Aleix Puig-Barbé
+relationship: part_of UBERON:0006642 ! muscle layer of oviduct
+property_value: dcterms-date "2025-03-04T15:32:23Z" xsd:dateTime
+
+[Term]
+id: UBERON:8600131
+name: inferior muscular layer of fallopian tube
+def: "The most inferior region of the muscularis layer of the fallopian tube." [https://orcid.org/0000-0001-6677-8489]
+is_a: UBERON:0000064 ! organ part
+relationship: dc-contributor https://orcid.org/0000-0001-6677-8489 ! Aleix Puig-Barbé
+relationship: part_of UBERON:0006642 ! muscle layer of oviduct
+property_value: dcterms-date "2025-03-04T15:32:52Z" xsd:dateTime
+
+[Term]
+id: UBERON:8600132
+name: mesosalpinx-proximal muscular layer of fallopian tube
+def: "The most proximal region to the mesosalpinx of the muscularis layer of the fallopian tube." [https://orcid.org/0000-0001-6677-8489]
+is_a: UBERON:0000064 ! organ part
+relationship: dc-contributor https://orcid.org/0000-0001-6677-8489 ! Aleix Puig-Barbé
+relationship: part_of UBERON:0006642 ! muscle layer of oviduct
+property_value: dcterms-date "2025-03-04T15:33:06Z" xsd:dateTime
+
+[Term]
+id: UBERON:8600133
+name: antimesosalpinx-proximal muscular layer of fallopian tube
+def: "The most proximal region to the antimesosalpinx of the muscularis layer of the fallopian tube." [https://orcid.org/0000-0001-6677-8489]
+is_a: UBERON:0000064 ! organ part
+relationship: dc-contributor https://orcid.org/0000-0001-6677-8489 ! Aleix Puig-Barbé
+relationship: part_of UBERON:0006642 ! muscle layer of oviduct
+property_value: dcterms-date "2025-03-04T15:33:17Z" xsd:dateTime
+
 [Term]
 id: UBERON:8700000
 name: aorta-gonad-mesonephros

```

## Agent Attempts (13)

| # | Model | Runtime | F1 | P | R | Blob | Eval PR | Detail |
|---|-------|---------|-----|-----|-----|------|---------|--------|
| 1 | gpt-5.4 | opencode | 0.226 | 0.231 | 0.222 | `cecb942` | [#656](https://github.com/ai4curation/eval-ont-agent-uberon/pull/656) | [attempt](attempts/pr656.md) |
| 2 | gpt-5.4 | opencode | 0.226 | 0.231 | 0.222 | `cecb942` | [#596](https://github.com/ai4curation/eval-ont-agent-uberon/pull/596) | [attempt](attempts/pr596.md) |
| 3 | gpt-5.5 | codex | 0.169 | 0.192 | 0.152 | `aa065cd` | [#22](https://github.com/ai4curation/eval-ont-agent-uberon/pull/22) | [attempt](attempts/pr22.md) |
| 4 | gemma-4-31b | opencode | 0.122 | 0.115 | 0.130 | `b6c00f5` | [#157](https://github.com/ai4curation/eval-ont-agent-uberon/pull/157) | [attempt](attempts/pr157.md) |
| 5 | gemma-4-31b | opencode | 0.122 | 0.115 | 0.130 | `b6c00f5` | [#156](https://github.com/ai4curation/eval-ont-agent-uberon/pull/156) | [attempt](attempts/pr156.md) |
| 6 | claude-sonnet-4.5 | claude | 0.109 | 0.115 | 0.103 | `d1787a7` | [#311](https://github.com/ai4curation/eval-ont-agent-uberon/pull/311) | [attempt](attempts/pr311.md) |
| 7 | claude-sonnet-4.5 | copilot | 0.109 | 0.115 | 0.103 | `2099636` | [#195](https://github.com/ai4curation/eval-ont-agent-uberon/pull/195) | [attempt](attempts/pr195.md) |
| 8 | gpt-5.5 | opencode | 0.092 | 0.115 | 0.077 | `14f7383` | [#60](https://github.com/ai4curation/eval-ont-agent-uberon/pull/60) | [attempt](attempts/pr60.md) |
| 9 | gpt-5.5 | opencode | 0.092 | 0.115 | 0.077 | `14f7383` | [#40](https://github.com/ai4curation/eval-ont-agent-uberon/pull/40) | [attempt](attempts/pr40.md) |
| 10 | claude-haiku-4.5 | claude | 0.085 | 0.077 | 0.095 | `01fe438` | [#285](https://github.com/ai4curation/eval-ont-agent-uberon/pull/285) | [attempt](attempts/pr285.md) |
| 11 | claude-haiku-4.5 | claude | 0.085 | 0.077 | 0.095 | `01fe438` | [#179](https://github.com/ai4curation/eval-ont-agent-uberon/pull/179) | [attempt](attempts/pr179.md) |
| 12 | claude-opus-4.7 | claude | 0.073 | 0.077 | 0.069 | `4a1c8ca` | [#239](https://github.com/ai4curation/eval-ont-agent-uberon/pull/239) | [attempt](attempts/pr239.md) |
| 13 | gpt-5.4 | codex | 0.065 | 0.077 | 0.056 | `7c3aff9` | [#391](https://github.com/ai4curation/eval-ont-agent-uberon/pull/391) | [attempt](attempts/pr391.md) |
