<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:145"],"source_type":"public","date":"2025-02-28","topics":["concurrency","testing","diagnosis","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-145-bug-pyobjectmaketpcall-unknownfile"></a>
# EndstoneMC/endstone #145: [bug] PyObject_MakeTpCall (UnknownFile:?) {#endstonemc-endstone-145-bug-pyobjectmaketpcall-unknownfile}

Source: https://github.com/EndstoneMC/endstone/issues/145

## Review scope and state {#review-scope-and-state}

- Thread author: pgrd1; state at review: closed; merged: not applicable.
- Evidence: The public issue and code/reproduction described below were reviewed statically; no code execution or tests were performed.
- Limits: Source snapshot only; no independent runtime verification.

## Engineering reading and attribution {#engineering-reading-and-attribution}

pgrd1 reports months of Linux crashes and rollback impact at 30–40 concurrent users, initially suspecting teleportation from a short _PyObject_MakeTpCall stack. Wu asks for reliable reproduction because the original stack is insufficient, then requests testing 0.6.2. The reporter later provides a different 0.6.3.dev21 join-time SIGSEGV with ReadOnlyBinaryStream::read/getByte/getUnsignedVarInt and OutgoingPacketEvent handling. Wu says previous crash reporting was malfunctioning and the new symbols should narrow the issue. Subsequent stable-0.6.2 reports describe malloc smallbin/double-linked-list corruption and a hang. These observations cannot be collapsed into a confirmed teleport bug or one proven cause; no patch, reproducible minimal test, or resolution confirmation is supplied before stale closure. Diagnostic infrastructure quality materially changes triage, while the memory-corruption reports require independent localization.


## Source index {#source-index}

- https://github.com/EndstoneMC/endstone/issues/145
- https://github.com/EndstoneMC/endstone/issues/145#issuecomment-2691192970
- https://github.com/EndstoneMC/endstone/issues/145#issuecomment-2692795077
- https://github.com/EndstoneMC/endstone/issues/145#issuecomment-2715044463
- https://github.com/EndstoneMC/endstone/issues/145#issuecomment-2715076110
- https://github.com/EndstoneMC/endstone/issues/145#issuecomment-2721840436
- https://github.com/EndstoneMC/endstone/issues/145#issuecomment-2721901894
- https://github.com/EndstoneMC/endstone/issues/145#issuecomment-2724641327
- https://github.com/EndstoneMC/endstone/issues/145#issuecomment-2733192215
- https://github.com/EndstoneMC/endstone/issues/145#issuecomment-2888582944
