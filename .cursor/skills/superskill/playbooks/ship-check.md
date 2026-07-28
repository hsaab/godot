### Ship check

**Runs after building something new, before final commits / PR. Three gates in parallel as subagents. You triage; you do not auto-fix or churn.**

1. Ensure the diff is complete first (implementation + docs + tests written).
2. Launch all three in parallel, in one message:
   - **Bugbot** — one `bugbot` subagent, description exactly `Bugbot`, prompt:
     `Full Repository Path: <repo root>` newline `Diff: uncommitted changes` (use `branch changes` when the work is committed on a branch). Do not compute the diff yourself.
   - **Security review** — one `security-review` subagent, description exactly `Security Review`, same prompt shape (`Diff:` one of `branch changes` / `uncommitted changes`).
   - **Smoke check** — one `shell` subagent: build if sources changed, then run the Test command from Repo bindings plus any repo verify script. Return pass/fail and the single decisive output line, not the full log.
3. Triage review findings skeptically. Both reviewers catch real bugs and also file nitpicks; assess each on its merits. Fix real bugs (fixes re-enter the change playbook's verify step), dismiss noise with a concrete reason. Never churn code to satisfy a non-issue.
4. Gate: smoke check must pass. High-severity findings block until fixed or explicitly waived by the user (`skip: <reason>` stays in the todolist).

**Reply:** one line per gate (Bugbot: N findings · Security: N findings · Smoke: pass/fail), then a table of findings kept vs dismissed with reasons.
