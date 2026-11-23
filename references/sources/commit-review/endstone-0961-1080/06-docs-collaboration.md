<!-- retrieval: {"source_ids":["public:commit:00c7ca3b67dd0eac2bb76afc1f4eb276e93f6bed","public:commit:1acf3792cf0490fb27f5943f0dfa2a338372a44a","public:commit:260039da4d0f6c7a79fc4fd39eb7126bf3b4e52b","public:commit:273b72599fd3a327776f71fd70e63e56abd1df0a","public:commit:306ccbb699ba7b0ab4181ee878aa2304b5fda4c5","public:commit:4710727d2456a89be617ac04d0371eb02961d513","public:commit:6775dab5ce060a8870ac8c433b93aea33d7e7b71","public:commit:a20e528f88221a68a11c0338a2b8c050d22eb0f1","public:commit:c7a19bf664e5a932b49819dc7b20727a7799f44f","public:commit:cc4b02c5e19b480aca4fcc72b069b34d96ce6bb5","public:commit:ff6b6c4e24c5f28e354e681154d1847c7d1ea531"],"source_type":"public","date":"2024-05-21..2024-05-27","topics":["ffi","testing","build","documentation","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
# Documentation tracks packaging changes and preserves contributor credit {#documentation-tracks-packaging-changes-and-preserves-contributor-credit}

## The onboarding route changes with the loader {#the-onboarding-route-changes-with-the-loader}

The previous unit taught editable installation into the running environment.1000 revises the tutorial to build a wheel with pipx and copy it into plugins, matching the wheel-plugin discovery introduced earlier. It also changes the sample project backend from setuptools to hatchling, fixes package-layout guidance and simplifies C++ artifact installation. The replacement screenshot was visually inspected: it shows a successful wheel in PyCharm with setuptools-style egg-info/build output. It demonstrates the intended artifact, not that the new backend example was executed. The removed editable-install screenshot is an exact previously inspected blob, so it receives verified reuse rather than another imaginary visual inspection.

Presentation-only CSS/badge/version-navigation edits are accounted for briefly. Removing a Compose example from README is not equivalent to removing Compose support. The roadmap’s estimates and in-progress labels are dated plans, not observed completion dates. Changelog claims are cross-checked against implementation: notably, temporarily-operator performCommand uses an elevated origin, and the riding/lava corrections have specific bounded meanings.

## Color documentation has a separate author and integration history {#color-documentation-has-a-separate-author-and-integration-history}

1055 merges PR13 by Lucy, whose GitHub account is Adrian8115. The branch contains a blank-file creation followed by the substantive tutorial. Both were read; the merged tree equals the branch head, so no conflict-resolution delta is attributed to the merger.1056 makes the tutorial discoverable in navigation.1057 adds imports/includes, makes reset guidance more prominent and reorganizes the table. These are meaningful integration edits by Vincent, while the original explanation/examples/table remain Lucy’s contribution.

1045 separately credits Duckos for the two native/logging PRs. These explicit acknowledgements plus branch metadata support collaborator attribution. They do not supply unseen review comments, objections or private motives. PR discussions are outside this unit’s read scope, and exact base/head equivalence must be established before anyone reuses commit coverage as a whole-PR claim.

## Testing and limits {#testing-and-limits}

No documentation generator, tutorial example, plugin build or image-producing command was executed. The screenshot and commit messages are published source evidence of intended/reported outcomes. Core explanatory reasoning is preserved locally in this dossier and the linked implementation families; public links below are provenance, not substitutes for offline explanations. Small presentation changes are not elevated into engineering principles, and obsolete Nukkit material is not used to fill gaps in modern evidence.


## Individual commit dispositions {#individual-commit-dispositions}


<a id="commit-999"></a>
### 999: docs: update CHANGELOG.md {#commit-999}

Source: [a20e528f88221a68a11c0338a2b8c050d22eb0f1](https://github.com/EndstoneMC/endstone/commit/a20e528f88221a68a11c0338a2b8c050d22eb0f1). Authored 2024-05-21T03:12:19Z; Git author Vincent. Disposition: behavior_documentation.

Changelog describes performCommand as temporarily granting operator permission. The inspected implementation uses an elevated command origin, without changing stored player op status. Preserve the author’s intent and this implementation distinction; do not infer account-level privilege changes from the shorthand description.


<a id="commit-1000"></a>
### 1000: docs: update tutorials {#commit-1000}

Source: [cc4b02c5e19b480aca4fcc72b069b34d96ce6bb5](https://github.com/EndstoneMC/endstone/commit/cc4b02c5e19b480aca4fcc72b069b34d96ce6bb5). Authored 2024-05-21T06:21:11Z; Git author Vincent. Disposition: onboarding_revision.

Changes tutorial packaging from setuptools to hatchling, replaces editable-install instructions with pipx build and copying a wheel into plugins, corrects flat package layout wording and simplifies C++ DLL installation. The new PNG visibly shows successful wheel output in PyCharm, including setuptools-style egg-info logs; it illustrates wheel production but is not proof the newly documented backend was exercised. Deleted editable-install PNG reuses the prior inspected exact blob.


<a id="commit-1001"></a>
### 1001: docs: update extra.css {#commit-1001}

Source: [260039da4d0f6c7a79fc4fd39eb7126bf3b4e52b](https://github.com/EndstoneMC/endstone/commit/260039da4d0f6c7a79fc4fd39eb7126bf3b4e52b). Authored 2024-05-21T06:46:45Z; Git author Vincent. Disposition: presentation.

Adjusts image/card/admonition border radii. The full CSS diff was read; it supplies no independent architectural or personal-style lesson.


<a id="commit-1008"></a>
### 1008: docs: update versions.json for mike {#commit-1008}

Source: [273b72599fd3a327776f71fd70e63e56abd1df0a](https://github.com/EndstoneMC/endstone/commit/273b72599fd3a327776f71fd70e63e56abd1df0a). Authored 2024-05-21T14:59:41Z; Git author Vincent. Disposition: presentation.

Removes the v0.4.2 item from documentation version navigation. This is a small maintained-documentation selection change, not evidence that the release was retracted or unsupported at runtime.


<a id="commit-1020"></a>
### 1020: docs: update README.md {#commit-1020}

Source: [c7a19bf664e5a932b49819dc7b20727a7799f44f](https://github.com/EndstoneMC/endstone/commit/c7a19bf664e5a932b49819dc7b20727a7799f44f). Authored 2024-05-22T03:27:48Z; Git author Vincent. Disposition: readme_revision.

Refreshes PyPI/Python/Docker badges and removes the README’s production Compose example. The actual diff does not remove the Compose implementation or prove a deployment strategy reversal.


<a id="commit-1024"></a>
### 1024: docs: update CHANGELOG.md {#commit-1024}

Source: [00c7ca3b67dd0eac2bb76afc1f4eb276e93f6bed](https://github.com/EndstoneMC/endstone/commit/00c7ca3b67dd0eac2bb76afc1f4eb276e93f6bed). Authored 2024-05-22T04:27:21Z; Git author Vincent. Disposition: behavior_documentation.

Adds changelog entries for Dimension/GameMode and riding-velocity correction. These are reported capabilities tied to the implementation sequence, not measured performance or complete test coverage.


<a id="commit-1026"></a>
### 1026: docs: update README.md {#commit-1026}

Source: [6775dab5ce060a8870ac8c433b93aea33d7e7b71](https://github.com/EndstoneMC/endstone/commit/6775dab5ce060a8870ac8c433b93aea33d7e7b71). Authored 2024-05-22T04:46:06Z; Git author Vincent. Disposition: planning.

Revises the roadmap into Player/Actor, Item, Block, Inventory and Form/Scoreboard phases with month estimates and in-progress labels. Treat these as dated planning claims; the estimates do not establish delivery dates or achieved completeness.


<a id="commit-1045"></a>
### 1045: docs: update CHANGELOG.md {#commit-1045}

Source: [1acf3792cf0490fb27f5943f0dfa2a338372a44a](https://github.com/EndstoneMC/endstone/commit/1acf3792cf0490fb27f5943f0dfa2a338372a44a). Authored 2024-05-26T01:05:37Z; Git author Vincent. Disposition: attribution_documentation.

Changelog credits Duckos for PR11’s native structure information and PR12’s log-switch change and records plugin configuration support. This is explicit collaborator attribution, not evidence of unseen review objections or benchmarking.


<a id="commit-1055"></a>
### 1055: Merge pull request #13 from Adrian8115/patch-1 {#commit-1055}

Source: [4710727d2456a89be617ac04d0371eb02961d513](https://github.com/EndstoneMC/endstone/commit/4710727d2456a89be617ac04d0371eb02961d513). Authored 2024-05-27T01:25:40Z; Git author Vincent (Zhengyu) Wu. Disposition: collaborative_merge.

Merges PR13 by Lucy (Adrian8115), adding the color-code tutorial with Python/C++ examples, reset guidance and a complete listed code table. Both branch commits are read: the first creates a blank file, the second supplies content. Merge tree equals the second parent, so no separate conflict-resolution code is attributed to Vincent.


<a id="commit-1056"></a>
### 1056: docs: add use-color-codes.md to mkdocs.yml {#commit-1056}

Source: [306ccbb699ba7b0ab4181ee878aa2304b5fda4c5](https://github.com/EndstoneMC/endstone/commit/306ccbb699ba7b0ab4181ee878aa2304b5fda4c5). Authored 2024-05-27T01:52:03Z; Git author Vincent. Disposition: documentation_integration.

Adds the contributed color tutorial to navigation and normalizes YAML spacing. This makes the document discoverable; it does not create the original tutorial or change runtime color formatting.


<a id="commit-1057"></a>
### 1057: docs: update use-color-codes.md {#commit-1057}

Source: [ff6b6c4e24c5f28e354e681154d1847c7d1ea531](https://github.com/EndstoneMC/endstone/commit/ff6b6c4e24c5f28e354e681154d1847c7d1ea531). Authored 2024-05-27T02:21:08Z; Git author Vincent. Disposition: documentation_revision.

Adds the Python import and C++ header, promotes reset advice into admonitions and reorganizes/lowercases the color table with presentation CSS. These are concrete usability edits to Lucy’s tutorial. No tutorial build or example execution was performed.
