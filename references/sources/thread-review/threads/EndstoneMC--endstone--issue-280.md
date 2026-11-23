<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:280"],"source_type":"public","date":"2025-10-21","topics":["concurrency","ffi","testing","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-280-feature-disable-endstone-default-commands"></a>
# EndstoneMC/endstone #280: [feature] Disable Endstone default commands {#endstonemc-endstone-280-feature-disable-endstone-default-commands}

Source: https://github.com/EndstoneMC/endstone/issues/280

## Review scope and state {#review-scope-and-state}

- Thread author: joalisonx; state at review: closed; merged: not applicable.
- Evidence: The public issue and code/reproduction described below were reviewed statically; no code execution or tests were performed.
- Limits: Source snapshot only; no independent runtime verification.

## Engineering reading and attribution {#engineering-reading-and-attribution}

joalisonx asks for an Endstone-specific command-disable config. After stale closure Wu researches native config/commands.json permission-level overrides, reports vanilla testing, and discovers both native and Endstone commands currently ignore those overrides under Endstone's modified system. He chooses to restore the existing mechanism instead of a parallel config, then reports implementation for 0.11. Setting original command names to internal makes them unreachable; aliases explicitly do not work. This resolves the earlier uncertainty in 142 and preserves original-name/alias identity as a migration constraint. No exact patch/test run is linked here, so implementation is maintainer-reported.


## Source index {#source-index}

- https://github.com/EndstoneMC/endstone/issues/280
- https://github.com/EndstoneMC/endstone/issues/280#issuecomment-3678117959
- https://github.com/EndstoneMC/endstone/issues/280#issuecomment-3708424483
- https://github.com/EndstoneMC/endstone/issues/280#issuecomment-3764510401
- https://github.com/EndstoneMC/endstone/issues/280#issuecomment-3765686811
