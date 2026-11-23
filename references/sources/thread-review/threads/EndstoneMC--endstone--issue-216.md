<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:216"],"source_type":"public","date":"2025-07-14","topics":["lifetime","concurrency","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-216-bug-docker-image-permission-problems"></a>
# EndstoneMC/endstone #216: [bug] Docker image permission problems {#endstonemc-endstone-216-bug-docker-image-permission-problems}

Source: https://github.com/EndstoneMC/endstone/issues/216

## Review scope and state {#review-scope-and-state}

- Thread author: cenk; state at review: closed; merged: not applicable.
- Evidence: The public issue and code/reproduction described below were reviewed statically; no code execution or tests were performed.
- Limits: Source snapshot only; no independent runtime verification.

## Engineering reading and attribution {#engineering-reading-and-attribution}

cenk's bind-mounted Docker directory first prevents tempfile creation; chmod 777 then gets past that stage but copytree still fails. Wu identifies host/container ownership mismatch and links de39fefc42daa2e56341a323a13ff386244643a2. Full patch inspected: image starts root, entrypoint recursively chowns an existing server directory to fixed uid 1001 endstone, then execs gosu endstone; Dockerfile also removes prior password/sudo setup. This repairs ownership before dropping privileges rather than keeping the application root. A bind mount means recursive chown affects host-visible file ownership, a consequential deployment tradeoff; no such operation was executed here. The thread contains no reporter validation, and world-writable permissions are not the recommended reusable remedy.


## Source index {#source-index}

- https://github.com/EndstoneMC/endstone/issues/216
- https://github.com/EndstoneMC/endstone/issues/216#issuecomment-3070718699
- https://github.com/EndstoneMC/endstone/issues/216#issuecomment-3228235891
- https://github.com/EndstoneMC/endstone/commit/de39fefc42daa2e56341a323a13ff386244643a2
