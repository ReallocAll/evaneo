<!-- retrieval: {"source_ids":["public:commit:003a439c9efc6dcec29db69ea993cff9346833bf","public:commit:09d9741778b5ab29d47ccb3058be5c20d1b34b46","public:commit:0a82030da895059a741540e5a81f1742e15b48d8","public:commit:0db6ce3b3bafd3bbfe772d2bb3fbeb260746291e","public:commit:129423285a309092bfdead9e188b7767af695277","public:commit:193dbba90cd198facee244f0afaa7563d7959178","public:commit:2cc982d5049b630136d8320a3b571a7a1e01961d","public:commit:2eacf6e82d46d35384309562fc6d822a230834be","public:commit:31cbdda8275b99680acb3706c1d25c447c2e03fd","public:commit:34df05632dfc446f41f429fdb18d12364f025a64","public:commit:429b076af8aa1ba42c71c2209e331fc264a361a8","public:commit:4a6005cae77ca85b4bc59dbc2c01a9c65a855798","public:commit:4a67cfd6962d5be34cfe616c3e000fd0b54755c3","public:commit:4b95995a7f48902b1e3b3451c362a88e34542a15","public:commit:4d13f94c80c2a0728e930d4d1bb30fca6484da7d","public:commit:6879f26820d02452cccf8760db921fd6fedbb283","public:commit:8e8a7ab5df77c12d4508a4188e500996e0da2552","public:commit:9929bc05285532ba721997496f1c3885e751f503","public:commit:a275e23419bd0769c89d0a91e0a26e4b1b07ab20","public:commit:cba8a9e22e98288efa4360ed22b2d7cb5bcc71d2","public:commit:d441ca2478ef7fe7ca5347d805e1697a26d1771f","public:commit:d4b8fcd6e4202e14d54ef2ad777f3c31e1d798e5","public:commit:e4eabe6495524478d905cb9a1aad7adf21894729","public:commit:ee5b938c95f4ea9c36e1328998a8c534ef96c90c","public:commit:f393d99874df0cd87f17ce63f3b92be55926eb9c"],"source_type":"public","date":"2025-09-14..2025-10-01","topics":["ffi","testing","build","performance","api","diagnosis","documentation","review","refactoring"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="dwarf2cpp-declarators-templates-merging"></a>
# Dwarf2cpp: declarators templates merging {#dwarf2cpp-declarators-templates-merging}

Each dossier presents its commits in causal DAG order. The numbering is stable;94 precedes93 because93 is its child. Read the cross-cutting [engineering synthesis](../ENGINEERING_SYNTHESIS.md) for revision chains, applicability, counterexamples and validation limits.


<a id="commit-029"></a>
## 029. feat: support split-qualified types {#commit-029}

- Commit: [2eacf6e82d46d35384309562fc6d822a230834be](https://github.com/EndstoneMC/dwarf2cpp/commit/2eacf6e82d46d35384309562fc6d822a230834be)
- Date: 2025-09-14T16:55:32Z; parent(s): 7e397ee8e505377e27d6633a3335ca5dbe6e34f4
- Exact reading: diff parent1 lines1–225; message parent1 lines1–1
- Attribution: GitHub-linked wu-vincent author, not exclusive authorship of copied dependencies or merged work.

Architectural declarator correction: exposes LLVM appendUnqualifiedNameBefore/After; type resolution returns either a simple string or a (before,after) tuple around identifier insertion, used for parameters and variables. Deletes bespoke array/C/member-function-pointer regex parser. insert_name joins the two halves, with pointer spacing and array boundary rule. Complex syntax now comes from LLVM recursive type traversal rather than regex; no execution or golden regression test accompanies migration.


<a id="commit-030"></a>
## 030. feat: add stubs {#commit-030}

- Commit: [9929bc05285532ba721997496f1c3885e751f503](https://github.com/EndstoneMC/dwarf2cpp/commit/9929bc05285532ba721997496f1c3885e751f503)
- Date: 2025-09-15T15:54:33Z; parent(s): 2eacf6e82d46d35384309562fc6d822a230834be
- Exact reading: diff parent1 lines1–118; message parent1 lines1–1
- Attribution: GitHub-linked wu-vincent author, not exclusive authorship of copied dependencies or merged work.

Adds handwritten binding stubs covering enums, contexts, units, DIE/form access and split printer API. Structure matches existing exports, but InlineAttribute.DECLARED_INLINED is written as 2, same as DECLARED_NOT_INLINED, whereas bindings reference distinct LLVM constants. Nullable names also not reflected consistently. Useful boundary documentation but source-of-truth drift risk; later generated stubs replace them.


<a id="commit-031"></a>
## 031. chore: add deps to `pyproject.toml` {#commit-031}

- Commit: [2cc982d5049b630136d8320a3b571a7a1e01961d](https://github.com/EndstoneMC/dwarf2cpp/commit/2cc982d5049b630136d8320a3b571a7a1e01961d)
- Date: 2025-09-15T15:54:45Z; parent(s): 9929bc05285532ba721997496f1c3885e751f503
- Exact reading: diff parent1 lines1–13; message parent1 lines1–1
- Attribution: GitHub-linked wu-vincent author, not exclusive authorship of copied dependencies or merged work.

Declares already-imported click and jinja2 runtime dependencies, closing installation metadata gaps. No dependency versions or tests added.


<a id="commit-032"></a>
## 032. feat(visitor): handle default access for class and struct members {#commit-032}

- Commit: [193dbba90cd198facee244f0afaa7563d7959178](https://github.com/EndstoneMC/dwarf2cpp/commit/193dbba90cd198facee244f0afaa7563d7959178)
- Date: 2025-09-15T16:33:38Z; parent(s): 2cc982d5049b630136d8320a3b571a7a1e01961d
- Exact reading: diff parent1 lines1–92; message parent1 lines1–1
- Attribution: GitHub-linked wu-vincent author, not exclusive authorship of copied dependencies or merged work.

Defaults missing member access to private for Class and public for other structures/unions, with explanatory DWARF semantics comment. Template starts at corresponding C++ default so unnecessary access labels disappear. Separately names inheritance access to avoid reusing member default variable. Removes unused typing import in stub.


<a id="commit-033"></a>
## 033. refactor: simplify cache lookup logic in visitor.py {#commit-033}

- Commit: [4b95995a7f48902b1e3b3451c362a88e34542a15](https://github.com/EndstoneMC/dwarf2cpp/commit/4b95995a7f48902b1e3b3451c362a88e34542a15)
- Date: 2025-09-15T17:35:10Z; parent(s): 193dbba90cd198facee244f0afaa7563d7959178
- Exact reading: diff parent1 lines1–16; message parent1 lines1–1
- Attribution: GitHub-linked wu-vincent author, not exclusive authorship of copied dependencies or merged work.

Replaces get+None check with membership plus indexed cache lookup. Under current cache populated only by objects, behavior is equivalent; if None were later a sentinel this would differ. Small refactor, not optimization evidence.


<a id="commit-034"></a>
## 034. feat: add merge functionality {#commit-034}

- Commit: [4d13f94c80c2a0728e930d4d1bb30fca6484da7d](https://github.com/EndstoneMC/dwarf2cpp/commit/4d13f94c80c2a0728e930d4d1bb30fca6484da7d)
- Date: 2025-09-15T17:53:22Z; parent(s): 4b95995a7f48902b1e3b3451c362a88e34542a15
- Exact reading: diff parent1 lines1–90; message parent1 lines1–1
- Attribution: GitHub-linked wu-vincent author, not exclusive authorship of copied dependencies or merged work.

Adds semantic merge protocol: per-line dedup first tests equality, then asks last accumulated object's merge; Attribute merges matching name/type and fills missing metadata/defaults. Removes template marker and clearing default from attribute visitation. Initial is_static None check cannot fill its False default; next commit uses logical OR. Order-sensitive local merging rather than globally proven symbol identity.


<a id="commit-035"></a>
## 035. feat: add merge logics for Functions and Structs {#commit-035}

- Commit: [d441ca2478ef7fe7ca5347d805e1697a26d1771f](https://github.com/EndstoneMC/dwarf2cpp/commit/d441ca2478ef7fe7ca5347d805e1697a26d1771f)
- Date: 2025-09-15T18:58:55Z; parent(s): 4d13f94c80c2a0728e930d4d1bb30fca6484da7d
- Exact reading: diff parent1 lines1–120; message parent1 lines1–3
- Attribution: GitHub-linked wu-vincent author, not exclusive authorship of copied dependencies or merged work.

Fix #6 extends merge to Function and Struct. Functions require same name, return, arity and parameter type/kind, fill names and OR flags; structs require kind/name/bases then recursively combine line-grouped members. Base Object merge becomes conservative False; attribute flags coalesce via OR. Constness is merged rather than included in function identity, a potential overload-collapsing risk when source-line grouping collides. No test proves algebraic properties or order independence.

The complete message source linked above records any explicit diagnosis. Behavioral explanation is static analysis; no successful execution is inferred.


<a id="commit-036"></a>
## 036. fix: handle cases for default value being bool {#commit-036}

- Commit: [129423285a309092bfdead9e188b7767af695277](https://github.com/EndstoneMC/dwarf2cpp/commit/129423285a309092bfdead9e188b7767af695277)
- Date: 2025-09-15T19:27:57Z; parent(s): d441ca2478ef7fe7ca5347d805e1697a26d1771f
- Exact reading: diff parent1 lines1–69; message parent1 lines1–1
- Attribution: GitHub-linked wu-vincent author, not exclusive authorship of copied dependencies or merged work.

Always returns before/after tuple for split printing, narrows no-space insertion to pointer followed by ')', and moves constant conversion into DW_AT_const_value. Checks type-prefix suffix for float/double/bool, emits true/false for bool, preserves integer otherwise. This adapts constant handling to the new representation but keeps textual type tests and native struct bit conversion.


<a id="commit-037"></a>
## 037. feat: add template support for attributes {#commit-037}

- Commit: [31cbdda8275b99680acb3706c1d25c447c2e03fd](https://github.com/EndstoneMC/dwarf2cpp/commit/31cbdda8275b99680acb3706c1d25c447c2e03fd)
- Date: 2025-09-15T21:49:23Z; parent(s): 129423285a309092bfdead9e188b7767af695277
- Exact reading: diff parent1 lines1–182; message parent1 lines1–1
- Attribution: GitHub-linked wu-vincent author, not exclusive authorship of copied dependencies or merged work.

Introduces Template/TemplateParameter models, explicit template<> on attribute instances and synthesized generic declaration copied from instance (erases template suffix/default). Registers generic declaration alongside instance in file/namespace. Expands per-line cap from five to eight entries to accommodate template data, but still drops overflow before merging. Parameters have type/constant/pack/template kinds; recovery of original source templates remains approximation.


<a id="commit-038"></a>
## 038. feat: add template support for classes {#commit-038}

- Commit: [429b076af8aa1ba42c71c2209e331fc264a361a8](https://github.com/EndstoneMC/dwarf2cpp/commit/429b076af8aa1ba42c71c2209e331fc264a361a8)
- Date: 2025-09-15T23:08:29Z; parent(s): 31cbdda8275b99680acb3706c1d25c447c2e03fd
- Exact reading: diff parent1 lines1–212; message parent1 lines1–1
- Attribution: GitHub-linked wu-vincent author, not exclusive authorship of copied dependencies or merged work.

Extends template reconstruction to classes: copy declaration, strip specialized name suffix, remove bases/members/alignment, mark forward declaration; attach generic template and instance separately, including nested class scope/access. Template rendering tolerates unnamed parameters and missing declarations. Function template collection exists but activation is commented out; do not count this commit as function-template support.


<a id="commit-039"></a>
## 039. docs: update README.md {#commit-039}

- Commit: [4a6005cae77ca85b4bc59dbc2c01a9c65a855798](https://github.com/EndstoneMC/dwarf2cpp/commit/4a6005cae77ca85b4bc59dbc2c01a9c65a855798)
- Date: 2025-09-15T23:15:55Z; parent(s): 429b076af8aa1ba42c71c2209e331fc264a361a8
- Exact reading: diff parent1 lines1–108; message parent1 lines1–1
- Attribution: GitHub-linked wu-vincent author, not exclusive authorship of copied dependencies or merged work.

Editorial README improvements and matching CLI --base-dir help. Keeps warning that headers may need adjustment and testing is trivial; changes overly absolute any-binary wording to may fail with certain binaries. No runtime change beyond help string.


<a id="commit-040"></a>
## 040. docs: update README.md {#commit-040}

- Commit: [0a82030da895059a741540e5a81f1742e15b48d8](https://github.com/EndstoneMC/dwarf2cpp/commit/0a82030da895059a741540e5a81f1742e15b48d8)
- Date: 2025-09-15T23:16:22Z; parent(s): 4a6005cae77ca85b4bc59dbc2c01a9c65a855798
- Exact reading: diff parent1 lines1–13; message parent1 lines1–1
- Attribution: GitHub-linked wu-vincent author, not exclusive authorship of copied dependencies or merged work.

Removes claim that release binaries inherently fail: only stripped binaries excluded. Important distinction between optimization/build mode and availability of debug information.


<a id="commit-041"></a>
## 041. fix(build): update wheel exclusion to match all .cpp files {#commit-041}

- Commit: [09d9741778b5ab29d47ccb3058be5c20d1b34b46](https://github.com/EndstoneMC/dwarf2cpp/commit/09d9741778b5ab29d47ccb3058be5c20d1b34b46)
- Date: 2025-09-15T23:19:07Z; parent(s): 0a82030da895059a741540e5a81f1742e15b48d8
- Exact reading: diff parent1 lines1–13; message parent1 lines1–1
- Attribution: GitHub-linked wu-vincent author, not exclusive authorship of copied dependencies or merged work.

Changes wheel exclusion from source-tree-specific path to *.cpp. Full two-line delta read; fixes pattern scope but actual wheel contents were not inspected.


<a id="commit-042"></a>
## 042. refactor: update template handling and parameter attributes {#commit-042}

- Commit: [0db6ce3b3bafd3bbfe772d2bb3fbeb260746291e](https://github.com/EndstoneMC/dwarf2cpp/commit/0db6ce3b3bafd3bbfe772d2bb3fbeb260746291e)
- Date: 2025-09-16T13:06:34Z; parent(s): 09d9741778b5ab29d47ccb3058be5c20d1b34b46
- Exact reading: diff parent1 lines1–31; message parent1 lines1–1
- Attribution: GitHub-linked wu-vincent author, not exclusive authorship of copied dependencies or merged work.

Renames template value_type to type, separates actual argument (excluded from equality) and default, and renders type defaults. Visitor call still uses value_type until commit 44, so this is an intermediate cross-layer inconsistency, not an independently complete working change.


<a id="commit-043"></a>
## 043. feat: add merge method to Template class {#commit-043}

- Commit: [8e8a7ab5df77c12d4508a4188e500996e0da2552](https://github.com/EndstoneMC/dwarf2cpp/commit/8e8a7ab5df77c12d4508a4188e500996e0da2552)
- Date: 2025-09-16T13:35:31Z; parent(s): 0db6ce3b3bafd3bbfe772d2bb3fbeb260746291e
- Exact reading: diff parent1 lines1–34; message parent1 lines1–1
- Attribution: GitHub-linked wu-vincent author, not exclusive authorship of copied dependencies or merged work.

Adds Template.merge requiring equal name/declaration/count and compatible parameter name/kind/type with no concrete argument values; merges defaults. Protects declaration versus instantiation distinction, though truthy-or default merge loses distinction for falsey defaults and later parameter models change.


<a id="commit-044"></a>
## 044. refactor: improve template handling and registration logic {#commit-044}

- Commit: [003a439c9efc6dcec29db69ea993cff9346833bf](https://github.com/EndstoneMC/dwarf2cpp/commit/003a439c9efc6dcec29db69ea993cff9346833bf)
- Date: 2025-09-16T14:12:38Z; parent(s): 8e8a7ab5df77c12d4508a4188e500996e0da2552
- Exact reading: diff parent1 lines1–117; message parent1 lines1–1
- Attribution: GitHub-linked wu-vincent author, not exclusive authorship of copied dependencies or merged work.

Registers template declarations by file-or-DIE key and source line, merges duplicates before emission, parses type arguments and DW_AT_default_value, fixes renamed keyword in constant parameter creation. Uses shallow template copy then mutates shared parameter.arg to None, a potential aliasing loss later avoided by to_declaration reconstruction (commit 46). Unknown attributes/children remain explicit errors.


<a id="commit-045"></a>
## 045. feat: support template parameter packs and default values {#commit-045}

- Commit: [d4b8fcd6e4202e14d54ef2ad777f3c31e1d798e5](https://github.com/EndstoneMC/dwarf2cpp/commit/d4b8fcd6e4202e14d54ef2ad777f3c31e1d798e5)
- Date: 2025-09-16T19:52:49Z; parent(s): 003a439c9efc6dcec29db69ea993cff9346833bf
- Exact reading: diff parent1 lines1–117; message parent1 lines1–1
- Attribution: GitHub-linked wu-vincent author, not exclusive authorship of copied dependencies or merged work.

Parses constant template values/defaults and GNU parameter packs from child type/value DIEs; None-aware Jinja default rendering preserves numeric zero. Registration clears arg/pack in declaration copies, still with shared shallow parameter objects. No tests for zero defaults or mixed packs.


<a id="commit-046"></a>
## 046. feat: improve template parameter parsing logics {#commit-046}

- Commit: [cba8a9e22e98288efa4360ed22b2d7cb5bcc71d2](https://github.com/EndstoneMC/dwarf2cpp/commit/cba8a9e22e98288efa4360ed22b2d7cb5bcc71d2)
- Date: 2025-09-16T20:49:26Z; parent(s): d4b8fcd6e4202e14d54ef2ad777f3c31e1d798e5
- Exact reading: diff parent1 lines1–203; message parent1 lines1–1
- Attribution: GitHub-linked wu-vincent author, not exclusive authorship of copied dependencies or merged work.

Redesigns TemplateParameter around kind/name/default/type/value/nested parameters and recursively constructs fresh declaration parameters, removing shared mutation of instantiations. Pack parsing distinguishes type and homogeneous constant packs and asserts no mixed-type inconsistency; GNU template-template name parsed. Temporarily replaces template parameter merge with NotImplementedError and leaves debug print. This is a partial architectural step, completed in commits 47–50.


<a id="commit-047"></a>
## 047. refactor: optimize template rendering logic {#commit-047}

- Commit: [6879f26820d02452cccf8760db921fd6fedbb283](https://github.com/EndstoneMC/dwarf2cpp/commit/6879f26820d02452cccf8760db921fd6fedbb283)
- Date: 2025-09-16T21:11:31Z; parent(s): cba8a9e22e98288efa4360ed22b2d7cb5bcc71d2
- Exact reading: diff parent1 lines1–65; message parent1 lines1–1
- Attribution: GitHub-linked wu-vincent author, not exclusive authorship of copied dependencies or merged work.

Removes temporary merge exception and debug print, passes pack type through declaration conversion, renders typed value packs or typename packs and recursively renders template-template parameters. Parameter merge remains TODO and template-template details corrected next; title's optimize wording is not measured performance evidence.


<a id="commit-048"></a>
## 048. fix(visitor): set type of template packs {#commit-048}

- Commit: [f393d99874df0cd87f17ce63f3b92be55926eb9c](https://github.com/EndstoneMC/dwarf2cpp/commit/f393d99874df0cd87f17ce63f3b92be55926eb9c)
- Date: 2025-09-16T21:18:35Z; parent(s): 6879f26820d02452cccf8760db921fd6fedbb283
- Exact reading: diff parent1 lines1–12; message parent1 lines1–1
- Attribution: GitHub-linked wu-vincent author, not exclusive authorship of copied dependencies or merged work.

Stores inferred pack_type on TemplateParameter after collecting values; enables constant-pack renderer introduced immediately before. One-line behavioral completion, not mechanical.


<a id="commit-049"></a>
## 049. fix: correct template template parameters rendering {#commit-049}

- Commit: [e4eabe6495524478d905cb9a1aad7adf21894729](https://github.com/EndstoneMC/dwarf2cpp/commit/e4eabe6495524478d905cb9a1aad7adf21894729)
- Date: 2025-09-16T21:36:19Z; parent(s): f393d99874df0cd87f17ce63f3b92be55926eb9c
- Exact reading: diff parent1 lines1–15; message parent1 lines1–1
- Attribution: GitHub-linked wu-vincent author, not exclusive authorship of copied dependencies or merged work.

Reverts recursive template-template rendering to the explicit approximation template<typename> class. Original nested template shape is not reconstructed; this is a fidelity limit, not generic complete template support.


<a id="commit-050"></a>
## 050. feat: implement template parameter merging {#commit-050}

- Commit: [4a67cfd6962d5be34cfe616c3e000fd0b54755c3](https://github.com/EndstoneMC/dwarf2cpp/commit/4a67cfd6962d5be34cfe616c3e000fd0b54755c3)
- Date: 2025-09-17T16:39:57Z; parent(s): e4eabe6495524478d905cb9a1aad7adf21894729
- Exact reading: diff parent1 lines1–33; message parent1 lines1–1
- Attribution: GitHub-linked wu-vincent author, not exclusive authorship of copied dependencies or merged work.

Declaration conversion removes concrete pack elements/nested template parameters; Template.merge requires same kind/name/type then coalesces defaults. Replaces TODO with implementation but truthy-or still treats zero default as absent; evidence supports an approximation rather than complete deduction or conflict resolution.


<a id="commit-051"></a>
## 051. feat: add support for function template {#commit-051}

- Commit: [a275e23419bd0769c89d0a91e0a26e4b1b07ab20](https://github.com/EndstoneMC/dwarf2cpp/commit/a275e23419bd0769c89d0a91e0a26e4b1b07ab20)
- Date: 2025-09-17T17:32:34Z; parent(s): 4a67cfd6962d5be34cfe616c3e000fd0b54755c3
- Exact reading: diff parent1 lines1–81; message parent1 lines1–1
- Attribution: GitHub-linked wu-vincent author, not exclusive authorship of copied dependencies or merged work.

Activates function-template parameter capture/rendering, expressly omitting synthesized generic function declaration because there is no trivial way to infer it. Template registration declines objects without a declaration, avoiding duplicate generic output. Packs require common kind; heterogeneous constant types become auto rather than asserting identical type. This retains uncertainty in source reconstruction.


<a id="commit-052"></a>
## 052. refactor(visitor): add relative scope support to type resolution {#commit-052}

- Commit: [34df05632dfc446f41f429fdb18d12364f025a64](https://github.com/EndstoneMC/dwarf2cpp/commit/34df05632dfc446f41f429fdb18d12364f025a64)
- Date: 2025-09-17T18:57:11Z; parent(s): a275e23419bd0769c89d0a91e0a26e4b1b07ab20
- Exact reading: diff parent1 lines1–56; message parent1 lines1–1
- Attribution: GitHub-linked wu-vincent author, not exclusive authorship of copied dependencies or merged work.

Adds optional relative-scope shortening by recursively stripping enclosing qualified-name prefixes from printed type strings; split declarator applies only to before half. No call site adopts relative argument in patch. It is later deleted in commit 62, so not lasting policy.


<a id="commit-053"></a>
## 053. feat: add .clang-format {#commit-053}

- Commit: [ee5b938c95f4ea9c36e1328998a8c534ef96c90c](https://github.com/EndstoneMC/dwarf2cpp/commit/ee5b938c95f4ea9c36e1328998a8c534ef96c90c)
- Date: 2025-10-01T10:49:19Z; parent(s): 34df05632dfc446f41f429fdb18d12364f025a64
- Exact reading: diff parent1 lines1–28; message parent1 lines1–1
- Attribution: GitHub-linked wu-vincent author, not exclusive authorship of copied dependencies or merged work.

Adds LLVM-based clang-format configuration with 4 spaces, 99 columns, explicit binary/operator/template choices and c++20 formatting standard. Formatting settings do not independently change compilation standard.
