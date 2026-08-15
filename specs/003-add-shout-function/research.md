# Research: Add shout(name) that returns name in caps

**Date**: 2026-08-15 | **Branch**: `spec/issue-21` | **Spec**: [spec.md](spec.md)

Phase 0 research for the plan phase. The Technical Context in plan.md contained
**zero NEEDS CLARIFICATION markers** — every decision below was already resolved
by the spec's Clarifications section (session 2026-08-15) or by direct inspection
of the repo. This document records those decisions in the required
Decision / Rationale / Alternatives format.

## Decision 1: Module location and export style

- **Decision**: `shout` is implemented in the existing `src/greet.js` as a named
  ESM export (`export function shout(name) {...}`), imported by callers as
  `import { shout } from "../src/greet.js"`.
- **Rationale**: Resolved during clarify phase. Matches the repo's only precedent —
  `greet` is a named export in that same module — and the spec's FR-007 mandates a
  named ESM export matching `greet`'s style.
- **Alternatives considered**: (a) New module `src/shout.js` — rejected: adds a
  file for a 4-line function in a constitutionally "Trivial By Design" repo, and
  contradicts the clarify-phase decision. (b) Default export — rejected: breaks
  symmetry with `greet` and FR-007.

## Decision 2: Upper-casing semantics

- **Decision**: Use `String.prototype.toUpperCase()` with no locale arguments.
- **Rationale**: The issue's contract is "name in all caps" with example
  `shout("alice") === "ALICE"`. The runtime's standard upper-casing handles ASCII
  and common Unicode (`"café" → "CAFÉ"`, `"straße" → "STRASSE"`) with zero code.
  Spec assumption: toy demo, no i18n requirement.
- **Alternatives considered**: (a) `toLocaleUpperCase()` with a fixed locale —
  rejected: introduces locale-dependence (e.g. Turkish `i` → `İ`) into a toy
  utility with no i18n requirement; non-deterministic across environments.
  (b) Hand-rolled ASCII-only case mapping — rejected: reinvents a built-in,
  violates the spirit of "Trivial By Design".

## Decision 3: Type validation and error semantics

- **Decision**: Guard with `typeof name !== "string"` and throw
  `new TypeError("shout(name) requires a string")`. No empty-string check, no
  content checks.
- **Rationale**: Spec FR-003 mandates `TypeError` (not generic `Error`) for
  non-string input with no coercion; clarify phase fixed the message wording to
  mirror `greet`'s convention while noting only the error *type* is contractual.
  Deliberate contrast with `greet`, which rejects empty strings: `shout("")`
  MUST return `""` (spec FR-002), so the guard must test type only — note
  `greet`'s guard `!name || typeof name !== "string"` would be wrong here because
  `!""` is truthy; the falsiness check must be dropped.
- **Alternatives considered**: (a) Copy `greet`'s `!name || ...` guard verbatim —
  rejected: would throw on `""`, directly violating acceptance criterion 2.
  (b) `instanceof String` to also accept String objects — rejected: spec says
  non-string input throws; boxed `new String("x")` is not a primitive string and
  accepting it adds complexity with no requirement.

## Decision 4: Test framework and file organisation

- **Decision**: Tests use Node's built-in `node:test` (`describe`/`it`) with
  `node:assert/strict`, added as a new `describe("shout")` block inside the
  existing `test/greet.test.js`.
- **Rationale**: Constitution principle III (No External Dependencies) and
  principle II (Test-First); existing `package.json` test script
  (`node --test test/*.test.js`) already picks the file up. Spec assumption names
  `test/greet.test.js` as the location, matching the module co-location decision.
- **Alternatives considered**: (a) New `test/shout.test.js` — rejected: spec
  assumption prefers the existing file; either would be picked up by the glob,
  but one suite file keeps the toy project obvious. (b) Jest/Vitest — rejected:
  external dependency, constitution violation.

## Decision 5: Node version floor

- **Decision**: Target Node.js 18+ (no engines field changes required).
- **Rationale**: `node:test` `describe`/`it` and `node --test` glob invocation are
  stable from Node 18; the repo already depends on this for the existing `greet`
  tests, so `shout` adds no new floor.
- **Alternatives considered**: None meaningful — pinned by existing repo setup.

## Resolution summary

All Technical Context fields in plan.md are concrete; no NEEDS CLARIFICATION
markers remain. Gate: **clear to proceed to Phase 1 design**.
