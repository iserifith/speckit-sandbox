# Quickstart: Validate Add shout(name) that returns name in caps

**Date**: 2026-08-15 | **Branch**: `spec/issue-21` | **Spec**: [spec.md](spec.md)

Runnable validation scenarios proving the feature works end-to-end. See
[contracts/library-api.md](contracts/library-api.md) for the full behavioural
contract and [data-model.md](data-model.md) for validation rules — not duplicated
here.

## Prerequisites

- Node.js 18+ (provides the built-in `node:test` runner; no npm install needed —
  the project has zero dependencies).
- Repo checked out on branch `spec/issue-21`.

## Setup

```bash
cd /workspace/repo
node --version   # expect v18.x or newer
```

No `npm install` step exists or is required (constitution principle III:
No External Dependencies).

## Scenario 1 — Acceptance criteria via the test suite (primary)

```bash
npm test
```

**Expected outcome**: exit status 0. Output shows the existing `greet` tests
passing unchanged plus a new `shout` block whose tests assert the three issue
acceptance criteria:

1. `shout("alice") === "ALICE"` (plus already-uppercase and mixed-content cases)
2. `shout("") === ""` (no throw)
3. `shout(undefined | null | 42 | {} | true | Symbol() | 10n)` throws `TypeError`

## Scenario 2 — Manual smoke check

```bash
node --input-type=module -e '
import { shout, greet } from "./src/greet.js";
console.log(shout("alice"));   // ALICE
console.log(shout(""));        // (empty line)
console.log(shout("café 42!")); // CAFÉ 42!
console.log(greet("alice"));   // Hello, alice! — unchanged neighbour
try { shout(42); } catch (e) {
  console.log(e instanceof TypeError, e.message); // true shout(name) requires a string
}
'
```

**Expected outcome**: output matches the inline comments exactly; the `TypeError`
line prints `true` for the instanceof check.

## Scenario 3 — Regression guard for `greet`

Covered automatically by Scenario 1 (the pre-existing `greet` tests run in the
same suite). Any change to `greet`'s signature, behaviour, or error semantics
fails the suite — per FR-006 this must not happen.

## Failure triage

| Symptom | Likely cause |
|---------|--------------|
| `shout("")` throws | Guard copied `greet`'s `!name ||` falsiness check — see research.md Decision 3 |
| Number input returns `"42"` | Missing type guard / accidental coercion — violates contract C7 |
| `npm test` fails on `greet` tests | `greet` was modified — out of scope, revert |
| `node --test` finds no tests | Not run from repo root, or test glob moved — run `npm test` from repo root |
