---
ontology: mondo
repo: monarch-initiative/mondo
issue_number: 9861
pr_number: 10113
issue_title: '[NTR/gene] Hyperinsulinemic hypoglycemia, familial 3'
pr_author: MeeSiing
pr_merged_at: '2026-04-02'
task_type: other
difficulty: medium
scoping: tightly_scoped
scope: single_term
review_outcome: changes_requested
num_agent_attempts: 12
generated_at: '2026-05-17'
scoping_notes: PR relabels an existing term and updates its classification and synonyms
  based on user request.
domain_area: metabolic-disease
best_f1: 0.421
best_model: kimi-k2.6
---

# PR #10113 — [NTR/gene] Hyperinsulinemic hypoglycemia, familial 3

**mondo** | [monarch-initiative/mondo](https://github.com/monarch-initiative/mondo) | [Issue #9861](https://github.com/monarch-initiative/mondo/issues/9861) | [PR #10113](https://github.com/monarch-initiative/mondo/pull/10113) | @MeeSiing | merged 2026-04-02

`other` `medium` `tightly_scoped` `changes_requested`

## Context

A user requested a new gene-disease term for "hyperinsulinemic hypoglycemia, familial 3" (GCK-related hyperinsulinism) under issue #9861. During curation, it was determined that the existing term MONDO:0011236 already represented this disease but carried an outdated label. Rather than creating a duplicate, the curator updated the label and synonyms of the existing term. The PR also replaced an earlier failed attempt (PR #10090) that had git conflicts.

## Changes Made

The PR modified MONDO:0011236 in `src/ontology/mondo-edit.obo` with 13 additions and 6 deletions across 6 commits. Changes included updating the rdfs:label to "hyperinsulinemic hypoglycemia, familial, 3", adding "GCK-related hyperinsulinism" as an exact synonym, and adjusting the classification under MONDO:0017182 "familial hyperinsulinism." The multiple commits reflect both the review iteration (a CHANGES_REQUESTED review asking about classification) and the recreation of the PR after rebasing issues.

## Resolution

Medium difficulty because the curator needed to recognize that an existing term matched the new term request rather than creating a duplicate. The review process involved a classification question from the reviewer, requiring the contributor to confirm that the OMIM entry and the requested term were the same concept. An agent would need to search for existing terms before creating new ones and handle reviewer questions about hierarchical placement.

## Curation Note (data quality)

Flagged by claude-opus-4.7 on 2026-05-15 during agent-attempt review.

**This is NOT a poor case in the gold-PR sense:** PR #10113 is the complete and
sole human resolution of issue #9861. The other PR returned by search, #10090, is
merely the conflicted predecessor that #10113 replaced (`replace #10090` in the PR
body) — there are no companion PRs, and the CASE_BRIEF gold diff matches the merged
PR diff byte-for-byte.

**Why every attempt scores low F1 (0.188–0.421), and how to read it:** the low
scores are genuine substantive divergence, not a metadiff artifact. Two factors:

1. **Contradictory primary-label requirement.** The issue body lists
   "Hyperinsulinemic hypoglycemia, familial 3" as the *preferred gene-related
   syndrome label* and "GCK-related hyperinsulinism" as a *synonym*. The comment
   thread then reverses this: `tpollin` (Co-Chair, ClinGen Monogenic Diabetes GCEP)
   explicitly asks for "GCK-related hyperinsulinism" as the **primary** term. The
   gold curator chose the OMIM-style label "hyperinsulinemic hypoglycemia, familial,
   3" as primary and made "GCK-related hyperinsulinism" a ClinGen-preferred EXACT
   synonym (`{OMO:0002001=".../clingen"}`) — the opposite of `tpollin`'s stated
   request. 9/10 agents reasonably honored the explicit ClinGen request and were
   systematically penalized on precision for it. Treat the primary-label choice as a
   defensible interpretation, not an error.

2. **Reviewer-driven reclassification.** After a CHANGES_REQUESTED review by
   `katiermullen` about classification, the gold *removed* `is_a: MONDO:0015624`
   (diazoxide-sensitive diffuse hyperinsulinism), added
   `relationship: excluded_subClassOf MONDO:0015624`, and added
   `is_a: MONDO:0019010` (congenital isolated hyperinsulinism). This is not derivable
   from the issue text; no agent (single-shot, no reviewer dialogue) could foresee
   it. Do not penalize attempts for missing it beyond noting incompleteness.

**Recommended grading basis:** judge attempts on (a) the core disambiguation —
recognizing MONDO:0011236 already covers the request and updating it in place rather
than minting a duplicate; (b) refreshing the definition with the supplied
PMID:15277402/24890200/34680961 (and retaining Orphanet:79299); (c) correct ClinGen
`OMO:0002001` synonym handling; (d) provenance hygiene — adding the `#9861`
`IAO:0000233` tracker *without dropping* the existing `#4985` tracker. Metadiff F1
materially under-represents quality for the higher-tier attempts (kimi #270, the
gpt/copilot runs) and roughly tracks quality for the weakest (haiku #194, which also
has a malformed `intersection_of` axiom and an empty PR narrative).

## Human Diff

```diff
diff --git a/src/ontology/mondo-edit.obo b/src/ontology/mondo-edit.obo
index 70c79e85cd..819fd34156 100644
--- a/src/ontology/mondo-edit.obo
+++ b/src/ontology/mondo-edit.obo
@@ -280521,8 +280521,8 @@ property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/
 
 [Term]
 id: MONDO:0011236
-name: hyperinsulinism due to glucokinase deficiency
-def: "Hyperinsulism due to glucokinase deficiency (HIGCK) is a form of diazoxide-sensitive diffuse hyperinsulinism, caused by a lowered threshold for insulin release, characterized by an excessive/ uncontrolled insulin secretion (inappropriate for the level of glycemia) and recurrent episodes of profound hypoglycemia induced by fasting and protein rich meals, requiring rapid and intensive treatment to prevent neurological sequelae." [Orphanet:79299]
+name: hyperinsulinemic hypoglycemia, familial, 3
+def: "A form of diffuse hyperinsulinism due to glucokinase hyperactivity associated with a variation in the GCK gene, and characterized by an excessive/ uncontrolled insulin secretion (inappropriate for the level of glycemia) and recurrent episodes of hypoglycemia induced by fasting and glucose rich meals." [https://clinicalgenome.org/affiliation/40016/, Orphanet:79299, PMID:15277402, PMID:24890200, PMID:34680961]
 subset: doid {source="DOID:0070216"}
 subset: doid_rare {source="DOID:0070216"}
 subset: gard_rare {source="GARD:0002818", source="MONDO:GARD"}
@@ -280533,10 +280533,15 @@ subset: orphanet {source="Orphanet:79299"}
 subset: orphanet_rare {source="Orphanet:79299"}
 subset: otar {source="MONDO:OTAR"}
 subset: rare
-synonym: "HHF3" RELATED ABBREVIATION [GARD:0009930, MONDO:Lexical]
-synonym: "hyperinsulinemic hypoglycemia familial 3" RELATED [GARD:0009930]
-synonym: "hyperinsulinemic hypoglycemia, familial, 3" RELATED [MONDO:Lexical]
+synonym: "congenital glucokinase-related hyperinsulinism" EXACT [Orphanet:79299]
+synonym: "GCK-related hyperinsulinism" EXACT [https://clinicalgenome.org/affiliation/40016/] {OMO:0002001="https://w3id.org/information-resource-registry/clingen"}
+synonym: "glucokinase-related hyperinsulinemic hypoglycemia" EXACT [Orphanet:79299]
+synonym: "HHF3" EXACT ABBREVIATION [MONDO:Lexical, OMIM:602485]
+synonym: "hyperinsulinemic hypoglycemia due to glucokinase deficiency" EXACT [DOID:0070216]
+synonym: "hyperinsulinemic hypoglycemia familial 3" EXACT [GARD:0009930]
+synonym: "hyperinsulinemic hypoglycemia, familial, 3" EXACT [MONDO:Lexical]
 synonym: "hyperinsulinemic hypoglycemia, familial, type 3" EXACT [MONDO:RULE_1]
+synonym: "hyperinsulinism due to glucokinase deficiency" EXACT [DOID:0070216]
 xref: DOID:0070216 {source="MONDO:equivalentTo"}
 xref: GARD:0002818 {source="MONDO:GARD"}
 xref: ICD10CM:E16.1 {source="Orphanet:79299/attributed", source="Orphanet:79299/ntbt", source="Orphanet:79299"}
@@ -280547,11 +280552,13 @@ xref: Orphanet:79299 {source="OMIM:602485", source="MONDO:equivalentTo"}
 xref: SCTID:717182006 {source="MONDO:equivalentTo"}
 xref: UMLS:C1865290 {source="MONDO:equivalentTo", source="MONDO:MEDGEN", source="MEDGEN:355435"}
 is_a: MONDO:0005803 {source="DC-OMIM:602485"} ! hyperinsulinemic hypoglycemia
-is_a: MONDO:0015624 {source="Orphanet:79299"} ! diazoxide-sensitive diffuse hyperinsulinism
 is_a: MONDO:0017688 {source="Orphanet:79299", source="PMID:33340416"} ! disorder of glycolysis
+is_a: MONDO:0019010 {source="https://clinicalgenome.org/affiliation/40016/"} ! congenital isolated hyperinsulinism
+relationship: excluded_subClassOf MONDO:0015624 {source="Orphanet:79299", source="https://orcid.org/0000-0002-7638-4659"} ! diazoxide-sensitive diffuse hyperinsulinism
 relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/4195 {source="OMIM:602485"} ! GCK
 property_value: curated_content_resource "https://www.malacards.org/card/hyperinsulinemic_hypoglycemia_familial_3_2" xsd:anyURI {source="MONDO:MalaCards"}
 property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/4985" xsd:anyURI
+property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9861" xsd:anyURI
 property_value: seeAlso "https://rarediseases.info.nih.gov/diseases/9930/hyperinsulinemic-hypoglycemia-familial-3" xsd:anyURI {source="GARD:0009930"}
 
 [Term]

```

## Agent Attempts (12)

| # | Model | Runtime | F1 | P | R | Blob | Eval PR | Detail |
|---|-------|---------|-----|-----|-----|------|---------|--------|
| 1 | kimi-k2.6 | opencode | 0.421 | 0.421 | 0.421 | `5127b2f` | [#270](https://github.com/ai4curation/eval-ont-agent-mondo/pull/270) | [attempt](attempts/pr270.md) |
| 2 | claude-sonnet-4.5 | copilot | 0.400 | 0.316 | 0.545 | `f00c73a` | [#531](https://github.com/ai4curation/eval-ont-agent-mondo/pull/531) | [attempt](attempts/pr531.md) |
| 3 | claude-sonnet-4.5 | copilot | 0.400 | 0.316 | 0.545 | `f00c73a` | [#496](https://github.com/ai4curation/eval-ont-agent-mondo/pull/496) | [attempt](attempts/pr496.md) |
| 4 | gpt-5.4 | codex | 0.400 | 0.316 | 0.545 | `aab83f4` | [#170](https://github.com/ai4curation/eval-ont-agent-mondo/pull/170) | [attempt](attempts/pr170.md) |
| 5 | gpt-5.5 | opencode | 0.378 | 0.368 | 0.389 | `3fe151a` | [#76](https://github.com/ai4curation/eval-ont-agent-mondo/pull/76) | [attempt](attempts/pr76.md) |
| 6 | gpt-5.5 | opencode | 0.378 | 0.368 | 0.389 | `3fe151a` | [#55](https://github.com/ai4curation/eval-ont-agent-mondo/pull/55) | [attempt](attempts/pr55.md) |
| 7 | gpt-5.4 | opencode | 0.323 | 0.263 | 0.417 | `d404700` | [#741](https://github.com/ai4curation/eval-ont-agent-mondo/pull/741) | [attempt](attempts/pr741.md) |
| 8 | gpt-5.4 | opencode | 0.323 | 0.263 | 0.417 | `d404700` | [#685](https://github.com/ai4curation/eval-ont-agent-mondo/pull/685) | [attempt](attempts/pr685.md) |
| 9 | gpt-5.5 | codex | 0.312 | 0.263 | 0.385 | `bbf125f` | [#38](https://github.com/ai4curation/eval-ont-agent-mondo/pull/38) | [attempt](attempts/pr38.md) |
| 10 | claude-sonnet-4.5 | claude | 0.250 | 0.211 | 0.308 | `e79778b` | [#447](https://github.com/ai4curation/eval-ont-agent-mondo/pull/447) | [attempt](attempts/pr447.md) |
| 11 | claude-opus-4.7 | claude | 0.240 | 0.158 | 0.500 | `6b2861c` | [#381](https://github.com/ai4curation/eval-ont-agent-mondo/pull/381) | [attempt](attempts/pr381.md) |
| 12 | claude-haiku-4.5 | claude | 0.188 | 0.158 | 0.231 | `3009f15` | [#194](https://github.com/ai4curation/eval-ont-agent-mondo/pull/194) | [attempt](attempts/pr194.md) |
