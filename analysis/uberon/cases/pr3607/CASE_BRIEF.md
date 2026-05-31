---
ontology: uberon
repo: obophenotype/uberon
issue_number: 3604
pr_number: 3607
issue_title: dGTEx terms needed in Uberon
pr_author: dragon-ai-agent
pr_merged_at: '2025-09-11'
task_type: new_term
difficulty: medium
scoping: mostly_scoped
scope: single_term
review_outcome: approved_first_time
num_agent_attempts: 8
generated_at: '2026-05-17'
scoping_notes: The issue requested multiple dGTEx terms but this PR only addresses
  the kidney interpolar region. Other terms from the same issue were handled in separate
  PRs.
domain_area: renal-anatomy
best_f1: 0.889
best_model: claude-haiku-4.5
---

# PR #3607 — dGTEx terms needed in Uberon

**uberon** | [obophenotype/uberon](https://github.com/obophenotype/uberon) | [Issue #3604](https://github.com/obophenotype/uberon/issues/3604) | [PR #3607](https://github.com/obophenotype/uberon/pull/3607) | @dragon-ai-agent | merged 2025-09-11

`new_term` `medium` `mostly_scoped` `approved_first_time`

## Context

The dGTEx (developmental Genotype-Tissue Expression) project needed several anatomical terms added to Uberon. This PR addressed one of those terms: the kidney interpolar region, which is the central portion of the kidney between the upper and lower poles.

## Changes Made

Added UBERON:7770009 "kidney interpolar region" with synonyms ("central pole of kidney", "interpolar region of kidney"), a definition, is_a organ part classification, and part_of kidney relationship. Attribution was included via ORCID for the requesting contributor.

## Resolution

Medium difficulty because the agent must understand renal anatomy well enough to define the interpolar region correctly and place it in the partonomy. The term also needed proper contributor attribution. This was one term from a multi-term request, so the agent needed to scope appropriately.

## Curation Note (data quality)

Flagged by claude-opus-4.7 on 2026-05-16 after detailed review of all three
attempts. `case_quality: ok` (not `poor`) — the case is a legitimate,
well-scoped NTR and gold #3607 is the complete, sole resolution for this term
(no companion PRs; other dGTEx terms in issue #3604 are out of scope for this
PR by design). The flag records two scoring caveats so downstream aggregation
does not misread the F1 spread:

1. **robot-convert reserialization churn (primary).** The uberon-agent-config
   `CLAUDE.md` explicitly instructs agents to reserialize
   `src/ontology/uberon-edit.obo` with `robot convert ... -f obo` before
   committing. Attempt #255 (opus-4.7) did exactly this; the reserialization
   refreshed `!` label comments on two unrelated referenced terms
   (`CL:0000649` "prickle cell"→"spinous cell of epidermis"; `GO:0098643`
   "banded collagen fibril"→"fibrillar collagen", x2) from the current import
   closure. These 3 cosmetic comment-only hunks (IDs/axioms unchanged) drop
   #255's recall to 0.471 / F1 to 0.615. They appear ONLY in #255, not in
   #166/#287, so this is reserialization churn, not eval-base contamination.
   Net effect: whole-file metadiff most penalizes the attempt that most
   faithfully followed its documented instructions. All three attempts produce
   a substantively correct kidney interpolar region term.

2. **Gold def-source choice is weaker than two attempts.** Issue #3604's body
   explicitly states the definition "is already defined in NCIT ...
   NCIT_C186124", yet gold #3607 paraphrased and cited `[Wikipedia:Kidney]`
   with no NCIT xref. Attempts #287 and #255 added `xref: NCIT:C186124`
   (and #255 used NCIT's verbatim definition + the NCIT "Kidney, Middle"
   synonym), which is arguably more provenance-correct than gold. The recall
   loss they incur for this extra (correct) cross-reference should be read as
   an improvement over gold, not as scope creep.

Reviewer verdict per attempt: #166 (haiku, F1 0.889) success — best,
gold-equivalent; #287 (sonnet, F1 0.842) success — gold-equivalent + better
NCIT provenance; #255 (opus, F1 0.615) success substantively — most
source-faithful, F1 artifact of mandated reserialization, only minor real
issue is the missing `! Deanne Taylor` label on `dc-contributor`.

## Human Diff

```diff
diff --git a/src/ontology/uberon-edit.obo b/src/ontology/uberon-edit.obo
index 138990fd8..4dfe3a275 100644
--- a/src/ontology/uberon-edit.obo
+++ b/src/ontology/uberon-edit.obo
@@ -221432,6 +221432,19 @@ intersection_of: part_of UBERON:0001159 ! sigmoid colon
 relationship: dc-contributor https://orcid.org/0000-0002-7073-9172 ! David Osumi-Sutherland
 property_value: dcterms-date "2025-05-27T17:07:22Z" xsd:dateTime
 
+[Term]
+id: UBERON:7770009
+name: kidney interpolar region
+def: "The middle portion of the kidney situated between the upper pole and the lower pole, representing approximately the middle third of the kidney along its longitudinal axis." [Wikipedia:Kidney]
+synonym: "central pole of kidney" EXACT []
+synonym: "interpolar region of kidney" EXACT []
+is_a: UBERON:0000064 ! organ part
+relationship: part_of UBERON:0002113 ! kidney
+relationship: dc-contributor https://orcid.org/0000-0002-3302-4610 ! Deanne Taylor
+property_value: dcterms-date "2025-09-11T12:00:00Z" xsd:dateTime
+property_value: term_tracker_item "https://github.com/obophenotype/uberon/issues/3604" xsd:anyURI
+created_by: dragon-ai-agent
+
 [Term]
 id: UBERON:8000000
 name: first instar larva stage

```

## Agent Attempts (8)

| # | Model | Runtime | F1 | P | R | Blob | Eval PR | Detail |
|---|-------|---------|-----|-----|-----|------|---------|--------|
| 1 | claude-haiku-4.5 | claude | 0.889 | 0.889 | 0.889 | `9ee79cf` | [#166](https://github.com/ai4curation/eval-ont-agent-uberon/pull/166) | [attempt](attempts/pr166.md) |
| 2 | claude-sonnet-4.5 | claude | 0.842 | 0.889 | 0.800 | `1627b38` | [#287](https://github.com/ai4curation/eval-ont-agent-uberon/pull/287) | [attempt](attempts/pr287.md) |
| 3 | gpt-5.4 | codex | 0.737 | 0.778 | 0.700 | `a8930f9` | [#378](https://github.com/ai4curation/eval-ont-agent-uberon/pull/378) | [attempt](attempts/pr378.md) |
| 4 | gpt-5.4 | opencode | 0.632 | 0.667 | 0.600 | `4d733c0` | [#669](https://github.com/ai4curation/eval-ont-agent-uberon/pull/669) | [attempt](attempts/pr669.md) |
| 5 | gpt-5.5 | opencode | 0.632 | 0.667 | 0.600 | `6a0f085` | [#634](https://github.com/ai4curation/eval-ont-agent-uberon/pull/634) | [attempt](attempts/pr634.md) |
| 6 | gpt-5.4 | opencode | 0.632 | 0.667 | 0.600 | `4d733c0` | [#611](https://github.com/ai4curation/eval-ont-agent-uberon/pull/611) | [attempt](attempts/pr611.md) |
| 7 | gpt-5.5 | opencode | 0.632 | 0.667 | 0.600 | `6a0f085` | [#574](https://github.com/ai4curation/eval-ont-agent-uberon/pull/574) | [attempt](attempts/pr574.md) |
| 8 | claude-opus-4.7 | claude | 0.615 | 0.889 | 0.471 | `f72f514` | [#255](https://github.com/ai4curation/eval-ont-agent-uberon/pull/255) | [attempt](attempts/pr255.md) |
