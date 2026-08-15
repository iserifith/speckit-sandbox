# Feature Specification: Add shout(name) that returns name in caps

**Feature Branch**: `spec/issue-21`

**Created**: 2026-08-15

**Status**: Draft

**Input**: User description: "A tiny utility for greeting messages. Add a function shout(name: str) -> str that returns the name in all caps. Acceptance criteria: shout(\"alice\") returns \"ALICE\"; shout(\"\") returns \"\"; Non-string input raises TypeError."

**Issue**: #21 — Add shout(name) that returns name in caps

## Clarifications

### Session 2026-08-15

- Q: Should `shout` be a named export alongside `greet` or a default export? → A: Named export alongside `greet` in the same module (matches repo precedent; assumed since no human available).
- Q: What is the exact `TypeError` message wording? → A: Mirror `greet`'s convention, i.e. `shout(name) requires a string` (message wording is non-contractual; assumed since no human available).
- Q: Should `shout` live in `src/greet.js` or its own module? → A: Co-locate in `src/greet.js` alongside `greet`/`farewell` precedent (assumed since no human available).
- Q: Are whitespace-only strings passed through unchanged like the empty string? → A: Yes — only the type is validated; no length or content checks (explicitly contrasted with `greet`, which rejects empty strings).

No human was available to answer clarification questions; all answers are autonomous best-supported choices, documented here and in Assumptions.

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Produce an all-caps version of a name (Priority: P1)

As a developer using the sandbox library, I want to call `shout("alice")` and receive `"ALICE"` so I can compose emphatic greeting messages (e.g. combining with `greet`/`farewell` style utilities) without hand-rolling case conversion.

**Why this priority**: This is the headline behaviour of the issue and its first acceptance criterion. Without the happy-path transformation there is nothing to ship.

**Independent Test**: Can be fully tested by importing `shout`, calling it with the string `"alice"`, and asserting the returned value equals `"ALICE"`. Delivers a standalone, usable string-transformation utility.

**Acceptance Scenarios**:

1. **Given** a lowercase or mixed-case string name (e.g. `"alice"`, `"AlIcE"`), **When** the caller invokes `shout(name)`, **Then** the function returns the same string with every cased character converted to upper case (e.g. `"ALICE"`).
2. **Given** a string that is already fully upper case (e.g. `"BOB"`), **When** the caller invokes `shout(name)`, **Then** the function returns the string unchanged (`"BOB"`).
3. **Given** a string containing non-letter characters (digits, punctuation, whitespace, e.g. `"alice 42!"`), **When** the caller invokes `shout(name)`, **Then** the function returns the string with letters upper-cased and non-letter characters preserved verbatim.

### User Story 2 - Pass the empty string through unchanged (Priority: P1)

As a developer using the sandbox library, I want `shout("")` to return `""` so that empty input is treated as a valid, pass-through value rather than an error — matching the issue's second acceptance criterion.

**Why this priority**: Same priority as the happy path — the issue explicitly specifies empty-string pass-through, which is a deliberate contrast with the sibling `greet`/`farewell` functions that reject empty strings. Getting this wrong would silently invert the documented contract.

**Independent Test**: Can be fully tested by calling `shout("")` and asserting the returned value is exactly `""` (a string, length 0, no error thrown). Delivers the documented empty-input behaviour.

**Acceptance Scenarios**:

1. **Given** the empty string `""`, **When** the caller invokes `shout("")`, **Then** the function returns the empty string `""` and does not throw.

### User Story 3 - Reject non-string input with TypeError (Priority: P1)

As a developer using the sandbox library, I want `shout` to fail loudly on non-string input so misuse is caught at the call site instead of producing silent coercion bugs like `"UNDEFINED"` or `"42"`.

**Why this priority**: Same priority as the happy path — the issue's third acceptance criterion mandates a `TypeError` on non-string input, and the sibling utilities in this repo enforce the same guarantee.

**Independent Test**: Can be fully tested by asserting `shout` throws an instance of `TypeError` (not a generic `Error`) for each of: `shout(undefined)`, `shout(null)`, `shout(42)`, `shout({})`, `shout(true)`. Delivers the documented input-validation contract.

**Acceptance Scenarios**:

1. **Given** a non-string value (e.g. `undefined`, `null`, a number, an object, a boolean), **When** the caller invokes `shout(value)`, **Then** the function throws a `TypeError` — it does not coerce to string, does not return a value, and does not throw a different error type.
2. **Given** a `Symbol` or `BigInt` value, **When** the caller invokes `shout(value)`, **Then** the function throws a `TypeError`, consistent with the other non-string rejections.

### Edge Cases

- **Empty string**: Passed through as `""` (documented acceptance criterion, NOT an error — deliberate contrast with `greet`, whose contract rejects empty strings).
- **Whitespace-only strings** (e.g. `"   "`): Returned unchanged, since there are no cased characters to transform. No trimming is performed.
- **Unicode / non-ASCII letters** (e.g. `"café"`, `"straße"`): Upper-cased using the runtime's standard string upper-casing semantics (e.g. `"CAFÉ"`, `"STRASSE"`). No custom locale handling is required for this toy utility.
- **Very long strings**: No length limit. The function returns the transformed string regardless of length.
- **Symbol or BigInt inputs**: Treated as non-string and rejected with `TypeError`, matching the existing `greet` behaviour.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: System MUST expose a `shout(name)` function that, for any string `name`, returns a new string equal to `name` with all cased characters converted to upper case (e.g. `shout("alice") === "ALICE"`).
- **FR-002**: System MUST return the empty string `""` unchanged from `shout("")` without throwing.
- **FR-003**: System MUST throw a `TypeError` from `shout(name)` when `name` is not a string (e.g. `undefined`, `null`, numbers, objects, booleans, symbols, bigints); it MUST NOT coerce the value to a string. The error message SHOULD mirror the `greet` convention, e.g. `shout(name) requires a string` — only the error *type* is contractual, not the exact wording.
- **FR-004**: System MUST NOT modify, trim, or otherwise normalise the input beyond upper-casing — non-letter characters are preserved verbatim and in order. Whitespace-only strings are passed through unchanged; only the input *type* is validated, never its length or content.
- **FR-005**: System MUST add test coverage asserting the three documented acceptance criteria: `shout("alice") === "ALICE"`, `shout("") === ""`, and non-string inputs throwing `TypeError`.
- **FR-006**: System MUST keep the existing `greet(name)` function and its tests intact and passing — no changes to behaviour, signature, or error semantics of `greet`.
- **FR-007**: System MUST export `shout` as a named ESM export (not a default export), matching the existing `greet` export style so callers use `import { shout } from ...`.

### Key Entities *(include if feature involves data)*

- **`shout` function**: A pure, synchronous function. Single parameter `name` (string). Returns a transformed string or throws `TypeError`. No side effects, no I/O, no module-level state. Sibling/companion to the existing `greet` function in the sandbox library.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: A developer importing `shout` and calling it with `"alice"` receives exactly the string `"ALICE"` on 100% of invocations.
- **SC-002**: A developer calling `shout("")` receives exactly the empty string `""` on 100% of invocations, with zero errors thrown.
- **SC-003**: A developer calling `shout` with any non-string value observes a thrown `TypeError` on 100% of invocations (zero silent coercions, zero wrong-type errors).
- **SC-004**: Running `npm test` on a clean checkout exits with status 0 and reports zero failing tests, including the pre-existing `greet` tests and the new `shout` tests covering all three acceptance criteria.

## Assumptions

- **Autonomous decisions (no human available)**: During the clarify phase (session 2026-08-15) all open questions were resolved autonomously and recorded under **Clarifications**. Key decisions: `shout` is a named ESM export co-located with `greet` in `src/greet.js`; the `TypeError` message mirrors `greet`'s convention (`shout(name) requires a string`) but only the error *type* is contractual; whitespace-only strings pass through unchanged.
- **Empty string is valid input**: Unlike `greet` (which rejects empty strings), `shout` explicitly passes `""` through unchanged per the issue's acceptance criteria. Only the *type* of the input is validated, not its length.
- **Error message**: The exact `TypeError` message text is unspecified by the issue. Assumed to follow the existing repo convention, e.g. `shout(name) requires a string` — mirroring `greet`'s message style with the `shout` function name substituted. The precise wording is an implementation detail; only the error *type* is contractual.
- **Upper-casing semantics**: "All caps" is interpreted as the runtime's standard string upper-case operation (e.g. JavaScript `String.prototype.toUpperCase()`), with no locale-specific or custom case-mapping logic. This is a toy demo, not user-facing i18n.
- **Test framework**: The test suite continues to use Node's built-in `node:test` + `node:assert/strict`, per the constitution's "No External Dependencies" principle and the existing `package.json` test script.
- **Test file organisation**: New `shout` tests live in the existing `test/greet.test.js` file alongside the `greet` tests (matching the farewell precedent), keeping the suite as one obvious unit.
- **Single-issue, single-PR scope**: This change touches only the library source and its test file — no README rewrites, no CI changes, no dependency additions. Consistent with the constitution's "Trivial By Design" principle.
- **Pipeline branch**: The speckit pipeline for this issue uses branch `spec/issue-21` carrying phases `specify` → `clarify` → `plan` → `tasks` → `issues`. The same PR carries every phase.
