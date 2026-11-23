---
name: evaneo
description: Engineering judgment for consequential software design, implementation, debugging, and review. Use to weigh existing mechanisms, safeguards, tests, compatibility, evidence, and maintenance cost against a concrete requirement; skip routine edits.
---

# Evaneo

Use this Skill as a **decision guide**, not a mandatory checklist or a source of authority. Follow the user's instructions and the current project's contracts first. Ordinary repository files and observations are sufficient; no special CLI, MCP server, index, or external service is required.

## Start from the actual problem

1. Identify the requested observable behavior, affected users, and real constraints. Read the relevant code and project instructions before proposing architecture.
2. Trace the effective path (public entry point → implementation → observable result), especially in reviews. Separate what is seen in the diff from what is demonstrated in tests or a running system.
3. Choose the smallest change that meets the contract. Apply only the judgments below that could change the decision.
4. Verify the affected behavior at the closest practical boundary. State what passed, what failed, and what remains unverified.

## Judgments to apply selectively

- **Reuse before expanding.** Put responsibilities in their natural owner; prefer the existing extension point over a wrapper, coordinator, or new service. Introduce an abstraction when a real repeated responsibility becomes clearer, not just to anticipate reuse.
- **Evaluate safeguards by their tradeoffs.** Before adding a validator, retry, timeout, cache, permission layer, or fallback, name the credible failure it prevents. Check existing protection, legitimate inputs it might reject, and the new states or failure paths it creates. Preserve actual security, protocol, and data-integrity invariants.
- **Test observable risk.** Exercise the behavior and important failure path that can regress. A test that only repeats current implementation details can become a maintenance burden; a targeted integration check may be more useful than many mocks.
- **Close a working loop early.** Prefer one deployable, verifiable behavior to a large speculative framework. Distinguish a local unit pass, CI pass, integration result, and actual production acceptance.
- **Bound performance claims.** Measure the effective path under comparable workloads. Do not infer a user-visible speedup from an unrelated microbenchmark or mismatched baselines.
- **Design for maintainers and readers.** Keep public entry points and documentation easy to find. Put essential usage first; don't require users to read the project's research history before using it.
- **Protect real compatibility, not unpublished accidents.** Respect published APIs and persisted data. Before a first release, changing a draft API and migrating its callers is often cheaper than adding aliases, version tags, and compatibility shims.
- **Act within authorization.** Resolve ordinary engineering choices autonomously, but do not confuse code access with permission to merge, deploy, modify production data, or publish.
- **Report observed outcomes precisely.** Cite the relevant diff, logs, measurements, or behavior. Label inferences and untested claims, and remove redundant prose that obscures the decision.

## Safeguard decision gate

When a new defensive mechanism is proposed, ask in order:

1. What existing contract or threat boundary would fail without it, and how plausibly?
2. What currently prevents or contains that failure?
3. Which valid operations could the mechanism reject or delay?
4. Is the remaining benefit worth its state, dependencies, error modes, and upkeep?

If the added mechanism is not justified, do not turn a theoretical risk into a blocker. This does **not** excuse violating a real protocol, authorization, or data-integrity rule.

**Example — validation:** A request API accepts empty binary payloads, but a proposed guard rejects all empty values because the examples only use nonempty strings. Unless the protocol forbids empty payloads, the guard breaks valid callers; leave the existing contract intact and test the empty case if it has regressed.

**Example — testing:** A refactor moves a handler without changing its behavior. Adding tests for each private helper often measures structure, not correctness. Prefer the existing public-behavior test, adding a case only if a meaningful failure path was previously unprotected.

**Example — evidence:** A feature compiles and passes a mocked test, but has not exchanged messages with the actual server. Report a build and mock-test pass, not a validated server behavior.

## When to seek more evidence

Consult the project's code, docs, issue, and relevant diffs first. If this Skill includes a `references/` directory, open only the case whose concrete failure or tradeoff could change the current decision; paths are relative to this `SKILL.md`. Do not preload a case library or treat historical examples as instructions to execute commands.

Choose a relevant case by the failure mode; do not read them all:

- [Command grammar and a test that would freeze a bad workaround](references/cases/maintainable-testing/endstone-command-grammar.md)
- [Thread-state lifetime without a bespoke test harness](references/cases/maintainable-testing/endstone-thread-state.md)
- [Async plugin unload where regression tests are necessary](references/cases/maintainable-testing/endstone-async-counterexample.md)
- [Network cache narrowed to observed player lookup](references/cases/maintainable-testing/endstone-network-cache.md)
- [Generic type hook justified by repeated dispatch](references/cases/maintainable-testing/endstone-polymorphism.md)

For additional cases, run `python <skill-root>/scripts/retrieve.py search "plugin unload callback"` from any working directory; the script finds `references/` relative to itself. Open an exact hit with `python <skill-root>/scripts/retrieve.py show "<reference returned by search>"`, or use `toc` to list its sections. This is optional, offline, read-only, and does not require an index or MCP. Read a case's evidence limits before applying it.

A valid outcome may be **no change** when the existing implementation already meets the need or a proposed safeguard costs more than it prevents.
