<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:190"],"source_type":"public","date":"2025-05-28","topics":["concurrency","testing","api","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-190-bug-ban-command-error"></a>
# EndstoneMC/endstone #190: [bug] /ban command error {#endstonemc-endstone-190-bug-ban-command-error}

Source: https://github.com/EndstoneMC/endstone/issues/190

## Review scope and state {#review-scope-and-state}

- Thread author: Arduinonk; state at review: closed; merged: not applicable.
- Evidence: The public issue and code/reproduction described below were reviewed statically; no code execution or tests were performed.
- Limits: Source snapshot only; no independent runtime verification.

## Engineering reading and attribution {#engineering-reading-and-attribution}

Arduinonk demonstrates quoted multiword names truncated by ban after the command refactor. Wu confirms a regression introduced by 180 and links test commit2361546b2cd3ff1e0b7a3816b128e5a294b1c8e1 in endstone-test. Full test patch inspected: add a multiword banned name via API, unban through quoted command; ban through command with quoted name and multiword colon-containing reason, assert exact name/reason, then remove via API. This tests parsing across both API/command boundaries and cleanup, not just a return code. Test names are opposite the principal command paths, and no run result is present. The tests establish intended protection but are not themselves the implementation fix.


## Source index {#source-index}

- https://github.com/EndstoneMC/endstone/issues/190
- https://github.com/EndstoneMC/endstone/issues/190#issuecomment-2916767364
- https://github.com/EndstoneMC/endstone/issues/190#issuecomment-2916896618
