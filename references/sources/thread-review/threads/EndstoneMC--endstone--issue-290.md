<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:290"],"source_type":"public","date":"2025-11-01","topics":["concurrency","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-290-endstoneruntime-dll-error-1114"></a>
# EndstoneMC/endstone #290: endstone_runtime.dll Error 1114 {#endstonemc-endstone-290-endstoneruntime-dll-error-1114}

Source: https://github.com/EndstoneMC/endstone/issues/290

## Review scope and state {#review-scope-and-state}

- Thread author: xXLarryTFVWXx; state at review: closed; merged: not applicable.
- Evidence: The public issue and code/reproduction described below were reviewed statically; no code execution or tests were performed.
- Limits: Source snapshot only; no independent runtime verification.

## Engineering reading and attribution {#engineering-reading-and-attribution}

xXLarryTFVWXx reports Windows DLL 1114 after Python 3.11→3.14 and manual BDS download with Endstone 0.10.7. Wu suggests latest VC redistributable; reporter updates both it and Endstone and confirms success. Because two variables changed, the result does not isolate the VC runtime as sole cause or prove Python 3.14 incompatibility. No patch or binary identity comparison is supplied.


## Source index {#source-index}

- https://github.com/EndstoneMC/endstone/issues/290
- https://github.com/EndstoneMC/endstone/issues/290#issuecomment-3476941352
- https://github.com/EndstoneMC/endstone/issues/290#issuecomment-3483266151
