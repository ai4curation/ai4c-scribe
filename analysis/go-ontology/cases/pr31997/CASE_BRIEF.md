---
ontology: go-ontology
repo: geneontology/go-ontology
issue_number: 27593
pr_number: 31997
issue_title: NTR ferric iron reductase (for non siderophore)
pr_author: dragon-ai-agent
pr_merged_at: '2026-04-28'
task_type: new_term
difficulty: hard
scoping: tightly_scoped
scope: single_term
review_outcome: approved_first_time
num_agent_attempts: 9
generated_at: '2026-05-15'
best_f1: 1.0
best_model: gpt-5.5
---

# PR #31997 — NTR ferric iron reductase (for non siderophore)

**go-ontology** | [geneontology/go-ontology](https://github.com/geneontology/go-ontology) | [Issue #27593](https://github.com/geneontology/go-ontology/issues/27593) | [PR #31997](https://github.com/geneontology/go-ontology/pull/31997) | @dragon-ai-agent | merged 2026-04-28

`new_term` `hard` `tightly_scoped` `approved_first_time`

## Context

A new term request for ferric iron reductase activity was filed in April 2024 to support GO-CAM modeling. The existing GO terms for iron reduction were tied to siderophore-mediated processes, but many organisms reduce ferric iron (Fe3+) to ferrous iron (Fe2+) through non-siderophore mechanisms using NADPH as the electron donor. The first attempt at this PR (#31797) was closed due to a GO ID collision where the allocated ID had already been used by a parallel branch.

## Changes Made

The PR added GO:7770068 `ferric iron reductase activity` as a new molecular function term with the reaction `2 Fe2+ + NADP+ + H+ = 2 Fe3+ + NADPH` cross-referenced to RHEA:71767 (skos:exactMatch). The term was placed under GO:0016723 (oxidoreductase activity, acting on metal ions, NAD or NADP as acceptor). The definition referenced PMID:8321236. Additionally, the existing term GO:0000293 was updated to reflect its relationship to the new term.

## Resolution

Hard difficulty due to several factors: the issue was open for over two years, a previous PR attempt failed due to ID collision (requiring careful ID allocation), and the definition needed precise alignment with the RHEA reaction database. The parent term selection required understanding the enzyme classification hierarchy for oxidoreductases acting on metal ion substrates with NAD(P) as acceptor.

## Human Diff

```diff
diff --git a/src/ontology/go-edit.obo b/src/ontology/go-edit.obo
index 5b4d6c89f..8ab446b18 100644
--- a/src/ontology/go-edit.obo
+++ b/src/ontology/go-edit.obo
@@ -3208,12 +3208,13 @@ intersection_of: has_primary_input SO:0000587 ! group_I_intron
 id: GO:0000293
 name: ferric-chelate reductase activity
 namespace: molecular_function
-def: "Catalysis of the reaction: 2 Fe3+-siderophore + electron donor = 2 Fe2+-siderophore + electron acceptor." [PMID:33559753]
+def: "Catalysis of the reaction: 2 Fe3+-chelate + electron donor = 2 Fe2+-chelate + electron acceptor." [PMID:33559753]
 synonym: "ferric chelate reductase activity" EXACT []
 synonym: "iron chelate reductase activity" EXACT []
-is_a: GO:0016722 ! oxidoreductase activity, acting on metal ions
+is_a: GO:7770068 ! ferric iron reductase activity
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/21029" xsd:anyURI
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/26726" xsd:anyURI
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/27593" xsd:anyURI
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30815" xsd:anyURI
 
 [Term]
@@ -617387,6 +617388,19 @@ property_value: term_tracker_item "https://github.com/geneontology/go-ontology/i
 created_by: dragon-ai-agent
 creation_date: 2026-04-21T19:33:16Z
 
+[Term]
+id: GO:7770068
+name: ferric iron reductase activity
+namespace: molecular_function
+def: "Catalysis of the reaction: 2 Fe2+ + NADP+ + H+ = 2 Fe3+ + NADPH." [PMID:8321236, PMID:34614242, PMID:39940646, RHEA:71767]
+synonym: "ferric reductase activity" EXACT []
+synonym: "Fe3+ reductase activity" EXACT []
+xref: RHEA:71767 {source="skos:exactMatch"}
+is_a: GO:0016723 ! oxidoreductase activity, acting on metal ions, NAD or NADP as acceptor
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/27593" xsd:anyURI
+created_by: dragon-ai-agent
+creation_date: 2026-04-28T09:37:41Z
+
 [Typedef]
 id: acts_on_population_of
 name: acts on population of

```

## Agent Attempts (9)

### Attempt 1: gpt-5.5 / codex

- **Eval PR**: [#73](https://github.com/ai4curation/eval-ont-agent-go/pull/73)
- **F1**: 1.000  **Precision**: 1.000  **Recall**: 1.000  **Jaccard**: 1.000
- **Trace**: [25615878020](https://github.com/ai4curation/eval-ont-agent-go/tree/master/traces/25615878020)
- **Workflow run**: [25615878020](https://github.com/ai4curation/eval-ont-agent-go/actions/runs/25615878020)

#### Agent PR Comment

## Summary

This PR addresses issue #27593 by adding a new molecular function term:

- `GO:7770068` ferric iron reductase activity

The term uses the RHEA:71767 equation:

`2 Fe2+ + NADP+ + H+ = 2 Fe3+ + NADPH`

It includes:

- definition xrefs: `PMID:8321236`, `PMID:34614242`, `PMID:39940646`, `RHEA:71767`
- exact synonym: `ferric reductase activity`
- exact synonym: `Fe3+ reductase activity`
- exact Rhea mapping: `xref: RHEA:71767 {source="skos:exactMatch"}`
- parent: `GO:0016723` oxidoreductase activity, acting on metal ions, NAD or NADP as acceptor
- term tracker link to issue #27593

`GO:0000293` ferric-chelate reductase activity was also updated:

- definition changed from Fe3+-siderophore/Fe2+-siderophore to Fe3+-chelate/Fe2+-chelate
- asserted parent changed to the new `GO:7770068`
- term tracker link to issue #27593 added

I changed both sides of the `GO:0000293` reaction to chelate. The issue text requested chelate on the substrate side while leaving siderophore on the product side, but the chelating agent should not become a siderophore during the redox reaction.

## Rationale

The issue requests a ferric iron reductase term for curation where the activity is ferric iron reduction rather than ferric-siderophore reduction. RHEA:71767 is available for the unchelated ferric/ferrous iron NADP/NADPH reaction, and the requested references support the ferric reductase activity and biological context.

The current branch already uses `GO:7770057` for a different term, so this reimplementation uses the next available local ID, `GO:7770068`.

## Validation

- Baseline pre-validation before ontology edits: `cd src/ontology && make travis_build` passed.
- Post-change validation: `cd src/ontology && make travis_build` passed.
- `linkml-reference-validator` was used to cache and validate the PMID support excerpts in `RESEARCH.md`; all three PMID support excerpts validated.
- RHEA:71767 was checked in the local Rhea RDF and on the Rhea site; it is approved and has the equation used in the new term.

## Checklist

- [x] PLAN: Issue context and comments were reviewed; the final request is clear.
- [x] PRE-VALIDATION: Current ontology validated before edits.
- [x] RESEARCH: `RESEARCH.md` created with validated PMID support.
- [x] TERM-SEARCH: Existing GO ferric-chelate/ferric reductase terms and parent terms checked.
- [x] DESIGN-PATTERNS: `DESIGN_PATTERNS.md` created; no `intersection_of` axioms added.
- [x] EDITS: Used `obo-checkout.pl`/`obo-checkin.pl` and edited only term stanzas in `terms/`.
- [x] RELATIONSHIPS: Added appropriate asserted `is_a` parentage and avoided over-specifying logical definitions.
- [x] SPECIALIZED-EDITS: Used reaction, mapping, chemical-entity, and external lookup guidance for RHEA/CHEBI participants and xref semantics.
- [x] METADATA: Added `created_by`, `creation_date`, and `term_tracker_item` for the new term only; added issue tracker link to modified existing term.
- [x] AUTOMATED-VALIDATION: `make travis_build` passed after changes.
- [x] REFERENCE-VALIDATION: PMID references and RHEA reaction were validated.
- [x] CHANGES-COMMITTED: `src/ontology/go-edit.obo` committed locally.

---
🤖 **Generated by codex agent**
- Runtime: `codex`
- Model: `gpt-5.5`
- Agent config: `ai4curation/go-ontology-agent-config@v9:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-go/actions/runs/25615878020)


#### Agent Issue Comment

Changes committed in PR #<NN>.

Summary:
- Added `GO:7770068` ferric iron reductase activity, with `RHEA:71767` and the requested PMID references.
- Updated `GO:0000293` ferric-chelate reductase activity to use chelate wording rather than siderophore wording, and classified it under the new ferric iron reductase activity term.

I changed both substrate and product wording in `GO:0000293` from siderophore to chelate, since the chelating agent is not changed by the reduction reaction.

---
🤖 **Generated by codex agent**
- Runtime: `codex`
- Model: `gpt-5.5`
- Agent config: `ai4curation/go-ontology-agent-config@v9:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-go/actions/runs/25615878020)


#### Agent Diff

```diff
diff --git a/src/ontology/go-edit.obo b/src/ontology/go-edit.obo
index 5b4d6c89f..f73e87689 100644
--- a/src/ontology/go-edit.obo
+++ b/src/ontology/go-edit.obo
@@ -3208,12 +3208,13 @@ intersection_of: has_primary_input SO:0000587 ! group_I_intron
 id: GO:0000293
 name: ferric-chelate reductase activity
 namespace: molecular_function
-def: "Catalysis of the reaction: 2 Fe3+-siderophore + electron donor = 2 Fe2+-siderophore + electron acceptor." [PMID:33559753]
+def: "Catalysis of the reaction: 2 Fe3+-chelate + electron donor = 2 Fe2+-chelate + electron acceptor." [PMID:33559753]
 synonym: "ferric chelate reductase activity" EXACT []
 synonym: "iron chelate reductase activity" EXACT []
-is_a: GO:0016722 ! oxidoreductase activity, acting on metal ions
+is_a: GO:7770068 ! ferric iron reductase activity
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/21029" xsd:anyURI
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/26726" xsd:anyURI
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/27593" xsd:anyURI
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30815" xsd:anyURI
 
 [Term]
@@ -617387,6 +617388,19 @@ property_value: term_tracker_item "https://github.com/geneontology/go-ontology/i
 created_by: dragon-ai-agent
 creation_date: 2026-04-21T19:33:16Z
 
+[Term]
+id: GO:7770068
+name: ferric iron reductase activity
+namespace: molecular_function
+def: "Catalysis of the reaction: 2 Fe2+ + NADP+ + H+ = 2 Fe3+ + NADPH." [PMID:8321236, PMID:34614242, PMID:39940646, RHEA:71767]
+synonym: "ferric reductase activity" EXACT []
+synonym: "Fe3+ reductase activity" EXACT []
+xref: RHEA:71767 {source="skos:exactMatch"}
+is_a: GO:0016723 ! oxidoreductase activity, acting on metal ions, NAD or NADP as acceptor
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/27593" xsd:anyURI
+created_by: dragon-ai-agent
+creation_date: 2026-05-10T01:23:47Z
+
 [Typedef]
 id: acts_on_population_of
 name: acts on population of

```

#### Review by gpt-5.5

**outcome**: success  **f1**: 1.0  **precision**: 1.0  **recall**: 1.0

<!-- Review this eval run following analysis/instructions/review-agent-eval.md

  Source issue: https://github.com/geneontology/go-ontology/issues/27593
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/31997
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/73
  Agent config: ai4curation/go-ontology-agent-config

  Quick reference:
    gh issue view 27593 --repo geneontology/go-ontology
    gh pr diff 31997 --repo geneontology/go-ontology
    gh pr diff 73 --repo ai4curation/eval-ont-agent-go
-->

## Summary

The agent successfully addressed issue #27593 by adding `GO:7770068` ferric iron reductase activity for non-siderophore ferric iron reduction contexts, and by updating `GO:0000293` ferric-chelate reductase activity to sit under the new broader term. The metadiff score is perfect (`f1: 1.0`, `precision: 1.0`, `recall: 1.0`) and accurately reflects the substantive result: the agent's ontology edits match the human PR, aside from an expected creation timestamp difference.


## Strengths

- Added the requested new molecular function term `GO:7770068` with the correct label, namespace, definition, definition xrefs (`PMID:8321236`, `PMID:34614242`, `PMID:39940646`, `RHEA:71767`), RHEA exact-match xref, and issue tracker link to geneontology/go-ontology#27593.
- Correctly used `RHEA:71767` for the reaction `2 Fe2+ + NADP+ + H+ = 2 Fe3+ + NADPH`, matching the human solution and providing a non-siderophore ferric iron reductase activity term for the use case described in the issue.
- Placed `GO:7770068` under `GO:0016723` oxidoreductase activity, acting on metal ions, NAD or NADP as acceptor, giving it the same asserted parentage as the human PR.
- Added useful exact synonyms for the new term: "ferric reductase activity" and "Fe3+ reductase activity".
- Updated `GO:0000293` ferric-chelate reductase activity in the same way as the human PR: changed the definition from Fe3+-siderophore/Fe2+-siderophore to Fe3+-chelate/Fe2+-chelate, reparented it from `GO:0016722` to `GO:7770068`, and added the issue tracker link.
- Showed good scope discipline. The agent did not add extra unrelated terms or axioms, and it explicitly noted why both sides of the `GO:0000293` reaction were changed to "chelate" rather than leaving the product as "siderophore".


## Issues

No significant issues found. The agent's diff is substantively equivalent to the human PR; the only visible difference is the `creation_date` timestamp on `GO:7770068`, which is expected for an independently generated edit and not an ontology-quality problem.

### Attempt 2: kimi-k2.6 / opencode

- **Eval PR**: [#269](https://github.com/ai4curation/eval-ont-agent-go/pull/269)
- **F1**: 0.889  **Precision**: 0.857  **Recall**: 0.923  **Jaccard**: 0.800
- **Trace**: [25646677913](https://github.com/ai4curation/eval-ont-agent-go/tree/master/traces/25646677913)
- **Workflow run**: [25646677913](https://github.com/ai4curation/eval-ont-agent-go/actions/runs/25646677913)

#### Agent PR Comment

## Changes for issue #27593 — NTR ferric iron reductase (for non-siderophore)

### Summary

1. **New term created:** GO:7770068 — ferric iron reductase activity
2. **Existing term updated:** GO:0000293 — ferric-chelate reductase activity (definition broadened, new parent added)

---

### New term details: GO:7770068 ferric iron reductase activity

```obo
id: GO:7770068
name: ferric iron reductase activity
namespace: molecular_function
def: "Catalysis of the reaction: 2 Fe2+ + NADP+ + H+ = 2 Fe3+ + NADPH." [PMID:8321236, PMID:34614242, PMID:39940646, RHEA:71767]
synonym: "ferric reductase activity" EXACT []
synonym: "ferrireductase activity" EXACT []
xref: RHEA:71767 {source="skos:exactMatch"}
is_a: GO:0016723 ! oxidoreductase activity, acting on metal ions, NAD or NADP as acceptor
property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/27593" xsd:anyURI
created_by: dragon-ai-agent
creation_date: 2026-05-11T02:38:39Z
```

- **Parentage:** Placed under GO:0016723 (oxidoreductase activity, acting on metal ions, NAD or NADP as acceptor), matching the pattern used by the existing specific child GO:0052851 (ferric-chelate reductase (NADPH) activity).
- **Reaction direction:** The definition follows the RHEA:71767 direction, which is the same convention used by sibling terms GO:0052851 (RHEA:28795) and GO:0140618 (RHEA:15061) in the ontology.
- **References validated:**
  - PMID:8321236 — Roman et al. 1993, original characterization of fission yeast frp1+ ferric reductase
  - PMID:34614242 — Beaudoin et al. 2021, Frp1 regulation by Puf2/Puf4
  - PMID:39940646 — Amadei et al. 2025, review on ferroxidase-permease systems

### Updated term: GO:0000293 ferric-chelate reductase activity

- **Definition change:**
  - **From:** `Catalysis of the reaction: 2 Fe3+-siderophore + electron donor = 2 Fe2+-siderophore + electron acceptor.`
  - **To:** `Catalysis of the reaction: 2 Fe3+-chelate + electron donor = 2 Fe2+-chelate + electron acceptor.`
  - **Rationale:** The substrate was changed from "siderophore" to "chelate" because not all chelates are siderophores. The product side was also changed to "chelate" for chemical consistency — the chelating agent does not change during the reduction reaction. This also aligns with requester intent (see discussion in issue).
- **New parent:** Added `is_a: GO:7770068 ! ferric iron reductase activity`
- **Existing parent retained:** `is_a: GO:0016722 ! oxidoreductase activity, acting on metal ions`

---

### Validation performed

- [x] OBO syntax validated via `robot convert` — passes
- [x] ELK reasoning validated via `robot reason` — passes, no unsatisfiable classes
- [x] Full `make travis_build` was attempted but blocked by missing `amm` dependency in this environment; core `robot` checks pass

### Checklist

- [x] PLAN: Issue analyzed and intent clear
- [x] PRE-VALIDATION: Ontology validates before changes
- [x] RESEARCH: PMIDs and RHEA validated
- [x] TERM-SEARCH: Relevant terms consulted
- [x] DESIGN-PATTERNS: Existing catalytic activity patterns followed
- [x] EDITS: Checkin/checkout procedure followed
- [x] RELATIONSHIPS: Appropriate `is_a` parents added
- [x] METADATA: `term_tracker_item`, `created_by`, `creation_date` included on new term
- [x] AUTOMATED-VALIDATION: `robot convert` and `robot reason` pass
- [x] REFERENCE-VALIDATION: All PMIDs verified
- [x] CHANGES-COMMITTED: `src/ontology/go-edit.obo` committed

---
🤖 **Generated by opencode agent**
- Runtime: `opencode`
- Model: `togetherai/moonshotai/Kimi-K2.6`
- Agent config: `ai4curation/go-ontology-agent-config@v9:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-go/actions/runs/25646677913)


#### Agent Issue Comment

Hi @ValWood — changes for this request have been committed in PR #<NN>.

**Summary of changes:**

- **Added new term: GO:7770068 ferric iron reductase activity**
  - Catalysis of the reaction: `2 Fe2+ + NADP+ + H+ = 2 Fe3+ + NADPH` (RHEA:71767)
  - References: PMID:8321236, PMID:34614242, PMID:39940646
  - Placed under GO:0016723 (oxidoreductase activity, acting on metal ions, NAD or NADP as acceptor)

- **Updated GO:0000293 ferric-chelate reductase activity**
  - Broadened definition from "siderophore" to "chelate" on both substrate and product sides
    (the chelating agent does not change during the reaction, so using "chelate" on both sides is the chemically consistent choice)
  - Added `is_a: GO:7770068` as requested

Let me know if anything needs adjustment.

---
🤖 **Generated by opencode agent**
- Runtime: `opencode`
- Model: `togetherai/moonshotai/Kimi-K2.6`
- Agent config: `ai4curation/go-ontology-agent-config@v9:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-go/actions/runs/25646677913)


#### Agent Diff

```diff
diff --git a/src/ontology/go-edit.obo b/src/ontology/go-edit.obo
index 5b4d6c89f..fc2dabe25 100644
--- a/src/ontology/go-edit.obo
+++ b/src/ontology/go-edit.obo
@@ -3208,10 +3208,11 @@ intersection_of: has_primary_input SO:0000587 ! group_I_intron
 id: GO:0000293
 name: ferric-chelate reductase activity
 namespace: molecular_function
-def: "Catalysis of the reaction: 2 Fe3+-siderophore + electron donor = 2 Fe2+-siderophore + electron acceptor." [PMID:33559753]
+def: "Catalysis of the reaction: 2 Fe3+-chelate + electron donor = 2 Fe2+-chelate + electron acceptor." [PMID:33559753]
 synonym: "ferric chelate reductase activity" EXACT []
 synonym: "iron chelate reductase activity" EXACT []
 is_a: GO:0016722 ! oxidoreductase activity, acting on metal ions
+is_a: GO:7770068 ! ferric iron reductase activity
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/21029" xsd:anyURI
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/26726" xsd:anyURI
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30815" xsd:anyURI
@@ -617387,6 +617388,19 @@ property_value: term_tracker_item "https://github.com/geneontology/go-ontology/i
 created_by: dragon-ai-agent
 creation_date: 2026-04-21T19:33:16Z
 
+[Term]
+id: GO:7770068
+name: ferric iron reductase activity
+namespace: molecular_function
+def: "Catalysis of the reaction: 2 Fe2+ + NADP+ + H+ = 2 Fe3+ + NADPH." [PMID:8321236, PMID:34614242, PMID:39940646, RHEA:71767]
+synonym: "ferric reductase activity" EXACT []
+synonym: "ferrireductase activity" EXACT []
+xref: RHEA:71767 {source="skos:exactMatch"}
+is_a: GO:0016723 ! oxidoreductase activity, acting on metal ions, NAD or NADP as acceptor
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/27593" xsd:anyURI
+created_by: dragon-ai-agent
+creation_date: 2026-05-11T02:38:39Z
+
 [Typedef]
 id: acts_on_population_of
 name: acts on population of

```

### Attempt 3: claude-sonnet-4.5 / copilot

- **Eval PR**: [#386](https://github.com/ai4curation/eval-ont-agent-go/pull/386)
- **F1**: 0.880  **Precision**: 0.786  **Recall**: 1.000  **Jaccard**: 0.786
- **Trace**: [25752250820](https://github.com/ai4curation/eval-ont-agent-go/tree/master/traces/25752250820)
- **Workflow run**: [25752250820](https://github.com/ai4curation/eval-ont-agent-go/actions/runs/25752250820)

#### Agent PR Comment

# Changes for Issue #27593: New Term for Ferric Iron Reductase Activity

## Summary

This PR addresses the need for a ferric iron reductase term suitable for annotating genes like *frp1* in *S. pombe* that reduce ferric iron without requiring siderophores as chelators. The changes include:

1. **New term**: GO:7770068 - ferric iron reductase activity
2. **Updated term**: GO:0000293 - ferric-chelate reductase activity (definition broadened and made subclass of new term)

## Detailed Changes

### 1. New Term: GO:7770068 - ferric iron reductase activity

```
id: GO:7770068
name: ferric iron reductase activity
namespace: molecular_function
def: "Catalysis of the reaction: 2 Fe2+ + NADP+ + H+ = 2 Fe3+ + NADPH." [PMID:8321236, PMID:34614242, PMID:39940646, RHEA:71767]
xref: RHEA:71767 {source="skos:exactMatch"}
is_a: GO:0016723 ! oxidoreductase activity, acting on metal ions, NAD or NADP as acceptor
```

**Rationale**: 
- Describes the reduction of ferric iron (Fe³⁺) to ferrous iron (Fe²⁺) using NADPH as electron donor
- Does not specify chelation requirements, allowing annotation of enzymes that work with unchelated iron
- RHEA:71767 provides the specific balanced chemical reaction
- Parent term GO:0016723 is appropriate for NAD(P)-dependent metal ion reductases

### 2. Updated Term: GO:0000293 - ferric-chelate reductase activity

**Changes made**:
- Definition changed from "2 Fe3+-**siderophore**" to "2 Fe3+-**chelate**" (both substrate and product sides)
- Added `is_a: GO:7770068` relationship
- Added term_tracker_item for issue #27593

**Rationale**:
- "Chelate" is broader than "siderophore" - not all iron chelates are siderophores
- Making GO:0000293 a subclass of GO:7770068 creates a logical hierarchy
- Previous definition was too restrictive for chelate-dependent (non-siderophore) iron reduction

## Biological Context

From the issue discussion and research:

- **frp1** in *S. pombe* encodes a cell surface ferrireductase required for ferric iron uptake (Roman et al. 1993, PMID:8321236)
- This enzyme reduces Fe³⁺ to Fe²⁺ prior to transport through the Fio1/Frp1 complex
- **NOT** involved in siderophore-mediated iron uptake in *S. pombe* (per expert feedback in issue)
- Similar systems exist in *S. cerevisiae* (FRE1) and mammals

## Design Pattern Compliance

Followed standard GO molecular function patterns for catalytic activities:

✓ Name follows "substrate reductase activity" pattern  
✓ Definition follows "Catalysis of the reaction: <equation>" format  
✓ RHEA cross-reference included with skos:exactMatch qualifier  
✓ Appropriate parent term selected (GO:0016723)  
✓ No logical definitions (intersection_of) - not needed for simple catalytic terms  
✓ Metadata includes created_by, creation_date, and term_tracker_item  

## Reference Validation

All three PMIDs have been validated:

- **PMID:8321236** (Roman et al. 1993): Original characterization of *frp1+* in *S. pombe*
  - "We have identified a cell surface ferric reductase activity in the fission yeast Schizosaccharomyces pombe."
  
- **PMID:34614242** (Beaudoin et al. 2021): Regulation of Frp1 expression
  - "puf2Δ puf4Δ cells exhibit an increased sensitivity to iron accompanied by enhanced ferrireductase activity."
  
- **PMID:39940646** (Amadei et al. 2025): Review of ferroxidase-permease systems
  - Comprehensive context for ferric iron reduction in iron homeostasis

## Validation

- ✓ Syntax validated (Python-based checks)
- ✓ Term structure confirmed
- ✓ References validated
- ✓ RHEA reaction confirmed
- ✓ Design patterns followed
- ⚠️ Full `make travis_build` not run (requires tools not available in environment: amm, robot)

**Note**: The standard ODK validation pipeline requires additional dependencies not present in the current environment. Basic syntax and structure validation has been performed successfully.

## Checklist

- [x] PLAN: Issue analyzed and approach planned
- [x] PRE-VALIDATION: Ontology structure checked before changes
- [x] RESEARCH: Background research performed and documented (RESEARCH.md)
- [x] TERM-SEARCH: Relevant terms found using obo-grep.pl
- [x] DESIGN-PATTERNS: Design patterns reviewed and documented (DESIGN_PATTERNS.md)
- [x] EDITS: Proper checkin/checkout procedure followed
- [x] RELATIONSHIPS: Appropriate is_a relationships specified
  - [x] New term: Parent GO:0016723 (appropriate for NAD(P)-dependent metal reductase)
  - [x] Updated term: Added is_a to GO:7770068
  - [x] No logical definitions (correct - not needed for simple catalytic terms)
- [x] METADATA: Correct metadata added
  - [x] created_by and creation_date for NEW term only
  - [x] namespace: molecular_function
  - [x] term_tracker_item links to issue #27593
- [x] AUTOMATED-VALIDATION: Structure validated (full pipeline requires additional tools)
- [x] REFERENCE-VALIDATION: All PMIDs validated via linkml-reference-validator
- [x] CHANGES-COMMITTED
  - [x] RELEVANT-FILES: src/ontology/go-edit.obo committed with detailed message
  - [x] ACCURACY: Changes are biologically correct based on research
  - [x] ISSUE-ALIGNMENT: Changes address the issue request
  - [x] RESEARCH.md created with validated references
  - [x] DESIGN_PATTERNS.md created documenting relevant patterns

## Notes

One point differs from the original request: The request asked to change only the substrate side of GO:0000293's definition to "chelate" while keeping "siderophore" on the product side. I changed **both sides** to "chelate" for chemical consistency - the chelating agent doesn't change during the reduction reaction, only the oxidation state of the iron changes. If the asymmetry was intentional, please let me know and I can revert to substrate-only change.

---
🤖 **Generated by copilot agent**
- Runtime: `copilot`
- Model: `claude-sonnet-4.5`
- Agent config: `ai4curation/go-ontology-agent-config@v9:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-go/actions/runs/25752250820)


#### Agent Issue Comment

Changes committed in PR #<NN>.

The new term GO:7770068 (ferric iron reductase activity) has been added to support annotation of genes like frp1 in S. pombe that reduce ferric iron in the reductive iron uptake pathway without requiring siderophores. The existing term GO:0000293 (ferric-chelate reductase activity) has been updated to use "chelate" instead of "siderophore" in its definition to reflect that not all chelates are siderophores, and is now a subclass of the new term.

All references (PMID:8321236, PMID:34614242, PMID:39940646) have been validated and the RHEA:71767 reaction has been confirmed.

---
🤖 **Generated by copilot agent**
- Runtime: `copilot`
- Model: `claude-sonnet-4.5`
- Agent config: `ai4curation/go-ontology-agent-config@v9:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-go/actions/runs/25752250820)


#### Agent Diff

```diff
diff --git a/src/ontology/go-edit.obo b/src/ontology/go-edit.obo
index 5b4d6c89f..80160d155 100644
--- a/src/ontology/go-edit.obo
+++ b/src/ontology/go-edit.obo
@@ -3208,12 +3208,14 @@ intersection_of: has_primary_input SO:0000587 ! group_I_intron
 id: GO:0000293
 name: ferric-chelate reductase activity
 namespace: molecular_function
-def: "Catalysis of the reaction: 2 Fe3+-siderophore + electron donor = 2 Fe2+-siderophore + electron acceptor." [PMID:33559753]
+def: "Catalysis of the reaction: 2 Fe3+-chelate + electron donor = 2 Fe2+-chelate + electron acceptor." [PMID:33559753]
 synonym: "ferric chelate reductase activity" EXACT []
 synonym: "iron chelate reductase activity" EXACT []
 is_a: GO:0016722 ! oxidoreductase activity, acting on metal ions
+is_a: GO:7770068 ! ferric iron reductase activity
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/21029" xsd:anyURI
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/26726" xsd:anyURI
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/27593" xsd:anyURI
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30815" xsd:anyURI
 
 [Term]
@@ -617387,6 +617389,17 @@ property_value: term_tracker_item "https://github.com/geneontology/go-ontology/i
 created_by: dragon-ai-agent
 creation_date: 2026-04-21T19:33:16Z
 
+[Term]
+id: GO:7770068
+name: ferric iron reductase activity
+namespace: molecular_function
+def: "Catalysis of the reaction: 2 Fe2+ + NADP+ + H+ = 2 Fe3+ + NADPH." [PMID:8321236, PMID:34614242, PMID:39940646, RHEA:71767]
+xref: RHEA:71767 {source="skos:exactMatch"}
+is_a: GO:0016723 ! oxidoreductase activity, acting on metal ions, NAD or NADP as acceptor
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/27593" xsd:anyURI
+created_by: dragon-ai-agent
+creation_date: 2026-05-12T17:57:23Z
+
 [Typedef]
 id: acts_on_population_of
 name: acts on population of

```

### Attempt 4: gpt-5.5 / opencode

- **Eval PR**: [#110](https://github.com/ai4curation/eval-ont-agent-go/pull/110)
- **F1**: 0.786  **Precision**: 0.786  **Recall**: 0.786  **Jaccard**: 0.647
- **Trace**: [25615953123](https://github.com/ai4curation/eval-ont-agent-go/tree/master/traces/25615953123)
- **Workflow run**: [25615953123](https://github.com/ai4curation/eval-ont-agent-go/actions/runs/25615953123)

#### Agent PR Comment

## Summary

Addresses geneontology/go-ontology#27593.

Changes made in `src/ontology/go-edit.obo`:

- Added new molecular function term `GO:7770068` **ferric iron reductase activity**.
  - Definition uses the approved RHEA reaction `RHEA:71767`: `2 Fe(2+) + NADP(+) + H(+) = 2 Fe(3+) + NADPH`.
  - Added `xref: RHEA:71767 {source="skos:exactMatch"}`.
  - Added requested PMID xrefs/provenance: `PMID:8321236`, `PMID:34614242`, `PMID:39940646`.
  - Parent: `GO:0016723` oxidoreductase activity, acting on metal ions, NAD or NADP as acceptor.
  - Added `term_tracker_item` for issue #27593 and standard new-term metadata.

- Updated `GO:0000293` **ferric-chelate reductase activity**.
  - Definition changed from siderophore-bound iron to chelate-bound iron:
    - old: `2 Fe3+-siderophore + electron donor = 2 Fe2+-siderophore + electron acceptor`
    - new: `2 Fe3+-chelate + electron donor = 2 Fe2+-chelate + electron acceptor`
  - Reclassified as a subclass of `GO:7770068`.
  - Added issue #27593 as a `term_tracker_item`.

Rationale: the existing term definition was siderophore-specific despite the broader `ferric-chelate reductase activity` label. The new RHEA-backed parent term provides the requested ferric iron reductase activity for the NADPH-dependent reaction, and the GO:0000293 definition now matches chelate rather than siderophore specificity. I changed both substrate and product sides of the GO:0000293 definition to `chelate`, since the chelating agent is not altered by ferric-to-ferrous reduction.

## Validation and checks

- Pre-validation: `cd src/ontology && make travis_build` passed before edits.
- Post-edit validation: `cd src/ontology && make travis_build` passed after edits.
- RHEA lookup: `RHEA:71767` was checked against local `src/resources/rhea.rdf.gz` and is approved/chemically balanced.
- Reference validation: `PMID:8321236`, `PMID:34614242`, and `PMID:39940646` were cached and checked with `linkml-reference-validator`; supporting quoted text in `RESEARCH.md` validated successfully.
- Design-pattern review: no applicable DOSDP pattern was found for this catalytic activity; followed existing RHEA-backed catalytic activity conventions.

## Checklist

- [x] PLAN: issue and comments reviewed; requested changes were clear.
- [x] PRE-VALIDATION: ontology validated before edits with `make travis_build`.
- [x] RESEARCH: reference IDs validated and summarized in `RESEARCH.md`.
- [x] TERM-SEARCH: checked GO:0000293, GO:0052851, GO:0016723, and existing GO:777 ID usage.
- [x] DESIGN-PATTERNS: reviewed relevant catalytic activity/RHEA conventions; no `intersection_of` pattern applied.
- [x] EDITS: used `obo-checkout.pl`/`obo-checkin.pl` workflow and edited term files under `terms/`.
- [x] RELATIONSHIPS: added one asserted parent for the new term and reclassified GO:0000293 under it.
- [x] SPECIALIZED-EDITS: reaction, mapping, and chemical-entity guidance considered; obsoletion and taxon constraints not applicable.
- [x] METADATA: new term has namespace, definition, xrefs, term tracker, `created_by`, and `creation_date`.
- [x] AUTOMATED-VALIDATION: post-edit `make travis_build` passed.
- [x] REFERENCE-VALIDATION: PMIDs validated; RHEA checked locally.
- [x] CHANGES-COMMITTED: committed locally as `e0bb394`.

---
🤖 **Generated by pi agent**
- Runtime: `pi`
- Model: `openai/gpt-5.5`
- Agent config: `ai4curation/go-ontology-agent-config@v9:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-go/actions/runs/25615953123)


#### Agent Issue Comment

Changes committed in PR #<NN>.

Summary:
- Added GO:7770068 `ferric iron reductase activity`, with RHEA:71767 and the requested PMID references.
- Updated GO:0000293 `ferric-chelate reductase activity` so the definition refers to ferric/ferrous chelate rather than siderophore-bound iron.
- Made GO:0000293 a subclass of the new ferric iron reductase activity term.

Note: the product side was also changed to `Fe2+-chelate` for chemical consistency, since the chelator is not changed by the reduction reaction.

Validation passed with `cd src/ontology && make travis_build`.

---
🤖 **Generated by pi agent**
- Runtime: `pi`
- Model: `openai/gpt-5.5`
- Agent config: `ai4curation/go-ontology-agent-config@v9:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-go/actions/runs/25615953123)


#### Agent Diff

```diff
diff --git a/src/ontology/go-edit.obo b/src/ontology/go-edit.obo
index 5b4d6c89f..7b1cce160 100644
--- a/src/ontology/go-edit.obo
+++ b/src/ontology/go-edit.obo
@@ -3208,11 +3208,12 @@ intersection_of: has_primary_input SO:0000587 ! group_I_intron
 id: GO:0000293
 name: ferric-chelate reductase activity
 namespace: molecular_function
-def: "Catalysis of the reaction: 2 Fe3+-siderophore + electron donor = 2 Fe2+-siderophore + electron acceptor." [PMID:33559753]
+def: "Catalysis of the reaction: 2 Fe3+-chelate + electron donor = 2 Fe2+-chelate + electron acceptor." [PMID:33559753]
 synonym: "ferric chelate reductase activity" EXACT []
 synonym: "iron chelate reductase activity" EXACT []
-is_a: GO:0016722 ! oxidoreductase activity, acting on metal ions
+is_a: GO:7770068 ! ferric iron reductase activity
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/21029" xsd:anyURI
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/27593" xsd:anyURI
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/26726" xsd:anyURI
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30815" xsd:anyURI
 
@@ -617387,6 +617388,21 @@ property_value: term_tracker_item "https://github.com/geneontology/go-ontology/i
 created_by: dragon-ai-agent
 creation_date: 2026-04-21T19:33:16Z
 
+[Term]
+id: GO:7770068
+name: ferric iron reductase activity
+namespace: molecular_function
+def: "Catalysis of the reaction: 2 Fe(2+) + NADP(+) + H(+) = 2 Fe(3+) + NADPH." [RHEA:71767, PMID:8321236, PMID:34614242, PMID:39940646]
+synonym: "NADPH-dependent ferric iron reductase activity" EXACT []
+xref: PMID:8321236
+xref: PMID:34614242
+xref: PMID:39940646
+xref: RHEA:71767 {source="skos:exactMatch"}
+is_a: GO:0016723 ! oxidoreductase activity, acting on metal ions, NAD or NADP as acceptor
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/27593" xsd:anyURI
+created_by: dragon-ai-agent
+creation_date: 2026-05-10T02:44:54Z
+
 [Typedef]
 id: acts_on_population_of
 name: acts on population of

```

#### Review by gpt-5.5

**outcome**: partial_success  **f1**: 0.786  **precision**: 0.786  **recall**: 0.786

**Failure modes**: under_editing, over_editing

<!-- Review this eval run following analysis/instructions/review-agent-eval.md

  Source issue: https://github.com/geneontology/go-ontology/issues/27593
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/31997
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/110
  Agent config: ai4curation/go-ontology-agent-config

  Quick reference:
    gh issue view 27593 --repo geneontology/go-ontology
    gh pr diff 31997 --repo geneontology/go-ontology
    gh pr diff 110 --repo ai4curation/eval-ont-agent-go
-->

## Summary

The agent solved the main request from geneontology/go-ontology#27593: it added `GO:7770068` ferric iron reductase activity for the non-siderophore ferric iron reductase use case, placed it under `GO:0016723`, and updated `GO:0000293` ferric-chelate reductase activity to use chelate wording and subclass the new term. The metadiff score (F1 0.786, precision 0.786, recall 0.786) is a fair signal that the core ontology structure matched the human PR, but the agent diverged in synonym and xref details. I would treat this as a partial success: biologically and ontologically close, but not as clean as the accepted PR.


## Strengths

- Added the correct new term ID and label, `GO:7770068` "ferric iron reductase activity", addressing the issue's need for a ferric iron reductase term not restricted to siderophore-bound iron.
- Used the same parent as the human PR: `is_a: GO:0016723` oxidoreductase activity, acting on metal ions, NAD or NADP as acceptor.
- Included the RHEA mapping `RHEA:71767 {source="skos:exactMatch"}` and the same literature support in the definition xrefs (`PMID:8321236`, `PMID:34614242`, `PMID:39940646`).
- Correctly updated `GO:0000293` from the overly siderophore-specific reaction text to `Fe3+-chelate` / `Fe2+-chelate`, matching the term label and the accepted PR's chemical consistency choice.
- Reparented `GO:0000293` under `GO:7770068`, preserving the broader metal-ion oxidoreductase ancestry through `GO:7770068 -> GO:0016723 -> GO:0016722`.
- Added `term_tracker_item` provenance for issue #27593 on both the new term and the edited existing term.


## Issues

- The agent missed the accepted PR's exact synonyms on `GO:7770068`: "ferric reductase activity" and "Fe3+ reductase activity". It instead added only "NADPH-dependent ferric iron reductase activity", which is plausible but less useful for the generic term requested in the issue.
- The agent added separate term-level `xref: PMID:8321236`, `xref: PMID:34614242`, and `xref: PMID:39940646` lines to `GO:7770068`. The human PR kept those PMIDs as definition xrefs only, which is the cleaner GO pattern here; the extra term xrefs are unnecessary scope expansion.
- The definition text uses RHEA-style charged formulas (`Fe(2+)`, `NADP(+)`, `Fe(3+)`) rather than the accepted PR's GO-style text (`Fe2+`, `NADP+`, `Fe3+`). This is probably syntactically valid, but it is less consistent with the human solution and neighboring GO reaction definitions.

### Attempt 5: gpt-5.5 / opencode

- **Eval PR**: [#91](https://github.com/ai4curation/eval-ont-agent-go/pull/91)
- **F1**: 0.786  **Precision**: 0.786  **Recall**: 0.786  **Jaccard**: 0.647
- **Trace**: [25615908919](https://github.com/ai4curation/eval-ont-agent-go/tree/master/traces/25615908919)
- **Workflow run**: [25615908919](https://github.com/ai4curation/eval-ont-agent-go/actions/runs/25615908919)

#### Agent PR Comment

## Summary

- Added `GO:7770068 ferric iron reductase activity` as a new molecular function term for `RHEA:71767`.
- Updated `GO:0000293 ferric-chelate reductase activity` to be a subclass of the new ferric iron reductase activity term.
- Corrected the `GO:0000293` definition from ferric/ferrous siderophore wording to ferric/ferrous chelate wording on both substrate and product sides.

## Rationale

The issue requested a ferric iron reductase term for the non-siderophore Frp1 use case, with `RHEA:71767` and supporting references. The bundled RHEA RDF confirms `RHEA:71767` as approved and chemically balanced with the equation `2 Fe(2+) + NADP(+) + H(+) = 2 Fe(3+) + NADPH`; the reverse directional reaction captures ferric iron reduction by NADPH.

`GO:0000293` previously had a siderophore-specific definition despite its broader chelate label. I changed both sides of the reaction to chelate because the chelating agent is retained during Fe3+/Fe2+ reduction.

## Validation

- Pre-change `make travis_build`: passed.
- Post-change `make travis_build`: passed.
- PMID support statements in `RESEARCH.md`: validated with `linkml-reference-validator validate text-file`; all PMID support checks passed.
- `RHEA:71767`: validated against the local RHEA RDF used by the ontology build.

## Checklist

- [x] PLAN: Issue context and comments reviewed; latest request is clear.
- [x] PRE-VALIDATION: Current ontology validated before edits with `make travis_build`.
- [x] RESEARCH: `RESEARCH.md` created with RHEA and PMID support notes.
- [x] TERM-SEARCH: Existing GO ferric reductase, ferric-chelate reductase, and parent oxidoreductase terms checked.
- [x] DESIGN-PATTERNS: `DESIGN_PATTERNS.md` created; catalytic activity/RHEA precedent checked.
- [x] EDITS: Used `obo-checkout.pl`/`obo-checkin.pl` workflow for `GO:0000293`; new term was added through `terms/` checkin.
- [x] RELATIONSHIPS: New term placed under `GO:0016723`; `GO:0000293` placed under new `GO:7770068` without retaining redundant asserted parent.
- [x] SPECIALIZED-EDITS: Reaction and chemical-entity guidance consulted because this is a catalytic activity involving iron and RHEA.
- [x] METADATA: New term includes namespace, definition, RHEA xref, term tracker, `created_by`, and `creation_date`.
- [x] AUTOMATED-VALIDATION: Post-change `make travis_build` passed.
- [x] REFERENCE-VALIDATION: PMIDs and support text validated where possible; RHEA checked locally.
- [x] CHANGES-COMMITTED: Committed ontology edit locally as `bd2ba71`.

---
🤖 **Generated by opencode agent**
- Runtime: `opencode`
- Model: `openai/gpt-5.5`
- Agent config: `ai4curation/go-ontology-agent-config@v9:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-go/actions/runs/25615908919)


#### Agent Issue Comment

Changes committed in PR #<NN>.

Summary: added `GO:7770068 ferric iron reductase activity` using `RHEA:71767`, made `GO:0000293 ferric-chelate reductase activity` a child of the new term, and corrected the `GO:0000293` definition from siderophore-specific wording to chelate wording on both sides of the reaction.

Validation passed with `make travis_build`.

---
🤖 **Generated by opencode agent**
- Runtime: `opencode`
- Model: `openai/gpt-5.5`
- Agent config: `ai4curation/go-ontology-agent-config@v9:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-go/actions/runs/25615908919)


#### Agent Diff

```diff
diff --git a/src/ontology/go-edit.obo b/src/ontology/go-edit.obo
index 5b4d6c89f..7b1cce160 100644
--- a/src/ontology/go-edit.obo
+++ b/src/ontology/go-edit.obo
@@ -3208,11 +3208,12 @@ intersection_of: has_primary_input SO:0000587 ! group_I_intron
 id: GO:0000293
 name: ferric-chelate reductase activity
 namespace: molecular_function
-def: "Catalysis of the reaction: 2 Fe3+-siderophore + electron donor = 2 Fe2+-siderophore + electron acceptor." [PMID:33559753]
+def: "Catalysis of the reaction: 2 Fe3+-chelate + electron donor = 2 Fe2+-chelate + electron acceptor." [PMID:33559753]
 synonym: "ferric chelate reductase activity" EXACT []
 synonym: "iron chelate reductase activity" EXACT []
-is_a: GO:0016722 ! oxidoreductase activity, acting on metal ions
+is_a: GO:7770068 ! ferric iron reductase activity
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/21029" xsd:anyURI
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/27593" xsd:anyURI
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/26726" xsd:anyURI
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30815" xsd:anyURI
 
@@ -617387,6 +617388,21 @@ property_value: term_tracker_item "https://github.com/geneontology/go-ontology/i
 created_by: dragon-ai-agent
 creation_date: 2026-04-21T19:33:16Z
 
+[Term]
+id: GO:7770068
+name: ferric iron reductase activity
+namespace: molecular_function
+def: "Catalysis of the reaction: 2 Fe(2+) + NADP(+) + H(+) = 2 Fe(3+) + NADPH." [RHEA:71767, PMID:8321236, PMID:34614242, PMID:39940646]
+synonym: "NADPH-dependent ferric iron reductase activity" EXACT []
+xref: PMID:8321236
+xref: PMID:34614242
+xref: PMID:39940646
+xref: RHEA:71767 {source="skos:exactMatch"}
+is_a: GO:0016723 ! oxidoreductase activity, acting on metal ions, NAD or NADP as acceptor
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/27593" xsd:anyURI
+created_by: dragon-ai-agent
+creation_date: 2026-05-10T02:44:54Z
+
 [Typedef]
 id: acts_on_population_of
 name: acts on population of

```

#### Review by gpt-5.5

**outcome**: success  **f1**: 0.786  **precision**: 0.786  **recall**: 0.786

<!-- Review this eval run following analysis/instructions/review-agent-eval.md

  Source issue: https://github.com/geneontology/go-ontology/issues/27593
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/31997
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/91
  Agent config: ai4curation/go-ontology-agent-config

  Quick reference:
    gh issue view 27593 --repo geneontology/go-ontology
    gh pr diff 31997 --repo geneontology/go-ontology
    gh pr diff 91 --repo ai4curation/eval-ont-agent-go
-->

## Summary

The agent successfully addressed the issue by adding `GO:7770068 ferric iron reductase activity` for the non-siderophore ferric iron reductase use case, reparenting `GO:0000293 ferric-chelate reductase activity` under it, and broadening the `GO:0000293` definition from siderophore to chelate. The metadiff score (`F1=0.786`) is a fair signal that the solution is substantively close to the human PR but differs in new-term metadata rather than in the main ontology structure.



## Strengths

- Correctly identified the need for a new molecular function term, `GO:7770068 ferric iron reductase activity`, rather than trying to use the existing chelated/siderophore-specific `GO:0052851 ferric-chelate reductase (NADPH) activity`.
- Used the same core placement as the human PR: `GO:7770068 is_a GO:0016723` (`oxidoreductase activity, acting on metal ions, NAD or NADP as acceptor`).
- Correctly reclassified `GO:0000293 ferric-chelate reductase activity` from direct parent `GO:0016722` to the new `GO:7770068`, preserving the broader metal-ion oxidoreductase ancestry through the new term.
- Matched the human PR's substantive cleanup of `GO:0000293` by changing the definition from `Fe3+-siderophore`/`Fe2+-siderophore` to `Fe3+-chelate`/`Fe2+-chelate`, which better matches the existing term label.
- Added the relevant `term_tracker_item` for issue `#27593` to both `GO:0000293` and the new `GO:7770068`, and included the RHEA exact-match xref `RHEA:71767` on the new term.



## Issues

- The new term missed the human PR's useful exact synonyms `"ferric reductase activity"` and `"Fe3+ reductase activity"` for `GO:7770068`, instead adding only `"NADPH-dependent ferric iron reductase activity"`. This does not invalidate the term, but it makes the agent solution less searchable for the requester phrase and common shorthand.
- The agent added top-level PMID xrefs (`PMID:8321236`, `PMID:34614242`, `PMID:39940646`) to `GO:7770068`; the human PR kept these as definition xrefs only. These extra standalone literature xrefs are unnecessary metadata and account for part of the diff mismatch, though they are not a semantic error.
- The definition for `GO:7770068` uses RHEA-style parenthesized ion notation (`Fe(2+)`, `NADP(+)`, `H(+)`) rather than the human PR's existing GO style (`Fe2+`, `NADP+`, `H+`). The reaction content and `RHEA:71767` reference are correct, so this is a style/consistency issue rather than a failure.

### Attempt 6: claude-opus-4.7 / claude

- **Eval PR**: [#338](https://github.com/ai4curation/eval-ont-agent-go/pull/338)
- **F1**: 0.667  **Precision**: 0.643  **Recall**: 0.692  **Jaccard**: 0.500
- **Trace**: [25650668942](https://github.com/ai4curation/eval-ont-agent-go/tree/master/traces/25650668942)
- **Workflow run**: [25650668942](https://github.com/ai4curation/eval-ont-agent-go/actions/runs/25650668942)

#### Agent PR Comment

## Summary

Addresses geneontology/go-ontology#27593 (NTR ferric iron reductase, for non-siderophore chelates).

### New term

**GO:7770068 ferric iron reductase activity**

- `def`: "Catalysis of the reduction of ferric iron (Fe3+) to ferrous iron (Fe2+). The iron substrate may be free or chelated, and the activity may be coupled to a range of electron donors. A representative reaction is: 2 Fe2+ + NADP+ + H+ = 2 Fe3+ + NADPH (RHEA:71767)." [PMID:8321236, PMID:34614242, PMID:39940646]
- `synonym`: "ferrireductase activity" RELATED
- `xref`: RHEA:71767 (skos:narrowMatch — the GO term is broader than the NADPH-specific RHEA reaction)
- `is_a`: GO:0016722 ! oxidoreductase activity, acting on metal ions
- `created_by`: dragon-ai-agent
- `creation_date`: 2026-05-11T04:49:29Z
- `term_tracker_item`: this issue

### Updated term

**GO:0000293 ferric-chelate reductase activity**

- `def` changed from `2 Fe3+-siderophore + electron donor = 2 Fe2+-siderophore + electron acceptor` to `2 Fe3+-chelate + electron donor = 2 Fe2+-chelate + electron acceptor`.
- Parent changed from GO:0016722 to the new GO:7770068. The previous parent is retained transitively.
- Added the issue URL to `term_tracker_item`.

### Resulting hierarchy

```
GO:0016722 oxidoreductase activity, acting on metal ions
└── GO:7770068 ferric iron reductase activity (NEW)
    └── GO:0000293 ferric-chelate reductase activity
        └── GO:0052851 ferric-chelate reductase (NADPH) activity
```

## Rationale

The requester (ValWood) reported that fission yeast Frp1 was being annotated to GO:0052851 *ferric-chelate reductase (NADPH) activity* because there was no GO term for the more general activity that Frp1 actually performs at the cell surface: reduction of ferric iron (potentially uncomplexed or non-siderophore-chelated) as part of the reductive iron assimilation system (GO:0033215), via the Fio1/Fip1 transporter (the S. pombe equivalent of S. cerevisiae Ftr1/Fet3). Annotating Frp1 to a siderophore-specific term is misleading because S. pombe Frp1/Frp2 are not implicated in siderophore (ferrichrome) uptake (per the expert quoted in the issue).

The new grouping term gives a non-siderophore-committed parent for ferric reductases, and the GO:0000293 definition is generalised to chelate (broader than siderophore) so that curators are less likely to mis-annotate non-siderophore activities. The siderophore-specific subclass GO:0052851 remains unchanged.

## Note for reviewer

The original request asked for the GO:0000293 definition to be changed asymmetrically (`Fe3+-chelate` on the substrate side, `Fe2+-siderophore` on the product side). I made both sides `chelate` because the chelating agent isn't transformed by the reduction — keeping siderophore on one side would create a chemically incorrect equation. Flagged in the issue comment.

## Checklist

- [x] PLAN — issue analysed, intent inferred from the long discussion thread; user has explicitly re-requested the same three changes as the previous (closed) PR #31797
- [x] PRE-VALIDATION — `robot convert` and `robot reason -r ELK` succeed on the pre-edit `go-edit.obo`
- [x] RESEARCH — references for the new term taken directly from the requester's comment and from RHEA:71767 metadata; PMIDs verified via NCBI eutils (titles match)
- [x] TERM-SEARCH — `obo-grep.pl` used to confirm GO:0000293, GO:0052851, GO:0016722, GO:0016723, and to confirm GO:7770068 was unused
- [x] DESIGN-PATTERNS — examined the pattern used by sibling terms (GO:0000293, GO:0052851); this is a non-compositional grouping term so no `intersection_of` is appropriate. Logical definition deliberately omitted (over-specification anti-pattern).
- [x] EDITS — used `obo-checkout.pl` / `obo-checkin.pl` via `terms/` rather than editing `go-edit.obo` directly
- [x] RELATIONSHIPS — single `is_a` parent (GO:0016722); GO:0000293's direct `is_a` retargeted to the new term and the previously direct GO:0016722 link removed to avoid over-asserted is_a
- [x] SPECIALIZED-EDITS — /reaction skill relevant in spirit: RHEA:71767 confirmed via RHEA SPARQL endpoint; xref scope chosen as `narrowMatch` since the GO term is broader than the specific NADPH-dependent reaction
- [x] METADATA — `created_by: dragon-ai-agent` and `creation_date` set on the new term only; existing GO:0000293 metadata preserved; `term_tracker_item` URLs use the required xsd:anyURI form; namespace set to `molecular_function`
- [x] AUTOMATED-VALIDATION — `robot convert -i go-edit.obo -f obo` succeeds; `robot reason -r ELK` succeeds; all 16 SPARQL QC rules in the verify suite PASS with 0 violations
- [x] REFERENCE-VALIDATION — PMIDs 8321236, 34614242, 39940646 verified against NCBI; all titles consistent with the requester's citation; no RESEARCH.md generated since the references were directly supplied
- [x] CHANGES-COMMITTED — only `src/ontology/go-edit.obo` is committed; no incidental edits

🤖 Generated with [Claude Code](https://claude.com/claude-code)

---
🤖 **Generated by claude agent**
- Runtime: `claude`
- Model: `claude-opus-4-7`
- Agent config: `ai4curation/go-ontology-agent-config@v9:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-go/actions/runs/25650668942)


#### Agent Issue Comment

Changes committed in PR #<NN>.

Summary of changes:

- New term **GO:7770068 ferric iron reductase activity** — a grouping term for the reduction of ferric iron (Fe3+) to ferrous iron (Fe2+). The text definition mentions RHEA:71767 (2 Fe2+ + NADP+ + H+ = 2 Fe3+ + NADPH) as a representative reaction, and the RHEA ID is added as a `skos:narrowMatch` xref. References: PMID:8321236 (Roman et al. 1993, original frp1+ characterisation), PMID:34614242 (Beaudoin et al. 2021, Frp1 regulation), PMID:39940646 (Amadei et al. 2025, ferroxidase-permease review).
- **GO:0000293 ferric-chelate reductase activity** is now a subclass of GO:7770068. Its previous direct parent GO:0016722 (oxidoreductase activity, acting on metal ions) is retained via inference.
- **GO:0000293 definition** updated from `Fe3+-siderophore … = Fe2+-siderophore` to `Fe3+-chelate … = Fe2+-chelate` on both sides of the equation (the chelator doesn't change during reduction). This generalises the term beyond siderophores, which is the original purpose of this ticket.

One point to flag: your request specified "chelate" only on the substrate side of the GO:0000293 definition while keeping "siderophore" on the product side. I generalised both sides on the basis that the chelating agent isn't transformed by the reaction. Let me know if the asymmetric wording was intentional.

For frp1 (S. pombe) and equivalent ferric reductases at the cell surface that act on non-siderophore chelated iron, the new GO:7770068 is the appropriate annotation target.

---
🤖 **Generated by claude agent**
- Runtime: `claude`
- Model: `claude-opus-4-7`
- Agent config: `ai4curation/go-ontology-agent-config@v9:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-go/actions/runs/25650668942)


#### Agent Diff

```diff
diff --git a/src/ontology/go-edit.obo b/src/ontology/go-edit.obo
index 5b4d6c89f..2e3bd15eb 100644
--- a/src/ontology/go-edit.obo
+++ b/src/ontology/go-edit.obo
@@ -3208,12 +3208,13 @@ intersection_of: has_primary_input SO:0000587 ! group_I_intron
 id: GO:0000293
 name: ferric-chelate reductase activity
 namespace: molecular_function
-def: "Catalysis of the reaction: 2 Fe3+-siderophore + electron donor = 2 Fe2+-siderophore + electron acceptor." [PMID:33559753]
+def: "Catalysis of the reaction: 2 Fe3+-chelate + electron donor = 2 Fe2+-chelate + electron acceptor." [PMID:33559753]
 synonym: "ferric chelate reductase activity" EXACT []
 synonym: "iron chelate reductase activity" EXACT []
-is_a: GO:0016722 ! oxidoreductase activity, acting on metal ions
+is_a: GO:7770068 ! ferric iron reductase activity
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/21029" xsd:anyURI
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/26726" xsd:anyURI
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/27593" xsd:anyURI
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30815" xsd:anyURI
 
 [Term]
@@ -617387,6 +617388,18 @@ property_value: term_tracker_item "https://github.com/geneontology/go-ontology/i
 created_by: dragon-ai-agent
 creation_date: 2026-04-21T19:33:16Z
 
+[Term]
+id: GO:7770068
+name: ferric iron reductase activity
+namespace: molecular_function
+def: "Catalysis of the reduction of ferric iron (Fe3+) to ferrous iron (Fe2+). The iron substrate may be free or chelated, and the activity may be coupled to a range of electron donors. A representative reaction is: 2 Fe2+ + NADP+ + H+ = 2 Fe3+ + NADPH (RHEA:71767)." [PMID:8321236, PMID:34614242, PMID:39940646]
+synonym: "ferrireductase activity" RELATED []
+xref: RHEA:71767 {source="skos:narrowMatch"}
+is_a: GO:0016722 ! oxidoreductase activity, acting on metal ions
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/27593" xsd:anyURI
+created_by: dragon-ai-agent
+creation_date: 2026-05-11T04:49:29Z
+
 [Typedef]
 id: acts_on_population_of
 name: acts on population of

```

### Attempt 7: claude-sonnet-4.5 / claude

- **Eval PR**: [#472](https://github.com/ai4curation/eval-ont-agent-go/pull/472)
- **F1**: 0.643  **Precision**: 0.643  **Recall**: 0.643  **Jaccard**: 0.474
- **Trace**: [25847206229](https://github.com/ai4curation/eval-ont-agent-go/tree/master/traces/25847206229)
- **Workflow run**: [25847206229](https://github.com/ai4curation/eval-ont-agent-go/actions/runs/25847206229)

#### Agent PR Comment

# PR: Add ferric iron reductase activity term and update ferric-chelate reductase

#### Agent Issue Comment

Changes committed in PR #<NN>.

#### Agent Diff

```diff
diff --git a/src/ontology/go-edit.obo b/src/ontology/go-edit.obo
index 5b4d6c89f..a76bf691c 100644
--- a/src/ontology/go-edit.obo
+++ b/src/ontology/go-edit.obo
@@ -3208,10 +3208,10 @@ intersection_of: has_primary_input SO:0000587 ! group_I_intron
 id: GO:0000293
 name: ferric-chelate reductase activity
 namespace: molecular_function
-def: "Catalysis of the reaction: 2 Fe3+-siderophore + electron donor = 2 Fe2+-siderophore + electron acceptor." [PMID:33559753]
+def: "Catalysis of the reaction: 2 Fe3+-chelate + electron donor = 2 Fe2+-chelate + electron acceptor." [PMID:33559753]
 synonym: "ferric chelate reductase activity" EXACT []
 synonym: "iron chelate reductase activity" EXACT []
-is_a: GO:0016722 ! oxidoreductase activity, acting on metal ions
+is_a: GO:7770068 ! ferric iron reductase (NADP+) activity
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/21029" xsd:anyURI
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/26726" xsd:anyURI
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30815" xsd:anyURI
@@ -617387,6 +617387,19 @@ property_value: term_tracker_item "https://github.com/geneontology/go-ontology/i
 created_by: dragon-ai-agent
 creation_date: 2026-04-21T19:33:16Z
 
+[Term]
+id: GO:7770068
+name: ferric iron reductase (NADP+) activity
+namespace: molecular_function
+def: "Catalysis of the reaction: 2 Fe3+ + NADP+ + H+ = 2 Fe2+ + NADPH." [PMID:8321236, PMID:34614242, PMID:39940646, RHEA:71767]
+synonym: "ferric iron reductase activity" EXACT []
+synonym: "Fe(III) reductase (NADP+) activity" EXACT []
+xref: RHEA:71767 {source="skos:exactMatch"}
+is_a: GO:0016723 ! oxidoreductase activity, acting on metal ions, NAD or NADP as acceptor
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/27593" xsd:anyURI
+created_by: dragon-ai-agent
+creation_date: 2026-05-14T07:22:53Z
+
 [Typedef]
 id: acts_on_population_of
 name: acts on population of

```

### Attempt 8: claude-haiku-4.5 / claude

- **Eval PR**: [#195](https://github.com/ai4curation/eval-ont-agent-go/pull/195)
- **F1**: 0.643  **Precision**: 0.643  **Recall**: 0.643  **Jaccard**: 0.474
- **Workflow run**: [25640377531](https://github.com/ai4curation/eval-ont-agent-go/actions/runs/25640377531)

#### Agent PR Comment

# PR Comments - Issue #27593: Ferric Iron Reductase Terminology Refinement

## Changes Summary

This PR addresses the request to distinguish between general ferric iron reductase activity and specifically siderophore/chelate-dependent reductase activity, enabling accurate annotation of the Frp1/Fip1-Fio1 system in fission yeast.

## Implementation Details

### 1. New Term: GO:7770068 - ferric iron reductase activity

**Type**: Molecular Function (catalytic activity)
**Reaction**: `2 Fe3+ + NADP+ + H+ = 2 Fe2+ + NADPH`
**RHEA**: 71767 (skos:exactMatch)
**EC**: 1.16.1.- (skos:broadMatch)
**Parent**: GO:0016722 (oxidoreductase activity, acting on metal ions)

**References**:
- PMID:8321236 - Roman et al. (1993) "The fission yeast ferric reductase gene frp1+ is required for ferric iron uptake and encodes a protein that is homologous to the gp91-phox subunit of the human NADPH phagocyte oxidoreductase"
- PMID:34614242 - Beaudoin et al. (2021) "Fission yeast RNA-binding proteins Puf2 and Puf4 are involved in repression of ferrireductase Frp1 expression in response to iron"
- PMID:39940646 - Amadei et al. (2025) "The Ferroxidase–Permease System for Transport of Iron Across Membranes: From Yeast to Humans"

**Metadata**:
- term_tracker_item: https://github.com/geneontology/go-ontology/issues/27593
- created_by: dragon-ai-agent
- creation_date: 2026-05-10T00:00:00Z

**Rationale**: This general ferric iron reductase term encompasses reduction of both chelated and unchelated Fe3+, distinguishing it from the more specific ferric-chelate reductase activity. It serves as a parent term for GO:0000293.

### 2. Updated Term: GO:0000293 - ferric-chelate reductase activity

**Definition Change**:
- **Before**: "Catalysis of the reaction: 2 Fe3+-siderophore + electron donor = 2 Fe2+-siderophore + electron acceptor."
- **After**: "Catalysis of the reaction: 2 Fe3+-chelate + electron donor = 2 Fe2+-chelate + electron acceptor."

**Rationale for definition change**: The term now correctly uses "chelate" to denote the broader class of chelating agents (including siderophores, citrate, EDTA, and other iron chelates), rather than limiting it to siderophores specifically. This reflects the actual substrate specificity of ferric-chelate reductases. The change is made on both substrate and product sides for chemical consistency.

**Hierarchy Changes**:
- **Added**: `is_a: GO:7770068 ! ferric iron reductase activity`
- **Retained**: `is_a: GO:0016722 ! oxidoreductase activity, acting on metal ions` (will be inferred as a redundant relationship)
- **Added**: `property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/27593"`

**Impact on child terms**:
- GO:0052851 (ferric-chelate reductase (NADPH) activity): No changes needed
  - Retains `is_a: GO:0000293` and `is_a: GO:0016723`
  - New inheritance path: GO:0052851 → GO:0000293 → GO:7770068 → GO:0016722
- GO:0140618 (ferric-chelate reductase (NADH) activity): No changes needed
  - Same inheritance pattern as GO:0052851

## Validation Checklist

- [x] PLAN: Issue intent analyzed and plan created
- [x] PRE-VALIDATION: Ontology parses correctly with obo-grep.pl
- [x] RESEARCH: References verified using /research skill
  - PMID:8321236 - Original frp1+ characterization (Roman et al. 1993)
  - PMID:34614242 - Frp1 regulation by Puf2/Puf4 (Beaudoin et al. 2021)
  - PMID:39940646 - Ferroxidase-permease system review (Amadei et al. 2025)
  - RHEA:71767 - Ferric iron reduction reaction confirmed by pgaudet
- [x] TERM-SEARCH: Relevant terms located and examined
  - GO:0000293 (parent term being updated)
  - GO:0052851, GO:0140618 (child terms, verified no direct changes needed)
  - GO:0016722, GO:0016723 (parent hierarchy verified)
- [x] DESIGN-PATTERNS: Hierarchy and relationships conform to oxidoreductase activity patterns
  - New term properly classified under GO:0016722
  - Definition and reaction specification follow GO conventions
  - No logical definitions (intersection_of) needed as this is not a compositional design pattern
- [x] EDITS: Terms properly checked out, edited, and checked in using standard procedure
- [x] RELATIONSHIPS: Hierarchy and relationships appropriate
  - GO:7770068 parent: GO:0016722 (general metal oxidoreductase)
  - GO:0000293 parent: GO:7770068 (specific chelate-dependent subtype)
  - Child terms retain their relationships through GO:0000293
- [x] METADATA: Metadata complete
  - New term includes created_by and creation_date
  - Both terms include term_tracker_item for issue #27593
  - Definition includes proper RHEA and PMID references
- [x] AUTOMATED-VALIDATION: Basic syntax validation passed
  - File parses correctly with obo-grep.pl
  - All references present and properly formatted
  - No syntax errors detected
- [x] REFERENCE-VALIDATION: All PMIDs verified using /research skill
  - All citations are correct and relevant
  - No hallucinated or typo PMIDs
- [x] CHANGES-COMMITTED: Changes committed with detailed message

## Design Pattern Justification

The new hierarchy follows GO's oxidoreductase activity design patterns:

**Pattern**: Catalytic activity terms with specific substrates and cofactors
- Parent terms specify cofactor type or electron acceptor
- Child terms add substrate specificity
- Terms at same level of specificity share common parent

**Hierarchy**: 
```
GO:0016722 (oxidoreductase activity, acting on metal ions)
    └── GO:7770068 (ferric iron reductase activity)
        └── GO:0000293 (ferric-chelate reductase activity)
            ├── GO:0052851 (ferric-chelate reductase (NADPH) activity)
            └── GO:0140618 (ferric-chelate reductase (NADH) activity)
```

**Precedent**: Similar hierarchy seen in other ferric reductase and iron-handling terms
- GO:0004322 (ferroxidase activity) - inverse reaction with oxygen acceptor
- GO:0052851/0140618 - specific cofactor versions of parent term

## Notes

- The definition change for GO:0000293 maintains backward compatibility in intent while improving accuracy. Existing annotations using this term will remain valid and more accurate (most annotated terms are likely specific siderophore reductases that are also chelate reductases).
- The new parent term enables proper annotation of non-siderophore chelate reductases and general ferric iron reductases.
- The Frp1/Fip1-Fio1 system, which was the original driver of this issue, can now be accurately annotated with GO:7770068 (or potentially created as a child term if cofactor specificity becomes important in the future).

---
🤖 **Generated by claude agent**
- Runtime: `claude`
- Model: `claude-haiku-4-5-20251001`
- Agent config: `ai4curation/go-ontology-agent-config@v9:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-go/actions/runs/25640377531)


#### Agent Issue Comment

# Issue #27593 - NTR ferric iron reductase (for non siderophore)

## Summary

Completed the request to create a new ferric iron reductase term and refine the ferric-chelate reductase definition.

## Changes Made

1. **New term created: GO:7770068 - ferric iron reductase activity**
   - Reaction: `2 Fe3+ + NADP+ + H+ = 2 Fe2+ + NADPH` (RHEA:71767)
   - References: PMID:8321236, PMID:34614242, PMID:39940646
   - Parent: GO:0016722 (oxidoreductase activity, acting on metal ions)

2. **GO:0000293 (ferric-chelate reductase activity) updated**
   - Definition refined: "Fe3+-siderophore" → "Fe3+-chelate" (both substrate and product sides)
   - New parent: GO:7770068 (ferric iron reductase activity)
   - Now properly distinguished from general iron reduction

## Biological Rationale

The Frp1/Fip1-Fio1 iron uptake system in fission yeast reduces unchelated ferric iron, distinct from siderophore-specific chelate reductases. The new parent term (GO:7770068) enables accurate annotation of proteins with general ferric iron reductase activity, while GO:0000293 now correctly specifies chelate-dependent reduction.

Changes committed in PR <NN>

---
🤖 **Generated by claude agent**
- Runtime: `claude`
- Model: `claude-haiku-4-5-20251001`
- Agent config: `ai4curation/go-ontology-agent-config@v9:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-go/actions/runs/25640377531)


#### Agent Diff

```diff
diff --git a/src/ontology/go-edit.obo b/src/ontology/go-edit.obo
index 5b4d6c89f..69ad86c59 100644
--- a/src/ontology/go-edit.obo
+++ b/src/ontology/go-edit.obo
@@ -3208,10 +3208,12 @@ intersection_of: has_primary_input SO:0000587 ! group_I_intron
 id: GO:0000293
 name: ferric-chelate reductase activity
 namespace: molecular_function
-def: "Catalysis of the reaction: 2 Fe3+-siderophore + electron donor = 2 Fe2+-siderophore + electron acceptor." [PMID:33559753]
+def: "Catalysis of the reaction: 2 Fe3+-chelate + electron donor = 2 Fe2+-chelate + electron acceptor." [PMID:33559753]
 synonym: "ferric chelate reductase activity" EXACT []
 synonym: "iron chelate reductase activity" EXACT []
+is_a: GO:7770068 ! ferric iron reductase activity
 is_a: GO:0016722 ! oxidoreductase activity, acting on metal ions
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/27593" xsd:anyURI
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/21029" xsd:anyURI
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/26726" xsd:anyURI
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30815" xsd:anyURI
@@ -617387,6 +617389,20 @@ property_value: term_tracker_item "https://github.com/geneontology/go-ontology/i
 created_by: dragon-ai-agent
 creation_date: 2026-04-21T19:33:16Z
 
+[Term]
+id: GO:7770068
+name: ferric iron reductase activity
+namespace: molecular_function
+def: "Catalysis of the reaction: 2 Fe3+ + NADP+ + H+ = 2 Fe2+ + NADPH." [PMID:8321236, PMID:34614242, PMID:39940646, RHEA:71767]
+synonym: "ferric reductase activity" RELATED []
+synonym: "iron(III) reductase activity" EXACT [EC:1.16.1.-]
+xref: EC:1.16.1.- {source="skos:broadMatch"}
+xref: RHEA:71767 {source="skos:exactMatch"}
+is_a: GO:0016722 ! oxidoreductase activity, acting on metal ions
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/27593" xsd:anyURI
+created_by: dragon-ai-agent
+creation_date: 2026-05-10T00:00:00Z
+
 [Typedef]
 id: acts_on_population_of
 name: acts on population of

```

#### Review by gpt-5-codex

**outcome**: partial_success  **f1**: 0.643  **precision**: 0.643  **recall**: 0.643

**Failure modes**: wrong_pattern, missed_requirement, over_editing

<!-- Review this eval run following analysis/instructions/review-agent-eval.md

  Source issue: https://github.com/geneontology/go-ontology/issues/27593
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/31997
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/195
  Agent config: ai4curation/go-ontology-agent-config

  Quick reference:
    gh issue view 27593 --repo geneontology/go-ontology
    gh pr diff 31997 --repo geneontology/go-ontology
    gh pr diff 195 --repo ai4curation/eval-ont-agent-go
-->

## Summary

The agent addressed the main shape of issue #27593 by creating `GO:7770068` for ferric iron reductase activity and making `GO:0000293` a ferric-chelate subtype with a broader chelate-based definition. The metadiff score (F1 0.643) is directionally fair: the agent found the right terms and much of the same edit surface, but it introduced a materially wrong reaction equation and weaker hierarchy/xref choices compared with the merged human PR.


## Strengths

- Created the requested new molecular function term `GO:7770068` "ferric iron reductase activity", with the same GO ID, label, namespace, issue tracker link, and core PMID evidence set used by the human PR (`PMID:8321236`, `PMID:34614242`, `PMID:39940646`).
- Correctly recognized that `GO:0000293` "ferric-chelate reductase activity" should be made more general than siderophore-specific wording, changing both substrate and product text from `siderophore` to `chelate`. This matches the human PR's chemically consistent fix.
- Correctly placed `GO:0000293` under the new `GO:7770068` term, capturing the intended relationship that ferric-chelate reductase activity is a subtype of ferric iron reductase activity.
- Added a `term_tracker_item` for issue #27593 to both the new term and the edited `GO:0000293`, matching the traceability expected for this ontology edit.


## Issues

- The definition for `GO:7770068` has the wrong reaction: `2 Fe3+ + NADP+ + H+ = 2 Fe2+ + NADPH`. This does not match the cited `RHEA:71767`, which the human PR used as `2 Fe2+ + NADP+ + H+ = 2 Fe3+ + NADPH`, and it is also chemically inconsistent for a ferric reductase because it reduces both Fe3+ and NADP+ in the same direction.
- The parent for `GO:7770068` is less specific than the human solution. The agent used `is_a: GO:0016722` "oxidoreductase activity, acting on metal ions", while the merged PR used `GO:0016723` "oxidoreductase activity, acting on metal ions, NAD or NADP as acceptor", matching the NADP-based Rhea reaction and preserving the intended oxidoreductase hierarchy.
- The agent retained the old direct `is_a: GO:0016722` on `GO:0000293` while adding `is_a: GO:7770068`. The human PR replaced the old parent, avoiding a redundant asserted parent that should be entailed through `GO:7770068 -> GO:0016723 -> GO:0016722`.
- Synonym and xref choices diverged from the accepted PR. The human PR added exact synonyms `"ferric reductase activity"` and `"Fe3+ reductase activity"` plus only the exact Rhea xref; the agent downgraded `"ferric reductase activity"` to RELATED, omitted `"Fe3+ reductase activity"`, added `"iron(III) reductase activity"` as EXACT, and added a broad EC xref `EC:1.16.1.-` that was not part of the accepted edit.

### Attempt 9: gpt-5.4 / codex

- **Eval PR**: [#174](https://github.com/ai4curation/eval-ont-agent-go/pull/174)
- **F1**: 0.593  **Precision**: 0.571  **Recall**: 0.615  **Jaccard**: 0.421
- **Workflow run**: [25640326272](https://github.com/ai4curation/eval-ont-agent-go/actions/runs/25640326272)

#### Agent PR Comment

This PR addresses issue #27593 by adding a new MF term for the Frp1-style ferric iron reductase reaction and by correcting the generic ferric-chelate parent definition.

Changes made:
- Added `GO:7770068` `ferric iron reductase (NADPH) activity`
  - Definition: `Catalysis of the reaction: 2 Fe(2+) + NADP(+) + H(+) = 2 Fe(3+) + NADPH.`
  - Provenance: `RHEA:71767`, `PMID:8321236`, `PMID:34614242`
  - Parent: `GO:0016723 oxidoreductase activity, acting on metal ions, NAD or NADP as acceptor`
- Updated `GO:0000293 ferric-chelate reductase activity`
  - Changed the definition from `Fe3+-siderophore ... Fe2+-siderophore` to `Fe3+-chelate ... Fe2+-chelate`

Rationale:
- The issue request clearly needs a term that can support annotation of Frp1-like reductive iron assimilation enzymes that reduce ferric iron in an NADPH-dependent reaction.
- `RHEA:71767` provides the exact reaction chemistry requested in the issue.
- The broad parent `GO:0000293` was mislabeled in practice by a siderophore-only definition; switching that definition to `chelate` matches the label and avoids conflating chelates with siderophores.
- I did not make `GO:0000293` a subclass of the new term. `GO:0000293` is generic with respect to donor/acceptor and is about ferric chelates broadly; the new term is specific to an NADPH-dependent free-ferric-ion reaction. That reparenting would overstate the biology and narrow the generic term incorrectly.
- I validated `PMID:39940646` during research, but did not use it in the new definition provenance because it is contextual review support rather than the strongest source for the specific catalytic reaction.

Checklist:
- [x] PLAN: The issue and comments were reviewed and the intended ontology change was clear.
- [x] PRE-VALIDATION: `make travis_build` passed before the edit.
- [x] RESEARCH: Completed and recorded in `RESEARCH.md`.
- [x] TERM-SEARCH: Relevant GO terms and reaction-term precedent were checked with `obo-grep.pl`.
- [x] DESIGN-PATTERNS: Checked and recorded in `DESIGN_PATTERNS.md`.
- [x] EDITS: Used checkout/checkin workflow via `obo-checkout.pl` and `obo-checkin.pl`.
- [x] RELATIONSHIPS: Parentage reviewed; no incorrect logical axioms added.
- [x] logical definitions are appropriate, and are not over-specified, and conform to DESIGN_PATTERNS.md doc
- [x] relationships conform to other similar terms in the ontology
- [x] is_a is not over-asserted
- [x] is_a, part_of, and other relationships specified appropriately
- [x] SPECIALIZED-EDITS: `/reaction`, `/research`, `/design-pattern`, and `/chemical-entity` skill guidance consulted as appropriate.
- [x] METADATA: New term includes `term_tracker_item`, `created_by`, and `creation_date`; existing term metadata was left untouched.
- [x] AUTOMATED-VALIDATION: `cd src/ontology && make travis_build` passed after the edit.
- [x] REFERENCE-VALIDATION: PMIDs were cached and validated; support text in `RESEARCH.md` was validated with `linkml-reference-validator`.
- [x] CHANGES-COMMITTED
- [x] RELEVANT-FILES: Only `src/ontology/go-edit.obo` was committed.
- [x] ACCURACY: The change is aligned with the issue and with reaction-term precedent.
- [x] ISSUE-ALIGNMENT: The final edit delivers the requested new annotation target and fixes the parent definition without adding an invalid subclass axiom.
- [ ] PR is created or amended
- [ ] Communicate high level summary of changes on original issue(s), and any requests for further info
- [ ] Communicated on PR detailed description of changes made, and rationale. Include checklists.

---
🤖 **Generated by codex agent**
- Runtime: `codex`
- Model: `gpt-5.4`
- Agent config: `ai4curation/go-ontology-agent-config@v9:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-go/actions/runs/25640326272)


#### Agent Issue Comment

Addressed in PR #<NN>.

Summary:
- Added `GO:7770068` `ferric iron reductase (NADPH) activity` for the `RHEA:71767` reaction.
- Corrected `GO:0000293 ferric-chelate reductase activity` so its definition now uses `chelate` rather than `siderophore`.

One modeling choice to flag: I did not make `GO:0000293` a subclass of the new term. `GO:0000293` is a donor/acceptor-generic ferric-chelate reductase term, while the new term is specific to the NADPH/free-ferric-ion reaction. Putting the generic chelate term under the NADPH-specific reaction term would be too strong.

If a broader grouping term for ferric iron reductases is still wanted for curator findability, that would fit better as a separate parent term, as discussed in the related thread.

---
🤖 **Generated by codex agent**
- Runtime: `codex`
- Model: `gpt-5.4`
- Agent config: `ai4curation/go-ontology-agent-config@v9:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-go/actions/runs/25640326272)


#### Agent Diff

```diff
diff --git a/src/ontology/go-edit.obo b/src/ontology/go-edit.obo
index 5b4d6c89f..78c01e844 100644
--- a/src/ontology/go-edit.obo
+++ b/src/ontology/go-edit.obo
@@ -3208,7 +3208,7 @@ intersection_of: has_primary_input SO:0000587 ! group_I_intron
 id: GO:0000293
 name: ferric-chelate reductase activity
 namespace: molecular_function
-def: "Catalysis of the reaction: 2 Fe3+-siderophore + electron donor = 2 Fe2+-siderophore + electron acceptor." [PMID:33559753]
+def: "Catalysis of the reaction: 2 Fe3+-chelate + electron donor = 2 Fe2+-chelate + electron acceptor." [PMID:33559753]
 synonym: "ferric chelate reductase activity" EXACT []
 synonym: "iron chelate reductase activity" EXACT []
 is_a: GO:0016722 ! oxidoreductase activity, acting on metal ions
@@ -617387,6 +617387,20 @@ property_value: term_tracker_item "https://github.com/geneontology/go-ontology/i
 created_by: dragon-ai-agent
 creation_date: 2026-04-21T19:33:16Z
 
+[Term]
+id: GO:7770068
+name: ferric iron reductase (NADPH) activity
+namespace: molecular_function
+def: "Catalysis of the reaction: 2 Fe(2+) + NADP(+) + H(+) = 2 Fe(3+) + NADPH." [RHEA:71767, PMID:8321236, PMID:34614242]
+synonym: "ferric iron reductase activity" BROAD []
+synonym: "NADPH:Fe(3+) oxidoreductase activity" EXACT []
+synonym: "NADPH:Fe3+ oxidoreductase activity" EXACT []
+xref: RHEA:71767 {source="skos:exactMatch"}
+is_a: GO:0016723 ! oxidoreductase activity, acting on metal ions, NAD or NADP as acceptor
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/27593" xsd:anyURI
+created_by: dragon-ai-agent
+creation_date: 2026-05-10T21:41:48Z
+
 [Typedef]
 id: acts_on_population_of
 name: acts on population of

```

#### Review by gpt-5

**outcome**: partial_success  **f1**: 0.593  **precision**: 0.571  **recall**: 0.615

**Failure modes**: under_editing, missed_requirement, wrong_pattern

<!-- Review this eval run following analysis/instructions/review-agent-eval.md

  Source issue: https://github.com/geneontology/go-ontology/issues/27593
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/31997
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/174
  Agent config: ai4curation/go-ontology-agent-config

  Quick reference:
    gh issue view 27593 --repo geneontology/go-ontology
    gh pr diff 31997 --repo geneontology/go-ontology
    gh pr diff 174 --repo ai4curation/eval-ont-agent-go
-->

## Summary

The agent partially addressed geneontology/go-ontology#27593: it added `GO:7770068` and updated the `GO:0000293` definition from siderophore-specific wording to chelate wording. However, it diverged from the accepted solution by making the new term `ferric iron reductase (NADPH) activity` rather than the requested broader `ferric iron reductase activity`, and by leaving `GO:0000293` under `GO:0016722` instead of reparenting it to the new term. The metadiff score (F1 0.593, precision 0.571, recall 0.615) is a fair warning: the core new term exists, but important ontology structure and naming details are wrong or missing.


## Strengths

- Added the correct new ID, `GO:7770068`, in the molecular function namespace and linked it to the requested tracker item for issue #27593.
- Used the same RHEA reaction cross-reference as the human PR, `xref: RHEA:71767 {source="skos:exactMatch"}`, and placed the new term under `GO:0016723` oxidoreductase activity, acting on metal ions, NAD or NADP as acceptor.
- Updated `GO:0000293` ferric-chelate reductase activity so the definition now says `Fe3+-chelate` and `Fe2+-chelate` rather than the overly narrow `Fe3+-siderophore` and `Fe2+-siderophore`.
- Included useful literature support in the new `GO:7770068` definition (`PMID:8321236` and `PMID:34614242`) and added reasonable NADPH:Fe(3+) oxidoreductase synonyms for the narrower reaction concept it modeled.


## Issues

- The new term label is too narrow relative to the issue and accepted PR. The human solution adds `GO:7770068` as `ferric iron reductase activity`; the agent instead names it `ferric iron reductase (NADPH) activity` and demotes the requested generic label to a BROAD synonym.
- The agent did not reparent `GO:0000293` under `GO:7770068`. The accepted PR changes `GO:0000293` from `is_a: GO:0016722` to `is_a: GO:7770068`, making ferric-chelate reductase a child of ferric iron reductase and preserving the old ancestry through `GO:7770068 -> GO:0016723 -> GO:0016722`.
- The agent did not add the issue #27593 `term_tracker_item` to the edited existing term `GO:0000293`, which the human PR did.
- The accepted exact synonyms for `GO:7770068`, `ferric reductase activity` and `Fe3+ reductase activity`, are missing. The agent added NADPH-specific exact synonyms instead, consistent with its narrower label but less aligned with the requested generic annotation target.
- The agent omitted `PMID:39940646` from the `GO:7770068` definition xrefs. This is not the largest problem, but it is another under-edit compared with the accepted PR.
- The definition uses RHEA-style charged formulas (`Fe(2+)`, `NADP(+)`, `Fe(3+)`) rather than the accepted GO text style (`Fe2+`, `NADP+`, `Fe3+`). This is likely syntactically valid, but less consistent with the surrounding GO edit and the human solution.
