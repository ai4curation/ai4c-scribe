# Skill Discovery: Claude Code vs Codex

## How progressive disclosure works (same principle, different paths)

Both harnesses follow the [Agent Skills](https://agentskills.io) open standard's three-stage progressive disclosure:

1. **Discovery**: at startup, scan skill directories and load only `name` + `description` from SKILL.md frontmatter
2. **Activation**: when a task matches a skill description, load the full SKILL.md content into context
3. **Execution**: the agent follows the skill instructions, optionally running bundled scripts

The skill descriptions (not the full content) are injected into context as part of the system prompt. This is why descriptions matter — they're what the model sees to decide whether to activate a skill. The full SKILL.md body loads only on activation, keeping context costs low.

### Context budgets

- **Claude Code**: skill descriptions capped at ~1% of context window (dynamic), with each entry's combined `description` + `when_to_use` truncated at 1,536 chars. Configurable via `SLASH_COMMAND_TOOL_CHAR_BUDGET` env var.
- **Codex**: skill descriptions capped at ~2% of context (~8,000 chars when context size unknown). Descriptions shortened when many skills exist.

## Directory paths

| Harness | Project skills | User skills | Instruction file |
|---------|---------------|-------------|-----------------|
| Claude Code | `.claude/skills/` | `~/.claude/skills/` | `CLAUDE.md` |
| Codex | `.agents/skills/` | `~/.agents/skills/` | `AGENTS.md` |

Both support the same SKILL.md format (name, description in YAML frontmatter, markdown body).

## Known gotchas

### Symlinks with Codex

Codex has had issues with symlinked `.agents/skills/` directories ([openai/codex#11314](https://github.com/openai/codex/issues/11314)). The issue was closed as "not planned" with the root cause identified as invalid relative symlink paths. However, community reports suggest symlink discovery remains unreliable in some environments. Our justfile creates `ln -sf ../.claude/skills .agents/skills` which should resolve correctly, but we haven't confirmed native discovery is working (see below).

**Recommendation**: consider copying skills to `.agents/skills/` instead of symlinking for maximum reliability.

### `codex exec` mode and skills

The official documentation does not explicitly confirm whether `codex exec` (headless/CI mode) performs skill discovery. [Community guides](https://www.getaiperks.com/en/blogs/36-codex-skills-best-practices-2026) state that "Codex CLI can run Skills in headless mode for CI/CD automation" but provide no specifics on whether the exec subcommand performs the same startup discovery as interactive mode.

### Distinguishing native discovery from model-driven discovery

A challenge in trace analysis: if skill discovery happens in the harness (before the first model call), it injects skill descriptions into the system prompt. These descriptions are invisible in the agent trace — you only see the model's subsequent decisions. When the model then runs `rg --files -g '.claude/**/SKILL.md'` to read skill files, this could mean either:

1. **Native discovery worked**: the model saw skill descriptions in its system prompt, matched the task, and loaded the full content via shell commands (normal activation behavior)
2. **Native discovery failed**: the model found no skill descriptions but independently searched for instruction files based on references in AGENTS.md

We cannot distinguish these cases from the trace alone. The JSONL trace from `codex exec --json` records only conversation-level events (tool calls, messages), not system prompt construction.

### CLAUDE.md vs AGENTS.md

Codex reads `AGENTS.md` as its project instruction file. It does NOT read `CLAUDE.md` by default. The `project_doc_fallback_filenames` config option could theoretically add CLAUDE.md as a fallback, but defaults to empty. Our workaround: create `AGENTS.md` as a symlink to `CLAUDE.md`.

The [Codex customization docs](https://developers.openai.com/codex/concepts/customization) describe AGENTS.md as loaded first, with skills discovered afterward. AGENTS.md content constrains how skills operate.

## Our current setup

The agent config repos create:
- `CLAUDE.md` (canonical instructions, used by Claude Code natively)
- `AGENTS.md` → symlink to `CLAUDE.md` (for Codex)
- `.claude/skills/` (canonical skill directory, used by Claude Code natively)
- `.agents/skills/` → symlink to `.claude/skills/` (for Codex, but may not work reliably)

### What traces show

In GO ontology Codex runs (v8 config), the model:
- Searched for `AGENTS.md` and `.claude/**/SKILL.md` (not `.agents/skills/`)
- Read 4 skill files: term-obsoletion, reaction, design-pattern, research
- Used the term checkout/checkin workflow described in the skills

This could indicate either native discovery failure (model searching on its own) or native discovery success (model loading full content after seeing descriptions). The fact that it searched `.claude/**` rather than `.agents/**` slightly favors the "native discovery didn't work" interpretation, since native discovery would have pointed the model to `.agents/skills/`.

## Recommendations for the paper

1. Report that both harnesses implement the Agent Skills progressive disclosure standard
2. Note that Codex's discovery from symlinked directories is not reliably confirmed
3. The ablation study (skills vs no-skills) shows identical Codex scores, consistent with either "native discovery failed and model found skills via search" OR "skills are consumed but don't change behavior on simple tasks"
4. Further testing needed with harder cases where skill content would be expected to alter the approach

## References

- [Agent Skills standard](https://agentskills.io)
- [Claude Code skills docs](https://code.claude.com/docs/en/skills)
- [Codex skills docs](https://developers.openai.com/codex/skills)
- [Codex customization stack](https://codex.danielvaughan.com/2026/04/12/codex-cli-customisation-stack-unified-system/)
- [Codex symlink issue #11314](https://github.com/openai/codex/issues/11314)
- [Codex skills best practices](https://www.getaiperks.com/en/blogs/36-codex-skills-best-practices-2026)
- [SKILL.md troubleshooting](https://www.agensi.io/learn/skill-md-not-loading-troubleshooting)
