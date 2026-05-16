---
ontology: go-ontology
repo: geneontology/go-ontology
issue_number: 32005
pr_number: 32026
issue_title: 'Obsoletion request: GO:0009095 aromatic amino acid biosynthetic process,
  prephenate pathway'
pr_author: dragon-ai-agent
pr_merged_at: '2026-05-04'
task_type: obsoletion
difficulty: medium
scoping: tightly_scoped
scope: single_term
review_outcome: approved_first_time
num_agent_attempts: 12
generated_at: '2026-05-15'
domain_area: biological_process
best_f1: 0.927
best_model: gpt-5.5
---

# PR #32026 — Obsoletion request: GO:0009095 aromatic amino acid biosynthetic process, prephenate pathway

**go-ontology** | [geneontology/go-ontology](https://github.com/geneontology/go-ontology) | [Issue #32005](https://github.com/geneontology/go-ontology/issues/32005) | [PR #32026](https://github.com/geneontology/go-ontology/pull/32026) | @dragon-ai-agent | merged 2026-05-04

`obsoletion` `medium` `tightly_scoped` `approved_first_time`

## Context

Issue #32005 requested obsoletion of GO:0009095 "aromatic amino acid biosynthetic process, prephenate pathway". This term represented a pre-composed superpathway that conflated the general aromatic amino acid biosynthetic process with a specific pathway variant. The MetaCyc cross-reference it carried was to a superpathway entry, which is not how GO typically represents metabolic specificity.

## Changes Made

In `src/ontology/go-edit.obo`, GO:0009095 was obsoleted:
- Removed all logical axioms (is_a relationships, intersection_of definitions)
- Added obsoletion metadata: `is_obsolete: true`, `consider` tags pointing to the individual pathway steps
- Retained the MetaCyc xref for provenance
- Net reduction of 6 lines, reflecting removal of redundant axioms

## Resolution

Merged directly. The obsoletion rationale was clear: GO prefers atomic terms that can be composed via GO-CAM models rather than pre-composed superpathway terms. No annotation migration was needed since the term had minimal direct annotations.

## Human Diff

```diff
diff --git a/src/ontology/go-edit.obo b/src/ontology/go-edit.obo
index 961e08ab9..017033244 100644
--- a/src/ontology/go-edit.obo
+++ b/src/ontology/go-edit.obo
@@ -90265,20 +90265,14 @@ property_value: term_tracker_item "https://github.com/geneontology/go-ontology/i
 
 [Term]
 id: GO:0009095
-name: aromatic amino acid biosynthetic process, prephenate pathway
-namespace: biological_process
-def: "The chemical reactions and pathways resulting in the formation of phenylalanine and tyrosine from other compounds, including chorismate, via the intermediate prephenate." [GOC:mah, ISBN:0471331309, MetaCyc:PWY-3481]
-synonym: "aromatic amino acid family anabolism, prephenate pathway" EXACT []
-synonym: "aromatic amino acid family biosynthetic process via prephenate" EXACT [GOC:pr]
-synonym: "aromatic amino acid family biosynthetic process via prephenate(2-)" EXACT [GOC:pr]
-synonym: "aromatic amino acid family formation, prephenate pathway" EXACT []
-synonym: "aromatic amino acid family synthesis, prephenate pathway" EXACT []
-xref: MetaCyc:PWY-3481
-is_a: GO:0009073 ! aromatic amino acid biosynthetic process
-intersection_of: GO:0009058 ! biosynthetic process
-intersection_of: has_intermediate CHEBI:57852 ! prephenate(2-)
-intersection_of: has_primary_output CHEBI:33856 ! aromatic amino acid
-property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31091" xsd:anyURI
+name: obsolete aromatic amino acid biosynthetic process, prephenate pathway
+namespace: biological_process
+def: "OBSOLETE. The chemical reactions and pathways resulting in the formation of phenylalanine and tyrosine from other compounds, including chorismate, via the intermediate prephenate." [GOC:mah, ISBN:0471331309, MetaCyc:PWY-3481]
+comment: This term was obsoleted because it represents a pre-composed pathway combining L-phenylalanine and L-tyrosine biosynthesis. MetaCyc:PWY-3481 is the 'superpathway of L-phenylalanine and L-tyrosine biosynthesis' and is composed of two separate pathways (PWY-3462 L-phenylalanine biosynthesis II and PWY-3461 L-tyrosine biosynthesis II) which are already represented as narrowMatch xrefs on GO:0009094 (L-phenylalanine biosynthetic process) and GO:0006571 (L-tyrosine biosynthetic process), respectively. Annotations should be transferred to the appropriate consider term(s).
+consider: GO:0006571
+consider: GO:0009094
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/32005" xsd:anyURI
+is_obsolete: true
 
 [Term]
 id: GO:0009097

```

## Agent Attempts (12)

| # | Model | Runtime | F1 | P | R | Blob | Eval PR | Detail |
|---|-------|---------|-----|-----|-----|------|---------|--------|
| 1 | gpt-5.5 | opencode | 0.927 | 0.905 | 0.950 | `995aa71` | [#163](https://github.com/ai4curation/eval-ont-agent-go/pull/163) | [attempt](attempts/pr163.md) |
| 2 | gpt-5.5 | opencode | 0.927 | 0.905 | 0.950 | `995aa71` | [#145](https://github.com/ai4curation/eval-ont-agent-go/pull/145) | [attempt](attempts/pr145.md) |
| 3 | gpt-5.5 | codex | 0.927 | 0.905 | 0.950 | `80c9bf3` | [#127](https://github.com/ai4curation/eval-ont-agent-go/pull/127) | [attempt](attempts/pr127.md) |
| 4 | kimi-k2.6 | opencode | 0.080 | 0.952 | 0.042 | `9bfb355` | [#291](https://github.com/ai4curation/eval-ont-agent-go/pull/291) | [attempt](attempts/pr291.md) |
| 5 | claude-haiku-4.5 | claude | 0.080 | 0.952 | 0.042 | `8b1a7d9` | [#224](https://github.com/ai4curation/eval-ont-agent-go/pull/224) | [attempt](attempts/pr224.md) |
| 6 | gpt-5.4 | codex | 0.076 | 0.905 | 0.040 | `f1536da` | [#223](https://github.com/ai4curation/eval-ont-agent-go/pull/223) | [attempt](attempts/pr223.md) |
| 7 | claude-sonnet-4.5 | claude | 0.072 | 0.857 | 0.038 | `318b009` | [#491](https://github.com/ai4curation/eval-ont-agent-go/pull/491) | [attempt](attempts/pr491.md) |
| 8 | claude-sonnet-4.5 | claude | 0.072 | 0.857 | 0.038 | `318b009` | [#487](https://github.com/ai4curation/eval-ont-agent-go/pull/487) | [attempt](attempts/pr487.md) |
| 9 | gemma-4-31b | opencode | 0.017 | 0.190 | 0.009 | `961e08a` | [#525](https://github.com/ai4curation/eval-ont-agent-go/pull/525) | [attempt](attempts/pr525.md) |
| 10 | claude-sonnet-4.5 | copilot | 0.017 | 0.190 | 0.009 | `961e08a` | [#450](https://github.com/ai4curation/eval-ont-agent-go/pull/450) | [attempt](attempts/pr450.md) |
| 11 | claude-sonnet-4.5 | copilot | 0.017 | 0.190 | 0.009 | `961e08a` | [#404](https://github.com/ai4curation/eval-ont-agent-go/pull/404) | [attempt](attempts/pr404.md) |
| 12 | claude-opus-4.7 | claude | 0.017 | 0.190 | 0.009 | `961e08a` | [#324](https://github.com/ai4curation/eval-ont-agent-go/pull/324) | [attempt](attempts/pr324.md) |
