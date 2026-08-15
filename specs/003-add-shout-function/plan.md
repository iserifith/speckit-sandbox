# Implementation Plan: Add shout(name) that returns name in caps

**Branch**: `spec/issue-21` | **Date**: 2026-08-15 | **Spec**: [spec.md](spec.md)

**Input**: Feature specification from `/specs/003-add-shout-function/spec.md` (issue #21)

## Summary

Add a pure, synchronous `shout(name)` function to the existing sandbox library that
returns the input string upper-cased, passes `""` through unchanged, and throws
`TypeError` on non-string input. Technical approach: co-locate `shout` as a named
ESM export in the existing `src/greet.js` module (repo precedent), implement via
`typeof` type-guard plus `String.prototype.toUpperCase()`, and add coverage in the
existing `test/greet.test.js` file using Node's built-in `node:test` runner. No new
dependencies, no CI changes, no README rewrites.

## Technical Context

**Language/Version**: JavaScript (ESM, `"type": "module"`), Node.js 18+ (built-in `node:test` runner requires >= 18)

**Primary Dependencies**: None — zero runtime/dev dependencies per constitution principle III

**Storage**: N/A

**Testing**: Node built-in `node:test` + `node:assert/strict`, invoked via `npm test` (`node --test test/*.test.js`)

**Target Platform**: Any Node.js runtime (library module, platform-agnostic)

**Project Type**: library (single trivial npm package, private)

**Performance Goals**: N/A — trivial pure string transformation; no latency/throughput targets

**Constraints**: No external dependencies; `npm test` must stay green; `greet` behaviour must remain untouched (FR-006)

**Scale/Scope**: One function (~4 lines) added to one source file, plus one test block added to one existing test file

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

| Principle | Gate | Status |
|-----------|------|--------|
| I. Trivial By Design | Proposal implementable in a single sandboxed run, handful of files/tests | PASS (initial + post-design re-check) — 1 function, 1 source file, 1 test file |
| II. Test-First | Every change adds/updates a test in `test/`; `npm test` stays green | PASS (initial + post-design re-check) — contracts/library-api.md maps every spec criterion to a test; quickstart Scenario 1 is `npm test` staying green |
| III. No External Dependencies | Only Node built-ins (`node:test`, `assert`) | PASS (initial + post-design re-check) — research.md Decision 4 selected built-ins only; no package.json changes |

Post-design re-evaluation (2026-08-15): Phase 0 (research.md) resolved all
unknowns with zero new dependencies; Phase 1 artifacts (data-model.md,
contracts/library-api.md, quickstart.md) introduce no new files outside
`specs/`, no dependencies, and keep tests in the existing suite. All gates
remain green. No violations → Complexity Tracking section intentionally left
empty.

## Project Structure

### Documentation (this feature)

```text
specs/003-add-shout-function/
├── plan.md              # This file ($speckit-plan command output)
├── research.md          # Phase 0 output ($speckit-plan command)
├── data-model.md        # Phase 1 output ($speckit-plan command)
├── quickstart.md        # Phase 1 output ($speckit-plan command)
├── contracts/           # Phase 1 output ($speckit-plan command)
│   └── library-api.md
├── checklists/
│   └── requirements.md  # Pre-existing (specify/clarify phases)
├── spec.md              # Pre-existing (specify/clarify phases)
└── tasks.md             # Phase 2 output ($speckit-tasks command - NOT created by $speckit-plan)
```

### Source Code (repository root)

```text
src/
└── greet.js             # Existing module; `shout` added here as named export alongside `greet`

test/
└── greet.test.js        # Existing test file; `shout` test block added alongside `greet` tests
```

**Structure Decision**: Single trivial npm package (Option 1, collapsed). The spec's
clarifications already resolved module location: `shout` is co-located in
`src/greet.js` with `greet`, and its tests live in `test/greet.test.js`. No new
files or directories are created in source; only documentation artifacts under
`specs/003-add-shout-function/`.

## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

No constitution violations — nothing to justify.
