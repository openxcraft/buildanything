## Stage 4 — Decompose into Small Elements


4.1 Each output (item 5) is split until you reach an element requiring no more than 1–3 days to implement.

4.2 Decision per element — Ready vs. Build

Decision When to choose What we need
Ready Exists and does the job as-is Link/license + acceptance test
Buy Exists but isn't ours, or cheaper to buy Option comparison + cost + terms
Reuse We have a prior version that can be adapted What needs changing + impact
Build No alternative meets the spec Spec + resources + time

Rule: never build before proving Ready is insufficient. Build is the last resort, not the first.

4.3 Element Card (mandatory, one per element)

```text
Element ID:            Name:
Function in one sentence:      Output:
Inputs:                Outputs:
Interface contract (how it connects to others?):
Decision: Ready / Buy / Reuse / Build
Source or effort estimate:
Dependencies (depends on / depended on by):
Owner:                 Due:
Definition of Done:
Element-specific risks:
```

Without a clear interface contract, assembly will fail — this is the single most important card in the workflow.

Stage 5 — Assembly & Readiness
