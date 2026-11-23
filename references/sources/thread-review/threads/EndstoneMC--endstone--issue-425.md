<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:425"],"source_type":"public","date":"2026-07-08","topics":["testing","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-425-custom-dimensions-don-t-show"></a>
# EndstoneMC/endstone #425: Custom Dimensions don't show {#endstonemc-endstone-425-custom-dimensions-don-t-show}

Source: https://github.com/EndstoneMC/endstone/issues/425

## Evidence and attribution {#evidence-and-attribution}

Primary author: MisledWater79. Created 2026-07-08T06:14:25Z; recorded state closed; merged not applicable.

## Registration versus instantiation {#registration-versus-instantiation}

MisledWater79 registers two custom dimensions during ScriptAPI startup, then enumerates getDimensions in plugin enable and sees only vanilla dimensions. wu-vincent reports reproducing on BDS 1.26.32.2: registration stores name→id definitions, but dimensions instantiate lazily when referenced/entered. Enumeration returns loaded instances, analogous to Bukkit loaded-world enumeration; a future explicit load/create API is separate work.

The main example includes a command that teleports using world.getDimension, which triggers first use later than plugin enable. Distinguish catalogs from live objects and lifecycle timing before labeling missing enumeration as data loss. A comment warns of a removed suspicious zip; it was not fetched or executed. No current code change was required.

## Code and verification boundary {#code-and-verification-boundary}

No code inspection required for the narrow discussion finding; no implementation claim independently verified. No upstream code was executed and no tests were run in this review. Runtime assertions are source-reported unless explicitly identified as static code findings.

## Traceability {#traceability}


- https://github.com/EndstoneMC/endstone/issues/425
- https://github.com/EndstoneMC/endstone/issues/425#issuecomment-4912294328
- https://github.com/EndstoneMC/endstone/issues/425#issuecomment-4936635746
