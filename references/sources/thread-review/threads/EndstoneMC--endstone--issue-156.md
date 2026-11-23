<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:156"],"source_type":"public","date":"2025-03-15","topics":["concurrency","ffi","diagnosis","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-156-bug-unknown-crash"></a>
# EndstoneMC/endstone #156: [bug] Unknown crash {#endstonemc-endstone-156-bug-unknown-crash}

Source: https://github.com/EndstoneMC/endstone/issues/156

## Review scope and state {#review-scope-and-state}

- Thread author: SuperEric1; state at review: closed; merged: not applicable.
- Evidence: The public issue and code/reproduction described below were reviewed statically; no code execution or tests were performed.
- Limits: Source snapshot only; no independent runtime verification.

## Engineering reading and attribution {#engineering-reading-and-attribution}

SuperEric1 reports Linux startup crashes with no plugins and one development behavior pack, then isolates a particular addon script but offers its source only by private contact. Wu states the crash should be resolved in 0.7.0; there is no public reproducer, linked patch, or reporter retest here. The native stack passes through Endstone's tick wrapper, which by itself does not locate the fault. Related issue 165 explicitly attributes reload crashes to the same scripting-event-hook problem, but this remains a maintainer correlation rather than a reproduced equivalence. Private script content was neither requested nor inferred.


## Source index {#source-index}

- https://github.com/EndstoneMC/endstone/issues/156
- https://github.com/EndstoneMC/endstone/issues/156#issuecomment-2726966174
- https://github.com/EndstoneMC/endstone/issues/156#issuecomment-2752136927
