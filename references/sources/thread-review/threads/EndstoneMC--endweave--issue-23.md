<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endweave:23"],"source_type":"public","date":"2026-05-07","topics":["testing","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endweave-23-craftingdata"></a>
# EndstoneMC/endweave #23: CraftingDATA {#endstonemc-endweave-23-craftingdata}

Source: https://github.com/EndstoneMC/endweave/issues/23

## Evidence and attribution {#evidence-and-attribution}

Primary author: DayOfMagic. Created 2026-05-07T10:19:01Z; recorded state closed; merged not applicable.

CraftingData translation944→975 fails when enum UnlockingContext reads202, traced through shaped-recipe requirement decoding. Wu requests upgrading0.4.2, reproducing and sending binary packet data. An invalid enum can reflect offset/schema desynchronization; no final cause is demonstrated and no dump supplied in captured text. Public player/address identifiers in logs are irrelevant to engineering and omitted.

## Code and verification boundary {#code-and-verification-boundary}

No code inspection required for the narrow discussion finding; no implementation claim independently verified. No upstream code was executed and no tests were run in this review. Runtime assertions are source-reported unless explicitly identified as static code findings.

## Traceability {#traceability}


- https://github.com/EndstoneMC/endweave/issues/23
- https://github.com/EndstoneMC/endweave/issues/23#issuecomment-4401831048
