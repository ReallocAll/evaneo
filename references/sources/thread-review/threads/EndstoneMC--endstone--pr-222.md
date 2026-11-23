<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:222"],"source_type":"public","date":"2025-07-21","topics":["testing","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-222-fix-enable-endstone-to-receive-input-from-inherited-stdin-in-a-subprocess"></a>
# EndstoneMC/endstone #222: fix: enable endstone to receive input from inherited stdin in a subprocess {#endstonemc-endstone-222-fix-enable-endstone-to-receive-input-from-inherited-stdin-in-a-subprocess}

Source: https://github.com/EndstoneMC/endstone/pull/222

## Review scope and state {#review-scope-and-state}

- Thread author: wu-vincent; state at review: closed; merged: True.
- Evidence: Public PR and patch reviewed statically (280 additions, 112 deletions, matching recorded metadata); no code execution or tests were performed.
- Limits: Source snapshot only; no independent runtime verification.

## Engineering reading and attribution {#engineering-reading-and-attribution}

Wu's merged PR fixes 211 across process launch and embedded interpreter initialization. Full 6-file patch read: Linux stops explicitly replacing stdin/stdout/stderr so normal inheritance applies; Windows replaces a blocking ANSI winext helper with PopenWithDll using wide-string process/environment creation, std-handle setup, pipe cleanup, retained process handle and normal Popen wait. Runtime saves stdin with dup before Python initialization and restores/closes the duplicate afterward, addressing interpreter-induced stream changes. The old helper explicitly disabled handle inheritance. No tests or human review discussion accompany the patch.

Static caveat: Python computes a filtered startupinfo handle_list and may clear close_fds on the premise that only listed handles will inherit, but the new C++ _detours bridge copies scalar startup/std handles and does not translate lpAttributeList into a native attribute list. Thus this historical patch does not visibly implement the restrictive handle-list semantics its Python comment claims. Duplicate/restore return values are also unchecked. These are code-reading observations, not reproduced failures or claims about current releases; successful stdin forwarding and full subprocess API parity are separate questions.


## Source index {#source-index}

- https://github.com/EndstoneMC/endstone/pull/222
