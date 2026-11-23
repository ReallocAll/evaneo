<!-- retrieval: {"source_ids":["public:commit:0cd346408d341fdbff2a7d689441ba98bbc27630","public:commit:10940cf48e86fc5babbf0e08224f0f7694df402a","public:commit:3a9a85eec4ad6462e40117efa67602d3adcd0f0a","public:commit:621c4d8da832b2e8a32a9d481d4cbf93771756be","public:commit:64609d4414889e752c7984781298f53c7cb1cacf","public:commit:73169419f75e228a1d1bfdabbb9d7f7c5dea52b2","public:commit:8aceb2431a2c56ffde2d0eaad95f398af7f827c5","public:commit:9fab65ae6ef106ec2f0799edede535e8984da4fb","public:commit:cc98dd2a662d9e8f689fa21d73a37e16b5b21f70","public:commit:de576b3d5dbe803dabb922d9e60d9ce148ccf76e","public:thread:EndstoneMC/endstone:189"],"source_type":"public","date":"2025-05-25..2025-05-27","topics":["lifetime","ffi","testing","build","recovery","api","refactoring"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
# ItemType: definition identity and stack construction contracts {#itemtype-definition-identity-and-stack-construction-contracts}


<a id="explicit-motivation-and-breaking-change"></a>
## Explicit motivation and breaking change {#explicit-motivation-and-breaking-change}

PR189 proposes an immutable item-definition object analogous in purpose to Bukkit Material, so plugin authors can inspect maximum durability and maximum stack size. Its body explicitly documents the breaking change: ItemStack.type becomes an ItemType object and callers wanting the old string use item.type.id. That is the author's rationale and migration guidance, not a preference inferred from a class name.

691–694 build the abstraction and adapter, a server registry initialized in setLevel, and a string ID view. The wrapper owns a NamespacedKey and borrows the native Item. The generic registry caches owned wrappers around native definitions; it does not add native lifetime ownership, synchronization or reload invalidation. Native item lookup uses the complete namespaced string, unlike the enchantment adapter's key-only lookup. Registry lifetime remains a prerequisite for stack type references.

## Stacks now refer to definition objects {#stacks-now-refer-to-definition-objects}

695 changes the stored type from string to reference_wrapper<const ItemType>, introduces Result factories and a protected typed constructor, and changes factory/meta interfaces accordingly. Typed create enforces1–255. String create initially omits the amount check, then699 delegates to typed create so both factories agree. The contract is representable stack count, not automatic adherence to an item's natural max stack size. Direct amount setters still have their own behavior.

696 connects native adapters. Its two native setType overloads diverge: the string overload delegates to the base implementation, which only replaces the stored reference; native getType instead queries handle_. The typed overload actually replaces the native handle with a new stack of amount1, or resets it for air. Thus the string route does not establish a changed native type, while typed replacement also discards old count/metadata unless separately restored. Python construction checks factory errors, but the string setter ignores its Result. These are precise static consequences, not tested plugin failures.

Lookup is nullable but native helpers dereference its result for a native item and for air. Python ItemType.get uses reference return policy, while the stub's nonoptional annotation understates nullability.698 reuses the generic registry binder, including its list-returning __iter__ and unspecified borrowed-return policy concerns from611.700 adds ID equality with strings and other ItemTypes; Python marks the value unhashable rather than promising hash compatibility.

## Do not import the next commit's semantics {#do-not-import-the-next-commit-s-semantics}

At commit700, C++ construction remains factory-based with the protected typed constructor. Commit701 later changes this to public-constructor behavior; that later API is not part of commit700's state.

No new ItemType/stack factory tests appear in691–700. The Codecov bot's captured comment claims modified coverable lines covered while showing0.00% project coverage and a report behind main. That is retained as a bot report, not accepted as proof of functional coverage or a test run by this review. Earlier standalone ItemStack test removal belongs to599 and is a documented coupling/cost tradeoff, not a new defect inferred here.

Use this case for typed-identity API migration, keeping overloads behaviorally aligned, auditing factory validation across entry points, and distinguishing wrapper ownership from native lifetime.

## Per-commit decisions and revisions {#per-commit-decisions-and-revisions}

<a id="commit-691"></a>
### Commit 691 {#commit-691}

[9fab65ae6ef1](https://github.com/EndstoneMC/endstone/commit/9fab65ae6ef106ec2f0799edede535e8984da4fb) · 2025-05-25T22:20:58Z · feat: add `ItemType` class

Introduces read-only ItemType API for key, translation key, maximum stack size and durability, plus umbrella inclusion. Exact PR189 patch. The PR explicitly compares its role to Bukkit Material and explains the missing definition properties; this is the author's stated motivation.


<a id="commit-692"></a>
### Commit 692 {#commit-692}

[0cd346408d34](https://github.com/EndstoneMC/endstone/commit/0cd346408d341fdbff2a7d689441ba98bbc27630) · 2025-05-25T22:37:40Z · feat: add `EndstoneItemType` implementation

Implements EndstoneItemType with an owned NamespacedKey and borrowed const native Item. Translation and durability come from the native item, maximum stack size through ItemDescriptor. Adds build source. Native registry lifetime remains a precondition.


<a id="commit-693"></a>
### Commit 693 {#commit-693}

[8aceb2431a2c](https://github.com/EndstoneMC/endstone/commit/8aceb2431a2c56ffde2d0eaad95f398af7f827c5) · 2025-05-25T22:50:19Z · feat: add `Server::getItemRegistry`

Adds const Server::getItemRegistry pure virtual accessor, core storage/initialization in setLevel, mock override and native registry specialization. Exact PR189 reused pieces are proven individually. Registry lazily owns wrappers but wrappers borrow native definitions; it does not add cache invalidation or synchronization.


<a id="commit-694"></a>
### Commit 694 {#commit-694}

[cc98dd2a662d](https://github.com/EndstoneMC/endstone/commit/cc98dd2a662d9e8f689fa21d73a37e16b5b21f70) · 2025-05-25T23:06:42Z · feat: add `ItemType::getId`

Adds ItemType::getId and native full-name view. Separates stable string identity from the typed property object; the later700 comparisons use this ID.


<a id="commit-695"></a>
### Commit 695 {#commit-695}

[73169419f75e](https://github.com/EndstoneMC/endstone/commit/73169419f75e228a1d1bfdabbb9d7f7c5dea52b2) · 2025-05-25T23:23:32Z · refactor: use `ItemType` in `ItemStack` and `ItemFactory`

Migrates ItemStack type from string to reference_wrapper<const ItemType>, moves construction behind a protected typed constructor and adds Result factories. Typed creation checks1–255; string creation initially omits that amount check. Setters update type references, factory/meta signatures follow ItemType, and copying asks virtual accessors. This is a public source/API break, not merely internal refactoring.


<a id="commit-696"></a>
### Commit 696 {#commit-696}

[3a9a85eec4ad](https://github.com/EndstoneMC/endstone/commit/3a9a85eec4ad6462e40117efa67602d3adcd0f0a) · 2025-05-25T23:51:57Z · feat: update item type-related implementations

Adds ItemType lookup through NamespacedKey and server registry; updates native stack/factory/meta conversion. Native string setType delegates to the base reference assignment, but native getType reads the native handle, so that overload does not change the observed native type. Typed native setType replaces the owned stack with amount1 or resets air. Native lookup results are dereferenced without null guards. Python construction checks Result failure; its string setter ignores the returned Result.


<a id="commit-697"></a>
### Commit 697 {#commit-697}

[de576b3d5dbe](https://github.com/EndstoneMC/endstone/commit/de576b3d5dbe803dabb922d9e60d9ce148ccf76e) · 2025-05-26T00:01:14Z · feat: add python binding for `ItemType`

Renames ItemType lookup to get, adds Python read-only property class/reference-return lookup, and updates ItemStack.type binding/stubs to ItemType. Stub lookup return is nonoptional even though native lookup may return null. PR189 explicitly documents migration from item.type to item.type.id.


<a id="commit-698"></a>
### Commit 698 {#commit-698}

[10940cf48e86](https://github.com/EndstoneMC/endstone/commit/10940cf48e86fc5babbf0e08224f0f7694df402a) · 2025-05-26T00:05:44Z · feat: add python binding for `ItemRegistry`

Adds ItemRegistry Python class, server property and facade export using the generic registry binder. That binder returns a list from __iter__ rather than an iterator and lacks explicit borrowed return policies for several accessors; those earlier protocol/lifetime issues are inherited, not repaired here.


<a id="commit-699"></a>
### Commit 699 {#commit-699}

[621c4d8da832](https://github.com/EndstoneMC/endstone/commit/621c4d8da832b2e8a32a9d481d4cbf93771756be) · 2025-05-26T00:20:11Z · refactor: improve `ItemStack::create`

Makes string ItemStack::create delegate to typed create, closing695's missing1–255 amount validation. This limit is the representable stack count contract, not the item's natural maximum stack size. No new tests.


<a id="commit-700"></a>
### Commit 700 {#commit-700}

[64609d441488](https://github.com/EndstoneMC/endstone/commit/64609d4414889e752c7984781298f53c7cb1cacf) · 2025-05-27T09:56:19Z · feat: add comparison operators for ItemType

Adds ItemType equality against ItemType/string by getId and corresponding Python equality/string representation; stub marks it unhashable. Endpoint remains factory-based C++ ItemStack construction. PR189 includes701's later public-constructor change outside this assignment, so that later behavior is not credited here. No tests added.

