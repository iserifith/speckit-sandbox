# Phase 1 Data Model: Tiny CLI Greeting Tool

**Date**: 2026-08-15 | **Feature**: `specs/001-cli-greeting-tool/spec.md`

This feature is a stateless, single-run CLI tool. It has no persistent
entities, no storage, and no state transitions. The only "model" is the shape
of one invocation, documented here for completeness.

## Invocation (transient, in-memory only)

| Field | Type | Source | Validation / rules |
|-------|------|--------|--------------------|
| `name` | string | `--name <value>` argument; default `"world"` | No trimming or validation; used verbatim, including spaces, punctuation, and the empty string (spec Edge Cases) |
| `shout` | boolean | presence of `--shout` flag; default `false` | Flag only; takes no value |

## Greeting (derived output)

| Field | Derivation |
|-------|------------|
| `text` | `"Hello, " + name + "!"`, then `text.upper()` if `shout` is true |
| destination | standard output, exactly one line (trailing newline from `print()`), then exit code 0 |

## Error result (invalid invocation)

| Condition | Behaviour |
|-----------|-----------|
| Unknown option, or `--name` supplied without a value | Usage/error message to standard error, no greeting on stdout, exit code 2 (argparse convention, pinned by clarify) |

## State Transitions

None — each process invocation is independent and terminates immediately after
printing (or after the argument error).
