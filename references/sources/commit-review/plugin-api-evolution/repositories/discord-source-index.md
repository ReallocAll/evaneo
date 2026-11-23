<!-- retrieval: {"source_ids":["public:commit:1891a7af834d454829a8e4b21015cfacd9d749ac","public:commit:1fb047800d471f4c4e63c668039d2bc782937d13","public:commit:30a490a8334bfbf89ee07e9e989ed7b6e7692d2a","public:commit:331e83247e0d3a2d441227cfc8d44548cd663977","public:commit:4c7de7e0e181a38d64a8982d96fd92bc2d3b64a2","public:commit:52e944c2de281ac762b0e642d7dcdc78205682e7","public:commit:76338833cb8fbc8430061e6ab87a8f64f5a6fa9f","public:commit:84723200b4353c1a4c0dcbf5cb8aa575c5194452","public:commit:9dff7c214bec83fe37a10a69125b060263d9138a","public:commit:ad0f4b216911b3815207b5e0bd3bddec2c8270d9","public:commit:bfa37cfb55cde458f9a9401db00c7450fe147325","public:commit:f027caf803d085239c023315c5bcd851e0f3897c","public:commit:f6889c02a0c5858b47cb95502a8e9412d243424a"],"source_type":"public","date":"2024-05-24..2026-07-12","topics":["build","documentation","refactoring"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstone-essentials-discord-source-index"></a>
# endstone-essentials/discord source index {#endstone-essentials-discord-source-index}

Each entry links to a public commit. Read the linked case before applying a change elsewhere.

<a id="1-76338833cb8fbc8430061e6ab87a8f64f5a6fa9f"></a>
## 1. 76338833cb8fbc8430061e6ab87a8f64f5a6fa9f {#1-76338833cb8fbc8430061e6ab87a8f64f5a6fa9f}

[Initial commit](https://github.com/endstone-essentials/discord/commit/76338833cb8fbc8430061e6ab87a8f64f5a6fa9f)

Disposition: duplicate_scaffold.

Root is exact whole-tree copy of python-example-plugin 44dd3ecd05c76566d2967eaa121ebb2d2fefb519, including template build/publish workflows and example command code. Copied scaffolding gets no independent Discord lesson.

Case: DISCORD01.

<a id="2-bfa37cfb55cde458f9a9401db00c7450fe147325"></a>
## 2. bfa37cfb55cde458f9a9401db00c7450fe147325 {#2-bfa37cfb55cde458f9a9401db00c7450fe147325}

[feat: update plugin metadata](https://github.com/endstone-essentials/discord/commit/bfa37cfb55cde458f9a9401db00c7450fe147325)

Disposition: substantive.

Replaces Python example with Discord plugin skeleton, distribution/entry-point identity, discord.py dependency and project metadata. Removes unrelated sample behavior.

Case: DISCORD01.

<a id="3-1fb047800d471f4c4e63c668039d2bc782937d13"></a>
## 3. 1fb047800d471f4c4e63c668039d2bc782937d13 {#3-1fb047800d471f4c4e63c668039d2bc782937d13}

[feat: send join and leave messages to channel](https://github.com/endstone-essentials/discord/commit/1fb047800d471f4c4e63c668039d2bc782937d13)

Disposition: substantive.

Starts separate multiprocessing worker running Discord asyncio client; sends plain player-name join/leave dictionaries via SimpleQueue; main process terminates/joins worker on disable. Sets Python executable by platform. Configuration token is placeholder text, not a credential.

Case: DISCORD01.

<a id="4-1891a7af834d454829a8e4b21015cfacd9d749ac"></a>
## 4. 1891a7af834d454829a8e4b21015cfacd9d749ac {#4-1891a7af834d454829a8e4b21015cfacd9d749ac}

[docs: update README.md](https://github.com/endstone-essentials/discord/commit/1891a7af834d454829a8e4b21015cfacd9d749ac)

Disposition: documentation.

README explicitly labels this a proof of concept. This narrows confidence rather than proving production readiness.

Case: DISCORD01.

<a id="5-ad0f4b216911b3815207b5e0bd3bddec2c8270d9"></a>
## 5. ad0f4b216911b3815207b5e0bd3bddec2c8270d9 {#5-ad0f4b216911b3815207b5e0bd3bddec2c8270d9}

[ci: remove workflow files](https://github.com/endstone-essentials/discord/commit/ad0f4b216911b3815207b5e0bd3bddec2c8270d9)

Disposition: substantive.

Deletes inherited installation/publishing workflows. No replacement tests or CI evidence; removal alone does not establish an anti-CI preference.

Case: DISCORD01.

<a id="6-9dff7c214bec83fe37a10a69125b060263d9138a"></a>
## 6. 9dff7c214bec83fe37a10a69125b060263d9138a {#6-9dff7c214bec83fe37a10a69125b060263d9138a}

[refactor: remove print](https://github.com/endstone-essentials/discord/commit/9dff7c214bec83fe37a10a69125b060263d9138a)

Disposition: mechanical.

Removes diagnostic printing of resolved channels. No architecture change.

Case: DISCORD01.

<a id="7-331e83247e0d3a2d441227cfc8d44548cd663977"></a>
## 7. 331e83247e0d3a2d441227cfc8d44548cd663977 {#7-331e83247e0d3a2d441227cfc8d44548cd663977}

[refactor: remove unused parameters](https://github.com/endstone-essentials/discord/commit/331e83247e0d3a2d441227cfc8d44548cd663977)

Disposition: mechanical.

Removes unused queue/config keyword arguments passed to discord.Client; values remain closed-over in main.

Case: DISCORD01.

<a id="8-f027caf803d085239c023315c5bcd851e0f3897c"></a>
## 8. f027caf803d085239c023315c5bcd851e0f3897c {#8-f027caf803d085239c023315c5bcd851e0f3897c}

[feat: add status and chat channels](https://github.com/endstone-essentials/discord/commit/f027caf803d085239c023315c5bcd851e0f3897c)

Disposition: substantive.

Introduces DiscordClient class, bidirectional queues, chat/start/stop messages and scheduled server-side draining. Shutdown becomes close sentinel plus unbounded join; client closes only within status-channel branch. Inbound path initially compares integer channel ID to configured string and queues Discord Message object.

Case: DISCORD01.

<a id="9-30a490a8334bfbf89ee07e9e989ed7b6e7692d2a"></a>
## 9. 30a490a8334bfbf89ee07e9e989ed7b6e7692d2a {#9-30a490a8334bfbf89ee07e9e989ed7b6e7692d2a}

[fix: chat event not working](https://github.com/endstone-essentials/discord/commit/30a490a8334bfbf89ee07e9e989ed7b6e7692d2a)

Disposition: substantive.

Normalizes configured chat ID to int and converts Discord Message to primitive formatted text before crossing process boundary; server adds [Discord] prefix. Repairs both data-type mismatch and transport representation.

Case: DISCORD01.

<a id="10-52e944c2de281ac762b0e642d7dcdc78205682e7"></a>
## 10. 52e944c2de281ac762b0e642d7dcdc78205682e7 {#10-52e944c2de281ac762b0e642d7dcdc78205682e7}

[Merge pull request #1 from ArkanDash/main](https://github.com/endstone-essentials/discord/commit/52e944c2de281ac762b0e642d7dcdc78205682e7)

Disposition: merge_integration.

Merges ArkanDash PR1: embeds, consolidated chat channel, death notices, player-count topic and console-command bridge. Imported privilege/lifecycle changes are ArkanDash-authored, with target merge/thanks only. Merge tree equals second parent; full six-file first-parent patch and thread dossier verified.

Case: DISCORD01.

<a id="11-4c7de7e0e181a38d64a8982d96fd92bc2d3b64a2"></a>
## 11. 4c7de7e0e181a38d64a8982d96fd92bc2d3b64a2 {#11-4c7de7e0e181a38d64a8982d96fd92bc2d3b64a2}

[feat: support endstone api v0.5](https://github.com/endstone-essentials/discord/commit/4c7de7e0e181a38d64a8982d96fd92bc2d3b64a2)

Disposition: substantive.

Migrates api_version to 0.5 and scheduler calls to run_task; removes manual executable override. Fixes player-count cache by assigning current count, and changes shutdown from 10-second sleep to join(timeout=5) then terminate. No final join/re-check/close acknowledgment is added; cache updates before awaited edit.

Case: DISCORD01.

<a id="12-f6889c02a0c5858b47cb95502a8e9412d243424a"></a>
## 12. f6889c02a0c5858b47cb95502a8e9412d243424a {#12-f6889c02a0c5858b47cb95502a8e9412d243424a}

[chore: bump version to 0.2.0](https://github.com/endstone-essentials/discord/commit/f6889c02a0c5858b47cb95502a8e9412d243424a)

Disposition: mechanical.

Bumps distribution version 0.1.0 to 0.2.0 and adds trailing config newline. No independent runtime improvement.

Case: DISCORD01.

<a id="13-84723200b4353c1a4c0dcbf5cb8aa575c5194452"></a>
## 13. 84723200b4353c1a4c0dcbf5cb8aa575c5194452 {#13-84723200b4353c1a4c0dcbf5cb8aa575c5194452}

[docs: update README.md](https://github.com/endstone-essentials/discord/commit/84723200b4353c1a4c0dcbf5cb8aa575c5194452)

Disposition: documentation.

README now documents installation, token/channel configuration, Endstone0.5 requirement, bidirectional chat, death and console commands, and troubleshooting. Console channel gives server-command privileges through code; docs do not add per-user authorization.

Case: DISCORD01.
