<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:148"],"source_type":"public","date":"2025-03-05","topics":["concurrency","documentation","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-148-no-logs-isn-t-running-on-linux"></a>
# EndstoneMC/endstone #148: No logs, isn't running on linux {#endstonemc-endstone-148-no-logs-isn-t-running-on-linux}

Source: https://github.com/EndstoneMC/endstone/issues/148

## Review scope and state {#review-scope-and-state}

- Thread author: Mih4n; state at review: closed; merged: not applicable.
- Evidence: The public issue and code/reproduction described below were reviewed statically; no code execution or tests were performed.
- Limits: Source snapshot only; no independent runtime verification.

## Engineering reading and attribution {#engineering-reading-and-attribution}

Mih4n's plugin loads on Windows but Linux reports an empty exception message. Wu supplies the import traceback: module import creates WLStorage, configuration lookup checks a missing path and raises bare Exception(). The missing error text is therefore explained by exception construction, while the traceback identifies the plugin's configuration existence check as the failing operation. The reporter acknowledges understanding. This supports retaining traceback context even when str(exception) is empty and avoiding a platform/framework diagnosis based only on a blank log. The third-party repository was not independently audited; no Endstone patch appears here.


## Source index {#source-index}

- https://github.com/EndstoneMC/endstone/issues/148
- https://github.com/EndstoneMC/endstone/issues/148#issuecomment-2701566076
- https://github.com/EndstoneMC/endstone/issues/148#issuecomment-2702069767
- https://github.com/EndstoneMC/endstone/issues/148#issuecomment-2702111582
