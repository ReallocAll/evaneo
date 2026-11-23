<!-- retrieval: {"source_ids":["public:commit:3d3683683b12e3753b11a28d106097383d116b48","public:commit:4817841a0b26ee47f84c20bf00adf08ef476c010","public:commit:8a6b67255abb9bb28ec8ddc34fe339ff076f89a8","public:commit:a02d4414ca0577a478bad5d646e8cf512ccd874f","public:commit:aa64d3a6efb662a9fad24c93da31ef3cbd05f1ac","public:commit:bca16e2c663297604086514ce61a906dfa8f84c1"],"source_type":"public","date":"2024-08-03..2025-02-11","topics":["lifetime","testing","build","api","documentation","review","refactoring"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="sidebar01-refactoring-a-display-registry-can-change-user-visible-behavior"></a>
# Refactoring a display registry can change user-visible behavior {#sidebar01-refactoring-a-display-registry-can-change-user-visible-behavior}

## Context, ownership and issue {#context-ownership-and-issue}

Six commits in the reviewed history range modify a sidebar plugin originated by daoge_cmd. The original scaffold is an exact tree copy of python-example-plugin `18ffc833b2c6004a4ddd2a4a2e15f10c62e2d0c3`; daoge_cmd then adds the sidebar, per-player scoreboard, timed update, configurable title/content and providers. Their early fixes use `set_display` and pass the title to add_objective. These are collaborator contributions, not inventions by Vincent.

The final update loop runs every configured period, creates a personal scoreboard on player join, formats title/content, unregisters any old custom objective and recreates it with scores for each line. It skips players still using the global server scoreboard. This context matters when interpreting later placeholder-only edits: they do not change objective recreation or initialize already-online players during reload.

Issue2 reports v0.0.1 failing because the bound Server no longer has `get_new_scoreboard`. The provided configuration is incidental to that missing-method exception. Vincent points to0.2.0. The existing release comparison has exact base `584f7f659057121ea0d7899ce3264ba0af96fdb1` and head `3d3683683b12e3753b11a28d106097383d116b48`; all five file hunks were matched to local git. No reporter retest was captured.

## Target evolution and semantic changes {#target-evolution-and-semantic-changes}

- `8a6b6725` changes x/y/z from raw float strings to zero-decimal rounded formatting, and replaces explicit __str__ calls with str. This affects visible coordinates.
- `bca16e2c` is only version0.0.2 and newline maintenance.
- `aa64d3a6` changes `get_new_scoreboard` to `create_scoreboard`. This is the precise missing-method repair later implicated by issue2. Its subject says upcoming API changes; it is not a response to the later issue itself.
- `a02d4414` replaces many nested provider functions with lambdas, centralizes `str(provider(player))`, widens registration to Callable returning Any and replaces wildcard scoreboard import with explicit names. The old coordinate expression rounds; the new `int(location)` truncates toward zero. For example +1.8 becomes1 instead of2, and -1.8 becomes-1 instead of-2. These examples explain language semantics, not executed upstream tests.
- The same refactor changes the game mode access from `p.game_mode` to `p.gamemode`, an apparent attribute typo. Since every provider is eagerly evaluated even when a format string does not use it, one bad provider can affect all sidebar formatting.
- `4817841a` releases0.1.0, adds Vincent alongside daoge_cmd in authors and removes an obsolete template-repository publish gate.
- `3d368368` releases0.2.0, corrects the game-mode attribute, retains `gamemode` as an alias while documenting `game_mode`, adds date/time/datetime and replaces numeric time components with strftime. Month/day/hour/minute/second gain zero-padding, while `%x/%X/%c` are locale-sensitive. Both English and Chinese documentation are updated. Release workflow now builds both sdist/wheel, attaches the wheel to GitHub release and publishes to PyPI.

## Constraints and costs visible in unchanged code {#constraints-and-costs-visible-in-unchanged-code}

`replace_placeholder` evaluates the entire provider dictionary for the title and again for every content line. Central string conversion makes provider implementations shorter and supports non-string values, but does not make evaluation lazy. Unknown keys or malformed braces passed to str.format raise; configuration indexing has no explicit validation/fallback. Recreating the objective each update is simple but may introduce work or display churn. No benchmark/flicker evidence is provided, so those remain costs to investigate, not measured regressions.

The registration annotation changes to Any while the stored dict annotation still says returns str. This is a type-documentation inconsistency rather than a runtime enforcement mechanism. The selected reviewed commits do not add disable cleanup, objective ownership reconciliation with other plugins or handling for repeated identical display lines. Do not infer those guarantees from successful source migration.

## What the evidence supports {#what-the-evidence-supports}

The issue's missing-method path is concretely replaced, the typo is repaired in the final release, and aliases preserve old config spelling. It does not establish a successful reporter retest or semantic preservation of the whole refactor. Release version labels are not a substitute for examining the full patch.

Use this case for API upgrade diagnosis, config-compatible renaming, callback registry simplification and review of “refactor” changes. Before adopting, specify coordinate rounding semantics, locale/time format expectations, malformed config behavior, eager versus lazy providers, existing-player reload, duplicate lines and interaction with another scoreboard owner. Those are proposed checks, not tests performed here.

## Provenance {#provenance}

[Per-commit source index](../repositories/sidebar-source-index.md) covers the six selected revisions. See the [related issue dossier](../../../thread-review/threads/dossiers/endstone-essentials__sidebar-2.md), [public issue](https://github.com/endstone-essentials/sidebar/issues/2), and [refactor commit](https://github.com/endstone-essentials/sidebar/commit/a02d4414ca0577a478bad5d646e8cf512ccd874f).
