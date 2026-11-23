<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:228"],"source_type":"public","date":"2025-07-25","topics":["concurrency","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-228-bug-server-crashes-on-running-reload-after-updating-plugins-written-in-c"></a>
# EndstoneMC/endstone #228: [bug] Server crashes on running `/reload` after updating plugins written in C++. {#endstonemc-endstone-228-bug-server-crashes-on-running-reload-after-updating-plugins-written-in-c}

Source: https://github.com/EndstoneMC/endstone/issues/228

## Review scope and state {#review-scope-and-state}

- Thread author: GyanPrakash2483; state at review: closed; merged: not applicable.
- Evidence: The public issue and code/reproduction described below were reviewed statically; no code execution or tests were performed.
- Limits: Source snapshot only; no independent runtime verification.

## Engineering reading and attribution {#engineering-reading-and-attribution}

GyanPrakash2483 replaces a loaded C++ plugin.so on disk and crashes on reload. Wu links69b8a298f75f150ff0fe2e33325252969e0faf41 for 0.10.4. Full patch inspected: loader creates plugins/.local, removes old regular files matching native-plugin patterns, copies the absolute source to a stem-plus-path-hash shadow filename, loads that copy, and reports copy/load/init errors. This decouples the actively mapped library from the administrator's replacement target. The hash is of the source path, not content, so this is not a content-addressed or per-generation immutable cache; safe unload before reusing the same shadow path still matters. Reporter thanks without explicit reproduction retest.


## Source index {#source-index}

- https://github.com/EndstoneMC/endstone/issues/228
- https://github.com/EndstoneMC/endstone/issues/228#issuecomment-3165300753
- https://github.com/EndstoneMC/endstone/issues/228#issuecomment-3177678641
