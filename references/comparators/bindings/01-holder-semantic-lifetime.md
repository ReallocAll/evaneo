<!-- retrieval: {"source_type":"public","topics":["engineering","comparator"],"limitations":"Comparative design guidance from external implementations; no upstream or target-implementation runtime tests were independently executed for this comparison.","source_ids":["public:comparator-source:bindings:PB-ISS1333","public:comparator-source:bindings:PB-CLASS","public:comparator-source:bindings:PB-SMART","public:comparator-source:bindings:PB-ISS5623","public:comparator-source:bindings:PB-PR5624","public:comparator-source:bindings:PB-WEAK-TEST","public:comparator-source:bindings:PB-WEAK-CODE"]} -->
# Cross-language object lifetime is not callback lifetime {#case}

## Mechanism {#mechanism}
A C++ shared_ptr retaining the native base does not automatically keep the Python-derived override alive. In pybind11, smart_holder plus trampoline_self_life_support can preserve Python-derived behavior. A weak_ptr obtained from a temporary control block can expire while the Python object still exists. The potentially_slicing_weak_ptr helper trades one behavior for another, so weak-subscription semantics must be explicit.

## Applicability and validation {#applicability}
Test deleting the last visible Python reference, invoking a later virtual callback, then cancelling the subscription. Assert the actual override target rather than only absence of a crash. Do not extend an engine-owned entity lifetime merely by changing its Python holder.

**Verification boundary:** No upstream or target-implementation runtime tests were independently executed for this comparison.

## References {#references}

Case BIND-01 in the [source inventory](sources.json) identifies the revisions and scope of these sources.

- [Lost Python override report (PB-ISS1333)](https://github.com/pybind/pybind11/issues/1333)
- [Python subclasses and ownership (PB-CLASS)](https://github.com/pybind/pybind11/blob/ed5057ded698e305210269dafa57574ecf964483/docs/advanced/classes.rst)
- [Smart holder contract (PB-SMART)](https://github.com/pybind/pybind11/blob/ed5057ded698e305210269dafa57574ecf964483/docs/advanced/smart_ptrs.rst)
- [Weak pointer expiry report (PB-ISS5623)](https://github.com/pybind/pybind11/issues/5623)
- [Weak pointer helper rationale (PB-PR5624)](https://github.com/pybind/pybind11/pull/5624)
- [Weak pointer test expectations (PB-WEAK-TEST)](https://github.com/pybind/pybind11/blob/ed5057ded698e305210269dafa57574ecf964483/tests/test_potentially_slicing_weak_ptr.py)
- [C++ test fixture (PB-WEAK-CODE)](https://github.com/pybind/pybind11/blob/ed5057ded698e305210269dafa57574ecf964483/tests/test_potentially_slicing_weak_ptr.cpp)
