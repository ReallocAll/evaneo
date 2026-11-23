<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:122"],"source_type":"public","date":"2025-01-10","topics":["concurrency","ffi","testing","api","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-122-feat-add-ll-runtime-support-for-endstone"></a>
# EndstoneMC/endstone #122: feat: add LL runtime support for endstone {#endstonemc-endstone-122-feat-add-ll-runtime-support-for-endstone}

Source: https://github.com/EndstoneMC/endstone/pull/122

## Review scope and state {#review-scope-and-state}

- Thread author: OEOTYAN; state at review: closed; merged: False.
- Evidence: Public PR and patch reviewed statically (1301 additions, 11 deletions, matching recorded metadata); no code execution or tests were performed.
- Limits: Source snapshot only; no independent runtime verification.

## Engineering reading and attribution {#engineering-reading-and-attribution}

OEOTYAN proposes LeviLamina runtime support. Wu closes the PR unmerged and directs interested users to separate LiteLDev/LeviStone for support. That establishes project-boundary/extraction disposition, not endorsement of this patch's safety or compatibility. The adapter and vendored parser are separately attributed below; Wu is not their original author.

### Complete patch inspection {#complete-patch-inspection}

OEOTYAN's proposed adapter uses Xmake/C++20, pinned LeviLamina commit 42b75be796e8481394a8dd380c2500f76287919f, Python 3.12.3 and Levi memory operators. It packages a native EndstoneRuntime mod plus embedded Python library, substitutes Levi logging/sinks for Endstone's logger, translates severity levels and Minecraft colors, and renames /version to /esversion while leaving ver/about aliases. The runtime installs hooks through Levi's global-thread-pausing hook API, rejects duplicate/missing targets, and skips ll_-prefixed detours.

Original-function access changes from hashed lookup to cached pointers to mutable original-pointer slots. That supports a hook framework updating chained originals, but clear/uninstall invalidates cached element pointers; unload is explicitly commented out as TODO, not a supported lifecycle. disable clears plugins/commands; re-enable reloads data and both startup/postworld plugins, emits Reload and resynchronizes player commands. load() sets enabled true after installing hooks, so the first enable callback does not run that reload path.

Python starts from an isolated PyConfig but deliberately resets isolated=0/use_environment=1 while disabling signal installation. It imports threading/numpy and disarms GIL release; no interpreter finalization is implemented in this proposal. This is not an isolated-from-environment security guarantee.

The 669-line vendored TOML parser/encoder was fully read. Its copyright attributes Jonathan Stoler (2017), separate from OEOTYAN/Wu. It supports strings/arrays/tables/booleans/numbers with optional strict checks; it is used for symbol generation. Static limitations include unbounded comment-skipping loops at EOF in some paths, incorrect Unicode scalar test excluding the valid upper range, and an encoder that mutates input tables. These are local parser observations, not a claim that normal symbols.toml triggers them. No compatibility test accompanies the proposal. The native hook API header changes also require the ordinary runtime implementation to agree; only the Levi replacement is supplied here.

Exact inspected base/head: 23ca36d51fd44b1cd3e96b2e4633b3f071cd0634…69c04b4eb84ca147e4a7df95691810c84a3c82f6. The complete PR diff was inspected; no upstream code or tests were executed.


## Source index {#source-index}

- https://github.com/EndstoneMC/endstone/pull/122
- https://github.com/EndstoneMC/endstone/pull/122#issuecomment-2590143594
