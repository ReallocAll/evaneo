<!-- retrieval: {"source_ids":["public:commit:054aed0e66c33928ee1cd48567dbd077bb49fbe5","public:commit:0bbb6b1286f425deab0be85860d465578d28ea05","public:commit:16f9c45efd16962a96be9913801d74b097abdb3d","public:commit:218f4c8100fb53c46d235772f99c3ff50b22d0e8","public:commit:3346fbb6a2fc7220a5faeb1e6cb48b2c6847f2e8","public:commit:3eae0ee8b2b6aa7d222d7ff4ff5c42fda7474f01","public:commit:40fd0a10d5c6e2606f5f79b5273bd711dda4fb67","public:commit:46fb1168427f56cc286d938aca8b5a1f7d74757c","public:commit:47d483de7a0906af81dbe7f448da64e9dd1c3073","public:commit:481a028345d769aa153668926aba9cab28acb04a","public:commit:60145da56fd7e4ff302d67a2cc0588112840f1d1","public:commit:6926d1e45f811fb658d4c882f4926ffce0291a75","public:commit:69b4fc7cba1cbfc3e90fc45c121041441997ed36","public:commit:6b6f5bd3425650324add11f22b9ab54298bb8d88","public:commit:6f6b73d59aeeac1128b31ee349f5510cface5d5d","public:commit:77448be8ebcde87600b89be172a6ee7f18c05f70","public:commit:c14628bb01fc7c507ca48570e2303bab8308b529","public:commit:c35b9e2aad279434ea5887b67d6387b81ebd974b","public:commit:cb94d4832e9ce8609e1a0b8b2364ad35b67bbaf1","public:commit:de41522a74f7211432ecaa59758c882ed1f9a1dc","public:commit:ea94b81ce8c8e96eb2474a5e1eb5336c98d53f98","public:commit:ec623b546a3333da640d978355092d0386363b9a","public:commit:eccf00b03a8e48a48ed022ddb8f50d738f4307fb"],"source_type":"public","date":"2025-10-01..2025-10-29","topics":["lifetime","ffi","testing","api","review","selection","refactoring"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="dwarf2cpp-type-unit-and-lifetime"></a>
# Dwarf2cpp: type unit and lifetime {#dwarf2cpp-type-unit-and-lifetime}

Each dossier presents its commits in causal DAG order. The numbering is stable;94 precedes93 because93 is its child. Read the cross-cutting [engineering synthesis](../ENGINEERING_SYNTHESIS.md) for revision chains, applicability, counterexamples and validation limits.


<a id="commit-054"></a>
## 054. feat: add resolve_type_unit_reference method to DWARFDie {#commit-054}

- Commit: [6b6f5bd3425650324add11f22b9ab54298bb8d88](https://github.com/EndstoneMC/dwarf2cpp/commit/6b6f5bd3425650324add11f22b9ab54298bb8d88)
- Date: 2025-10-01T10:52:19Z; parent(s): ee5b938c95f4ea9c36e1328998a8c534ef96c90c
- Exact reading: diff parent1 lines1–546; message parent1 lines1–1
- Attribution: GitHub-linked wu-vincent author, not exclusive authorship of copied dependencies or merged work.

Entire binding file reformatted; substantive addition is resolve_type_unit_reference wrapper returning optional DIE and matching stub. Full 546-line diff read, not misclassified by large churn. Exposes LLVM resolution rather than implementing resolution in Python.


<a id="commit-055"></a>
## 055. feat: add new properties and methods for DWARFType unit handling {#commit-055}

- Commit: [cb94d4832e9ce8609e1a0b8b2364ad35b67bbaf1](https://github.com/EndstoneMC/dwarf2cpp/commit/cb94d4832e9ce8609e1a0b8b2364ad35b67bbaf1)
- Date: 2025-10-01T13:02:55Z; parent(s): 6b6f5bd3425650324add11f22b9ab54298bb8d88
- Exact reading: diff parent1 lines1–82; message parent1 lines1–1
- Attribution: GitHub-linked wu-vincent author, not exclusive authorship of copied dependencies or merged work.

Exposes types-section enumeration, unit offset/is_type_unit and DIE.unit to Python with stub additions. Supplies identity/context needed to avoid conflating offsets from different DWARF sections. No type-unit execution test.


<a id="commit-056"></a>
## 056. refactor(visitor): replace `_cache` with `_objects` for type unit-aware storage and improve type handling {#commit-056}

- Commit: [3eae0ee8b2b6aa7d222d7ff4ff5c42fda7474f01](https://github.com/EndstoneMC/dwarf2cpp/commit/3eae0ee8b2b6aa7d222d7ff4ff5c42fda7474f01)
- Date: 2025-10-01T13:25:49Z; parent(s): cb94d4832e9ce8609e1a0b8b2364ad35b67bbaf1
- Exact reading: diff parent1 lines1–406; message parent1 lines1–1
- Attribution: GitHub-linked wu-vincent author, not exclusive authorship of copied dependencies or merged work.

Replaces single offset cache with _objects keyed by is_type_unit then offset and routes all model lookup/registration through _get/_set; parent annotation now admits Object. Begins following type-unit references for composite types and ignores GNU call-site metadata. Uses normpath for one source path branch. Critically includes temporary break after compile-unit index 40, limiting analysis despite title describing refactor; next commit removes it. New read helper uses truthiness of cached object. Identity separation is only boolean type-unit partition, not arbitrary file/context identity.


<a id="commit-057"></a>
## 057. fix: use `resolve_type_unit_reference` for type resolution {#commit-057}

- Commit: [46fb1168427f56cc286d938aca8b5a1f7d74757c](https://github.com/EndstoneMC/dwarf2cpp/commit/46fb1168427f56cc286d938aca8b5a1f7d74757c)
- Date: 2025-10-01T13:38:08Z; parent(s): 3eae0ee8b2b6aa7d222d7ff4ff5c42fda7474f01
- Exact reading: diff parent1 lines1–97; message parent1 lines1–1
- Attribution: GitHub-linked wu-vincent author, not exclusive authorship of copied dependencies or merged work.

Removes temporary 41-compile-unit cutoff and resolves type-unit references at typedef/enum/function/parameter/template/variable/inheritance consumption points. This is semantic propagation of a reference abstraction, not merely a renaming; some repeated resolution remains centralized later.


<a id="commit-058"></a>
## 058. fix(visitor): correct type hinting {#commit-058}

- Commit: [47d483de7a0906af81dbe7f448da64e9dd1c3073](https://github.com/EndstoneMC/dwarf2cpp/commit/47d483de7a0906af81dbe7f448da64e9dd1c3073)
- Date: 2025-10-01T13:43:09Z; parent(s): 46fb1168427f56cc286d938aca8b5a1f7d74757c
- Exact reading: diff parent1 lines1–13; message parent1 lines1–1
- Attribution: GitHub-linked wu-vincent author, not exclusive authorship of copied dependencies or merged work.

Corrects Generator type annotation to include send/return None. Full patch only annotation; runtime typing evaluation compatibility may matter because annotations are not postponed in file, but no execution evidence supplied.


<a id="commit-059"></a>
## 059. style: fix formatting {#commit-059}

- Commit: [6f6b73d59aeeac1128b31ee349f5510cface5d5d](https://github.com/EndstoneMC/dwarf2cpp/commit/6f6b73d59aeeac1128b31ee349f5510cface5d5d)
- Date: 2025-10-01T13:49:31Z; parent(s): 47d483de7a0906af81dbe7f448da64e9dd1c3073
- Exact reading: diff parent1 lines1–41; message parent1 lines1–1
- Attribution: GitHub-linked wu-vincent author, not exclusive authorship of copied dependencies or merged work.

Reformats tqdm expression and multiline type resolution calls. Full diff read; no intentional behavioral change or independent engineering principle.


<a id="commit-060"></a>
## 060. fix(visitor): handle `decl_file` assignment more robustly {#commit-060}

- Commit: [40fd0a10d5c6e2606f5f79b5273bd711dda4fb67](https://github.com/EndstoneMC/dwarf2cpp/commit/40fd0a10d5c6e2606f5f79b5273bd711dda4fb67)
- Date: 2025-10-01T14:18:58Z; parent(s): 6f6b73d59aeeac1128b31ee349f5510cface5d5d
- Exact reading: diff parent1 lines1–32; message parent1 lines1–1
- Attribution: GitHub-linked wu-vincent author, not exclusive authorship of copied dependencies or merged work.

Uses computed child.decl_file rather than direct DW_AT_decl_file presence, allowing recursively inherited specification location and guarding missing paths before replace. Both compile-unit and namespace paths updated. This aligns filtering with binding's findRecursively semantics.


<a id="commit-061"></a>
## 061. fix(visitor): replace `abspath` with `normpath` to correct logics {#commit-061}

- Commit: [ea94b81ce8c8e96eb2474a5e1eb5336c98d53f98](https://github.com/EndstoneMC/dwarf2cpp/commit/ea94b81ce8c8e96eb2474a5e1eb5336c98d53f98)
- Date: 2025-10-01T14:36:23Z; parent(s): 40fd0a10d5c6e2606f5f79b5273bd711dda4fb67
- Exact reading: diff parent1 lines1–13; message parent1 lines1–1
- Attribution: GitHub-linked wu-vincent author, not exclusive authorship of copied dependencies or merged work.

Finishes abspath-to-normpath correction in namespace branch. Avoids resolving foreign compilation paths against host current working directory; causal portability reasoning follows path operations, not an explicit detailed message.


<a id="commit-062"></a>
## 062. fix: printer now prints qualified name for typedef types {#commit-062}

- Commit: [0bbb6b1286f425deab0be85860d465578d28ea05](https://github.com/EndstoneMC/dwarf2cpp/commit/0bbb6b1286f425deab0be85860d465578d28ea05)
- Date: 2025-10-01T14:56:16Z; parent(s): ea94b81ce8c8e96eb2474a5e1eb5336c98d53f98
- Exact reading: diff parent1 lines1–963; message parent1 lines1–1
- Attribution: GitHub-linked wu-vincent author, not exclusive authorship of copied dependencies or merged work.

Vendors LLVM DWARFTypePrinter implementation/header and routes bindings to it, with explicit local FIXME adding DW_TAG_typedef to scoped tags so names such as std::string remain qualified, including nested recursion. Adds qualified-name-before wrapper and deletes Python scoped_tags/relative-scope manipulation in favor of native printer. Full 751-line C++ body and 67-line header read: recursive arrays/pointer/member-pointer/function/cv/ref declarators, language lower bounds, template args, calling-convention attributes, pointer authentication and scope stopping. Code identifies LLVM provenance (Apache-2.0 with LLVM exception header) and Clang-derived character rendering with acknowledged incompleteness; do not credit bulk upstream implementation as Wu's original invention. No independent upstream-version byte comparison yet, so only explicitly marked local typedef change and observed integration are attributed. Several fallback outputs intentionally describe types rather than guaranteed compilable C++; pointer template arguments omitted, unknown tags fall back, and char handling has TODOs. Cost is maintaining a substantial copied library implementation, later retired against LLVM22.


<a id="commit-063"></a>
## 063. feat: add `merge` method for `TypeDef` {#commit-063}

- Commit: [c35b9e2aad279434ea5887b67d6387b81ebd974b](https://github.com/EndstoneMC/dwarf2cpp/commit/c35b9e2aad279434ea5887b67d6387b81ebd974b)
- Date: 2025-10-01T15:22:40Z; parent(s): 0bbb6b1286f425deab0be85860d465578d28ea05
- Exact reading: diff parent1 lines1–64; message parent1 lines1–1
- Attribution: GitHub-linked wu-vincent author, not exclusive authorship of copied dependencies or merged work.

TypeDef.merge checks matching kind/name/value runtime type, requires exact string target or recursively merges inline object target, then coalesces alignment; normalizes all merge annotations to Object. None targets fall into self.value.merge and can fail, fixed when overflow folding makes path reachable in commit112.


<a id="commit-064"></a>
## 064. refactor: improve logging messages {#commit-064}

- Commit: [054aed0e66c33928ee1cd48567dbd077bb49fbe5](https://github.com/EndstoneMC/dwarf2cpp/commit/054aed0e66c33928ee1cd48567dbd077bb49fbe5)
- Date: 2025-10-01T15:23:14Z; parent(s): c35b9e2aad279434ea5887b67d6387b81ebd974b
- Exact reading: diff parent1 lines1–35; message parent1 lines1–1
- Attribution: GitHub-linked wu-vincent author, not exclusive authorship of copied dependencies or merged work.

Progress messages drop unmatched trailing parenthesis, show skipped compilation directory and avoid unused CU-name local. Introduces incorrect relative-path argument choice for visiting description, corrected immediately next commit. No traversal behavior change.


<a id="commit-065"></a>
## 065. refactor: improve logging messages {#commit-065}

- Commit: [60145da56fd7e4ff302d67a2cc0588112840f1d1](https://github.com/EndstoneMC/dwarf2cpp/commit/60145da56fd7e4ff302d67a2cc0588112840f1d1)
- Date: 2025-10-01T15:28:19Z; parent(s): 054aed0e66c33928ee1cd48567dbd077bb49fbe5
- Exact reading: diff parent1 lines1–13; message parent1 lines1–1
- Attribution: GitHub-linked wu-vincent author, not exclusive authorship of copied dependencies or merged work.

Fixes visited CU display to relpath(cu_die.short_name, base_dir), rather than base_dir relative to compilation_dir. Observation/logging correction only.


<a id="commit-066"></a>
## 066. fix(models): correct type hint for `default_value` to include `str` {#commit-066}

- Commit: [6926d1e45f811fb658d4c882f4926ffce0291a75](https://github.com/EndstoneMC/dwarf2cpp/commit/6926d1e45f811fb658d4c882f4926ffce0291a75)
- Date: 2025-10-01T15:50:09Z; parent(s): 60145da56fd7e4ff302d67a2cc0588112840f1d1
- Exact reading: diff parent1 lines1–13; message parent1 lines1–1
- Attribution: GitHub-linked wu-vincent author, not exclusive authorship of copied dependencies or merged work.

Attribute.default_value type annotation changes from int|float to int|str, matching rendered decimal/bool literal strings already produced. Interface alignment, no runtime transformation.


<a id="commit-067"></a>
## 067. fix(models): use `is` and `is not` for type comparisons {#commit-067}

- Commit: [69b4fc7cba1cbfc3e90fc45c121041441997ed36](https://github.com/EndstoneMC/dwarf2cpp/commit/69b4fc7cba1cbfc3e90fc45c121041441997ed36)
- Date: 2025-10-01T15:50:48Z; parent(s): 6926d1e45f811fb658d4c882f4926ffce0291a75
- Exact reading: diff parent1 lines1–13; message parent1 lines1–1
- Attribution: GitHub-linked wu-vincent author, not exclusive authorship of copied dependencies or merged work.

Uses type identity rather than != for TypeDef target runtime classes. Narrow comparison clarity; does not fix None merge path yet.


<a id="commit-068"></a>
## 068. refactor: replace `get_qualified_type` with `_resolve_type` for improved type resolution {#commit-068}

- Commit: [c14628bb01fc7c507ca48570e2303bab8308b529](https://github.com/EndstoneMC/dwarf2cpp/commit/c14628bb01fc7c507ca48570e2303bab8308b529)
- Date: 2025-10-04T17:00:40Z; parent(s): 69b4fc7cba1cbfc3e90fc45c121041441997ed36
- Exact reading: diff parent1 lines1–170; message parent1 lines1–1
- Attribution: GitHub-linked wu-vincent author, not exclusive authorship of copied dependencies or merged work.

Moves globally cached get_qualified_type into per-Visitor _resolve_type and _types map keyed by (is_type_unit,offset,split), centralizing signature resolution and giving cache lifecycle the owning context's lifetime. Unifies compile/type unit traversal through _handle_unit. Type-unit visitation TODO remains; next two commits compare lazy and eager approaches.


<a id="commit-069"></a>
## 069. feat(visitor): enhance type unit handling {#commit-069}

- Commit: [218f4c8100fb53c46d235772f99c3ff50b22d0e8](https://github.com/EndstoneMC/dwarf2cpp/commit/218f4c8100fb53c46d235772f99c3ff50b22d0e8)
- Date: 2025-10-04T17:42:25Z; parent(s): c14628bb01fc7c507ca48570e2303bab8308b529
- Exact reading: diff parent1 lines1–66; message parent1 lines1–1
- Attribution: GitHub-linked wu-vincent author, not exclusive authorship of copied dependencies or merged work.

Flattens model map to tuple (is_type_unit,offset), adds lazy type-chain traversal during resolution and visited type-unit set to load referenced units once. Mark-before-visit avoids immediate repeated visitation. Traversal still assumes well-formed type chain; no explicit arbitrary cycle guard for DW_AT_type chain.


<a id="commit-070"></a>
## 070. feat(visitor): enhance type unit handling {#commit-070}

- Commit: [3346fbb6a2fc7220a5faeb1e6cb48b2c6847f2e8](https://github.com/EndstoneMC/dwarf2cpp/commit/3346fbb6a2fc7220a5faeb1e6cb48b2c6847f2e8)
- Date: 2025-10-04T18:18:55Z; parent(s): 218f4c8100fb53c46d235772f99c3ff50b22d0e8
- Exact reading: diff parent1 lines1–49; message parent1 lines1–1
- Attribution: GitHub-linked wu-vincent author, not exclusive authorship of copied dependencies or merged work.

Reverses lazy per-resolution type-unit discovery: visits all types_section_units before compilation units, removes visited set/type-chain loop, retaining per-context caches. This is concrete architecture revision from demand traversal to staged preprocessing. No benchmark or explicit cost rationale accompanies it.


<a id="commit-071"></a>
## 071. feat(dwarf2cpp): add polyfills for DW_AT_signature support from LLVM 20 {#commit-071}

- Commit: [eccf00b03a8e48a48ed022ddb8f50d738f4307fb](https://github.com/EndstoneMC/dwarf2cpp/commit/eccf00b03a8e48a48ed022ddb8f50d738f4307fb)
- Date: 2025-10-09T16:27:02Z; parent(s): 3346fbb6a2fc7220a5faeb1e6cb48b2c6847f2e8
- Exact reading: diff parent1 lines1–155; message parent1 lines1–1
- Attribution: GitHub-linked wu-vincent author, not exclusive authorship of copied dependencies or merged work.

Backports LLVM20 recursive attribute lookup while linked to LLVM19: stack plus Seen set follows abstract_origin/specification/signature and stops cycles, with form resolution for unit-relative/debug-info/signature references. Binds name/linkage/decl-line/file to this lookup; comments explicitly mark polyfill and removal after LLVM20. Attribution belongs to LLVM implementation; local work is version bridge/integration. Python location filtering consolidated. Not evidence to retain permanent fork after dependency upgrade.


<a id="commit-072"></a>
## 072. feat(visitor): add support for DW_AT_signature in type handling {#commit-072}

- Commit: [ec623b546a3333da640d978355092d0386363b9a](https://github.com/EndstoneMC/dwarf2cpp/commit/ec623b546a3333da640d978355092d0386363b9a)
- Date: 2025-10-09T16:42:24Z; parent(s): eccf00b03a8e48a48ed022ddb8f50d738f4307fb
- Exact reading: diff parent1 lines1–80; message parent1 lines1–1
- Attribution: GitHub-linked wu-vincent author, not exclusive authorship of copied dependencies or merged work.

When class/struct/union/enum has DW_AT_signature, resolves and visits target then copies its model before local handling; previous approach created empty local object and visited referenced definition separately. Allows namespace parent to match by name. Initial shallow copies risk shared nested members, corrected to deepcopy for structures in74.


<a id="commit-073"></a>
## 073. refactor(visitor): rename variables for clarity in type handling {#commit-073}

- Commit: [481a028345d769aa153668926aba9cab28acb04a](https://github.com/EndstoneMC/dwarf2cpp/commit/481a028345d769aa153668926aba9cab28acb04a)
- Date: 2025-10-09T19:58:01Z; parent(s): ec623b546a3333da640d978355092d0386363b9a
- Exact reading: diff parent1 lines1–32; message parent1 lines1–1
- Attribution: GitHub-linked wu-vincent author, not exclusive authorship of copied dependencies or merged work.

Renames cls locals to union/struct in corresponding handlers. Full diff read; mechanical clarity with unchanged behavior.


<a id="commit-074"></a>
## 074. refactor(visitor): simplify `_handle_struct` logic and unify type handling mechanism {#commit-074}

- Commit: [de41522a74f7211432ecaa59758c882ed1f9a1dc](https://github.com/EndstoneMC/dwarf2cpp/commit/de41522a74f7211432ecaa59758c882ed1f9a1dc)
- Date: 2025-10-10T14:21:53Z; parent(s): 481a028345d769aa153668926aba9cab28acb04a
- Exact reading: diff parent1 lines1–74; message parent1 lines1–1
- Attribution: GitHub-linked wu-vincent author, not exclusive authorship of copied dependencies or merged work.

Centralizes signature-aware class/struct/union handling by passing model class to _handle_struct; verifies referenced declaration exists and deep-copies it instead of sharing nested mutable lists/maps. Enum retains separate shallow-copy logic. Distinguish this ownership fix from simple deduplication of code.


<a id="commit-075"></a>
## 075. feat(visitor): add handling for char default values in DW_AT_const_value {#commit-075}

- Commit: [16f9c45efd16962a96be9913801d74b097abdb3d](https://github.com/EndstoneMC/dwarf2cpp/commit/16f9c45efd16962a96be9913801d74b097abdb3d)
- Date: 2025-10-10T14:59:41Z; parent(s): de41522a74f7211432ecaa59758c882ed1f9a1dc
- Exact reading: diff parent1 lines1–28; message parent1 lines1–1
- Attribution: GitHub-linked wu-vincent author, not exclusive authorship of copied dependencies or merged work.

Prints printable ASCII char default values as quoted characters while retaining integer fallback; renames int_value to val. Range includes quote and backslash but code does not escape them, so reconstructed literals for those values remain a concrete static risk. No regression fixture.


<a id="commit-076"></a>
## 076. feat(visitor): add handling for attributes {#commit-076}

- Commit: [77448be8ebcde87600b89be172a6ee7f18c05f70](https://github.com/EndstoneMC/dwarf2cpp/commit/77448be8ebcde87600b89be172a6ee7f18c05f70)
- Date: 2025-10-29T18:56:33Z; parent(s): 16f9c45efd16962a96be9913801d74b097abdb3d
- Exact reading: diff parent1 lines1–41; message parent1 lines1–1
- Attribution: GitHub-linked wu-vincent author, not exclusive authorship of copied dependencies or merged work.

Handles typedef accessibility, GNU template-template default from template name, and ignores DW_AT_data_bit_offset. Targeted DWARF attribute compatibility; ignored location metadata is not evidence of ABI-exact bitfield reconstruction.
