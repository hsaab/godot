### Change

**You own the design. Map, race plans, audit, then implement. Delegate code; review the diff yourself.**

1. Read Principles in full (todolist item 1 from the router).
2. Map the surface with parallel `explore` subagents: where the change lands, which existing thing to mirror, where tests and docs live. Collect paths and short findings only.
3. Race two plans via `generalPurpose` on `claude-opus-5-thinking-high-fast` and `gpt-5.6-sol-max-fast` with the same brief (paths from step 2 + success criteria). Compare in a table; pick or merge. Divergence is the signal.
4. Audit the winning plan with `plan-auditor` on `cursor-grok-4.5-fast`. Implementation is blocked until clean. Blocking findings return to step 3 — do not patch them away in the parent.
5. Delegate implementation to a `generalPurpose` subagent on `cursor-grok-4.5-fast` with named file-path scope and success criteria. Review its diff yourself (review separation; no skip escape).
6. Docs and tests are steps, not afterthoughts — include them in the same wave when the API surface changes.
7. Verify on the matching surface (build + tests + a binding or runtime check). Inconclusive is not a pass.
8. Ship check: run [ship-check.md](ship-check.md) — Bugbot + Security Review + smoke check as parallel subagents. Triage findings; fixes re-enter step 7.
9. Small ordered commits. Each unit ends in a check before the next.

**Reply:** what you built, which plan won and why, ship-check gate results, principles applied with the decisions they changed, open decisions.
