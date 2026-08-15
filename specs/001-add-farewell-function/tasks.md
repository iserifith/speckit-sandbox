---
description: "Task list for Add farewell(name) companion to greet(name)"
---

# Tasks: Add farewell(name) companion to greet(name)

**Input**: Design documents from `/specs/001-add-farewell-function/`

**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/library-api.md, quickstart.md

**Tests**: Tests ARE included — the constitution (Principle II: Test-First) and spec FR-005 make test coverage mandatory for this feature.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

**Assumptions (tasks phase, autonomous run — no human available)**:

- The repo scaffold (`package.json`, `src/greet.js`, `test/greet.test.js`) already exists and `npm test` is already wired to `node --test test/*.test.js`, so Phase 1 (Setup) and Phase 2 (Foundational) contain only verification tasks — no initialization work.
- Tests are written FIRST and must FAIL before implementation (Constitution II; plan.md orders tests before implementation).
- All decisions from the 2026-08-15 clarify session and research.md (D1–D5) are final and are not re-opened here: co-location in `src/greet.js`, exact `TypeError` message, no trimming, tests in the existing `test/greet.test.js`, zero dependencies.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- Single project: `src/`, `test/` at repository root (matches plan.md Project Structure).

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Verify the existing scaffold satisfies the plan's Technical Context — no new structure is created (plan.md Structure Decision: no new directories, no new modules, no build step).

- [ ] T001 Verify project structure matches plan.md: `src/greet.js` exports `greet`, `test/greet.test.js` exists, and `package.json` has `"type": "module"` with `"test": "node --test test/*.test.js"`
- [ ] T002 Verify toolchain prerequisite from quickstart.md: `node --version` reports >= 18 (built-in `node:test` runner) with no `npm install` step required (zero dependencies, Constitution III)

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Establish the green baseline that all user stories build on (Constitution II: `npm test` MUST stay green).

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [ ] T003 Run `npm test` on the untouched checkout and confirm exit status 0 with the two existing `greet` tests passing — this is the baseline every later task must preserve (FR-006)

**Checkpoint**: Baseline green — user story implementation can now begin

---

## Phase 3: User Story 1 - Produce a farewell string for a given name (Priority: P1) 🎯 MVP

**Goal**: `farewell("World")` returns exactly `"Goodbye, World!"`; any non-empty string is interpolated verbatim (`"Goodbye, <name>!"`, no trimming, no case-folding) — FR-001, SC-001.

**Independent Test**: Import `farewell` from `src/greet.js`, call it with `"World"`, assert the return equals `"Goodbye, World!"` (contract case C1), plus verbatim-interpolation cases C2 and C7. Runnable standalone via `node --test test/greet.test.js`.

### Tests for User Story 1 ⚠️

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation** (`farewell` is not yet exported, so they fail at import/assertion time).

- [ ] T004 [P] [US1] Add happy-path test to `test/greet.test.js` asserting `farewell("World") === "Goodbye, World!"` (contract C1, FR-001, SC-001, issue acceptance)
- [ ] T005 [P] [US1] Add verbatim-interpolation tests to `test/greet.test.js` asserting `farewell("  alice  ") === "Goodbye,   alice  !"` (no trimming/case-folding, contract C2, AS 1.2) and `farewell("   ") === "Goodbye,    !"` (whitespace-only accepted, contract C7, clarify 2026-08-15)
- [ ] T006 [US1] Run `npm test` and confirm the new US1 tests FAIL (red) — required before implementation per Constitution II

### Implementation for User Story 1

- [ ] T007 [US1] Implement `farewell(name)` in `src/greet.js` as a second named export appended after `greet`, returning `` `Goodbye, ${name}!` `` (template literal, verbatim interpolation per research D3); include the validation guard `if (!name || typeof name !== "string") { throw new TypeError("farewell(name) requires a non-empty string"); }` mirroring `greet` (research D2) — the guard makes US2's contract satisfiable and costs nothing here
- [ ] T008 [US1] Run `npm test` and confirm the US1 happy-path tests now pass (green) while the suite exits 0 overall

**Checkpoint**: User Story 1 is fully functional and independently testable — `farewell("World") === "Goodbye, World!"` proven by an executable test

---

## Phase 4: User Story 2 - Reject empty / non-string names with TypeError (Priority: P1)

**Goal**: `farewell` throws `TypeError` (exact message `farewell(name) requires a non-empty string`) for `""`, `undefined`, `null`, numbers, objects, booleans, Symbols, BigInts — FR-002, FR-003, FR-004, SC-002. No coercion, no fallback, no other error type.

**Independent Test**: Import `farewell` and assert it throws an instance of `TypeError` (not a generic `Error`) with the exact message for each of `""`, `undefined`, `null`, `42`, `{}` (spec US2 independent test), plus `Symbol()` and `1n` (contract C6). Runnable standalone via `node --test test/greet.test.js`.

### Tests for User Story 2 ⚠️

> **NOTE**: The validation guard lands with T007 (US1 implementation), so these tests are expected to PASS immediately when added. Per Constitution II they are still added as explicit executable coverage; if T007 is deferred or reverted, they MUST fail.

- [ ] T009 [P] [US2] Add empty-string rejection test to `test/greet.test.js` asserting `farewell("")` throws `TypeError` whose message is exactly `farewell(name) requires a non-empty string` (contract C3, FR-002, FR-004)
- [ ] T010 [P] [US2] Add non-string rejection tests to `test/greet.test.js` asserting `farewell` throws `TypeError` for each of `undefined`, `null`, `42`, `{}` (contract C4/C5, FR-003) and for `Symbol()` and `1n` (contract C6, spec edge case)
- [ ] T011 [US2] Add exact-message assertion to `test/greet.test.js` for the non-string path (e.g. `farewell(undefined)`) matching `farewell(name) requires a non-empty string` byte-for-byte (FR-004)

### Implementation for User Story 2

- [ ] T012 [US2] Run `npm test` and confirm all US2 rejection tests pass (green); if any fail, fix the guard in `src/greet.js` to exactly `if (!name || typeof name !== "string") { throw new TypeError("farewell(name) requires a non-empty string"); }` per research D2 and re-run

**Checkpoint**: User Stories 1 AND 2 both work independently — happy path and full rejection contract proven by executable tests

---

## Phase 5: User Story 3 - Co-located test coverage alongside existing greet tests (Priority: P2)

**Goal**: The test suite reads as one obvious unit covering both companion functions: every acceptance scenario from US1/US2 has an assertion in `test/greet.test.js`, and all pre-existing `greet` tests still pass unchanged — FR-005, FR-006, SC-003, SC-004.

**Independent Test**: Run `npm test` on a clean checkout; observe exit status 0, zero failures, the original two `greet` tests still present and passing, and farewell tests covering contract cases C1–C7.

- [ ] T013 [US3] Review `test/greet.test.js` and confirm every contract case C1–C7 from `contracts/library-api.md` has at least one assertion and that the two original `greet` tests are byte-for-byte unchanged (FR-006 guard); add any missing assertion in `test/greet.test.js`
- [ ] T014 [US3] Run `npm test` on a clean checkout and confirm exit status 0 with zero failures across both `greet` and `farewell` tests (SC-003)

**Checkpoint**: All user stories are independently functional and the suite is green as one unit

---

## Phase 6: Polish & Cross-Cutting Concerns

**Purpose**: End-to-end validation against the design artifacts; no scope expansion (single-issue, single-PR scope per spec assumptions).

- [ ] T015 [P] Run quickstart.md Scenario 2 (happy-path smoke: `farewell("World")` prints `OK: Goodbye, World!`) and Scenario 3 (error-path smoke: all of `""`, `undefined`, `null`, `42`, `{}` throw `TypeError` with the exact message)
- [ ] T016 [P] Run quickstart.md Scenario 4 (greet regression: `greet("World") === "Hello, World!"`, confirming FR-006)
- [ ] T017 Final gate: run `npm test` one last time and confirm exit status 0; confirm no files outside `src/greet.js` and `test/greet.test.js` were modified by the implementation (spec single-scope assumption; `package.json` and README untouched)

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - US1 (Phase 3) and US2 (Phase 4) share one implementation file (`src/greet.js`); execute sequentially US1 → US2 to avoid same-file conflicts
  - US3 (Phase 5) depends on US1+US2 test tasks existing (it audits their coverage)
- **Polish (Phase 6)**: Depends on all user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Starts after Foundational (Phase 2) - no dependencies on other stories
- **User Story 2 (P1)**: Its validation guard is implemented inside T007 (US1); US2 tasks are tests + verification only. Sequenced after US1 because both touch `src/greet.js` / `test/greet.test.js`
- **User Story 3 (P2)**: Depends on US1 and US2 test tasks (T004–T011) — it is a coverage audit of those same files

### Within Each User Story

- Tests MUST be written before implementation (Constitution II); for US1 they must be observed FAILING (T006) before T007
- Story complete (checkpoint green) before moving to next priority

### Parallel Opportunities

- T004 and T005 (US1 test cases) are independent assertions and can be written in one editing pass over `test/greet.test.js`
- T009, T010, T011 (US2 test cases) can likewise be written in one editing pass
- T015 and T016 (quickstart smoke checks) are independent read-only commands and can run in parallel
- Different user stories CANNOT run in parallel here: all stories touch the same two files (`src/greet.js`, `test/greet.test.js`), so same-file conflict rules force sequential execution

---

## Parallel Example: User Story 1

```bash
# Write both US1 test tasks together (same file, one editing pass):
Task: "Add happy-path test to test/greet.test.js (farewell(\"World\") === \"Goodbye, World!\")"
Task: "Add verbatim-interpolation tests to test/greet.test.js (\"  alice  \" and \"   \" cases)"

# Then implement:
Task: "Implement farewell(name) in src/greet.js (template literal + TypeError guard)"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup (verify only — no new structure)
2. Complete Phase 2: Foundational (green baseline)
3. Complete Phase 3: User Story 1 (tests red → implement → green)
4. **STOP and VALIDATE**: `farewell("World") === "Goodbye, World!"` proven by `npm test`
5. MVP is deliverable at this checkpoint

### Incremental Delivery

1. Setup + Foundational → baseline green
2. Add User Story 1 → happy path proven → checkpoint
3. Add User Story 2 → rejection contract proven → checkpoint
4. Add User Story 3 → full suite audited green → checkpoint
5. Polish → quickstart scenarios 2–4 pass → feature complete

Note: US1's implementation task (T007) deliberately includes the validation guard, so US2 lands as pure test coverage — this keeps `src/greet.js` edits to a single task and mirrors `greet` one-for-one (plan.md Summary).

---

## Notes

- [P] tasks = independent assertions or read-only commands; same-file edits are still applied in one pass
- [Story] label maps task to specific user story for traceability
- Verify US1 tests fail before implementing (T006 is the red gate)
- Commit after each task or logical group; `npm test` must be green at every commit (Constitution II)
- Stop at any checkpoint to validate the story independently via `node --test test/greet.test.js`
- Avoid: new modules, new dependencies, README/CI changes — all out of scope for this single-issue feature
