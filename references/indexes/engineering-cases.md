<!-- retrieval: {"source_type":"navigation","topics":["engineering-cases","navigation"],"limitations":"Navigation to static analyses; source-reported tests and outcomes were not independently reproduced."} -->
# Engineering case studies {#engineering-case-studies}

These 14 generalized examples present static analyses without links to the original implementations. Each case explains the engineering reasoning and the limits of its evidence. Browse by engineering problem or use the offline search tool.

## Lifecycle and ownership

- [Defer reclamation until active callbacks are safe](../cases/lifecycle/callback-reclamation.md#defer-reclamation-until-active-callbacks-are-safe)
- [Align replacement lifetime with the real owner](../cases/lifecycle/owner-lifetime.md#align-replacement-lifetime-with-the-real-owner)

## Testing and test oracles

- [Normalize only observations outside the contract](../cases/testing/golden-contract.md#normalize-only-observations-outside-the-contract)
- [Isolate the external resources a fixture actually uses](../cases/testing/fixture-isolation.md#isolate-the-external-resources-a-fixture-actually-uses)
- [Keep comparison policy independent of test output](../cases/testing/comparison-policy.md#keep-comparison-policy-independent-of-test-output)

## Concurrency and asynchronous work

- [Preserve event triggers when refactoring execution](../cases/concurrency/event-triggers.md#preserve-event-triggers-when-refactoring-execution)
- [Audit every continuation's executor](../cases/concurrency/executor-audit.md#audit-every-continuation-s-executor)
- [Serialization does not identify an asynchronous completion](../cases/concurrency/async-correlation.md#serialization-does-not-identify-an-asynchronous-completion)

## Build and dependency identity

- [Track artifact and recipe identity](../cases/build/artifact-recipe-identity.md#track-artifact-and-recipe-identity)

## Recovery and state

- [Design recovery before mutation](../cases/recovery/recovery-ownership.md#design-recovery-before-mutation)

## Evidence and capability claims

- [Bound negative claims by the search that produced them](../cases/evidence/negative-evidence.md#bound-negative-claims-by-the-search-that-produced-them)
- [Match capability claims to the boundary actually exercised](../cases/evidence/capability-evidence.md#match-capability-claims-to-the-boundary-actually-exercised)

## Compatibility and conversions

- [Check the value at the transformation boundary](../cases/compatibility/transformation-boundaries.md#check-the-value-at-the-transformation-boundary)

## Refactoring

- [Preserve progress, identity and polarity during mechanical-looking migrations](../cases/refactoring/migration-invariants.md#preserve-progress-identity-and-polarity-during-mechanical-looking-migrations)
