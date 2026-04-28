# Failure Analysis: PR #30604

## PR Title
Add taxon constraint for GO:0061708 excluding fungi

## Failure Mode
**Incorrect file format**

## What Happened
1. Agent attempted to add a taxon constraint to `src/taxon_constraints/never_in_taxon.tsv`
2. The format was incorrect
3. Reviewer closed the PR

## Reviewer Feedback
From @raymond91125:
> The format appears wrong.

## What Was Submitted
The PR added entries to `never_in_taxon.tsv` but the format did not match the expected TSV structure.

## Root Causes
1. **Did not properly inspect the existing file format** before making changes
2. **Assumed TSV format without verification**

## Correct Approach
When modifying configuration/data files:
1. First READ the existing file to understand the exact format
2. Note column headers and delimiter
3. Follow the exact same format for new entries
4. Validate the change passes any automated checks before submitting

## What the Correct Format Should Be
The `never_in_taxon.tsv` file has a specific structure that should be observed by reading the existing entries first.

## Status
Closed without merge - format was incorrect
