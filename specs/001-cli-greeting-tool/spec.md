# Feature Specification: Tiny CLI Greeting Tool

**Feature Branch**: `spec/issue-23`

**Created**: 2026-08-15

**Status**: Draft

**Input**: User description: "Add a small Python CLI tool `greet.py` at the repo root that prints a greeting. Acceptance criteria: Running `python3 greet.py` prints a greeting line to stdout and exits 0. An optional `--name <name>` flag personalises the greeting; default name is `world`. A `--shout` flag uppercases the greeting. Include a simple `tests/test_greet.py` (or equivalent) covering default, --name, and --shout behaviour. (GitHub issue #23)"

## Clarifications

### Session 2026-08-15

- Q: What is the exact canonical greeting text the tool prints? → A: `Hello, <name>!` (e.g. `Hello, world!`)
- Q: Where are usage/error messages written, and with what exit code, on invalid arguments? → A: standard error, exit code 2

Note: no human was available during this autonomous clarify run; both answers were self-selected as the best-supported choices and are recorded here and in Assumptions per the autonomous-operation instruction.

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Print a default greeting (Priority: P1)

A user runs the greeting tool from the command line with no arguments and immediately sees a friendly greeting line printed to their terminal, addressed to a generic default recipient ("world").

**Why this priority**: This is the core, minimal value of the tool — a working greeting with zero input. Without it there is no feature at all.

**Independent Test**: Can be fully tested by invoking the tool with no arguments and verifying a greeting line containing "world" appears on standard output and the run completes successfully (exit code 0). Delivers a working minimal greeting tool on its own.

**Acceptance Scenarios**:

1. **Given** the tool is installed at the repository root, **When** the user runs it with no arguments, **Then** a single greeting line addressed to "world" is printed to standard output.
2. **Given** the tool is run with no arguments, **When** the greeting has been printed, **Then** the process terminates with exit code 0 and no error output.

---

### User Story 2 - Personalise the greeting with a name (Priority: P2)

A user passes an optional name flag so the greeting addresses a specific person or entity instead of the generic default.

**Why this priority**: Personalisation is the primary way users make the tool their own, but the tool is already useful (P1) without it.

**Independent Test**: Can be fully tested by invoking the tool with a name argument and verifying the printed greeting contains that name instead of "world", with exit code 0.

**Acceptance Scenarios**:

1. **Given** the tool is available, **When** the user runs it with a name option set to "Ada", **Then** the greeting line addresses "Ada" rather than "world".
2. **Given** the tool is available, **When** the user runs it with a name option, **Then** the process still terminates with exit code 0.

---

### User Story 3 - Shout the greeting (Priority: P3)

A user passes an optional "shout" flag so the entire greeting is printed in uppercase, for emphasis or fun.

**Why this priority**: A cosmetic flourish that builds on the basic greeting; the lowest-priority story.

**Independent Test**: Can be fully tested by invoking the tool with the shout flag and verifying the printed greeting is entirely uppercase, with exit code 0.

**Acceptance Scenarios**:

1. **Given** the tool is available, **When** the user runs it with the shout flag, **Then** every letter in the greeting line is uppercase.
2. **Given** the tool is available, **When** the user combines the shout flag with a name option, **Then** the personalised greeting is printed entirely in uppercase.

---

### Edge Cases

- When the name option is supplied without a value, the tool prints a usage error to standard error and exits with code 2 (standard command-line argument parsing behaviour).
- When an unrecognised option is supplied, the tool prints a usage error to standard error and exits with code 2.
- An empty or whitespace-only name value is treated as provided (the greeting addresses it literally); no special trimming or validation is required for this trivial tool.
- Names containing spaces or punctuation are accepted as-is and appear in the greeting unchanged.
- The shout transformation applies to the whole greeting line, including the name.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: The tool MUST print a greeting line to standard output when invoked with no arguments. The canonical greeting text is `Hello, <name>!` (e.g. `Hello, world!` with the default recipient).
- **FR-002**: The tool MUST exit with status code 0 after successfully printing the greeting.
- **FR-003**: The greeting MUST address a default recipient named "world" when no name is provided.
- **FR-004**: The tool MUST accept an optional name option (`--name <name>`) that replaces the default recipient in the greeting.
- **FR-005**: The tool MUST accept an optional shout flag (`--shout`) that uppercases the entire greeting line.
- **FR-006**: The name option and shout flag MUST be composable (both may be used together in a single invocation).
- **FR-007**: The tool MUST exit with a non-zero status (exit code 2, matching standard command-line argument parsing behaviour) and print a usage/error message to standard error when given invalid arguments (e.g., unknown flags or a missing value for the name option); no greeting line is printed to standard output in this case.
- **FR-008**: The feature MUST include an automated test covering: default greeting behaviour, personalised greeting via the name option, and uppercase greeting via the shout flag.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: 100% of valid invocations (no arguments, name option, shout flag, or both options) print exactly one greeting line to standard output and exit with status code 0.
- **SC-002**: 100% of invalid invocations (unknown option or missing name value) exit with code 2, print a usage/error message to standard error, and print no greeting line to standard output.
- **SC-003**: A first-time user can run the tool and see a greeting in under 10 seconds, with no setup steps beyond having a standard runtime available.
- **SC-004**: All automated tests for the three required behaviours (default, name, shout) pass on every run.

## Assumptions

- The implementation language is Python 3 and the entry point is a single file named `greet.py` at the repository root, exactly as stated in issue #23. (Spec-level behaviour above is written technology-agnostically; this assumption records the issue-mandated implementation constraint for downstream phases.)
- The exact greeting text is unspecified by the issue; the canonical wording is pinned to `Hello, <name>!` (e.g. `Hello, world!`, `Hello, Ada!`, shouted form `HELLO, ADA!`) so acceptance tests can assert exact output. (Resolved during clarify; see Clarifications section.)
- Usage/error messages are written to standard error and the process exits with code 2 on invalid arguments, matching the Python 3 standard library argument-parsing convention. (Resolved during clarify; see Clarifications section.)
- The automated test lives at `tests/test_greet.py` (or an equivalent path chosen in planning) and exercises the tool's observable behaviour; the repo's existing Node test suite in `test/` remains untouched and green per the constitution.
- The tool adds no external dependencies beyond the Python 3 standard library, consistent with the constitution's dependency-free spirit.
- No human was available to answer clarification questions during this phase; all ambiguities were resolved with the reasonable defaults documented here.
