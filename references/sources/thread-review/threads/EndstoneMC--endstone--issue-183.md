<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:183"],"source_type":"public","date":"2025-05-18","topics":["concurrency","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-183-bug-unknown-error"></a>
# EndstoneMC/endstone #183: [bug] unknown error {#endstonemc-endstone-183-bug-unknown-error}

Source: https://github.com/EndstoneMC/endstone/issues/183

## Review scope and state {#review-scope-and-state}

- Thread author: graifc; state at review: closed; merged: not applicable.
- Evidence: The public issue and code/reproduction described below were reviewed statically; no code execution or tests were performed.
- Limits: Source snapshot only; no independent runtime verification.

## Engineering reading and attribution {#engineering-reading-and-attribution}

graifc supplies a Linux 0.8.1.dev3 SIGSEGV with a Python-bound Player string-returning call and asyncio frames but no reproducible code. Wu asks for reproduction, then closes with invitation to reopen when available. The stack is consistent with several possibilities, including invalid wrapper/lifecycle or thread use, but neither is established; it should not be silently merged into 182 or 181. No patch or diagnosis beyond suspected plugin Python involvement is supported.


## Source index {#source-index}

- https://github.com/EndstoneMC/endstone/issues/183
- https://github.com/EndstoneMC/endstone/issues/183#issuecomment-2889088795
- https://github.com/EndstoneMC/endstone/issues/183#issuecomment-2908089667
