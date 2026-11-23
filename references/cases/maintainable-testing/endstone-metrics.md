<!-- retrieval: {"source_ids":[],"source_type":"public","date":"2026-08-22","topics":["testing","maintainability","complexity","review","ffi","api","duplicate-tests","test-harness"],"limitations":"Static review of linked primary sources and bundled historical analyses; upstream tests were not executed. Historical claims and code changes are distinguished from proven runtime outcomes."} -->
# Endstone #510: shrink an invented metrics service and delete expensive low-value tests {#case}

## Before and after {#changes}

[EndstoneMC/endstone PR #510](https://github.com/EndstoneMC/endstone/pull/510) initially supplied a `MetricsService` plus `MetricsRegistration` handles, per-plugin registration machinery, multiple callback and ownership layers, C++ chart types and a Python transport bridge. [Initial commit](https://github.com/EndstoneMC/endstone/commit/00f4d3a434fe) changed 32 paths, **+2,039/−77** against its base. Maintainer wu-vincent proposed matching bStats' simpler value-type API instead of designing a novel service and registration interface. [Architectural reduction](https://github.com/EndstoneMC/endstone/commit/f5810e3cbd5f) itself adds 616 and removes 1,058 lines, dropping the unnecessary registration hierarchy. Later, the [single C++ chart implementation](https://github.com/EndstoneMC/endstone/commit/b89b1a33c679) is exposed through Python bindings, removing duplicated Python chart implementations and bridging adapters.

Later in the same PR, [ba013842](https://github.com/EndstoneMC/endstone/commit/ba013842aae6) further adjusted backend ownership so short-lived value handles could safely disappear while the server retained the reporter. The final design was **not** simply a locally owned `Metrics` object whose destructor always stopped all collection.

The final cumulative PR reports **+1,545/−418 over 49 paths**, but includes additional JSON API work. This is **not** a valid estimate of module-only reduction; cite concrete intervening commits for causality.

## Three independent test reductions {#tests}

- [e1a8bc0](https://github.com/EndstoneMC/endstone/commit/e1a8bc07a012): roughly **394 deleted lines** from embedded-Python bridge tests and altered CI. The tests initialized Python inside GTest and required CI runtime dependencies, but mocked away the actual metrics backend. A later Python runtime suite was a better place for transport behavior.
- [83ea732](https://github.com/EndstoneMC/endstone/commit/83ea732d6cdd): **153 deleted lines** of C++ chart tests; the same chart types were already exercised through the Python bindings and Python was the consuming transport.
- [0113d00](https://github.com/EndstoneMC/endstone/commit/0113d0007d2e): **20 deleted lines** of public-header tests that merely scanned for substrings such as `std::mutex`. String absence does not prove the API compiles independently; a real out-of-tree translation unit would be the proper contract check.

The maintainer subsequently added targeted Python chart assertions in [c7ae406](https://github.com/EndstoneMC/endstone/commit/c7ae4068f957). This was consolidation, not abandonment of validation.

## Losses and unresolved risk {#limits}

The deletion messages explicitly acknowledge lost coverage of a native C++ `CustomChart` subclass and destruction of callbacks with captured resources. The bundled review of the final PR also flags incomplete proof for delayed callbacks, native plugin unload, and chart lifetime. Thus "less test code" is **not** the success criterion: any uncovered but material contract must remain a known gap, receive a narrower oracle, or be restored.

## Reusable decision {#reading}

Before adding a cross-language test harness or a service hierarchy, ask whether existing API ownership and the consumer's actual execution path can do the job. A test that stubs away the target and forces new CI dependencies has weak value relative to its maintenance cost. Related detailed analysis: [EndstoneMC--endstone--pull_request-510.md](../../sources/thread-review/threads/EndstoneMC--endstone--pull_request-510.md).
