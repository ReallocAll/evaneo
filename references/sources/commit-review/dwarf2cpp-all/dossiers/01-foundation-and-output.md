<!-- retrieval: {"source_ids":["public:commit:08c91aec73271a231215d8bd02980c09ec04d092","public:commit:0a03b11c0689264a900f9d61df93bc14e9bc6036","public:commit:0b3a4d03944497259c7dc5db2cab339c539ea648","public:commit:0cec4722b2392d804cba8e6ef074232221501cd6","public:commit:0ecfe36824122da012536674deae859be3f49131","public:commit:191330fa73e821114069fe10fc467f0eef23a089","public:commit:1ffe7b3bc7435db2c95e61dcf77f366e0303676d","public:commit:3084ec16a0d1cc8c5e134b393b0834a0d7b7840f","public:commit:3337ca803e28397814486cc7ab4d7e414f233958","public:commit:34a037720593ed0f8aec89af2607feac45ec2524","public:commit:34c50e6ffb375cbda3c2e099681fcf8acc2ffad7","public:commit:384a548abec742b5eda689f70adaf688f087fa34","public:commit:3956d876c988b045b6608de64ad8f3bd8f6d56ab","public:commit:421f8d1409831cb0430055a68d11e3e707856587","public:commit:42fbbfad6a616d458d861240f848a6dd37ce8c97","public:commit:5521ccb5a3251b52160903fba03112aa31847229","public:commit:628052f26527736f398a28c27864110a93749237","public:commit:7aad748d22ac0b26f29d84db0f6b1f6bf9af9567","public:commit:7e397ee8e505377e27d6633a3335ca5dbe6e34f4","public:commit:976aa1d858d8963dc7e00163653685d1a918f51e","public:commit:9d0e95ebc4b789f45c00bface6c6ece69dcdeb04","public:commit:a1fe919ee48faf142cdc1d12f03248eea68292e4","public:commit:a7c7b22da714d3b6cd00e0a0c588f6321f883a4a","public:commit:b866f66bf528003edb44cf838d3a50ef353bbc2e","public:commit:db0165a5b2047092bebe562126a05dfc135fbbe2","public:commit:dcece752fd7eddf159333dc69fbbe10d579ad569","public:commit:f3b288145b81e14113aed2470c41ebee95ef6f84","public:commit:fae8447a913a2d0e795da8a720874770ada5e7ab"],"source_type":"public","date":"2025-09-13..2025-09-14","topics":["ffi","testing","build","api","diagnosis","documentation","review","refactoring"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="dwarf2cpp-foundation-and-output"></a>
# Dwarf2cpp: foundation and output {#dwarf2cpp-foundation-and-output}

Each dossier presents its commits in causal DAG order. The numbering is stable;94 precedes93 because93 is its child. Read the cross-cutting [engineering synthesis](../ENGINEERING_SYNTHESIS.md) for revision chains, applicability, counterexamples and validation limits.


<a id="commit-001"></a>
## 001. feat: initial commit {#commit-001}

- Commit: [5521ccb5a3251b52160903fba03112aa31847229](https://github.com/EndstoneMC/dwarf2cpp/commit/5521ccb5a3251b52160903fba03112aa31847229)
- Date: 2025-09-13T00:01:15Z; parent(s): root
- Exact reading: diff parent1 lines1–1663; message parent1 lines1–1
- Attribution: GitHub-linked wu-vincent author, not exclusive authorship of copied dependencies or merged work.

Introduces a three-layer reconstruction pipeline: LLVM object/DWARF ownership and type printing exposed through pybind11; Python Visitor builds dataclass objects keyed by DIE offsets, resolves declarations and definitions and groups by original file/line; Jinja templates render scopes and declarations. LLVM remains parser/type-printer authority rather than reimplementing DWARF binary decoding. ObjectFile load errors become runtime_error; invalid string/constant forms become ValueError; many unknown tags/attributes fail fast. This trades coverage for visible unsupported inputs. File filtering uses compilation-directory prefix and relative-path exclusion; line cap retains at most five entries before semantic deduplication, a later correctness fault. DW_AT_specification links definitions to declarations; a global linkage-or-short-name plus arity map fills missing parameter names. Anonymous types can be nested inside typedefs. Type cleanup is textual, recursive fixed-point rewriting of standard-library defaults and project-specific spellings, not an AST equivalence proof. Root README lists concrete missing const/template/access/declarator support. pyproject declares Python >=3.10 while models use enum.StrEnum (a compatibility risk until requirements change). No test files. Copyright reads 2024 endstone-insider; commit attribution alone does not establish original authorship of LLVM mechanisms or all initial implementation.


<a id="commit-002"></a>
## 002. ci: add GitHub Actions workflow for building wheels {#commit-002}

- Commit: [976aa1d858d8963dc7e00163653685d1a918f51e](https://github.com/EndstoneMC/dwarf2cpp/commit/976aa1d858d8963dc7e00163653685d1a918f51e)
- Date: 2025-09-13T00:08:08Z; parent(s): 5521ccb5a3251b52160903fba03112aa31847229
- Exact reading: diff parent1 lines1–32; message parent1 lines1–1
- Attribution: GitHub-linked wu-vincent author, not exclusive authorship of copied dependencies or merged work.

Adds push/PR wheel builds over six runner/architecture variants with fail-fast disabled and uploaded wheel artifacts. A placeholder CIBW_SOME_OPTION remains; this is initial CI plumbing, not evidence of successful builds or runtime validation.


<a id="commit-003"></a>
## 003. refactor: remove unused <format> header {#commit-003}

- Commit: [0ecfe36824122da012536674deae859be3f49131](https://github.com/EndstoneMC/dwarf2cpp/commit/0ecfe36824122da012536674deae859be3f49131)
- Date: 2025-09-13T02:05:57Z; parent(s): 976aa1d858d8963dc7e00163653685d1a918f51e
- Exact reading: diff parent1 lines1–10; message parent1 lines1–1
- Attribution: GitHub-linked wu-vincent author, not exclusive authorship of copied dependencies or merged work.

Deletes unused <format> include and leading blank line from bindings. Complete patch is a mechanical cleanup; plausible wider compiler compatibility is inference, not stated rationale.


<a id="commit-004"></a>
## 004. chore: freeze libxml2 version {#commit-004}

- Commit: [3337ca803e28397814486cc7ab4d7e414f233958](https://github.com/EndstoneMC/dwarf2cpp/commit/3337ca803e28397814486cc7ab4d7e414f233958)
- Date: 2025-09-13T02:06:09Z; parent(s): 0ecfe36824122da012536674deae859be3f49131
- Exact reading: diff parent1 lines1–17; message parent1 lines1–1
- Attribution: GitHub-linked wu-vincent author, not exclusive authorship of copied dependencies or merged work.

Pins libxml2 to >=2.13,<2.14 alongside LLVM 19.1.7 and pybind11 3.0.1; title explicitly says freeze version. No failing version/reproduction appears, so do not invent an incompatibility or claim pin fixed CI.


<a id="commit-005"></a>
## 005. chore: update build workflow {#commit-005}

- Commit: [34c50e6ffb375cbda3c2e099681fcf8acc2ffad7](https://github.com/EndstoneMC/dwarf2cpp/commit/34c50e6ffb375cbda3c2e099681fcf8acc2ffad7)
- Date: 2025-09-13T02:06:36Z; parent(s): 3337ca803e28397814486cc7ab4d7e414f233958
- Exact reading: diff parent1 lines1–43; message parent1 lines1–1
- Attribution: GitHub-linked wu-vincent author, not exclusive authorship of copied dependencies or merged work.

Reduces wheel matrix from six runner variants to Ubuntu latest, Windows latest and macOS 14, removes placeholder option, and sets Conan C++17/compiler-version overrides per platform (MSVC 193, GCC 11, Apple Clang 13). A packaging target narrowing, not proof those platforms work.


<a id="commit-006"></a>
## 006. ci: skip 32-bit builds {#commit-006}

- Commit: [3956d876c988b045b6608de64ad8f3bd8f6d56ab](https://github.com/EndstoneMC/dwarf2cpp/commit/3956d876c988b045b6608de64ad8f3bd8f6d56ab)
- Date: 2025-09-13T02:12:00Z; parent(s): 34c50e6ffb375cbda3c2e099681fcf8acc2ffad7
- Exact reading: diff parent1 lines1–13; message parent1 lines1–1
- Attribution: GitHub-linked wu-vincent author, not exclusive authorship of copied dependencies or merged work.

CIBW_SKIP excludes win32 and manylinux_i686. Explicitly avoids these 32-bit wheels; does not universally exclude every possible 32-bit Linux tag.


<a id="commit-007"></a>
## 007. refactor: improve qualified type {#commit-007}

- Commit: [f3b288145b81e14113aed2470c41ebee95ef6f84](https://github.com/EndstoneMC/dwarf2cpp/commit/f3b288145b81e14113aed2470c41ebee95ef6f84)
- Date: 2025-09-13T11:43:20Z; parent(s): 3956d876c988b045b6608de64ad8f3bd8f6d56ab
- Exact reading: diff parent1 lines1–58; message parent1 lines1–1
- Attribution: GitHub-linked wu-vincent author, not exclusive authorship of copied dependencies or merged work.

For scoped tags (class/struct/union/namespace/enum/typedef), prepends parent scopes then prints an unqualified name rather than using appendQualifiedName blindly. Other changes are indentation. Type qualification becomes an explicit policy around LLVM printer behavior, later replaced by split declarators and typedef-aware vendoring.


<a id="commit-008"></a>
## 008. feat: add support for inline function attribute {#commit-008}

- Commit: [a1fe919ee48faf142cdc1d12f03248eea68292e4](https://github.com/EndstoneMC/dwarf2cpp/commit/a1fe919ee48faf142cdc1d12f03248eea68292e4)
- Date: 2025-09-13T11:53:51Z; parent(s): f3b288145b81e14113aed2470c41ebee95ef6f84
- Exact reading: diff parent1 lines1–131; message parent1 lines1–1
- Attribution: GitHub-linked wu-vincent author, not exclusive authorship of copied dependencies or merged work.

Binds InlineAttribute, adds Function.is_inline and renders inline. Only DECLARED_NOT_INLINED/DECLARED_INLINED set source-level inline, preserving difference between declared inline and optimizer inlining. Remaining hunks are formatting; no tests added.


<a id="commit-009"></a>
## 009. refactor: improve function parameter name sync for constructors {#commit-009}

- Commit: [fae8447a913a2d0e795da8a720874770ada5e7ab](https://github.com/EndstoneMC/dwarf2cpp/commit/fae8447a913a2d0e795da8a720874770ada5e7ab)
- Date: 2025-09-13T12:53:12Z; parent(s): a1fe919ee48faf142cdc1d12f03248eea68292e4
- Exact reading: diff parent1 lines1–29; message parent1 lines1–1
- Attribution: GitHub-linked wu-vincent author, not exclusive authorship of copied dependencies or merged work.

Restricts parameter-name synchronization keys to linkage names or external C short names plus arity. Constructor definitions may point through DW_AT_specification to declarations lacking a linkage name; explicitly registers that declaration under known definition identity. Reduces accidental matching of unrelated local names, but key+arity still depends on adequate DWARF linkage identity.


<a id="commit-010"></a>
## 010. docs: update README.md {#commit-010}

- Commit: [7aad748d22ac0b26f29d84db0f6b1f6bf9af9567](https://github.com/EndstoneMC/dwarf2cpp/commit/7aad748d22ac0b26f29d84db0f6b1f6bf9af9567)
- Date: 2025-09-13T13:24:50Z; parent(s): fae8447a913a2d0e795da8a720874770ada5e7ab
- Exact reading: diff parent1 lines1–167; message parent1 lines1–1
- Attribution: GitHub-linked wu-vincent author, not exclusive authorship of copied dependencies or merged work.

Expands README from usage/missing-feature checklist to prerequisites, prebuilt wheel path, purpose, reconstruction limitations and legal caution. Explicitly says usable DWARF-enabled input is required, generated headers may need manual fixes, and templates/inline functions/macros may not be faithfully reconstructed. Documentation's tested-mainly claim is reported, not independently reproduced; clone and badge still contain placeholders and Python text is inconsistent.


<a id="commit-011"></a>
## 011. docs: update README.md {#commit-011}

- Commit: [3084ec16a0d1cc8c5e134b393b0834a0d7b7840f](https://github.com/EndstoneMC/dwarf2cpp/commit/3084ec16a0d1cc8c5e134b393b0834a0d7b7840f)
- Date: 2025-09-13T13:29:09Z; parent(s): 7aad748d22ac0b26f29d84db0f6b1f6bf9af9567
- Exact reading: diff parent1 lines1–70; message parent1 lines1–1
- Attribution: GitHub-linked wu-vincent author, not exclusive authorship of copied dependencies or merged work.

Condenses build prerequisites, clarifies supporting framework development, repairs LICENSE link and shortens contribution wording. Removes inconsistent Python 3.9 section. Documentation editorial revision with no code behavior change.


<a id="commit-012"></a>
## 012. docs: update README.md {#commit-012}

- Commit: [384a548abec742b5eda689f70adaf688f087fa34](https://github.com/EndstoneMC/dwarf2cpp/commit/384a548abec742b5eda689f70adaf688f087fa34)
- Date: 2025-09-13T13:29:39Z; parent(s): 3084ec16a0d1cc8c5e134b393b0834a0d7b7840f
- Exact reading: diff parent1 lines1–13; message parent1 lines1–1
- Attribution: GitHub-linked wu-vincent author, not exclusive authorship of copied dependencies or merged work.

Replaces placeholder clone URL with then-current endstone-insider repository URL. Narrow reproducibility/documentation correction.


<a id="commit-013"></a>
## 013. docs: remove outdated README.md from dwarf2cpp directory {#commit-013}

- Commit: [0cec4722b2392d804cba8e6ef074232221501cd6](https://github.com/EndstoneMC/dwarf2cpp/commit/0cec4722b2392d804cba8e6ef074232221501cd6)
- Date: 2025-09-13T13:32:05Z; parent(s): 384a548abec742b5eda689f70adaf688f087fa34
- Exact reading: diff parent1 lines1–34; message parent1 lines1–1
- Attribution: GitHub-linked wu-vincent author, not exclusive authorship of copied dependencies or merged work.

Deletes the duplicate src README containing legacy invocation and known-issue checklist. Full deletion read; this does not prove listed issues were fixed.


<a id="commit-014"></a>
## 014. fix: correct broken build status badge link {#commit-014}

- Commit: [db0165a5b2047092bebe562126a05dfc135fbbe2](https://github.com/EndstoneMC/dwarf2cpp/commit/db0165a5b2047092bebe562126a05dfc135fbbe2)
- Date: 2025-09-13T13:34:43Z; parent(s): 0cec4722b2392d804cba8e6ef074232221501cd6
- Exact reading: diff parent1 lines1–12; message parent1 lines1–1
- Attribution: GitHub-linked wu-vincent author, not exclusive authorship of copied dependencies or merged work.

Repairs build badge destination from yourusername to endstone-insider. No independent engineering lesson beyond verifying copied links.


<a id="commit-015"></a>
## 015. feat: add support for static member functions detection {#commit-015}

- Commit: [191330fa73e821114069fe10fc467f0eef23a089](https://github.com/EndstoneMC/dwarf2cpp/commit/191330fa73e821114069fe10fc467f0eef23a089)
- Date: 2025-09-13T17:16:37Z; parent(s): db0165a5b2047092bebe562126a05dfc135fbbe2
- Exact reading: diff parent1 lines1–47; message parent1 lines1–1
- Attribution: GitHub-linked wu-vincent author, not exclusive authorship of copied dependencies or merged work.

Adds static-member model/rendering flag, initially inferred on an out-of-line definition solely by absence of DW_AT_object_pointer; mutates referenced declaration. This initial heuristic has no parent-kind guard, so it is broader than member functions and is corrected later. No tests.


<a id="commit-016"></a>
## 016. feat: add tqdm for progress bar {#commit-016}

- Commit: [42fbbfad6a616d458d861240f848a6dd37ce8c97](https://github.com/EndstoneMC/dwarf2cpp/commit/42fbbfad6a616d458d861240f848a6dd37ce8c97)
- Date: 2025-09-13T18:13:53Z; parent(s): 191330fa73e821114069fe10fc467f0eef23a089
- Exact reading: diff parent1 lines1–81; message parent1 lines1–1
- Attribution: GitHub-linked wu-vincent author, not exclusive authorship of copied dependencies or merged work.

Adds tqdm dependency and progress for compile-unit visitation and generated files, ending with absolute output directory. Replaces per-unit/per-file info logging with progress descriptions. Shows long-running extraction observability; does not benchmark speed.


<a id="commit-017"></a>
## 017. feat: add support for const member functions {#commit-017}

- Commit: [dcece752fd7eddf159333dc69fbbe10d579ad569](https://github.com/EndstoneMC/dwarf2cpp/commit/dcece752fd7eddf159333dc69fbbe10d579ad569)
- Date: 2025-09-13T18:28:43Z; parent(s): 42fbbfad6a616d458d861240f848a6dd37ce8c97
- Exact reading: diff parent1 lines1–60; message parent1 lines1–3
- Attribution: GitHub-linked wu-vincent author, not exclusive authorship of copied dependencies or merged work.

Extends member qualification by walking DW_AT_object_pointer's type chain until a const DIE, setting declaration.is_const and copying it to out-of-line function. Renders trailing const; message explicitly fixes issue #1. Initial algorithm considers any const in chain and is later tightened to pointee constness, so do not recommend it as final rule.

The complete message source linked above records any explicit diagnosis. Behavioral explanation is static analysis; no successful execution is inferred.


<a id="commit-018"></a>
## 018. refactor: replace type_cleanup filter with cleanup function {#commit-018}

- Commit: [0b3a4d03944497259c7dc5db2cab339c539ea648](https://github.com/EndstoneMC/dwarf2cpp/commit/0b3a4d03944497259c7dc5db2cab339c539ea648)
- Date: 2025-09-13T18:47:01Z; parent(s): dcece752fd7eddf159333dc69fbbe10d579ad569
- Exact reading: diff parent1 lines1–252; message parent1 lines1–1
- Attribution: GitHub-linked wu-vincent author, not exclusive authorship of copied dependencies or merged work.

Moves cleanup from individual Jinja type filters to a post-render whole-file pass. Most replacement patterns move intact, but std::map/unordered_map allocator matching now accepts both const Key and Key const. Whole-output normalization covers previously unfiltered positions at cost of textual transformation outside isolated type strings; it is not merely file relocation or a general C++ parser.


<a id="commit-019"></a>
## 019. feat: add insert_name filter for improved type formatting {#commit-019}

- Commit: [34a037720593ed0f8aec89af2607feac45ec2524](https://github.com/EndstoneMC/dwarf2cpp/commit/34a037720593ed0f8aec89af2607feac45ec2524)
- Date: 2025-09-13T19:31:47Z; parent(s): 0b3a4d03944497259c7dc5db2cab339c539ea648
- Exact reading: diff parent1 lines1–97; message parent1 lines1–1
- Attribution: GitHub-linked wu-vincent author, not exclusive authorship of copied dependencies or merged work.

Introduces cached insert_name filter for attributes/parameters, with regex cases for arrays and C-style function pointers; member-function-pointer case is commented out. This fixes the simplistic first-[ split but remains a grammar heuristic. Later split-type API supersedes it; no independent parser-completeness evidence.


<a id="commit-020"></a>
## 020. fix: update parsing for member function pointers {#commit-020}

- Commit: [b866f66bf528003edb44cf838d3a50ef353bbc2e](https://github.com/EndstoneMC/dwarf2cpp/commit/b866f66bf528003edb44cf838d3a50ef353bbc2e)
- Date: 2025-09-13T19:50:23Z; parent(s): 34a037720593ed0f8aec89af2607feac45ec2524
- Exact reading: diff parent1 lines1–43; message parent1 lines1–3
- Attribution: GitHub-linked wu-vincent author, not exclusive authorship of copied dependencies or merged work.

Enables member-function-pointer pattern including const/volatile and &/&& suffixes, inserts identifier after Class::*, and links issue #4. Argument pattern excludes nested closing parentheses, illustrating why regex recognition cannot robustly handle recursive C++ declarators. Includes temporary print(t), removed next commit.

The complete message source linked above records any explicit diagnosis. Behavioral explanation is static analysis; no successful execution is inferred.


<a id="commit-021"></a>
## 021. fix(visitor): handle missing import cases in DWARF visitor {#commit-021}

- Commit: [a7c7b22da714d3b6cd00e0a0c588f6321f883a4a](https://github.com/EndstoneMC/dwarf2cpp/commit/a7c7b22da714d3b6cd00e0a0c588f6321f883a4a)
- Date: 2025-09-13T20:01:25Z; parent(s): b866f66bf528003edb44cf838d3a50ef353bbc2e
- Exact reading: diff parent1 lines1–34; message parent1 lines1–3
- Attribution: GitHub-linked wu-vincent author, not exclusive authorship of copied dependencies or merged work.

Removes debug print and returns early for an imported DIE that visitation did not register, then asserts valid import. Fixes #5, preventing blank/unresolved using declarations rather than fabricating a name or crashing on absent cache entry.

The complete message source linked above records any explicit diagnosis. Behavioral explanation is static analysis; no successful execution is inferred.


<a id="commit-022"></a>
## 022. feat: handle access attribute {#commit-022}

- Commit: [9d0e95ebc4b789f45c00bface6c6ece69dcdeb04](https://github.com/EndstoneMC/dwarf2cpp/commit/9d0e95ebc4b789f45c00bface6c6ece69dcdeb04)
- Date: 2025-09-13T20:31:11Z; parent(s): a7c7b22da714d3b6cd00e0a0c588f6321f883a4a
- Exact reading: diff parent1 lines1–89; message parent1 lines1–3
- Attribution: GitHub-linked wu-vincent author, not exclusive authorship of copied dependencies or merged work.

Adds shared Object.access, parses DW_AT_accessibility for functions/attributes/structures, emits access labels when first member at a source line changes access. Completes #3 per message. Source-line grouping assumes compatible member access within a line; initial absent-access handling still needs class/struct defaults (commit 32).

The complete message source linked above records any explicit diagnosis. Behavioral explanation is static analysis; no successful execution is inferred.


<a id="commit-023"></a>
## 023. docs: update README.md {#commit-023}

- Commit: [0a03b11c0689264a900f9d61df93bc14e9bc6036](https://github.com/EndstoneMC/dwarf2cpp/commit/0a03b11c0689264a900f9d61df93bc14e9bc6036)
- Date: 2025-09-13T20:37:57Z; parent(s): 9d0e95ebc4b789f45c00bface6c6ece69dcdeb04
- Exact reading: diff parent1 lines1–65; message parent1 lines1–1
- Attribution: GitHub-linked wu-vincent author, not exclusive authorship of copied dependencies or merged work.

Repositions README as general DWARF reconstruction rather than exclusively Minecraft, keeps input prerequisites and concrete examples, and explicitly replaces tested-mainly wording with only trivially tested and may not work on arbitrary DWARF input. This narrows validation claims materially; no successful test run can be inferred.


<a id="commit-024"></a>
## 024. fix: support inline struct declaration for variables {#commit-024}

- Commit: [08c91aec73271a231215d8bd02980c09ec04d092](https://github.com/EndstoneMC/dwarf2cpp/commit/08c91aec73271a231215d8bd02980c09ec04d092)
- Date: 2025-09-13T22:41:32Z; parent(s): 0a03b11c0689264a900f9d61df93bc14e9bc6036
- Exact reading: diff parent1 lines1–115; message parent1 lines1–1
- Attribution: GitHub-linked wu-vincent author, not exclusive authorship of copied dependencies or merged work.

Attributes can hold anonymous class/struct/union/enum model objects, mark their separately visited definitions implicit, and render them inline before variable name. Jinja loop-level filtering of implicit entries makes loop.last reflect rendered objects, avoiding dangling separators; empty structure-content indentation is suppressed. Type annotation not yet widened despite object values.


<a id="commit-025"></a>
## 025. fix: update parent handling in object and visitor logic {#commit-025}

- Commit: [628052f26527736f398a28c27864110a93749237](https://github.com/EndstoneMC/dwarf2cpp/commit/628052f26527736f398a28c27864110a93749237)
- Date: 2025-09-13T23:47:23Z; parent(s): 08c91aec73271a231215d8bd02980c09ec04d092
- Exact reading: diff parent1 lines1–25; message parent1 lines1–1
- Attribution: GitHub-linked wu-vincent author, not exclusive authorship of copied dependencies or merged work.

Sets struct-member parent links and excludes Object.parent from dataclass equality. Parent assignment creates a bidirectional model graph; excluding parent prevents recursive comparison during deduplication (causal inference from structure, no message detail). Parent annotation still says Namespace only.


<a id="commit-026"></a>
## 026. feat: add support for detecting and rendering static members {#commit-026}

- Commit: [421f8d1409831cb0430055a68d11e3e707856587](https://github.com/EndstoneMC/dwarf2cpp/commit/421f8d1409831cb0430055a68d11e3e707856587)
- Date: 2025-09-14T11:33:56Z; parent(s): 628052f26527736f398a28c27864110a93749237
- Exact reading: diff parent1 lines1–36; message parent1 lines1–1
- Attribution: GitHub-linked wu-vincent author, not exclusive authorship of copied dependencies or merged work.

Adds Attribute.is_static and rendering; DW_TAG_member with DW_AT_external is flagged static after visitation. Later DW_TAG_variable handling is required for another compiler encoding (commit 87).


<a id="commit-027"></a>
## 027. feat(visitor): add float and double to string conversion {#commit-027}

- Commit: [1ffe7b3bc7435db2c95e61dcf77f366e0303676d](https://github.com/EndstoneMC/dwarf2cpp/commit/1ffe7b3bc7435db2c95e61dcf77f366e0303676d)
- Date: 2025-09-14T15:25:03Z; parent(s): 421f8d1409831cb0430055a68d11e3e707856587
- Exact reading: diff parent1 lines1–83; message parent1 lines1–1
- Attribution: GitHub-linked wu-vincent author, not exclusive authorship of copied dependencies or merged work.

Converts integer DWARF constant bit patterns to float/double and renders fixed decimal precision (7/16 fractional digits, trailing-zero removal with .0 preserved). Adds double support. Not round-trip-guaranteed for extreme magnitudes, NaN/Inf or endian-independent binary decoding; no tests provided. Other hunks formatting.


<a id="commit-028"></a>
## 028. chore: exclude unnecessary file from wheel build {#commit-028}

- Commit: [7e397ee8e505377e27d6633a3335ca5dbe6e34f4](https://github.com/EndstoneMC/dwarf2cpp/commit/7e397ee8e505377e27d6633a3335ca5dbe6e34f4)
- Date: 2025-09-14T15:36:56Z; parent(s): 1ffe7b3bc7435db2c95e61dcf77f366e0303676d
- Exact reading: diff parent1 lines1–14; message parent1 lines1–1
- Attribution: GitHub-linked wu-vincent author, not exclusive authorship of copied dependencies or merged work.

Attempts to exclude src/dwarf2cpp/_dwarf.cpp from built wheel via scikit-build wheel.exclude; later generalized to *.cpp, so initial pattern should not be assumed effective.
