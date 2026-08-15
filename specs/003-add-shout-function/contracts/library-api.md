# Contract: Library API — `shout`

**Date**: 2026-08-15 | **Feature**: specs/003-add-shout-function | **Module**: `src/greet.js`

The project is a library, so its external interface is its public module API.
This is the contract implementation must satisfy and tests must verify.

## Export

```js
// src/greet.js
export function shout(name) { /* ... */ }
```

- **Export kind**: Named ESM export, alongside the existing `greet` named export.
  No default export is added or changed.
- **Import surface**: `import { shout } from "<path>/src/greet.js";`

## Signature

`shout(name: string): string`

## Behavioural contract

| # | Input | Guaranteed behaviour |
|---|-------|----------------------|
| C1 | `"alice"` (any lowercase/mixed-case string) | Returns `"ALICE"` — every cased character upper-cased via runtime-standard semantics; result is a **new** string |
| C2 | `"BOB"` (already upper case) | Returns `"BOB"` unchanged |
| C3 | `"alice 42!"` (digits/punctuation/whitespace) | Letters upper-cased; non-letter characters preserved verbatim and in order |
| C4 | `""` (empty string) | Returns `""`; does **not** throw |
| C5 | `"   "` (whitespace-only) | Returned unchanged; no trimming |
| C6 | `"café"`, `"straße"` (non-ASCII) | Default `toUpperCase()` Unicode semantics (`"CAFÉ"`, `"STRASSE"`); no locale-specific handling |
| C7 | `undefined`, `null`, `42`, `{}`, `true`, `Symbol()`, `10n` | Throws `TypeError` — never coerces, never returns, never throws a different error type |

## Error contract

- **Type**: `TypeError` exactly (instanceof check passes). Contractual.
- **Message**: `"shout(name) requires a string"` — follows the `greet`
  convention. **Non-contractual**: tests must assert the error type, not the
  exact message wording.

## Non-contract (explicitly out of scope)

- No changes to `greet`'s contract (FR-006).
- No locale-aware casing, no trimming, no length limits, no content validation.
- No async behaviour, no callbacks, no options parameter.
