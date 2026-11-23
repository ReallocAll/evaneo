<!-- retrieval: {"source_ids":["public:commit:37edd85996c7a51153ed68e879486c560ece8fcc","public:commit:5628cd5b700432ce1d0ad2f80ec4799ed4949f5b","public:commit:721f412dda9397c609064ea8b84a2c6bf46ea4e4","public:commit:888c0ad9739893b0df43a83ab69eb0a3f8037f7a","public:commit:921342b0750c858253911c50844be5d880a8a383","public:commit:92cc35a47e600ec41b6990b8c6cd65f5b1621b9a","public:commit:b188d49d0df5e76354ec04190f7d92a348267f0e","public:commit:c0ac26ef101e52d3540f7f7922268b6f0e830def","public:commit:ce77169007a43b4fad6fad406f9903cec3089da3","public:commit:cfde59be08acccd6320d423c0111c6cc87b8fb0c","public:commit:d10ceb34829788095b48f018bdc29de1fee87ff7","public:commit:d86e3e8463543ac81b369753b325d0854d63b99c","public:commit:f49b4a70a155827e58602b5211e184f198062896"],"source_type":"public","date":"2025-02-14..2025-02-23","topics":["lifetime","concurrency","ffi","testing","build","recovery","diagnosis","review","selection","refactoring"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
# ABI-shaped utilities, tests and recovery limits {#abi-shaped-utilities-tests-and-recovery-limits}

## Compact strings and versions {#compact-strings-and-versions}

238–244 replace a larger semantic-version representation with SemVersionBase over an 8-byte StaticOptimizedString, yielding a 24-byte native layout.244 also fixes the old unequal-version self-tuple comparison and replaces the same-core prerelease exception path with numeric/alphabetic comparison and '-'/'+' formatting. Tests cover ordinary version ordering; numeric prerelease components still use stoi, whose range can be exceeded. The historical repair is real; comprehensive SemVer validity and unbounded numeric ordering are not demonstrated.

The string stores a pointer plus byte metadata, choosing static borrowing or aligned dynamic allocation. Copies choose ownership based on length rather than the source's storage tag. A short dynamically owned source can therefore yield a borrowed copy, which dangles when the source dies. reset and assignment overwrite existing owned storage without releasing it. The tests' literals, live backing string, long construction and initially empty assignment destinations do not exercise these transitions. Size conformance and happy-path values are insufficient ownership tests. Endpoint snapshots retain the exact implementation.

## Function wrapper evolution and attribution {#function-wrapper-evolution-and-attribution}

231–233 are incomplete scaffolding.234 explicitly imports a LeviLamina reference implementation, credited in both the message and source links. It adds inline/heap storage, vtable-managed copy/move/destroy and cv/ref/noexcept invocation machinery. The intermediate implementation has missing returns and alignment-offset array-pointer arithmetic hazards.261 repairs some template/return issues, then263 substantially narrows the design to a native allocator adapter, rather than merely fixing one constructor.

The rewritten263 specialization handles Copyable Return(Xs...) const with an empty argument pack in its base instantiation, and lacks the former general call interface. Heap-target branches have void-pointer copy/delete/assignment issues when instantiated; implicit wrapper copying does not invoke the target-aware vtable clone. Nonzero embedded offsets still use array-pointer arithmetic. The actually used zero-argument allocator function pointer may avoid these generic branches, so this is a static applicability boundary, not an observed allocator crash.264's alignas(max_align_t) explicitly addresses a reported Linux startup crash. A copied external utility still needs local ABI and ownership review, especially after simplification.

## Synchronization and parser recovery {#synchronization-and-parser-recovery}

246 adds a recursive SpinLockImpl with an atomic owner value but separate empty-check and owner-store. Two contenders can both observe empty and acquire; atomic storage alone does not make that operation atomic. The contention test increments an atomic counter, which can remain correct even when mutual exclusion fails. Wrong-owner and recursive tests have value, but do not close that gap.247 uses the lock while resolving deferred block descriptors, making its exclusion contract relevant beyond the standalone utility.

272 implements named NBT loading. Type, name and allocation errors propagate, but tag->load's Result is ignored. Compound loading clears its contents, loops until the entire input is exhausted and inserts EndTag rather than terminating at the compound's end marker. Nested containers can consume outer bytes, and failure leaves partial contents. These are bounded static counterexamples directly in the patch, not a general audit of unrelated parsers. No nested/malformed fixtures or round-trip tests accompany it.

## Test evidence {#test-evidence}

Actual test additions are static-optimized-string238, test registration239, SemVersion244, SpinLock246, and their merge253. Their content was read directly or through exact completed PR reuse. No weak-entity, packet reentrancy, nested NBT or native-host tests appear in this target range. Wheel builds explicitly disable testing.298 intends to exclude a clang-tidy check but leaves adjacent entries without a separating comma in its folded Checks value; effective tool selection was not executed or assumed. No tests or upstream tools were run.


<!-- PER-COMMIT RECORDS -->

## Individual commit records {#individual-commit-records}


<a id="commit-231"></a>
### 231. fix: change type of `Overload::AllocFunction` to `brstd::copyable_function` {#commit-231}

[cfde59be08acccd6320d423c0111c6cc87b8fb0c](https://github.com/EndstoneMC/endstone/commit/cfde59be08acccd6320d423c0111c6cc87b8fb0c) · 2025-02-14T17:04:50Z · author Vincent.

Parents: `b1abbc204b675c53225abb9abe4ba0fa649c25dc`. Full message and sources: parent 1.

Changes command Overload allocator from raw function pointer to a64-byte brstd::copyable_function representation. Adds only vtable/storage/inheritance skeleton, with no usable construction/invocation implementation; subsequent232–234 fill it in. Params offset changes to72 while later comments remain stale until239. This is an ABI-sized staged port, not a working standard-library replacement yet.

Coverage: 3 all-parent changed-file occurrences; 0 exact prior PR133 file-patch occurrences reused.


<a id="commit-232"></a>
### 232. feat: draft implementation of brstd::copyable_function (not completed) {#commit-232}

[5628cd5b700432ce1d0ad2f80ec4799ed4949f5b](https://github.com/EndstoneMC/endstone/commit/5628cd5b700432ce1d0ad2f80ec4799ed4949f5b) · 2025-02-14T19:44:29Z · author Vincent.

Parents: `cfde59be08acccd6320d423c0111c6cc87b8fb0c`. Full message and sources: parent 1.

Explicitly labeled unfinished draft adds empty/target construction and vtable copy/move/destroy/invoke branches. Source has unresolved T in storage and void*-typed target operations, incomplete invoke declarations and default copying; it is not a usable final utility. No AI attribution is present; draft-like wording or comments are not evidence of AI authorship.

Coverage: 2 all-parent changed-file occurrences; 0 exact prior PR133 file-patch occurrences reused.


<a id="commit-233"></a>
### 233. refactor: update `copyable_function` constructors and assignment operators {#commit-233}

[721f412dda9397c609064ea8b84a2c6bf46ea4e4](https://github.com/EndstoneMC/endstone/commit/721f412dda9397c609064ea8b84a2c6bf46ea4e4) · 2025-02-14T23:40:54Z · author Vincent.

Parents: `5628cd5b700432ce1d0ad2f80ec4799ed4949f5b`. Full message and sources: parent 1.

Reworks draft constructors/assignment: default constructor, delegating nullptr construction, declared move/copy operations and construct_from_function forwarding. Required base functionality is not yet implemented in this intermediate tree. Resets via empty swap;234 replaces the draft rather than completing this exact design.

Coverage: 1 all-parent changed-file occurrences; 0 exact prior PR133 file-patch occurrences reused.


<a id="commit-234"></a>
### 234. feat: add copyable_function implementation from LeviLamina {#commit-234}

[c0ac26ef101e52d3540f7f7922268b6f0e830def](https://github.com/EndstoneMC/endstone/commit/c0ac26ef101e52d3540f7f7922268b6f0e830def) · 2025-02-15T15:43:14Z · author Vincent.

Parents: `721f412dda9397c609064ea8b84a2c6bf46ea4e4`. Full message and sources: parent 1.

Explicitly imports a LeviLamina-referenced function-wrapper implementation at fbb3c97, preserving that external project attribution. Replaces draft with inline/heap target selection, per-target vtables, copy/move/destruction, invocation qualifiers and constructor constraints; allocator signature becomes const-callable. Full intermediate diff read because its prior blobs differ from aggregate PR133. Static concerns include array-pointer arithmetic in embedded_target_ptr, missing returned references in nullptr/copy assignment, and exception-sensitive destroy-before-copy. No upstream execution or blanket correctness endorsement.

Coverage: 3 all-parent changed-file occurrences; 0 exact prior PR133 file-patch occurrences reused.


<a id="commit-238"></a>
### 238. feat: implement `StaticOptimizedString` {#commit-238}

[921342b0750c858253911c50844be5d880a8a383](https://github.com/EndstoneMC/endstone/commit/921342b0750c858253911c50844be5d880a8a383) · 2025-02-15T20:12:39Z · author Vincent.

Parents: `0c06473d1719cfdb79a3395204ebc7c541a93699`. Full message and sources: parent 1.

Implements eight-byte StaticOptimizedString using PackedPointer metadata, short static borrowing and aligned dynamic storage with size prefix; tests exactly reuse PR133 reading. Short dynamic source copies become borrowed because copying chooses storage by length, and reset/copy/move assignment can discard owned pointers without release. Tests cover ordinary literals/live backing storage, not all ownership transitions. Header references PackedPointer before239 adds it; intermediate tree is staged.

Coverage: 2 all-parent changed-file occurrences; 1 exact prior PR133 file-patch occurrences reused.


<a id="commit-239"></a>
### 239. feat: add `Bedrock::PackedPointer` storage type {#commit-239}

[ce77169007a43b4fad6fad406f9903cec3089da3](https://github.com/EndstoneMC/endstone/commit/ce77169007a43b4fad6fad406f9903cec3089da3) · 2025-02-15T20:15:01Z · author Vincent.

Parents: `921342b0750c858253911c50844be5d880a8a383`. Full message and sources: parent 1.

Adds PackedPointer implementation via exact PR133 reuse, satisfying238's representation dependency; registers static-string tests in CMake and removes stale Overload offset comments. Pointer packing is native ABI-specific, not universal portable pointer representation. No tests executed.

Coverage: 3 all-parent changed-file occurrences; 1 exact prior PR133 file-patch occurrences reused.


<a id="commit-244"></a>
### 244. refactor: add `SemVersionBase` and derive `SemVersion` from `SemVersionBase<Bedrock::StaticOptimizedString>` {#commit-244}

[b188d49d0df5e76354ec04190f7d92a348267f0e](https://github.com/EndstoneMC/endstone/commit/b188d49d0df5e76354ec04190f7d92a348267f0e) · 2025-02-15T23:03:08Z · author Vincent.

Parents: `3bb01af0d23bfb3e08f3b915d2f6ef045625b658`. Full message and sources: parent 1.

Introduces SemVersionBase with StaticOptimizedString-backed SemVersion, compact24-byte ABI and prerelease ordering/formatting tests through exact PR133 reuse. Adds implicit string_view conversion and CMake test source directly. This supersedes earlier incomplete SemVersion implementation; numeric prerelease conversion uses stoi with overflow boundary untested. Ordinary tests do not prove complete semantic-version conformance or string-ownership safety.

Coverage: 5 all-parent changed-file occurrences; 3 exact prior PR133 file-patch occurrences reused.


<a id="commit-246"></a>
### 246. feat: add implementation for `SpinLockImpl` {#commit-246}

[37edd85996c7a51153ed68e879486c560ece8fcc](https://github.com/EndstoneMC/endstone/commit/37edd85996c7a51153ed68e879486c560ece8fcc) · 2025-02-16T13:47:04Z · author Vincent.

Parents: `0e3f6516800aa8469fb1d635ca598f852c49b386`. Full message and sources: parent 1.

Adds SpinLockImpl and tests through exact completed PR133 reuse; CMake registration read directly. Atomic owner load and later store are separate, allowing competing threads to both enter. The contention test increments an atomic counter, which cannot itself prove mutual exclusion; other tests cover wrong-owner/recursion errors. No lock stress test executed.

Coverage: 4 all-parent changed-file occurrences; 3 exact prior PR133 file-patch occurrences reused.


<a id="commit-247"></a>
### 247. fix: correct implementation of `BlockDescriptor::tryGetBlockNoLogging` {#commit-247}

[d10ceb34829788095b48f018bdc29de1fee87ff7](https://github.com/EndstoneMC/endstone/commit/d10ceb34829788095b48f018bdc29de1fee87ff7) · 2025-02-16T13:58:47Z · author Vincent.

Parents: `37edd85996c7a51153ed68e879486c560ece8fcc`. Full message and sources: parent 1.

Replaces direct tryGetBlockNoLogging native symbol with ResolveHelper::resolve and a lock-protected deferred resolution path; header/body exactly reuse PR133 and changed symbol mapping read directly. Correctness depends on lock implementation, including246's check/store race; no concurrent descriptor-resolution outcome observed.

Coverage: 3 all-parent changed-file occurrences; 2 exact prior PR133 file-patch occurrences reused.


<a id="commit-263"></a>
### 263. ix: correct constructor implementations of `brstd::copyable_function` {#commit-263}

[888c0ad9739893b0df43a83ab69eb0a3f8037f7a](https://github.com/EndstoneMC/endstone/commit/888c0ad9739893b0df43a83ab69eb0a3f8037f7a) · 2025-02-19T17:06:38Z · author Vincent.

Parents: `92bc5b750f93f0bf1e08db589c407fc7d288968b`. Full message and sources: parent 1.

Rewrites copyable_function from general cv/ref/noexcept-capable template machinery to a much smaller native ABI adapter. Only unqualified CopyableReturn(Xs...) const specialization remains, instantiating base without Xs; template constructor excludes self but implicit wrapper copying is no substitute for target-aware cloning. Heap-copy/destroy expressions operate through void* targets and are unsafe or ill-formed when instantiated; nonzero SBO offset still uses array-pointer arithmetic. The actually used allocator function pointer can avoid these generic branches. LeviLamina reference credit is retained; no broad std::function conformance claim.

Coverage: 2 all-parent changed-file occurrences; 0 exact prior PR133 file-patch occurrences reused.


<a id="commit-264"></a>
### 264. fix: resolve a crash on Linux by aligning class `function_base_impl::storage` to std::max_align_t {#commit-264}

[f49b4a70a155827e58602b5211e184f198062896](https://github.com/EndstoneMC/endstone/commit/f49b4a70a155827e58602b5211e184f198062896) · 2025-02-19T18:05:19Z · author Vincent.

Parents: `888c0ad9739893b0df43a83ab69eb0a3f8037f7a`. Full message and sources: parent 1.

Adds alignas(std::max_align_t) to the rewritten function storage. Explicit message reports a Linux startup crash fix. The 261 removal then264 restoration of alignment is a concrete ABI-sensitive revision chain; static inspection does not reproduce the crash or prove all target paths safe.

Coverage: 1 all-parent changed-file occurrences; 0 exact prior PR133 file-patch occurrences reused.


<a id="commit-272"></a>
### 272. feat: add `NbtIo::readNamedTag` {#commit-272}

[92cc35a47e600ec41b6990b8c6cd65f5b1621b9a](https://github.com/EndstoneMC/endstone/commit/92cc35a47e600ec41b6990b8c6cd65f5b1621b9a) · 2025-02-20T01:32:57Z · author Vincent.

Parents: `6f3a2e8c6ceb54a18ea482560b736b33ea2072ce`. Full message and sources: parent 1.

Implements NbtIo::readNamedTag and CompoundTag::load with Result propagation for type/name/tag creation, but ignores the returned result from tag->load. Compound clears old contents then reads until bytes exhausted, inserting EndTag rather than terminating at it. Thus nested streams and partial-load failure need scrutiny; no malformed/nested NBT fixtures or round-trip tests accompany this patch.

Coverage: 3 all-parent changed-file occurrences; 0 exact prior PR133 file-patch occurrences reused.


<a id="commit-298"></a>
### 298. chore: disable `readability-simplify-boolean-expr` in .clang-tidy {#commit-298}

[d86e3e8463543ac81b369753b325d0854d63b99c](https://github.com/EndstoneMC/endstone/commit/d86e3e8463543ac81b369753b325d0854d63b99c) · 2025-02-23T16:53:34Z · author Vincent.

Parents: `de49d084e7917fde9c0ff87ece490dfe88e97d39`. Full message and sources: parent 1.

Adds readability-simplify-boolean-expr exclusion to clang-tidy text. Adjacent exclusions lack a separating comma in the folded Checks value, so intended selection is not proven effective; no lint invocation was run.

Coverage: 1 all-parent changed-file occurrences; 0 exact prior PR133 file-patch occurrences reused.
