<!-- retrieval: {"source_ids":["public:thread:AllayMC/Allay:335"],"source_type":"public","date":"2024-08-10","topics":["concurrency","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="allaymc-allay-335-feat-allow-3rd-plugin-loader"></a>
# AllayMC/Allay #335: feat: allow 3rd plugin loader {#allaymc-allay-335-feat-allow-3rd-plugin-loader}

Source: https://github.com/AllayMC/Allay/issues/335

## Review scope and state {#review-scope-and-state}

- Thread author: smartcmd; state at review: closed; merged: not applicable.
- Evidence: The public issue and code/reproduction described below were reviewed statically; no code execution or tests were performed.
- Limits: Source snapshot only; no independent runtime verification.

## Engineering reading and attribution {#engineering-reading-and-attribution}

The technical explanation belongs to smartcmd, not wu: a plugin could not register a third-party loader because the manager was already frozen by the time plugins loaded. Cdm2883 challenged why loader support needed an issue, eliciting this lifecycle-order constraint. Wu contributed only an emoji. The reusable design question is whether extension registration occurs before the registry freezes; the thread neither specifies the eventual ordering change nor proves its implementation. No independent code attribution to wu is warranted.



## Source index {#source-index}

- https://github.com/AllayMC/Allay/issues/335
- https://github.com/AllayMC/Allay/issues/335#issuecomment-2281166797
- https://github.com/AllayMC/Allay/issues/335#issuecomment-2382158087
- https://github.com/AllayMC/Allay/issues/335#issuecomment-2382346507
- https://github.com/AllayMC/Allay/issues/335#issuecomment-2387553059
- https://github.com/AllayMC/Allay/issues/335#issuecomment-2387582826
