<!-- retrieval: {"source_ids":["public:commit:12b20ed43e593c6dd8492a92e40d51b061fb2854","public:commit:353d644fc6bf333623ed347a3729ca0f35925109","public:commit:57f0dab3ba38f775604dfed863c5f9c696ab11a5","public:commit:5a142dd2a125ee67e78ab54e1fbcfd9998f2f88f","public:commit:6d154e5c8a4a0714c084cdc8fe699a92f6997df5","public:commit:8a3ef2811c11486e0b010bf50d5f720a9cdb7ed4","public:commit:a0c26748af85060240f890f614510767f0935c5a","public:commit:b6771a639077cafad2253c6606282d5bb4d04190","public:commit:c16d9d2f521f5a8620586e77642300184a54b262","public:commit:e0e739b61d8721046938d54ac0697e1ddd4652eb","public:commit:fa9d66e266d60ac991da86f7bbecb7dc07cde3c6","public:commit:fc23d7bdb219264ef97695a58db53a7f93834b74"],"source_type":"public","date":"2024-09-09..2024-09-10","topics":["ffi","testing","performance","api","documentation","review","selection","refactoring","networking"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
# Metrics, metadata normalization and literal logging {#metrics-metadata-normalization-and-literal-logging}


Endstone commits 1681–1800, dated August 29–September 14, 2024.

## Observability built from API surfaces {#observability-built-from-api-surfaces}

Metrics integration ties Python plugin-loader lifetime to an external bStats implementation. The local adapter supplies configuration-backed UUID and logging switches, service identity, server/Minecraft/Python versions, aggregate player platform/version counts and host OS/architecture/core count. Follow-on commits refine those analytical dimensions: Python drilldown, player-count line chart, clearer platform labels, amd64 normalization and physical rather than logical CPU count. These are small schema choices with concrete downstream interpretation, not independent grand design principles.

The implementation of endstone-bstats is outside this workunit. Its constructor scheduling, upload transport, persistent-config behavior and the meaning of MetricsConfig's positional true argument are not established by reading the adapter alone. Local aggregate maps do not prove the complete remote payload contains only those fields. No metrics transmission, package installation or host probe was performed. The destructor's shutdown call is observed, not a proof that every partial initialization or reload sequence terminates background work safely.

Client platform/version fields are reported connection metadata, with a server-version fallback for missing GameVersion. They improve practical visibility but are not authenticated client-environment evidence. Choosing psutil for physical cores adds a dependency and a possible unavailable-result case. No chart, benchmark or operational before/after measurement appears in this source chain.

## Data versus formatting and verified noise {#data-versus-formatting-and-verified-noise}

The Python logger repair is more than cosmetic: log(level,message) preserves braces as literal user text instead of interpreting them through formatting convenience methods. It is a precise boundary rule that can be reused when assessing language bindings. The patch does not repair every C++ logging call.

Ruff configuration and import sorting are treated proportionately. Eleven Python files have the same non-import AST and import multiset after normalizing a constant-only f-string. That verifies the intended formatting scope without claiming imports are universally side-effect-free. The generated stub is explicitly excluded from Ruff. All diffs were read before these mechanical proofs were used; hashes and AST extraction did not substitute for source review.

## Individual commit dispositions {#individual-commit-dispositions}

<a id="commit-1754"></a>
### Commit 1754 {#commit-1754}

2024-09-09T11:35:58Z · `8a3ef2811c11486e0b010bf50d5f720a9cdb7ed4` · fix(python): prevent format error when logging with curly brackets

Changes Python logger bindings from formatting convenience methods to log(level,message), so braces in user-provided text remain data rather than a format string. This is an explicit correctness boundary fix. It does not change every C++ logging call or add a regression assertion, and no logger execution was performed.

Source: [individual commit](https://github.com/EndstoneMC/endstone/commit/8a3ef2811c11486e0b010bf50d5f720a9cdb7ed4). Classification: literal_logging_fix.

<a id="commit-1755"></a>
### Commit 1755 {#commit-1755}

2024-09-09T14:56:29Z · `5a142dd2a125ee67e78ab54e1fbcfd9998f2f88f` · feat(player): improve `Player::getDeviceOS` to return clearer OS names

Maps internal device-platform enum labels to clearer names such as Android, Windows and PlayStation, and capitalizes Unknown. A source comment credits a Geyser DeviceOs file; that external file was not separately audited here. The values come from connection metadata, so readable naming is not verification of the client's actual platform.

Source: [individual commit](https://github.com/EndstoneMC/endstone/commit/5a142dd2a125ee67e78ab54e1fbcfd9998f2f88f). Classification: metadata_normalization.

<a id="commit-1756"></a>
### Commit 1756 {#commit-1756}

2024-09-09T15:02:36Z · `6d154e5c8a4a0714c084cdc8fe699a92f6997df5` · feat(metrics): add bStats integration

Adds endstone-bstats, constructs Metrics alongside the Python plugin loader and requests shutdown in its destructor. Local code supplies service ID, configuration-backed UUID/log flags, player aggregates and host/runtime versions. MetricsConfig receives a positional true argument, but its external implementation is not read here, so default consent, startup schedule and transport behavior remain dependencies rather than asserted facts. The integration adds lifecycle and dependency costs even for loading the server's Python support.

Source: [individual commit](https://github.com/EndstoneMC/endstone/commit/6d154e5c8a4a0714c084cdc8fe699a92f6997df5). Classification: telemetry_integration.

<a id="commit-1757"></a>
### Commit 1757 {#commit-1757}

2024-09-09T15:12:41Z · `e0e739b61d8721046938d54ac0697e1ddd4652eb` · refactor(version): remove leading 'v' from Minecraft version strings

Caches the native game version and removes an initial v for consumers such as metrics. This changes the public version string format, not the underlying supported binary. The code reads the first character without an explicit empty check; no observed empty native result or crash is claimed.

Source: [individual commit](https://github.com/EndstoneMC/endstone/commit/e0e739b61d8721046938d54ac0697e1ddd4652eb). Classification: version_normalization.

<a id="commit-1758"></a>
### Commit 1758 {#commit-1758}

2024-09-09T15:15:15Z · `353d644fc6bf333623ed347a3729ca0f35925109` · feat(player): add Player::getGameVersion to retrieve player's client version

Adds Player::getGameVersion and its Python property, taking GameVersion from connection data and falling back to the server version when empty. This enables subsequent client-version metrics. The fallback is an availability choice, not proof of the real client version, and no metadata-validation test is added.

Source: [individual commit](https://github.com/EndstoneMC/endstone/commit/353d644fc6bf333623ed347a3729ca0f35925109). Classification: client_metadata_api.

<a id="commit-1759"></a>
### Commit 1759 {#commit-1759}

2024-09-09T15:22:49Z · `a0c26748af85060240f890f614510767f0935c5a` · feat(metrics): add advanced pie chart for player game version tracking

Adds an AdvancedPie of client versions and simplifies the preceding metadata assignment branch without changing its fallback. Aggregation counts version labels rather than transmitting individual player identities in this local code. The actual external metrics payload and schedule are outside this unit's coverage.

Source: [individual commit](https://github.com/EndstoneMC/endstone/commit/a0c26748af85060240f890f614510767f0935c5a). Classification: metrics_extension.

<a id="commit-1760"></a>
### Commit 1760 {#commit-1760}

2024-09-09T16:00:18Z · `57f0dab3ba38f775604dfed863c5f9c696ab11a5` · feat(metrics): implement DrilldownPie for Python version

Changes Python-version reporting to an implementation/major-minor/full-version drilldown, and splits Windows release naming from build number while retaining the Linux kernel release. These are analytical-schema decisions supporting compatibility visibility. Other operating systems have no explicit branch, consistent with the project's bounded platform focus rather than proof of universal telemetry support.

Source: [individual commit](https://github.com/EndstoneMC/endstone/commit/57f0dab3ba38f775604dfed863c5f9c696ab11a5). Classification: metrics_schema_revision.

<a id="commit-1761"></a>
### Commit 1761 {#commit-1761}

2024-09-09T16:27:18Z · `fc23d7bdb219264ef97695a58db53a7f93834b74` · feat(metrics): add SingleLineChart for player amount

Moves player count from generic platform_data into a SingleLineChart. The count is still derived from the online-player collection. This is a chart/schema correction, with no independently measured effect on reporting or performance.

Source: [individual commit](https://github.com/EndstoneMC/endstone/commit/fc23d7bdb219264ef97695a58db53a7f93834b74). Classification: metrics_schema_revision.

<a id="commit-1763"></a>
### Commit 1763 {#commit-1763}

2024-09-09T19:20:11Z · `fa9d66e266d60ac991da86f7bbecb7dc07cde3c6` · feat(metrics): map 'x86_64' to 'amd64' for consistent OS architecture naming

Normalizes x86_64 to amd64 in metrics. The full change was read; it affects label consistency only and adds no separate platform support or architecture probing.

Source: [individual commit](https://github.com/EndstoneMC/endstone/commit/fa9d66e266d60ac991da86f7bbecb7dc07cde3c6). Classification: small_normalization.

<a id="commit-1765"></a>
### Commit 1765 {#commit-1765}

2024-09-09T20:38:05Z · `c16d9d2f521f5a8620586e77642300184a54b262` · feat: use psutil to get physical processor count instead of os.cpu_count

Adds psutil and switches from logical os.cpu_count to physical cpu_count(logical=False). The title explicitly requests physical processor counts. This improves the intended meaning of the chart at the cost of another dependency; the local adapter does not handle an unavailable count specially. No host probe or package installation was performed.

Source: [individual commit](https://github.com/EndstoneMC/endstone/commit/c16d9d2f521f5a8620586e77642300184a54b262). Classification: dependency_tradeoff.

<a id="commit-1766"></a>
### Commit 1766 {#commit-1766}

2024-09-10T11:44:01Z · `b6771a639077cafad2253c6606282d5bb4d04190` · refactor(metrics): simplify python verion in advanced pie

Removes the repeated interpreter implementation name from the drilldown's full-version leaf label. The parent grouping still contains implementation and major/minor version. This is display-schema cleanup, not a runtime compatibility change.

Source: [individual commit](https://github.com/EndstoneMC/endstone/commit/b6771a639077cafad2253c6606282d5bb4d04190). Classification: verified_mechanical.

<a id="commit-1768"></a>
### Commit 1768 {#commit-1768}

2024-09-10T12:06:48Z · `12b20ed43e593c6dd8492a92e40d51b061fb2854` · style: apply code formatting to python codes

Adds Ruff settings for 120-column lines, import sorting and generated-stub exclusion, and reformats/import-sorts eleven Python files. Static AST comparison proves unchanged non-import syntax after constant-only f-string normalization and the same import multiset. Import order can have side effects in principle, so no runtime equivalence is asserted merely from that proof. The tooling policy change is retained separately from formatting noise.

Source: [individual commit](https://github.com/EndstoneMC/endstone/commit/12b20ed43e593c6dd8492a92e40d51b061fb2854). Classification: verified_format_with_config.

## Coverage boundary {#coverage-boundary}

Findings rely on the linked public sources; external PR/issue discussions, dependencies, and native engine internals are outside the cited evidence. Runtime and current-release behavior were not tested.
