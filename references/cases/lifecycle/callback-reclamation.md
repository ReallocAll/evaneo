<!-- retrieval: {"source_type":"static_review","topics":["C++","lifecycle","callbacks","cancellation","teardown","use-after-free","regression-testing"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="defer-reclamation-until-active-callbacks-are-safe"></a>

# Defer reclamation until active callbacks are safe {#defer-reclamation-until-active-callbacks-are-safe}

## Problem and constraint {#problem-and-constraint}

A connection can fail while the object processing it is still executing a callback. Logical disconnection may be correct immediately, while physical destruction is unsafe until the active call finishes. Treating those two moments as identical can leave the remainder of the callback running on reclaimed memory.

## Observed reasoning and change {#observed-reasoning-and-change}

The inspected change repaired the ordering of a guard that indicated active callback execution. A failure path invoked cleanup after prematurely clearing that guard. Cleanup therefore considered a retired object immediately reclaimable, although its own callback still had work to do.

The correction kept the active state in place through cleanup. Cleanup could sever the connection and retire the object, while the existing deferred-release mechanism postponed destruction to a later safe point. The surrounding implementation was inspected to establish that retirement and collection were separate operations; this was more than a suggestive commit title.

A targeted transport fixture induced disconnection at the state transition that had exposed the problem. Assertions checked that the original operation completed, another operation could run, closure was observable and transport cleanup occurred once. The source reports that the previous behavior crashed and the corrected test continued. That report was not reproduced in this review.

## How to use it {#how-to-use-it}

For teardown code, trace:

1. Which callback frames may still refer to the object?
2. Which action marks the resource logically closed?
3. Which owner actually destroys it?
4. What condition makes deferred objects safe to reclaim?
5. Can cleanup invoke a callback, reconnect, reenter a loop or release another owner?

Test failure at the transition itself, not only clean disconnect before or after the operation. Include continued useful work after failure and an exactly-once resource-release assertion where that is part of the contract.

## Alternatives and limits {#alternatives-and-limits}

An explicit ownership token, scoped lifetime guard, executor-confined retirement queue or redesigned callback ownership can express the same invariant. The appropriate choice depends on reentrancy, nesting and ownership; the inspected flag ordering is not a universal recipe.

A Boolean guard is especially questionable when callbacks can nest or overlap. A later safe point must itself be proven safe. Context destruction and forced shutdown can have separate destruction paths that a single disconnect test does not cover.

Evidence supports the narrow ordering repair and the existence of its regression test. It does not prove all lifetime paths are safe, nor that the reported test was independently run.
