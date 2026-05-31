---
ontology: uberon
repo: obophenotype/uberon
issue_number: 3583
pr_number: 3588
issue_title: New terms for tooth surfaces
pr_author: aleixpuigb
pr_merged_at: '2025-08-05'
task_type: new_term
difficulty: medium
scoping: tightly_scoped
scope: multi_term
review_outcome: approved_first_time
num_agent_attempts: 9
generated_at: '2026-05-17'
domain_area: dental-anatomy
best_f1: 0.444
best_model: gpt-5.4
---

# PR #3588 — New terms for tooth surfaces

**uberon** | [obophenotype/uberon](https://github.com/obophenotype/uberon) | [Issue #3583](https://github.com/obophenotype/uberon/issues/3583) | [PR #3588](https://github.com/obophenotype/uberon/pull/3588) | @aleixpuigb | merged 2025-08-05

`new_term` `medium` `tightly_scoped` `approved_first_time`

## Context

A request was made to add multiple new terms for tooth surfaces to Uberon. Dental anatomy uses specific terminology for the different surfaces of a tooth (mesial, distal, buccal, lingual, etc.), and these were needed for downstream annotation projects.

## Changes Made

Added approximately 7-8 new tooth surface terms with 75 lines of additions to uberon-edit.obo. Each term followed a consistent pattern with definitions, synonyms, parent class (tooth surface structure), and relationships. The 5 commits suggest iterative refinement of the batch.

## Resolution

Medium difficulty because while each individual term follows a standard pattern, the agent must consistently apply the same modeling approach across multiple terms, ensure no duplication, and get the dental anatomy right for each surface type. The batch nature makes it more complex than a single NTR.

## Curation Note (data quality)

**Flagged `case_quality: poor` — `gold_renegotiated_in_pr_comments` (claude-opus-4.7, 2026-05-16).**

The gold PR #3588 is a faithful, single self-contained PR that resolves issue #3583, but it is a **poor metadiff reference** because the human solution was substantially renegotiated *during PR review*, beyond anything the agent could see:

- **Issue #3583 asked for**: 5 terms (distal, incisal, labial, lingual, mesial); definitions in the form "A tooth surface that…"; parent term **`surface structure` (UBERON:0003102)** directly; ORCID 0000-0001-6677-8489.
- **Issue comments added**: discussion that `facial surface` should parent `labial`/`buccal`, and the clinical "F for facial" shorthand (so a `facial`↔`labial` synonym is warranted). Agents legitimately had this.
- **Introduced only in PR review (not visible to agents)**: reviewer @wdduncan (PR comment 2025-08-02) proposed creating a new intermediate grouping class **`tooth surface structure` (UBERON:8600148)**, `is_a surface structure` + `part_of calcareous tooth`, with `synonym "tooth surface" EXACT`, and reparenting every surface term under it. A multi-round label/definition debate followed ("tooth surface" vs "tooth surface structure", whether surfaces are 2D or 3D, adding a buccal-mucosa gloss). The final gold definitions read "A tooth surface **structure** that…" purely because of this review thread. This is the single biggest structural feature of the gold diff and is unreachable from the issue.

Consequently every agent attempt scores low F1 (~0.36–0.38) by construction. The two attempts are in fact substantively strong: both produced the 5 requested terms with near-verbatim definitions, correctly synthesised the facial/labial/buccal hierarchy from the issue comments, attached `part_of calcareous tooth`, and used the correct contributor ORCID. Attempt #318 (sonnet-4.5) even used the literally-requested `surface structure` parent and added `occlusal` (later independently added by humans in PRs #3603/#3633 as UBERON:8600149, vindicating the instinct). The low F1 is driven by (a) the PR-review-only `tooth surface structure` superclass and definition rewording, and (b) the standard placeholder-vs-canonical UBERON ID artifact (UBERON:99xxxxx vs UBERON:86001xx). Downstream scoring should exclude or heavily down-weight this case, or re-score attempts against the issue + issue comments rather than the renegotiated gold.

No companion PRs are needed to reconstruct the issue resolution (PR #3588 alone fully resolved #3583); `companion_prs` is empty. The later occlusal PRs (#3603, #3632, #3633) are independent follow-ups for a different surface and are not part of this issue's resolution.

## Human Diff

```diff
diff --git a/src/ontology/uberon-edit.obo b/src/ontology/uberon-edit.obo
index a84557c7c..0479f338d 100644
--- a/src/ontology/uberon-edit.obo
+++ b/src/ontology/uberon-edit.obo
@@ -225288,6 +225288,81 @@ intersection_of: part_of UBERON:0001052 ! rectum
 relationship: dc-contributor https://orcid.org/0000-0002-7073-9172 ! David Osumi-Sutherland
 property_value: dcterms-date "2025-05-27T17:07:22Z" xsd:dateTime
 
+[Term]
+id: UBERON:8600141
+name: distal surface of tooth
+def: "A tooth surface structure that is oriented away from the median plane of the dental arch or oral cavity." [https://dentaleducationhub.com/surfaces-of-the-teeth/, https://terminology.hl7.org/CodeSystem-FDI-surface.html]
+is_a: UBERON:8600148 ! tooth surface structure
+relationship: dc-contributor https://orcid.org/0000-0001-6677-8489 ! Aleix Puig-Barbé
+relationship: dc-contributor https://orcid.org/0000-0001-9625-1899
+property_value: dcterms-date "2025-07-24T08:20:48Z" xsd:dateTime
+
+[Term]
+id: UBERON:8600142
+name: incisal surface of tooth
+def: "A tooth surface structure that forms the cutting edge of an incisor or canine tooth. It functions to shear or incise food during biting." [https://dentaleducationhub.com/surfaces-of-the-teeth/, https://terminology.hl7.org/CodeSystem-FDI-surface.html]
+is_a: UBERON:8600148 ! tooth surface structure
+relationship: dc-contributor https://orcid.org/0000-0001-6677-8489 ! Aleix Puig-Barbé
+relationship: dc-contributor https://orcid.org/0000-0001-9625-1899
+property_value: dcterms-date "2025-07-24T08:20:48Z" xsd:dateTime
+
+[Term]
+id: UBERON:8600143
+name: labial surface of tooth
+def: "A tooth surface structure that faces the lips." [https://dentaleducationhub.com/surfaces-of-the-teeth/]
+comment: Tooth surfaces are typically abbreviated using their initial letters. To avoid confusion between 'L' for lingual and labial surfaces, the letter 'F' (for facial surface) is commonly used to refer to the labial surface. {xref="https://orcid.org/0000-0001-9625-1899"}
+synonym: "facial surface of tooth" BROAD []
+is_a: UBERON:8600147 ! facial surface of tooth
+relationship: dc-contributor https://orcid.org/0000-0001-6677-8489 ! Aleix Puig-Barbé
+relationship: dc-contributor https://orcid.org/0000-0001-9625-1899
+property_value: dcterms-date "2025-07-24T08:20:48Z" xsd:dateTime
+
+[Term]
+id: UBERON:8600144
+name: lingual surface of tooth
+def: "A tooth surface structure that faces the tongue or its anatomical equivalent." [https://dentaleducationhub.com/surfaces-of-the-teeth/, https://terminology.hl7.org/CodeSystem-FDI-surface.html]
+is_a: UBERON:8600148 ! tooth surface structure
+relationship: dc-contributor https://orcid.org/0000-0001-6677-8489 ! Aleix Puig-Barbé
+relationship: dc-contributor https://orcid.org/0000-0001-9625-1899
+property_value: dcterms-date "2025-07-24T08:20:48Z" xsd:dateTime
+
+[Term]
+id: UBERON:8600145
+name: mesial surface of tooth
+def: "A tooth surface structure that is oriented toward the median plane of the dental arch." [https://dentaleducationhub.com/surfaces-of-the-teeth/, https://terminology.hl7.org/CodeSystem-FDI-surface.html]
+is_a: UBERON:8600148 ! tooth surface structure
+relationship: dc-contributor https://orcid.org/0000-0001-6677-8489 ! Aleix Puig-Barbé
+relationship: dc-contributor https://orcid.org/0000-0001-9625-1899
+property_value: dcterms-date "2025-07-24T08:20:48Z" xsd:dateTime
+
+[Term]
+id: UBERON:8600146
+name: buccal surface of tooth
+def: "A tooth surface structure that is oriented toward the buccal mucosa (i.e., the inner lining of the cheek)." [https://dentaleducationhub.com/surfaces-of-the-teeth/, https://terminology.hl7.org/CodeSystem-FDI-surface.html]
+is_a: UBERON:8600147 ! facial surface of tooth
+relationship: dc-contributor https://orcid.org/0000-0001-6677-8489 ! Aleix Puig-Barbé
+relationship: dc-contributor https://orcid.org/0000-0001-9625-1899
+property_value: dcterms-date "2025-07-24T08:20:48Z" xsd:dateTime
+
+[Term]
+id: UBERON:8600147
+name: facial surface of tooth
+def: "A tooth surface structure that is oriented toward the lips or cheeks." [https://dentaleducationhub.com/surfaces-of-the-teeth/]
+is_a: UBERON:8600148 ! tooth surface structure
+relationship: dc-contributor https://orcid.org/0000-0001-6677-8489 ! Aleix Puig-Barbé
+relationship: dc-contributor https://orcid.org/0000-0001-9625-1899
+property_value: dcterms-date "2025-07-24T08:20:48Z" xsd:dateTime
+
+[Term]
+id: UBERON:8600148
+name: tooth surface structure
+def: "A surface structure that is part of a calcareous tooth." [PMID:32491475]
+synonym: "tooth surface" EXACT [PMID:32071532]
+intersection_of: UBERON:0003102 ! surface structure
+intersection_of: part_of UBERON:0001091 ! calcareous tooth
+relationship: dc-contributor https://orcid.org/0000-0001-6677-8489 ! Aleix Puig-Barbé
+property_value: dcterms-date "2025-08-05T09:28:57Z" xsd:dateTime
+
 [Term]
 id: UBERON:8700000
 name: aorta-gonad-mesonephros

```

## Agent Attempts (9)

| # | Model | Runtime | F1 | P | R | Blob | Eval PR | Detail |
|---|-------|---------|-----|-----|-----|------|---------|--------|
| 1 | gpt-5.4 | opencode | 0.444 | 0.400 | 0.500 | `977ff8e` | [#667](https://github.com/ai4curation/eval-ont-agent-uberon/pull/667) | [attempt](attempts/pr667.md) |
| 2 | gpt-5.4 | opencode | 0.444 | 0.400 | 0.500 | `977ff8e` | [#608](https://github.com/ai4curation/eval-ont-agent-uberon/pull/608) | [attempt](attempts/pr608.md) |
| 3 | gpt-5.5 | opencode | 0.431 | 0.440 | 0.423 | `80fd07e` | [#628](https://github.com/ai4curation/eval-ont-agent-uberon/pull/628) | [attempt](attempts/pr628.md) |
| 4 | gpt-5.5 | opencode | 0.431 | 0.440 | 0.423 | `80fd07e` | [#570](https://github.com/ai4curation/eval-ont-agent-uberon/pull/570) | [attempt](attempts/pr570.md) |
| 5 | claude-opus-4.7 | claude | 0.379 | 0.440 | 0.333 | `65caaa1` | [#250](https://github.com/ai4curation/eval-ont-agent-uberon/pull/250) | [attempt](attempts/pr250.md) |
| 6 | claude-sonnet-4.5 | claude | 0.364 | 0.400 | 0.333 | `a806812` | [#318](https://github.com/ai4curation/eval-ont-agent-uberon/pull/318) | [attempt](attempts/pr318.md) |
| 7 | claude-haiku-4.5 | claude | 0.341 | 0.280 | 0.438 | `91b605a` | [#566](https://github.com/ai4curation/eval-ont-agent-uberon/pull/566) | [attempt](attempts/pr566.md) |
| 8 | claude-haiku-4.5 | claude | 0.341 | 0.280 | 0.438 | `91b605a` | [#504](https://github.com/ai4curation/eval-ont-agent-uberon/pull/504) | [attempt](attempts/pr504.md) |
| 9 | gpt-5.4 | codex | 0.339 | 0.400 | 0.294 | `d9694a9` | [#394](https://github.com/ai4curation/eval-ont-agent-uberon/pull/394) | [attempt](attempts/pr394.md) |
