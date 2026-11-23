<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:134"],"source_type":"public","date":"2025-02-18","topics":["concurrency","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-134-sudden-server-stop"></a>
# EndstoneMC/endstone #134: Sudden Server Stop {#endstonemc-endstone-134-sudden-server-stop}

Source: https://github.com/EndstoneMC/endstone/issues/134

## Review scope and state {#review-scope-and-state}

- Thread author: PrimeStrat; state at review: closed; merged: not applicable.
- Evidence: The public issue and code/reproduction described below were reviewed statically; no code execution or tests were performed.
- Limits: Source snapshot only; no independent runtime verification.

## Engineering reading and attribution {#engineering-reading-and-attribution}

PrimeStrat’s dev263 server stops without a crash trace. Initial clean-install/pack isolation does not establish a cause. yuhangle reproduces with Python 3.13 and a thread-shutdown SystemError. Wu then reproduces only GitHub Actions artifacts, while local builds work, and links 888c0ad9739893b0df43a83ab69eb0a3f8037f7a for dev268. This narrows the fault to build/artifact differences rather than user world data. Closure is wu’s expectation; no reporter confirmation follows.


## Source index {#source-index}

- https://github.com/EndstoneMC/endstone/issues/134
- https://github.com/EndstoneMC/endstone/issues/134#issuecomment-2665380982
- https://github.com/EndstoneMC/endstone/issues/134#issuecomment-2666204556
- https://github.com/EndstoneMC/endstone/issues/134#issuecomment-2666516690
- https://github.com/EndstoneMC/endstone/issues/134#issuecomment-2667529654
- https://github.com/EndstoneMC/endstone/issues/134#issuecomment-2668636239
- https://github.com/EndstoneMC/endstone/issues/134#issuecomment-2669297248
- https://github.com/EndstoneMC/endstone/issues/134#issuecomment-2670098354
- https://github.com/EndstoneMC/endstone/commit/888c0ad9739893b0df43a83ab69eb0a3f8037f7a
