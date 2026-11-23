<!-- retrieval: {"source_ids":["public:thread:numpy/numpy:24833"],"source_type":"public","date":"2023-09-29","topics":["concurrency","ffi","testing","diagnosis","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="numpy-numpy-24833-bug-importing-embedded-numpy-hangs-on-windows"></a>
# numpy/numpy#24833: BUG: Importing embedded NumPy hangs on Windows {#numpy-numpy-24833-bug-importing-embedded-numpy-hangs-on-windows}

Source: https://github.com/numpy/numpy/issues/24833

Thread state: closed; merged: not applicable.

## Problem and constraints {#problem-and-constraints}
NumPy 1.22.2 import hangs inside an embedded Python 3.10.4 subinterpreter on Windows Server 2016, near longdouble discovery; Linux reportedly imports in a single subinterpreter. Reporter acknowledges subinterpreters are unsupported.

## Reasoning, alternatives, and revision sequence {#reasoning-alternatives-and-revision-sequence}
mattip and seberg initially suspect floating-point traps/host compiler state and suggest relevant prior cases and newer NumPy. Reporter says workarounds fail and 1.26.0 still hangs, then provides debug backtraces. ngoldbaum identifies NumPyOS_ascii_strtod_plain trying to acquire the GIL through NPY_ALLOW_C_API and requests inspecting the holder thread. Vincent later reports a temporary workaround: import NumPy immediately after pybind11 interpreter initialization on the main thread, before first releasing the GIL. seberg closes as apparently external embedding misuse; Vincent agrees it seems external but clarifies that reacquiring the GIL later still hangs, so his observation is more specific than simply forgetting to hold it.

## Implementation and attribution {#implementation-and-attribution}
Both original public attachment images were downloaded successfully and visually inspected. First shows PyCOND_TIMEDWAIT→take_gil→PyEval_RestoreThread→PyGILState_Ensure under _multiarray_umath. Second resolves NumPyOS_ascii_strtod_plain/strtod/strtold→npy_longdouble_from_PyLong→string_to_long_double→LONGDOUBLE_setitem→array construction. This supports a blocked GIL acquisition in the conversion path, not proof of a NumPy-internal root cause. Vincent’s three-line initialization-order snippet is a workaround, not a patch to NumPy. Images preserved in ../images/numpy-24833-stack1.png and stack2.png.

## Verification, outcome, and remaining limits {#verification-outcome-and-remaining-limits}
Closed without a general fix or full embedding reproducer. No holder-thread trace or controlled multithread/subinterpreter experiment appears. Main-thread pre-import should not be generalized into supported NumPy subinterpreter use; importing while holding the GIL remains required.

## Reusable decision and costs {#reusable-decision-and-costs}
When an import hangs in native code, inspect both the waiting stack and lock holder; distinguish floating-point host state, interpreter ownership and initialization order. Preserve unsuccessful workarounds and the reporter’s narrowing clarification rather than rewriting the history as the first maintainer hypothesis being confirmed.

## Evidence coverage {#evidence-coverage}
No upstream source was executed.

Cited source links:
- [mattip · 2023-09-29T08:04:42Z](https://github.com/numpy/numpy/issues/24833#issuecomment-1740478690).
- [car-bianco · 2023-09-29T08:32:29Z](https://github.com/numpy/numpy/issues/24833#issuecomment-1740513145).
- [mattip · 2023-09-29T08:50:29Z](https://github.com/numpy/numpy/issues/24833#issuecomment-1740535577).
- [seberg · 2023-09-29T10:20:54Z](https://github.com/numpy/numpy/issues/24833#issuecomment-1740656801).
- [car-bianco · 2023-10-02T07:59:36Z](https://github.com/numpy/numpy/issues/24833#issuecomment-1742562416).
- [ngoldbaum · 2023-10-02T16:17:28Z](https://github.com/numpy/numpy/issues/24833#issuecomment-1743317981).
- [wu-vincent · 2024-07-09T09:38:45Z](https://github.com/numpy/numpy/issues/24833#issuecomment-2217171053).
- [seberg · 2024-07-09T09:46:06Z](https://github.com/numpy/numpy/issues/24833#issuecomment-2217185185).
- [wu-vincent · 2024-07-09T09:49:47Z](https://github.com/numpy/numpy/issues/24833#issuecomment-2217192765).
