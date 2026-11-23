<!-- retrieval: {"source_type":"public","topics":["engineering","comparator"],"limitations":"Comparative design guidance from external implementations; no upstream or target-implementation runtime tests were independently executed for this comparison.","source_ids":["public:comparator-source:bindings:CP-PR105805","public:comparator-source:bindings:CP-FINAL-CODE","public:comparator-source:bindings:CP-FINAL-DOC","public:comparator-source:bindings:CP-FINAL-NEWS","public:comparator-source:bindings:CP-PR137827","public:comparator-source:bindings:CP-BACKPORT-COMMIT","public:comparator-source:bindings:CP-FINAL-TEST"]} -->
# Interpreter finalization is not a shutdown protocol {#case}

## Mechanism {#mechanism}
An interpreter waiting for native Python-using work to finish does not guarantee cancellation, resource delivery, completed destruction, or safe dynamic-library unload. Workers that may re-enter Python need explicit ownership and stop/join sequencing. Minor interpreter versions may differ, so a shutdown observation is version-bounded.

## Applicability and validation {#applicability}
Define who stops new callbacks, drains in-flight work, releases Python references, and owns the interpreter. Test blocked callbacks and unloading without assuming global finalization solves the worker lifecycle.

**Verification boundary:** No upstream or target-implementation runtime tests were independently executed for this comparison.

## References {#references}

Case BIND-03 in the [source inventory](sources.json) identifies the revisions and scope of these sources.

- [Finalization change rationale (CP-PR105805)](https://github.com/python/cpython/pull/105805)
- [GIL acquisition during finalization (CP-FINAL-CODE)](https://github.com/python/cpython/blob/8cc5aa47ee464ddfd8da5461edecf4a5c72df2ff/Python/ceval_gil.c)
- [CPython 3.14.0 finalization contract (CP-FINAL-DOC)](https://github.com/python/cpython/blob/ebf955df7a89ed0c7968f79faec1de49f61ed7cb/Doc/c-api/init.rst)
- [CPython finalization release note (CP-FINAL-NEWS)](https://github.com/python/cpython/blob/ebf955df7a89ed0c7968f79faec1de49f61ed7cb/Misc/NEWS.d/3.14.0a1.rst)
- [CPython 3.13 backport discussion (CP-PR137827)](https://github.com/python/cpython/pull/137827)
- [CPython 3.13 backport patch (CP-BACKPORT-COMMIT)](https://github.com/python/cpython/commit/9face218e7b640e52b83cd68cebb441d5ff0f8e2)
- [Worker thread finalization test (CP-FINAL-TEST)](https://github.com/python/cpython/blob/8cc5aa47ee464ddfd8da5461edecf4a5c72df2ff/Lib/test/test_threading.py)
