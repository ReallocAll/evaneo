<!-- retrieval: {"source_ids":["public:commit:3d3683683b12e3753b11a28d106097383d116b48","public:commit:4817841a0b26ee47f84c20bf00adf08ef476c010","public:commit:8a6b67255abb9bb28ec8ddc34fe339ff076f89a8","public:commit:a02d4414ca0577a478bad5d646e8cf512ccd874f","public:commit:aa64d3a6efb662a9fad24c93da31ef3cbd05f1ac","public:commit:bca16e2c663297604086514ce61a906dfa8f84c1"],"source_type":"public","date":"2024-05-24..2026-07-12","topics":["api","refactoring"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstone-essentials-sidebar-source-index"></a>
# endstone-essentials/sidebar source index {#endstone-essentials-sidebar-source-index}

Each entry links to a public commit. Read the linked case before applying a change elsewhere.

<a id="1-8a6b67255abb9bb28ec8ddc34fe339ff076f89a8"></a>
## 1. 8a6b67255abb9bb28ec8ddc34fe339ff076f89a8 {#1-8a6b67255abb9bb28ec8ddc34fe339ff076f89a8}

[refactor: improve placeholder](https://github.com/endstone-essentials/sidebar/commit/8a6b67255abb9bb28ec8ddc34fe339ff076f89a8)

Disposition: substantive.

Changes coordinate display from raw float string to rounded zero-decimal formatting, replaces direct __str__ calls with str. Initial registry/update architecture is daoge_cmd context. Rounding is an observable choice later reversed to truncation.

Case: SIDEBAR01.

<a id="2-bca16e2c663297604086514ce61a906dfa8f84c1"></a>
## 2. bca16e2c663297604086514ce61a906dfa8f84c1 {#2-bca16e2c663297604086514ce61a906dfa8f84c1}

[chore: 0.0.2 is next](https://github.com/endstone-essentials/sidebar/commit/bca16e2c663297604086514ce61a906dfa8f84c1)

Disposition: mechanical.

Bumps 0.0.1 to 0.0.2 and adds final newline; no behavior change.

Case: SIDEBAR01.

<a id="3-aa64d3a6efb662a9fad24c93da31ef3cbd05f1ac"></a>
## 3. aa64d3a6efb662a9fad24c93da31ef3cbd05f1ac {#3-aa64d3a6efb662a9fad24c93da31ef3cbd05f1ac}

[fix: accommodate upcoming API changes](https://github.com/endstone-essentials/sidebar/commit/aa64d3a6efb662a9fad24c93da31ef3cbd05f1ac)

Disposition: substantive.

Replaces removed server.get_new_scoreboard with create_scoreboard for joining players. Exact API change later matches reported AttributeError in issue2; no reporter retest in captured thread.

Case: SIDEBAR01.

<a id="4-a02d4414ca0577a478bad5d646e8cf512ccd874f"></a>
## 4. a02d4414ca0577a478bad5d646e8cf512ccd874f {#4-a02d4414ca0577a478bad5d646e8cf512ccd874f}

[refactor: simplify placeholder registration using lambdas](https://github.com/endstone-essentials/sidebar/commit/a02d4414ca0577a478bad5d646e8cf512ccd874f)

Disposition: substantive.

Replaces nested provider functions with lambdas, coerces results centrally to str and widens callback type to Any; explicit scoreboard imports replace wildcard. Coordinates change rounding to int truncation; gamemode accidentally accesses p.gamemode instead of p.game_mode. This is not semantic-preserving formatting.

Case: SIDEBAR01.

<a id="5-4817841a0b26ee47f84c20bf00adf08ef476c010"></a>
## 5. 4817841a0b26ee47f84c20bf00adf08ef476c010 {#5-4817841a0b26ee47f84c20bf00adf08ef476c010}

[chore: bump version to 0.1.0](https://github.com/endstone-essentials/sidebar/commit/4817841a0b26ee47f84c20bf00adf08ef476c010)

Disposition: substantive.

Bumps to0.1.0, adds Vincent while preserving daoge_cmd authorship, removes stale template-repository gate so publish job can run for this repository. No run result inspected.

Case: SIDEBAR01.

<a id="6-3d3683683b12e3753b11a28d106097383d116b48"></a>
## 6. 3d3683683b12e3753b11a28d106097383d116b48 {#6-3d3683683b12e3753b11a28d106097383d116b48}

[chore: bump version to 0.2.0](https://github.com/endstone-essentials/sidebar/commit/3d3683683b12e3753b11a28d106097383d116b48)

Disposition: substantive.

0.2.0 release adds wheel asset upload, date/time/datetime placeholders and zero-padded strftime components; corrects game_mode attribute while retaining gamemode alias. Updates English/Chinese docs; unchanged update loop rebuilds objective and evaluates every provider for every formatted line.

Case: SIDEBAR01.
