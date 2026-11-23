<!-- retrieval: {"source_ids":["public:commit:01518f1d77f9a06a76042d4760ddbe977c773089","public:commit:076213f71493e840dc71ce87ef7662b8e1e36b5a","public:commit:08a3147faba92f823da810f33925cd60e4a93a37","public:commit:1b4af017155a9393226c0a314f7e51fa8b0ba3b9","public:commit:25e275ddc5ff67914b2ae3a9e84efa73e28addd0","public:commit:4704e4a97c10b776756ba0d746b9f49e44a63bb9","public:commit:4e7570cfd193c0192c9bd073e9592308a1680a1c","public:commit:81af283838a548411193960fc216e765e8adaa07","public:commit:9fb1c02bb570f8ad57ef177dd11f045f8d606712","public:commit:aa5646684c90d901327baec06a6812e2870a8916"],"source_type":"public","date":"2026-02-24..2026-02-27","topics":["api","review","networking"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="rd01-preserve-provenance-and-measure-migration-coverage"></a>
# Preserve provenance and measure migration coverage {#rd01-preserve-provenance-and-measure-migration-coverage}

## Problem and evidence chain {#problem-and-evidence-chain}

RakNet's fork replaces an old Help tree with a Fumadocs site. Commit 014 creates the application and65 manual-oriented MDX pages plus a new landing page. Commit 027 adds 13 remaining topic pages and a six-video index. Commit 028 deletes all 1,215 old Help files, saying substantive content has been ported and generated APIs can be regenerated. These are linked implementation steps, not three independent endorsements of all old text.

Read the per-SHA dossiers014,027 and028 for concrete source links and detailed exceptions. The exact structural proofs establish that the 71 copied images and1,215 deleted files are inherited. The migration review then examines residuals and omissions instead of reassigning authorship to the commit author.

## Mechanism and tradeoffs {#mechanism-and-tradeoffs}

A content-source adapter, root catch-all page and section metadata replace a large hand-linked HTML presentation. Tutorial samples are consolidated, six video wrappers become metadata rows, deprecation notices direct readers from old APIs to successors, and old navigation/footer presentation is trimmed. This reduces navigational fragmentation and creates a consistent authoring format. The benefit is inferred from structure; no user study or measured discoverability result was recorded.

The conversion is not lossless. DistributedNetworkObject and MemorySynchronizer are shortened enough to lose old contract detail. Congestion-control equations remain attributed to Yunhong Gu, but several assumptions/units/counter definitions disappear. Embedded tutorial sample code is inherited while exercise introductions are deleted. A source-page destination is therefore weaker evidence than exact preserved semantics.

The deletion reconciliation matters independently of algorithm review:

-99 top-level HTML sources have94 direct/composite maps and five exceptions.
- The empty ConnectionFilter page has no substantive content to preserve.
- Two MajorFeatures wrappers point to the same media file; that media-reference identity is verified, while HTML blobs differ.
- The SQLite3LoggerPlugin video is distinct and omitted from the new six-video list.
- MessageHandlerInterface and PlayerID have related modern concepts but no exact migrated old contract.
- A separate Word operations manual has 197 paragraph-text records and11 deployment steps. Its shutdown/backup ordering and service setup are not represented by the shorter cloud-hosting page.

The old operations manual also contains obsolete dependency/security directions. Recording that it was omitted does not mean restoring it as current advice is desirable. A better migration review asks whether to archive, explicitly deprecate, summarize with links, or modernize after validation. The examined commits do not document that decision for every omitted item; those alternatives are reviewer applicability guidance, not attributed author intent.

## Explicit versus inferred positions {#explicit-versus-inferred-positions}

Explicit: modern site; seven sections; remaining historical pages; deprecation callouts; removing Help after migration; regenerating Doxygen. Observed: some content is condensed/omitted and no final tracked Doxygen config was found. Inferred lesson for a reviewer: separate source identity, preservation coverage and contemporary validity. Do not label the author as supporting every retained old platform, algorithm or anecdote.

Claude Opus 4.6 is explicitly co-authored on all three commits. The old congestion-control author and historical video author retain separate credit. The site scaffold identifies Create Fumadocs generation. Neither AI participation nor a generator declaration explains who wrote each individual sentence.

## Use and counterexample {#use-and-counterexample}

Use when asked: “Can we remove the old docs after converting them?”, “Which imported pages deserve fresh review?”, “Does a new Markdown commit make this current design guidance?”, or “How do we audit a vendor/manual migration efficiently?”

The counterexample is the claim that all substantive content was ported. Image/blob identity and a destination map cannot establish it. The review deliberately avoids wasting effort re-deriving inherited networking algorithms, but still reads new prose, compatibility edits, omitted caveats and unmapped sources.

## Validation boundary {#validation-boundary}

No generated-doc reproduction, site rendering, example execution or current service/platform validation. Image pixels, CHM and generated Doxygen interiors remain structurally dispositioned. This is a migration-analysis case, not a benchmark or runtime implementation case.
