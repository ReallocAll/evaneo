<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:331"],"source_type":"public","date":"2026-02-13","topics":["lifetime","ffi","testing","api","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-331-feat-attribute-add-attribute-api"></a>
# EndstoneMC/endstone #331: feat(attribute): add attribute api {#endstonemc-endstone-331-feat-attribute-add-attribute-api}

Source: https://github.com/EndstoneMC/endstone/pull/331

## Evidence and attribution {#evidence-and-attribution}

Primary author: killcerr. Created 2026-02-13T16:11:19Z; recorded state closed; merged False.

## Discussion disposition {#discussion-disposition}

killcerr proposed the Attribute API for #293. wu-vincent later stated #411 rebases and finishes it, with original commits squash-rebased into its first commit and explicit co-author credit. Closed unmerged; do not erase that contributor lineage.

The full associated patch was subsequently inspected; test execution is not independently verified.

## Direct patch findings {#direct-patch-findings}

Direct defects in the original unmerged implementation explain why #411 is a redesign: _calculateValue mutates already-current values without resetting the base, and multiply-base multiplies current by amount rather than adding base-scaled amount. getAttributes dereferences AttributesComponent without a null guard. Modifier enumeration omits native UUID/operand/persistence and leaves operation uninitialized for Cap/default. Tiny Python test only checks list length add/remove, not numerical semantics/lifetime. It also adds substantial unrelated formatting churn and changes Level::tick symbol local to static.

### Proxy-iterator correction from exact-head linked code {#proxy-iterator-correction-from-exact-head-linked-code}

The complete attribute_map.h/.cpp and relevant associative_adapter.h iterator definitions were inspected at this PR head. The backing map is brstd::flat_map, whose dereference returns pair<const Key&, T&> (or const T& for const iteration). Therefore auto [id, instance] copies reference-bearing proxy state, not an AttributeInstance; &instance still points into the container. An earlier dangling-copy interpretation was incorrect and is withdrawn. Native container mutation and owner lifetime still govern validity, but the structured binding itself does not establish a dangling pointer. Do not diagnose proxy ranges using ordinary std::map value-copy assumptions.


## Code and verification boundary {#code-and-verification-boundary}

Inspected every hunk of captured PR diff (27430 characters; SHA-256 9bf78e8b2c732b8917e1ec67d1b92bc58fc3bfcf50eef0d0989e003b35e36404), head 47aab0acc73a64426c4eefc84579cbeae8a84fe1. Scope is this supplied patch, not all linked implementation history. No upstream code was executed and no tests were run in this review. Runtime assertions are source-reported unless explicitly identified as static code findings.

## Traceability {#traceability}


- https://github.com/EndstoneMC/endstone/pull/331
- https://github.com/EndstoneMC/endstone/pull/331#issuecomment-4603643447
