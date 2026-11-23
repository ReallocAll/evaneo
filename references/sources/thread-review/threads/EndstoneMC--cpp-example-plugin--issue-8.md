<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/cpp-example-plugin:8"],"source_type":"public","date":"2026-07-13","topics":["concurrency","build","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-cpp-example-plugin-8-build-failed-to-compile-for-linux-using-github-workflows"></a>
# EndstoneMC/cpp-example-plugin #8: Build failed to compile for Linux using github workflows {#endstonemc-cpp-example-plugin-8-build-failed-to-compile-for-linux-using-github-workflows}

Source: https://github.com/EndstoneMC/cpp-example-plugin/issues/8

## Review scope and state {#review-scope-and-state}

- Thread author: RWRmrfrog; state at review: closed; merged: not applicable.
- Evidence: The public issue and code/reproduction described below were reviewed statically; no code execution or tests were performed.
- Limits: Source snapshot only; no independent runtime verification.

## Engineering reading and attribution {#engineering-reading-and-attribution}

RWRmrfrog reports template Linux CI failure on Clang 18 with Endstone 0.11.6 and an unsuccessful attempt to add -stdlib=libc++ to compile/link options. Wu says the fix lives on the fetched v0.11 Endstone branch and a fresh build needs no template CMakeLists changes. This attributes the remedy upstream rather than endorsing the reporter workaround. Linked build-log attachments and the correcting commit were not captured/inspected, so the underlying compiler failure and actual fix remain unverified; the thread text is complete but diagnostic evidence is incomplete.



## Source index {#source-index}

- https://github.com/EndstoneMC/cpp-example-plugin/issues/8
- https://github.com/EndstoneMC/cpp-example-plugin/issues/8#issuecomment-5078967789
