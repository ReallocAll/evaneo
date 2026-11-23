<!-- retrieval: {"source_ids":["public:commit:020877a6ef9d08287fd8b87036aef40b40b9515d","public:commit:0fea1dffa0bad8b854e553c68a56e7b3ae22e5bb","public:commit:24b6a578d51752a0863f9245e4f01cb3ded2f0a7","public:commit:4947cf72085ac2387d9e99d188b0b6a5654729bf","public:commit:4a4e413ed8474a25694440382a1515c6559e7187","public:commit:5b3fd86f19eecd0fb998491d0ee487891f5e3a53","public:commit:5b520487be624d779b4734df71528b762d789c92","public:commit:7ff77454194958eaa8091c9f78dd619af6ae00a8","public:commit:812a97021302dbf5ae13e54812a888acac4836e2","public:commit:81f76156c2f8a64980715cf8df0417ec736c8428","public:commit:92521a59699c1979a40e281cf6428afbab93e971","public:commit:abe42714d0cc81147b2d9b62f56fa1d3ba30ebf7","public:commit:c173222bad83959e2385ffc2a5a582eba8a24dba","public:commit:c917c4f3cd86c978aa099145a6a7952d704d48ab","public:commit:caf77eaeacdf6d1d5e65cfaf47020580bcfdcdb3","public:commit:d2d5db75a2aa2eac01d64e1ada818176f5012801","public:commit:ed0e08eb76a7f9681259fda0be8d624e1453e1da","public:commit:f878a0c77045b8da3fda450be8b60650fc616994","public:commit:f9b1cdb59ad6632ee93403359f6fdb908d46ce71"],"source_type":"public","date":"2026-02-24..2026-02-25","topics":["ffi","testing","build","api","diagnosis","documentation","selection","refactoring","networking"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="rn01-build-modernization-is-a-sequence-of-dependency-and-public-surface-decisions"></a>
# Build modernization is a sequence of dependency and public-surface decisions {#rn01-build-modernization-is-a-sequence-of-dependency-and-public-surface-decisions}

## Preserve the ancestry boundary {#preserve-the-ancestry-boundary}

The2026 sequence begins from upstream commit1a169895a900c9fc4841c556e16514182b75faf8, a2015 merge authored by Alex Howland. The target's new work is the selected43-commit modernization sequence. The inherited RakNet transport algorithms, third-party code and historical manuals are not attributed to the target. The old source is inspected for structural equivalence and local call-site context; its entire historical development is not reinterpreted as present-day style.

The initial CMake minimum sweep is mechanically verified:69 files are exactly the3.5 replacement after CRLF normalization, six are line-ending-only, and two residual variants implement the same spacing/version edit. Pointer casts in Windows FormatMessage diagnostics follow. Those casts address C++ formatting argument types; they do not transcode a wide string to narrow encoding and have no accompanying platform result.

## Target-oriented packaging, then simplification {#target-oriented-packaging-then-simplification}

Commit004 replaces global compiler/linker string manipulation with target-based settings, raises the root to CMake3.14/C++11, adds install/export package files and a sample helper, and guards optional extension dependencies. Static and shared targets initially coexist. Commit006 consolidates them into one RakNet target selected by BUILD_SHARED_LIBS, default OFF, with the relevant static/DLL defines. This reduces target duplication but removes the old ability to build both variants in one configuration.

The source/header/sample tree then moves to include/RakNet, src and samples. Exact blob and CRLF-only equivalence proofs account for most of the movement. Root path wiring arrives in a following commit, so the message of the move should not be treated as proof that every intermediate commit already configures. Later, extensions and libcat receive their own locations with hundreds more exact moves.

A custom sample helper introduced early is removed in018 in favor of ordinary CMake declarations. The next patch replaces broad globbing with explicit source lists for many samples and co-locates small shared source files. These reversals argue against treating either a custom helper or all globbing as a lasting personal rule. The observed direction is the particular build graph becoming simpler and more explicit, with exceptions retained where needed.

## Titles conceal consequential defaults {#titles-conceal-consequential-defaults}

Several changes are larger than their titles suggest:
- The extension reorganization also raises C++11 to C++14 and defaults samples/extensions OFF.
- Version metadata is briefly removed while package-version generation still exists, then restored as4.081 in024. This is a transient chain state, not a final-state bug claim.
- Tests default OFF in024, then return ON when GoogleTest is introduced in033.
- The test migration in041 also changes PostgreSQLInterface detection/linking to libpq::libpq.

The final inspected root is CMake3.14, project version4.081, C++14, one static-by-default RakNet target, samples/extensions OFF and tests ON. Package exports use the RakNet namespace and SameMajorVersion version compatibility. That declared CMake compatibility is not a binary ABI measurement.

## Dependency replacement and its limits {#dependency-replacement-and-its-limits}

The Conan migration removes bundled bzip2, libjpeg, miniupnpc, PortAudio and Speex copies while retaining and relocating libcat. Source identity proves1,144 of1,148 deleted files match the upstream boundary; the four exceptions are local CMake files already reviewed. The new declared requirements include bzip2, libjpeg9f, miniupnpc2.2.5, OpenSSL3.6.1 and PortAudio19.7. A separate Speex1.2.1 recipe uses a pinned source hash and Meson with tools/tests disabled, but is not automatically a root dependency. Optional RakVoice therefore still needs an appropriate package setup.

OpenSSL discovery/linking is present while the library feature macro remains disabled by default. Merely finding a crypto library does not prove a security feature is enabled. Removing /GS-, /GR-, /W0 and -w later stops forcing those compiler settings for the core target; it is not a demonstrated security improvement or a uniform warning policy for every extension.

The XML parser replacement is a real call-site migration, not a file deletion alone. A legacy Frank Vanden Berghen/Business-Insight parser and its license entry are removed; pugixml1.14 is added. RoomsBrowserGFx3 SaveProperty/LoadProperty become document operations, including different behavior for absent/empty values and ignored parse/save returns. No tests establish identical persistence semantics. The absence of compile/link results also limits confidence in optional sample integration.

## Use this case {#use-this-case}

When modernizing a native build, compare the final public target, options, default feature set, language level and dependency discovery with each earlier state. Prove bulk moves mechanically and spend reading effort on their residual CMake/call-site deltas. Preserve the reasons for simplifying abstractions and narrowing optional dependencies without turning every intermediate choice into doctrine. Validate only the configurations actually needed by a downstream task; this static research did not build, link, install or execute any upstream project.

Sources: bundled dossiers 001–013, 016–026, 033 and 041 and the pinned public commits below. [Large changes need provenance accounting before engineering interpretation](vendor-provenance-and-proportionate-review.md#verified-bulk-and-local-exceptions) summarizes the original structural accounting; [Modern documentation needs both content provenance and serving-model checks](documentation-migration-and-static-delivery.md) covers documentation. The path-level comparison files and final working-tree snapshots are not bundled, so the reported counts were not independently reproduced for this release.

## Exact commit navigation {#exact-commit-navigation}

- [001 d2d5db75a2aa: chore: update CMake minimum required version to 3.5 across all CMakeLists.txt files](../dossiers/001-d2d5db75a2aa.md) · [public source](https://github.com/wu-vincent/RakNet/commit/d2d5db75a2aa2eac01d64e1ada818176f5012801)
- [002 ed0e08eb76a7: chore: cast messageBuffer to const char* in debug print statements](../dossiers/002-ed0e08eb76a7.md) · [public source](https://github.com/wu-vincent/RakNet/commit/ed0e08eb76a7f9681259fda0be8d624e1453e1da)
- [003 f878a0c77045: chore: cast messageBuffer to const char* in debug print statements in RakNetSocket2_Berkley.cpp](../dossiers/003-f878a0c77045.md) · [public source](https://github.com/wu-vincent/RakNet/commit/f878a0c77045b8da3fda450be8b60650fc616994)
- [004 c917c4f3cd86: refactor: modernize CMake build system to target-based CMake 3.14](../dossiers/004-c917c4f3cd86.md) · [public source](https://github.com/wu-vincent/RakNet/commit/c917c4f3cd86c978aa099145a6a7952d704d48ab)
- [005 81f76156c2f8: chore: remove Visual Studio .sln files, CMake generates projects now](../dossiers/005-81f76156c2f8.md) · [public source](https://github.com/wu-vincent/RakNet/commit/81f76156c2f8a64980715cf8df0417ec736c8428)
- [006 92521a59699c: refactor: use single RakNet target with BUILD_SHARED_LIBS](../dossiers/006-92521a59699c.md) · [public source](https://github.com/wu-vincent/RakNet/commit/92521a59699c1979a40e281cf6428afbab93e971)
- [007 7ff774541949: refactor: restructure directory layout to conventional C++ project structure](../dossiers/007-7ff774541949.md) · [public source](https://github.com/wu-vincent/RakNet/commit/7ff77454194958eaa8091c9f78dd619af6ae00a8)
- [008 caf77eaeacdf: refactor: update CMake paths for new directory layout](../dossiers/008-caf77eaeacdf.md) · [public source](https://github.com/wu-vincent/RakNet/commit/caf77eaeacdf6d1d5e65cfaf47020580bcfdcdb3)
- [011 020877a6ef9d: chore: remove hand-crafted iOS Xcode project](../dossiers/011-020877a6ef9d.md) · [public source](https://github.com/wu-vincent/RakNet/commit/020877a6ef9d08287fd8b87036aef40b40b9515d)
- [013 5b520487be62: chore: remove all legacy .vcproj files](../dossiers/013-5b520487be62.md) · [public source](https://github.com/wu-vincent/RakNet/commit/5b520487be624d779b4734df71528b762d789c92)
- [016 c173222bad83: chore: remove CmakeIncludes directory and legacy Find modules](../dossiers/016-c173222bad83.md) · [public source](https://github.com/wu-vincent/RakNet/commit/c173222bad83959e2385ffc2a5a582eba8a24dba)
- [017 abe42714d0cc: chore: remove all legacy .dsp files](../dossiers/017-abe42714d0cc.md) · [public source](https://github.com/wu-vincent/RakNet/commit/abe42714d0cc81147b2d9b62f56fa1d3ba30ebf7)
- [018 24b6a578d517: refactor: remove raknet_add_sample macro, use explicit CMake](../dossiers/018-24b6a578d517.md) · [public source](https://github.com/wu-vincent/RakNet/commit/24b6a578d51752a0863f9245e4f01cb3ded2f0a7)
- [019 4a4e413ed847: refactor: replace file(GLOB) with explicit sources; rename spaced dirs](../dossiers/019-4a4e413ed847.md) · [public source](https://github.com/wu-vincent/RakNet/commit/4a4e413ed8474a25694440382a1515c6559e7187)
- [020 4947cf72085a: chore: remove version specifier from project() in CMakeLists.txt](../dossiers/020-4947cf72085a.md) · [public source](https://github.com/wu-vincent/RakNet/commit/4947cf72085ac2387d9e99d188b0b6a5654729bf)
- [022 812a97021302: chore: add Conan-related files to .gitignore](../dossiers/022-812a97021302.md) · [public source](https://github.com/wu-vincent/RakNet/commit/812a97021302dbf5ae13e54812a888acac4836e2)
- [023 f9b1cdb59ad6: refactor: rename DependentExtensions/ to extensions/](../dossiers/023-f9b1cdb59ad6.md) · [public source](https://github.com/wu-vincent/RakNet/commit/f9b1cdb59ad6632ee93403359f6fdb908d46ce71)
- [024 5b3fd86f19ee: refactor: simplify CMake configuration by removing unused alias targets](../dossiers/024-5b3fd86f19ee.md) · [public source](https://github.com/wu-vincent/RakNet/commit/5b3fd86f19eecd0fb998491d0ee487891f5e3a53)
- [026 0fea1dffa0ba: refactor: remove redundant target_compile_options for RakNet in CMake configuration](../dossiers/026-0fea1dffa0ba.md) · [public source](https://github.com/wu-vincent/RakNet/commit/0fea1dffa0bad8b854e553c68a56e7b3ae22e5bb)
