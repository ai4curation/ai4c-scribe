# Failure Analysis: PR #30312

## PR Title
Merge GO:0017050 D-erythro-sphingosine kinase activity into GO:0008481 sphingosine kinase activity

## Failure Mode
**Duplicate PR creation + Obsolete term still had superclass**

## What Happened
1. This PR was created after #30310 was reviewed
2. Agent created a NEW PR instead of updating the existing branch
3. Even after fixing some issues, the obsolete term still had a superclass which violates GO rules
4. Additionally, obsoletion has more complexity that wasn't addressed:
   - Email announcement required
   - Annotation review needed
   - RHEA reaction participants file needs updating

## Reviewer Feedback
From @sjm41:
> FAIL Rule ../sparql/obsolete-reference-violation.sparql: 1 violation(s)
> obsolete,reason
> http://purl.obolibrary.org/obo/GO_0017050,Obsolete term should not have a superclass

From @pgaudet:
> For training the AI:
> - obsoletion is more complex, we need to send an email announcement, we need to review annotations
> - if there are RHEA xrefs we need to update the reaction participants file.
> I did this manually.

## Root Causes
1. **Created new PR instead of updating existing branch**
2. **Incomplete obsoletion** - did not remove superclass (is_a parent)
3. **Lack of awareness of full obsoletion workflow** (email, annotations, RHEA)

## Correct Approach
When obsoleting GO terms:
1. ALWAYS update existing PR branch, never create new PR
2. Remove ALL logical axioms including:
   - `is_a` (superclass relationships)
   - `intersection_of`
   - `relationship:`
3. Be aware that obsoletion may require:
   - Email announcement to GO mailing list
   - Annotation review by curators
   - RHEA reaction participants file updates

## Status
Closed without merge - handled manually by curator
