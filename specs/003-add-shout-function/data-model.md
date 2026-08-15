# Data Model: Add shout(name) that returns name in caps

**Date**: 2026-08-15 | **Branch**: `spec/issue-21` | **Spec**: [spec.md](spec.md)

This feature is a single pure function — there is no persisted state, no storage,
and no entity relationships. The "model" is the function's input/output contract.

## Entity: `shout` function

| Aspect | Value |
|--------|-------|
| Kind | Pure, synchronous function; named ESM export of `src/greet.js` |
| Signature | `shout(name: string): string` |
| Input | `name` — any value; only primitive strings are accepted |
| Output | New string equal to `name` with all cased characters upper-cased |
| Side effects | None — no I/O, no mutation, no module-level state |
| Error mode | Throws `TypeError` when `name` is not a primitive string |

## Validation rules (from spec requirements)

| Rule | Source | Behaviour |
|------|--------|-----------|
| Type guard | FR-003 | `typeof name !== "string"` → throw `TypeError("shout(name) requires a string")`. Covers `undefined`, `null`, numbers, booleans, objects, symbols, bigints. Only the error **type** is contractual; wording follows the `greet` convention. |
| No coercion | FR-003 | Non-string input never produces a return value (no `String(name)` fallback). |
| Empty string valid | FR-002 | `shout("")` returns `""` without throwing. The guard tests type only — no length/content checks (deliberate contrast with `greet`, which rejects empty strings). |
| No normalisation | FR-004 | No trimming, no length limits, no character filtering. Non-letter characters pass through verbatim and in order; whitespace-only strings returned unchanged. |
| Case mapping | FR-001, Assumptions | `String.prototype.toUpperCase()` — runtime-standard semantics, no locale arguments. Unicode letters map per default rules (`"café" → "CAFÉ"`, `"straße" → "STRASSE"`). |

## State transitions

N/A — stateless function. Each invocation is independent.

## Neighbouring entity (unchanged): `greet` function

`greet(name)` in the same module is **not modified** by this feature (FR-006): its
signature, non-empty-string validation, error type/message, and existing tests
remain intact. `shout` is additive only.
