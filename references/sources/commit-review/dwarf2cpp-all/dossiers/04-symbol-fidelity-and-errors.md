<!-- retrieval: {"source_ids":["public:commit:134bfe40bda1da714197a8bb66ec8799b58c0669","public:commit:1e150b2f37a99279850b89cc30f0bef56f24592e","public:commit:28cfe0e0e81c97bbf1f28328927718d697ff5dc5","public:commit:3dc43f9f0a0d925cf366c140cc1e8c9d9d278ce0","public:commit:758043f040882fbe944b15ac12f2c10a7ab07b87","public:commit:7f72fe4fe38d4ceb162bb5be5445b95e93090260","public:commit:83b099a592c13346b2f9e73fd9bfbc83e8ec47ee","public:commit:8bf47bd0c99534c6541ec0c01dd1b4b8ae2207b1","public:commit:9486e0d8ade39480822d38762b32f9dba9530f30","public:commit:9721460bd46d5881252eaa75a4974701cbb92b74","public:commit:d0294588c96612d00c600ad6790bd56eec60e496","public:commit:d22d77f353cb6565e46cb8abc0a143da2b071a5e","public:commit:d9649d1b5c922d16ef7f5986d48c309ac6a37a51","public:commit:eb784a26eaf49251ae3483adc5afa3d6d37ff12f","public:commit:ef9c69994f9bfd49a4b98d22b015a0f14331a180","public:commit:f96cfc99d1a0dae6ddd904d1b99752613adfaff3"],"source_type":"public","date":"2025-10-29..2026-05-16","topics":["testing","build","diagnosis","documentation","review","refactoring"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="dwarf2cpp-symbol-fidelity-and-errors"></a>
# Dwarf2cpp: symbol fidelity and errors {#dwarf2cpp-symbol-fidelity-and-errors}

Each dossier presents its commits in causal DAG order. The numbering is stable;94 precedes93 because93 is its child. Read the cross-cutting [engineering synthesis](../ENGINEERING_SYNTHESIS.md) for revision chains, applicability, counterexamples and validation limits.


<a id="commit-077"></a>
## 077. fix: constructors, destructors and operators should have no return type {#commit-077}

- Commit: [1e150b2f37a99279850b89cc30f0bef56f24592e](https://github.com/EndstoneMC/dwarf2cpp/commit/1e150b2f37a99279850b89cc30f0bef56f24592e)
- Date: 2025-10-29T22:09:27Z; parent(s): 77448be8ebcde87600b89be172a6ee7f18c05f70
- Exact reading: diff parent1 lines1–67; message parent1 lines1–1
- Attribution: GitHub-linked wu-vincent author, not exclusive authorship of copied dependencies or merged work.

Moves constructor/destructor/conversion-operator return suppression into function construction before grouping/definition-copying, and excludes member functions from external-C short-name grouping. Comment loosely says operators, but actual startswith('operator ') matches conversion-style names and may include spaced operator spellings; cannot claim all operator overloads lack returns. Previously _handle_struct mutates after creation, so earlier consumers could see erroneous void.


<a id="commit-078"></a>
## 078. refactor(visitor): extract parent type check into `is_member_function` {#commit-078}

- Commit: [83b099a592c13346b2f9e73fd9bfbc83e8ec47ee](https://github.com/EndstoneMC/dwarf2cpp/commit/83b099a592c13346b2f9e73fd9bfbc83e8ec47ee)
- Date: 2025-10-29T22:17:56Z; parent(s): 1e150b2f37a99279850b89cc30f0bef56f24592e
- Exact reading: diff parent1 lines1–43; message parent1 lines1–1
- Attribution: GitHub-linked wu-vincent author, not exclusive authorship of copied dependencies or merged work.

Extracts parent-kind member-function predicate reused for grouping and later qualifier logic. Includes class/enum/union/struct tags; predicate concerns DIE lexical parent and is not universal language semantic analysis.


<a id="commit-079"></a>
## 079. fix(visitor): improve `this` pointer constness check for member functions {#commit-079}

- Commit: [d22d77f353cb6565e46cb8abc0a143da2b071a5e](https://github.com/EndstoneMC/dwarf2cpp/commit/d22d77f353cb6565e46cb8abc0a143da2b071a5e)
- Date: 2025-10-29T22:38:36Z; parent(s): 83b099a592c13346b2f9e73fd9bfbc83e8ec47ee
- Exact reading: diff parent1 lines1–45; message parent1 lines1–1
- Attribution: GitHub-linked wu-vincent author, not exclusive authorship of copied dependencies or merged work.

Replaces arbitrary object-pointer type-chain const search with artificial formal-parameter handling for member functions: requires pointer DIE directly followed by const DIE. Avoids confusing other qualifier positions with pointee constness but initially accepts any artificial parameter; next commit restricts first formal parameter.


<a id="commit-080"></a>
## 080. fix(visitor): refine `this` pointer handling for static and member functions {#commit-080}

- Commit: [d9649d1b5c922d16ef7f5986d48c309ac6a37a51](https://github.com/EndstoneMC/dwarf2cpp/commit/d9649d1b5c922d16ef7f5986d48c309ac6a37a51)
- Date: 2025-10-29T23:15:05Z; parent(s): d22d77f353cb6565e46cb8abc0a143da2b071a5e
- Exact reading: diff parent1 lines1–49; message parent1 lines1–1
- Attribution: GitHub-linked wu-vincent author, not exclusive authorship of copied dependencies or merged work.

Member function starts static by default; first artificial formal parameter clears static and pointer-to-const test determines const. Out-of-line DW_AT_object_pointer now asserts declaration already non-static instead of globally marking absence as static. Ties inference to class membership and parameter position; still relies on compiler DWARF shape and does not prove arbitrary compiler coverage.


<a id="commit-081"></a>
## 081. fix: correct string formatting in typedef.jinja {#commit-081}

- Commit: [eb784a26eaf49251ae3483adc5afa3d6d37ff12f](https://github.com/EndstoneMC/dwarf2cpp/commit/eb784a26eaf49251ae3483adc5afa3d6d37ff12f)
- Date: 2025-12-09T15:29:12Z; parent(s): d9649d1b5c922d16ef7f5986d48c309ac6a37a51
- Exact reading: diff parent1 lines1–10; message parent1 lines1–1
- Attribution: GitHub-linked wu-vincent author, not exclusive authorship of copied dependencies or merged work.

Fixes Jinja alignas formatting from percent-style format filter used on braces to str.format. A two-line patch with real runtime effect when alignment is present, not cosmetic template punctuation.


<a id="commit-082"></a>
## 082. fix(visitor): handle missing functions {#commit-082}

- Commit: [28cfe0e0e81c97bbf1f28328927718d697ff5dc5](https://github.com/EndstoneMC/dwarf2cpp/commit/28cfe0e0e81c97bbf1f28328927718d697ff5dc5)
- Date: 2026-01-17T15:36:44Z; parent(s): eb784a26eaf49251ae3483adc5afa3d6d37ff12f
- Exact reading: diff parent1 lines1–17; message parent1 lines1–1
- Attribution: GitHub-linked wu-vincent author, not exclusive authorship of copied dependencies or merged work.

Permits subprogram without direct declaration file/line when specification exists, then separately requires inherited short_name. This retains definition metadata useful for declaration synchronization rather than skipping before following identity link.


<a id="commit-083"></a>
## 083. docs: add CLAUDE.md {#commit-083}

- Commit: [3dc43f9f0a0d925cf366c140cc1e8c9d9d278ce0](https://github.com/EndstoneMC/dwarf2cpp/commit/3dc43f9f0a0d925cf366c140cc1e8c9d9d278ce0)
- Date: 2026-01-17T15:36:52Z; parent(s): 28cfe0e0e81c97bbf1f28328927718d697ff5dc5
- Exact reading: diff parent1 lines1–64; message parent1 lines1–1
- Attribution: GitHub-linked wu-vincent author, not exclusive authorship of copied dependencies or merged work.

Adds repository agent guide summarizing pipeline, module responsibilities, build/lint/format commands and versions. Read as historical project documentation, never executed or adopted as instructions. Useful agent navigation artifact; by later backend/LLVM/nanobind changes these version-specific details become stale unless updated.


<a id="commit-084"></a>
## 084. fix(visitor): skip lambda function definitions {#commit-084}

- Commit: [758043f040882fbe944b15ac12f2c10a7ab07b87](https://github.com/EndstoneMC/dwarf2cpp/commit/758043f040882fbe944b15ac12f2c10a7ab07b87)
- Date: 2026-01-17T16:09:09Z; parent(s): 3dc43f9f0a0d925cf366c140cc1e8c9d9d278ce0
- Exact reading: diff parent1 lines1–16; message parent1 lines1–1
- Attribution: GitHub-linked wu-vincent author, not exclusive authorship of copied dependencies or merged work.

Skips out-of-line lambda function definitions identified by printed-name prefix ending class ::operator(). Output suppression is string-pattern heuristic, not complete lambda classification; no test proves accepted/rejected cases.


<a id="commit-085"></a>
## 085. fix(visitor): skip hidden objects during visitation and model generation {#commit-085}

- Commit: [d0294588c96612d00c600ad6790bd56eec60e496](https://github.com/EndstoneMC/dwarf2cpp/commit/d0294588c96612d00c600ad6790bd56eec60e496)
- Date: 2026-01-17T16:34:25Z; parent(s): 758043f040882fbe944b15ac12f2c10a7ab07b87
- Exact reading: diff parent1 lines1–75; message parent1 lines1–1
- Attribution: GitHub-linked wu-vincent author, not exclusive authorship of copied dependencies or merged work.

Renames declared Object.is_implicit field to is_hidden and skips hidden top-level/namespace objects during collection; marks missing-direct-location specification-linked functions hidden while retaining metadata for name propagation. Final context shows is_implicit remains dynamically assigned to anonymous inline types and used in Jinja filters. These now coexist as distinct mechanisms: hidden metadata-bearing functions versus inline-owned type declarations. No declared is_implicit default remains; permissive template lookup is relied upon. This is a consistency/typing concern, not a proven functional regression.


<a id="commit-086"></a>
## 086. refactor(visitor): remove `_param_names` and streamline parameter name synchronization {#commit-086}

- Commit: [9486e0d8ade39480822d38762b32f9dba9530f30](https://github.com/EndstoneMC/dwarf2cpp/commit/9486e0d8ade39480822d38762b32f9dba9530f30)
- Date: 2026-01-17T17:31:04Z; parent(s): d0294588c96612d00c600ad6790bd56eec60e496
- Exact reading: diff parent1 lines1–59; message parent1 lines1–1
- Attribution: GitHub-linked wu-vincent author, not exclusive authorship of copied dependencies or merged work.

Removes parallel _param_names cache; after traversal groups _functions once, collects first available names with arity assertion, then fills missing names. Reduces duplicated incremental state and preserves definitions held only for synchronization. No merge-before-sync reorder, relevant to112 preservation claim.


<a id="commit-087"></a>
## 087. fix(visitor): support `DW_TAG_variable` for static members in classes/structs {#commit-087}

- Commit: [7f72fe4fe38d4ceb162bb5be5445b95e93090260](https://github.com/EndstoneMC/dwarf2cpp/commit/7f72fe4fe38d4ceb162bb5be5445b95e93090260)
- Date: 2026-01-30T15:16:22Z; parent(s): 9486e0d8ade39480822d38762b32f9dba9530f30
- Exact reading: diff parent1 lines1–34; message parent1 lines1–1
- Attribution: GitHub-linked wu-vincent author, not exclusive authorship of copied dependencies or merged work.

Supports compilers representing class static data as DW_TAG_variable, adds it to member traversal and marks it static, accepts member or variable specification references. Broadens a specific encoding pair without relaxing unknown-attribute checks generally.


<a id="commit-088"></a>
## 088. Fix org references, add release workflow, CHANGELOG, dependabot {#commit-088}

- Commit: [134bfe40bda1da714197a8bb66ec8799b58c0669](https://github.com/EndstoneMC/dwarf2cpp/commit/134bfe40bda1da714197a8bb66ec8799b58c0669)
- Date: 2026-03-23T17:51:57Z; parent(s): 7f72fe4fe38d4ceb162bb5be5445b95e93090260
- Exact reading: diff parent1 lines1–203; message parent1 lines1–8
- Attribution: GitHub-linked wu-vincent author, not exclusive authorship of copied dependencies or merged work.

Adds manual release pipeline with version input, X.Y.Z validation and duplicate-tag rejection, nonempty Unreleased extraction, dry-run gates, version/changelog mutation, commit/tag/push, GitHub release and three-platform wheel attachment. Also updates organization URLs and checkout, adds weekly action-update configuration. No workflow execution inspected. Initial changelog notes reside under a preexisting 0.1.0 heading, making the new nonempty-Unreleased gate fail until91 repairs it; intermediate release design is not final.

The complete message source linked above records any explicit diagnosis. Behavioral explanation is static analysis; no successful execution is inferred.


<a id="commit-089"></a>
## 089. Update README: fix warning syntax, point wheels to Releases, add Releasing section {#commit-089}

- Commit: [8bf47bd0c99534c6541ec0c01dd1b4b8ae2207b1](https://github.com/EndstoneMC/dwarf2cpp/commit/8bf47bd0c99534c6541ec0c01dd1b4b8ae2207b1)
- Date: 2026-03-23T17:54:30Z; parent(s): 134bfe40bda1da714197a8bb66ec8799b58c0669
- Exact reading: diff parent1 lines1–61; message parent1 lines1–1
- Attribution: GitHub-linked wu-vincent author, not exclusive authorship of copied dependencies or merged work.

Repairs README warning syntax, points wheel users at Releases instead of Actions, and documents manual Release workflow and dry run. These instructions are valid for this historical design but become stale after109 deletes that workflow.


<a id="commit-090"></a>
## 090. ci: derive release version from pyproject.toml, publish to PyPI {#commit-090}

- Commit: [9721460bd46d5881252eaa75a4974701cbb92b74](https://github.com/EndstoneMC/dwarf2cpp/commit/9721460bd46d5881252eaa75a4974701cbb92b74)
- Date: 2026-05-16T15:56:12Z; parent(s): 5afd37f13e114ef764ed876ffdc2cd3eb36d2fb9
- Exact reading: diff parent1 lines1–246; message parent1 lines1–7
- Attribution: GitHub-linked wu-vincent author, not exclusive authorship of copied dependencies or merged work.

Makes pyproject.toml the release-version source rather than separate workflow input; adds sdist and OIDC PyPI publish gated on prerequisite distribution jobs, scopes branch pushes/PRs to main, recommends uvx/pip. Commit message claims one-time publisher setup documentation, but actual README delta contains no such setup instructions. A configuration declaration is not proof that PyPI trust was configured or publication succeeded.

The complete message source linked above records any explicit diagnosis. Behavioral explanation is static analysis; no successful execution is inferred.


<a id="commit-091"></a>
## 091. docs(changelog): move 0.1.0 notes under [Unreleased] {#commit-091}

- Commit: [ef9c69994f9bfd49a4b98d22b015a0f14331a180](https://github.com/EndstoneMC/dwarf2cpp/commit/ef9c69994f9bfd49a4b98d22b015a0f14331a180)
- Date: 2026-05-16T15:59:29Z; parent(s): 9721460bd46d5881252eaa75a4974701cbb92b74
- Exact reading: diff parent1 lines1–13; message parent1 lines1–5
- Attribution: GitHub-linked wu-vincent author, not exclusive authorship of copied dependencies or merged work.

Moves preexisting 0.1.0 changelog notes into Unreleased, allowing the release workflow to create a single dated version heading. Explicit message explains duplicate-section avoidance. No runtime behavior or independent preference inferred.

The complete message source linked above records any explicit diagnosis. Behavioral explanation is static analysis; no successful execution is inferred.


<a id="commit-092"></a>
## 092. fix(visitor): ignore DW_AT_decl_file/line in visit_namespace (#14) {#commit-092}

- Commit: [f96cfc99d1a0dae6ddd904d1b99752613adfaff3](https://github.com/EndstoneMC/dwarf2cpp/commit/f96cfc99d1a0dae6ddd904d1b99752613adfaff3)
- Date: 2026-05-16T16:04:36Z; parent(s): ef9c69994f9bfd49a4b98d22b015a0f14331a180
- Exact reading: diff parent1 lines1–14; message parent1 lines1–6
- Attribution: GitHub-linked wu-vincent author, not exclusive authorship of copied dependencies or merged work.

Adds exact namespace allowlist for DW_AT_decl_file and DW_AT_decl_line before exhaustive attribute matching. Full three-line patch verified byte-identical to PR14 head5f6a974 and target squashf96cfc9 with same baseef9c699. PR rationale: namespace reopening makes one declaration location unnecessary while members carry locations. Reporter mrxenginner issue13 shows Windows Python3.14 traceback; PR unchecked test plan supplies no retest outcome. Other unknown attributes still raise.

The complete message source linked above records any explicit diagnosis. Behavioral explanation is static analysis; no successful execution is inferred.
