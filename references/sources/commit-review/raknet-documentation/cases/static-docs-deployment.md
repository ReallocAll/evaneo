<!-- retrieval: {"source_ids":["public:commit:01518f1d77f9a06a76042d4760ddbe977c773089","public:commit:076213f71493e840dc71ce87ef7662b8e1e36b5a","public:commit:08a3147faba92f823da810f33925cd60e4a93a37","public:commit:1b4af017155a9393226c0a314f7e51fa8b0ba3b9","public:commit:25e275ddc5ff67914b2ae3a9e84efa73e28addd0","public:commit:4704e4a97c10b776756ba0d746b9f49e44a63bb9","public:commit:4e7570cfd193c0192c9bd073e9592308a1680a1c","public:commit:81af283838a548411193960fc216e765e8adaa07","public:commit:9fb1c02bb570f8ad57ef177dd11f045f8d606712","public:commit:aa5646684c90d901327baec06a6812e2870a8916"],"source_type":"public","date":"2026-02-24..2026-02-27","topics":["concurrency","build","documentation","review","selection","refactoring"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="rd04-adapt-search-and-routes-to-a-static-documentation-host"></a>
# Adapt search and routes to a static documentation host {#rd04-adapt-search-and-routes-to-a-static-documentation-host}

## Problem and implementation {#problem-and-implementation}

Commit 014 introduced a Next.js/Fumadocs application with a content adapter, page routes, server search, Markdown/LLM routes and generated OG images. Commit 043 adapts it for GitHub Pages: output:export, a conditional /RakNet basePath, unoptimized images, static search data and a browser-side Orama search dialog. The explicit message states these serving-model goals and credits Claude Opus 4.6.

The route uses createFromSource staticGET with revalidate=false. A client provider supplies the search dialog to RootProvider. The dialog uses static docs search, an English Orama instance, query state, loading feedback and result-list composition. The direct Orama dependency is promoted from an already locked transitive entry; the lock graph remains691 entries. This is a targeted import/dependency boundary change, not a wholesale dependency refresh.

The Actions workflow builds docs on main pushes touching docs/** and on manual dispatch. It uses Node 22, npm ci, the deployment environment flag, an exported out directory, .nojekyll, Pages artifact upload and deploy. Permissions distinguish read access from Pages write and OIDC deployment, and concurrency avoids cancelling in-progress Pages runs. No workflow or deployment was triggered during this review.

## Integration costs and unresolved assumptions {#integration-costs-and-unresolved-assumptions}

Static hosting removes server rewrite support from the configuration, but Markdown copy/open controls still request `${page.url}.mdx` while the actual handler lives at /llms.mdx/[[...slug]]. The original root-route and /docs rewrite assumptions already conflicted. Source links also use a path missing the repository docs/ prefix and later target facebookarchive rather than this fork. Four landing cards and two ReplicaManager links do not match the inventoried root content routes.

These are grounded source/configuration inconsistencies, not observed production failures. Framework base-path rewriting, generated outputs, asset URLs, OG generation and browser fetch behavior require build/render checks before a definitive runtime claim. Those runtime checks were not performed.

Workflow path filtering also means a change only to the workflow file is not included in the docs/** push trigger. Manual dispatch remains available. The workflow builds but does not explicitly invoke the separate lint/type-check scripts or a link/API/example-consistency suite. Configuration intent should not be reported as successful validation.

## Explicit versus inferred lesson {#explicit-versus-inferred-lesson}

Explicit: static export, client-side search, conditional project path and Pages deployment. Observed: provider/search dependency wiring and runtime rewrite removal. Inferred applicability: serving-model migrations should review data generation, browser search, canonical URLs, copy/raw-source endpoints, assets and source-repository links together. This is useful engineering reasoning supported by a concrete mechanism and counterexamples, not proof of universal author preference or a verified deployment outcome.

Use when publishing a documentation SPA/static export, removing a runtime server, changing base paths, adapting search or reviewing deployment permissions/triggers. The source files and their complete changed diffs were read; no package code was executed and no live site was checked.
