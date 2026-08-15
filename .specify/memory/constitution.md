# Speckit Sandbox Constitution

## Core Principles

### I. Trivial By Design
This repo exists to exercise the Hermes speckit/codetask runner pipeline, not to
ship real features. Every proposal MUST be small enough to implement in a single
sandboxed run — a handful of files, a handful of tests. If a proposal looks like
real work, it belongs in a real repo instead.

### II. Test-First
Every change adds or updates a test in `test/`. `npm test` MUST stay green.

### III. No External Dependencies
Keep the toy project dependency-free (Node's built-in `node:test` + `assert`
only) so runs are fast and don't depend on network installs mid-sandbox.

## Development Workflow

Standard speckit pipeline: `/hermes-spec` → `/hermes-clarify` → `/hermes-plan` →
`/hermes-tasks` → `/hermes-issues` → `/hermes-implement` (or `/hermes-fix` for a
one-shot issue). One branch/PR per issue, base branch `dev`.

## Governance

This constitution only governs this sandbox repo. Amend freely — there is
nothing downstream depending on stability here.

**Version**: 1.0.0 | **Ratified**: 2026-08-15 | **Last Amended**: 2026-08-15
