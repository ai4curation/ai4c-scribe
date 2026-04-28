# Why SCRIBE?

SCRIBE addresses a fundamental challenge in adopting AI coding agents: **how do you know if they're actually good at your specific tasks?**

## The evaluation problem

AI coding agents (Claude Code, Cursor, GitHub Copilot, etc.) are increasingly capable, but their performance varies dramatically based on:

- **Domain**: Ontology editing differs from web development
- **Repository conventions**: Each project has implicit rules
- **Task complexity**: Simple typos vs. architectural changes
- **Context**: What information does the agent have access to?

General benchmarks like HumanEval or SWE-Bench provide useful baselines, but they don't answer the question that matters: **"Will this agent work well in my repository?"**

## SCRIBE's approach

SCRIBE lets you evaluate agents on **your actual tasks** using **your historical data**.

### Mining the past

Every merged PR in your repository represents:

- A real problem someone needed to solve
- A verified solution (it was merged)
- Rich context (issue discussions, review feedback)
- The exact starting point (base commit)

This is valuable evaluation data sitting unused in your git history.

### Reproducible testing

By checking out the repository at the commit *before* a PR was created, you can:

1. Give an agent the same information the human had
2. Let the agent attempt the fix
3. Compare the result to what the human actually did

This creates a fair, reproducible evaluation.

## Two complementary uses

### 1. Training data for LLMs

Extract PR data to train or fine-tune models:

```
GitHub History → Extract → Review Cases → Distill → Training Data
```

The "review case" format captures the state at first review, which is ideal for training LLM code reviewers.

### 2. Agent evaluation

Run agents against known problems:

```
Shadow Repo → Historical Issue → Agent Attempt → Compare to Human Solution
```

This tells you concretely how well an agent performs on tasks similar to your real work.

## Why GitHub-based projects?

SCRIBE focuses on GitHub repositories because:

1. **Git preserves everything**: Full commit history, diffs, timestamps
2. **PRs encode process**: Not just what changed, but the discussion and iteration
3. **Issues provide context**: The "why" behind changes
4. **APIs are accessible**: Easy to extract data programmatically

This applies beyond software:

- **Ontologies**: OBO Foundry projects (Mondo, Gene Ontology, Uberon)
- **Documentation**: Technical writing in Markdown
- **Data files**: CSV, JSON, YAML changes with review
- **Schemas**: LinkML, JSON Schema definitions

Any project with a review-based workflow benefits.

## The AI4Curation vision

SCRIBE is part of the broader [AI4Curation](https://github.com/ai4curation) initiative exploring how AI can assist knowledge curation.

Key principles:

### AI augments expertise

Curators have irreplaceable domain knowledge. AI can help with:

- Routine tasks (formatting, consistency checks)
- Research (finding relevant literature, cross-references)
- Quality assurance (catching errors)

But humans make the final judgment calls.

### Evaluation before deployment

Before using AI in production curation:

1. Define what "good" looks like
2. Test on representative tasks
3. Measure actual performance
4. Iterate on prompts and configurations

SCRIBE provides infrastructure for steps 2-4.

### Learning from history

Mature ontologies like Mondo have 15+ years of curation history. This represents:

- Thousands of expert decisions
- Established patterns and conventions
- Edge cases and their resolutions

Mining this history creates valuable training signal.

## Practical benefits

### For ontology projects

- Test agents on ontology-specific tasks (term additions, merges, obsoletions)
- Evaluate whether agents follow OBO conventions
- Build training data for domain-specific review

### For software projects

- Assess agents on repository-specific patterns
- Test on real bugs from your issue tracker
- Compare different models and configurations

### For research teams

- Systematic evaluation across multiple repositories
- Reproducible benchmarks for publications
- Iteration tracking for prompt engineering

## Getting started

Choose your path:

- **Extract training data**: [Tutorial: Your first extraction](../tutorials/first-extraction.md)
- **Evaluate agents**: [Tutorial: Shadow repo evaluation](../tutorials/shadow-repo-eval.md)
- **Understand the design**: Continue to [Shadow repos](shadow-repos.md)
