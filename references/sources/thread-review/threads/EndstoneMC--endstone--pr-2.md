<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:2"],"source_type":"public","date":"2023-09-06","topics":["lifetime","ffi","testing","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-2-new-hook-system"></a>
# EndstoneMC/endstone #2: New hook system {#endstonemc-endstone-2-new-hook-system}

Source: https://github.com/EndstoneMC/endstone/pull/2

## Review scope and state {#review-scope-and-state}

- Thread author: wu-vincent; state at review: closed; merged: True.
- Evidence: Public PR and patch reviewed statically (893 additions, 884 deletions, matching recorded metadata); no code execution or tests were performed.
- Limits: Source snapshot only; no independent runtime verification.

## Engineering reading and attribution {#engineering-reading-and-attribution}

Wu's merged New hook system has no human discussion. Codecov reports a 7.53-point coverage decrease and 58.33% diff coverage for ac01d8e, explicitly warning that the final c2d823f head differs. That bot result cannot validate the final patch. Full base/head patch was read, including removed old hook/cache implementation and new wrappers.

The design changes explicit manually registered hook symbols to exported detour enumeration. It loads Endstone and executable symbol modules, maps symbol addresses relative to each loaded module base, matches decorated names for detours, undecorates non-hook symbols for convenient lookup, then replaces original map entries with MinHook trampolines. Missing symbols throw instead of implicitly yielding map-created empty hooks. This removes the version-keyed JSON symbol-offset cache and its fixed executable-base subtraction. Bedrock export/import visibility macros become separate from public Endstone API. Native declarations are made signature-shaped, including reference arguments, CommandFlag structure, MCRESULT value return, and explicit hidden-return-value adapters. The macros use __FUNCDNAME__, making this implementation Windows/compiler-specific.

Hook behavior is split into per-Bedrock-type files. Server lifecycle still loads/enables/disables plugins. Native commands retain fallback-prefix stripping and original execution, while custom commands still use console sender with an explicit origin-type TODO. Logger levels become sequential public enum values translated to native bit values; Python LogLevel and generic log binding are removed. The logger still passes a completed message as printf-format with an empty varargs list, so percent-containing messages remain a static risk, not a tested regression claim. Tests update logger-level names and simulate native formatting but do not cover hook installation.

RAII manager/symbol-handler classes are introduced, yet their move constructors only invalidate the source without transferring owned handle/initialized state. Initialization failures after MinHook starts can escape before destructor-based cleanup. SymEnumSymbols' result is unchecked. The DllMain detach path now only reacquires the GIL and relies on object lifetime for other cleanup. These are limits in this historical snapshot, not claims about later releases. Full static review supplies no runtime validation. Exact inspected base/head: 84bac040b42961421d6d429bdec83f61a013689e…c2d823feb4cd7dcd557325371b5b2cad002af1af.


## Source index {#source-index}

- https://github.com/EndstoneMC/endstone/pull/2
- https://github.com/EndstoneMC/endstone/pull/2#issuecomment-1707467274
- https://github.com/EndstoneMC/endstone/commit/84bac040b42961421d6d429bdec83f61a013689e/hovercard
- https://github.com/EndstoneMC/endstone/commit/84bac040b42961421d6d429bdec83f61a013689e
- https://github.com/EndstoneMC/endstone/commit/c2d823feb4cd7dcd557325371b5b2cad002af1af/hovercard
- https://github.com/EndstoneMC/endstone/commit/c2d823feb4cd7dcd557325371b5b2cad002af1af
