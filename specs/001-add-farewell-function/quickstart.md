# Quickstart: Validate the farewell(name) feature

**Date**: 2026-08-15 | **Feature**: `specs/001-add-farewell-function`

Runnable validation scenarios proving the feature works end-to-end. Uses only
the repository's real commands — no new tooling. Behavioural details live in
[contracts/library-api.md](./contracts/library-api.md) and
[data-model.md](./data-model.md); this guide does not repeat implementation
code.

## Prerequisites

- Node.js >= 18 (provides the built-in `node:test` runner).
- A clean checkout of branch `spec/issue-1` with the implementation applied
  (during the plan phase only the spec artifacts exist; run this after the
  implement phase, or after writing the implementation manually).
- No `npm install` needed — the project has zero dependencies.

## Setup

```bash
git clone https://github.com/iserifith/speckit-sandbox.git
cd speckit-sandbox
git checkout spec/issue-1
node --version   # expect v18+ ; no install step required
```

## Scenario 1 — Automated test suite (primary gate)

```bash
npm test
```

**Expected outcome**: exit status 0, zero failures. The output lists the
pre-existing `greet` tests (still passing — FR-006) plus new `farewell` tests
covering every contract case C1–C7 (FR-005, SC-003, SC-004).

## Scenario 2 — Happy-path smoke check

```bash
node -e 'import("./src/greet.js").then(({ farewell }) => {
  const out = farewell("World");
  if (out !== "Goodbye, World!") { console.error("FAIL:", out); process.exit(1); }
  console.log("OK:", out);
})'
```

**Expected outcome**: prints `OK: Goodbye, World!` and exits 0 (C1, SC-001).

## Scenario 3 — Error-path smoke check

```bash
node -e 'import("./src/greet.js").then(({ farewell }) => {
  for (const bad of ["", undefined, null, 42, {}]) {
    try { farewell(bad); console.error("FAIL: no throw for", bad); process.exit(1); }
    catch (e) {
      if (!(e instanceof TypeError)) { console.error("FAIL: wrong error type"); process.exit(1); }
      if (e.message !== "farewell(name) requires a non-empty string") { console.error("FAIL: wrong message:", e.message); process.exit(1); }
    }
  }
  console.log("OK: all error paths throw TypeError with the exact message");
})'
```

**Expected outcome**: prints the OK line and exits 0 (C3–C5, FR-002/003/004,
SC-002).

## Scenario 4 — Greet regression check

```bash
node -e 'import("./src/greet.js").then(({ greet }) => {
  if (greet("World") !== "Hello, World!") { console.error("FAIL: greet changed"); process.exit(1); }
  console.log("OK: greet unchanged");
})'
```

**Expected outcome**: prints the OK line and exits 0 (FR-006).

## Failure handling

Any `FAIL:` line or non-zero exit means the implementation deviates from the
contract — do not proceed to PR merge; fix `src/greet.js` or
`test/greet.test.js` against [contracts/library-api.md](./contracts/library-api.md)
and re-run Scenario 1.
