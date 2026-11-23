<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:235"],"source_type":"public","date":"2025-08-04","topics":["concurrency","ffi","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-235-bug-custom-block-bug"></a>
# EndstoneMC/endstone #235: [bug] custom block bug {#endstonemc-endstone-235-bug-custom-block-bug}

Source: https://github.com/EndstoneMC/endstone/issues/235

## Review scope and state {#review-scope-and-state}

- Thread author: pgrd1; state at review: closed; merged: not applicable.
- Evidence: The public issue and code/reproduction described below were reviewed statically; no code execution or tests were performed.
- Limits: Source snapshot only; no independent runtime verification.

## Engineering reading and attribution {#engineering-reading-and-attribution}

pgrd1 reports Linux 0.10.1 custom-block interaction crashes, later narrows the plugin call to event.item.type. The symbolized stack reaches pybind11 polymorphic ItemType casting during PlayerInteractEvent; the supplied block includes custom tick component, light/loot settings and a nonstandard identifier. Wu initially cannot reproduce on 0.10.3 and requests the full RP/BP/plugin combination; reporter says Windows does not reproduce and supplies only block JSON. Wu later says the latest dev build should fix it, without an exact link or user confirmation. Thus a custom-item registry/binding failure is plausible, but malformed identifier, specific component, or platform ABI cannot be established as the cause from this thread. All long stack text and comments were read; unrelated crashpad diagnostics were not mistaken for the initial fault.


## Source index {#source-index}

- https://github.com/EndstoneMC/endstone/issues/235
- https://github.com/EndstoneMC/endstone/issues/235#issuecomment-3151322737
- https://github.com/EndstoneMC/endstone/issues/235#issuecomment-3151347884
- https://github.com/EndstoneMC/endstone/issues/235#issuecomment-3151568754
- https://github.com/EndstoneMC/endstone/issues/235#issuecomment-3172605759
- https://github.com/EndstoneMC/endstone/issues/235#issuecomment-3172734725
- https://github.com/EndstoneMC/endstone/issues/235#issuecomment-3268387163
