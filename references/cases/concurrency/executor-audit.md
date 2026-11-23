<!-- retrieval: {"source_type":"static_review","topics":["C++","concurrency","Asio","strand","executor","timers","cancellation","code-review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="audit-every-continuation-s-executor"></a>

# Audit every continuation's executor {#audit-every-continuation-s-executor}

## Principle {#principle}

Choose the serialization boundary from the shared resource. Several logical sessions may touch one socket, registry or state machine. Separate per-session executors do not serialize operations on that shared object.

Then verify the entire continuation chain. Starting a function on a serialized executor does not establish that every asynchronous callback it initiates will return through that executor.

## Evidence and counterevidence {#evidence-and-counterevidence}

The inspected design explained that a shared resource and its protocol state relied on a common strand. Relevant receive and shutdown work was visibly submitted through that strand.

However, the recurring timer was constructed on the underlying execution context and its wait callback had no explicit strand binding in the inspected file. The first invocation was dispatched through a strand; that fact alone did not demonstrate the executor of later callbacks. Multiple worker threads were also visible.

This is an analyst review concern. It is not a documented author correction, a reproduced race, or a claim that the whole repository is unsafe. It prevents using the design comment as proof that the implementation satisfied the stated serialization invariant.

The public [Asio executor documentation](https://think-async.com/Asio/asio-1.38.2/doc/asio/overview/model/executors.html) explains that associated executors determine completion scheduling. The public [strand documentation](https://think-async.com/Asio/asio-1.30.2/doc/asio/overview/core/strands.html) describes handler binding and consistency through intermediate operations. The latter is an earlier documentation version; neither page substitutes for testing a particular program.

## Practical audit {#practical-audit}

For each shared object, list every entry point and continuation that can read, mutate, close or cancel it. Include timer recurrence, completion handlers, intermediate handlers, synchronous public methods and shutdown callbacks.

For every asynchronous operation, identify its default executor and the completion handler's associated executor. Follow actual propagation or explicit binding. Do not rely on lexical nesting, comments, an included binding header, or the executor of the caller.

Where appropriate, add assertions that sensitive code runs in the expected execution domain. Exercise cancellation and shutdown while timers and receive operations are active. Thread sanitizers and stress tests can supplement the proof, but absence of a reproduced race is not evidence that an executor guarantee exists.

## Alternatives and limits {#alternatives-and-limits}

A single-thread execution context, explicit synchronization, executor-owned resources or properly bound continuations may each be suitable. The chosen invariant must cover all operations that require serialization.

This case strengthens a review method and records a bounded uncertainty. It does not establish a universal preference for strands, prohibit multithreading, or certify a concrete fix.
