<!-- retrieval: {"source_ids":["public:commit:9d16275dd60ec2fa945ceadb6c4581ccd21872d7","public:commit:f2e5dc41dc1503ac2cf6126363ae241a3741d605"],"source_type":"public","date":"2026-02-25","topics":["testing","build","api","documentation","review","selection","refactoring","networking"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="rn04-large-changes-need-provenance-accounting-before-engineering-interpretation"></a>
# Large changes need provenance accounting before engineering interpretation {#rn04-large-changes-need-provenance-accounting-before-engineering-interpretation}

## Why line counts mislead here {#why-line-counts-mislead-here}

The selected RakNet history contains roughly a million full diff lines, largely because of old generated project files, vendor trees, documentation and tree reorganization. Treating those lines as a million lines of new transport engineering would distort both attribution and review effort. Conversely, calling every large change mechanical from its title would miss language-level changes, default options, dependency replacements and rewritten tests.

The original review used guarded diffs and a finite structural audit before semantic reading. Its path-level comparison tracked old/new blob IDs, CRLF-normalized hashes, exact-move or residual dispositions, and upstream-boundary equivalent paths where relevant. The audit records are not distributed with this Skill; the summaries below can be checked selectively against linked public history. Exact moves use identical blobs; CRLF-only moves use identical normalized bytes. Only specific substitutions such as the minimum-CMake version sweep receive dedicated normalization. General whitespace or token comparisons are not treated as proof of equivalent C++ behavior.

<a id="verified-bulk-and-local-exceptions"></a>
## Verified bulk and local exceptions {#verified-bulk-and-local-exceptions}

The main source/header/sample migration007 has471 exact blob moves and444 CRLF-only moves; its meaningful sample-index and build-wiring residuals are read separately. Test relocation012 has99 exact moves. The libcat move021 has239 exact moves, and extension reorganization023 has402. File movement therefore does not confer authorship of the moved algorithms.

The original path-level comparison reported:
- All17 deleted solution files in005 match the upstream boundary.
- All181 vcproj files in013 and23 DSP files in017 match upstream content after the documented normalization.
- Of1,148 vendor removals in021,1,144 match upstream; four local CMake integration files are separately read and identified.
- All1,215 Help files in028 match upstream, including the generated Doxygen bulk. The meaningful new documentation and deletion decision are reviewed separately.
- The old XML parser source/header removed in025 match upstream; its local CMake placeholder and new pugixml call sites are distinct deltas.
- Retired dependency-discovery modules in016 are mostly upstream helpers; two local replacement/comment files are separately identified.

This reports the original path-level disposition without pretending to have semantically reread every removed compression routine, generated Visual Studio XML field, binary image or Doxygen page. Those old algorithms are not used to infer contemporary preferences. The linked public commit history remains available for targeted reinspection.

## Attribution survives simplification {#attribution-survives-simplification}

The repository retains Oculus BSD-style license/patent provenance. A formatting change to LICENSE does not erase its conditions or make all inherited work local authorship. The XML parser removal separately names Frank Vanden Berghen/Business-Insight and its prior license terms. libcat remains vendor code even after its new third_party path. The2015 upstream merge is an ancestry boundary, not a reviewed commit or an eligible contemporary style example.

Many modernization messages include Co-Authored-By: Claude Opus4.6. Public commit messages preserve the original trailers; the bundled per-SHA dossiers quote those relevant to each analysis. A trailer records declared coauthorship but does not allocate line-level ownership. No collaborator or review objection is inferred from a commit title. The documentation subreview separately distinguishes upstream manual content, changed examples, newly written guidance and changes to certainty of claims.

## Source limits and reusable method {#source-limits-and-reusable-method}

Mechanical disposition answers “what bytes moved or disappeared and where they came from.” Semantic review answers “what the new integration does and why.” Runtime validation is a third question that this task does not perform. Generated lockfiles and old project inventories are proportionately checked for their role and identity; their mere presence is not dependency-security or compatibility validation.

For a future third-party migration, preserve an exact path/blob manifest, isolate local integration deltas, verify known equivalences and then read every novel or changed mechanism. Use the upstream license and source identity as provenance, not as a reason to import another author's philosophy. Retain unexplained residuals until resolved; do not silently count them as read. This review leaves algorithmic bulk under explicit structural disposition and does not claim an independent vendor security audit.

Sources: bundled dossiers 001–028, including [021](../dossiers/021-9d16275dd60e.md) and [025](../dossiers/025-f2e5dc41dc15.md), and their linked public commits. The underlying structural, deletion-provenance and DAG audit files are not distributed. All comparisons were local read-only Git operations. No upstream source, build script, package installer or test program was executed.

## Exact commit navigation {#exact-commit-navigation}

- [021 9d16275dd60e: refactor: replace vendored third-party libs with Conan + find_package](../dossiers/021-9d16275dd60e.md) · [public source](https://github.com/wu-vincent/RakNet/commit/9d16275dd60ec2fa945ceadb6c4581ccd21872d7)
- [025 f2e5dc41dc15: refactor: replace bundled xmlParser with pugixml via Conan](../dossiers/025-f2e5dc41dc15.md) · [public source](https://github.com/wu-vincent/RakNet/commit/f2e5dc41dc1503ac2cf6126363ae241a3741d605)
