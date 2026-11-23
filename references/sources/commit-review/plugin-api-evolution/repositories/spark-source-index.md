<!-- retrieval: {"source_ids":["public:commit:23f9839b16e600c08c409889a9298347d776eb16","public:commit:316b5acf307af522041ff091280398b7970e9ba8","public:commit:4c53cc0e0d0451697769c0ae37a2848adb50fe47","public:commit:8cc11d8a26a7088f3943f260f0266d14d3b00d5e"],"source_type":"public","date":"2024-05-24..2026-07-12","topics":["ffi","build","documentation","networking"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-spark-source-index"></a>
# EndstoneMC/spark source index {#endstonemc-spark-source-index}

Each entry links to a public commit. Read the linked case before applying a change elsewhere.

<a id="1-4c53cc0e0d0451697769c0ae37a2848adb50fe47"></a>
## 1. 4c53cc0e0d0451697769c0ae37a2848adb50fe47 {#1-4c53cc0e0d0451697769c0ae37a2848adb50fe47}

[Initial commit: endstone-spark, a spark-style native profiler for BDS](https://github.com/EndstoneMC/spark/commit/4c53cc0e0d0451697769c0ae37a2848adb50fe47)

Disposition: substantive_with_imported_schema.

Initial implementation has independent core, platform capture, queues/tick aggregation, module+RVA identities, deferred symbolization, manual protobuf writer, system metrics, plugin commands and background export. Source explicitly credits lucko/spark for protocol/viewer and marks Windows unexercised; schemas are declared vendored. Detailed static risks and test limitations retained in SPARK01-SPARK03; no execution or upload performed.

Case: SPARK01, SPARK02, SPARK03.

<a id="2-23f9839b16e600c08c409889a9298347d776eb16"></a>
## 2. 23f9839b16e600c08c409889a9298347d776eb16 {#2-23f9839b16e600c08c409889a9298347d776eb16}

[docs: frame as a native port of spark to Endstone](https://github.com/EndstoneMC/spark/commit/23f9839b16e600c08c409889a9298347d776eb16)

Disposition: documentation.

Reframes README from spark-style to native port and strengthens explicit lucko/spark format/protocol/viewer credit; argument-parser comment follows terminology. This is positioning/attribution, not new runtime capability.

Case: SPARK03.

<a id="3-8cc11d8a26a7088f3943f260f0266d14d3b00d5e"></a>
## 3. 8cc11d8a26a7088f3943f260f0266d14d3b00d5e {#3-8cc11d8a26a7088f3943f260f0266d14d3b00d5e}

[build: use conanfile.txt instead of conanfile.py](https://github.com/EndstoneMC/spark/commit/8cc11d8a26a7088f3943f260f0266d14d3b00d5e)

Disposition: substantive.

Replaces Python Conan recipe with declarative conanfile.txt preserving four dependency versions and libunwind requirement. Explicit comment ties libunwind to signal-safe capture; recipe-level fPIC option/default is removed while spark_core retains CMake POSITION_INDEPENDENT_CODE.

Case: SPARK03.

<a id="4-316b5acf307af522041ff091280398b7970e9ba8"></a>
## 4. 316b5acf307af522041ff091280398b7970e9ba8 {#4-316b5acf307af522041ff091280398b7970e9ba8}

[docs: add GPLv3 LICENSE (matching spark)](https://github.com/EndstoneMC/spark/commit/316b5acf307af522041ff091280398b7970e9ba8)

Disposition: standard_license.

Adds GPLv3 text, exactly byte-equal to local /usr/share/common-licenses/GPL-3. Commit explicitly says matching spark. Standard legal text is proportionately verified, not treated as 674 lines of novel engineering reasoning.

Case: SPARK03.
