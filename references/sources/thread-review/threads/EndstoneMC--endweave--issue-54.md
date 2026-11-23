<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endweave:54"],"source_type":"public","date":"2026-09-25","topics":["testing","build","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endweave-54-v0-5-1-missing-windows-cp312-abi3-wheel-python-3-12-users-cannot-install-on-endstone-0-11-11"></a>
# EndstoneMC/endweave #54: v0.5.1 missing Windows cp312-abi3 wheel — Python 3.12+ users cannot install on Endstone 0.11.11 {#endstonemc-endweave-54-v0-5-1-missing-windows-cp312-abi3-wheel-python-3-12-users-cannot-install-on-endstone-0-11-11}

Source: https://github.com/EndstoneMC/endweave/issues/54

## Evidence and attribution {#evidence-and-attribution}

Primary author: xie52a. Created 2026-09-25T13:25:24Z; recorded state closed; merged not applicable.

Reporter infers missing Windowscp312-abi3 wheel from failed production installs and proposes an MSVC/matrix failure hypothesis, then documents Python-only protocol2193→2192 workaround on six servers. Wu checks official release/PyPI and says the wheel was present sinceSept15 and selected by Python3.13; build-failure hypothesis is rejected. Mirror lag becomes a tentative explanation, with official index/full pip output the next discriminating check. No reply verifies mirror causality. Keep compatibility of stable-ABI wheel separate from claimed absence and avoid recommending patching old translator engines unnecessarily.

## Code and verification boundary {#code-and-verification-boundary}

No code inspection required for the narrow discussion finding; no implementation claim independently verified. No upstream code was executed and no tests were run in this review. Runtime assertions are source-reported unless explicitly identified as static code findings.

## Traceability {#traceability}


- https://github.com/EndstoneMC/endweave/issues/54
- https://github.com/EndstoneMC/endweave/issues/54#issuecomment-6252588252
