<!-- retrieval: {"source_ids":["public:commit:f3a696cc01d7438a7bcbab1c37a93df14dff4d35"],"source_type":"public","date":"2026-10-12","topics":["concurrency","ffi","testing","build","recovery","api","selection"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="tests-and-source-navigation"></a>
# Tests and source navigation {#tests-and-source-navigation}

These are source assertions, not executed outcomes. All 111 test function definitions in five files were read; decorators can expand cases, so this is not a collected/passed test count. No upstream module import, compiler, server, bot or test command was run. Synthetic console fixtures are explicitly distinct from live observations.

## What each module establishes by construction {#what-each-module-establishes-by-construction}

### tests/unit/test_adapter_nukkit.py {#tests-unit-testadapternukkit-py}

17 static functions. Synthetic JAR/config/runtime and monkeypatched helper build. Contract, dialect fixtures, install/config categories, watcher variant, JVM/native/Docker command construction, one-shot jcmd/fallback, effects/chaos, catalogs and helper manifest. Optional javac test compiles a trivial demo twice, not the real helper against the pinned API.

### tests/unit/test_adapter_pocketmine.py {#tests-unit-testadapterpocketmine-py}

18 static functions. Synthetic raw/deflated PHARs and fake runtimes. Member extraction/missing/corrupt CRC, adapter dialect, copied helper/defaults, fresh/config provenance/readback, stock memory, nonempty-directory refusal, native PHP extension/environment and Docker arguments, command support and catalog checks.

### tests/unit/test_adapter_powernukkitx.py {#tests-unit-testadapterpowernukkitx-py}

13 static functions. Fake release/runtime and synthetic template. Metadata/dialect/version normalization, fresh world db boundary/all seeds, semantic YAML and JSON readback changes, preserved template config/missing-template refusal, JVM arguments, effects/chaos and catalog.

### tests/unit/test_adapter_standalone.py {#tests-unit-testadapterstandalone-py}

38 static functions. Narrow YAML scalar/editor behavior and types; config schema/default/variant/duplicate/reason/placeholder validation; every committed plan renders; semantic readback; tar executable/symlink/escape cases; archive dispatch; local fake pinned-runtime/cache/release behavior; local artifact adoption; deterministic ZIP; position block completeness; jcmd/heap/runtime-release parsers.

### tests/unit/test_pregen.py {#tests-unit-testpregen-py}

25 static functions. Geometry/world key/report serialization, count and coverage rejection, read-only template store/tree and world mutation detection, missing reports, synthetic helper lines/completion timeout, stop cleanup including force-kill, fake clock/bot-row tour success/stall/retry/death/max dwell, scenario derivation, latest rows and CLI refusal/reuse. No real build_template/save/restart pipeline executed; forced stop is not asserted invalid.

## Cross-cutting limits worth retaining {#cross-cutting-limits-worth-retaining}

- Nukkit install tests replace the helper build with bytes. The optional reproducibility test finds `javac` on PATH, skips if absent, and compiles a trivial class; it does not compile the real helper or prove API compatibility. The tool search does not independently guarantee that a found compiler supports release 21.
- PocketMine PHAR fixtures cover the parser subset, not actual release signature/runtime loading. Java/PHP catalog entries are source data and fixture checks, not downloaded artifact availability proofs.
- JVM tests mock tool output and thread lists. They cannot establish native attachment permissions, OS thread behavior or sampling accuracy.
- Pregen fake-console tests immediately append supplied lines. FakeTourWorld advances a simulated clock and manufactures counts from rate/cap, so no network, engine generation, crash recovery or filesystem durability is established.
- The stop test expects a force-kill when the fake process does not stop. It does not assert that an otherwise coverage-complete template is rejected after that kill.
- Store/verify tests prove the intended rejection of changed bytes, different world parameters and poor recorded coverage. They do not independently establish unique/correct cell coordinates, exact expected counts, current-scenario coverage thresholds, adapter identity or a cleanly saved/restartable world.
- The CLI reuse test uses a synthetic report whose embedded version comes from its helper default; reuse does not assert server/version identity equality.
- Shared archive tests cover simple traversal/absolute/link escape cases and normal platform paths, not every archive/link/platform combination.
- Fixture/global-contract checks can show internal consistency between adapter and authored expectations. They cannot turn feature declarations into observed cross-engine behavior.

## Exact changed-file coverage {#exact-changed-file-coverage}

Every path below was new in this commit and read in full. Patch ranges refer to the logical numbered lines in the full guarded patch, excluding its JSON header. All 35 reconstructed source contents matched the `index` Git blob identities. The 70 nonsemantic mode/index lines omitted from the reduced view were also inspected.

| Path | Source lines | Full patch lines |
| --- | ---: | ---: |
| `artifacts/nukkit.toml` | 18 | 1–24 |
| `artifacts/pocketmine.toml` | 16 | 25–46 |
| `artifacts/powernukkitx.toml` | 17 | 47–69 |
| `artifacts/runtimes.toml` | 51 | 70–126 |
| `docs/servers/nukkit.md` | 148 | 127–280 |
| `docs/servers/pocketmine.md` | 136 | 281–422 |
| `docs/servers/powernukkitx.md` | 126 | 423–554 |
| `features/nukkit.toml` | 33 | 555–593 |
| `features/pocketmine.toml` | 32 | 594–631 |
| `features/powernukkitx.toml` | 33 | 632–670 |
| `matrices/cross-server.toml` | 55 | 671–731 |
| `servers/nukkit/config.toml` | 46 | 732–783 |
| `servers/nukkit/plugin/plugin.yml` | 30 | 784–819 |
| `servers/nukkit/plugin/src/bench/BenchTick.java` | 154 | 820–979 |
| `servers/nukkit/plugin/src/bench/PreGen.java` | 201 | 980–1186 |
| `servers/pocketmine/config.toml` | 44 | 1187–1236 |
| `servers/pocketmine/plugins/BenchHelper.php` | 76 | 1237–1318 |
| `servers/powernukkitx/config.toml` | 31 | 1319–1355 |
| `servers/powernukkitx/world-config.json` | 54 | 1356–1415 |
| `src/bedrock_bench/adapters/nukkit.py` | 288 | 1416–1709 |
| `src/bedrock_bench/adapters/pocketmine.py` | 292 | 1710–2007 |
| `src/bedrock_bench/adapters/powernukkitx.py` | 167 | 2008–2180 |
| `src/bedrock_bench/adapters/standalone.py` | 1007 | 2181–3193 |
| `src/bedrock_bench/pregen.py` | 621 | 3194–3820 |
| `tests/fixtures/logs/nukkit-session.log` | 24 | 3821–3850 |
| `tests/fixtures/logs/nukkit.toml` | 52 | 3851–3908 |
| `tests/fixtures/logs/pocketmine-session.log` | 30 | 3909–3944 |
| `tests/fixtures/logs/pocketmine.toml` | 52 | 3945–4002 |
| `tests/fixtures/logs/powernukkitx-session.log` | 19 | 4003–4027 |
| `tests/fixtures/logs/powernukkitx.toml` | 42 | 4028–4075 |
| `tests/unit/test_adapter_nukkit.py` | 339 | 4076–4420 |
| `tests/unit/test_adapter_pocketmine.py` | 322 | 4421–4748 |
| `tests/unit/test_adapter_powernukkitx.py` | 268 | 4749–5022 |
| `tests/unit/test_adapter_standalone.py` | 461 | 5023–5489 |
| `tests/unit/test_pregen.py` | 372 | 5490–5867 |

## Test function inventory {#test-function-inventory}

Source line ranges below are within each named upstream file. Every body was read, including assertions and fixtures; this inventory is navigation rather than a substitute for reading.

### tests/unit/test_adapter_nukkit.py {#tests-unit-testadapternukkit-py-2}

- `test_build_plugin_is_reproducible`: 310–325
- `test_build_plugin_needs_sources`: 328–331
- `test_helper_sources_are_committed`: 334–339
- `test_registered`: 112–118
- `test_pins`: 120–124
- `test_dialect_samples`: 126–147
- `test_session_log`: 149–154
- `test_install_layout`: 158–162
- `test_configs_and_overrides`: 164–189
- `test_no_watchdog_variant`: 191–197
- `test_launch`: 199–214
- `test_docker_launch`: 216–220
- `test_tick_thread_from_jcmd`: 222–242
- `test_tick_thread_when_jcmd_fails`: 244–255
- `test_effects_and_helper_commands`: 259–265
- `test_chaos_dialect`: 267–285
- `test_every_catalogue_command_is_rendered_or_unsupported`: 287–296

### tests/unit/test_adapter_pocketmine.py {#tests-unit-testadapterpocketmine-py-2}

- `test_registered`: 122–129
- `test_pins`: 131–136
- `test_dialect_samples`: 138–159
- `test_session_log`: 161–172
- `test_reads_a_member`: 177–180 (parameterized)
- `test_missing_member`: 182–185
- `test_corrupt_member`: 187–193
- `test_not_a_phar`: 195–198
- `test_install_layout`: 202–209
- `test_prepare_writes_configs_and_overrides`: 211–244
- `test_stock_variant_keeps_the_memory_limit`: 246–252
- `test_refuses_a_used_work_dir`: 254–259
- `test_launch_windows_layout`: 261–267
- `test_launch_with_extension_dir`: 273–283 (parameterized)
- `test_docker_launch`: 285–289
- `test_effects`: 293–300
- `test_chaos_dialect`: 302–311
- `test_every_catalogue_command_is_rendered_or_unsupported`: 313–322

### tests/unit/test_adapter_powernukkitx.py {#tests-unit-testadapterpowernukkitx-py-2}

- `test_registered`: 101–107
- `test_pins`: 109–113
- `test_dialect_samples`: 115–136
- `test_banner_version`: 145–146 (parameterized)
- `test_session_log`: 148–154
- `test_fresh_world`: 158–178
- `test_read_back_after_the_server_rewrote_its_config`: 180–191
- `test_template_world`: 193–216
- `test_template_scenario_needs_a_template`: 218–221
- `test_launch`: 223–235
- `test_positions_come_from_the_bots`: 239–243
- `test_chaos_dialect`: 245–257
- `test_every_catalogue_command_is_rendered_or_unsupported`: 259–268

### tests/unit/test_adapter_standalone.py {#tests-unit-testadapterstandalone-py-2}

- `test_deterministic_zip`: 400–406
- `test_scalars_by_path`: 66–72
- `test_quoted_values`: 74–76
- `test_replace_scalar_keeps_the_rest`: 78–82
- `test_replace_drops_an_inline_comment`: 84–86
- `test_replace_mapping_with_its_children`: 88–92
- `test_add_under_existing_parent_with_its_indentation`: 94–96
- `test_add_new_sections`: 98–102
- `test_cannot_nest_under_a_scalar`: 104–106
- `test_crlf_is_kept`: 108–110
- `test_values`: 117–118 (parameterized)
- `test_bad_values`: 121–123 (parameterized)
- `test_load`: 163–171
- `test_rejects`: 190–194 (parameterized)
- `test_properties_from_scratch`: 196–202
- `test_yaml_on_a_shipped_file`: 204–214
- `test_variant_pins`: 216–221
- `test_read_back`: 223–236
- `test_bad_placeholder`: 238–240
- `test_committed_plans_render`: 243–253 (parameterized)
- `test_extracts_and_marks_executables`: 279–285
- `test_relative_symlinks_inside_are_kept`: 288–291
- `test_refuses_escapes`: 302–305 (parameterized)
- `test_missing_executable`: 307–310
- `test_extract_archive_dispatch`: 312–319
- `test_runtime`: 373–380 (parameterized)
- `test_unpinned_runtime`: 382–384
- `test_release`: 386–391
- `test_local_release`: 393–397
- `test_complete_reply`: 415–423
- `test_incomplete_and_missing_replies_are_unknown`: 425–428
- `test_no_players`: 430–431
- `test_jdk21_format`: 435–441
- `test_old_hex_format`: 443–444
- `test_no_main_thread`: 446–448
- `test_heap`: 451–452 (parameterized)
- `test_bad_heap`: 454–456
- `test_java_release`: 458–461

### tests/unit/test_pregen.py {#tests-unit-testpregen-py-2}

- `test_disc`: 50–51 (parameterized)
- `test_cells_match_the_spread_grid`: 54–57
- `test_world_key`: 60–68
- `test_plugin_cells`: 151–163
- `test_plugin_pass`: 192–199
- `test_plugin_pass_without_a_finish_line`: 202–205
- `test_stop`: 228–232 (parameterized)
- `test_tour_covers_every_cell`: 283–292
- `test_tour_leaves_a_stalled_round`: 295–299
- `test_tour_retries_a_teleport_and_reports_a_bot_that_never_arrives`: 302–310
- `test_tour_stops_when_the_server_dies`: 313–317
- `test_tour_caps_the_dwell`: 320–323
- `test_tour_needs_bots`: 326–328
- `test_tour_scenario`: 331–336
- `test_latest_rows`: 339–346
- `test_cli_refuses_a_fresh_world_scenario`: 358–360
- `test_cli_keeps_a_valid_template`: 363–372
- `test_round_trip`: 72–77
- `test_problems`: 79–89
- `test_unknown_schema`: 91–93
- `test_store_and_verify`: 104–111
- `test_changed_tree_is_refused`: 113–122
- `test_other_world_parameters_are_refused`: 124–130
- `test_failed_validation_is_refused`: 132–138
- `test_missing_report`: 140–143
