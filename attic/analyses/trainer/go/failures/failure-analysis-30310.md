# Failure Analysis: PR #30310

## PR Title
Merge GO:0017050 D-erythro-sphingosine kinase activity into GO:0008481 sphingosine kinase activity

## Failure Mode
**Multiple GO obsoletion convention violations**

## What Happened
1. Agent created initial PR with the following issues:
   - Used `alt_id` incorrectly (this was not a direct merge)
   - Did not prefix obsolete term name with "obsolete"
   - Used `consider` tag instead of `replaced_by`
   - Did not move xrefs from obsolete term to replacement term

2. Reviewer (@cmungall) requested changes on existing branch
3. **Agent created a NEW PR (#30312) instead of updating the existing branch**

## Reviewer Feedback
From @cmungall:
> - don't do `alt_id`, this is not a full merge
> - the names of obsolete terms should start with `obsolete `
> - use `replaced_by` rather than consider (this is an ObsoletionWithDirectReplacement)
> Please make the changes on this branch rather than making a new PR

## Root Causes
1. **Lack of knowledge about GO obsoletion conventions**
2. **Failure to update existing branch** when asked to revise
3. **Incomplete understanding of merge vs obsoletion patterns**

## Correct Approach
When obsoleting a GO term:
1. Prefix the term name with "obsolete "
2. Prefix definition with "OBSOLETE. "
3. Use `replaced_by` for direct replacements (ObsoletionWithDirectReplacement)
4. Use `consider` only when multiple alternatives exist
5. Remove all is_a parents from obsolete terms
6. Move xrefs to the replacement term with appropriate qualifiers (exactMatch, narrowMatch)
7. Do NOT use `alt_id` unless it's a true merge
8. Always update the existing branch, never create a new PR when revising

## Status
Closed without merge - replaced by PR #30312
