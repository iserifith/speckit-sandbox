# Research: Add farewell(name) companion to greet(name)

**Date**: 2026-08-15 | **Feature**: `specs/001-add-farewell-function`

## Scope

The Technical Context section of `plan.md` contains **zero** NEEDS
CLARIFICATION markers: every decision was either settled in the spec's clarify
session (2026-08-15) or is directly observable in the repository. This
document records the evidence for each decision so later phases
(tasks/implement) do not re-open them.

## Decisions

### D1: Module placement — co-locate `farewell` in `src/greet.js`

- **Decision**: Append `farewell(name)` as a second named export in the
  existing `src/greet.js`; do not create `src/farewell.js`.
- **Rationale**: The issue body says "alongside the existing `greet(name)`",
  and the clarify session (2026-08-15) locked this. The file is 6 lines;
  splitting a one-function module in a toy repo adds ceremony with no payoff.
- **Alternatives considered**: Separate `src/farewell.js` module — rejected as
  needless structure for a two-function library (Constitution I: Trivial By
  Design).

### D2: Validation idiom — mirror `greet` exactly

- **Decision**: Use the identical guard
  `if (!name || typeof name !== "string") { throw new TypeError("farewell(name) requires a non-empty string"); }`.
- **Rationale**: FR-002/FR-003/FR-004 require `TypeError` on empty string and
  on non-string input with an exact message. The existing `greet` guard
  already satisfies this exact contract (verified by reading
  `src/greet.js:2-4`): `!name` catches `""`, `undefined`, `null`; the
  `typeof` check catches numbers, objects, booleans, Symbols, BigInts.
  Mirroring keeps the two companion functions behaviourally symmetric, which
  is the point of the issue.
- **Alternatives considered**: Stricter validation (trim whitespace, length
  caps) — rejected: clarify session decided whitespace-only names are
  accepted as non-empty, no trimming; edge cases in `spec.md` confirm.
  Weaker/different error type — rejected: issue acceptance requires
  `TypeError` specifically.

### D3: Output format — template literal, no normalisation

- **Decision**: Return `` `Goodbye, ${name}!` `` — the name interpolated
  verbatim, no `.trim()`, no case-folding, no escaping.
- **Rationale**: FR-001 and Acceptance Scenario 1.2 require the supplied value
  to be used as-is (`"  alice  "` → `"Goodbye,   alice  !"`). Matches
  `greet`'s `` `Hello, ${name}!` `` shape.
- **Alternatives considered**: Sanitising/escaping names containing commas —
  rejected (spec edge case: "toy demo, not user-facing UI").

### D4: Test strategy — extend `test/greet.test.js` with node:test

- **Decision**: Add `farewell` tests to the existing `test/greet.test.js`,
  importing `farewell` alongside `greet`, using `node:test` +
  `node:assert/strict`. Cover: happy path (`"World"` → `"Goodbye, World!"`),
  empty-string rejection, `undefined` rejection, plus the additional
  non-string cases listed in the spec's Independent Test for US2 (`null`,
  `42`, `{}`) and the exact error message (FR-004).
- **Rationale**: Clarify session (2026-08-15) decided test-file placement;
  Constitution III forbids external test frameworks; `package.json` already
  wires `npm test` → `node --test test/*.test.js`, so no script changes.
- **Alternatives considered**: New `test/farewell.test.js` — rejected per the
  clarify decision to keep the suite as one obvious unit (US3).

### D5: Runtime/toolchain — existing Node, ESM, no build step

- **Decision**: Keep `"type": "module"`, plain `.js` files, no transpiler, no
  lockfile changes, no dependency installs.
- **Rationale**: Constitution III (no external dependencies) and the existing
  `package.json`; `node --test` requires only Node >= 18, already the de
  facto runtime in the sandbox.
- **Alternatives considered**: None — any toolchain addition would violate the
  constitution.

## Outstanding unknowns

None. All NEEDS CLARIFICATION items are resolved; the plan gate is clear to
proceed to Phase 1 design artifacts.
