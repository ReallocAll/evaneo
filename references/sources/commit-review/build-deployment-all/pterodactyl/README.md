<!-- retrieval: {"source_ids":["public:commit:07d9dbc96a6fe5403eb8ee885d521326e623df5d","public:commit:0f59fec50545f71df149afbaaa56ee2f9db3b3e4","public:commit:1e8a2ea06238a93cfaa6588756409d7791ffe432","public:commit:23577f1b6a679b6ce0a74b5f375221ed2425c5ea","public:commit:2be7388206d05e929ce606694592a926c876444b","public:commit:3055d5155cb44e02e7bc507feb8019e65c05eadb","public:commit:34c34d9bb52b20e0882a7808e8238a6e35f75add","public:commit:3ab4f7f6fe4d570722376795f004790796420a99","public:commit:448ef25f5def9cae016b03ea4816bcd8ebd44cbf","public:commit:4a01201ba3f17f8b1d0ed4483c2071a3c1417304","public:commit:55594291d306952777e698ecd9d8b0ec178b2927","public:commit:6a3cd2d7c6821cedb55d1689983c67780e58da51","public:commit:6fdaa65ee8da79b17a42caae42612288be39e19f","public:commit:852226c7ab5938b9d33184bdc1ad8fcc44767847","public:commit:8689ffc3df2d1786a034263e5bc5bc41c8d2d3b2","public:commit:875f2eb73f37c55b7096d9ca353c9b71d89c28e9","public:commit:8780ad2a2fd34640e90ab87d064b2b91cc3a8ffd","public:commit:a2962a55b3288ed260a5893c9fc15d82d4805669","public:commit:b3c4e526d43f4353f2b75ed1fa0db6de5deb0005","public:commit:b54ccc805c2093b828aa93ef58600f9771d5da5f","public:commit:b85323b9e6b62127eced58dcc3e6c1d89733e7d3","public:commit:c38cfc4eb3582a544e53efa834332fe9401d66d4","public:commit:c4c9e96ccf8c8399cf3ca11d506f119927782228","public:commit:d1df88cb99a7f22cc69dcc0cdba8f941fa801833","public:commit:d64f026bb90a701513eb38866c91a16428494d97","public:commit:eb1b540c0623a276c65f2739d9468f1515eb6f9c","public:commit:fa73ce733e313ad18205098338401bad682b7861","public:commit:fe3948630dafefa54e46938f6826f4f435942907","public:commit:ff222bf4e636bb7b4b20413944854186ce169848"],"source_type":"public","date":"2024-05-13..2026-07-10","topics":["build","performance","recovery","api","diagnosis","documentation","selection","networking"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="hosting-deployment-panel-schema-shell-translation-and-operational-configuration"></a>
# Hosting deployment: panel schema, shell translation and operational configuration {#hosting-deployment-panel-schema-shell-translation-and-operational-configuration}

## Causal progression {#causal-progression}
The first design maintained four custom Python yolks and a daily/manual/main GHCR build workflow. It carried an adapted entrypoint credited to Matthew Penner. The initial Debian-based images nevertheless used Alpine-style user creation and ash, later changed uniformly to Debian useradd and bash. Custom yolks and their workflow were then removed, and the egg adopted parkervcp's maintained images. Reduced maintenance is a reasonable effect, but the change did not state why the custom route was abandoned.

The egg is an adapter across several contracts: PTDL_v2 JSON import, nested JSON strings for file parsing/startup readiness, image entrypoint placeholder rewriting, shell evaluation, Python package resolution, and Endstone's server directory. Changes 11–15 repeatedly synchronize installer destination, panel-managed properties path and Endstone's -s argument. One intermediate subdirectory change omitted mkdir; the next change supplies it. The eventual root directory mode uses && from pip upgrade through install to module launch, while the early form used a semicolon before launch. Preserving an existing properties file avoids overwriting operator configuration, although no migration mechanism upgrades those existing files.

Version input first supported latest or a numeric pin, then became a full pip requirement, then became an optional bare version. Direct URLs and uploaded wheel filenames were explicitly documented during the full-requirement phase. Later SERVER_WHLFILE restored that flexibility as a separate higher-priority override. This simplifies the common input while keeping development artifacts possible, but it changes old field semantics; no automatic migration is shown. Restarting with a blank version now asks pip for latest. Version pinning controls selection, but it is not by itself a rollback plan: persistent world/plugin compatibility, downloaded server state and prior artifact availability still need separate treatment.

## The important failure boundary {#the-important-failure-boundary}
The validator checks import-time structure and nested JSON parseability, reserved names and basic types, aggregating errors in CI. It is explicitly based on Pterodactyl's EggImporterService, which remains upstream's work. It is not a runtime validator. A later nested shell expression creates adjacent closing braces. The container entrypoint's {{...}}→shell translation collapses those braces, and the changelog explicitly reports servers failed to start. Splitting the package expression into PKG avoids nesting at the entrypoint transformation boundary. Passing JSON validation could never establish correctness at that second parser. Reproducing the whole panel/entrypoint/shell pipeline is the relevant future test, not merely parsing egg-endstone.json.

The final installer uses a prebuilt Alpine installer rather than provisioning curl in a Python image. curl -fL and a user agent improve declared download handling, but the script lacks set -e and ends in a success message, so failure propagation remains an untested concern. Quiet pip flags reduce console noise but do not substitute for diagnostics.

## Defaults, support and evidence limits {#defaults-support-and-evidence-limits}
server.properties is read as an upstream-derived operating template. The refreshed transport, UDP mapping and strict movement options expose genuine network/deployment constraints. Commented diagnostic, watchdog and profiling settings document possibilities rather than activating them. The chunk-generation false change is later reversed by a default refresh; there is no enduring preference or performance conclusion to infer. Offered Python versions narrow to 3.11–3.14. The CalVer changelog records input migration, platform changes and startup failure cause; its quicker-install claim has no timing data here. Every target diff and message is covered locally, including exact rename identity. No panel import, installation, shell execution, package download, benchmark or rollback was run.

## Complete per-SHA navigation {#complete-per-sha-navigation}

- [01 a2962a55b328 — Initial commit](dossiers/01-a2962a55b3288ed260a5893c9fc15d82d4805669.md)
- [02 b85323b9e6b6 — feat: add Dockerfile and entrypoint.sh for yolk](dossiers/02-b85323b9e6b62127eced58dcc3e6c1d89733e7d3.md)
- [03 fe3948630daf — feat: add .gitignore](dossiers/03-fe3948630dafefa54e46938f6826f4f435942907.md)
- [04 2be7388206d0 — feat: add build yolks workflow](dossiers/04-2be7388206d05e929ce606694592a926c876444b.md)
- [05 fa73ce733e31 — feat: update yolk.yml](dossiers/05-fa73ce733e313ad18205098338401bad682b7861.md)
- [06 b54ccc805c20 — feat: add yolks for Python 3.9, 3.10, 3.11](dossiers/06-b54ccc805c2093b828aa93ef58600f9771d5da5f.md)
- [07 448ef25f5def — feat: update Dockerfiles and entrypoint.sh](dossiers/07-448ef25f5def9cae016b03ea4816bcd8ebd44cbf.md)
- [08 b3c4e526d43f — feat: add egg-endstone.json](dossiers/08-b3c4e526d43f4353f2b75ed1fa0db6de5deb0005.md)
- [09 1e8a2ea06238 — feat: add server.properties](dossiers/09-1e8a2ea06238a93cfaa6588756409d7791ffe432.md)
- [10 d1df88cb99a7 — refactor: remove custom yolks](dossiers/10-d1df88cb99a7f22cc69dcc0cdba8f941fa801833.md)
- [11 eb1b540c0623 — feat: update egg-endstone.json](dossiers/11-eb1b540c0623a276c65f2739d9468f1515eb6f9c.md)
- [12 c4c9e96ccf8c — feat: update egg-endstone.json](dossiers/12-c4c9e96ccf8c8399cf3ca11d506f119927782228.md)
- [13 c38cfc4eb358 — feat: update egg-endstone.json](dossiers/13-c38cfc4eb3582a544e53efa834332fe9401d66d4.md)
- [14 0f59fec50545 — feat: update server.properties](dossiers/14-0f59fec50545f71df149afbaaa56ee2f9db3b3e4.md)
- [15 55594291d306 — Update egg-endstone.json](dossiers/15-55594291d306952777e698ecd9d8b0ec178b2927.md)
- [16 ff222bf4e636 — Update egg-endstone.json](dossiers/16-ff222bf4e636bb7b4b20413944854186ce169848.md)
- [17 23577f1b6a67 — Update server.properties](dossiers/17-23577f1b6a679b6ce0a74b5f375221ed2425c5ea.md)
- [18 6a3cd2d7c682 — Overhaul Pterodactyl egg repo for hosting providers](dossiers/18-6a3cd2d7c6821cedb55d1689983c67780e58da51.md)
- [19 852226c7ab59 — Document installing Endstone from URL or local .whl file](dossiers/19-852226c7ab5938b9d33184bdc1ad8fcc44767847.md)
- [20 8689ffc3df2d — Replace 'install' with 'run' in version docs](dossiers/20-8689ffc3df2d1786a034263e5bc5bc41c8d2d3b2.md)
- [21 3ab4f7f6fe4d — Add egg JSON validator based on Pterodactyl panel rules](dossiers/21-3ab4f7f6fe4d570722376795f004790796420a99.md)
- [22 8780ad2a2fd3 — Rename validate_egg.py to validate.py](dossiers/22-8780ad2a2fd34640e90ab87d064b2b91cc3a8ffd.md)
- [23 07d9dbc96a6f — Default to latest endstone and accept bare version pin](dossiers/23-07d9dbc96a6fe5403eb8ee885d521326e623df5d.md)
- [24 34c34d9bb52b — Update server.properties to latest BDS defaults](dossiers/24-34c34d9bb52b20e0882a7808e8238a6e35f75add.md)
- [25 3055d5155cb4 — Add SERVER_WHLFILE variable to install endstone from a local wheel](dossiers/25-3055d5155cb44e02e7bc507feb8019e65c05eadb.md)
- [26 6fdaa65ee8da — Drop Python 3.10 support and document ENDSTONE_VERSION/SERVER_WHLFILE](dossiers/26-6fdaa65ee8da79b17a42caae42612288be39e19f.md)
- [27 d64f026bb90a — Fix startup brace collapse and switch install to alpine installers image](dossiers/27-d64f026bb90a701513eb38866c91a16428494d97.md)
- [28 875f2eb73f37 — Quiet pip and skip user script-location warning in startup](dossiers/28-875f2eb73f37c55b7096d9ca353c9b71d89c28e9.md)
- [29 4a01201ba3f1 — Add CHANGELOG following Keep a Changelog with CalVer](dossiers/29-4a01201ba3f17f8b1d0ed4483c2071a3c1417304.md)
