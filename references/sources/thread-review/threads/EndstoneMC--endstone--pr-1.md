<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:1"],"source_type":"public","date":"2023-08-07","topics":["lifetime","concurrency","ffi","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-1-new-plugin-manager"></a>
# EndstoneMC/endstone #1: New Plugin Manager {#endstonemc-endstone-1-new-plugin-manager}

Source: https://github.com/EndstoneMC/endstone/pull/1

## Review scope and state {#review-scope-and-state}

- Thread author: wu-vincent; state at review: closed; merged: True.
- Evidence: Public PR and patch reviewed statically (770 additions, 455 deletions, matching recorded metadata); no code execution or tests were performed.
- Limits: Source snapshot only; no independent runtime verification.

## Engineering reading and attribution {#engineering-reading-and-attribution}

Wu's merged New Plugin Manager has an empty body and no comments or reviews. Full base/head patch reading shows policy moving from a C++ directory/TOML loader retaining py::objects into a Python PluginManager, reached through native trampoline interfaces and separate _server, _plugin and _plugin_manager modules. Python loads only directories containing plugin.toml, resolves module/class from the declared main path, retains instances, and invokes on_load. Per-directory exceptions are printed and scanning continues; no dependency ordering or rollback is added. An exception after appending the instance can leave it retained despite a failed load callback.

Plugin gains enabled state and onLoad. setEnabled is idempotent, changes state before invoking the enable/disable callback, and does not roll back if that callback raises. Manager enable/disable methods check state first. Server startup loads and then enables; server-thread stop now disables rather than clearing retained instances. This distinguishes lifecycle notification from object destruction.

Interpreter/GIL ownership moves from ad hoc DllMain initialization/thread-state manipulation into Server's scoped_interpreter and gil_scoped_release members; each Python-manager call acquires the GIL. Member destruction order deserves care: pluginManager_ is destroyed before release_ reacquires the GIL, so this patch alone is not proof of safe Python-object teardown. Native PyPluginManager trampoline macros omit supplied path/directory/plugin arguments in several overrides, though Server invokes the Python object directly. Do not infer those native interface entry points work from the Python-only path. Hook headers are reorganized/documented, MinHook error conversion moves out of the header, and log-area names are prefixed. The intent beyond the title is inferred from code, not attributed as a stated design rationale.

Reusable decisions: explicit idempotent enable state, separate load/enable/disable phases, Python-owned policy, and GIL-scoped bridge calls. Counterexamples preserve partial initialization and destruction-order risk. Exact inspected base/head: 48813258a5cbdd939a5af4fb8d7c6e32d6ed57da…5056b7e424fef8642da2056a7f9b5524d6ac1e3d.


## Source index {#source-index}

- https://github.com/EndstoneMC/endstone/pull/1
