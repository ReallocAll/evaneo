<!-- retrieval: {"source_ids":["public:commit:0e98a44d96464615d109f7fc6b43f59d48cdba6a","public:commit:14ff0382a4f718d14803c79c380ee1dc6d4c6289","public:commit:1c4e4651682101f94cd27d1f0de76f8d573b2c24","public:commit:1ddf485d5e56a747f0d013fe05e18f1647686537","public:commit:36e7d78fed54dab390b2196cdb8ef39838e6939d","public:commit:44cf49cf7068c80f6d81b18b7828574954e00450","public:commit:7867f3089f5d2f99364ab114734a09deb42b6506","public:commit:844186dde40b9679b1ddd7dd782408b0ccf430f2","public:commit:8be798ad09ad18f4e57c41e8ae6648be54433efb","public:commit:a0ba1989ed37394780df7e59f770093404225776","public:commit:a7d9ff3d188c4a7d19920d76fa9ae3370fc75776","public:commit:d2ea23f6e34eb3ee288467fa36d84298afb124ae","public:commit:e532b44887b1821bab12115044eca82c5cfa18da","public:commit:e94c362f496756e96c1464599d73c88c43c3fa2a","public:commit:f232524fc35b9a1d405f069daec49801c96ed9d8"],"source_type":"public","date":"2026-06-15..2026-07-08","topics":["ffi","testing","build","api","diagnosis","documentation","review","selection","refactoring"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="dwarf2cpp-native-build-migration"></a>
# Dwarf2cpp: native build migration {#dwarf2cpp-native-build-migration}

Each dossier presents its commits in causal DAG order. The numbering is stable;94 precedes93 because93 is its child. Read the cross-cutting [engineering synthesis](../ENGINEERING_SYNTHESIS.md) for revision chains, applicability, counterexamples and validation limits.


<a id="commit-098"></a>
## 098. Add local llvm-core 22.1.7 Conan recipe and switch to it {#commit-098}

- Commit: [f232524fc35b9a1d405f069daec49801c96ed9d8](https://github.com/EndstoneMC/dwarf2cpp/commit/f232524fc35b9a1d405f069daec49801c96ed9d8)
- Date: 2026-06-15T16:57:45Z; parent(s): 53febf325056cee05f2d73ea48e0117fc50700f8
- Exact reading: diff parent1 lines1–930; message parent1 lines1–20
- Attribution: GitHub-linked wu-vincent author, not exclusive authorship of copied dependencies or merged work. Declared trailer: Co-Authored-By: Claude Opus 4.8 (1M context) <noreply@anthropic.com>

Introduces LLVM22.1.7 local Conan recipe adapted from conan-center-index19.1.7, not an original from-scratch LLVM build system; commit explicitly declares Claude Opus4.8 coauthorship. Reads required C++ standard/targets/compiler minima from downloaded source, switches to full monorepo tarball with pinned checksum, re-cuts dependency patch, trims consumer targets/tools/utils/Z3/libedit while keeping compression. Configures project-local Conan home and public Cloudsmith remote, excludes cache/auth state from Git. Full522-line recipe,93-line patch and package tests read: options/validation/dependency components/graphviz analysis/package cleanup/CMake compatibility module, sharedWindows/mac restrictions and no crosscompile. CMake package test checks exported variables and runs LLVM IR interpreter; it does not validate generated C++ headers. It is present but unexecuted. Initial monorepo rename later fails on Windows per103. README claim of otherwise unchanged recipe is broader than actual collapsed version gates; no independent upstream byte audit performed.

The complete message source linked above records any explicit diagnosis. Behavioral explanation is static analysis; no successful execution is inferred.


<a id="commit-099"></a>
## 099. build: switch PEP 517 backend to conan-py-build {#commit-099}

- Commit: [36e7d78fed54dab390b2196cdb8ef39838e6939d](https://github.com/EndstoneMC/dwarf2cpp/commit/36e7d78fed54dab390b2196cdb8ef39838e6939d)
- Date: 2026-06-26T12:04:18Z; parent(s): f232524fc35b9a1d405f069daec49801c96ed9d8
- Exact reading: diff parent1 lines1–180; message parent1 lines1–13
- Attribution: GitHub-linked wu-vincent author, not exclusive authorship of copied dependencies or merged work.

Switches PEP517 backend from scikit-build-core-conan to conan-py-build and moves requires/options to Python Conan recipe with explicit CMake build/install. Explicit Python3 discovery replaces backend injection; CMake tool requirement added, cppstd17 passed, wheel C++/header exclusions and CI recipe hash updated. Message explains backend responsibility change. The removed per-OS compiler-version overrides are not carried forward; agent guide still temporarily states old dependency versions.

The complete message source linked above records any explicit diagnosis. Behavioral explanation is static analysis; no successful execution is inferred.


<a id="commit-100"></a>
## 100. refactor: drop vendored DWARFTypePrinter for LLVM 22's upstream {#commit-100}

- Commit: [e94c362f496756e96c1464599d73c88c43c3fa2a](https://github.com/EndstoneMC/dwarf2cpp/commit/e94c362f496756e96c1464599d73c88c43c3fa2a)
- Date: 2026-06-26T12:34:27Z; parent(s): 36e7d78fed54dab390b2196cdb8ef39838e6939d
- Exact reading: diff parent1 lines1–881; message parent1 lines1–6
- Attribution: GitHub-linked wu-vincent author, not exclusive authorship of copied dependencies or merged work.

Replaces vendored DWARFTypePrinter with LLVM22 header-only DWARFTypePrinter<DWARFDie>, removes source from CMake and includes native header. Explicit reason is upstream availability after buggy LLVM19 workaround. All novel integration read; entire818-line deletion verified byte-identical to fully read added files in62, not discarded as unreviewed bulk. No independent LLVM22 implementation comparison or generated-output equivalence run; retirement rationale is author report supported by integration change.

The complete message source linked above records any explicit diagnosis. Behavioral explanation is static analysis; no successful execution is inferred.


<a id="commit-101"></a>
## 101. feat: migrate bindings from pybind11 to nanobind (stable ABI) {#commit-101}

- Commit: [e532b44887b1821bab12115044eca82c5cfa18da](https://github.com/EndstoneMC/dwarf2cpp/commit/e532b44887b1821bab12115044eca82c5cfa18da)
- Date: 2026-06-26T12:36:30Z; parent(s): e94c362f496756e96c1464599d73c88c43c3fa2a
- Exact reading: diff parent1 lines1–490; message parent1 lines1–13
- Attribution: GitHub-linked wu-vincent author, not exclusive authorship of copied dependencies or merged work.

Migrates exported classes/enums/optional conversions/errors from pybind11 to nanobind, builds STABLE_ABI NB_STATIC, requires Python>=3.12 and tags one cp312-abi3 wheel per platform through backend environment. Explicit tradeoff: drop3.10/3.11 to reduce per-version wheel builds. Integer form conversion now explicitly constructs nb::int_; native enum binding semantics change and were not runtime-tested. Conan CMake tool requirement>=3.27 and later build isolation reflect SABIModule need, but CMakeLists declares3.6 and guide says3.26+, an observed version-contract inconsistency. No actual ABI/wheel/import validation.

The complete message source linked above records any explicit diagnosis. Behavioral explanation is static analysis; no successful execution is inferred.


<a id="commit-102"></a>
## 102. fix: build _dwarf bindings against LLVM 22 {#commit-102}

- Commit: [844186dde40b9679b1ddd7dd782408b0ccf430f2](https://github.com/EndstoneMC/dwarf2cpp/commit/844186dde40b9679b1ddd7dd782408b0ccf430f2)
- Date: 2026-06-26T13:56:12Z; parent(s): e532b44887b1821bab12115044eca82c5cfa18da
- Exact reading: diff parent1 lines1–115; message parent1 lines1–7
- Attribution: GitHub-linked wu-vincent author, not exclusive authorship of copied dependencies or merged work.

Deletes LLVM20 recursive-lookup polyfill and its support includes, routes properties through upstream DWARFDie.findRecursively, adapts remaining getTypeUnitForHash call to LLVM22 hash/isDWO signature. Completes part of dependency migration rather than assuming compilation after100. Message says both call sites; deleted helper contained one and surviving binding contains the other.

The complete message source linked above records any explicit diagnosis. Behavioral explanation is static analysis; no successful execution is inferred.


<a id="commit-103"></a>
## 103. fix(llvm-core): build the monorepo llvm/ dir directly, no rename {#commit-103}

- Commit: [7867f3089f5d2f99364ab114734a09deb42b6506](https://github.com/EndstoneMC/dwarf2cpp/commit/7867f3089f5d2f99364ab114734a09deb42b6506)
- Date: 2026-06-26T13:56:22Z; parent(s): 844186dde40b9679b1ddd7dd782408b0ccf430f2
- Exact reading: diff parent1 lines1–64; message parent1 lines1–7
- Attribution: GitHub-linked wu-vincent author, not exclusive authorship of copied dependencies or merged work.

Removes llvm/→llvm-main monorepo rename and updates configure/source/patch base paths together. Explicit reported failure is Windows antivirus retaining extracted-file handles while Conan robocopy /move deletes per-file. Avoids unnecessary filesystem movement rather than adding retries or disabling antivirus. No live Windows reproduction.

The complete message source linked above records any explicit diagnosis. Behavioral explanation is static analysis; no successful execution is inferred.


<a id="commit-104"></a>
## 104. build: provide cmake/ninja and use the Ninja generator {#commit-104}

- Commit: [1ddf485d5e56a747f0d013fe05e18f1647686537](https://github.com/EndstoneMC/dwarf2cpp/commit/1ddf485d5e56a747f0d013fe05e18f1647686537)
- Date: 2026-06-26T13:56:32Z; parent(s): 7867f3089f5d2f99364ab114734a09deb42b6506
- Exact reading: diff parent1 lines1–37; message parent1 lines1–7
- Attribution: GitHub-linked wu-vincent author, not exclusive authorship of copied dependencies or merged work.

Adds CMake>=3.27 and Ninja to PEP517 build isolation and chooses Ninja through Conan extra arguments. Explicit reason: dependency source recipes need executables on PATH even after consumer CMake tool_require; parallel LLVM build desired. No speed measurement.108 reverses consumer Ninja selection after execution failure; maintain this causal failure chain.

The complete message source linked above records any explicit diagnosis. Behavioral explanation is static analysis; no successful execution is inferred.


<a id="commit-105"></a>
## 105. chore(deps): drop redundant direct libxml2 requirement {#commit-105}

- Commit: [a0ba1989ed37394780df7e59f770093404225776](https://github.com/EndstoneMC/dwarf2cpp/commit/a0ba1989ed37394780df7e59f770093404225776)
- Date: 2026-06-26T14:14:23Z; parent(s): 1ddf485d5e56a747f0d013fe05e18f1647686537
- Exact reading: diff parent1 lines1–16; message parent1 lines1–4
- Attribution: GitHub-linked wu-vincent author, not exclusive authorship of copied dependencies or merged work.

Drops direct libxml2 requirement as reportedly redundant with LLVM selected2.13.8. Actual direct range>=2.13,<2.14 disappears, while tracked LLVM recipe allows>=2.12.5,<3 with_xml2 default true. Thus snapshot dependency duplication may be redundant, but removal also widens allowable future resolution; no Conan lock graph confirms resolved version here.

The complete message source linked above records any explicit diagnosis. Behavioral explanation is static analysis; no successful execution is inferred.


<a id="commit-106"></a>
## 106. build: generate _dwarf.pyi via nanobind stubgen {#commit-106}

- Commit: [14ff0382a4f718d14803c79c380ee1dc6d4c6289](https://github.com/EndstoneMC/dwarf2cpp/commit/14ff0382a4f718d14803c79c380ee1dc6d4c6289)
- Date: 2026-06-26T14:50:25Z; parent(s): a0ba1989ed37394780df7e59f770093404225776
- Exact reading: diff parent1 lines1–149; message parent1 lines1–6
- Attribution: GitHub-linked wu-vincent author, not exclusive authorship of copied dependencies or merged work.

Generates _dwarf.pyi and py.typed by importing compiled module through nanobind_add_stub and installs them alongside extension. Deletes fully read122-line handwritten stub including duplicated enum value, leaving binding exports authoritative. Benefit is drift reduction; cost is build-time runtime import requirement, which exposes musl linkage failure in110. No generated stub file checked because none is committed and no build executed.

The complete message source linked above records any explicit diagnosis. Behavioral explanation is static analysis; no successful execution is inferred.


<a id="commit-107"></a>
## 107. refactor(_dwarf): document bindings, drop as_referenced_die polyfill {#commit-107}

- Commit: [8be798ad09ad18f4e57c41e8ae6648be54433efb](https://github.com/EndstoneMC/dwarf2cpp/commit/8be798ad09ad18f4e57c41e8ae6648be54433efb)
- Date: 2026-06-26T14:50:43Z; parent(s): 14ff0382a4f718d14803c79c380ee1dc6d4c6289
- Exact reading: diff parent1 lines1–168; message parent1 lines1–7
- Attribution: GitHub-linked wu-vincent author, not exclusive authorship of copied dependencies or merged work.

Adds selective docstrings attributed explicitly to documented LLVM headers, clarifying direct find versus recursively inherited properties; replaces remaining manual form-reference resolution with upstream getAttributeValueAsReferencedDie invoked from form unit DIE. Comment explains form unit determines result. Message claims equivalence was verified; this review independently reads old/new bodies but does not repeat upstream equivalence testing or claim all malformed/null unit behavior is equivalent.

The complete message source linked above records any explicit diagnosis. Behavioral explanation is static analysis; no successful execution is inferred.


<a id="commit-108"></a>
## 108. build: drop the Ninja generator {#commit-108}

- Commit: [1c4e4651682101f94cd27d1f0de76f8d573b2c24](https://github.com/EndstoneMC/dwarf2cpp/commit/1c4e4651682101f94cd27d1f0de76f8d573b2c24)
- Date: 2026-06-26T16:04:06Z; parent(s): 8be798ad09ad18f4e57c41e8ae6648be54433efb
- Exact reading: diff parent1 lines1–25; message parent1 lines1–3
- Attribution: GitHub-linked wu-vincent author, not exclusive authorship of copied dependencies or merged work.

Removes Ninja from PEP517 requirements and consumer generator arguments after reported conancenter Ninja binary no-such-file failure in manylinux. Message promises fallback default generators. Crucial final-source limit: tracked LLVM recipe still tool_requires Ninja and explicitly constructs CMakeToolchain(generator="Ninja"); no patch here changes it. Therefore only consumer configuration removal is verified; universal Ninja elimination is not.

The complete message source linked above records any explicit diagnosis. Behavioral explanation is static analysis; no successful execution is inferred.


<a id="commit-109"></a>
## 109. ci: consolidate release into build.yml, fix Conan cache {#commit-109}

- Commit: [44cf49cf7068c80f6d81b18b7828574954e00450](https://github.com/EndstoneMC/dwarf2cpp/commit/44cf49cf7068c80f6d81b18b7828574954e00450)
- Date: 2026-06-26T16:04:06Z; parent(s): 1c4e4651682101f94cd27d1f0de76f8d573b2c24
- Exact reading: diff parent1 lines1–534; message parent1 lines1–5
- Attribution: GitHub-linked wu-vincent author, not exclusive authorship of copied dependencies or merged work.

Consolidates distribution publication into build.yml: main/PR wheels, v* tag sdist, repository-guarded publish requiring both, OIDC, GitHub release notes. Tag builds not cancelled; branch builds superseded. Fixes actual Conan-localhome cache/mount path .conan2/p and /project/.conan2, retains Linux ownership repair. New196-line release-agent document specifies local version/changelog approval/tag push/monitor/verify and failure recovery; read as source data, never executed. Static limits: README still points to deleted manual Release workflow; tag/version equality is documented but not machine-enforced; PyPI upload precedes changelog validation so failure can leave partial publication; suggested rerun after follow-up changelog commit does not itself change checkout at original tag. Commit message mentions dropping compiler pin step, but diff contains no such step deletion.

The complete message source linked above records any explicit diagnosis. Behavioral explanation is static analysis; no successful execution is inferred.


<a id="commit-110"></a>
## 110. build: build LLVM without backtraces to support musllinux {#commit-110}

- Commit: [0e98a44d96464615d109f7fc6b43f59d48cdba6a](https://github.com/EndstoneMC/dwarf2cpp/commit/0e98a44d96464615d109f7fc6b43f59d48cdba6a)
- Date: 2026-06-26T17:48:41Z; parent(s): 44cf49cf7068c80f6d81b18b7828574954e00450
- Exact reading: diff parent1 lines1–46; message parent1 lines1–3
- Attribution: GitHub-linked wu-vincent author, not exclusive authorship of copied dependencies or merged work.

Adds LLVM backtraces/crash_overrides recipe options default on, consumer off, disables LLVM bindings/libpfm. Explicit reported reason is musl import relocation failure during generated-stub step caused by glibc backtrace; message also reports remote recipe revision uploaded, which was not independently checked and no upload was performed here. Adds controls instead of assuming Python abi3 solves native libc compatibility.111 narrows promised platform support.

The complete message source linked above records any explicit diagnosis. Behavioral explanation is static analysis; no successful execution is inferred.


<a id="commit-111"></a>
## 111. ci: skip musllinux wheels {#commit-111}

- Commit: [d2ea23f6e34eb3ee288467fa36d84298afb124ae](https://github.com/EndstoneMC/dwarf2cpp/commit/d2ea23f6e34eb3ee288467fa36d84298afb124ae)
- Date: 2026-06-26T21:42:16Z; parent(s): 0e98a44d96464615d109f7fc6b43f59d48cdba6a
- Exact reading: diff parent1 lines1–13; message parent1 lines1–3
- Attribution: GitHub-linked wu-vincent author, not exclusive authorship of copied dependencies or merged work.

Adds *-musllinux* skip selector. Explicit diagnosis: shared cache reuses glibc LLVM for musl and backtrace/mallinfo incompatibilities remain; claimed Linux delivery becomes manylinux plus source distribution. This is a support withdrawal following110, not a successful musl fix or proof source builds work on musl. Other32-bit exclusions remain.

The complete message source linked above records any explicit diagnosis. Behavioral explanation is static analysis; no successful execution is inferred.


<a id="commit-112"></a>
## 112. fix(visitor): fold, don't drop, definitions past the per-line cap {#commit-112}

- Commit: [a7d9ff3d188c4a7d19920d76fa9ae3370fc75776](https://github.com/EndstoneMC/dwarf2cpp/commit/a7d9ff3d188c4a7d19920d76fa9ae3370fc75776)
- Date: 2026-07-08T19:36:37Z; parent(s): d2ea23f6e34eb3ee288467fa36d84298afb124ae
- Exact reading: diff parent1 lines1–47; message parent1 lines1–15
- Attribution: GitHub-linked wu-vincent author, not exclusive authorship of copied dependencies or merged work.

Preserves the normal append-first-eight then parameter-name synchronization then final-merge sequence; on overflow tries semantic merge against each existing entry and returns on success. Explicit motivating report is ~160-CU repeated BlockType where only one carries full nested NameInfo. Adds None-safe TypeDef.merge path because new merges expose it. No regression fixture or reproduction executed. Residuals: unmatched overflow silently drops; separate _handle_struct member bucket skips when len>4 before visiting; Function.merge still ORs qualifiers and adjacent final fold remains order-sensitive. Fix is targeted richer-information preservation under existing cap, not lossless global deduplication.

The complete message source linked above records any explicit diagnosis. Behavioral explanation is static analysis; no successful execution is inferred.
