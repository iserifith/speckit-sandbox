# Quickstart: Tiny CLI Greeting Tool

**Date**: 2026-08-15 | **Feature**: `specs/001-cli-greeting-tool/spec.md`

Runnable validation scenarios proving the feature works end-to-end. For exact
flag/output/exit-code details see [contracts/cli.md](./contracts/cli.md); for
field rules see [data-model.md](./data-model.md).

## Prerequisites

- A Python 3 interpreter available as `python3` (no packages to install).
- Run all commands from the repository root (where `greet.py` lives).

## Scenario 1 — Default greeting (User Story 1, P1)

```bash
python3 greet.py
```

Expected: prints `Hello, world!` on stdout, nothing on stderr, exit code 0.
Verify exit code with `echo $?` → `0`.

## Scenario 2 — Personalised greeting (User Story 2, P2)

```bash
python3 greet.py --name Ada
```

Expected: prints `Hello, Ada!`, exit code 0.

## Scenario 3 — Shouted greeting (User Story 3, P3)

```bash
python3 greet.py --shout
python3 greet.py --name Ada --shout
```

Expected: prints `HELLO, WORLD!` and `HELLO, ADA!` respectively, each with
exit code 0.

## Scenario 4 — Invalid arguments (edge cases)

```bash
python3 greet.py --bogus     # unknown option
python3 greet.py --name      # missing value
```

Expected (each): usage/error message on stderr, **no** greeting on stdout,
exit code 2.

## Automated tests

```bash
# Zero-install runner (always available):
python3 -m unittest discover -s tests -v

# Or, if pytest is present:
python3 -m pytest tests/ -v
```

Expected: all tests pass — covering default, `--name`, and `--shout`
behaviour (including exact stdout text and exit codes).

## Regression check (constitution II)

```bash
npm test
```

Expected: the pre-existing Node suite (`node --test test/*.test.js`) remains
green; this feature adds no Node changes.
