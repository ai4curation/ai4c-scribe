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
num_agent_attempts: 10
generated_at: '2026-05-15'
domain_area: reproductive-anatomy
best_f1: 0.169
best_model: gpt-5.5
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

## Agent Attempts (10)

| # | Model | Runtime | F1 | P | R | Blob | Eval PR | Detail |
|---|-------|---------|-----|-----|-----|------|---------|--------|
| 1 | gpt-5.5 | codex | 0.169 | 0.192 | 0.152 | `aa065cd` | [#22](https://github.com/ai4curation/eval-ont-agent-uberon/pull/22) | [attempt](attempts/pr22.md) |
| 2 | gemma-4-31b | opencode | 0.122 | 0.115 | 0.130 | `b6c00f5` | [#157](https://github.com/ai4curation/eval-ont-agent-uberon/pull/157) | [attempt](attempts/pr157.md) |
| 3 | gemma-4-31b | opencode | 0.122 | 0.115 | 0.130 | `b6c00f5` | [#156](https://github.com/ai4curation/eval-ont-agent-uberon/pull/156) | [attempt](attempts/pr156.md) |
| 4 | claude-sonnet-4.5 | claude | 0.109 | 0.115 | 0.103 | `d1787a7` | [#311](https://github.com/ai4curation/eval-ont-agent-uberon/pull/311) | [attempt](attempts/pr311.md) |
| 5 | claude-sonnet-4.5 | copilot | 0.109 | 0.115 | 0.103 | `2099636` | [#195](https://github.com/ai4curation/eval-ont-agent-uberon/pull/195) | [attempt](attempts/pr195.md) |
| 6 | gpt-5.5 | opencode | 0.092 | 0.115 | 0.077 | `14f7383` | [#60](https://github.com/ai4curation/eval-ont-agent-uberon/pull/60) | [attempt](attempts/pr60.md) |
| 7 | gpt-5.5 | opencode | 0.092 | 0.115 | 0.077 | `14f7383` | [#40](https://github.com/ai4curation/eval-ont-agent-uberon/pull/40) | [attempt](attempts/pr40.md) |
| 8 | claude-haiku-4.5 | claude | 0.085 | 0.077 | 0.095 | `01fe438` | [#285](https://github.com/ai4curation/eval-ont-agent-uberon/pull/285) | [attempt](attempts/pr285.md) |
| 9 | claude-haiku-4.5 | claude | 0.085 | 0.077 | 0.095 | `01fe438` | [#179](https://github.com/ai4curation/eval-ont-agent-uberon/pull/179) | [attempt](attempts/pr179.md) |
| 10 | claude-opus-4.7 | claude | 0.073 | 0.077 | 0.069 | `4a1c8ca` | [#239](https://github.com/ai4curation/eval-ont-agent-uberon/pull/239) | [attempt](attempts/pr239.md) |
