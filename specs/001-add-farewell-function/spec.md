# Feature Specification: Add farewell(name) companion to greet(name)

**Feature Branch**: `spec/issue-1`

**Created**: 2026-08-15

**Status**: Draft

**Input**: User description: "Add a `farewell(name)` function to `src/greet.js`, alongside the existing `greet(name)`. Same shape: returns a string, throws `TypeError` on an empty/non-string name."

**Issue**: #1 — Add farewell(name) companion to greet(name)

## Clarifications

### Session 2026-08-15

- Q: Should whitespace-only names like `"   "` be accepted or rejected? → A: Accepted as non-empty (no trimming); mirrors existing `greet` behaviour.
- Q: Should `farewell` live in `src/greet.js` or its own module? → A: Co-located in `src/greet.js` per the issue's "alongside" wording.
- Q: What exact TypeError message should `farewell` throw? → A: `farewell(name) requires a non-empty string`, mirroring `greet`'s message.
- Q: Where should the new `farewell` tests live? → A: In the existing `test/greet.test.js`, alongside the `greet` tests.
- Q: Is any error-path beyond empty string and non-string in scope? → A: No; empty string + non-string (including Symbol/BigInt) covers the contract.

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Produce a farewell string for a given name (Priority: P1)

As a developer using the sandbox library, I want to call `farewell("World")` and receive `"Goodbye, World!"` so I can demonstrate symmetric greet/farewell behaviour when exercising the pipeline.

**Why this priority**: This is the headline behaviour of the issue and the only acceptance criterion that exercises the happy path. Without it there is nothing to ship.

**Independent Test**: Can be fully tested by importing `farewell` from `src/greet.js`, calling it with the string `"World"`, and asserting the returned string equals `"Goodbye, World!"`. Delivers the new greeting/farewell pairing as a standalone, usable function.

**Acceptance Scenarios**:

1. **Given** a non-empty string name (e.g. `"World"`), **When** the caller invokes `farewell(name)`, **Then** the function returns a string of the exact form `"Goodbye, <name>!"` (no extra whitespace, no trailing punctuation beyond `!`).
2. **Given** a non-empty string name with surrounding whitespace or different casing (e.g. `"  alice  "`), **When** the caller invokes `farewell(name)`, **Then** the function returns `"Goodbye, <name>!"` using the name value as supplied (no trimming, no case-folding).

### User Story 2 - Reject empty / non-string names with TypeError (Priority: P1)

As a developer using the sandbox library, I want `farewell` to fail loudly on bad input (empty string or non-string) so misuse is caught at the call site rather than producing a silent "Goodbye, !" string.

**Why this priority**: Same priority as the happy path — the issue explicitly calls out `TypeError` on empty/non-string, and the existing `greet` already enforces this. Skipping it would produce a library with weaker guarantees than its sibling.

**Independent Test**: Can be fully tested by importing `farewell` and asserting it throws an instance of `TypeError` (not a generic `Error`) for each of: `farewell("")`, `farewell(undefined)`, `farewell(null)`, `farewell(42)`, `farewell({})`. Delivers the documented input-validation contract.

**Acceptance Scenarios**:

1. **Given** the empty string `""`, **When** the caller invokes `farewell("")`, **Then** the function throws a `TypeError` whose message identifies the `farewell(name)` function and the requirement for a non-empty string.
2. **Given** a non-string value (e.g. `undefined`, `null`, a number, an object), **When** the caller invokes `farewell(value)`, **Then** the function throws a `TypeError` (it does not coerce to string, does not return a value, does not throw a different error type).

### User Story 3 - Co-located test coverage alongside existing greet tests (Priority: P2)

As a reviewer of the sandbox library, I want `farewell` tests to live alongside the existing `greet` tests so the test suite reads as one obvious unit covering both companion functions.

**Why this priority**: Tests are mandatory under the constitution (Principle II: Test-First; `npm test` must stay green), but the *organisation* of tests is secondary to the behaviour. Placed at P2 so implementation is not blocked on test-file layout choices.

**Independent Test**: Can be fully tested by running `npm test` and observing that every new `farewell` acceptance scenario above is exercised by at least one assertion, and that all previously-passing `greet` tests still pass. Delivers a green, expanded test suite.

**Acceptance Scenarios**:

1. **Given** the test file `test/greet.test.js` (or its replacement), **When** `npm test` is run, **Then** every acceptance scenario from User Stories 1 and 2 has a corresponding assertion, and the previously-passing `greet` tests continue to pass.
2. **Given** the test suite, **When** `npm test` is run on a clean checkout, **Then** the run exits with status 0 and reports zero failures.

## Edge Cases

- **Whitespace-only names** (e.g. `"   "`): Treated as non-empty (the function does not trim). `farewell("   ")` returns `"Goodbye,    !"` — preserve the supplied value, matching the documented contract. (Documented assumption; the issue body does not require trimming.)
- **Names containing the comma/space separator** (e.g. `"Smith, Jr."`): Returned verbatim in the formatted string. No escaping or sanitisation is required; this is a toy demo, not user-facing UI.
- **Very long names**: No length limit. The function returns the formatted string regardless of name length.
- **Symbol or BigInt inputs**: Treated as non-string and rejected with `TypeError`, matching the existing `greet` behaviour.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: System MUST expose a `farewell(name)` function in `src/greet.js` (co-located with `greet`, per the issue's "alongside" wording — clarified 2026-08-15) that returns the string `"Goodbye, <name>!"` for any non-empty string `name`.
- **FR-002**: System MUST throw a `TypeError` from `farewell(name)` when `name` is the empty string `""`.
- **FR-003**: System MUST throw a `TypeError` from `farewell(name)` when `name` is not a string (e.g. `undefined`, `null`, numbers, objects, booleans, symbols).
- **FR-004**: The `TypeError` thrown by `farewell` MUST use the exact message `farewell(name) requires a non-empty string`, mirroring `greet`'s message style with the `farewell` function name substituted (clarified 2026-08-15).
- **FR-005**: System MUST add test coverage in the existing `test/greet.test.js` file (alongside the `greet` tests — clarified 2026-08-15) that asserts the happy path (`farewell("World") === "Goodbye, World!"`) and the rejection paths (`farewell("")` and `farewell(undefined)` each throw `TypeError`).
- **FR-006**: System MUST keep the existing `greet(name)` function and its tests intact and passing — no changes to behaviour, signature, or error semantics of `greet`.

### Key Entities *(include if feature involves data)*

- **`farewell` function**: A pure, synchronous function exported from `src/greet.js`. Single parameter `name` (string). Returns a formatted string or throws `TypeError`. No side effects, no I/O, no module-level state. Sibling/companion to the existing `greet` function.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: A developer importing `farewell` from `src/greet.js` and calling it with `"World"` receives exactly the string `"Goodbye, World!"` on 100% of invocations.
- **SC-002**: A developer calling `farewell("")` or `farewell(undefined)` observes a thrown `TypeError` on 100% of invocations (zero silent fallbacks, zero wrong-type errors).
- **SC-003**: Running `npm test` on a clean checkout exits with status 0 and reports zero failing tests, including the pre-existing `greet` tests and the new `farewell` tests.
- **SC-004**: The added test file or test cases cover all four documented acceptance scenarios (happy path with `"World"`, empty string rejection, undefined rejection, and the previously-existing greet behaviour remains intact).

## Assumptions

- **Module location** (decided in clarify 2026-08-15): `farewell` is added to the existing `src/greet.js` file (matching the issue body's "alongside the existing `greet(name)`" instruction) rather than split into a separate `src/farewell.js` module.
- **No trimming / no case-folding**: `farewell` treats the `name` argument as opaque — it does not call `.trim()` or normalise case. This matches the existing `greet` behaviour and avoids silent surprises for callers.
- **Test framework**: The test suite continues to use Node's built-in `node:test` + `node:assert/strict`, with tests placed in `test/*.test.js`, per the constitution's "no external dependencies" principle and the existing `package.json` test script.
- **Test file organisation** (decided in clarify 2026-08-15): New `farewell` tests live in the existing `test/greet.test.js` file alongside the `greet` tests, keeping the suite as one obvious unit.
- **Single-issue, single-PR scope**: This change touches only `src/greet.js` and the test file(s) — no README rewrites, no CI changes, no dependency additions. Consistent with the constitution's "Trivial By Design" principle.
- **Pipeline branch**: The speckit pipeline for this issue uses branch `spec/issue-1` (already created) carrying phases `specify` → `clarify` → `plan` → `tasks` → `issues` → `implement`. The same PR carries every phase.