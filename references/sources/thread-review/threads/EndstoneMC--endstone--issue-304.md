<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:304"],"source_type":"public","date":"2025-11-25","topics":["lifetime","concurrency","testing","api","documentation","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-304-feature-async-config-sqlite-api"></a>
# EndstoneMC/endstone #304: [feature] Async Config/SQLite API {#endstonemc-endstone-304-feature-async-config-sqlite-api}

Source: https://github.com/EndstoneMC/endstone/issues/304

## Evidence and attribution {#evidence-and-attribution}

Primary author: emmagine. Created 2025-11-25T10:53:47Z; recorded state closed; merged not applicable.

## Problem, alternatives, and ownership {#problem-alternatives-and-ownership}

emmagine wanted a beginner-friendly asynchronous config/SQLite API, citing PocketMine Config. zevlaoxie2010 proposed standard Python SQLite; the reporter objected that it is not itself asynchronous and that beginners repeatedly reopen connections rather than managing one across enable/disable.

wu-vincent chose a general asyncio helper (described as running each coroutine on a separate thread in the next version) and possible documentation examples instead of incorporating one database backend. Different plugin authors need different storage systems. Connection lifecycle correctness remains the plugin author's responsibility rather than something core should hide.

## Reusable decision and costs {#reusable-decision-and-costs}

Centralize reusable async execution, leave backend-specific persistence and data handling at the plugin boundary. This reduces core coupling but keeps a learning/documentation burden on plugin authors. No helper code or performance/safety tests are present; the thread's description should not be read as a verified threading contract for current versions.

## Code and verification boundary {#code-and-verification-boundary}

No code inspection required for the narrow discussion finding; no implementation claim independently verified. No upstream code was executed and no tests were run in this review. Runtime assertions are source-reported unless explicitly identified as static code findings.

## Traceability {#traceability}


- https://github.com/EndstoneMC/endstone/issues/304
- https://github.com/EndstoneMC/endstone/issues/304#issuecomment-3575183229
- https://github.com/EndstoneMC/endstone/issues/304#issuecomment-3575455955
- https://github.com/EndstoneMC/endstone/issues/304#issuecomment-3760394477
