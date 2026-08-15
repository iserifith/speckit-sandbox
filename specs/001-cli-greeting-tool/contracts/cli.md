# CLI Contract: `greet.py`

**Date**: 2026-08-15 | **Feature**: `specs/001-cli-greeting-tool/spec.md`

The feature exposes exactly one external interface: the `greet.py` command line.

## Synopsis

```text
python3 greet.py [--name NAME] [--shout]
python3 greet.py -h | --help
```

## Arguments

| Argument | Kind | Default | Effect |
|----------|------|---------|--------|
| `--name NAME` | option (takes a value) | `world` | Recipient addressed in the greeting. Value used verbatim — no trimming, no validation; spaces/punctuation/empty string accepted. |
| `--shout` | flag (no value) | absent (false) | Uppercases the entire greeting line, including the name. |
| `-h`, `--help` | flag | — | Prints usage/help to stdout and exits 0 (standard argparse behaviour). |

`--name` and `--shout` are composable in a single invocation, in any order.

## Output contract

| Invocation | stdout | stderr | Exit code |
|------------|--------|--------|-----------|
| `python3 greet.py` | `Hello, world!\n` | empty | 0 |
| `python3 greet.py --name Ada` | `Hello, Ada!\n` | empty | 0 |
| `python3 greet.py --shout` | `HELLO, WORLD!\n` | empty | 0 |
| `python3 greet.py --name Ada --shout` | `HELLO, ADA!\n` | empty | 0 |
| `python3 greet.py --bogus` | empty (no greeting) | usage/error message | 2 |
| `python3 greet.py --name` (missing value) | empty (no greeting) | usage/error message | 2 |

## Guarantees

- Exactly one greeting line is printed for every valid invocation; nothing else
  is written to stdout.
- No greeting line is printed for invalid invocations.
- No files are read or written; no network access; no environment dependence
  beyond a Python 3 interpreter.
