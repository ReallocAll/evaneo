<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:380"],"source_type":"public","date":"2026-04-15","topics":["lifetime","ffi","testing","api","review","selection"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-380-plain-c-abi"></a>
# EndstoneMC/endstone #380: Plain C ABI {#endstonemc-endstone-380-plain-c-abi}

Source: https://github.com/EndstoneMC/endstone/issues/380

## Evidence and attribution {#evidence-and-attribution}

Primary author: Mih4n. Created 2026-04-15T07:58:24Z; recorded state closed; merged not applicable.

## Need, rejected alternative and chosen direction {#need-rejected-alternative-and-chosen-direction}

Mih4n requested a separate stable extern-C/POD/opaque-handle API with explicit ownership and callbacks to enable ClangSharp/C#/Rust interoperability without every consumer writing wrappers. The proposed separation aimed to let the C++ API evolve independently.

wu-vincent rejected maintaining a second flattened API: templates, RAII, Result, smart pointers and containers would become a large lossy surface requiring synchronization, while language-specific wrappers would still exist. He preferred each embedded language's C embedding API with a C++ bridge directly into Endstone, using CPython+pybind11 as the model.

## Applicability and caveats {#applicability-and-caveats}

The maintenance tradeoff is explicit and useful for an actively evolving C++ plugin API. It is not a general proof that stable C ABIs are bad or that Rust/C# cannot interoperate/embed. The response's broad classification of C# and Rust as AOT/native rather than embeddable runtimes oversimplifies their ecosystems; direct consumption of C++ headers still needs ABI/FFI tooling. No prototype or cost measurement tests either alternative. The requester accepted the explanation and no C layer is planned.

## Code and verification boundary {#code-and-verification-boundary}

No code inspection required for the narrow discussion finding; no implementation claim independently verified. No upstream code was executed and no tests were run in this review. Runtime assertions are source-reported unless explicitly identified as static code findings.

## Traceability {#traceability}


- https://github.com/EndstoneMC/endstone/issues/380
- https://github.com/EndstoneMC/endstone/issues/380#issuecomment-4604465047
- https://github.com/EndstoneMC/endstone/issues/380#issuecomment-4604588383
