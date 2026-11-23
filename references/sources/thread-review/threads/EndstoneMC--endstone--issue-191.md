<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:191"],"source_type":"public","date":"2025-05-31","topics":["concurrency","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-191-bug-funchookerroriprelativeoffset-error-when-attempting-to-start-container"></a>
# EndstoneMC/endstone #191: [bug] FUNCHOOK_ERROR_IP_RELATIVE_OFFSET error when attempting to start container {#endstonemc-endstone-191-bug-funchookerroriprelativeoffset-error-when-attempting-to-start-container}

Source: https://github.com/EndstoneMC/endstone/issues/191

## Review scope and state {#review-scope-and-state}

- Thread author: fosrox; state at review: closed; merged: not applicable.
- Evidence: The public issue and code/reproduction described below were reviewed statically; no code execution or tests were performed.
- Limits: Source snapshot only; no independent runtime verification.

## Engineering reading and attribution {#engineering-reading-and-attribution}

fosrox reports an IP-relative-hook error in Docker on Unraid despite trying privileged/seccomp/permission adjustments. Wu suggests possible duplicate 167-style BDS mismatch, with historical 0.8.0/1.21.80 and 0.8.1/1.21.82 mapping. Crucially the reporter then verifies 1.21.82 in version.txt and says the identical Docker command succeeds on another PC but fails on the server. This counterevidence leaves the suggested cause unresolved; do not turn it into a confirmed version mismatch or conclude disabling sandboxing fixes it. A version marker is not a binary checksum, but no further binary/CPU/kernel investigation is supplied.


## Source index {#source-index}

- https://github.com/EndstoneMC/endstone/issues/191
- https://github.com/EndstoneMC/endstone/issues/191#issuecomment-2930712226
- https://github.com/EndstoneMC/endstone/issues/191#issuecomment-2931407757
