<!-- retrieval: {"source_ids":["public:commit:0bba19ffa3c6b6b9d1e79c55a12999af9e58d8d1","public:commit:0eff4a2ba1450c217d4a167106d78ee73a99ca3a","public:commit:37a312705ea0a0db7fb4dc8fe16349f1ac8915e3","public:commit:3c21f907aafee7d09fd3d48d44942ed77070bc3e","public:commit:424e464e031bd0def15187d3821f158ed1b290c0","public:commit:4ea7715a7006f27c5ba5c9c9e2b41d24b4376f5b","public:commit:516b70533be4ee32c8d28e6d0aba3173b1eefc2e","public:commit:730765aaa75f6ce09ea6f04305f387792716235b","public:commit:840fe1e56acc42d418a8e53e519cc65c76b1adf5","public:commit:84ea0ee67ae9692e48b72dbd615caa7314e18af7","public:commit:9133f2ec0cb24910a73a19ba301f41e1d1d52961","public:commit:b48ca13c19e79eff4a13f8ab0c8f2ce80dff747d","public:commit:b710680efcd4d483f74bcf6e6337b847ebc3caac","public:commit:be7db7578d2b8b8a50ce586b0c8feb14149eecd0","public:commit:c19049e566cc4a4919360841e39c3059a059bd64","public:commit:c42fe7ead340fb29227fe16212c7b8b5cc613a1a","public:commit:d460b9259f12f3918ec5045bb6d192bdfa6bd6cf","public:commit:e56ecbd18590e1c50d442ca4a12963a5bb23ecee","public:commit:ff15c53555abde8709669079ea87187255db6f79"],"source_type":"public","date":"2024-08-29..2024-09-11","topics":["ffi","testing","build","performance","api","diagnosis","documentation","review","refactoring"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
# Native compatibility, typed hooks and build policy {#native-compatibility-typed-hooks-and-build-policy}


Endstone commits 1681–1800, dated August 29–September 14, 2024.

## Decision chain {#decision-chain}

The August–September compatibility work crosses three separate boundaries: consumer compiler/STL settings, native function-pointer representation, and version-specific address/layout data. They should not be collapsed into a single claim that matching a version string establishes compatibility. The plugin CMake path explicitly enforces MSVC/Clang and ABI-affecting flags. Its temporary fmt-link experiment and removal/restoration of the Debug guard show that build policy was revised in small increments. The release notes provide stronger motivation for libc++ than inference alone: they name Linux symbol errors.

The original-call redesign at 1702 removes manual return handling and asks the compiler to invoke a typed function/member pointer. That is a meaningful simplification, but 1703–1705 show the cost of crossing macro and ABI representation boundaries. In particular, storage for a member pointer and its adjustment word must match the chosen model. A zero adjustment is not evidence that all native multiple-inheritance cases are handled. This chain follows the prior unit's removal of template-static original-target caching; it does not reverse that decision.

Address maintenance is also iterative. 1769's Linux refresh is followed by two exact address repairs and a version-label repair, while 1771 improves diagnostics by identifying the failed hook. Those commits are counterexamples to treating a generated-looking numeric map or a claimed compatibility update as uninteresting, automatically correct noise. Full map comparison is useful for preserving exceptions; it cannot verify the native code at an address.

## Use and limits {#use-and-limits}

Use this evidence when choosing where to enforce an ABI contract, reviewing macro helpers, distinguishing typed invocation from portable calling-convention guarantees, or making hook failures actionable. Relevant context includes the full 1705 hook header and EndstoneHeaders.cmake, the endpoint CMake source globs, and each map's exact before/after audit. No compiler, linker, CI job or BDS process was run. Native offsets, claimed Linux fixes and platform support remain source-backed claims rather than reproduced outcomes. Neither the paper linked from the member-pointer code nor external compiler documentation was read in this bounded unit.

## Individual commit dispositions {#individual-commit-dispositions}

<a id="commit-1681"></a>
### Commit 1681 {#commit-1681}

2024-08-29T16:41:22Z · `840fe1e56acc42d418a8e53e519cc65c76b1adf5` · fix: support BDS 1.21.22 (linux)

Updates the Linux symbol-address map and Python Minecraft version to 1.21.22. All numeric changes were read and the entire TOML before/after mapping compared. Windows addresses remain on the previous build until 1683. This is a version-specific compatibility artifact, not evidence that arbitrary binaries with the same public version have compatible layouts.

Source: [individual commit](https://github.com/EndstoneMC/endstone/commit/840fe1e56acc42d418a8e53e519cc65c76b1adf5). Classification: compatibility_manifest.

<a id="commit-1682"></a>
### Commit 1682 {#commit-1682}

2024-08-29T17:59:26Z · `0bba19ffa3c6b6b9d1e79c55a12999af9e58d8d1` · fix: virtual function table of BlockSource

Adds collision-shape/AABB virtual entries to IBlockSource with platform conditionals. The immediate goal is the claimed BlockSource vtable repair. Commit 1701 subsequently moves the remaining methods into the derived BlockSource class and removes these conditionals; treat this as an intermediate ABI model, not the final design.

Source: [individual commit](https://github.com/EndstoneMC/endstone/commit/0bba19ffa3c6b6b9d1e79c55a12999af9e58d8d1). Classification: native_layout_revision.

<a id="commit-1683"></a>
### Commit 1683 {#commit-1683}

2024-08-29T21:18:10Z · `424e464e031bd0def15187d3821f158ed1b290c0` · feat: support BDS 1.21.22 (windows)

Refreshes the Windows 1.21.22 addresses and map timestamp. An initially clipped display was re-read completely. The changes are not all one displacement, so the TOML audit preserves each symbol rather than inferring correctness from a common shift. No native binary or server execution validates the addresses here.

Source: [individual commit](https://github.com/EndstoneMC/endstone/commit/424e464e031bd0def15187d3821f158ed1b290c0). Classification: compatibility_manifest.

<a id="commit-1697"></a>
### Commit 1697 {#commit-1697}

2024-08-30T14:19:18Z · `c19049e566cc4a4919360841e39c3059a059bd64` · fix: explicitly link endstone plugins to fmt::fmt

Explicitly links fmt privately to plugin targets. The subsequent CMake revision removes this extra link while retaining the interface dependency through endstone::headers. Preserve the short experiment rather than presenting explicit duplicate linkage as an enduring build policy.

Source: [individual commit](https://github.com/EndstoneMC/endstone/commit/c19049e566cc4a4919360841e39c3059a059bd64). Classification: intermediate_build_fix.

<a id="commit-1698"></a>
### Commit 1698 {#commit-1698}

2024-08-30T16:12:36Z · `d460b9259f12f3918ec5045bb6d192bdfa6bd6cf` · fix: CMake toolchains for C++ plugins

Moves ABI requirements into the plugin-consumer CMake path: require MSVC on Windows and Clang on Unix, force iterator debug level zero or libc++/PIC through cached global CMAKE_CXX_FLAGS, and retain fmt through the interface target. Comments explicitly connect these choices to BDS ABI compatibility; release notes later cite Linux symbol errors. Global forced flags affect the including build, a real integration cost. The existing Debug prohibition is temporarily removed.

Source: [individual commit](https://github.com/EndstoneMC/endstone/commit/d460b9259f12f3918ec5045bb6d192bdfa6bd6cf). Classification: build_abi_policy.

<a id="commit-1699"></a>
### Commit 1699 {#commit-1699}

2024-08-30T16:20:32Z · `b48ca13c19e79eff4a13f8ab0c8f2ce80dff747d` · fix: Debug mode is disabled again for C++ plugins

Restores the Debug-build prohibition shortly after 1698 and tells developers to use Release or RelWithDebInfo. The check reads CMAKE_BUILD_TYPE, so it should not be generalized to every multi-configuration generator. The actual CMake branch was read; neither configuration nor compilation was run.

Source: [individual commit](https://github.com/EndstoneMC/endstone/commit/b48ca13c19e79eff4a13f8ab0c8f2ce80dff747d). Classification: build_policy_restoration.

<a id="commit-1701"></a>
### Commit 1701 {#commit-1701}

2024-08-31T18:01:19Z · `4ea7715a7006f27c5ba5c9c9e2b41d24b4376f5b` · refactor: update virtual table of Actor and BlockSource, remove platform-specific macros

Corrects the BlockSource inheritance model by moving virtual entries from IBlockSource into derived BlockSource, including the collision-query signatures, and removes platform-specific slot workarounds. It also relocates the unchanged Actor component helper templates while unifying the hasComponent virtual slot. The meaningful change is the class/vtable model, not merely declaration order or a new nonvirtual forwarding wrapper.

Source: [individual commit](https://github.com/EndstoneMC/endstone/commit/4ea7715a7006f27c5ba5c9c9e2b41d24b4376f5b). Classification: native_layout_revision.

<a id="commit-1702"></a>
### Commit 1702 {#commit-1702}

2024-08-31T19:00:02Z · `37a312705ea0a0db7fb4dc8fe16349f1ac8915e3` · refactor: remove ENDSTONE_HOOK_CALL_ORIGINAL_RVO and clean up codes

Replaces std::function-based original-call machinery and manual return-value handling with typed free/member-function pointers and std::invoke, updating all call sites. Constructor helpers retain distinct Windows and Linux return conventions. A temporary fake Level pointer used for return handling disappears. This transfers more calling-convention work to typed C++ invocation, an inference from the implementation. The initial member-pointer conversion uses undersized storage on the Linux representation; 1705 adds the adjustment word.

Source: [individual commit](https://github.com/EndstoneMC/endstone/commit/37a312705ea0a0db7fb4dc8fe16349f1ac8915e3). Classification: hook_dispatch_redesign.

<a id="commit-1703"></a>
### Commit 1703 {#commit-1703}

2024-08-31T19:34:23Z · `e56ecbd18590e1c50d442ca4a12963a5bb23ecee` · refactor: use `##__VA_ARGS__` in favour of `__VA_ARGS__`

Adds comma-eliding variadic macros for zero-argument calls, changes the documented minimum Clang version to 9, and replaces a native BlockLegacy opaque integer with shared_mutex. Its factory-declaration macro also introduces an invalid token-paste placement, repaired at 1704. These are build and native-layout changes, not formatting noise; each hunk was read.

Source: [individual commit](https://github.com/EndstoneMC/endstone/commit/e56ecbd18590e1c50d442ca4a12963a5bb23ecee). Classification: mixed_compatibility_revision.

<a id="commit-1704"></a>
### Commit 1704 {#commit-1704}

2024-08-31T19:42:43Z · `0eff4a2ba1450c217d4a167106d78ee73a99ca3a` · fix(ci): linux build

Removes the erroneous token-paste operator from the factory declaration macro. The commit claims a Linux CI repair, consistent with the source correction, but this review did not inspect or rerun the CI job. It does not undo the zero-argument handling retained elsewhere.

Source: [individual commit](https://github.com/EndstoneMC/endstone/commit/0eff4a2ba1450c217d4a167106d78ee73a99ca3a). Classification: compile_repair.

<a id="commit-1705"></a>
### Commit 1705 {#commit-1705}

2024-09-01T00:11:35Z · `84ea0ee67ae9692e48b72dbd615caa7314e18af7` · fix: call original functions on Linux

Constructs a member-pointer representation containing the original code pointer and a zero adjustment word before casting it to the deduced member-function-pointer type. This addresses 1702's missing storage component and cites a paper whose contents were not examined here. Zero adjustment remains a layout assumption; the code is not a portable proof for every inheritance model or compiler ABI. It does not restore the previously removed per-template original-target cache.

Source: [individual commit](https://github.com/EndstoneMC/endstone/commit/84ea0ee67ae9692e48b72dbd615caa7314e18af7). Classification: hook_representation_repair.

<a id="commit-1722"></a>
### Commit 1722 {#commit-1722}

2024-09-02T18:01:35Z · `c42fe7ead340fb29227fe16212c7b8b5cc613a1a` · fix(ci): linux build

Replaces EnTT's overloaded helper with the local helper, rewrites the problematic formatter visitor, avoids capturing a structured-binding name in the factory visitor and adjusts declaration attribute order. The title reports a Linux CI fix. Most visit bodies are equivalent, but the formatter and capture changes are meaningful compatibility corrections rather than wholesale formatting. CI success is not independently verified.

Source: [individual commit](https://github.com/EndstoneMC/endstone/commit/c42fe7ead340fb29227fe16212c7b8b5cc613a1a). Classification: compiler_compatibility_revision.

<a id="commit-1732"></a>
### Commit 1732 {#commit-1732}

2024-09-04T20:34:10Z · `be7db7578d2b8b8a50ce586b0c8feb14149eecd0` · fix: hasher for ActorUniqueID

Changes the NetworkIdentifier hash's address handling from unsigned to signed. The low component still masks with 0xffffff, so this code does not hash all lower 32 bits. Collisions are permissible for a hash, and the source gives no benchmark or complete distribution argument. Preserve the exact native-compatibility change without declaring the hasher universally correct.

Source: [individual commit](https://github.com/EndstoneMC/endstone/commit/be7db7578d2b8b8a50ce586b0c8feb14149eecd0). Classification: native_hasher_revision.

<a id="commit-1767"></a>
### Commit 1767 {#commit-1767}

2024-09-10T11:59:54Z · `ff15c53555abde8709669079ea87187255db6f79` · feat: add support for BDS v1.21.23 on Windows

Marks Minecraft 1.21.23 support on Windows by updating public/map version and timestamp, with no Windows address changes in this patch. Linux addresses are refreshed at 1769. Source metadata alone does not establish that both platforms were tested simultaneously.

Source: [individual commit](https://github.com/EndstoneMC/endstone/commit/ff15c53555abde8709669079ea87187255db6f79). Classification: compatibility_manifest.

<a id="commit-1769"></a>
### Commit 1769 {#commit-1769}

2024-09-11T17:27:18Z · `730765aaa75f6ce09ea6f04305f387792716235b` · feat: add support for BDS v1.21.23 on Linux

Updates the Linux address map for 1.21.23 but writes 1.21.20 in the shared version field and introduces two address mistakes later corrected. Full per-symbol comparison preserves those exceptions rather than assuming every address moved uniformly. Commits 1770, 1772 and 1773 are causal repairs to this patch.

Source: [individual commit](https://github.com/EndstoneMC/endstone/commit/730765aaa75f6ce09ea6f04305f387792716235b). Classification: compatibility_revision_with_errors.

<a id="commit-1770"></a>
### Commit 1770 {#commit-1770}

2024-09-11T17:31:07Z · `3c21f907aafee7d09fd3d48d44942ed77070bc3e` · fix: rva of ServerPlayer::die

Corrects ServerPlayer::die from the outlying Linux address introduced at 1769 to 97863648. This is a small but operationally meaningful correction because hooking the wrong target can invalidate the whole adapter. No native disassembly or runtime test independently verifies the new address.

Source: [individual commit](https://github.com/EndstoneMC/endstone/commit/3c21f907aafee7d09fd3d48d44942ed77070bc3e). Classification: address_correction.

<a id="commit-1771"></a>
### Commit 1771 {#commit-1771}

2024-09-11T17:32:36Z · `516b70533be4ee32c8d28e6d0aba3173b1eefc2e` · feat: improve error message on hook failure

Adds the specific symbol name to exceptions from both funchook_prepare and funchook_install. It preserves the underlying error category/status while making failures locatable. Its proximity to address repairs is suggestive context, but the commit does not explicitly say which failure prompted it.

Source: [individual commit](https://github.com/EndstoneMC/endstone/commit/516b70533be4ee32c8d28e6d0aba3173b1eefc2e). Classification: diagnostic_improvement.

<a id="commit-1772"></a>
### Commit 1772 {#commit-1772}

2024-09-11T17:34:59Z · `b710680efcd4d483f74bcf6e6337b847ebc3caac` · fix: version string in symbols.toml

Repairs symbols.toml's accidental 1.21.20 version label to 1.21.23. This is an exact metadata fix to 1769, not new compatibility implementation.

Source: [individual commit](https://github.com/EndstoneMC/endstone/commit/b710680efcd4d483f74bcf6e6337b847ebc3caac). Classification: metadata_correction.

<a id="commit-1773"></a>
### Commit 1773 {#commit-1773}

2024-09-11T17:47:47Z · `9133f2ec0cb24910a73a19ba301f41e1d1d52961` · fix: rva of Common::getGameVersionString

Corrects Common::getGameVersionString's Linux address from 65264140 to 65264160. The actual one-symbol change was read and included in the map audit. Treat it as a revision in the compatibility chain, not a general address-generation rule.

Source: [individual commit](https://github.com/EndstoneMC/endstone/commit/9133f2ec0cb24910a73a19ba301f41e1d1d52961). Classification: address_correction.

## Coverage boundary {#coverage-boundary}

Findings rely on the linked public sources; external PR/issue discussions, dependencies, and native engine internals are outside the cited evidence. Runtime and current-release behavior were not tested.
