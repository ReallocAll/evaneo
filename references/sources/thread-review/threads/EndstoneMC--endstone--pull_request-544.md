<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:544"],"source_type":"public","date":"2026-10-06","topics":["ffi","testing","performance","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-544-fix-redstone-drop-a-power-source-s-links-to-blocks-that-are-gone"></a>
# EndstoneMC/endstone #544: fix(redstone): drop a power source's links to blocks that are gone {#endstonemc-endstone-544-fix-redstone-drop-a-power-source-s-links-to-blocks-that-are-gone}

Source: https://github.com/EndstoneMC/endstone/pull/544

## Evidence and attribution {#evidence-and-attribution}

Primary author: wu-vincent. Created 2026-10-06T13:00:57Z; recorded state closed; merged True.

## Repair stale relationships before the native walk {#repair-stale-relationships-before-the-native-walk}
Wu documents a native redstone leak independently of LeviOptimize's earlier fix: pending relinks skip entries whose component is gone, then lazily create replacement components, appending more32-byte stale entries. Repeated break/place grows scans; eventual per-entry vector erase is quadratic and keeps capacity. Windows/Linux disassembly and symbol-bearing Android ordering support remove→pending-add→pending-update timing.
The chosen pre-pass on public CircuitSceneGraph::update bulk-erases only positions absent from both live components and pending adds, then invokes native code for all live unlinking. It never dereferences dangling component pointers. Components removed later in the same tick can retain one entry until the next relink. This minimizes copied native behavior and avoids hooking a function now inlined away. Wu identifies erase-then-dereference-next/end defects in cited LeviOptimize08cd382, later removedb353eb9; these third-party claims need independent source inspection before being treated as audited findings.
100-torch150-cycle headless tests on Windows and Linux reportedly keep497 entries versus30,347; lamp state matches. Heavy1000-torch600-cycle Windows benchmark reports1.745m versus7,790 entries, end cost1.61→0.34ms/tick, worst clear422→4.5ms, memory1264→1351MB versus1263→1274MB. Pre-pass6–10ms per10s is included; heavy synthetic scene is not a universal gameplay benefit.67/67 symbols, builds and format checks claimed; no real-client run. Layout asserts408Windows/264Linux and finite version scan are important portability boundaries.

## Direct patch findings {#direct-patch-findings}

All code matches narrow pre-pass: iterate pending_updates values, locate power_association_map by position, erase entries absent from both all_components and pending_adds, then original update. Layouts reconstruct maps/pending entries with408/264 and item32/vector24 assertions. Adds exact symbol recipes/addresses plus CMake source and changelog. No test or benchmark harness committed, so source-reported measurements remain unaudited experiments.

## Code and verification boundary {#code-and-verification-boundary}

Inspected every hunk of captured PR diff (10515 characters; SHA-256 480cf8c47ccb04f45c176a299d6ee280c5fef0e51554e363a59f383c9193838a), head c5e17e0f9f15e4c149b4c7ca44ff13388ecb88f4. Scope is this supplied patch, not all linked implementation history. No upstream code was executed and no tests were run in this review. Runtime assertions are source-reported unless explicitly identified as static code findings.

## Traceability {#traceability}


- https://github.com/EndstoneMC/endstone/pull/544
