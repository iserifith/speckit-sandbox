# Implementation Plan: Tiny CLI Greeting Tool

**Branch**: `spec/issue-23` | **Date**: 2026-08-15 | **Spec**: [spec.md](./spec.md)

**Input**: Feature specification from `/specs/001-cli-greeting-tool/spec.md`

## Summary

Add a single-file Python 3 CLI tool, `greet.py`, at the repository root that
prints the canonical greeting `Hello, <name>!` to stdout and exits 0. It
supports `--name <name>` (default `world`) and `--shout` (uppercases the whole
greeting), composable in either order. Invalid arguments (unknown flag, missing
`--name` value) produce a usage message on stderr and exit code 2, per Python
`argparse` convention. Behaviour is covered by a Python test module at
`tests/test_greet.py` exercising the three required behaviours (default,
`--name`, `--shout`). The repo's existing Node `node:test` suite in `test/`
stays untouched and green per the constitution. Technical approach: pure Python
3 standard library (`argparse`), no external dependencies, tests runnable with
either the stdlib `unittest` runner or pytest — no installs required.

## Technical Context

**Language/Version**: Python 3 (any Python 3.8+ interpreter; invoked as `python3 greet.py`)
**Primary Dependencies**: Python standard library only (`argparse`); no third-party packages
**Storage**: N/A
**Testing**: Python tests at `tests/test_greet.py` written against the stdlib `unittest` API so they run with zero installs (`python3 -m unittest` or `python3 -m pytest`); the existing Node suite (`npm test`, `node --test test/*.test.js`) is unaffected
**Target Platform**: Any platform with a `python3` interpreter (Linux/macOS/Windows); primary target is the sandbox's Linux runner
**Project Type**: CLI (single-file command-line tool)
**Performance Goals**: N/A (trivial; startup-dominated, well under 1s per invocation)
**Constraints**: No external dependencies (constitution III); implementation must be a handful of files completable in one sandboxed run (constitution I); test-first (constitution II) — the Python test module lands alongside the tool and the Node suite must remain green
**Scale/Scope**: 2 new files (`greet.py`, `tests/test_greet.py`); ~40 LOC total

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

| Principle | Gate | Verdict |
|-----------|------|---------|
| I. Trivial By Design | Feature is a handful of files/tests, implementable in a single sandboxed run | PASS — 2 new files, ~40 LOC |
| II. Test-First | Every change adds or updates a test; `npm test` MUST stay green | PASS — `tests/test_greet.py` covers all three behaviours; no changes to `src/`, `test/`, or `package.json`, so `npm test` remains green |
| III. No External Dependencies | No third-party installs; stdlib only | PASS — `argparse` + stdlib test runner only |

No violations. Complexity Tracking table intentionally left empty.

## Project Structure

### Documentation (this feature)

```text
specs/001-cli-greeting-tool/
├── spec.md              # Feature specification (specify phase, amended by clarify)
├── checklists/
│   └── requirements.md  # Spec quality checklist (specify phase)
├── plan.md              # This file ($speckit-plan command output)
├── research.md          # Phase 0 output ($speckit-plan command)
├── data-model.md        # Phase 1 output ($speckit-plan command)
├── quickstart.md        # Phase 1 output ($speckit-plan command)
├── contracts/           # Phase 1 output ($speckit-plan command)
│   └── cli.md           # CLI contract: flags, output, exit codes
└── tasks.md             # Phase 2 output ($speckit-tasks command - NOT created by $speckit-plan)
```

### Source Code (repository root)

```text
greet.py                 # NEW: the CLI tool (stdlib argparse; prints greeting, exit 0/2)
tests/
└── test_greet.py        # NEW: Python tests for default / --name / --shout behaviour

# Existing, untouched by this feature:
src/greet.js             # Existing toy Node module
test/greet.test.js       # Existing Node test suite (npm test)
package.json             # Unchanged
```

**Structure Decision**: Single-project layout, per the issue's explicit
acceptance criteria: `greet.py` lives at the repository root (not under
`src/`), and its tests live in a new `tests/` directory (Python) to avoid
colliding with the existing Node `test/` directory whose glob
(`node --test test/*.test.js`) must keep matching only JavaScript files. This
keeps `npm test` green by construction and satisfies the issue's
`tests/test_greet.py` naming.

## Complexity Tracking

No constitution violations — this section is intentionally empty.
