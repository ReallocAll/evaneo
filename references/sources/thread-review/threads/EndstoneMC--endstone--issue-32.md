<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:32"],"source_type":"public","date":"2024-08-05","topics":["lifetime","concurrency","testing","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-32-bug-creating-a-form-without-a-on-submit-callback-crashes-the-server"></a>
# EndstoneMC/endstone #32: [bug] Creating a form without a on submit callback crashes the server {#endstonemc-endstone-32-bug-creating-a-form-without-a-on-submit-callback-crashes-the-server}

Source: https://github.com/EndstoneMC/endstone/issues/32

## Review scope and state {#review-scope-and-state}

- Thread author: zSALLAZAR; state at review: closed; merged: not applicable.
- Evidence: The public issue and code/reproduction described below were reviewed statically; no code execution or tests were performed.
- Limits: Source snapshot only; no independent runtime verification.

## Engineering reading and attribution {#engineering-reading-and-attribution}

zSALLAZAR reports ActionForm submission without a callback crashes. Wu first cannot reproduce, then reproduces the supplied temporary-form expression and links 89058cdf750c02f8eb9e71cd976ab452ab47af30. The inspected fix removes the constructor lambda capturing this, defaults the constructor and dispatches button callbacks inside onFormResponse using the stored form, checking callbacks and selection bounds. A stale this after temporary copying is an inference from that change, not a diagnosis stated in the thread. Submit now runs before button access, so broader reentrancy/lifetime safety is not proven. Wu reports a fix and impending release, not a test result independently verified here.


## Source index {#source-index}

- https://github.com/EndstoneMC/endstone/issues/32
- https://github.com/EndstoneMC/endstone/issues/32#issuecomment-2269884655
- https://github.com/EndstoneMC/endstone/issues/32#issuecomment-2269899268
- https://github.com/EndstoneMC/endstone/issues/32#issuecomment-2269918087
- https://github.com/EndstoneMC/endstone/issues/32#issuecomment-2269990520
- https://github.com/EndstoneMC/endstone/commit/89058cdf750c02f8eb9e71cd976ab452ab47af30
