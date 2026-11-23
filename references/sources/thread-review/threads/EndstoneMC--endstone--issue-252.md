<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:252"],"source_type":"public","date":"2025-08-24","topics":["concurrency","ffi","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-252-bug-error-occurred-when-trying-to-register-a-plugin-loader-typeerror-metadatapathfinder-invalidatecaches-m"></a>
# EndstoneMC/endstone #252: [bug] Error occurred when trying to register a plugin loader: TypeError: MetadataPathFinder.invalidate_caches() missing 1 required positional argument: 'cls' {#endstonemc-endstone-252-bug-error-occurred-when-trying-to-register-a-plugin-loader-typeerror-metadatapathfinder-invalidatecaches-m}

Source: https://github.com/EndstoneMC/endstone/issues/252

## Review scope and state {#review-scope-and-state}

- Thread author: FalkRaft; state at review: closed; merged: not applicable.
- Evidence: The public issue and code/reproduction described below were reviewed statically; no code execution or tests were performed.
- Limits: Source snapshot only; no independent runtime verification.

## Engineering reading and attribution {#engineering-reading-and-attribution}

FalkRaft's fresh Codespace 0.10.4 startup fails registering a Python plugin loader: importlib.invalidate_caches reaches MetadataPathFinder.invalidate_caches with missing cls, then an uncaught pybind11 error aborts native startup. Vanilla BDS runs. Wu suggests a specific Python-version bug and trying another interpreter; no dependency versions, reproducer package set, or successful retest establishes that hypothesis. The evidence distinguishes an actionable Python metadata/cache exception from the subsequent SIGABRT and repetitive crashpad noise. No private Codespace content was accessed.


## Source index {#source-index}

- https://github.com/EndstoneMC/endstone/issues/252
- https://github.com/EndstoneMC/endstone/issues/252#issuecomment-3218241767
- https://github.com/EndstoneMC/endstone/issues/252#issuecomment-3220153396
