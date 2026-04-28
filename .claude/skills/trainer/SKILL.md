---
name: trainer
description: Use to analyze the failure modes of PRs by a given individual or agent, and come up with training strategies to improve acceptance rate.
---

First analyze and summarize all PRs in [PROJECT] for [GITHUB_ACCOUNT]. E.g. analyze go for failures from dragon-ai-agent

You can use pre-cached analyses/data/prs-go-cases-2000.jsonl. Collect which PRs were not merged. Summarize the general success rate.

Place this in a file analysis/trainer/PROJECT/summary.md. Make a checklist with every umerged PR, or every PR that was not merged first time.

Next, go through each failed PR, create a file analysis/trainer/PROJECT/failure-analysis-PRNUM.md

Make sure EVERY failure is accounted for

Finally, create analysis/trainer/PROJECT/training-plan.md, where you summarize all failure modes and write instructions that will help the agent on future iterations.
