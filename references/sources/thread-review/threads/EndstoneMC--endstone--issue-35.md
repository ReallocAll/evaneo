<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:35"],"source_type":"public","date":"2024-08-15","topics":["concurrency","testing","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-35-bug-unable-to-start-the-server"></a>
# EndstoneMC/endstone #35: [bug]Unable to start the server {#endstonemc-endstone-35-bug-unable-to-start-the-server}

Source: https://github.com/EndstoneMC/endstone/issues/35

## Review scope and state {#review-scope-and-state}

- Thread author: Monarchdos; state at review: closed; merged: not applicable.
- Evidence: The public issue and code/reproduction described below were reviewed statically; no code execution or tests were performed.
- Limits: Source snapshot only; no independent runtime verification.

## Engineering reading and attribution {#engineering-reading-and-attribution}

Monarchdos cannot start via pip or Docker. Wu first suspects stale incompatible BDS binaries and asks to test without a volume mount. That works, but the reporter contradicts the stale-directory explanation with an empty-folder reproduction. Wu acknowledges the anomaly, cannot reproduce and requests system details (WSL kernel, Python 3.10). A later Windows failure has an access-denied dialog; wu separates it as filesystem permissions and suggests portable distribution. There is no confirmed single root cause for the Linux mount failure. Preserve the disconfirmed initial hypothesis; closure invites reopening and is not a verified fix. Image-only error details were not inspected.


## Source index {#source-index}

- https://github.com/EndstoneMC/endstone/issues/35
- https://github.com/EndstoneMC/endstone/issues/35#issuecomment-2290744070
- https://github.com/EndstoneMC/endstone/issues/35#issuecomment-2290747097
- https://github.com/EndstoneMC/endstone/issues/35#issuecomment-2290747559
- https://github.com/EndstoneMC/endstone/issues/35#issuecomment-2290752718
- https://github.com/EndstoneMC/endstone/issues/35#issuecomment-2290782786
- https://github.com/EndstoneMC/endstone/issues/35#issuecomment-2290784943
- https://github.com/EndstoneMC/endstone/issues/35#issuecomment-2290786305
- https://github.com/EndstoneMC/endstone/issues/35#issuecomment-2290796283
- https://github.com/EndstoneMC/endstone/issues/35#issuecomment-2290840058
- https://github.com/EndstoneMC/endstone/issues/35#issuecomment-2292324299
- https://github.com/EndstoneMC/endstone/issues/35#issuecomment-2292539353
- https://github.com/EndstoneMC/endstone/issues/35#issuecomment-2293376428
- https://github.com/EndstoneMC/endstone/issues/35#issuecomment-2293742257
- https://github.com/EndstoneMC/endstone/issues/35#issuecomment-2293803801
- https://github.com/EndstoneMC/endstone/issues/35#issuecomment-2293807838
- https://github.com/EndstoneMC/endstone/issues/35#issuecomment-2307177179
