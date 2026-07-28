### Bug fix

**Reproduce first. Evidence before design. Fix only what the evidence names.**

1. Read Principles in full.
2. Reproduce on the matching surface yourself. Capture the failing signal (log, assert, screenshot, return code) before any fix.
3. Map the surface with parallel `explore` subagents only after you have a repro: likely owners, related tests, recent touch points. Paths + short findings only.
4. Plan the fix. If the root cause is obvious from the repro, one plan is enough (`skip: single-plan — cause confirmed by runtime evidence`). Otherwise race two plans on `claude-opus-5-thinking-high-fast` and `gpt-5.6-sol-max`.
5. Audit the plan with `plan-auditor` when the fix spans more than two files or touches a public API. Otherwise `n/a: scoped local fix`.
6. Implement. Prefer a failing repro commit or staged check before the fix so history tells the story.
7. Verify on the same surface as step 2. Repro must no longer fire. Inconclusive is not a pass.

**Reply:** root cause with evidence, what changed, how you verified, principles applied with decisions.
