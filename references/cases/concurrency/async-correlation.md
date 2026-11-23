<!-- retrieval: {"source_type":"static_review","topics":["asynchronous","concurrency","state-machine","correlation","callbacks","cancellation","code-review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="serialization-does-not-identify-an-asynchronous-completion"></a>

# Serialization does not identify an asynchronous completion {#serialization-does-not-identify-an-asynchronous-completion}

## Problem {#problem}

Serial callbacks prevent simultaneous mutation. They do not ensure that the next event belongs to the operation currently waiting for completion.

## Inspected pattern and concern {#inspected-pattern-and-concern}

An implementation stored one pending association while opening another resource. Its next activation callback consumed that pending association without checking an operation identifier or distinguishing the role of the arriving resource.

A second independent activation could occur before the awaited operation completed. Even with perfectly serialized callbacks, the state shape allowed that event to be paired with the pending request. The latest observed surrounding implementation retained the same single-slot assumption.

The source described a successful simple scenario. That report does not establish correctness under overlapping operations. This is a static review concern; no failure was reproduced, and no source-author fix or production incident is claimed.

## Model the identity separately {#model-the-identity-separately}

List the events that can reach the same callback: a requested completion, an unrelated activation, failure, timeout, cancellation and a late completion after cancellation. For each, identify what proves the event belongs to the pending operation.

Possible designs include an operation-keyed pending map, explicit roles plus a stable identifier, or a single-flight gate that rejects or queues additional work until the outstanding operation finishes. The correct choice depends on whether concurrency is a requirement.

State transitions should specify:

- Who creates and owns the pending entry
- How success finds exactly that entry
- Which failure or cancellation removes it
- Whether an identifier can be reused while a late event is still possible
- What happens to unknown or duplicate completions

These are design alternatives, not a reconstruction of the inspected implementation.

## Verification {#verification}

Drive two operations with their completions reversed. Insert an unrelated activation between start and completion. Cancel one operation and deliver its completion late. Repeat failure and completion to check idempotence.

A single event loop simplifies mutation ordering, but the test oracle must still verify which operation received which result. Locking, a strand or a passing single-operation test cannot supply missing correlation.

The abstraction applies to background jobs, resource acquisition, session setup and request/response adapters. If the environment guarantees one outstanding operation and the boundary enforces it, a single slot can be appropriate. Document and test that enforcement rather than assuming the environment remains quiet.
