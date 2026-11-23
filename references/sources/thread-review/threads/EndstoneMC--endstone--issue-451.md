<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:451"],"source_type":"public","date":"2026-07-30","topics":["testing","diagnosis","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-451-strange-level-crash"></a>
# EndstoneMC/endstone #451: Strange Level Crash {#endstonemc-endstone-451-strange-level-crash}

Source: https://github.com/EndstoneMC/endstone/issues/451

## Evidence and attribution {#evidence-and-attribution}

Primary author: PrimeStrat. Created 2026-07-30T21:11:24Z; recorded state closed; merged not applicable.

Custom dimension plus reload produces unresolved vanilla-tick crashes and missing dimension registration. Wu explains that registration may depend on player-tick/spawn-chunk activation, requiring an online player in the custom dimension; Endstone reload invokes native reload plus its own commands/plugins/registries, not a new dimension lifecycle. Old-version evidence did not establish a current defect or a fix. Closed with a request for a current minimal pack. Similar outer Level::tick frames are not proof this shares #539's scoreboard cause.

## Code and verification boundary {#code-and-verification-boundary}

No code inspection required for the narrow discussion finding; no implementation claim independently verified. No upstream code was executed and no tests were run in this review. Runtime assertions are source-reported unless explicitly identified as static code findings.

## Traceability {#traceability}


- https://github.com/EndstoneMC/endstone/issues/451
- https://github.com/EndstoneMC/endstone/issues/451#issuecomment-5148369977
- https://github.com/EndstoneMC/endstone/issues/451#issuecomment-6252279832
