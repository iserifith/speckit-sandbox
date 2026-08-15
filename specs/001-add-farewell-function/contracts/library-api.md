# Contract: Library API — `farewell(name)`

**Date**: 2026-08-15 | **Feature**: `specs/001-add-farewell-function`

The project is a library, so its external interface is its public JavaScript
API. This contract is the implementable definition of the new export. It
mirrors the existing `greet` contract shape for symmetry.

## Export

```text
Module:  src/greet.js  (ES module; package "type": "module")
Export:  export function farewell(name)
```

## Signature

```js
farewell(name: string): string
```

## Behaviour

### Happy path

- **Precondition**: `typeof name === "string"` and `name.length > 0`.
- **Postcondition**: returns exactly `"Goodbye, " + name + "!"` —
  e.g. `farewell("World") === "Goodbye, World!"`.
- The `name` value is interpolated verbatim: no trimming, no case-folding,
  no escaping, no length limit.

### Error path

- **Trigger**: `name` is `""` (empty string) OR `typeof name !== "string"`
  (covers `undefined`, `null`, numbers, booleans, objects, arrays, symbols,
  bigints, functions).
- **Behaviour**: throws `TypeError` (the built-in `TypeError` class — not a
  subclass, not a generic `Error`).
- **Message**: exactly `farewell(name) requires a non-empty string`.
- The function never coerces, never returns a fallback value, and never
  throws a different error type.

## Contract test cases (traceable to spec)

| # | Input | Expected | Traces to |
|---|-------|----------|-----------|
| C1 | `"World"` | returns `"Goodbye, World!"` | FR-001, SC-001, issue acceptance |
| C2 | `"  alice  "` | returns `"Goodbye,   alice  !"` (verbatim) | AS 1.2, FR-001 |
| C3 | `""` | throws `TypeError`, exact message | FR-002, FR-004, SC-002, issue acceptance |
| C4 | `undefined` | throws `TypeError` | FR-003, SC-002, issue acceptance |
| C5 | `null` / `42` / `{}` | throws `TypeError` | FR-003, US2 independent test |
| C6 | `Symbol()` / `1n` | throws `TypeError` | FR-003, spec edge case |
| C7 | `"   "` (whitespace-only) | returns `"Goodbye,    !"` | clarify 2026-08-15, V4 |

## Stability contract for `greet`

The pre-existing export `greet(name)` in the same module is part of this
contract surface by adjacency: its signature, return format
(`"Hello, <name>!"`), and `TypeError` semantics MUST remain byte-for-byte
identical after this feature lands (FR-006). The existing tests in
`test/greet.test.js` are the executable guard.
