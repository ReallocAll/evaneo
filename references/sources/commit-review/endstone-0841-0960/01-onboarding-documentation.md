<!-- retrieval: {"source_ids":["public:commit:03f8279e7900eb41050e455cb6a3b7f689c10d9b","public:commit:0561089b8c9dee7411871560531d1dbe656e54e8","public:commit:0bf4239cb87387a7ad0d556a9715483cbb68ae9c","public:commit:0f7971a24174a5c50bd42791d321173daf6195ff","public:commit:1147286bbbc27a1d25584d8e4e516e54e6b73ff2","public:commit:2b7b6b28398d437d77fb34688b6d728da433d415","public:commit:3da0bb49a0226b1f11b24ed2b3d299b3a1506b6e","public:commit:44fcaa6d1ea333dcc00e77d21abeca0e30f47bf1","public:commit:4a5ff0f3f4e67e88deb719df9fa6b938270b9780","public:commit:5948c0b69971bf453b6b8a99de9e14d2f9e70506","public:commit:6a51d67eb4a6f182fb25360f575742f516ebb3eb","public:commit:8347c2204db190954865edb064fe54f9ebb320b8","public:commit:8c705f14daa8603ebddfe5ab8aceb4ac557a9621","public:commit:95deab5285df0b51982bffee06d43646f9198b01","public:commit:9a6c14a207ec32b6846ed404c794860bcc6a44f9","public:commit:a3933828f320dec25af257253983b760cad364fc","public:commit:a4e3aebbe0f85984c903266f5877b6ddf6d46ecd","public:commit:aa2d3fb1b0a35fc8c4c672da7e8b03cabf2082d1","public:commit:af33693996b50b2256a15596e3ac701daf21e0b9","public:commit:bc2bba5f2106aa769f087a93ac62371734f89539","public:commit:d96b05deed9bf0b1d73cfafe09d5f1c4e2cb368f","public:commit:e774552e92435267471bca720b588f07317ad7e8","public:commit:ed2522d24e917f3bb9b7d3c5f9dd9da576e1be30"],"source_type":"public","date":"2024-05-01..2024-05-10","topics":["ffi","testing","build","api","documentation","review","selection"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
# Onboarding becomes an end-to-end path, with intermediate corrections {#onboarding-becomes-an-end-to-end-path-with-intermediate-corrections}

## What this family establishes {#what-this-family-establishes}

The meaningful documentation work is the May 3 sequence from project creation through packaging, registration, installation and a visible lifecycle result ([861](#commit-861)–[871](#commit-871)). It supplies two genuinely different integration paths. Python needs the correct environment, distribution/import naming and entry-point metadata. C++ needs a shared library, compatible compiler/runtime choices, the public headers target and plugin registration macro. The tutorial does not merely describe the Plugin class: it connects that class to how a server can discover and load it.

The final tutorial was read in full at ordinal 960. Python's project name uses a dash-separated endstone- prefix, its import package uses underscores, and its entry-point name omits the prefix. The environment is explicitly the one where Endstone is installed. C++ uses FetchContent against main while explicitly warning that a release tag may be preferable; ABI compatibility flags are explained as necessary for the native host. This retains the tension already seen in the previous unit's dependency-consumption work: a copyable development example is available, but the text itself warns about the moving revision. It is not evidence that unpinned production builds are preferred.

## Causal evolution and outcome limits {#causal-evolution-and-outcome-limits}

The first Python completion claim in863 still contains an import typo. The C++ completion in865 still leaves semicolon/header inconsistencies.866 corrects these while completing installation and restart instructions. A reader should retrieve the corrected end state together with the revision chain, rather than assume every commit titled 'finish' was an independently buildable tutorial. The inspected screenshots show the intended IDE structure, a Windows DLL build, editable installation and server plugin load/enable logs. Those are published illustrations. They are not test runs performed here, nor evidence covering every platform/version listed in prerequisites.

The editable-install guidance makes code changes visible to the installed package without rebuilding a wheel, but the instructions also restart the server. It would overreach to infer module hot-reload support. Later wheel-plugin support in941 changes installation options, and942 explicitly repairs editable discovery. Thus onboarding and loader implementation must be considered together rather than freezing the May 3 path as a timeless guarantee.

The surrounding CSS, tab icon, navigation and social-link changes are individually accounted for below and are not elevated into architectural principles. Documentation generators become CI-conditional in860; generated Python inheritance display changes again in879. These are revisable local presentation choices. The address documentation commit870 also changes a default constructor, so title-based filtering would have missed a small but real initialization semantic change.

## Attribution, applicability and checks {#attribution-applicability-and-checks}

Git records Vincent as author and committer throughout this sequence; no PR discussion or reviewer objections were examined here. IDEs and build tools retain their own authorship; screenshots do not make their design Vincent's work. No user-experience measurement is reported. The history is useful for first-plugin initialization, environment mismatch, public API navigation, distinguishing install from reload, and checking examples against implementation. The review reports inspecting 13 distinct image assets, including reuse of the renamed server screenshot, but does not include the binary comparison needed to verify exact-byte reuse. Adjacent TODO tutorials remain incomplete, and no claim of complete documentation coverage follows.

## Per-commit source dispositions {#per-commit-source-dispositions}

<a id="commit-841"></a>
### 841 · docs: fix search bar background colour {#commit-841}

[Full commit 0561089b8c9dee7411871560531d1dbe656e54e8](https://github.com/EndstoneMC/endstone/commit/0561089b8c9dee7411871560531d1dbe656e54e8) · 2024-05-01T22:09:04Z · parent `2e789bef8044aba3f823aefdd15765208b106557` · presentation.

Changes checked-search background to the surface-container color and removes its box shadow. This is a verified CSS-only visual correction, without runtime or independent architectural evidence.

Changed paths: `docs/stylesheets/extra.css`. Whole changed content was read; exact move/header reuse and binary handling are recorded in the coverage artifacts.

<a id="commit-842"></a>
### 842 · docs: update style {#commit-842}

[Full commit 1147286bbbc27a1d25584d8e4e516e54e6b73ff2](https://github.com/EndstoneMC/endstone/commit/1147286bbbc27a1d25584d8e4e516e54e6b73ff2) · 2024-05-02T12:14:38Z · parent `0561089b8c9dee7411871560531d1dbe656e54e8` · presentation.

Makes homepage/reference buttons bold, rounds cards, adjusts buttons and active-tab underline, and splits the Python reference index into general/module navigation. Actual stylesheet and Markdown changes were read; this is discoverability/presentation work, not a runtime feature or measured usability result.

Changed paths: `docs/index.md`, `docs/reference/index.md`, `docs/reference/python/general.md`, `docs/reference/python/index.md`, `docs/stylesheets/extra.css`, `mkdocs.yml`. Whole changed content was read; exact move/header reuse and binary handling are recorded in the coverage artifacts.

<a id="commit-843"></a>
### 843 · docs: update accent colours {#commit-843}

[Full commit 4a5ff0f3f4e67e88deb719df9fa6b938270b9780](https://github.com/EndstoneMC/endstone/commit/4a5ff0f3f4e67e88deb719df9fa6b938270b9780) · 2024-05-02T12:31:08Z · parent `1147286bbbc27a1d25584d8e4e516e54e6b73ff2` · presentation.

Replaces tertiary accent usage with primary-container/on-primary-container variables in light and dark themes. The change is a concrete semantic-color choice for this website; it does not support a general software-engineering preference.

Changed paths: `docs/stylesheets/extra.css`. Whole changed content was read; exact move/header reuse and binary handling are recorded in the coverage artifacts.

<a id="commit-847"></a>
### 847 · docs: update python api references {#commit-847}

[Full commit e774552e92435267471bca720b588f07317ad7e8](https://github.com/EndstoneMC/endstone/commit/e774552e92435267471bca720b588f07317ad7e8) · 2024-05-02T14:20:38Z · parent `283557607c4064a3e1006ec59cb0109693181054` · documentation.

Reorganizes Python reference entries around server, player and miscellaneous APIs, removes the old C++/Python index/general pages, and makes the C++ link go directly to annotated types. This follows844's module split. It improves direct navigation but does not itself verify the documented APIs.

Changed paths: `docs/reference/cpp/index.md`, `docs/reference/index.md`, `docs/reference/python/general.md`, `docs/reference/python/index.md`, `docs/reference/python/misc.md`, `docs/reference/python/player.md`, `docs/reference/python/server.md`, `mkdocs.yml`. Whole changed content was read; exact move/header reuse and binary handling are recorded in the coverage artifacts.

<a id="commit-853"></a>
### 853 · docs: update start-your-server.md {#commit-853}

[Full commit ed2522d24e917f3bb9b7d3c5f9dd9da576e1be30](https://github.com/EndstoneMC/endstone/commit/ed2522d24e917f3bb9b7d3c5f9dd9da576e1be30) · 2024-05-02T16:27:19Z · parent `ebdb9e4e7b85355443019d9c937ad83c697ef7a4` · documentation_with_binary.

Corrects the 0.4.2 Minecraft compatibility text from1.20.82 to1.20.81 and replaces pasted startup logs with an inspected screenshot and confirmation tip. The screenshot shows Linux download/hash verification and Endstone0.4.2 with Minecraft1.20.81.01 starting; it is a recorded illustration, not a test executed during this review. This resolves the earlier release-text inconsistency rather than proving all compatibility claims.

Changed paths: `CHANGELOG.md`, `docs/getting-started/start-your-server.md`, `docs/getting-started/start-your-server.png`. Whole changed content was read; exact move/header reuse and binary handling are recorded in the coverage artifacts.

<a id="commit-856"></a>
### 856 · docs: add reference for module `endstone.util` {#commit-856}

[Full commit 9a6c14a207ec32b6846ed404c794860bcc6a44f9](https://github.com/EndstoneMC/endstone/commit/9a6c14a207ec32b6846ed404c794860bcc6a44f9) · 2024-05-02T22:49:57Z · parent `21fb1662a06170ab7b81f63bed77a2372b450e12` · documentation.

Adds the endstone.util reference page and navigation for the newly introduced utility namespace. This is accompanying API discoverability, with no separate runtime change.

Changed paths: `docs/reference/python/misc.md`. Whole changed content was read; exact move/header reuse and binary handling are recorded in the coverage artifacts.

<a id="commit-859"></a>
### 859 · docs: add Discord invite link to README.md {#commit-859}

[Full commit bc2bba5f2106aa769f087a93ac62371734f89539](https://github.com/EndstoneMC/endstone/commit/bc2bba5f2106aa769f087a93ac62371734f89539) · 2024-05-03T11:42:00Z · parent `38456a48ee9b2f8fcbec0788cecb6a9fa0e1a281` · documentation.

Adds a public Discord invitation badge/link to README. This is community access metadata, without evidence about API design, collaboration quality or an individual participant's decisions.

Changed paths: `README.md`. Whole changed content was read; exact move/header reuse and binary handling are recorded in the coverage artifacts.

<a id="commit-860"></a>
### 860 · docs: enable plugins if in CI {#commit-860}

[Full commit 0bf4239cb87387a7ad0d556a9715483cbb68ae9c](https://github.com/EndstoneMC/endstone/commit/0bf4239cb87387a7ad0d556a9715483cbb68ae9c) · 2024-05-03T15:32:24Z · parent `bc2bba5f2106aa769f087a93ac62371734f89539` · build_documentation.

Makes mkdocstrings, mkdoxy and Git-derived author/date plugins conditional on the CI environment flag, defaulting off locally. The configuration differentiates local preview from CI generation; reduced local dependency/work is a plausible effect, not an explicitly measured performance result. Local previews therefore need not include the same generated API content as CI.

Changed paths: `mkdocs.yml`. Whole changed content was read; exact move/header reuse and binary handling are recorded in the coverage artifacts.

<a id="commit-861"></a>
### 861 · docs: add "Create a new project" section for Python {#commit-861}

[Full commit 03f8279e7900eb41050e455cb6a3b7f689c10d9b](https://github.com/EndstoneMC/endstone/commit/03f8279e7900eb41050e455cb6a3b7f689c10d9b) · 2024-05-03T15:32:59Z · parent `0bf4239cb87387a7ad0d556a9715483cbb68ae9c` · onboarding.

Adds the Python new-project tutorial with PyCharm, Python>=3.9, the endstone- project-name convention and reuse of the server's environment. The same-environment/virtual-environment advice addresses discovery and installation location directly. A TOC partial now respects page metadata and child depth. All four IDE screenshots were inspected; they illustrate PyCharm2023.3.3 and an existing Python3.11 environment, not a newly executed installation.

Changed paths: `docs/overrides/partials/toc-item.html`, `docs/tutorials/create-your-first-plugin.md`, `docs/tutorials/screenshots/pycharm-create-project.png`, `docs/tutorials/screenshots/pycharm-create-pyproject-toml.png`, `docs/tutorials/screenshots/pycharm-welcome.png`, `docs/tutorials/screenshots/pycharm-workspace.png`. Whole changed content was read; exact move/header reuse and binary handling are recorded in the coverage artifacts.

<a id="commit-862"></a>
### 862 · docs: add "Create a new project" section for C++ {#commit-862}

[Full commit 0f7971a24174a5c50bd42791d321173daf6195ff](https://github.com/EndstoneMC/endstone/commit/0f7971a24174a5c50bd42791d321173daf6195ff) · 2024-05-03T16:03:30Z · parent `03f8279e7900eb41050e455cb6a3b7f689c10d9b` · onboarding.

Adds the C++ project setup path through CLion: CMake>=3.15, supported MSVC/Clang toolchains, C++17 shared library, and removal of the generated hello-library files. Three inspected screenshots show the initial shared-library project. These are period-specific requirements in a historical tutorial, not present-day tool recommendations or proof that every listed minimum was tested.

Changed paths: `docs/getting-started/installation.md`, `docs/getting-started/start-your-server.md`, `docs/tutorials/create-your-first-plugin.md`, `docs/tutorials/screenshots/clion-create-project.png`, `docs/tutorials/screenshots/clion-welcome.png`, `docs/tutorials/screenshots/clion-workspace.png`. Whole changed content was read; exact move/header reuse and binary handling are recorded in the coverage artifacts.

<a id="commit-863"></a>
### 863 · docs: finish the "Create your first plugin" tutorial for Python {#commit-863}

[Full commit 2b7b6b28398d437d77fb34688b6d728da433d415](https://github.com/EndstoneMC/endstone/commit/2b7b6b28398d437d77fb34688b6d728da433d415) · 2024-05-03T16:38:49Z · parent `0f7971a24174a5c50bd42791d321173daf6195ff` · onboarding_then_corrected.

Extends Python setup into a src-layout endstone_my_plugin package, Plugin subclass/lifecycle metadata and the endstone entry-point group. The distinction between distribution dash naming and import underscore naming is useful integration detail. It also introduces an enstone import typo and inconsistent example class naming;865/866 repair these. The package-tree screenshot confirms intended structure, but neither screenshot nor commit title establishes that this intermediate text runs.

Changed paths: `docs/tutorials/create-your-first-plugin.md`, `docs/tutorials/screenshots/pycharm-create-package.png`. Whole changed content was read; exact move/header reuse and binary handling are recorded in the coverage artifacts.

<a id="commit-864"></a>
### 864 · docs: update tab icons {#commit-864}

[Full commit a4e3aebbe0f85984c903266f5877b6ddf6d46ecd](https://github.com/EndstoneMC/endstone/commit/a4e3aebbe0f85984c903266f5877b6ddf6d46ecd) · 2024-05-03T16:40:32Z · parent `2b7b6b28398d437d77fb34688b6d728da433d415` · presentation.

Changes language-tab icons only. Verified actual Markdown changes support a brief visual disposition; no separate implementation rationale is inferred.

Changed paths: `docs/tutorials/create-your-first-plugin.md`. Whole changed content was read; exact move/header reuse and binary handling are recorded in the coverage artifacts.

<a id="commit-865"></a>
### 865 · docs: finish the "Create your first plugin" tutorial for C++ {#commit-865}

[Full commit a3933828f320dec25af257253983b760cad364fc](https://github.com/EndstoneMC/endstone/commit/a3933828f320dec25af257253983b760cad364fc) · 2024-05-03T21:21:52Z · parent `a4e3aebbe0f85984c903266f5877b6ddf6d46ecd` · onboarding_then_corrected.

Completes the C++ plugin class/source, headers target linkage and registration macro, while aligning Python example naming. The intermediate C++ snippets still omit class semicolons and refer to an old header name; the Python import typo also remains until866. This is an incremental tutorial construction chain, not evidence that every intermediate example was buildable.

Changed paths: `docs/tutorials/create-your-first-plugin.md`. Whole changed content was read; exact move/header reuse and binary handling are recorded in the coverage artifacts.

<a id="commit-866"></a>
### 866 · docs: finish "Install your plugin" tutorial {#commit-866}

[Full commit af33693996b50b2256a15596e3ac701daf21e0b9](https://github.com/EndstoneMC/endstone/commit/af33693996b50b2256a15596e3ac701daf21e0b9) · 2024-05-03T22:01:38Z · parent `a3933828f320dec25af257253983b760cad364fc` · onboarding.

Finishes installation instructions: editable Python installation into the selected environment and copying the C++ DLL into the server plugins directory, followed by restart and log confirmation. Repairs the Python import and C++ semicolons/header mismatch from863/865. Three inspected screenshots show CMake configuration, successful Windows DLL build and plugin load/enable logging. These are source-reported outcomes. Editable installation exposes source changes to future imports; the text's restart step must not be generalized into automatic live module reload.

Changed paths: `docs/tutorials/create-your-first-plugin.md`, `docs/tutorials/install-your-plugin.md`, `docs/tutorials/screenshots/clion-build-plugin.png`, `docs/tutorials/screenshots/clion-update-cmakelists.png`, `docs/tutorials/screenshots/install-plugin.png`. Whole changed content was read; exact move/header reuse and binary handling are recorded in the coverage artifacts.

<a id="commit-867"></a>
### 867 · docs: update tab icons {#commit-867}

[Full commit 5948c0b69971bf453b6b8a99de9e14d2f9e70506](https://github.com/EndstoneMC/endstone/commit/5948c0b69971bf453b6b8a99de9e14d2f9e70506) · 2024-05-03T22:06:36Z · parent `af33693996b50b2256a15596e3ac701daf21e0b9` · presentation.

Updates language-tab icons on five tutorial pages and removes explicit TOC depth settings. Other tutorial sections still contain TODO placeholders; completing the first-plugin path does not complete all tutorial coverage.

Changed paths: `docs/tutorials/install-your-plugin.md`, `docs/tutorials/publish-your-plugin.md`, `docs/tutorials/register-commands.md`, `docs/tutorials/register-event-listeners.md`, `docs/tutorials/schedule-tasks.md`. Whole changed content was read; exact move/header reuse and binary handling are recorded in the coverage artifacts.

<a id="commit-868"></a>
### 868 · docs: update changelog, add to pyproject.toml {#commit-868}

[Full commit 8c705f14daa8603ebddfe5ab8aceb4ac557a9621](https://github.com/EndstoneMC/endstone/commit/8c705f14daa8603ebddfe5ab8aceb4ac557a9621) · 2024-05-03T22:10:26Z · parent `5948c0b69971bf453b6b8a99de9e14d2f9e70506` · documentation.

Adds changelog page metadata and an active changelog URL in pyproject.toml. This improves release navigation; no release behavior or version is changed by this commit.

Changed paths: `docs/changelog.md`, `pyproject.toml`. Whole changed content was read; exact move/header reuse and binary handling are recorded in the coverage artifacts.

<a id="commit-869"></a>
### 869 · docs: add missing documentation for endstone::EventHandler {#commit-869}

[Full commit 6a51d67eb4a6f182fb25360f575742f516ebb3eb](https://github.com/EndstoneMC/endstone/commit/6a51d67eb4a6f182fb25360f575742f516ebb3eb) · 2024-05-03T22:37:00Z · parent `8c705f14daa8603ebddfe5ab8aceb4ac557a9621` · documentation.

Adds EventHandler documentation and reorders getters without changing their implementations. The isIgnoreCancelled prose describes accepting cancelled events while the Boolean means ignoring them, so this text is not a reliable behavioral specification by itself. The implementation and surrounding dispatcher remain the authority.

Changed paths: `include/endstone/event/event_handler.h`. Whole changed content was read; exact move/header reuse and binary handling are recorded in the coverage artifacts.

<a id="commit-870"></a>
### 870 · docs: add missing documentation for endstone::SocketAddress {#commit-870}

[Full commit 8347c2204db190954865edb064fe54f9ebb320b8](https://github.com/EndstoneMC/endstone/commit/8347c2204db190954865edb064fe54f9ebb320b8) · 2024-05-03T22:38:53Z · parent `6a51d67eb4a6f182fb25360f575742f516ebb3eb` · documentation_with_semantics.

Documents SocketAddress and changes its user-provided empty default constructor to '= default'. This is not strictly comment-only: value-initializing the now non-user-provided default constructor can zero-initialize the uint32 port, whereas ordinary default initialization still does not guarantee it. The API still performs no address validation. The semantic delta is narrow and not an explicit initialization-policy statement.

Changed paths: `include/endstone/util/socket_address.h`. Whole changed content was read; exact move/header reuse and binary handling are recorded in the coverage artifacts.

<a id="commit-871"></a>
### 871 · docs: update install-your-plugin.md {#commit-871}

[Full commit aa2d3fb1b0a35fc8c4c672da7e8b03cabf2082d1](https://github.com/EndstoneMC/endstone/commit/aa2d3fb1b0a35fc8c4c672da7e8b03cabf2082d1) · 2024-05-03T22:42:39Z · parent `8347c2204db190954865edb064fe54f9ebb320b8` · documentation_with_binary.

Replaces editable-install text output with an inspected PyCharm pip-install screenshot and renames the prior server/plugin startup screenshot without changing its bytes. The exact binary relocation is verified in rename coverage; it is not counted as a second independent successful run. The new screenshot reports an editable package installation, not hot reload.

Changed paths: `docs/tutorials/install-your-plugin.md`, `docs/tutorials/screenshots/pycharm-install-package.png`, `docs/tutorials/screenshots/start-server-with-plugin.png`. Whole changed content was read; exact move/header reuse and binary handling are recorded in the coverage artifacts.

<a id="commit-879"></a>
### 879 · docs: update mkdocstrings options {#commit-879}

[Full commit 95deab5285df0b51982bffee06d43646f9198b01](https://github.com/EndstoneMC/endstone/commit/95deab5285df0b51982bffee06d43646f9198b01) · 2024-05-04T15:52:45Z · parent `427ccda13c783bfe0f97a2254b8f93fc80e6dc0b` · documentation_configuration.

Turns on base-class display and turns off inherited-member expansion in generated Python documentation, reversing the earlier inherited-member display choice from811. The local decision favors showing relationships without repeating all inherited members; no user study or durable general documentation preference is established.

Changed paths: `mkdocs.yml`. Whole changed content was read; exact move/header reuse and binary handling are recorded in the coverage artifacts.

<a id="commit-902"></a>
### 902 · docs: add social link for discord {#commit-902}

[Full commit d96b05deed9bf0b1d73cfafe09d5f1c4e2cb368f](https://github.com/EndstoneMC/endstone/commit/d96b05deed9bf0b1d73cfafe09d5f1c4e2cb368f) · 2024-05-07T14:07:22Z · parent `1e1611fb56dd9eaf6ba2008e534838a5c9c8a1ff` · documentation.

Adds Discord to website social navigation. Verified link-only metadata does not establish an implementation or collaboration principle.

Changed paths: `mkdocs.yml`. Whole changed content was read; exact move/header reuse and binary handling are recorded in the coverage artifacts.

<a id="commit-912"></a>
### 912 · docs: update README.md {#commit-912}

[Full commit 3da0bb49a0226b1f11b24ed2b3d299b3a1506b6e](https://github.com/EndstoneMC/endstone/commit/3da0bb49a0226b1f11b24ed2b3d299b3a1506b6e) · 2024-05-09T15:34:09Z · parent `15f67c00450c7b0e6e0c3f984f1bbdfd52cec47e` · build_documentation.

Simplifies source-build instructions to clone plus pip installation, retaining the toolchain requirement table in a later section. This documents907–911's backend integration and lowers the number of manual commands shown to consumers. It does not mean native compilers/dependencies disappeared or that all supported systems were exercised.

Changed paths: `README.md`. Whole changed content was read; exact move/header reuse and binary handling are recorded in the coverage artifacts.

<a id="commit-919"></a>
### 919 · docs: update discord invite link {#commit-919}

[Full commit 44fcaa6d1ea333dcc00e77d21abeca0e30f47bf1](https://github.com/EndstoneMC/endstone/commit/44fcaa6d1ea333dcc00e77d21abeca0e30f47bf1) · 2024-05-10T14:58:18Z · parent `12bc154566f005b221fa579b1e33f16685a18c25` · documentation.

Updates the Discord invitation in README and website configuration. This is a verified link replacement with no independent engineering lesson.

Changed paths: `README.md`, `mkdocs.yml`. Whole changed content was read; exact move/header reuse and binary handling are recorded in the coverage artifacts.
