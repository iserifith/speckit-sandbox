# Phase 0 Research: Tiny CLI Greeting Tool

**Date**: 2026-08-15 | **Feature**: `specs/001-cli-greeting-tool/spec.md`

The Technical Context in plan.md contained no `NEEDS CLARIFICATION` markers —
every decision is either mandated by issue #23 or pinned by the clarify phase.
This file records the decisions and the alternatives that were considered.

## Decision 1: Argument parsing via Python stdlib `argparse`

- **Decision**: Use `argparse.ArgumentParser` with a `--name` option
  (`default="world"`) and a `--shout` flag (`action="store_true"`).
- **Rationale**: `argparse` is the Python 3 standard-library argument parser.
  It natively produces the clarify-pinned error behaviour for free: unknown
  flags and a missing `--name` value print a usage message to **stderr** and
  exit with code **2**. It is dependency-free (constitution III).
- **Alternatives considered**:
  - Manual `sys.argv` parsing — rejected: easy to get the stderr/exit-2
    convention wrong, more code, no benefit at this scale.
  - Third-party parsers (click, typer) — rejected: violate the
    no-external-dependencies constitution principle.

## Decision 2: Exact greeting wording and shout semantics

- **Decision**: Canonical greeting is `Hello, <name>!` followed by a single
  newline (standard `print()` behaviour). `--shout` applies `str.upper()` to
  the entire greeting line, including the name (`HELLO, ADA!`).
- **Rationale**: Pinned during the clarify phase (see spec.md Clarifications,
  Session 2026-08-15) so acceptance tests can assert exact output.
- **Alternatives considered**: Other wordings (`Hi, <name>.`, `Greetings,
  <name>`) — rejected: the clarify phase already pinned `Hello, <name>!`, and
  it matches the repo's existing Node toy (`src/greet.js` returns
  `Hello, ${name}!`), keeping the sandbox consistent.

## Decision 3: Test framework — stdlib `unittest`-style tests (pytest-compatible)

- **Decision**: Write `tests/test_greet.py` using only stdlib constructs so it
  runs with **both** `python3 -m unittest discover tests` (zero installs,
  guaranteed available) and `python3 -m pytest tests/` (nicer output if pytest
  happens to be present). Tests invoke the CLI as a subprocess
  (`subprocess.run([sys.executable, "greet.py", ...])`) and assert on stdout,
  stderr, and exit code.
- **Rationale**: The issue says "a simple `tests/test_greet.py` (or
  equivalent)" without naming a framework. Stdlib-compatible tests honour the
  dependency-free constitution: the sandbox runner never needs a network
  install. Subprocess testing exercises the tool's *observable* behaviour
  (stdout text, exit codes) exactly as the acceptance criteria phrase it,
  rather than reaching into internals.
- **Alternatives considered**:
  - pytest-only style with `capsys`/`monkeypatch` — rejected: requires a
    pytest install, violating constitution III's no-network-installs spirit.
  - Importing `greet.py` as a module and calling a `main()` — rejected as the
    primary mechanism: it cannot observe the real exit code / stdout stream
    contract; kept as an option only if subprocess proves flaky (it won't).

## Decision 4: Test placement — new `tests/` directory, Node `test/` untouched

- **Decision**: Python tests go in a new `tests/` directory; the existing Node
  suite in `test/` is not modified.
- **Rationale**: `package.json` runs `node --test test/*.test.js`; adding
  Python files to `test/` would not break that glob, but a separate `tests/`
  directory matches the issue's requested path (`tests/test_greet.py`) and
  keeps the two toy stacks cleanly separated. `npm test` stays green by
  construction (constitution II).
- **Alternatives considered**: Putting Python tests in `test/` — rejected:
  conflates the two toolchains and deviates from the issue's literal path.

## Decision 5: Empty/whitespace and unusual name values

- **Decision**: No validation or trimming of `--name` values; whatever string
  is supplied appears in the greeting verbatim (including spaces and
  punctuation). `--name ""` yields `Hello, !`.
- **Rationale**: Spec edge cases explicitly state no special handling is
  required for this trivial tool.
- **Alternatives considered**: Trimming/rejecting empty names (mirroring
  `src/greet.js`'s TypeError on empty input) — rejected: the spec for *this*
  feature explicitly declines validation; the Node module's contract is
  separate and unchanged.

## Open Questions

None. All NEEDS CLARIFICATION items are resolved; proceed to Phase 1.
