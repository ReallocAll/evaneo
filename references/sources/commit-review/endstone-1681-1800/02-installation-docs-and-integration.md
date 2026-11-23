<!-- retrieval: {"source_ids":["public:commit:1450c69a6ce4a5a61876566f24431f4b85930dc0","public:commit:1b75bf04ec5780a6cfc6299237005be0549d3c56","public:commit:1d8b51dcfbe75a43ef08c7d843c8a95480f3cd6e","public:commit:20e02426d3df22945bee3969b5e25b34cf87c4a3","public:commit:28c483ca4861dde0ff5c83873cfe4531727a5409","public:commit:337e890c0d2fe0e130d16b52180327afebc0a511","public:commit:3fcf086e725a22579721d86ebedff8a052f0525c","public:commit:47363dcfa3e6c5f7bf52f9e3e8b72bb3c9324fde","public:commit:53befab4c8cd675180c6c7fd3645e9a04b722289","public:commit:77145ea8c6c5f1df957c32d21706606d9d9036b6","public:commit:7ce7f873eaae171cd777e4dc7f6eef94db0f1de7","public:commit:7f2af673f6ef55898b106cf958b2dbd1c8f7f737","public:commit:98ad1dfa0deaa76674dc4a5d17c82bb035ac3c91","public:commit:a0d3c537bd133e068a5370b76d9c527c1934a108","public:commit:aaed9cdc430a1b35d31382dfcd666a9513c1938b","public:commit:c37416c04fda0db5963cdcf9a357ec588c645079","public:commit:ca561eba67b5ab2762f1458d67f232b5dee37a10","public:commit:dee50d353672b595f410b8a13a688b7b663b0585","public:commit:e8316ff38aaf17f405b73e2c0cc37a1127f9ea68","public:commit:eb0502b8283572f583c40f1fedc5c7ce02d8dad9","public:commit:f5a811fa7d3e4571dc9dcf4c3d627f3017764a9f","public:commit:f7cc244fe040ada770daa83a48ebbcdb91eb8c9e","public:context-commit:4ffe94c13e0328ff8046414a5469704d289ccbce","public:context-commit:57af0e5b51f4bc09aa2dec2e8a649dfdcad45036","public:context-commit:63e4b2e1ff974656025935e0b25b26a1945fc4fc","public:context-commit:8ae668acb0f316392e81c1b3af93930bafccf2a3","public:context-commit:8f0699b906f470e985efd4cebb12a73de330651d","public:context-commit:ad1aee1d647946be9e1aa74ba4e836473d75ded4","public:context-commit:f71acc131f8f9ed386a1c0bde5ba529dd89013ac"],"source_type":"public","date":"2024-08-29..2024-09-14","topics":["lifetime","ffi","testing","build","performance","api","documentation","review","refactoring"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
# Installation, development documentation and collaborator integration {#installation-development-documentation-and-collaborator-integration}


Endstone commits 1681–1800, dated August 29–September 14, 2024.

## Decision chain and attribution {#decision-chain-and-attribution}

The installer is collaborator work. legitbox authored three initial script/documentation commits and three follow-on derivative-distribution changes; Vincent integrated them and then repaired paths, wording and the missing ID fallback. The initial branch's README downloads from the collaborator fork and repeats the wrong chmod target. Subsequent project edits move scripts into scripts/, use official repository paths and separate installation from repeated startup. The six contextual legitbox commits retain independent SHA identities in the collaborator ledger.

The scripts solve a practical setup problem but make broad operational choices: a shared $HOME/venv, package-manager changes, an Arch full upgrade, and unconditional restart after any process exit. These facts delimit reuse. This review did not execute them, and does not recommend copying them into current deployment automation without explicit error, version and stop-policy decisions. The ID→ID_LIKE→ID_LIKE-or-ID chain is a compact example of broadening a feature while temporarily regressing the original base case.

Documentation expands into editable development and staged publication. The explicit editable-install rationale is faster iteration without wheel rebuilding. TestPyPI before production is a documented staging step. The unrestricted-token wording is retained only as historical evidence, not as current security guidance. No login or publication occurred. Release prose provides useful rationale but can be imprecise: 1777 says PlayerKnockbackEvent while the actual API is ActorKnockbackEvent.

The Ko-fi widget is a separate, short-lived site experiment: add, adjust mobile behavior, then remove all dynamic overlay code in favor of a static badge. The reason for removal is unknown. It does not support a durable UI or privacy preference.

## Causal ordering and reusable coverage {#causal-ordering-and-reusable-coverage}

Chronological ordinal order is not a single linear branch. 1693 descends from 1689, then 1694 merges the collaborator/funding branch. Likewise 1797's Gurkan spelling repair descends from 1793 while 1798 follows the independent local refactor branch. At 1799, all 70 inherited changed-path endpoints and the canonical base-to-local patch match already-read work. The six merges have empty remerge diffs. These facts justify source reuse without attributing imported implementation to the merge author or claiming an entire PR's discussion was reviewed. Gurkan's actual spelling commit is preserved as additional collaborator context.

## Individual commit dispositions {#individual-commit-dispositions}

<a id="commit-1684"></a>

### Commit 1684 {#commit-1684}

2024-08-29T21:19:22Z · `20e02426d3df22945bee3969b5e25b34cf87c4a3` · feat: add auto-installer and start bash script for Linux

Integrates legitbox's three commits adding installation, restart and README instructions. The installer chooses apt/dnf/pacman, creates a fixed home-directory virtual environment and installs Endstone; Arch includes a noninteractive full upgrade. The restart loop restarts clean stops as well as crashes. Error checking and environment isolation are limited. Both parent diffs, the branch commits and empty remerge result were examined; Vincent's merge does not transfer authorship of these scripts.

Source: [individual commit](https://github.com/EndstoneMC/endstone/commit/20e02426d3df22945bee3969b5e25b34cf87c4a3). Classification: collaborator_integration.

<a id="commit-1685"></a>
### Commit 1685 {#commit-1685}

2024-08-29T21:28:36Z · `7ce7f873eaae171cd777e4dc7f6eef94db0f1de7` · refactor: move bash scripts to script folder

Moves the two shell scripts into scripts/ with exact blob identity. Their installation and restart behavior is unchanged. README references are repaired in the next commit rather than in this move. Canonical delete/add representations are covered by exact relocation proof, not counted as new script implementation.

Source: [individual commit](https://github.com/EndstoneMC/endstone/commit/7ce7f873eaae171cd777e4dc7f6eef94db0f1de7). Classification: verified_mechanical.

<a id="commit-1686"></a>
### Commit 1686 {#commit-1686}

2024-08-29T21:28:43Z · `1d8b51dcfbe75a43ef08c7d843c8a95480f3cd6e` · docs: update README.md

Reworks Linux installation instructions to use the official EndstoneMC repository paths after the relocation, fixes the repeated chmod target so start.sh is executable, and separates download, install and start steps. This is an operational documentation correction. The scripts themselves still have the constraints described at 1684.

Source: [individual commit](https://github.com/EndstoneMC/endstone/commit/1d8b51dcfbe75a43ef08c7d843c8a95480f3cd6e). Classification: documentation_revision.

<a id="commit-1687"></a>
### Commit 1687 {#commit-1687}

2024-08-29T22:16:05Z · `28c483ca4861dde0ff5c83873cfe4531727a5409` · docs: update README.md

Changes the README distinction between supported operating systems and their derivative distributions. This wording-only revision does not add distribution detection. The subsequent collaborator patch changes the detection logic, and 1744 later restores a fallback for systems without ID_LIKE.

Source: [individual commit](https://github.com/EndstoneMC/endstone/commit/28c483ca4861dde0ff5c83873cfe4531727a5409). Classification: verified_mechanical.

<a id="commit-1688"></a>
### Commit 1688 {#commit-1688}

2024-08-29T22:22:37Z · `77145ea8c6c5f1df957c32d21706606d9d9036b6` · docs: update CHANGELOG.md

Adds release notes for Minecraft 1.21.22, boss bars, block events and chunk-access protection, and credits legitbox's installer. The notes also report the virtual-environment fix associated with issue 38. These are dated release claims supported to varying degrees by prior code review; the issue discussion and runtime outcomes were not read or reproduced in this unit.

Source: [individual commit](https://github.com/EndstoneMC/endstone/commit/77145ea8c6c5f1df957c32d21706606d9d9036b6). Classification: release_claims.

<a id="commit-1689"></a>
### Commit 1689 {#commit-1689}

2024-08-29T23:22:43Z · `aaed9cdc430a1b35d31382dfcd666a9513c1938b` · chore: release v0.5.2

Releases 0.5.2, opens the 0.5.3 changelog section, refreshes the compatibility badge, adds a dismissible Discord announcement template and changes the site copyright attribution to EndstoneMC. It is not just a version bump. The site changes provide project-maintenance context, not a strong inference about enduring UI taste.

Source: [individual commit](https://github.com/EndstoneMC/endstone/commit/aaed9cdc430a1b35d31382dfcd666a9513c1938b). Classification: release_and_site_change.

<a id="commit-1690"></a>

### Commit 1690 {#commit-1690}

2024-08-30T00:17:25Z · `1b75bf04ec5780a6cfc6299237005be0549d3c56` · Autoinstall.sh update (#41)

Merges legitbox's ID_LIKE wildcard detection and removal of the warning about derivative distributions. The two branch commits were read separately; the second-parent tree is identical to the merge tree. Using only ID_LIKE introduces an omitted-base-distribution case when that variable is absent. Commit 1744 repairs this with ID fallback. PR 41's discussion is not inferred from the merge title.

Source: [individual commit](https://github.com/EndstoneMC/endstone/commit/1b75bf04ec5780a6cfc6299237005be0549d3c56). Classification: collaborator_integration.

<a id="commit-1691"></a>

### Commit 1691 {#commit-1691}

2024-08-30T00:17:31Z · `3fcf086e725a22579721d86ebedff8a052f0525c` · Update README.md (#42)

Merges legitbox's README claim that derivatives are supported. The branch starts from 1689, independently of the installer branch, so its second-parent diff imports the already-read installer changes. Exact base/parent/merge endpoint checks establish that provenance. This commit documents the detection patch; it does not independently implement or validate broad distro support.

Source: [individual commit](https://github.com/EndstoneMC/endstone/commit/3fcf086e725a22579721d86ebedff8a052f0525c). Classification: collaborator_integration.

<a id="commit-1692"></a>
### Commit 1692 {#commit-1692}

2024-08-30T10:52:07Z · `47363dcfa3e6c5f7bf52f9e3e8b72bb3c9324fde` · chore: update FUNDING.yml

Changes funding configuration to Ko-fi while leaving other funding-provider entries commented out. The actual configuration diff was read. No independent software-engineering preference follows from this administrative choice.

Source: [individual commit](https://github.com/EndstoneMC/endstone/commit/47363dcfa3e6c5f7bf52f9e3e8b72bb3c9324fde). Classification: verified_mechanical.

<a id="commit-1693"></a>
### Commit 1693 {#commit-1693}

2024-08-30T11:45:10Z · `dee50d353672b595f410b8a13a688b7b663b0585` · docs: add ko-fi button

Adds an externally loaded Ko-fi overlay, right-side positioning and scroll-based hide/show behavior. It branches directly from 1689, before the two collaborator integrations and funding change. The script assumes its queried element exists. Later mobile adjustments and complete removal at 1700 make this a short-lived experiment, with no documented reason for eventual removal.

Source: [individual commit](https://github.com/EndstoneMC/endstone/commit/dee50d353672b595f410b8a13a688b7b663b0585). Classification: site_experiment.

<a id="commit-1694"></a>

### Commit 1694 {#commit-1694}

2024-08-30T11:45:17Z · `c37416c04fda0db5963cdcf9a357ec588c645079` · Merge remote-tracking branch 'origin/main'

Integrates the 1690–1692 branch into the separately authored Ko-fi overlay branch. The first-parent changes are the previously reviewed installer, README and funding work; the second-parent changes are the overlay from 1693. Every changed endpoint and the empty remerge diff match the independent branches. There is no separate conflict-resolution implementation to attribute.

Source: [individual commit](https://github.com/EndstoneMC/endstone/commit/c37416c04fda0db5963cdcf9a357ec588c645079). Classification: verified_merge_reuse.

<a id="commit-1695"></a>
### Commit 1695 {#commit-1695}

2024-08-30T11:59:15Z · `7f2af673f6ef55898b106cf958b2dbd1c8f7f737` · docs: add ko-fi badge to README.md

Adds a Ko-fi support badge to README. This is a small project-support navigation change, fully read, with no independent implementation lesson.

Source: [individual commit](https://github.com/EndstoneMC/endstone/commit/7f2af673f6ef55898b106cf958b2dbd1c8f7f737). Classification: verified_mechanical.

<a id="commit-1696"></a>
### Commit 1696 {#commit-1696}

2024-08-30T13:52:11Z · `eb0502b8283572f583c40f1fedc5c7ce02d8dad9` · fix: kofi button on mobile devices

Adjusts the overlay for mobile containers, position, width, color and stacking. The script now works with multiple queried widget elements but still assumes they exist. The commit claims a mobile-display repair; no browser execution was performed. Its lifetime is bounded by 1700's removal of the entire overlay approach.

Source: [individual commit](https://github.com/EndstoneMC/endstone/commit/eb0502b8283572f583c40f1fedc5c7ce02d8dad9). Classification: site_experiment_revision.

<a id="commit-1700"></a>
### Commit 1700 {#commit-1700}

2024-08-31T17:36:13Z · `f5a811fa7d3e4571dc9dcf4c3d627f3017764a9f` · docs: update announcement

Deletes the external Ko-fi overlay and scroll scripts, replacing them with a static support badge in the announcement alongside Discord. This is a clear reversal of 1693 and 1696, but the commit does not explain why. Do not invent a performance, privacy or aesthetic rationale.

Source: [individual commit](https://github.com/EndstoneMC/endstone/commit/f5a811fa7d3e4571dc9dcf4c3d627f3017764a9f). Classification: reversal.

<a id="commit-1738"></a>
### Commit 1738 {#commit-1738}

2024-09-05T21:33:29Z · `a0d3c537bd133e068a5370b76d9c527c1934a108` · docs: add instructions of entering the "development mode"

Documents editable installation inside the server's virtual environment and using reload to pick up development changes without rebuilding a wheel. It also tells developers to uninstall the editable package when finished. The explicit rationale is shorter development iteration. The documented workflow is not evidence that every import/lifetime edge of reload has been solved.

Source: [individual commit](https://github.com/EndstoneMC/endstone/commit/a0d3c537bd133e068a5370b76d9c527c1934a108). Classification: development_workflow.

<a id="commit-1739"></a>
### Commit 1739 {#commit-1739}

2024-09-05T22:21:42Z · `98ad1dfa0deaa76674dc4a5d17c82bb035ac3c91` · docs: finish the "Publish your plugin" tutorial

Adds a packaging tutorial using isolated build tooling, TestPyPI before production PyPI, twine and optional release automation. It recommends tokens over account passwords but also describes an unrestricted token, a historical security choice rather than current advice from this review. No credentials were read, recorded or used; no build, login or upload was performed.

Source: [individual commit](https://github.com/EndstoneMC/endstone/commit/98ad1dfa0deaa76674dc4a5d17c82bb035ac3c91). Classification: publishing_workflow.

<a id="commit-1744"></a>
### Commit 1744 {#commit-1744}

2024-09-07T13:39:11Z · `1450c69a6ce4a5a61876566f24431f4b85930dc0` · feat: improve auto installer script

Uses ID_LIKE when available and ID otherwise, repairing the collaborator detection path that excluded base distributions without ID_LIKE. The change is small and directly supported by the shell expression. It does not address package-manager failures, shared virtual-environment naming or the restart policy.

Source: [individual commit](https://github.com/EndstoneMC/endstone/commit/1450c69a6ce4a5a61876566f24431f4b85930dc0). Classification: installer_repair.

<a id="commit-1777"></a>
### Commit 1777 {#commit-1777}

2024-09-11T23:15:01Z · `e8316ff38aaf17f405b73e2c0cc37a1127f9ea68` · docs: update CHANGELOG.md

Prepares 0.5.3 notes covering block APIs, messages, metrics, reload expansion and fixes. It explicitly explains the breaking scoreboard rename as factory-name consistency and identifies XP precision and libc++ symbol errors. The notes call the knockback event PlayerKnockbackEvent although the source implements ActorKnockbackEvent; preserve that discrepancy rather than treating release prose as an exact API inventory.

Source: [individual commit](https://github.com/EndstoneMC/endstone/commit/e8316ff38aaf17f405b73e2c0cc37a1127f9ea68). Classification: release_claims_and_rationale.

<a id="commit-1780"></a>
### Commit 1780 {#commit-1780}

2024-09-12T09:22:21Z · `53befab4c8cd675180c6c7fd3645e9a04b722289` · chore: release v0.5.3

Increments the public patch version to 0.5.3. ENDSTONE_API_VERSION remains 0.5 despite this unit's documented C++ API changes. The version bump was read in full; it is release bookkeeping, not independent proof of binary compatibility or test success.

Source: [individual commit](https://github.com/EndstoneMC/endstone/commit/53befab4c8cd675180c6c7fd3645e9a04b722289). Classification: verified_mechanical.

<a id="commit-1781"></a>
### Commit 1781 {#commit-1781}

2024-09-12T13:11:27Z · `f7cc244fe040ada770daa83a48ebbcdb91eb8c9e` · docs: update README.md

Updates the README Minecraft compatibility badge from 1.21.22 to 1.21.23. This follows the source-map corrections and release bump. No new executable behavior is introduced.

Source: [individual commit](https://github.com/EndstoneMC/endstone/commit/f7cc244fe040ada770daa83a48ebbcdb91eb8c9e). Classification: verified_mechanical.

<a id="commit-1797"></a>

### Commit 1797 {#commit-1797}

2024-09-14T12:37:45Z · `337e890c0d2fe0e130d16b52180327afebc0a511` · fix spelling of recommended (#50)

Merges Gurkan's one-word recommended spelling repair from PR 50. The collaborator commit was read independently and the merge equals its second-parent tree. Its first parent is 1793, not the timestamp-preceding 1796 branch; that causal distinction is preserved in the DAG audit. No broader review or style endorsement is inferred.

Source: [individual commit](https://github.com/EndstoneMC/endstone/commit/337e890c0d2fe0e130d16b52180327afebc0a511). Classification: collaborator_mechanical_integration.

<a id="commit-1799"></a>

### Commit 1799 {#commit-1799}

2024-09-14T16:29:18Z · `ca561eba67b5ab2762f1458d67f232b5dee37a10` · Merge remote-tracking branch 'origin/main'

Integrates the remote spelling merge into the local native-refactor branch. The first-parent patch repeats Gurkan's spelling change. The large second-parent diff is proven byte-identical to the already-read base-to-local chain 1794, 1795, 1796 and 1798, with all 70 changed path endpoints verified and no remerge delta. It receives exact inherited coverage, not duplicate authorship or a new independent lesson.

Source: [individual commit](https://github.com/EndstoneMC/endstone/commit/ca561eba67b5ab2762f1458d67f232b5dee37a10). Classification: verified_merge_reuse.

## Coverage boundary {#coverage-boundary}

Findings rely on the linked public sources; external PR/issue discussions, dependencies, and native engine internals are outside the cited evidence. Runtime and current-release behavior were not tested.
