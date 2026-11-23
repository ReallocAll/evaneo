<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:429"],"source_type":"public","date":"2026-07-09","topics":["testing","build","review","selection"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-429-crashpadhandler-fails-with-missing-libc-when-running-via-pterodactyl-egg"></a>
# EndstoneMC/endstone #429: crashpad_handler fails with missing libc++ when running via Pterodactyl egg {#endstonemc-endstone-429-crashpadhandler-fails-with-missing-libc-when-running-via-pterodactyl-egg}

Source: https://github.com/EndstoneMC/endstone/issues/429

## Evidence and attribution {#evidence-and-attribution}

Primary author: dyan1619. Created 2026-07-09T23:33:13Z; recorded state closed; merged not applicable.

## Packaging failure and actual fix {#packaging-failure-and-actual-fix}

dyan1619 reported crashpad_handler unable to resolve hashed vendored libc++ under Pterodactyl while the game server itself continued. wu-vincent traced a relocatability error: auditwheel patches handler RPATH relative to its package location, but bootstrap copied the executable into the server directory.

The inspected f8b13b1a3 removes bootstrap copying and Linux chmod of the copied handler, resolves runtime::get_module_pathname().parent_path()/platform-specific handler name in C++, and passes it to sentry_options_set_handler_path. This preserves the packaged dependency graph instead of installing another libc++ globally. It fixes reporting, not the main process or network connection issue. No loader smoke test is included in this commit.

## Code and verification boundary {#code-and-verification-boundary}

Inspected complete f8b13b1a30b63653a39ccaf503ea5fb6bcfeaa05 across Python bootstrap and C++ Sentry configuration. No upstream code was executed and no tests were run in this review. Runtime assertions are source-reported unless explicitly identified as static code findings.

## Traceability {#traceability}


- https://github.com/EndstoneMC/endstone/issues/429
- https://github.com/EndstoneMC/endstone/issues/429#issuecomment-4936350795
