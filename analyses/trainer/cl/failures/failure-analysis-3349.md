# Failure Analysis: PR #3349

**PR:** [#3349 - Generate links between CL terms and LungMap Cell Cards with automated discovery](https://github.com/obophenotype/cell-ontology/pull/3349)

**Issue:** [#3348](https://github.com/obophenotype/cell-ontology/issues/3348)

**Status:** CLOSED (not merged)

**Closed:** 2025-09-26

## Summary

The issue requested generating links between Cell Ontology terms and LungMap Cell Cards by browsing the LungMap website to find exact matches. The agent was unable to access external web resources and instead created infrastructure for manual discovery.

## What the Agent Did

1. Added one known annotation (CL:0002062 -> LMCC0000000003)
2. Created a Python script (`build_lungmap_links.py`) for fetching LungMap data
3. Added Makefile targets for lungmap integration
4. Created documentation for manual verification
5. Identified 47 potential lung-related CL terms programmatically

## Why It Failed

### Root Cause: Capability Limitation

The agent could not browse external websites to gather the required data. When asked if it could browse LungMap:

dosumis:
> "@copilot - in the absence of an API are you able to browse links on the lungmap cell cards page to find more links?"

Agent explained it created a framework but couldn't actually fetch the data due to network access restrictions.

dosumis:
> "Hmmm - I'll call this a fail. Will try locally with a web browsing MCP."

### Technical Limitation

GitHub Copilot SWE Agent runs in a sandboxed environment that blocks:
- External HTTP requests to arbitrary websites
- Web scraping operations
- Real-time data fetching from external APIs

## Failure Mode

**Category:** Capability limitation - external web access

**Severity:** N/A (not a behavioral issue - infrastructure limitation)

## Lessons Learned

1. **Recognize capability boundaries**: Tasks requiring external web browsing are outside the agent's capabilities
2. **Communicate limitations early**: Rather than building elaborate workarounds, clearly state what cannot be done
3. **Don't create over-engineered alternatives**: The scripts and infrastructure created added complexity without solving the core problem

## What Should Have Happened

The agent should have:
1. Immediately recognized this task requires external web access
2. Stated clearly: "I cannot browse external websites like LungMap. This task requires a web browsing capability (MCP) or manual curation."
3. Not created elaborate workaround infrastructure that doesn't solve the problem

## Remediation

For tasks requiring external web access:
```
Response template:
"This task requires browsing external websites (LungMap Cell Cards), which I cannot do due to
network access restrictions. Alternative approaches:
1. Use a web browsing MCP locally
2. Provide the data as input (e.g., a CSV of LungMap -> CL mappings)
3. Manual curation by a human curator"
```

## Training Instruction

```
When an issue requires:
- Browsing external websites
- Fetching data from external APIs without credentials
- Web scraping

Immediately respond:
"I cannot access external websites due to sandboxing restrictions.
This task requires [alternative approach]."

Do NOT:
- Create elaborate workaround scripts that don't solve the problem
- Add infrastructure that requires manual intervention anyway
- Spend time on partial solutions
```
