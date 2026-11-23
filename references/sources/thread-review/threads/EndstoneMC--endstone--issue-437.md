<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:437"],"source_type":"public","date":"2026-07-17","topics":["testing","build","diagnosis","review","selection"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-437-bug-std-format-with-identifier-t-fails-to-compile-on-clang-18-libc-registry-h-itemstack-h"></a>
# EndstoneMC/endstone #437: [Bug] std::format with Identifier<T> fails to compile on Clang 18 + libc++ (registry.h, item_stack.h) {#endstonemc-endstone-437-bug-std-format-with-identifier-t-fails-to-compile-on-clang-18-libc-registry-h-itemstack-h}

Source: https://github.com/EndstoneMC/endstone/issues/437

## Evidence and attribution {#evidence-and-attribution}

Primary author: dyan1619. Created 2026-07-17T03:46:28Z; recorded state closed; merged not applicable.

## Compiler-portability report and alternative {#compiler-portability-report-and-alternative}

dyan1619 provided Clang 18/libc++18/C++20 build commands and complete diagnostics showing Identifier<ItemType>/Identifier<BlockType> rejected by std::format in public item_stack and registry headers. The full plugin was used rather than a minimized reproducer. The reporter suggested explicit string conversion at call sites.

wu-vincent says the v0.11 fix instead changes public formatter specializations to deduced return types and was verified with clang 18.1.0 -stdlib=libc++. That keeps formatting support centralized rather than patching every use. The thread has no linked commit or actual formatter patch, so this review preserves the reported diagnosis and compiler result without certifying exact implementation or broad toolchain compatibility.

## Code and verification boundary {#code-and-verification-boundary}

No code inspection required for the narrow discussion finding; no implementation claim independently verified. No upstream code was executed and no tests were run in this review. Runtime assertions are source-reported unless explicitly identified as static code findings.

## Traceability {#traceability}


- https://github.com/EndstoneMC/endstone/issues/437
- https://github.com/EndstoneMC/endstone/issues/437#issuecomment-5079074375
