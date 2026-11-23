<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:311"],"source_type":"public","date":"2025-12-11","topics":["testing","build","diagnosis","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-311-nautilus-causes-endstone-crash"></a>
# EndstoneMC/endstone #311: Nautilus causes Endstone crash {#endstonemc-endstone-311-nautilus-causes-endstone-crash}

Source: https://github.com/EndstoneMC/endstone/issues/311

## Evidence and attribution {#evidence-and-attribution}

Primary author: PrimeStrat. Created 2025-12-11T16:49:23Z; recorded state closed; merged not applicable.

## Failure and investigation sequence {#failure-and-investigation-sequence}

PrimeStrat reported an exit when spawning a nautilus. wu-vincent initially reproduced only on Windows, but the reporter corrected that the original was Linux and supplied Linux 1.21.130.4 crash output. wu-vincent acknowledged both platforms, then identified nautilus dehydration as a new damage type missing from Endstone handling.

A development build was offered. The reporter thought the Windows build had failed to compile; wu-vincent clarified that it was an HTTP failure, retried the action, and asked for retesting once ready. PrimeStrat confirmed both Windows and Linux worked on the development build and latest release.

## Reusable decision and verification limits {#reusable-decision-and-verification-limits}

New game entities can expose enum/domain expansion through ordinary gameplay before a version port is complete. Treat cross-platform evidence separately from initial reproduction assumptions, and distinguish infrastructure build failure from compiler failure. The thread contains a two-platform user verification, but no patch or automated regression test is included.

## Code and verification boundary {#code-and-verification-boundary}

No code inspection required for the narrow discussion finding; no implementation claim independently verified. No upstream code was executed and no tests were run in this review. Runtime assertions are source-reported unless explicitly identified as static code findings.

## Traceability {#traceability}


- https://github.com/EndstoneMC/endstone/issues/311
- https://github.com/EndstoneMC/endstone/issues/311#issuecomment-3642891266
- https://github.com/EndstoneMC/endstone/issues/311#issuecomment-3642903252
- https://github.com/EndstoneMC/endstone/issues/311#issuecomment-3642909943
- https://github.com/EndstoneMC/endstone/issues/311#issuecomment-3642977676
- https://github.com/EndstoneMC/endstone/issues/311#issuecomment-3643097425
- https://github.com/EndstoneMC/endstone/issues/311#issuecomment-3643116209
- https://github.com/EndstoneMC/endstone/issues/311#issuecomment-3643118513
- https://github.com/EndstoneMC/endstone/issues/311#issuecomment-3643143202
- https://github.com/EndstoneMC/endstone/issues/311#issuecomment-3643150634
- https://github.com/EndstoneMC/endstone/issues/311#issuecomment-3643432386
- https://github.com/EndstoneMC/endstone/issues/311#issuecomment-3644693970
