<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:155"],"source_type":"public","date":"2025-03-12","topics":["lifetime","concurrency","api","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-155-feature-implement-servicemanager-for-cross-language-plugin-interaction"></a>
# EndstoneMC/endstone #155: [feature] Implement `ServiceManager` for Cross-Language Plugin Interaction {#endstonemc-endstone-155-feature-implement-servicemanager-for-cross-language-plugin-interaction}

Source: https://github.com/EndstoneMC/endstone/issues/155

## Review scope and state {#review-scope-and-state}

- Thread author: wu-vincent; state at review: closed; merged: not applicable.
- Evidence: The public issue and code/reproduction described below were reviewed statically; no code execution or tests were performed.
- Limits: Source snapshot only; no independent runtime verification.

## Engineering reading and attribution {#engineering-reading-and-attribution}

Wu proposes ServiceManager as a common cross-plugin mechanism for C++ and Python: a Service base interface, registration/retrieval, initially one instance per service type. He explicitly requires py::keep_alive on Python registration to retain both the Python instance lifetime and its exact retrieved type, not merely the underlying C++ pointer. Multiple instances, priorities, and dependency injection are future extensions, not initial promises. The rationale is to share behavior without depending on another plugin's internals. The issue is closed with no discussion or implementation link; this is an authored design plan, not proof that its API or lifetime policy shipped. A later implementation must independently verify ownership during unregister/plugin unload and binding behavior.


## Source index {#source-index}

- https://github.com/EndstoneMC/endstone/issues/155
