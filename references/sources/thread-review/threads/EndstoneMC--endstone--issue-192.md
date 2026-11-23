<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:192"],"source_type":"public","date":"2025-06-01","topics":["concurrency","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-192-load-plugin-before-server-starts-add-ons-processing"></a>
# EndstoneMC/endstone #192: Load plugin before server starts add-ons processing {#endstonemc-endstone-192-load-plugin-before-server-starts-add-ons-processing}

Source: https://github.com/EndstoneMC/endstone/issues/192

## Review scope and state {#review-scope-and-state}

- Thread author: Mih4n; state at review: closed; merged: not applicable.
- Evidence: The public issue and code/reproduction described below were reviewed statically; no code execution or tests were performed.
- Limits: Source snapshot only; no independent runtime verification.

## Engineering reading and attribution {#engineering-reading-and-attribution}

Mih4n wants plugin execution before addon processing so a plugin can populate content. Wu rejects loading plugins during server initialization because of possible scripting API conflicts. He proposes a separate Python startup wrapper to download/unpack addons before launching Endstone, preserving a clear initialization boundary rather than adding another plugin phase. This is a stated design decision, not a benchmark or proof that all early hooks are inherently unsafe; no implementation patch appears.


## Source index {#source-index}

- https://github.com/EndstoneMC/endstone/issues/192
- https://github.com/EndstoneMC/endstone/issues/192#issuecomment-3141334134
- https://github.com/EndstoneMC/endstone/issues/192#issuecomment-3173921633
