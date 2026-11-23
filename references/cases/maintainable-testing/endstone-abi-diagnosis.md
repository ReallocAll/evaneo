<!-- retrieval: {"source_ids":[],"source_type":"public","date":"2026-08-05","topics":["testing","maintainability","complexity","review","abi","ffi","diagnosis"],"limitations":"Static review of linked primary sources and bundled historical analyses; upstream tests were not executed. Historical claims and code changes are distinguished from proven runtime outcomes."} -->
# Endstone #459: reject a narrow-looking ABI workaround when the model is wrong {#case}

## Root cause review {#changes}

In [PR #459](https://github.com/EndstoneMC/endstone/pull/459), ReallocAll proposed packet-layout and map serialization fixes for Linux. Maintainer wu-vincent confirmed real symptoms but corrected the ABI explanation: a flattened `UpdateSoftEnumPacket` model reused base-class tail padding at offset 44, while the actual native payload was a separately aligned subobject at offset 48. The separate [payload-struct repair](https://github.com/EndstoneMC/endstone/commit/c41890cb4bd8353f25cf282c5cf8e6466137f2d9) works without OS-specific conditional padding. The corresponding [map tracked-ID fix](https://github.com/EndstoneMC/endstone/commit/97071083e893b9d4addf47a8c62b3b1d158731ee) was also accepted separately. The original PR was closed, **not merged**. [Maintainer review](https://github.com/EndstoneMC/endstone/pull/459#issuecomment-5197129104).

## Judgment {#reading}

A small patch is not automatically maintainable if it encodes a wrong model. Prefer accurately reflecting a stable external layout over growing platform-specific special cases, assertions and workaround tests. Confirm the native contract first, then test the resulting layout and wire behavior.

## Limit {#limits}

This is a corrected diagnosis and scope case, not a direct observation of tests being deleted. The remaining claim about non-finite client rotation was not established as the cause of the packet layout issue.
