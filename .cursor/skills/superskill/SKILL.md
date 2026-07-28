---
name: superskill
description: Routes nontrivial work in a large unfamiliar codebase. Maps the change surface with parallel explore subagents, races competing implementation plans across top-tier models, audits the winning plan against the source before any code is written, then verifies on the real artifact. Use for /superskill, or when adding a feature, chasing a defect, or answering how a subsystem works in a big or unfamiliar repo.
disable-model-invocation: true
---

# Superskill

Router, not a persona. Match the task to a playbook, copy that playbook's steps into the todo list verbatim, then reason about the task. Detail loads only when matched.

## Run loop

1. Open a todolist. First item: read the **Principles** section below in full.
2. Match one playbook. Open its file. Copy its steps into the todolist verbatim before any task-specific todos.
3. Execute the playbook. Route to the subagent roster as the steps fire.
4. A step you choose not to do stays in the list as `skip: <reason>` or `n/a: <reason>`. Silent omission is not allowed.
5. End on the playbook's terminal verification. "It compiles" and "inconclusive" are not a pass.

## Playbooks

| Match | File |
|---|---|
| New or changed behavior / feature / API | [playbooks/change.md](playbooks/change.md) |
| Reported defect to reproduce and fix | [playbooks/bug-fix.md](playbooks/bug-fix.md) |
| Read-only question: how / why / are we sure | [playbooks/investigation.md](playbooks/investigation.md) |
| Just built something: review + smoke gate | [playbooks/ship-check.md](playbooks/ship-check.md) |

No match: stay on `change.md` and note why in the todolist. `ship-check.md` also runs automatically as the last step of `change.md`.

## Subagent roster

| Role | Type | Model / notes |
|---|---|---|
| Map the surface | `explore` (parallel, one question each) | Parent model OK; return paths + short findings, never pasted source |
| Plan race | `generalPurpose` ×2 | `claude-opus-5-thinking-high-fast` and `gpt-5.6-sol-max` (Zynga-approved; no Fable/Grok) |
| Plan audit | `plan-auditor` | `cursor-grok-4.5-fast`; blocks implementation until clean |
| Implementation | `generalPurpose` | `cursor-grok-4.5-fast`; named file-path scope; lead reviews the diff |
| Ship check | `bugbot` + `security-review` + `shell` | In parallel; per [playbooks/ship-check.md](playbooks/ship-check.md) |

## Principles

Read any principle you apply. In the reply, name each one and the decision it changed. A citation with no decision does not count.

- **smallest-scoped-diff** — Bias to the smallest change that solves the problem. No drive-by refactors.
- **follow-the-neighborhood** — Mirror the existing family (neighboring files, style, binding pattern) before inventing a subsystem.
- **prove-it-works** — Verify against the real artifact on the matching surface, not a proxy.
- **fix-root-causes** — Reproduce first. Trace each symptom to its root. Ask why until you reach it.
- **guard-the-context-window** — Route bulk reads to subagents. Keep summaries in the main thread.
- **sequence-verifiable-units** — Break work into small units that each end in a check. Verify before the next.

## Escape hatches

- `skip: <reason>` — step applies, you chose not to run it.
- `n/a: <reason>` — step does not apply to this task.
Both stay visible in the todolist.

## Repo bindings (edit when porting)

- Build: `scons -j14 target=editor tests=yes vulkan=no accesskit=no angle=no`
- Test: `./bin/godot.macos.editor.arm64 --headless --test`
- Conventions: `.cursor/rules/godot-cpp.mdc`
