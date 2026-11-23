<!-- retrieval: {"source_type":"static_review","topics":["build","dependencies","packaging","CI","cache","reproducibility","ABI","diagnosis"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="track-artifact-and-recipe-identity"></a>

# Track artifact and recipe identity {#track-artifact-and-recipe-identity}

## Problem {#problem}

A dependency's semantic version can remain unchanged while its package contents change. A build may have the correct binary version but an older recipe revision that omits required headers or generated support files. A cache can preserve that mismatch after the packaging source is fixed.

## Inspected chain {#inspected-chain}

One change added missing public and generated headers to a package. The source distinguished verification performed on one platform from export behavior merely inferred on another, and reported that repackaging did not change the existing library binary.

A later change addressed selection rather than packaging: CI had restored a package revision predating the added headers. The dependency reference was tightened to select the revision containing them. This demonstrates why “the packaging fix exists” and “the consumer resolved the fixed package” are separate claims.

A related preflight change checked the actual runtime version selected by the execution environment before a compatibility test. It separated environment bootstrapping from the scenario run so a drifted version could fail early instead of masquerading as an implementation defect.

## Diagnostic procedure {#diagnostic-procedure}

Record the identities of:

- Source revision and package recipe revision
- Resolved package/binary identity and cache origin
- Build-tree artifact
- Installed layout and generated headers
- Artifact or runtime actually loaded by the consumer

Compare those identities before rebuilding unrelated code. Verify the delivered include tree as well as exported symbols: a library can expose a symbol while the consumer cannot compile a declaration for it.

Keep observed and inferred platform evidence separate. A successful link or symbol inspection on one platform does not establish another platform's packaging, import library or export behavior.

## Tradeoffs {#tradeoffs}

An exact recipe pin makes an intended revision selectable and reproducible, but it also needs an update policy. Automatic refresh, lockfiles and controlled cache invalidation can be better fits in other workflows. Clearing every cache is a diagnostic experiment, not a substitute for identifying the stale object.

A contrasting dependency change replaced a fixed version requirement with a compatible range so that direct and transitive requirements could resolve together. That supports dependency-graph consistency, not a universal preference for either exact pins or ranges. Another local recipe override was removed after the build configuration that needed it was no longer used; retiring a conditional workaround does not prove the original upstream problem was fixed.

Generated-file discovery also deserves validation: a search that assumes exactly one matching output directory can fail or pick stale output. The inspected change did not establish a general solution for every build generator.

The patches were read; builds, packaging, symbol inspection and runtime preflight were not executed in this review. This case supports a layered identity check, not a claim that all platforms passed.
