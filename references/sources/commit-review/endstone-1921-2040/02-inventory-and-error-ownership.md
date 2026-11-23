<!-- retrieval: {"source_ids":["public:commit:06829e8bea49d15204a7816777c0f717e0f737a2","public:commit:11a73e91cc32900e5eabff8f794aaedf1a981b60","public:commit:15495a55984fe5ee8ca604a841f8dda9ab07702e","public:commit:1fefad9c9f33a8979c1a221ef7ef262b7f380cfc","public:commit:40ed3d0d4ad475fbd38880f3423fef4c7f90ac68","public:commit:7bbbb68298af8c32704461f2343ffbc8ab0a6de9","public:commit:8dd9acfc5c114edf5ee1e14d050e02863231bb24","public:commit:dc18e323ed65c646e3b71025aa4993f4b6e114ab","public:commit:f17c5b7ee55d31993a0be6b3fc6c7f8f9a86242a","public:commit:fa430aac04960c1cf9757baaf821f2bdeb4197c2"],"source_type":"public","date":"2024-10-25..2024-12-16","topics":["lifetime","ffi","testing","api","review","selection","networking"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
# Ownership, conversion and client-visible inventory state {#ownership-conversion-and-client-visible-inventory-state}

## Error strings: ownership before formatting convenience {#error-strings-ownership-before-formatting-convenience}

1930 changes Error's stored message/trace from string_view to owning string. The formatting helper creates a temporary formatted string and explicitly selects the string_view overload while that temporary is still alive; the Error constructor now copies it. The causal fix is ownership of data that outlives the formatting expression, not a claim that string_view itself is generally wrong. This patch also changes native I18n's localization argument to shared_ptr, a separate ABI correction retained in its individual record.

## Inventory API progression {#inventory-api-progression}

1937 introduces shared_from_this and a shared_ptr Python holder.1939 adds public getItem/setItem and PlayerInventory forwarding, but conversion is initially only declared.1940 adds native default/copy/type construction and lookup;1942 allows Python None before1943 repairs C++ null/air handling and unknown-type lookup. Reviewing only the final binding or only the scaffold would miss the temporary null-dereference path.

The wrapper returned for a native slot contains a reference to engine-owned ItemStack data. Shared ownership of the wrapper does not own that native slot, container or player lifetime. For a non-wrapper API item, conversion locates the native type and uses the native constructor; unknown types become empty. Custom NBT metadata remains TODO. The Windows copy-constructor decorated-name backreference repair1944 is a platform ABI fix, not merely formatting.

1945 adds addItem, getContents, first, isEmpty and clear. Empty slots are preserved in contents. addItem's shared_from_this use assumes the API item itself is held by shared_ptr, an important C++ caller precondition that Python's holder alone cannot guarantee. The Python binding names __get_item__/__set_item__ do not implement the standard __getitem__/__setitem__ protocol. The source does not establish that bracket access works.

## Mutating state is not notifying clients {#mutating-state-is-not-notifying-clients}

1941 stores the native player holder and sends inventory after setItem. addItem and clear initially mutate native state without that notification.2014 adds holder.sendInventory(false) to both, a narrow source-visible repair for stale client state. No live server or packet test was run, and commit/issue wording is retained as reported motivation.

## Apply with limits {#apply-with-limits}

The transferable check is to separate wrapper lifetime, native object lifetime, conversion failure, ownership requirements and network notification. Proposed verification would cover None/air/unknown type, borrowed slot invalidation, stack-allocated API ItemStack, add/clear notifications and Python indexing. These are review-derived test needs, not tests executed or claimed passing. No blanket preference for shared_ptr or exception-based failure is inferred.

## Individual commit evidence {#individual-commit-evidence}

<a id="commit-1930"></a>
### Commit 1930 {#commit-1930}

40ed3d0d4ad475fbd38880f3423fef4c7f90ac68 · 2024-10-25T11:40:52Z

[fix: various crashes on Linux](https://github.com/EndstoneMC/endstone/commit/40ed3d0d4ad475fbd38880f3423fef4c7f90ac68)


Error now owns std::string message/trace instead of retaining string_views to temporary formatted data. Declares string_view overload before formatting template and explicitly casts formatted string_view, preventing undesired template recursion/selection. I18n current language changes optional_ref to not_null shared_ptr and caller dereferences directly; title reports Linux crash fixes, unexecuted.

Static review only; no upstream execution.

<a id="commit-1937"></a>
### Commit 1937 {#commit-1937}

15495a55984fe5ee8ca604a841f8dda9ab07702e · 2024-10-27T17:36:20Z

[feat: enable shared from ItemStack](https://github.com/EndstoneMC/endstone/commit/15495a55984fe5ee8ca604a841f8dda9ab07702e)


Adds enable_shared_from_this<ItemStack> and Python shared_ptr holder; this owns API wrapper, not necessarily native inventory slot.

Static review only; no upstream execution.

<a id="commit-1939"></a>
### Commit 1939 {#commit-1939}

7bbbb68298af8c32704461f2343ffbc8ab0a6de9 · 2024-10-27T20:07:28Z

[feat: add methods to Inventory class](https://github.com/EndstoneMC/endstone/commit/7bbbb68298af8c32704461f2343ffbc8ab0a6de9)


Introduces getItem/setItem interfaces and delegating PlayerInventory; getItem wraps const-cast native slot by shared API wrapper, empty native item yields null. Declares conversion and adds asEndstoneItemStack dispatch; conversion implementation only arrives1940. Formatting in vanilla exporter also disambiguates global ItemStack.

Static review only; no upstream execution.

<a id="commit-1940"></a>
### Commit 1940 {#commit-1940}

f17c5b7ee55d31993a0be6b3fc6c7f8f9a86242a · 2024-10-27T23:46:10Z

[feat: add Inventory::getItem and Inventory::setItem](https://github.com/EndstoneMC/endstone/commit/f17c5b7ee55d31993a0be6b3fc6c7f8f9a86242a)


Implements conversion by native copy construction for existing Endstone wrappers, default empty native stack otherwise, or type/amount for generic items with explicit NBT TODO. Adds ctor symbols and Python methods. At this point null public item dereferences;1943 repairs after1942 admits None. Invalid type handling depends on1943 nonthrowing registry lookup.

Static review only; no upstream execution.

<a id="commit-1941"></a>
### Commit 1941 {#commit-1941}

06829e8bea49d15204a7816777c0f717e0f737a2 · 2024-10-28T00:10:01Z

[feat(inventory): send updated inventory to players after calling `PlayerInventory::setItem`](https://github.com/EndstoneMC/endstone/commit/06829e8bea49d15204a7816777c0f717e0f737a2)


PlayerInventory retains native holder and sends inventory(false) after setItem, separating server mutation from client refresh. Other mutation methods introduced later do not yet all refresh.

Static review only; no upstream execution.

<a id="commit-1942"></a>
### Commit 1942 {#commit-1942}

11a73e91cc32900e5eabff8f794aaedf1a981b60 · 2024-10-29T12:38:12Z

[fix: allow None as a valid argument of set_item](https://github.com/EndstoneMC/endstone/commit/11a73e91cc32900e5eabff8f794aaedf1a981b60)


Python set_item accepts optional shared_ptr and passes None as nullptr; get_item arg renamed index. C++ toMinecraft null guard absent until1943, so this commit alone does not safely support None.

Static review only; no upstream execution.

<a id="commit-1943"></a>
### Commit 1943 {#commit-1943}

dc18e323ed65c646e3b71025aa4993f4b6e114ab · 2024-10-29T12:38:50Z

[fix Return null when ItemRegistry::getItem is called with an invalid id](https://github.com/EndstoneMC/endstone/commit/dc18e323ed65c646e3b71025aa4993f4b6e114ab)


Adds null/air conversion to default empty native stack, switches ItemRegistry at() to find()/null sentinel for unknown names and int16 ids, centralizes ItemRegistryRef delegation, replaces WeakPtr bool with isNull and not_null arrow. This closes1942's null-dereference chain; no bounds tests shown.

Static review only; no upstream execution.

<a id="commit-1944"></a>
### Commit 1944 {#commit-1944}

1fefad9c9f33a8979c1a221ef7ef262b7f380cfc · 2024-10-29T18:04:47Z

[fix: call original copy constructor on Windows](https://github.com/EndstoneMC/endstone/commit/1fefad9c9f33a8979c1a221ef7ef262b7f380cfc)


Windows ctor-name synthesis corrects BV1@@Z backreference to BV0@@Z for original copy constructor, with cached decorated-name calculation. Generic heuristic remains mangling-dependent, not universal ABI portability. Also fixes ConanInvalidConfiguration import.

Static review only; no upstream execution.

<a id="commit-1945"></a>
### Commit 1945 {#commit-1945}

fa430aac04960c1cf9757baaf821f2bdeb4197c2 · 2024-10-31T12:10:21Z

[feat: add more api functions to the `Inventory` class](https://github.com/EndstoneMC/endstone/commit/fa430aac04960c1cf9757baaf821f2bdeb4197c2)


Adds addItem, contents preserving empty slots, first, isEmpty and clear; uses force-balance native mutation. addItem/first invoke shared_from_this on ItemStack&, introducing shared-ownership precondition for C++ callers. Python special methods are spelled __get_item__/__set_item__ rather than Python indexing protocol. Player clear only delegates here;2014 adds client refresh.

Static review only; no upstream execution.

<a id="commit-2014"></a>
### Commit 2014 {#commit-2014}

8dd9acfc5c114edf5ee1e14d050e02863231bb24 · 2024-12-16T15:55:20Z

[fix: player inventory not being updated after calling `clear`](https://github.com/EndstoneMC/endstone/commit/8dd9acfc5c114edf5ee1e14d050e02863231bb24)


Sends holder inventory after both addItem and clear; earlier setItem already sent. Closes visible stale-client state after successful native mutation; no network test executed.

Static review only; no upstream execution.
