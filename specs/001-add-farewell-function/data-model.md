# Data Model: Add farewell(name) companion to greet(name)

**Date**: 2026-08-15 | **Feature**: `specs/001-add-farewell-function`

This feature is a pure function library with **no persisted data, no state,
and no I/O**. There are no database schemas, no files, and no entities with
lifecycles. The only "model" is the function's input/output contract, captured
below so `tasks.md` and the implementation phase have a single reference.

## Entities

### `farewell(name)` — pure function (new)

- **Module**: `src/greet.js` (named export, alongside `greet`)
- **Signature**: `farewell(name: string) -> string`
- **Parameters**:
  - `name` — required, non-empty string. Used verbatim (no trimming, no
    case-folding, no escaping).
- **Returns**: string of the exact form `"Goodbye, <name>!"`.
- **Throws**: `TypeError` with exact message
  `farewell(name) requires a non-empty string` when `name` is the empty
  string or any non-string value.
- **Side effects**: none. No module-level state, no mutation, no I/O.

### `greet(name)` — pure function (existing, unchanged)

- **Module**: `src/greet.js` (existing named export)
- **Invariant (FR-006)**: behaviour, signature, and error semantics MUST NOT
  change as a side effect of this feature.

## Validation rules (from spec requirements)

| Rule | Source | Behaviour |
|------|--------|-----------|
| V1: empty string rejected | FR-002 | `farewell("")` throws `TypeError` |
| V2: non-string rejected | FR-003 | `farewell(undefined/null/42/{}/true/Symbol()/1n)` throws `TypeError` |
| V3: exact error message | FR-004 | message === `farewell(name) requires a non-empty string` |
| V4: whitespace-only accepted | Clarify 2026-08-15 / spec edge case | `farewell("   ")` returns `"Goodbye,    !"` |
| V5: no length limit | spec edge case | any length name returns the formatted string |
| V6: verbatim interpolation | FR-001 / AS 1.2 | names with commas/space/casing pass through unchanged |

## State transitions

None — the function is stateless and deterministic: same input always yields
the same output or the same thrown error (SC-001, SC-002).
