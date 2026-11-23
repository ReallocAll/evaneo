<!-- retrieval: {"source_type":"public","topics":["engineering","comparator"],"limitations":"Comparative design guidance from external implementations; no upstream or target-implementation runtime tests were independently executed for this comparison.","source_ids":["public:comparator-source:bindings:PB-PR4877","public:comparator-source:bindings:PB-ONCE","public:comparator-source:bindings:PB-DEADLOCK","public:comparator-source:bindings:PB-PR5246","public:comparator-source:bindings:PB-ATOMIC-PATCH"]} -->
# Static initialization may deadlock with the GIL {#case}

## Mechanism {#mechanism}
A function-local static may acquire an implicit initialization lock. If its initializer enters Python, releases the GIL, and another thread tries the same static while holding the GIL, lock ordering can deadlock. Moving storage or changing initialization order can break the cycle; never-destroy storage is not a shutdown or reload contract.

## Applicability and validation {#applicability}
Test concurrent first use with controlled GIL release and reacquisition. Avoid adding atomics or GIL lock helpers to unrelated simple values.

**Verification boundary:** No upstream or target-implementation runtime tests were independently executed for this comparison.

## References {#references}

Case BIND-02 in the [source inventory](sources.json) identifies the revisions and scope of these sources.

- [GIL-safe initialization rationale (PB-PR4877)](https://github.com/pybind/pybind11/pull/4877)
- [Initialization helper implementation (PB-ONCE)](https://github.com/pybind/pybind11/blob/ed5057ded698e305210269dafa57574ecf964483/include/pybind11/gil_safe_call_once.h)
- [Static initializer lock ordering (PB-DEADLOCK)](https://github.com/pybind/pybind11/blob/ed5057ded698e305210269dafa57574ecf964483/docs/advanced/deadlock.md)
- [Free-threaded initialization fix (PB-PR5246)](https://github.com/pybind/pybind11/pull/5246)
- [Atomic initialization patch (PB-ATOMIC-PATCH)](https://github.com/pybind/pybind11/commit/43de8014f96ab8fc0028f11a26edbcf9b937cd91)
