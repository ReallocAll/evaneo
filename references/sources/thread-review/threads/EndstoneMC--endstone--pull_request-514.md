<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:514"],"source_type":"public","date":"2026-08-23","topics":["ffi","testing","build","performance","review","selection","networking"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-514-perf-network-compress-packets-with-libdeflate"></a>
# EndstoneMC/endstone #514: perf(network): compress packets with libdeflate {#endstonemc-endstone-514-perf-network-compress-packets-with-libdeflate}

Source: https://github.com/EndstoneMC/endstone/pull/514

## Evidence and attribution {#evidence-and-attribution}

Primary author: wu-vincent. Created 2026-08-23T19:24:05Z; recorded state closed; merged True.

## Compression is a measured CPU/bandwidth tradeoff {#compression-is-a-measured-cpu-bandwidth-tradeoff}
Wu replaces per-batch fresh zlib raw level7 with per-connection reusable libdeflate level6, preserving packet framing. A 3,465-batch/39.7MB live corpus reports zlib25.5MiB/s versus libdeflate117.9MiB/s (4.6×), compressed sizes8,900,113 versus8,936,071 bytes (~0.4% larger). Levels1/4/6/8/9/10/12 were compared; CPU savings motivate6 rather than8 even though another level can be smaller. The benchmark is disabled in CI. The reported throughput figures apply to the measured packet corpus.
Below-threshold stored blocks, hybrid FF passthrough, Snappy1.2.1 and native unknown-algorithm send/receive asymmetry are retained. A single incoming-peer hook constructs a compatible derived peer; this avoids unproven Result<string>/CallStack return ABI. Corrected layout includes a previously missing capacity field, with128-byte Windows/112-byte Linux assertions. Unexpected peer chains log and fall back; normal operation is silent, so silence alone does not prove optimization activation.
Source reports78/78 symbol matches across two BDS versions,341 wire/cross-compression tests, and live26.44 traffic for zlib and Snappy. Linux build/size asserts are distinct from those live observations. Claude assistance disclosed.

## Direct patch findings {#direct-patch-findings}

Incoming hook invokes native setup first, locks weak compressed peer, searches chain by identity, then replaces just that node and weak reference; missing/unknown chain keeps vanilla. Copies negotiated flags/limits/options. Per-peer libdeflate compressors allocate lazily at levels0/6; Snappy is reimplemented via RawCompress rather than forwarding to native. Receive validates negotiated/header equality, Snappy advertised length and deflate capacity doubling, rejecting malformed/unknown data. Raw hybrid FF and disabled-compression paths copy without that size check; initial inflate guess is at least1024 even if max_decompressed_size is smaller, a boundary assumption needing explicit tests. send silently returns on allocation/compression failure. Committed tests are three library interoperability/ratio tests with six constructed payloads plus disabled corpus benchmark; they do not instantiate the replacement peer or test negotiated framing/limits. The claimed341-case wire matrix is therefore external evidence, not these checked-in tests. Benchmark compares reused and fresh zlib separately and has deterministic fallback payloads when no corpus is supplied.

## Code and verification boundary {#code-and-verification-boundary}

Inspected every semantic hunk of captured PR diff (35266 characters; SHA-256 dd957980e0b45a15295970e93d3cc7b09ee94f3be37f05743329ab8ea3a9bc17), head f253987262603ba50448f209acec091c4dc8425d. Repeated Apache license boilerplate was collapsed for104; no code omitted. Scope is this supplied patch, not all linked implementation history. No upstream code was executed and no tests were run in this review. Runtime assertions are source-reported unless explicitly identified as static code findings.

## Traceability {#traceability}


- https://github.com/EndstoneMC/endstone/pull/514
