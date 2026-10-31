## Stage 2 — The Question Engine

Stage 2 — The Question Engine

2.1 The Matrix: 12 Dimensions × 10 Question Forms. Fill every cell with at least one question.

Dimension What Who Why How When Where How many Which Is/Does What if
1. Identity What exactly is it? Who owns it? Why does it exist? How is it defined? When does it start/end? Where does it live? How many versions? Which version first? Is it a project or product? What if its definition changes?
2. Goal What outcome? Who judges success? Why now? How is it measured? When do we evaluate? Where is it recorded? How many goals? Which goal is priority? Is the goal realistic? What if it isn't achieved?
3. User What is their need? Who are they? Why do they care? How do they use it? When do they use it? Where do they use it? How many users? Which segment first? Are they ready? What if they don't use it?
4. Scope What's in? Who approves it? Why this boundary? How do we prevent scope creep? When is it frozen? Where are system boundaries? How many items? Which item is deferred? Is scope sufficient? What if it expands?
5. Outputs What deliverables? Who receives them? Why these specifically? How are they delivered? When is each due? Where are they stored? How many? Which is first? Are they measurable? What if one is missing?
6. Time What schedule? Who is committed? Why this date? How do we track? When are milestones? Where is the calendar? How many hours/days? Which date is critical? Is the schedule realistic? What if we're late?
7. Place / Environment What environment? Who administers it? Why this one? How do we access it? When is it available? Where physically? How many envs (test/prod)? Which env first? Is it secure? What if it fails?
8. Resources What is required? Who supplies it? Why this quantity? How is it managed? When is it acquired? Where is it kept? How much does it cost? Which resource is critical? Is it enough? What if a resource is short?
9. Method What steps? Who executes? Why this method? How in detail? When is each step? Where is it executed? How many iterations? Which alternative? Is the method proven? What if it fails?
10. Quality What standard? Who inspects? Why this level? How do we measure? When do we inspect? Where are results logged? What acceptance rate? Which criterion is priority? Is it met? What if quality drops?
11. Risk What is the biggest risk? Who owns it? Why is it likely? How do we prevent it? When do we monitor? Where does it surface? What likelihood/impact? Which risk first? Do we have a fallback? What if it materializes?
12. Governance What decisions? Who is accountable? Why this authority? How is it documented? When do we review? Where is the log? How many reviews? Which decision needs approval? Is delegation clear? What if we disagree?

Result: ~120 customizable questions. Not all are always needed — but any empty cell is a hole in the picture.

2.2 The Two Modes

 No-AI AI-assisted
Question generation Use the matrix above as a paper checklist Give the model the idea + matrix to generate customized questions per cell
Answering Interviews + workshop + prior experience + analogous projects Model proposes answers; tag uncertain ones [assumption]
Audit Human reviewer + "what did we miss?" checklist Model scans for contradictions and gaps
Decision Manual scoring matrix Model proposes; humans approve

Hard rule: "Unknown" is never accepted bare. Every unknown becomes either a declared assumption or an open question with an owner and a due date.

2.3 Two Mandatory Logs

```text
Assumption Log
ID | Assumption | Why we assumed it | Impact if wrong | Who verifies | When

Open Questions Log
ID | Question | Dimension | Answer owner | Due | Status
```

G1: No empty cells; no "unknown" without an owner.

