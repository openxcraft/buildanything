## Stage 6 — The Two Execution Modes


Path A — No-AI (manual): print the 12×10 matrix and fill it by hand → collect answers from experience, prior projects, two interviews, quick research → every unknown becomes an assumption → draw the Blueprint on A3 → decompose onto sticky notes, one element per card → review with another person (the one-minute test) → fill the Readiness Pack.
Strength: full control, no hallucination, deep context. Limit: slow generation and coverage.

Path B — AI-assisted. Use the model in 6 roles only, and never give it approval authority:

```text
[P1] Question generation
"My idea: [...]. Using the twelve dimensions (identity, goal, user, scope,
outputs, time, place, resources, method, quality, risk, governance), generate
5 questions per dimension in the forms: what/who/why/how/when/where/how many/
which/is/what-if. Classify each: Critical / Important / Enhancement. Do not answer."

[P2] Conditional answering
"Answer these questions from what I have stated. Prefix every unconfirmed answer
with [ASSUMPTION] plus the reason and the impact if wrong. Do not invent numbers."

[P3] Audit
"Find: contradictions, gaps, scope bloat, non-measurable success criteria,
risks without fallback. Output as a list."

[P4] Assembly
"Summarize everything above into a one-page Blueprint with the ten fields.
Add no new information."

[P5] Decomposition
"Decompose outputs into elements of no more than 3 days. For each: full Element
Card + decision (Ready/Buy/Reuse/Build) + rationale + dependencies."

[P6] Readiness
"Review the 13-item Readiness Pack and list only what is missing."
```

Safety rule: every AI output is a draft until a human approves it. Numbers and dates are verified manually.

Stage 7 — Summary of Rules
