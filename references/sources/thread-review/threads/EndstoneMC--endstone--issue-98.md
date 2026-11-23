<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:98"],"source_type":"public","date":"2024-12-01","topics":["concurrency","testing","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-98-feature-issue-with-loading-custom-plugins-in-endstone-due-to-plugin-loading-mechanism"></a>
# EndstoneMC/endstone #98: [feature] Issue with Loading Custom Plugins in Endstone due to Plugin Loading Mechanism {#endstonemc-endstone-98-feature-issue-with-loading-custom-plugins-in-endstone-due-to-plugin-loading-mechanism}

Source: https://github.com/EndstoneMC/endstone/issues/98

## Review scope and state {#review-scope-and-state}

- Thread author: engsr6982; state at review: closed; merged: not applicable.
- Evidence: The public issue and code/reproduction described below were reviewed statically; no code execution or tests were performed.
- Limits: Source snapshot only; no independent runtime verification.

## Engineering reading and attribution {#engineering-reading-and-attribution}

engsr6982’s language-engine DLL registers a loader during onLoad, after ordinary discovery; recursively rescanning reloads existing plugins indefinitely. Wu adds single-file/list-of-files loading and prematurely closes as completed. Reporter testing reveals missing file-filter checks sending Lua files to C++/Python loaders, then vector invalidation when onLoad registers another loader. PR #110 supplies filtering; wu’s later 6ed7faf87c6febe70f007a51f3012f90db376513 was inspected: copy current PluginLoader raw pointers into a snapshot vector before invoking callbacks. This prevents vector-iterator invalidation and deliberately limits that pass to existing loaders, assuming pointed-to loaders remain alive. The reporter confirms the code runs fine. This is a multi-stage correction, not proof that overloads alone solved extensibility. Loader removal, concurrent mutation and dependency ordering are not solved by the shown snapshot.


## Source index {#source-index}

- https://github.com/EndstoneMC/endstone/issues/98
- https://github.com/EndstoneMC/endstone/issues/98#issuecomment-2512844910
- https://github.com/EndstoneMC/endstone/issues/98#issuecomment-2522452491
- https://github.com/EndstoneMC/endstone/issues/98#issuecomment-2525025781
- https://github.com/EndstoneMC/endstone/issues/98#issuecomment-2548555517
- https://github.com/EndstoneMC/endstone/issues/98#issuecomment-2556936114
- https://github.com/EndstoneMC/endstone/issues/98#issuecomment-2558111770
- https://github.com/EndstoneMC/endstone/commit/6ed7faf87c6febe70f007a51f3012f90db376513
- https://github.com/EndstoneMC/endstone/commit/6ed7faf87c6febe70f007a51f3012f90db376513)
