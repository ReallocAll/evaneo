<!-- retrieval: {"source_ids":["public:commit:04c9664d34546b24af57592f6a59c30ce31d829c","public:commit:072b5de3f3d856bfb622e113371f28e8970f722e","public:commit:0784ab169f4db741499276469dbf43b0953f33a9","public:commit:083860379332042d7a0a0348189a80e3dd95b01a","public:commit:1bf6b79d5a550dd83727f66f9d9772a88ae1d821","public:commit:1f7d6595e28fe94509b249a76d813c97425bbda4","public:commit:21340a23b221c6b572c6ecab09f3ee75f0fc817b","public:commit:29fefd1d7f161ad2c76c44d42508d2ae6cb13bca","public:commit:2ca13607ea24665dc5d487f264a032e7b7b5df56","public:commit:2da6ac5030f44814e6b0fb7cea61f745e2c33f4e","public:commit:2ff4a7a91f732876381130efb8e4238806af4b62","public:commit:30068e7ba43a723731b2e1a26c0484295fe77b7e","public:commit:375a0f2dbe8cd91439538b73534bd8216499db9b","public:commit:39f0b621cd71d6251f1e95d0d20ba4ce28f3d2df","public:commit:4649a455c8b6ba5411eaca1c304e08e8ec5b0b1d","public:commit:4f3a227fa894c5c592313986189c368fb5e6d982","public:commit:4f5d2a031f22c3f5b8f153fe71fae839bfc2112d","public:commit:52c0ec0531217c7f4c18cf4e32869c1686cdbdf7","public:commit:53d759779aaba62140b2aabfebd4463b13090e2c","public:commit:6c760fc581edded62e25d8795d06aced09db5952","public:commit:72ec5594f18bc0473f6d3ed69260c9e9a636b61c","public:commit:73eb4cb9dfacbd2d18717021dc1e178a5b691690","public:commit:87eb2d531f107d2f5786436515d63b496fb569d9","public:commit:90fa8ab1139573aef5df6912c96e0f25e85fcbbc","public:commit:93fb7e03201d217f5fc06512e92cc91693ad892a","public:commit:9d01b15a8161de855d93dfd61a90211620ffb2c9","public:commit:c010c4866fa282d1b44afb8a08490a379e9066ea","public:commit:d104b5d330bfe0097d28cdd563c58b7da43d565e","public:commit:d3c818fd798250edb03fdb114f4fe11a2f91de09","public:commit:dd90f4780d3a4720b0158be9c480e9eca9fe444d","public:commit:e33ca422ae9e47d2f9513700db025fd5cf4f22c9","public:commit:e5e3842d07daaaf7f59270f2c2bb5576e8675704","public:commit:e677f38cfe1f4042c54ebe9217cc291e5426b1a6"],"source_type":"public","date":"2024-06-04..2024-06-17","topics":["concurrency","ffi","testing","build","performance","api","diagnosis","documentation","review","selection","refactoring"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
# Documentation, packaging and deployment choices with their reversals {#documentation-packaging-and-deployment-choices-with-their-reversals}

## Documentation tooling follows the public API shape {#documentation-tooling-follows-the-public-api-shape}

The source switches through three dependency configurations: public mkdocstrings[python], a short-lived insider Git requirement with an environment placeholder, then public mkdocstrings-python plus griffe-endstone/custom templates. The decisive implementation in 1096 renders overload signatures/docstrings explicitly, with a single-signature fallback, and uses stub discovery with runtime inspection disabled. This supports the overloaded binding surface without requiring this review to import or execute the extension. The placeholder is not a captured credential. No external access, package installation or docs build was performed.

Inherited-member rendering is false at 1083, true at 1092 and false again at 1161. The last toggle follows explicit event bases, but its reason is not stated. Similarly 1116 briefly changes a CI environment fallback to true and 1117 restores false. These are dated reversals that defeat a timeless preference claim. The large 1119 change is mostly class/docstring punctuation and mirrored stub prose; it was actually paged/read, but does not deserve hundreds of architectural lessons. Issue templates request useful diagnostic fields and alternatives, while title-prefix normalization is only mechanical maintenance.

## Deployment source is not deployment evidence {#deployment-source-is-not-deployment-evidence}

A new docs workflow builds on main pushes, installs Doxygen/Python requirements and force-deploys with contents-write permission. Checkout becomes full-depth. README/CNAME route readers to endstone.dev rather than ReadTheDocs. Later path filtering limits triggers to workflow/docs/include/python trees and omits root mkdocs.yml and src binding sources, a concrete mismatch between some doc-affecting inputs and trigger scope. No claim is made that the workflow failed or succeeded, because runs were not inspected. This research did not publish anything or alter GitHub permissions.

Portable Windows publishing gets the missing tag-push trigger at 1129. That connects to 1028's existing tag-conditioned release step and closes an observable configuration gap. Release metadata proceeds 0.4.7, 0.4.8, then changelog 0.4.8.1, with date/link/header corrections. A release note is useful evidence of intended/reportable behavior, not independent runtime verification. In particular permission and UUID outcomes retain their source-level caveats in the companion dossier.

## Build choices evolve rather than form a single fixed rule {#build-choices-evolve-rather-than-form-a-single-fixed-rule}

The explicit wheel MSVC toolset pin is removed, Conan compiler version temporarily rises to 194, windows-2022 is temporarily removed from a test matrix, then fixed Conan profile files are removed entirely. The later setup uses detected compiler identity plus explicit language/libc++/Ninja settings, and points cc/c++ alternatives to the intended Clang. Wheel/portable runners move to windows-2019. These patches support a practical compatibility adjustment, but no specific root cause or successful matrix outcome is provided. Do not infer a permanent preference for one compiler or runner.

The Windows bootstrap adds a thread-exit query after the remote loading thread finishes. Inspection distinguishes the implemented API-call success check from the intended DLL-load-result check: it branches on result, not the returned exit code value. That narrow distinction is enough; this is not an invitation to execute the bootstrap or extend the task into a security audit. The existing environment/symbol-path/process lifecycle remains visible in full context.

Plugin data directories supply another explicit reversal chain. 1042 tried snake_case, 1058 restored original names, and 1106 lowercases only. Lowercasing FooBar yields foobar rather than foo_bar. C++ and Python loaders change together, but no on-disk migration or rationale is shown. This is useful evidence to retain when interpreting future path decisions, not a recommendation to rename existing user data without a migration plan.

## Collaborator and merge accounting {#collaborator-and-merge-accounting}

Dependabot authors e7d03b28742c6c874ef6ab0c2c5475aa3212b7c8, a two-line v5→v6 update to docker/build-push-action. Its full message/diff is read as context; target-credit remains false. Vincent's 1183 merge is tree-identical to that branch head. 1189 imports the same update into the independently developed translation branch, with exact first-parent patch identity and disjoint tree union. The second-parent translation diff was also read. Linked upstream release notes/action internals and PR review discussion were not read, so no claim about the major action version's internal safety or performance is supported.

## Evidence limits {#evidence-limits}

All repository sources are public Git objects read offline under disabled lazy fetch/protocol access. Mechanical and generated-looking changes were inspected before disposition. Tests were never executed; CI run history, native server correctness, dependency internals and external documentation output remain unverified. These are research deliverables, not changes to the project or a current preference model derived from obsolete material.

## Commit-by-commit dispositions {#commit-by-commit-dispositions}

<a id="commit-1082"></a>
### 1082: chore: update issue templates {#commit-1082}

Source: [2ca13607ea24665dc5d487f264a032e7b7b5df56](https://github.com/EndstoneMC/endstone/commit/2ca13607ea24665dc5d487f264a032e7b7b5df56) · 2024-06-04T06:57:51Z · documentation

Adds bug and feature request Markdown templates. The bug form requests reproduction, expected behavior, screenshots, OS and version; the feature form requests the problem, proposed solution, alternatives and context. This is project intake scaffolding, not evidence that a particular bug was diagnosed or alternatives evaluated.

<a id="commit-1083"></a>
### 1083: docs: update mkdocstrings options {#commit-1083}

Source: [6c760fc581edded62e25d8795d06aced09db5952](https://github.com/EndstoneMC/endstone/commit/6c760fc581edded62e25d8795d06aced09db5952) · 2024-06-04T09:50:55Z · documentation

Reorganizes mkdocstrings member/signature options, excludes private members and initially disables inherited members. Python Plugin and PluginCommand bases become explicitly qualified through endstone_python rather than private aliases. The actual changes mainly affect introspection/documentation naming; no plugin lifecycle policy is changed. Later 1092 and 1161 reverse inherited-member rendering.

<a id="commit-1085"></a>
### 1085: chore: update bug_report.md {#commit-1085}

Source: [1f7d6595e28fe94509b249a76d813c97425bbda4](https://github.com/EndstoneMC/endstone/commit/1f7d6595e28fe94509b249a76d813c97425bbda4) · 2024-06-04T09:55:37Z · mechanical

Changes bug-template title prefix from [BUG] to [bug]. No independent engineering lesson.

<a id="commit-1086"></a>
### 1086: chore: update feature_request.md {#commit-1086}

Source: [2ff4a7a91f732876381130efb8e4238806af4b62](https://github.com/EndstoneMC/endstone/commit/2ff4a7a91f732876381130efb8e4238806af4b62) · 2024-06-04T09:55:58Z · mechanical

Changes feature-template prefix from [FR] to [feature]. No runtime or intake-field change.

<a id="commit-1092"></a>
### 1092: refactor: remove enum member docstring from python stubs {#commit-1092}

Source: [c010c4866fa282d1b44afb8a08490a379e9066ea](https://github.com/EndstoneMC/endstone/commit/c010c4866fa282d1b44afb8a08490a379e9066ea) · 2024-06-04T12:35:15Z · documentation

Disables automatic enum-member docstrings and removes their duplicated Members sections from the stub. Re-enables inherited member rendering after 1083; this is subsequently reversed at 1161. Actual enum values/behavior are unchanged.

<a id="commit-1093"></a>
### 1093: docs: use mkdocstrings-python insider {#commit-1093}

Source: [39f0b621cd71d6251f1e95d0d20ba4ce28f3d2df](https://github.com/EndstoneMC/endstone/commit/39f0b621cd71d6251f1e95d0d20ba4ce28f3d2df) · 2024-06-04T13:15:06Z · build_configuration

Switches docs from public mkdocstrings[python] to an insider Git dependency with a GH_TOKEN environment placeholder. No credential value occurs in the source. This short-lived acquisition choice is replaced at 1096; no token was used or package fetched in this review.

<a id="commit-1094"></a>
### 1094: docs: update mkdocs.yml {#commit-1094}

Source: [0784ab169f4db741499276469dbf43b0953f33a9](https://github.com/EndstoneMC/endstone/commit/0784ab169f4db741499276469dbf43b0953f33a9) · 2024-06-04T15:37:28Z · documentation

Configures external-module loading, stub discovery, disabled runtime inspection, merged initializer docs and summaries. The explicit configuration supports a static/stub-driven documentation route; actual generated output was not run or inspected here.

<a id="commit-1096"></a>
### 1096: docs: render overloaded functions {#commit-1096}

Source: [04c9664d34546b24af57592f6a59c30ce31d829c](https://github.com/EndstoneMC/endstone/commit/04c9664d34546b24af57592f6a59c30ce31d829c) · 2024-06-06T15:23:27Z · substantive

Replaces the insider dependency with public mkdocstrings-python plus griffe-endstone and a custom Jinja function template that iterates overloads with formatted signatures/docstrings, falling back to a single signature. Adds the Griffe extension/custom-template configuration and include-path stripping. This is concrete adaptation to overloaded bindings, not evidence for preferring private dependencies.

<a id="commit-1098"></a>
### 1098: fix(ci): remove toolset version from MSVC setup {#commit-1098}

Source: [e677f38cfe1f4042c54ebe9217cc291e5426b1a6](https://github.com/EndstoneMC/endstone/commit/e677f38cfe1f4042c54ebe9217cc291e5426b1a6) · 2024-06-06T19:09:50Z · build_configuration

Removes the explicit MSVC 14.3 toolset selection from wheel CI. Actual toolchain behavior is delegated to the runner/setup defaults; no successful build is evidenced by this patch.

<a id="commit-1100"></a>
### 1100: fix(ci): temporarily disable windows-2022 runner {#commit-1100}

Source: [90fa8ab1139573aef5df6912c96e0f25e85fcbbc](https://github.com/EndstoneMC/endstone/commit/90fa8ab1139573aef5df6912c96e0f25e85fcbbc) · 2024-06-06T21:46:04Z · build_configuration

Raises the Conan MSVC version from 193 to 194 and temporarily removes windows-2022 from the Windows test matrix, leaving windows-2019. The title explicitly calls the removal temporary; no deeper cause or test result is supplied.

<a id="commit-1106"></a>
### 1106: refactor: use lowercase of plugin name for the data folder {#commit-1106}

Source: [083860379332042d7a0a0348189a80e3dd95b01a](https://github.com/EndstoneMC/endstone/commit/083860379332042d7a0a0348189a80e3dd95b01a) · 2024-06-07T17:50:17Z · substantive

Lowercases plugin data-folder names in both C++ and Python loaders. This is a third observed policy after snake_case at 1042 and its revert at 1058: now only case changes, no underscore insertion. The source supplies no migration or reason for the revised choice; logger/original plugin identity is not changed.

<a id="commit-1116"></a>
### 1116: docs: add module endstone.inventory {#commit-1116}

Source: [dd90f4780d3a4720b0158be9c480e9eca9fe444d](https://github.com/EndstoneMC/endstone/commit/dd90f4780d3a4720b0158be9c480e9eca9fe444d) · 2024-06-08T21:42:41Z · documentation

Adds an inventory reference page/navigation and changes the docs CI-environment fallback from false to true. The fallback toggle is reversed immediately at 1117; inventory documentation remains.

<a id="commit-1117"></a>
### 1117: docs: fix mkdocs.yml {#commit-1117}

Source: [87eb2d531f107d2f5786436515d63b496fb569d9](https://github.com/EndstoneMC/endstone/commit/87eb2d531f107d2f5786436515d63b496fb569d9) · 2024-06-08T21:43:43Z · corrective

Restores the CI default to false in mkdocs.yml while retaining the newly added inventory navigation. The reason for the short-lived true setting is unstated; avoid deriving a stable CI preference from it.

<a id="commit-1119"></a>
### 1119: docs: add docstrings for classes {#commit-1119}

Source: [d104b5d330bfe0097d28cdd563c58b7da43d565e](https://github.com/EndstoneMC/endstone/commit/d104b5d330bfe0097d28cdd563c58b7da43d565e) · 2024-06-08T22:04:18Z · documentation

Full 933-line raw diff read in two pages. Adds/revises class descriptions, punctuation and Python docstrings with corresponding stub text, including replacing stale HumanActor wording with Player. It is mostly repeated API documentation, not hundreds of independent implementation decisions; changed Python class docstring metadata is acknowledged.

<a id="commit-1121"></a>
### 1121: docs: add workflow for documentation deployment {#commit-1121}

Source: [4f5d2a031f22c3f5b8f153fe71fae839bfc2112d](https://github.com/EndstoneMC/endstone/commit/4f5d2a031f22c3f5b8f153fe71fae839bfc2112d) · 2024-06-10T22:23:27Z · deployment

Adds a GitHub docs workflow for main pushes with contents write, checkout, bot identity, Python, Doxygen, cache, docs requirements and mkdocs gh-deploy --force. This is repository deployment configuration; the reviewer did not execute it, publish pages or change permissions.

<a id="commit-1122"></a>
### 1122: fix: update docs.yml to include fetch-depth in checkout step {#commit-1122}

Source: [e33ca422ae9e47d2f9513700db025fd5cf4f22c9](https://github.com/EndstoneMC/endstone/commit/e33ca422ae9e47d2f9513700db025fd5cf4f22c9) · 2024-06-10T22:58:06Z · corrective

Sets checkout fetch-depth to zero for docs deployment. Full history becomes available to the existing docs tooling; a relation to history-sensitive plugins is an inference, not a recorded CI diagnosis.

<a id="commit-1123"></a>
### 1123: docs: update badges in README.md {#commit-1123}

Source: [4649a455c8b6ba5411eaca1c304e08e8ec5b0b1d](https://github.com/EndstoneMC/endstone/commit/4649a455c8b6ba5411eaca1c304e08e8ec5b0b1d) · 2024-06-10T23:17:17Z · documentation

Repoints README documentation status/links from ReadTheDocs to the docs GitHub workflow and endstone.dev. This records a published documentation route, not proof of deployment success.

<a id="commit-1124"></a>
### 1124: docs: add CNAME file {#commit-1124}

Source: [72ec5594f18bc0473f6d3ed69260c9e9a636b61c](https://github.com/EndstoneMC/endstone/commit/72ec5594f18bc0473f6d3ed69260c9e9a636b61c) · 2024-06-10T23:20:50Z · deployment

Adds docs/CNAME containing endstone.dev for the site build. No DNS or hosting account configuration is performed or independently verified.

<a id="commit-1126"></a>
### 1126: docs: update CHANGELOG.md {#commit-1126}

Source: [d3c818fd798250edb03fdb114f4fe11a2f91de09](https://github.com/EndstoneMC/endstone/commit/d3c818fd798250edb03fdb114f4fe11a2f91de09) · 2024-06-13T11:38:21Z · release_evidence

Updates the unreleased changelog with conditional seed hiding, permission checking, command dispatch, player-name/max-player APIs, no debug symbols at runtime and the reported Python 3.9 loader fix. The claims are release descriptions; earlier source shows permission checking is conditional on resolvable command and sender, not every native origin.

<a id="commit-1127"></a>
### 1127: release: version 0.4.7 {#commit-1127}

Source: [1bf6b79d5a550dd83727f66f9d9772a88ae1d821](https://github.com/EndstoneMC/endstone/commit/1bf6b79d5a550dd83727f66f9d9772a88ae1d821) · 2024-06-13T11:39:37Z · release_metadata

Bumps 0.4.6 to 0.4.7 and creates a release changelog section. Its initial May 15 date is corrected at 1128 and the unreleased comparison URL still points to the preceding release range until later cleanup. No release execution is claimed.

<a id="commit-1128"></a>
### 1128: docs: fix CHANGELOG.md {#commit-1128}

Source: [375a0f2dbe8cd91439538b73534bd8216499db9b](https://github.com/EndstoneMC/endstone/commit/375a0f2dbe8cd91439538b73534bd8216499db9b) · 2024-06-13T11:56:02Z · corrective

Corrects the 0.4.7 changelog date to June 13. Documentation-only repair with no independent runtime lesson.

<a id="commit-1129"></a>
### 1129: fix(ci): build windows portable when a new tag is added {#commit-1129}

Source: [30068e7ba43a723731b2e1a26c0484295fe77b7e](https://github.com/EndstoneMC/endstone/commit/30068e7ba43a723731b2e1a26c0484295fe77b7e) · 2024-06-13T11:59:29Z · corrective

Adds tag '*' to the portable Windows workflow's push trigger. This closes the earlier 1028 mismatch where release-only conditions existed without ordinary tag-push triggering. The source fix is verified; an actual release run is not.

<a id="commit-1131"></a>
### 1131: feat: update minecraft version to 1.21.0 {#commit-1131}

Source: [2da6ac5030f44814e6b0fb7cea61f745e2c33f4e](https://github.com/EndstoneMC/endstone/commit/2da6ac5030f44814e6b0fb7cea61f745e2c33f4e) · 2024-06-13T17:43:51Z · release_metadata

Updates Python __minecraft_version__ to 1.21.0. This advertised compatibility marker accompanies native changes; it does not itself establish compatibility.

<a id="commit-1134"></a>
### 1134: docs: update README.md {#commit-1134}

Source: [52c0ec0531217c7f4c18cf4e32869c1686cdbdf7](https://github.com/EndstoneMC/endstone/commit/52c0ec0531217c7f4c18cf4e32869c1686cdbdf7) · 2024-06-13T17:56:32Z · release_metadata

Updates README's supported Minecraft badge to 1.21.0, matching 1131/1130. No separate engineering preference.

<a id="commit-1151"></a>
### 1151: chore: prepare release v0.4.8 {#commit-1151}

Source: [29fefd1d7f161ad2c76c44d42508d2ae6cb13bca](https://github.com/EndstoneMC/endstone/commit/29fefd1d7f161ad2c76c44d42508d2ae6cb13bca) · 2024-06-15T18:34:28Z · release_metadata

Bumps public patch version to 0.4.8 and documents 1.21 support plus Linux ping, flying and UUID fixes. Initial changelog accidentally links to 0.4.7 and loses that section header; repaired at 1152. Claimed outcomes remain release claims.

<a id="commit-1152"></a>
### 1152: fix: CHANGELOG.md {#commit-1152}

Source: [73eb4cb9dfacbd2d18717021dc1e178a5b691690](https://github.com/EndstoneMC/endstone/commit/73eb4cb9dfacbd2d18717021dc1e178a5b691690) · 2024-06-15T18:37:37Z · corrective

Corrects the 0.4.8 release URL and restores the older 0.4.7 heading. Metadata repair only.

<a id="commit-1155"></a>
### 1155: chore: prepare release v0.4.8.1 {#commit-1155}

Source: [072b5de3f3d856bfb622e113371f28e8970f722e](https://github.com/EndstoneMC/endstone/commit/072b5de3f3d856bfb622e113371f28e8970f722e) · 2024-06-15T21:48:40Z · release_evidence

Rewrites the latest changelog release as 0.4.8.1 and adds vanilla-permission regression/attachment fixes. The public header remains patch 8 in this commit; no fabricated four-component macro version or actual release run is claimed.

<a id="commit-1161"></a>
### 1161: docs: update mkdocs.yml to disable rendering inherited members {#commit-1161}

Source: [93fb7e03201d217f5fc06512e92cc91693ad892a](https://github.com/EndstoneMC/endstone/commit/93fb7e03201d217f5fc06512e92cc91693ad892a) · 2024-06-16T19:05:46Z · documentation

Disables inherited-member rendering again. This reverses 1092's setting after introducing explicit event base classes, but causation is not stated. Record the dated sequence rather than a universal preference against inheritance in docs.

<a id="commit-1176"></a>
### 1176: ci: update workflows {#commit-1176}

Source: [53d759779aaba62140b2aabfebd4463b13090e2c](https://github.com/EndstoneMC/endstone/commit/53d759779aaba62140b2aabfebd4463b13090e2c) · 2024-06-17T09:05:25Z · substantive

Removes fixed Conan profile files, relies on detected compiler identity with explicit C++/libc++/Ninja overrides, and points cc/c++ alternatives at the intended Clang instead of only clang/clang++. Wheel and portable jobs move from windows-2022 to windows-2019. This evolves away from the explicit MSVC 194 pin; no single timeless runner/compiler policy is implied.

<a id="commit-1177"></a>
### 1177: feat: use GetExitCodeThread for DLL load result check on Windows {#commit-1177}

Source: [e5e3842d07daaaf7f59270f2c2bb5576e8675704](https://github.com/EndstoneMC/endstone/commit/e5e3842d07daaaf7f59270f2c2bb5576e8675704) · 2024-06-17T09:30:54Z · substantive

Adds GetExitCodeThread declaration/call after waiting for the remote LoadLibrary thread and before resuming the server. The branch tests the API call's BOOL result, not exit_code.value, despite the title's DLL-result claim. Record the exact check as implemented and do not equate it with validated library-load success. No injection or process launch was performed.

<a id="commit-1178"></a>
### 1178: ci: update GitHub workflow triggers in docs.yml {#commit-1178}

Source: [21340a23b221c6b572c6ecab09f3ee75f0fc817b](https://github.com/EndstoneMC/endstone/commit/21340a23b221c6b572c6ecab09f3ee75f0fc817b) · 2024-06-17T09:39:50Z · deployment

Narrows docs pushes to workflow/docs/include/python paths. The workflow still uses contents write and force deployment. Root mkdocs.yml and docs-binding C++ under src are not included in the path filters, so a docs-relevant change alone there would not satisfy this configured filter; this is a bounded source observation, not a CI failure report.

<a id="commit-1183"></a>
### 1183: Merge pull request #21 from EndstoneMC/dependabot/github_actions/docker/build-push-action-6 {#commit-1183}

Source: [9d01b15a8161de855d93dfd61a90211620ffb2c9](https://github.com/EndstoneMC/endstone/commit/9d01b15a8161de855d93dfd61a90211620ffb2c9) · 2024-06-17T14:42:49Z · collaborator_merge

Merges Dependabot PR21: docker/build-push-action v5 to v6 in two workflow jobs. Complete diff against both parents read; second-parent tree is exactly the merge tree, so no additional merge resolution. The bot authored the dependency change and Vincent integrated it; linked action release notes/implementation were not independently reviewed.

<a id="commit-1189"></a>
### 1189: Merge branch 'main' of github.com:EndstoneMC/endstone {#commit-1189}

Source: [4f3a227fa894c5c592313986189c368fb5e6d982](https://github.com/EndstoneMC/endstone/commit/4f3a227fa894c5c592313986189c368fb5e6d982) · 2024-06-17T17:42:49Z · integration_merge

Merges main's Dependabot update into the translation branch. First-parent patch exactly matches 1183's two workflow edits; second-parent patch is the already read 1184–1188 translation work. Full all-parent patches read and full-tree disjoint union verified, with no conflict-specific invention. Do not credit the bot update or repeated translation patch twice.
