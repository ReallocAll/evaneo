<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:75"],"source_type":"public","date":"2024-10-11","topics":["concurrency","ffi","testing","build","api","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-75-make-fields-public-for-serverlistpingevent"></a>
# EndstoneMC/endstone #75: Make fields public for ServerListPingEvent {#endstonemc-endstone-75-make-fields-public-for-serverlistpingevent}

Source: https://github.com/EndstoneMC/endstone/pull/75

## Review scope and state {#review-scope-and-state}

- Thread author: theaddonn; state at review: closed; merged: True.
- Evidence: Public PR and patch reviewed statically (1392 additions, 952 deletions, matching recorded metadata); no code execution or tests were performed.
- Limits: Source snapshot only; no independent runtime verification.

## Engineering reading and attribution {#engineering-reading-and-attribution}

theaddonn initially proposes public ping fields, then revises to local IPv4/IPv6 port and GUID setters. Wu questions the use case because fields were intentionally read-only and would not change visible list appearance. Dingsel supplies the proxy/backend port mismatch counterexample: clients may infer an unavailable server. Wu accepts the use case while preferring proxy-side response rewriting and asks for Python bindings. theaddonn corrects the assumption that proxies lack capability, arguing backend rewriting avoids overhead. No measurements substantiate the overhead claim. Captured PR is merged. Codecov is 149 commits stale with only 12.2963% patch coverage, so it is not final-head validation.

### Complete patch inspection {#complete-patch-inspection}

All 76 file changes were read, including native layouts, build-system changes, symbol-map migration and Python bindings. The actual ping change adds setters for GUID and IPv4/IPv6 local ports, exposes all three through writable Python properties, and updates stubs. It does not make every field public; remote-address/protocol fields remain read-only. No new port-range validation is included.

The aggregate diff also carries the 1.21.50 transition: binary-stream storage moves to owned string plus view; actor initialization shrinks to typed VariantParameterList; registry enum values become uint32 pairs, command parameter fields are renamed/reinterpreted, and CommandRunStats is added. Block/BlockLegacy move component storage from inheritance to composition with a much larger storage layout; new detection-rule data supplies liquid containment. Biome gains category lists/component storage; Dimension gains sea/light fields and interface methods; ILevel/Level virtual slots and player/script event variants change. These are ABI-sensitive implementation changes with platform-size assertions, not cosmetic renaming or independent correctness proof. Symbols update both platforms for 1.21.50.

Other behavior changes: remove native reload before command-registry snapshot; regex-filter single-file plugin loading; send player inventory after add/clear; tolerate resource-pack JSON comments and log parse failures; register signal handlers at server construction; handle new scripting startup/shutdown event variants while preserving native forwarding and the null script-handler guard for messages. DevTools removes material dumps and special-tool enumeration, replacing fields with native solidity/translucency/tool requirements. Its block-permutation callback return remains ignored. Runtime CMake changes to explicit source lists and fetches pinned funchook v1.1.3 directly instead of local Conan recipe; GTest discovery moves inside the testing conditional.

These broad changes exist in the inspected PR comparison but are not all assigned to theaddonn. The thread's narrow ping rationale does not explain their design or testing. This is a concrete warning against deriving authorship or feature scope from PR title alone.

Exact inspected base/head: 2c9e13e3f8b4d83a5cce412f52b269da58b57b64…219c890cfa0801241e33ac648f9e5e939c3a0d54. The complete PR diff was inspected; no upstream code or tests were executed.


## Source index {#source-index}

- https://github.com/EndstoneMC/endstone/pull/75
- https://github.com/EndstoneMC/endstone/pull/75#issuecomment-2407561752
- https://github.com/EndstoneMC/endstone/pull/75#issuecomment-2407684112
- https://github.com/EndstoneMC/endstone/pull/75#issuecomment-2417531077
- https://github.com/EndstoneMC/endstone/pull/75#issuecomment-2417576249
- https://github.com/EndstoneMC/endstone/pull/75#issuecomment-2419347428
- https://github.com/EndstoneMC/endstone/pull/75#issuecomment-2419490153
