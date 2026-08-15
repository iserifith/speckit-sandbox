# speckit-sandbox

A dummy repo for exercising the Hermes `github-spec-runner` /
`github-codetask-runner` pipeline against something disposable, instead of a
real project. Safe to break, force-push, or nuke and recreate at will.

Contains the standard portable speckit toolkit (`.agents/skills/speckit-*`,
`.specify/`) plus a trivial, dependency-free Node project (`src/greet.js` +
`node:test`) so the pipeline has something small and fast to actually work on.

## Usage

Open an issue describing a tiny, toy change (a new function, an edge case, a
README tweak) and drive it through the normal comment triggers:

```
/hermes-spec        # github-spec-runner --phase specify
/hermes-clarify      # github-spec-runner --phase clarify
/hermes-plan         # github-spec-runner --phase plan
/hermes-tasks        # github-spec-runner --phase tasks
/hermes-issues       # github-spec-runner --phase issues
/hermes-implement    # github-codetask-runner (one-shot fix/implement)
```

Base branch is `dev`, matching the convention used by the real repos this
pipeline runs against (never assume `main`).

Do not put real feature work here — see `.specify/memory/constitution.md`.
