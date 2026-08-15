---
description: "GitHub issues generated from tasks.md for Add farewell(name) companion to greet(name)"
---

# Issues: Add farewell(name) companion to greet(name)

**Phase**: issues (speckit-taskstoissues)
**Input**: `specs/001-add-farewell-function/tasks.md` (17 tasks, T001–T017)
**Parent issue**: #1

## Assumptions (issues phase, autonomous run — no human available)

- No GitHub MCP server is available in this environment, so the `gh` CLI was
  used for the equivalent list/dedupe/create operations against the repository
  matching the `origin` remote (`iserifith/speckit-sandbox`).
- Dedupe check: `gh issue list --state all --limit 100` returned only the
  parent issue #1 — no existing issue title matched any task ID `T001`–`T017`,
  so all 17 issues were created fresh.
- Each issue title follows the canonical form `T###: <description>` with the
  task description taken verbatim from the corresponding checkbox line in
  `tasks.md` (leading `- [ ]` and `[P]` / `[US#]` markers stripped).

## Created issues

| Task | Issue | Title |
| ---- | ----- | ----- |
| T001 | https://github.com/iserifith/speckit-sandbox/issues/3 | T001: Verify project structure matches plan.md |
| T002 | https://github.com/iserifith/speckit-sandbox/issues/4 | T002: Verify toolchain prerequisite from quickstart.md |
| T003 | https://github.com/iserifith/speckit-sandbox/issues/5 | T003: Run `npm test` on the untouched checkout (green baseline) |
| T004 | https://github.com/iserifith/speckit-sandbox/issues/6 | T004: Add happy-path test (`farewell("World") === "Goodbye, World!"`) |
| T005 | https://github.com/iserifith/speckit-sandbox/issues/7 | T005: Add verbatim-interpolation tests |
| T006 | https://github.com/iserifith/speckit-sandbox/issues/8 | T006: Confirm US1 tests FAIL (red gate) |
| T007 | https://github.com/iserifith/speckit-sandbox/issues/9 | T007: Implement `farewell(name)` in `src/greet.js` |
| T008 | https://github.com/iserifith/speckit-sandbox/issues/10 | T008: Confirm US1 tests pass (green) |
| T009 | https://github.com/iserifith/speckit-sandbox/issues/11 | T009: Add empty-string rejection test |
| T010 | https://github.com/iserifith/speckit-sandbox/issues/12 | T010: Add non-string rejection tests |
| T011 | https://github.com/iserifith/speckit-sandbox/issues/13 | T011: Add exact-message assertion |
| T012 | https://github.com/iserifith/speckit-sandbox/issues/14 | T012: Confirm US2 rejection tests pass (green) |
| T013 | https://github.com/iserifith/speckit-sandbox/issues/15 | T013: Coverage audit of contract cases C1–C7 |
| T014 | https://github.com/iserifith/speckit-sandbox/issues/16 | T014: Clean-checkout `npm test` green |
| T015 | https://github.com/iserifith/speckit-sandbox/issues/17 | T015: Quickstart Scenario 2 + 3 smoke checks |
| T016 | https://github.com/iserifith/speckit-sandbox/issues/18 | T016: Quickstart Scenario 4 greet regression |
| T017 | https://github.com/iserifith/speckit-sandbox/issues/19 | T017: Final gate — `npm test` green, scope check |

All 17 tasks now have exactly one GitHub issue each; no duplicates were
created and none were skipped.
