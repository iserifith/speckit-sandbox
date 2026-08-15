# Implementation Plan: Add farewell(name) companion to greet(name)

**Branch**: `spec/issue-1` | **Date**: 2026-08-15 | **Spec**: [spec.md](./spec.md)

**Input**: Feature specification from `/specs/001-add-farewell-function/spec.md`

**Note**: This template is filled in by the `$speckit-plan` command; its definition describes the execution workflow.

## Summary

Add a `farewell(name)` function alongside the existing `greet(name)` in
`src/greet.js`. It returns `"Goodbye, <name>!"` for any non-empty string and
throws `TypeError` (exact message `farewell(name) requires a non-empty string`)
for empty or non-string input. Test coverage is added in the existing
`test/greet.test.js` so `npm test` stays green. Technical approach: mirror the
existing `greet` implementation one-for-one — same validation idiom
(`if (!name || typeof name !== "string")`), same module (ESM, single named
export appended), same test runner (`node:test` + `node:assert/strict`). No
research unknowns remain; all decisions were settled in the spec's clarify
session (2026-08-15).

## Technical Context

**Language/Version**: JavaScript (ES modules) on Node.js — any version with
built-in `node:test` (Node >= 18); sandbox runs on the Node available in the
pipeline container.

**Primary Dependencies**: None (zero runtime and dev dependencies per
Constitution Principle III).

**Storage**: N/A — pure in-memory string formatting, no persistence.

**Testing**: Node's built-in test runner: `node --test test/*.test.js` via
`npm test`; assertions via `node:assert/strict`.

**Target Platform**: Cross-platform Node.js (sandbox CI / local dev); no
platform-specific APIs used.

**Project Type**: Library (toy single-module ESM package).

**Performance Goals**: N/A — trivial pure function; no performance
requirements beyond "instantaneous".

**Constraints**: No external dependencies (constitution); no network access
required; `npm test` must stay green at every commit; `greet` behaviour,
signature, and error semantics must remain unchanged (FR-006).

**Scale/Scope**: Two functions in one source file (`src/greet.js`), one test
file (`test/greet.test.js`). Single-issue, single-PR scope.

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

| Principle | Gate | Pre-design verdict |
|-----------|------|--------------------|
| I. Trivial By Design | Change must be implementable in a single sandboxed run — a handful of files, a handful of tests | PASS (pre) → PASS (post-design) — design touches 1 source file + 1 test file, ~10 lines of implementation; no new structure |
| II. Test-First | Every change adds/updates a test in `test/`; `npm test` MUST stay green | PASS (pre) → PASS (post-design) — contract cases C1–C7 are all executable `node:test` assertions in `test/greet.test.js`; quickstart Scenario 1 is the green gate; tasks phase will order tests before implementation |
| III. No External Dependencies | Node built-ins only (`node:test` + `assert`) | PASS (pre) → PASS (post-design) — design adds no dependencies, no lockfile changes, no install step (research D5) |

**Gate result (pre-Phase-0): PASS — no violations, no justifications needed.**

**Gate result (post-Phase-1): PASS — design artifacts (research.md, data-model.md, contracts/library-api.md, quickstart.md) introduce no new complexity and no principle violations.**

## Project Structure

### Documentation (this feature)

```text
specs/001-add-farewell-function/
├── plan.md              # This file ($speckit-plan command output)
├── research.md          # Phase 0 output ($speckit-plan command)
├── data-model.md        # Phase 1 output ($speckit-plan command)
├── quickstart.md        # Phase 1 output ($speckit-plan command)
├── contracts/           # Phase 1 output ($speckit-plan command)
│   └── library-api.md
└── tasks.md             # Phase 2 output ($speckit-tasks command - NOT created by $speckit-plan)
```

### Source Code (repository root)

```text
src/
└── greet.js          # Existing greet(name); farewell(name) is appended here

test/
└── greet.test.js     # Existing greet tests; farewell tests are added here

package.json          # Unchanged: "test": "node --test test/*.test.js"
```

**Structure Decision**: Single-project layout (the repository's existing
layout, unchanged). `farewell` is co-located with `greet` in `src/greet.js`
per the issue's "alongside" wording and the spec's clarify session; tests are
co-located in the existing `test/greet.test.js`. No new directories, no new
modules, no build step.

## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

No constitution violations — this section is intentionally empty.
