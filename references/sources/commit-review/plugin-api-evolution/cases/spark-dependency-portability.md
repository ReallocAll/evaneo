<!-- retrieval: {"source_ids":["public:commit:23f9839b16e600c08c409889a9298347d776eb16","public:commit:316b5acf307af522041ff091280398b7970e9ba8","public:commit:4c53cc0e0d0451697769c0ae37a2848adb50fe47","public:commit:8cc11d8a26a7088f3943f260f0266d14d3b00d5e"],"source_type":"public","date":"2026-07-11..2026-07-12","topics":["concurrency","ffi","testing","build","performance","documentation","review","selection"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="spark03-revalidate-workarounds-against-the-exact-dependency-revision"></a>
# Revalidate workarounds against the exact dependency revision {#spark03-revalidate-workarounds-against-the-exact-dependency-revision}

## Explicit author choices {#explicit-author-choices}

The initial spark build separates a static, position-independent profiler core from Endstone's header-only plugin API. It uses hidden visibility and, on Unix, --exclude-libs,ALL to prevent its statically linked cpptrace/zlib/libunwind/libc++ symbols from interposing with differently built copies inside the host. The README explicitly warns that plugin/runtime libc++ must be ABI-compatible and recommends the same major Clang. This is an explicit constraint, not an independently validated ABI guarantee.

`8cc11d8a26a7088f3943f260f0266d14d3b00d5e` changes conanfile.py to declarative conanfile.txt, retaining cpptrace1.0.4, concurrentqueue1.0.4, zlib1.3.1 and expected-lite0.9.0. It preserves the libunwind option and adds the explicit explanation that signal-safe cpptrace capture depends on it. The Python recipe's fPIC option/default is removed; spark_core still sets POSITION_INDEPENDENT_CODE. Do not describe the conversion as entirely byte-equivalent configuration or infer dependency PIC behavior without a resolved graph/build.

## The scheduler workaround is historically grounded but stale {#the-scheduler-workaround-is-historically-grounded-but-stale}

Spark's initial plugin.cpp says Endstone runTaskAsync has a use-after-free because it submits `[&task]{ task->run(); }`, then erases the containing queue. It therefore starts its own export std::thread and hops back with a synchronous scheduled task. The source comment is explicit rationale.

Independent local context establishes a narrower chronology:

- Endstone commit `83f231871ace5764c4bf26b10a29fdff778841a2`, authored July11 18:36UTC and committed18:55UTC, changes exactly `[&task]` to `[task]` in scheduler.cpp with a use-after-free fix message.
- Spark's root is committed July11 23:59UTC. Thus the corrective Endstone commit already existed before spark's initial commit; which dependency snapshot the author actually built is not recorded.
- CMake selects `GIT_TAG v0.11`. In this captured Endstone mirror, `v0.11` is a moving **branch**, not an immutable release tag. It resolves to `b3857a990210972a59c34839c306baae2b41d627`, dated October18, and scheduler.cpp captures by value. This observed source does not contain the claimed reference-capture bug.

The appropriate retained knowledge is: the reference-capture bug existed in the fix's parent, and the plugin records a workaround rationale, but that comment cannot establish a current defect or justify permanently avoiding all async scheduling. Re-check the exact dependency commit, available fixes and unload semantics before carrying a workaround forward. The independently examined dependency patch is context only, not one of this partition's69 reviewed commits or a second review credit for the separate Endstone source review.

## Platform support is incomplete {#platform-support-is-incomplete}

Source claims Linux and Windows capture backends but explicitly marks Windows unexercised. Static inspection finds further limits:

- bytebin.cpp is always compiled yet unconditionally includes unistd and uses mkstemp/write/unlink/popen plus POSIX shell commands and `/tmp`.
- The default-on selftest unconditionally uses SYS_gettid and unistd.
- Windows system_stats supplies stubs for several functions, but lacks a processVirtualBytes definition while common profiler code calls it.
- Windows sleeping-thread/frame filtering is TODO. CPU/system metrics return unavailable/default data.
- Wall-clock milliseconds are stored in long in plugin/profiler code; Windows long is32-bit under the usual ABI, so epoch milliseconds need a width audit.
- CMake visibility flags and dependency backend options require actual Windows-toolchain validation rather than assuming parity from `if(WIN32)` source selection.

These are static portability concerns. No Windows compilation or BDS launch was performed. They prevent presenting the initial profiler as a validated cross-platform implementation.

## Attribution and licensing {#attribution-and-licensing}

`23f9839b16e600c08c409889a9298347d776eb16` reframes the README as a native port of spark rather than spark-style and explicitly credits lucko/spark's profile format, protocol and viewer. It does not add capability. Schema files are source-declared verbatim upstream imports; their fields were examined for serializer context, but byte-identity against an upstream lucko commit was not independently established because no upstream revision is specified.

`316b5acf307af522041ff091280398b7970e9ba8` adds GPLv3, with message “matching spark.” The entire blob exactly matches `/usr/share/common-licenses/GPL-3`; standard text is verified proportionately, not treated as new design reasoning. This documents the source's license choice; it is not a legal opinion about sufficiency of obligations or permission to relicense other code.

## Tests, cost and applicability {#tests-cost-and-applicability}

The independent core and optional offline tool make isolated future testing possible. They are architectural affordances, not actual test results. No compiler, installed package, selftest, curl, BDS or live viewer was used. Other project histories or dependency fixes must retain their own author/source identity.

Use this case for version-pinned workaround audits, ABI-sensitive plugin packaging, mixed-host native dependencies and cross-platform claims. The decision procedure is: identify the exact failing dependency code; locate the fixed commit; resolve branch versus tag; inspect whether old workaround still has a separate purpose; test platform-specific build/runtime paths; only then retain or remove it. The target history supports this need through a concrete stale-comment counterexample, not through a universal preference for custom threads or manual protobuf.

## Public sources {#local-evidence}

- [Spark source index](../repositories/spark-source-index.md) covers the four pinned revisions.
- [Endstone scheduler fix](https://github.com/EndstoneMC/endstone/commit/83f231871ace5764c4bf26b10a29fdff778841a2) and [Spark Conan change](https://github.com/EndstoneMC/spark/commit/8cc11d8a26a7088f3943f260f0266d14d3b00d5e). The branch-resolution observation above is dated; verify the dependency ref again for a current build.
