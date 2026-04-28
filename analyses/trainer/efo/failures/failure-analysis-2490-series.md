# Failure Analysis: Issue #2490 CHEBI Terms Series (13 PRs)

## Issue Title
Add CHEBI terms to 'response to ...' EFO terms

## PRs in Series
- PR #2491, #2493, #2494, #2497, #2501, #2502, #2505, #2507, #2509, #2511, #2514, #2558, #2559

## Failure Mode
**Excessive duplicate PR creation for single issue**

## What Happened

1. Issue #2490 requested adding `has_primary_input` (RO:0004009) axioms to EFO 'response to' terms
2. Agent created **13 separate PRs** attempting to solve the same issue
3. Each PR claimed to add different numbers of terms (14, 21, 25, 29, 41, 44, etc.)
4. No PR was merged; eventually the issue was resolved differently (likely merged via #2561)

### Timeline of PRs
| PR | Date | Terms Added | Status |
|----|------|-------------|--------|
| 2491 | First attempt | 21 terms | Closed |
| 2493 | Same day | 14 terms | Closed |
| 2494 | Same day | 4 terms | Closed |
| 2497 | Next day | 17→29 terms | Closed |
| 2501 | Later | 31 terms | Closed |
| 2502 | Later | 35 terms | Closed |
| 2505 | Later | 25 terms | Closed |
| 2507 | Later | 41 terms | Closed |
| 2509 | Later | 18 terms | Closed |
| 2511 | Later | 44 terms | Closed |
| 2514 | Later | 16 terms | Closed |
| 2558 | Later | 21 terms | Closed |
| 2559 | Later | 79 terms | Closed |

## Root Causes

1. **No branch reuse** - Agent created new branches/PRs instead of updating existing ones
2. **Inconsistent results** - Different runs produced different term counts
3. **No coordination** - Each run started fresh without checking for existing PRs
4. **Firewall issues** - Many runs blocked from accessing OLS/external resources

## Reviewer Feedback

From PR #2497 comments:
> @copilot what about the rest?

From PR #2558 comments:
> @copilot Can you use the EFO-importer to look into CHEBI to import the remaining terms?
> Agent response: "I don't have direct access to OLS MCP tools in my available functions"

## Correct Approach

1. Check for existing PRs on the same issue before creating new ones
2. If a PR exists, push commits to the same branch
3. If blocked by firewall/tools, document blockers clearly instead of creating new attempts
4. Maintain a consistent methodology across runs
5. Track which terms have been processed to avoid duplication

## Lessons Learned

- **ONE PR per issue** - Always update existing branches
- **Document blockers** - If tools are unavailable, say so clearly
- **Incremental progress** - Add commits to existing PR, not new PRs
- **Verification** - Ensure each run uses the same methodology for consistency
