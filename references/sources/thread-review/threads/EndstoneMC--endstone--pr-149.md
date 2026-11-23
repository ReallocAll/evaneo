<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:149"],"source_type":"public","date":"2025-03-05","topics":["ffi","testing","review","selection","networking"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-149-feature-1-21-70-support"></a>
# EndstoneMC/endstone #149: [feature] 1.21.70 support {#endstonemc-endstone-149-feature-1-21-70-support}

Source: https://github.com/EndstoneMC/endstone/pull/149

## Review scope and state {#review-scope-and-state}

- Thread author: wu-vincent; state at review: closed; merged: True.
- Evidence: Public PR and patch reviewed statically (594 additions, 538 deletions, matching recorded metadata); no code execution or tests were performed.
- Limits: Source snapshot only; no independent runtime verification.

## Engineering reading and attribution {#engineering-reading-and-attribution}

Wu describes this as a preliminary 1.21.70 port prepared against preview beta.26 on Windows and Linux, with final release adjustments expected shortly afterward. The PR was merged as release approached. That is a dated release preparation statement, not a lasting compatibility or turnaround promise. Two captured comments and the primary body were read; there are no review discussions. The Codecov report is not evidence of native runtime correctness.

### Complete patch inspection {#complete-patch-inspection}

The 58-file port contains launcher, authentication/identity, and native layout changes in addition to address rebasing. The bootstrap switches metadata discovery to a versioned v2 path with release/prerelease channels and checks the returned version and binary SHA-256. Those checks detect a mismatched download; they do not prove every native declaration matches that binary.

Windows injection is replaced: the previous Python remote-allocation/WriteProcessMemory/LoadLibraryW sequence becomes a C++ extension calling DetourCreateProcessWithDllExA, waiting, collecting the exit code, and closing handles. Microsoft Detours is pinned as a submodule; its upstream implementation is not authored by Wu and was not independently audited here. CI now fetches submodules. The extension constructs an ANSI environment and process path, so non-ASCII path/environment behavior deserves separate validation. The binding waits while holding the Python GIL, does not validate the wait result, and some error reporting occurs after handle cleanup. Linux retains LD_PRELOAD/LD_LIBRARY_PATH and inherited process streams. A failed child exit now gets an explicit delay and log.

Identity handling changes materially. Player addresses are returned by value and resolved from current RakNet or direct-address identity rather than mutating the network identifier in the constructor. Unsupported address kinds produce an empty result; IPv4/IPv6 formatting buffers are bounded. GameServerToken checks validity and rejects self-signed tokens when untrusted before returning XUID. UserEntityIdentifier now exposes token/network getters, and player construction uses persistent UUID/XUID components. This is a protocol/layout adaptation, not evidence of a general authentication guarantee.

Native declarations change packet receipt configuration, pack dependency upgrades and I/O provider ownership, ServerPlayer construction, Actor/Mob/Player layout, item registry validation, timer tick type, block virtual slots, level sound/particle signatures, and mutable actor-event dispatch. Both platform symbol tables are rebased; Windows I18n uses a preview-specific offset. Such field/slot changes are coupled to the selected binary. There are no new runtime tests in this patch. A successful compile or Codecov report cannot establish ABI correctness.

Exact inspected base/head: 491f13a67ef01a56f7357ed62d87200963f9511d…5a02eeb2b1387b20a9e35b0cede031e9502ac4b5. The complete PR diff was inspected; no upstream code or tests were executed.


## Source index {#source-index}

- https://github.com/EndstoneMC/endstone/pull/149
- https://github.com/EndstoneMC/endstone/pull/149#issuecomment-2743347513
- https://github.com/EndstoneMC/endstone/pull/149#issuecomment-2743347799
