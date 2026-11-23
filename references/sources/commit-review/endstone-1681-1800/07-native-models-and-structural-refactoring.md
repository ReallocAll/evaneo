<!-- retrieval: {"source_ids":["public:commit:08a49407db01c8f6a97904835152b74d9022c2fd","public:commit:12b0c30fd54b3ff456b928b47e019c9d29536c2c","public:commit:32b1de91bdac014c7b8d602742b63e3f34ed75ae","public:commit:474c6e7f6f6d0862befb27b3657a211764033751","public:commit:5455e6ae997b6f363cf56e9e469e5e3123f05015","public:commit:5e067d473f66006a341ca8fbbc82cbfeb5253911","public:commit:74816a73420ea480a42dd2fc8fbd09011ca1d3f1","public:commit:769fd841666427103c3f9bebdd00552566810bae","public:commit:7ca9fc21f5d0e225df19ea0d198e3da41cf9718c","public:commit:86791c078eef64220c05e681d3da150a2c1e9521","public:commit:96111fbcd60ac2acf6138ff1cc8e6bddbc26824e","public:commit:a49bb23cff285bcbf293bfc1e45f72c8569016a7","public:commit:b497b19b0ca9e5ed924c79d472880bf74eb554d9","public:commit:b6b1c633e70f04cd4b98525b46a2b1a2004dc97b","public:commit:d2a77d380eda48a2e27f9df47c05d1da25109fff","public:commit:e598a9c2b0bb975ee734b36692e19c1356aeba2a","public:commit:fb0bf839d489f7a8e37272497391a65f0a0b5a45"],"source_type":"public","date":"2024-09-13..2024-09-14","topics":["lifetime","concurrency","ffi","testing","build","review","selection","refactoring"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
# Native model refinement and structural refactoring {#native-model-refinement-and-structural-refactoring}


Endstone commits 1681–1800, dated August 29–September 14, 2024.

## Titles are an index, not a semantic classification {#titles-are-an-index-not-a-semantic-classification}

The September 13–14 series repeatedly says move or refactor, but its content spans exact file relocations, body extraction, encapsulation, native layout reconstruction and corrective fixes. Exact moves and unchanged method bodies receive compact treatment. Meaningful exceptions remain explicit: RelativeFloat's flag type, observer virtual slots, CallStack fields, ValueOrRef's discriminant/reference semantics, logging parameter type, HashedString initialization, GameRefs ownership wrappers and publisher mutex representation.

The central build recursively discovers core/runtime source files, explaining why extracting functions into new .cpp files need not change a source list. It does not prove those files compile, link or preserve exported symbols. Include-path changes, especially the unusual relative shared_constants includes, remain source-visible boundaries rather than tested success. Existing hash-vector tests and UUID round-trip assertions are retained, not expanded into comprehensive ABI tests.

## Ownership vocabulary and correction chains {#ownership-vocabulary-and-correction-chains}

GameRefs introduces separate owner, weak and stack-result storage, with EntityContext specialization. This improves explicit representation, but names alone do not establish lifetime safety: EntityContext stores references to registries, and weak access returns a reference/pointer after a temporary shared lock ends. Actor enumeration and form callbacks contain explicit TODOs questioning correct usage. These are valuable evidence of uncertainty, which should survive synthesis instead of being rewritten as a finished design rationale.

The series also creates and repairs local regressions. SynchedActorDataEntityWrapper acquires an unnecessary virtual destructor at 1796, then loses it at 1798 with a 48-byte assertion. The log hook's priority changes from uint32_t to a named enum at 1794 and returns to uint32_t at 1798, preserving a named enum only for switch interpretation. HashedString's move out of line also initializes last_match_ in constructors that previously did not. These sequences distinguish corrective engineering from a blanket preference for abstraction or renaming.

Publisher modeling at 1800 replaces opaque bytes with typed intrusive-list/subscription fields and changes the mutex representation/model. The code remains a skeletal view of engine objects; it contains no complete subscription algorithm or concurrency proof. Size assertions and field-offset comments express the intended native layout, not a reviewer-run validation. Likewise certificate flag naming clarifies an existing self-signed XUID gate, not new cryptographic verification.

Use these cases to review bulk refactors with exact relocation proofs while isolating semantic changes, to separate wrapper ownership from referent ownership, and to retain unknown native behavior honestly. No upstream implementation, tests, build or host runtime was executed.

## Individual commit dispositions {#individual-commit-dispositions}

<a id="commit-1782"></a>
### Commit 1782 {#commit-1782}

2024-09-13T12:30:24Z · `b6b1c633e70f04cd4b98525b46a2b1a2004dc97b` · feat: update actor.h

Replaces several Actor unknown-field names with initialization parameters, alias, previous render transform, last-player-hurt time and bone matrices. A 72-byte opaque region becomes optional matrix plus integer while stated downstream offsets remain. These are reverse-engineered layout claims, not a feature implementation or demonstrated cross-platform validation.

Source: [individual commit](https://github.com/EndstoneMC/endstone/commit/b6b1c633e70f04cd4b98525b46a2b1a2004dc97b). Classification: native_model_refinement.

<a id="commit-1783"></a>
### Commit 1783 {#commit-1783}

2024-09-13T13:29:08Z · `5455e6ae997b6f363cf56e9e469e5e3123f05015` · refactor: move class EnableNonOwnerReferences into separate header file

Moves EnableNonOwnerReferences into its own header without changing its constructor/control-block/default-destructor behavior. The default destructor's lack of explicit pointer invalidation is inherited, not a new fix or regression from this extraction. Class and include boundaries improve, but native object lifetime still requires contextual reasoning.

Source: [individual commit](https://github.com/EndstoneMC/endstone/commit/5455e6ae997b6f363cf56e9e469e5e3123f05015). Classification: verified_extraction.

<a id="commit-1784"></a>
### Commit 1784 {#commit-1784}

2024-09-13T13:46:16Z · `b497b19b0ca9e5ed924c79d472880bf74eb554d9` · refactor: move Certificate class definition to a separate source file

Moves certificate accessors out of line, makes representation private and names the formerly unknown flag self_signed. ExtendedCertificate's trust_self_signed parameter clarifies an existing XUID gate rather than adding cryptographic verification. Git's similarity-based header-to-source rename is not the logical move: UnverifiedCertificate now lives inside certificate.h. All actual additions/deletions were read.

Source: [individual commit](https://github.com/EndstoneMC/endstone/commit/b497b19b0ca9e5ed924c79d472880bf74eb554d9). Classification: encapsulation_and_named_semantics.

<a id="commit-1785"></a>
### Commit 1785 {#commit-1785}

2024-09-13T14:12:29Z · `32b1de91bdac014c7b8d602742b63e3f34ed75ae` · refactor: move BaseGameVersion and SemVersion classes into their own separate files

Separates BaseGameVersion, SemVersion and the Common version function into dedicated headers/source paths and updates users. The data members and function body are retained. This is dependency organization with build consequences through includes, not a new version-parsing policy.

Source: [individual commit](https://github.com/EndstoneMC/endstone/commit/32b1de91bdac014c7b8d602742b63e3f34ed75ae). Classification: verified_structural_change.

<a id="commit-1786"></a>
### Commit 1786 {#commit-1786}

2024-09-13T16:38:09Z · `a49bb23cff285bcbf293bfc1e45f72c8569016a7` · refactor: DataIO and StringByteOutput class

Moves byte-output serialization bodies out of headers, relocates PrintStream and separates StringByteOutput. All methods were read; the BytesDataOutput bodies are additionally compared exactly after whitespace/comment normalization. The existing short-string length mask and big-endian byte conversion remain. Do not describe the move as a serializer correctness rewrite.

Source: [individual commit](https://github.com/EndstoneMC/endstone/commit/a49bb23cff285bcbf293bfc1e45f72c8569016a7). Classification: verified_body_relocation.

<a id="commit-1787"></a>
### Commit 1787 {#commit-1787}

2024-09-13T17:17:42Z · `08a49407db01c8f6a97904835152b74d9022c2fd` · refactor: move mce::Color into separate source file

Moves Color conversion functions out of line, simplifies equivalent initialization/parentheses and relocates IntRange while renaming its members. The existing output includes a leading # whereas the input requires eight characters; that asymmetry is not fixed here. No parsing tests or new conversion algorithm appear.

Source: [individual commit](https://github.com/EndstoneMC/endstone/commit/08a49407db01c8f6a97904835152b74d9022c2fd). Classification: structural_change_with_small_cleanup.

<a id="commit-1788"></a>
### Commit 1788 {#commit-1788}

2024-09-13T19:13:54Z · `7ca9fc21f5d0e225df19ea0d198e3da41cf9718c` · refactor: move observers into separate files

Adds generic Subject/Observer layout, a subject-destroyed virtual callback and concrete social-observer callbacks while splitting their headers. Also replaces RelativeFloat's floating-point relative flag with bool and supplies constructor/value helpers. Command::collectOptionalArguments merely moves out of line. The title's relocation wording must not hide these ABI and semantic changes.

Source: [individual commit](https://github.com/EndstoneMC/endstone/commit/7ca9fc21f5d0e225df19ea0d198e3da41cf9718c). Classification: native_model_change.

<a id="commit-1789"></a>
### Commit 1789 {#commit-1789}

2024-09-13T19:26:58Z · `86791c078eef64220c05e681d3da150a2c1e9521` · refactor: UUID-related classes

Makes native UUID a simple two-int64 representation and moves Endstone conversion into EndstoneUUID helpers, preserving the six byte-reversal segments in both directions. Consumers and the existing round-trip test are updated. Its assertions remain the same; round-trip consistency is weaker than an independent known native-layout fixture, and no test was executed here.

Source: [individual commit](https://github.com/EndstoneMC/endstone/commit/86791c078eef64220c05e681d3da150a2c1e9521). Classification: boundary_extraction_with_tests.

<a id="commit-1790"></a>
### Commit 1790 {#commit-1790}

2024-09-13T19:39:52Z · `fb0bf839d489f7a8e37272497391a65f0a0b5a45` · refactor: move automatic_id.h to bedrock/core/utility

Relocates AutomaticID, renames its value member to runtime_id and moves DimensionType's alias; dimension callers follow the rename. AppPlatformListener's state field is also renamed. The represented widths and comparison logic are retained. This is naming/header organization, not an ID-allocation algorithm change.

Source: [individual commit](https://github.com/EndstoneMC/endstone/commit/fb0bf839d489f7a8e37272497391a65f0a0b5a45). Classification: verified_structural_change.

<a id="commit-1791"></a>
### Commit 1791 {#commit-1791}

2024-09-13T19:51:00Z · `74816a73420ea480a42dd2fc8fbd09011ca1d3f1` · refactor: move ErrorInfo class to bedrock/platform/check.h

Replaces opaque CallStack frame words with filename hash, string_view and line number, and wraps the existing frame vector in a CallStack member inside ErrorInfo. Existing size assertions are retained. The change gives the native structure semantic names but does not show stack capture, error propagation or runtime layout validation.

Source: [individual commit](https://github.com/EndstoneMC/endstone/commit/74816a73420ea480a42dd2fc8fbd09011ca1d3f1). Classification: native_model_refinement.

<a id="commit-1792"></a>
### Commit 1792 {#commit-1792}

2024-09-13T22:53:25Z · `769fd841666427103c3f9bebdd00552566810bae` · refactor: move ValueOrRef class to event_variant.h

Replaces ValueOrRef's integer discriminant and copy-return accessor with a bool pointer/value discriminant and reference-return accessor, updating form-event consumers. StorageAreaStateListener also replaces enable_shared_from_this inheritance with a shared state member and mutex alias. These are representation revisions, not pure moves. The ValueOrRef constructor is private and assigns a const union member; current engine-object reads do not prove every template construction path is usable.

Source: [individual commit](https://github.com/EndstoneMC/endstone/commit/769fd841666427103c3f9bebdd00552566810bae). Classification: representation_and_access_revision.

<a id="commit-1793"></a>
### Commit 1793 {#commit-1793}

2024-09-13T23:01:57Z · `d2a77d380eda48a2e27f9df47c05d1da25109fff` · refactor: move everything from bedrock/common to bedrock/

Moves common headers/source into more specific bedrock paths, including nine exact-blob renames, and updates all shown include sites. Nonrename hunks were read separately, including the unusual relative includes in shared_constants.cpp. The central CMake uses recursive source globs, so source additions need not have explicit list edits; successful configuration/build remains unverified.

Source: [individual commit](https://github.com/EndstoneMC/endstone/commit/d2a77d380eda48a2e27f9df47c05d1da25109fff). Classification: verified_bulk_relocation.

<a id="commit-1794"></a>
### Commit 1794 {#commit-1794}

2024-09-13T23:18:01Z · `96111fbcd60ac2acf6138ff1cc8e6bddbc26824e` · refactor: move BedrockLog::log_va to bedrock_event_logger.h

Splits logging declarations, names category/rule/level enums and changes hook priority from uint32_t to LogLevel while retaining the same numeric switch values. That type change can affect symbol identity even if its width matches. Commit 1798 restores uint32_t. The patch also moves the SemVersion path and adds direct bitset includes; it is not merely a file move.

Source: [individual commit](https://github.com/EndstoneMC/endstone/commit/96111fbcd60ac2acf6138ff1cc8e6bddbc26824e). Classification: mixed_structure_and_abi_change.

<a id="commit-1795"></a>
### Commit 1795 {#commit-1795}

2024-09-13T23:40:59Z · `12b0c30fd54b3ff456b928b47e019c9d29536c2c` · refactor: move HashedString to bedrock/core/string/string_hash.h

Moves HashedString methods out of line and fixes hash width to uint64_t. Ordinary and null constructors now initialize last_match_ to null, a real correction hidden in a relocation title. Hashing and cross-object equality-cache logic remain; move assignment still copies its string. Existing hash-vector tests only change their include path and do not add coverage of cached-pointer lifetime or construction.

Source: [individual commit](https://github.com/EndstoneMC/endstone/commit/12b0c30fd54b3ff456b928b47e019c9d29536c2c). Classification: extraction_with_initialization_fix.

<a id="commit-1796"></a>
### Commit 1796 {#commit-1796}

2024-09-14T01:18:42Z · `e598a9c2b0bb975ee734b36692e19c1356aeba2a` · refactor: add gamerefs and correct related implementations

Introduces GameRefs storage traits for shared-pointer and EntityContext cases, splits owner/weak/stack-result types and replaces public field access with helpers in actor enumeration and form callbacks. The code explicitly questions correct usage in TODOs. EntityContext keeps registry references, and weak-lock access returns after the temporary strong lock ends, so the names do not establish durable ownership. The patch also models GameSession fields and accidentally adds a virtual destructor to SynchedActorDataEntityWrapper, repaired at 1798. All 1,193 raw display lines were read in three contiguous pages.

Source: [individual commit](https://github.com/EndstoneMC/endstone/commit/e598a9c2b0bb975ee734b36692e19c1356aeba2a). Classification: gamerefs_redesign.

<a id="commit-1798"></a>
### Commit 1798 {#commit-1798}

2024-09-14T16:29:11Z · `5e067d473f66006a341ca8fbbc82cbfeb5253911` · fix: correct struct size of SynchedActorDataEntityWrapper

On the local branch after 1796, removes the new virtual destructor, restoring SynchedActorDataEntityWrapper's three pointers plus 24-byte weak context and asserting 48 bytes on both platforms. Also restores log priority to uint32_t, relocates EnTT traits and inherits constructors for owner/stack-result wrappers. This corrects multiple native-model edges; the title names only the struct-size repair.

Source: [individual commit](https://github.com/EndstoneMC/endstone/commit/5e067d473f66006a341ca8fbbc82cbfeb5253911). Classification: layout_and_abi_repair.

<a id="commit-1800"></a>
### Commit 1800 {#commit-1800}

2024-09-14T17:18:35Z · `474c6e7f6f6d0862befb27b3657a211764033751` · refactor: move pubsub-related classes into their own files

Splits publisher infrastructure and replaces opaque subscription bytes with an intrusive-list model plus subscription ownership/context fields. It also changes MultiThreaded from inherited recursive_mutex to a contained std::mutex, and defines a separate recursive model; Linux SharedMutex maps to shared_timed_mutex. These changes affect layout/locking assumptions, not just filenames. The types remain skeletal native models without subscription algorithms or reviewer-run ABI tests.

Source: [individual commit](https://github.com/EndstoneMC/endstone/commit/474c6e7f6f6d0862befb27b3657a211764033751). Classification: publisher_model_revision.

## Coverage boundary {#coverage-boundary}

Findings rely on the linked public sources; external PR/issue discussions, dependencies, and native engine internals are outside the cited evidence. Runtime and current-release behavior were not tested.
