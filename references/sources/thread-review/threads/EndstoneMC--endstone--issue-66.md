<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:66"],"source_type":"public","date":"2024-09-30","topics":["concurrency","ffi","diagnosis","review","selection"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-66-bug-crash-getting-player-name-when-listening-to-events"></a>
# EndstoneMC/endstone #66: [bug]Crash getting player name when listening to events {#endstonemc-endstone-66-bug-crash-getting-player-name-when-listening-to-events}

Source: https://github.com/EndstoneMC/endstone/issues/66

## Review scope and state {#review-scope-and-state}

- Thread author: wuliao697; state at review: closed; merged: not applicable.
- Evidence: The public issue and code/reproduction described below were reviewed statically; no code execution or tests were performed.
- Limits: Source snapshot only; no independent runtime verification.

## Engineering reading and attribution {#engineering-reading-and-attribution}

wuliao697 reports getName crashing while UUID access works. Wu first suggests plugin frames and asks for RelWithDebInfo/PDB. Rebuilding exposes a missing expected-lite header; wu then identifies a moving main GIT_TAG instead of the deployed Endstone release, explaining changing C++ ABI. The reporter confirms pinning the matching release solves it. This is stronger than a generic blame-plugin diagnosis: dependency/compiler setup led to a concrete version/ABI mismatch. Successful UUID access did not prove object-layout compatibility. The exact dependency-tag issue is separately fixed in PR #68.


## Source index {#source-index}

- https://github.com/EndstoneMC/endstone/issues/66
- https://github.com/EndstoneMC/endstone/issues/66#issuecomment-2382625912
- https://github.com/EndstoneMC/endstone/issues/66#issuecomment-2383106473
- https://github.com/EndstoneMC/endstone/issues/66#issuecomment-2383119107
- https://github.com/EndstoneMC/endstone/issues/66#issuecomment-2383135555
