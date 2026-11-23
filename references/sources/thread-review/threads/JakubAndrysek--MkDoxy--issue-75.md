<!-- retrieval: {"source_ids":["public:thread:JakubAndrysek/MkDoxy:75"],"source_type":"public","date":"2023-08-30","topics":["testing","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="jakubandrysek-mkdoxy-75-how-to-find-an-execution-issue"></a>
# JakubAndrysek/MkDoxy #75: how to find an execution issue {#jakubandrysek-mkdoxy-75-how-to-find-an-execution-issue}

Source: https://github.com/JakubAndrysek/MkDoxy/issues/75

## Evidence and attribution {#evidence-and-attribution}

Primary author: ghost. Created 2023-08-30T15:11:27Z; recorded state closed; merged not applicable.

MkDoxy initially blames missing Doxygen, but reporter has identical container and suspects poetry invocation. Issue closes while unresolved. Months later Wu isolates plain mkdocs build success versus --config-file mkdocs.yml failure and associates it with cwd derived from configuration path; this turns environment speculation into a minimal differential reproduction. Maintainer lacks time, invites PR; Wu supplies #103. Reporter plans retest, not confirmed final success. Full traceback ends FileNotFoundError with empty filename; the patch must establish whether path resolution, cwd directory, or executable discovery is repaired.

## Code and verification boundary {#code-and-verification-boundary}

No code inspection required for the narrow discussion finding; no implementation claim independently verified. No upstream code was executed and no tests were run in this review. Runtime assertions are source-reported unless explicitly identified as static code findings.

## Traceability {#traceability}


- https://github.com/JakubAndrysek/MkDoxy/issues/75
- https://github.com/JakubAndrysek/MkDoxy/issues/75#issuecomment-1699391278
- https://github.com/JakubAndrysek/MkDoxy/issues/75#issuecomment-1699396067
- https://github.com/JakubAndrysek/MkDoxy/issues/75#issuecomment-1725431390
- https://github.com/JakubAndrysek/MkDoxy/issues/75#issuecomment-1725437585
- https://github.com/JakubAndrysek/MkDoxy/issues/75#issuecomment-1725450170
- https://github.com/JakubAndrysek/MkDoxy/issues/75#issuecomment-2085774418
- https://github.com/JakubAndrysek/MkDoxy/issues/75#issuecomment-2085824382
- https://github.com/JakubAndrysek/MkDoxy/issues/75#issuecomment-2088129282
- https://github.com/JakubAndrysek/MkDoxy/issues/75#issuecomment-2089715389
