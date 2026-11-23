<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:288"],"source_type":"public","date":"2025-10-29","topics":["concurrency","diagnosis","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-288-bug-crash-on-could-not-connect-to-minecraft-services-stop-request"></a>
# EndstoneMC/endstone #288: [bug] Crash on "Could not connect to Minecraft services" stop request {#endstonemc-endstone-288-bug-crash-on-could-not-connect-to-minecraft-services-stop-request}

Source: https://github.com/EndstoneMC/endstone/issues/288

## Review scope and state {#review-scope-and-state}

- Thread author: MisledWater79; state at review: closed; merged: not applicable.
- Evidence: The public issue and code/reproduction described below were reviewed statically; no code execution or tests were performed.
- Limits: Source snapshot only; no independent runtime verification.

## Engineering reading and attribution {#engineering-reading-and-attribution}

MisledWater79 reports Linux 0.10.8 failure after a Minecraft-services connection-stop request. The stack is a Python getOnlineMode call through Minecraft::getServerNetworkHandler and GameSession pointer access; this points to a server-state/lifecycle access path rather than proving the external service outage itself caused memory corruption. Wu states fixed in 0.10.10, no linked patch/retest. Retain the distinction between the external trigger and robust shutdown/access behavior expected locally.


## Source index {#source-index}

- https://github.com/EndstoneMC/endstone/issues/288
- https://github.com/EndstoneMC/endstone/issues/288#issuecomment-3463110673
- https://github.com/EndstoneMC/endstone/issues/288#issuecomment-3476742039
