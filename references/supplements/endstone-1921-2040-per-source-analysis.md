<!-- retrieval: {"source_ids":["public:commit:1519507f44ee1711eb1d420c0c5fff2f99b4009e","public:commit:6ed7faf87c6febe70f007a51f3012f90db376513","public:commit:6f646e0a0cc86deaa40675451cb0e9f6c925d2e6"],"source_type":"public","date":"2024-12-16..2024-12-23","topics":["build","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
# Additional per-source analysis and source qualifications {#additional-per-source-causal-analysis}

These supplemental notes record commit-specific engineering observations and evidence limits alongside the main source analyses. Public commit links identify the inspected revisions; no runtime result is independently verified here. A repeated review-scope qualification describes a limit of the analysis, not necessarily a change made by every listed commit.

<a id="commit-6f646e0a0cc86deaa40675451cb0e9f6c925d2e6"></a>
## ci: fix static_assert macros for class size checks {#commit-6f646e0a0cc86deaa40675451cb0e9f6c925d2e6}

Summary: Uses BEDROCK_STATIC_ASSERT_SIZE for Biome component base/storage instead of unconditional assertions; exact assertion gate evaluated in context. Context confirms this macro skips the assertions outside NDEBUG; it is a conditional build check.

### Provenance {#commit-6f646e0a0cc86deaa40675451cb0e9f6c925d2e6-provenance}

Public source: https://github.com/EndstoneMC/endstone/commit/6f646e0a0cc86deaa40675451cb0e9f6c925d2e6

Source date: 2024-12-16T15:49:29Z


<a id="commit-6ed7faf87c6febe70f007a51f3012f90db376513"></a>
## fix: potential iterator invalidation during plugin loading {#commit-6ed7faf87c6febe70f007a51f3012f90db376513}

Summary: Snapshots raw PluginLoader pointers before invoking load/onLoad, avoiding iterator invalidation when callbacks register new unique-owned loaders. Existing pointees remain stable on vector reallocation; newly registered loaders intentionally deferred to later pass. Does not implement dependency ordering or protect removal/destruction. At the later 2040-commit review endpoint, single-file loadPlugin still iterated the live loader vector through initPlugin.

### Provenance {#commit-6ed7faf87c6febe70f007a51f3012f90db376513-provenance}

Public source: https://github.com/EndstoneMC/endstone/commit/6ed7faf87c6febe70f007a51f3012f90db376513

Source date: 2024-12-20T12:41:41Z


<a id="commit-1519507f44ee1711eb1d420c0c5fff2f99b4009e"></a>
## fix: `Actor::setNameTagAlwaysVisible` now works as expected {#commit-1519507f44ee1711eb1d420c0c5fff2f99b4009e}

Summary: Switches always-visible from status flag to byte dataID81 and updates name_tag_hash after name mutation. Introduces hasData as id >= items_array_.size() && items_array_[id], an inverted bounds condition: valid indices return false; out-of-range indices can be accessed. Thus new getInt8/getString regress despite commit success wording. Setter _find remains unchecked. Endpoint persistence checked separately. The incorrect bounds check persisted at the later 2056-commit review endpoint. A subsequent [public fix](https://github.com/EndstoneMC/endstone/commit/0b6684a726c5b8848af2c7f3bd5747910e777753) corrected `hasData` to require `id < items_array_.size()`; that repair is outside the December 2024 revisions analyzed here.

### Provenance {#commit-1519507f44ee1711eb1d420c0c5fff2f99b4009e-provenance}

Public source: https://github.com/EndstoneMC/endstone/commit/1519507f44ee1711eb1d420c0c5fff2f99b4009e

Source date: 2024-12-23T02:59:59Z
