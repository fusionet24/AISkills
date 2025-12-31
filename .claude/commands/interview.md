---
allowed-tools: AskUserQuestion, Read, Glob, Grep, Write, Edit
argument-hint: [plan-file]
description: Interview to flesh out a plan/spec
version: 1.0
---

Here's the current plan:

@$ARGUMENTS

Interview me in detail AskUserQuestion to close only the gaps in the plan (missing decisions, assumptions, constraints, edge cases, tradeoffs). Don’t ask anything already answered. Prefer high-leverage questions; ask concise questions (use A/B options when useful). 

Be very in-depth and continue interviewing me continually until it's complete and no more questions exist for the current plan, then write the spec back to `$ARGUMENTS`.
