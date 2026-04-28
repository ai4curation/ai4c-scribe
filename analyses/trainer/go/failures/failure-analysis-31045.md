# Failure Analysis: PR #31045

## PR Title
Add new term: glycoprotein cargo receptor activity (GO:7770028)

## Failure Mode
**Superseded by corrected version (PR #31046)**

## What Happened
1. Agent created this PR for glycoprotein cargo receptor activity
2. The term used GO:7770028 as the ID
3. This conflicted with PR #31004 which also used GO:7770028
4. A corrected version was created as PR #31046 (which was merged)

## The Term ID Conflict
- PR #31004 (Nov 4): Created GO:7770028 for N-acetyl-D-glucosamine transmembrane transporter
- PR #31045 (Nov 10): Created GO:7770028 for glycoprotein cargo receptor activity

Same term ID used for completely different concepts!

## Root Causes
1. **Term ID collision** - did not check if GO:7770028 was already proposed
2. **No coordination between tasks** - different PRs using same ID
3. **Did not verify term ID availability** before creating new terms

## Correct Approach
Before creating new GO terms:
1. Check if the proposed term ID is already in use
2. Check if there are pending PRs using the same ID
3. Use the next available sequential ID in the GO:777xxxx range
4. Consider checking the ID registry or recent PRs

## Status
Closed without merge - superseded by PR #31046 with correct term ID
