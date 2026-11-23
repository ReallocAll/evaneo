<!-- retrieval: {"source_type":"public","topics":["engineering","comparator"],"limitations":"Comparative design guidance from external implementations; no upstream or target-implementation runtime tests were independently executed for this comparison.","source_ids":["public:comparator-source:bindings:CP-FT-DOC","public:comparator-source:bindings:CP-LIST-DOC","public:comparator-source:bindings:CP-LIST-CODE","public:comparator-source:bindings:CP-FT-CRITICAL"]} -->
# Acquiring a strong reference is a concurrent API decision {#case}

## Mechanism {#mechanism}
In free-threaded Python, a strong reference to a container element must be acquired using an API with appropriate concurrent access semantics. Strong references keep objects alive but do not freeze mutable state or provide multi-object business atomicity. Critical sections may suspend, and nested locks are not a universal transaction boundary.

## Applicability and validation {#applicability}
Use APIs documented for the active Python build, then test concurrent modifications and meaningful invariants. Do not generalize these restrictions to single-threaded, immutable contexts.

**Verification boundary:** No upstream or target-implementation runtime tests were independently executed for this comparison.

## References {#references}

Case BIND-04 in the [source inventory](sources.json) identifies the revisions and scope of these sources.

- [Free-threaded extension guidance (CP-FT-DOC)](https://github.com/python/cpython/blob/60403a5409ff2c3f3b07dd2ca91a7a3e096839c7/Doc/howto/free-threading-extensions.rst)
- [Strong reference list API (CP-LIST-DOC)](https://github.com/python/cpython/blob/60403a5409ff2c3f3b07dd2ca91a7a3e096839c7/Doc/c-api/list.rst)
- [List item acquisition implementation (CP-LIST-CODE)](https://github.com/python/cpython/blob/60403a5409ff2c3f3b07dd2ca91a7a3e096839c7/Objects/listobject.c)
- [Python critical sections (CP-FT-CRITICAL)](https://github.com/python/cpython/blob/60403a5409ff2c3f3b07dd2ca91a7a3e096839c7/Doc/c-api/init.rst)
