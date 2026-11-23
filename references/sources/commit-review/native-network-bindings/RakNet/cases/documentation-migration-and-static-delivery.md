<!-- retrieval: {"source_ids":["public:commit:01518f1d77f9a06a76042d4760ddbe977c773089","public:commit:076213f71493e840dc71ce87ef7662b8e1e36b5a","public:commit:08a3147faba92f823da810f33925cd60e4a93a37","public:commit:1b4af017155a9393226c0a314f7e51fa8b0ba3b9","public:commit:25e275ddc5ff67914b2ae3a9e84efa73e28addd0","public:commit:4704e4a97c10b776756ba0d746b9f49e44a63bb9","public:commit:4e7570cfd193c0192c9bd073e9592308a1680a1c","public:commit:81af283838a548411193960fc216e765e8adaa07","public:commit:9fb1c02bb570f8ad57ef177dd11f045f8d606712","public:commit:aa5646684c90d901327baec06a6812e2870a8916","public:commit:b173bf2182679d9a947d237cd1f74661707160db","public:commit:dc0c2ad6a72fc9a9927ee83228128624e50f653c"],"source_type":"public","date":"2026-02-24..2026-02-27","topics":["ffi","build","api","documentation","review","selection","refactoring","networking"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="rn02-modern-documentation-needs-both-content-provenance-and-serving-model-checks"></a>
# Modern documentation needs both content provenance and serving-model checks {#rn02-modern-documentation-needs-both-content-provenance-and-serving-model-checks}

## The engineering sequence {#the-engineering-sequence}

Commits 014/015 introduce a Fumadocs/Next site and simplify navigation. Commit 027 adds the remaining historical topics; 028 deletes the old Help tree. Commits 029–032 refine components, hierarchy, code typography and colors. Commit 042 makes prose more concise. Commit 043 converts delivery to static export, browser-side Orama search and a GitHub Pages workflow. These are related but distinct changes: importing a manual, rewriting its meaning, and changing where its pages can run demand different checks.

The complete specialist review is in the documentation dossiers and per-commit coverage. This bridge connects those detailed findings to the native API/build history; it does not replace their source-specific limits. Detailed subcases cover [migration lineage](../../../raknet-documentation/cases/migration-lineage.md), [editorial/API refactoring](../../../raknet-documentation/cases/editorial-refactoring.md), [confidence drift](../../../raknet-documentation/cases/confidence-drift.md) and [static deployment](../../../raknet-documentation/cases/static-docs-deployment.md).

## Attribution and preservation {#attribution-and-preservation}

Most networking explanations are inherited Oculus/RakNet material. The congestion-control page explicitly attributes its algorithm to Yunhong Gu and August 2009. Training-video records preserve Kevin Jenkins attribution. Modern MDX timestamps, new prose style and repository ownership do not transfer authorship of those algorithms or historical benchmarks.

The import was not lossless. Commit 027 deliberately summarizes older distributed-object, memory-synchronizer and congestion-control pages, while adding useful deprecation directions. Some old API caveats disappear. The deletion inventory accounts for all 1,215 Help files by upstream identity, but destination mapping is different from content preservation: 94 of 99 top-level HTML pages have direct or composite destinations, while the logger video and two legacy interface/concept pages do not have exact replacements. An 11-step MasterServer2/Lobby3/NAT deployment manual in a DOCX is also omitted. Its startup/shutdown and backup ordering are substantive historical operations information; its obsolete dependency/security instructions should not be promoted as current guidance.

Commit 014 copies 71 images exactly and imports 66 MDX pages. Original presentation/media internals and generated API pages have structural or provenance dispositions, not fresh line-by-line semantic credit. This is proportionate review without treating inherited bulk as newly authored engineering philosophy.

## Formatting can conceal semantic edits {#formatting-can-conceal-semantic-edits}

Commits 030/031 do more than formatting: they repair example punctuation and identifiers, revise API tables and units, and remove qualifications. The TwoWayAuthentication page loses an explicit warning that verification alone does not block other messages or decide application privileges. The shortened page does not thereby establish stronger access control. A repaired Startup example still disagrees with the final native function signature and treats a zero-valued success enum as truthy success. Punctuation correctness is a different contract from API correctness.

All 77 fenced-code bodies in commit 042 are byte-identical before and after. That is strong evidence about those bodies only. Prose simultaneously changes tentative historical compatibility statements into confident ones, such as “should work” becoming “works,” without new platform/provider measurements. A mechanical code-body proof cannot establish meaning-preserving prose edits or current external compatibility.

## Static hosting changes the interface contract {#static-hosting-changes-the-interface-contract}

The final deployment change is a concrete serving-model adjustment: Next static export, an optional `/RakNet` base path, disabled image optimization, static search data and browser-side Orama querying replace assumptions about a runtime server. The existing transitive Orama package becomes a direct dependency; the lock still contains 691 package records. The Pages workflow builds on qualifying main-branch docs changes and deploys its generated output. No workflow, installation, build, browser or external assistant service was run.

Static source checks find inconsistencies worth retaining as bounded questions. The content source is mounted at `/`, while four Quick Start cards use `/docs/...`; two catalog links use an outdated replica-manager route. Page actions request `${page.url}.mdx` but the handler is `/llms.mdx/[[...slug]]`, and the final export removes the earlier rewrite without changing those requests. Source links choose an upstream repository and omit the repository's `docs/` prefix. These are source-level mismatches, not browser-confirmed failures. Similarly, bare `doxygen` instructions coexist with no tracked Doxygen configuration in the checked final tree, so reproducibility is not established.

## When to retrieve this case {#when-to-retrieve-this-case}

Use it when migrating manuals, presenting inherited material as modern docs, reviewing an apparent formatting-only PR, changing a server-rendered docs application to a static project site, or aligning examples with native APIs. Keep lineage, semantic fidelity, route correctness, build success and current compatibility as separate evidence dimensions. Shorter prose and cheaper maintenance can be valuable; preserve the caveats needed for the actual contract, rather than indiscriminately restoring every historical page.

Explicit Claude Opus 4.6 coauthor trailers occur on 014, 027, 028, 030, 031 and 043. Other messages do not establish whether assistance was used. Imported source authors, declared assistance and the target-era local changes remain separate.

## Exact commit navigation {#exact-commit-navigation}

- [009 dc0c2ad6a72f: docs: rewrite README for modernized fork](../dossiers/009-dc0c2ad6a72f.md) · [public source](https://github.com/wu-vincent/RakNet/commit/dc0c2ad6a72fc9a9927ee83228128624e50f653c)
- [010 b173bf218267: chore: reformat LICENSE to standard GitHub BSD 2-Clause template](../dossiers/010-b173bf218267.md) · [public source](https://github.com/wu-vincent/RakNet/commit/b173bf2182679d9a947d237cd1f74661707160db)
- [014 4704e4a97c10: docs: convert Help/ HTML documentation to Fumadocs site](../dossiers/014-4704e4a97c10.md) · [public source](https://github.com/wu-vincent/RakNet/commit/4704e4a97c10b776756ba0d746b9f49e44a63bb9)
- [015 08a3147faba9: docs: simplify docs/meta.json by removing redundant section headers](../dossiers/015-08a3147faba9.md) · [public source](https://github.com/wu-vincent/RakNet/commit/08a3147faba92f823da810f33925cd60e4a93a37)
- [027 1b4af017155a: docs: port all remaining Help pages to MDX](../dossiers/027-1b4af017155a.md) · [public source](https://github.com/wu-vincent/RakNet/commit/1b4af017155a9393226c0a314f7e51fa8b0ba3b9)
- [028 4e7570cfd193: chore: remove legacy Help/ directory](../dossiers/028-4e7570cfd193.md) · [public source](https://github.com/wu-vincent/RakNet/commit/4e7570cfd193c0192c9bd073e9592308a1680a1c)
- [029 25e275ddc5ff: docs: update branding and enhance MDX component support](../dossiers/029-25e275ddc5ff.md) · [public source](https://github.com/wu-vincent/RakNet/commit/25e275ddc5ff67914b2ae3a9e84efa73e28addd0)
- [030 81af283838a5: docs: modernize all 79 MDX pages with Fumadocs components and cleanup](../dossiers/030-81af283838a5.md) · [public source](https://github.com/wu-vincent/RakNet/commit/81af283838a548411193960fc216e765e8adaa07)
- [031 aa5646684c90: docs: add inline code backticks throughout all MDX documentation](../dossiers/031-aa5646684c90.md) · [public source](https://github.com/wu-vincent/RakNet/commit/aa5646684c90d901327baec06a6812e2870a8916)
- [032 01518f1d77f9: docs: update global.css with primary color theme variables](../dossiers/032-01518f1d77f9.md) · [public source](https://github.com/wu-vincent/RakNet/commit/01518f1d77f9a06a76042d4760ddbe977c773089)
- [042 9fb1c02bb570: docs: improve documentation](../dossiers/042-9fb1c02bb570.md) · [public source](https://github.com/wu-vincent/RakNet/commit/9fb1c02bb570f8ad57ef177dd11f045f8d606712)
- [043 076213f71493: ci: add GitHub Actions workflow to deploy docs to GitHub Pages](../dossiers/043-076213f71493.md) · [public source](https://github.com/wu-vincent/RakNet/commit/076213f71493e840dc71ce87ef7662b8e1e36b5a)
