<!-- retrieval: {"source_type":"judgment_synthesis","topics":["engineering-judgment","mechanisms"],"limitations":"A conditional synthesis of historical engineering decisions; not project policy or proof of future outcomes."} -->
<a id="overview"></a>
# Do not add mechanisms merely to justify a design {#overview}

## Rationale {#rationale}
Ask whether the responsibility belongs in an existing layer before adding adapters, wrappers, state, or defensive processes. A small helper is warranted when it isolates real responsibility; fewer lines alone do not imply a simpler system. Preserve ownership, lifetime, and ABI constraints when removing redundancy.

Evaluate protective mechanisms in both directions: what plausible failure they prevent, what existing boundary already addresses it, and what legitimate requests they might reject or interrupt. A hypothetical risk alone is not a mandate for a new layer. Do not reopen an explicitly accepted trust model without new material evidence; still preserve independently required safety, protocol, and data-integrity contracts.

## Case and counterexample {#example}
A codebase has duplicated parsing for options already owned by a configuration reader. Reuse that reader rather than maintaining a shadow parser. A helper may still be beneficial where it removes deeply nested error handling.

### Observed agent decision failure

In a design discussion about relaying a renewable credential between two operator-controlled, OAuth-authenticated HTTPS MCP services, the operator explicitly accepted the model as a transient intermediary. The assistant had already read the general engineering guide, but repeatedly proposed additional encryption, persistent services, and recovery machinery without evidence that the existing boundary was inadequate. Repeated warnings displaced the actual unanswered implementation questions. This was an **observed advice failure**, not evidence of a production security incident or a failed implementation.

The correction is to honor the stated trust model, assess the incremental value and failure costs of each suggested safeguard, then investigate only material unknowns. For this decision, [autonomy](autonomy.md#overview) (stated authority and trust) and [compatibility](compatibility.md#overview) (real security and compatibility contracts) are relevant alongside [mechanisms](mechanisms.md#overview); mandatory default reading of unrelated documents would not fix the decision. If a guard could reject legitimate protocol traffic, validate that possibility against the actual contract before enforcing it.

## Applicability {#applicability}
Use when evaluating architecture, abstractions, refactors, or duplicated safeguards.

## Evidence boundaries {#limits}
This account summarizes historical decisions and their limits. It is not an authorization to perform new work and does not override a current repository contract.
