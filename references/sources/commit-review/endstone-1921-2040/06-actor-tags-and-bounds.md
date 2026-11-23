<!-- retrieval: {"source_ids":["public:commit:1519507f44ee1711eb1d420c0c5fff2f99b4009e","public:commit:2d5fddaf00df34c62c7d3b0f61b380359cfd8278","public:commit:2ec06ffcb1ab7cc601d5a68cc62f2f9f1e633779","public:commit:6d7939d880edfe985f90f1bed12d94eb1b2891d9","public:commit:727add20495afc26a9d6ca4e35127e99ec331cf3","public:commit:a0f1c7402936f547e9f7ef85abc8e98c6a55f651","public:commit:d3979e1b4f143c634277380743b4683eb6e32889","public:commit:fab6d4b59935a36404ab4444d463c2c8c555aef4"],"source_type":"public","date":"2024-12-22..2024-12-23","topics":["ffi","testing","api","review","selection"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
# Actor tags: representation, dirty state and a failed repair {#actor-tags-representation-dirty-state-and-a-failed-repair}

## Separate scaffolding, state mutation and public surface {#separate-scaffolding-state-mutation-and-public-surface}

2032/2033 add typed actor-data IDs/wrappers and native name/score APIs, but backing methods are not implemented until2035.2035 updates actor flag storage and the matching dirty metadata word, and adds string lookup/mutation. Updating a value without dirty notification would not establish client synchronization. Getters have bounds/null/type guards; setters call unchecked _find before null/type checks, so they still require a valid ID/storage shape.

2036 exposes Actor/Mob/Player delegates and changes name visibility from ALWAYS_SHOW_NAME to CAN_SHOW_NAME.2037 supplies Python properties;2039 renames the Python visibility spelling and adds a separate always-visible API. It also changes status lookup to return false when the component is absent. Public wrappers return string copies while the native getter exposes a reference.

##2040: a representation repair with an introduced bounds regression

2040's commit message says setNameTagAlwaysVisible now works. Its code moves always-visible control from the status flag to byte actor-data ID81 and also refreshes name_tag_hash when setting the name. Those mechanisms are independently useful findings. However, the new helper is:

    return id >= items_array_.size() && items_array_[id];

For an in-range id, the first condition is false, so getString/getInt8 return their empty/zero defaults even when data exists. For an out-of-range id, the right-hand indexing expression may execute. The intended existence guard needs the opposite comparison. Both setter specializations still use unchecked _find. This is static source reasoning, not an executed exploit, a current-server vulnerability claim, or a claim about the external engine's reachable inputs.

The full file at the final2024 target5310484c580f9077b436a58c8f90905f3ddff2c4 was read and retains the condition. The completed later dossier [2025 Commit313](../endstone-2025-0301-0400/01-lifecycle-policy.md#commit-313) records its repair in [0b6684a726c5b8848af2c7f3bd5747910e777753](https://github.com/EndstoneMC/endstone/commit/0b6684a726c5b8848af2c7f3bd5747910e777753),2025-03-01, together with DataItem virtual/layout changes. That is a qualifier from already completed work; this owner neither reviews nor claims that2025 target anew.

## Apply with limits {#apply-with-limits}

The strongest lesson is to test logical predicates and data representation separately: valid/missing/wrong-type/out-of-range IDs; current versus always-visible flags; changing a name and its hash; and dirty-state emission. A fix title and plausible representation change can coexist with an elementary bounds error. Native cast layouts and client rendering were not validated here. Resin color2034 is a distinct small cross-surface addition and receives its own source entry.

## Individual commit evidence {#individual-commit-evidence}

<a id="commit-2032"></a>
### Commit 2032 {#commit-2032}

2d5fddaf00df34c62c7d3b0f61b380359cfd8278 · 2024-12-22T22:49:25Z

[feat: add SynchedActorDataAccess and SynchedActorData](https://github.com/EndstoneMC/endstone/commit/2d5fddaf00df34c62c7d3b0f61b380359cfd8278)


Introduces132actor-data IDs, typed dirtyflags/data wrapper and name-tag methods, but backing get/set and flag helper remain declarations/empty source until2035. Initial visible setter uses ALWAYS_SHOW_NAME, corrected to CAN_SHOW_NAME2036. Native layout declarations are compatibility assumptions.

Static review only; no upstream execution.

<a id="commit-2033"></a>
### Commit 2033 {#commit-2033}

727add20495afc26a9d6ca4e35127e99ec331cf3 · 2024-12-22T23:29:08Z

[feat: add getter and setter for score tags in Actor class](https://github.com/EndstoneMC/endstone/commit/727add20495afc26a9d6ca4e35127e99ec331cf3)


Adds native score-tag get/set via SCORE dataID; depends on subsequent typed backing implementation2035.

Static review only; no upstream execution.

<a id="commit-2034"></a>
### Commit 2034 {#commit-2034}

6d7939d880edfe985f90f1bed12d94eb1b2891d9 · 2024-12-22T23:45:40Z

[feat: add material_resin color (§v)](https://github.com/EndstoneMC/endstone/commit/6d7939d880edfe985f90f1bed12d94eb1b2891d9)


Adds resin §v color across C++constant, ANSItruecolor mapping234,113,19 and Python property; small complete cross-surface feature, not boilerplate.

Static review only; no upstream execution.

<a id="commit-2035"></a>
### Commit 2035 {#commit-2035}

fab6d4b59935a36404ab4444d463c2c8c555aef4 · 2024-12-23T00:43:18Z

[feat: implement SynchedActorDataAccess::setActorFlag and SynchedActorData::getString](https://github.com/EndstoneMC/endstone/commit/fab6d4b59935a36404ab4444d463c2c8c555aef4)


Implements status flag update with corresponding dirty-word mark, typed string getter and setter. Getter bounds/null/type guards exist; setter calls unchecked _find before null/type guard, so bounds are not protected. No tests. Dirty notification is essential beyond assignment.

Static review only; no upstream execution.

<a id="commit-2036"></a>
### Commit 2036 {#commit-2036}

d3979e1b4f143c634277380743b4683eb6e32889 · 2024-12-23T00:57:51Z

[feat: add functions for name tag and score tag manipulation to Actor class](https://github.com/EndstoneMC/endstone/commit/d3979e1b4f143c634277380743b4683eb6e32889)


Exposes name/score tags and name visibility through public Actor, Mob and Player delegates; changes native visibility flag ALWAYS_SHOW_NAME→CAN_SHOW_NAME. Preserves getter stringcopy at public boundary; no Python surface until2037.

Static review only; no upstream execution.

<a id="commit-2037"></a>
### Commit 2037 {#commit-2037}

2ec06ffcb1ab7cc601d5a68cc62f2f9f1e633779 · 2024-12-23T01:04:45Z

[feat: add python bindings for newly added APIs](https://github.com/EndstoneMC/endstone/commit/2ec06ffcb1ab7cc601d5a68cc62f2f9f1e633779)


Adds Python tag/visibility properties and stubs plus resin stub; is_nametag_visible spelling immediately changes2039. Binding/generated-looking stub changes are interface evidence, not independently credited generated authorship.

Static review only; no upstream execution.

<a id="commit-2039"></a>
### Commit 2039 {#commit-2039}

a0f1c7402936f547e9f7ef85abc8e98c6a55f651 · 2024-12-23T02:23:36Z

[feat: add `isNameTagAlwaysVisible` and `setNameTagAlwaysVisible` methods](https://github.com/EndstoneMC/endstone/commit/a0f1c7402936f547e9f7ef85abc8e98c6a55f651)


Adds always-visible public/Python API using ALWAYS_SHOW_NAME status flag; native getStatusFlag now returns false if component absent. Renames Python visibility spelling. Always-visible representation is corrected2040; this is an intermediate failed approach.

Static review only; no upstream execution.

<a id="commit-2040"></a>
### Commit 2040 {#commit-2040}

1519507f44ee1711eb1d420c0c5fff2f99b4009e · 2024-12-23T02:59:59Z

[fix: `Actor::setNameTagAlwaysVisible` now works as expected](https://github.com/EndstoneMC/endstone/commit/1519507f44ee1711eb1d420c0c5fff2f99b4009e)


Switches always-visible from status flag to byte dataID81 and updates name_tag_hash after name mutation. Introduces hasData as id >= items_array_.size() && items_array_[id], an inverted bounds condition: valid indices return false; out-of-range indices can be accessed. Thus new getInt8/getString regress despite commit success wording. Setter _find remains unchecked. Endpoint persistence checked separately.

Static review only; no upstream execution.
