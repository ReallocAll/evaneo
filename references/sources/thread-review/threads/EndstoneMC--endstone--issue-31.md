<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:31"],"source_type":"public","date":"2024-08-01","topics":["concurrency","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-31-feature-request-to-add-command-execution-result-to-the-return-value-of-server-dispatchcommand"></a>
# EndstoneMC/endstone #31: [feature] Request to add "command execution result" to the return value of "Server.dispatch_command" {#endstonemc-endstone-31-feature-request-to-add-command-execution-result-to-the-return-value-of-server-dispatchcommand}

Source: https://github.com/EndstoneMC/endstone/issues/31

## Review scope and state {#review-scope-and-state}

- Thread author: MengHanLOVE1027; state at review: closed; merged: not applicable.
- Evidence: The public issue and code/reproduction described below were reviewed statically; no code execution or tests were performed.
- Limits: Source snapshot only; no independent runtime verification.

## Engineering reading and attribution {#engineering-reading-and-attribution}

MengHanLOVE1027 needs /save query output after /save hold for backup-file paths/sizes and proposes a dispatch_command result. Wu later identifies CommandSenderWrapper with message/error callbacks as the implemented alternative. Wrapping preserves the sender while collecting output without redefining dispatcher return values. Synchronous behavior, raw versus translated output and structured save-query data are unspecified; linked 3ff6d42109819f34070ec43650df55bda44ed395 has not been inspected here.


## Source index {#source-index}

- https://github.com/EndstoneMC/endstone/issues/31
- https://github.com/EndstoneMC/endstone/issues/31#issuecomment-2323496330
- https://github.com/EndstoneMC/endstone/issues/31#issuecomment-2336823472
- https://github.com/EndstoneMC/endstone/issues/31#issuecomment-2397263295
- https://github.com/EndstoneMC/endstone/commit/3ff6d42109819f34070ec43650df55bda44ed395
