<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:395"],"source_type":"public","date":"2026-05-19","topics":["lifetime","ffi","testing","diagnosis","review","networking"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-395-fix-network-guard-closeconnection-against-double-onconnectionclosed-dispatch"></a>
# EndstoneMC/endstone #395: fix(network): guard closeConnection against double onConnectionClosed dispatch {#endstonemc-endstone-395-fix-network-guard-closeconnection-against-double-onconnectionclosed-dispatch}

Source: https://github.com/EndstoneMC/endstone/pull/395

## Evidence and attribution {#evidence-and-attribution}

Primary author: gamezaSRC. Created 2026-05-19T00:10:48Z; recorded state closed; merged True.

## Failure and initial proposal {#failure-and-initial-proposal}

gamezaSRC reported natural disconnect crashes, much easier after /reload. Their diagnosis was duplicate onConnectionClosed: native transport already tears down the connection, then Endstone's post-original disconnect hook immediately closes it again. Reload reinitializes Script API listeners, increasing stale-object exposure. The initial proposed guard checked the connection exists and is not already marked closing, preserving forced disconnection for malicious clients that ignore kick messages.

## Revision resolved by code {#revision-resolved-by-code}

wu-vincent's comment says he changed approach so only a flag is set and the server loop owns teardown. Its sentence accidentally reverses closeConnection and setCloseConnection names. The final patch is unambiguous: the hook calls setCloseConnection(id), which looks up the connection, sets should_close_connection_=true and stamps closed_time with steady_clock. It adds friendship to access the native field. Thus a single lifecycle owner performs eventual transport closure and callback dispatch.

## Verification and reusable rule {#verification-and-reusable-rule}

The PR body lists natural-disconnect, post-reload and kick/ban checks as successful scenarios; no logs or automated tests accompany them. Credit gamezaSRC for diagnosis/proposal and wu-vincent for the final deferred-close revision. Prefer idempotent intent marking over duplicating lifecycle callbacks on already-closing objects, and use final code to resolve contradictory prose.

## Code and verification boundary {#code-and-verification-boundary}

Inspected complete 1,468-character final patch, including setCloseConnection implementation and call-site replacement. No upstream code was executed and no tests were run in this review. Runtime assertions are source-reported unless explicitly identified as static code findings.

## Traceability {#traceability}


- https://github.com/EndstoneMC/endstone/pull/395
- https://github.com/EndstoneMC/endstone/pull/395#issuecomment-4604277723
