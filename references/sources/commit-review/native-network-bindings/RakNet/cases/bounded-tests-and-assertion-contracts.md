<!-- retrieval: {"source_ids":["public:commit:119c12ae0b299199818008fb6ff41f48e33a383e","public:commit:2a89d3abb0cc54d8098bbd59ad95d9d3436da8df","public:commit:4c4588a0453c501af87225325122c0ea7b0058d9","public:commit:544b20633f5b2d6f6546d60c9d3cf0d811ad6f82","public:commit:74acca5d264124b6f660a1c497aa3df40aeca466","public:commit:b2e060e32b7f0a45693117005e5f7ecf39ceab4d","public:commit:c313ee26624b0ea15ea9172dd7026a63608dadc8","public:commit:cf307cc8d07ca6e39a90158e4e57e17fd493b05f","public:commit:d948d871eee8eadc63712bda8ce65e30a681a514","public:commit:e814af9398fd1100f712785c485c40009ccc0a2f"],"source_type":"public","date":"2026-02-24..2026-02-26","topics":["lifetime","concurrency","testing","build","performance","api","selection","networking"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="rn03-convert-demonstrations-into-useful-ci-checks-without-confusing-coverage-with-volume"></a>
# Convert demonstrations into useful CI checks without confusing coverage with volume {#rn03-convert-demonstrations-into-useful-ci-checks-without-confusing-coverage-with-volume}

## What changes in the test architecture {#what-changes-in-the-test-architecture}

The chain033–041 moves standalone/manual programs into one GoogleTest executable, discovers cases through CTest and uses ephemeral ports instead of fixed ones. Fixtures own RakPeer instances and destroy them during teardown. Tests are explicitly listed in CMake rather than discovered through a broad source glob. This establishes a repeatable validation interface, but the research does not execute it or claim a passing build.

The migrations intentionally shorten or focus some workloads. ThreadTest drops from60 seconds to3, comprehensive random operations from long manual runs to5 seconds, disconnect/reconnect from30 to15 seconds, and an83,296,256-byte transfer becomes three cases capped at5,000,000 bytes. The removal message calls TestDLL redundant and identifies PostgreSQL as unsuitable for CI. These are maintenance/feedback-cost tradeoffs. The source does not justify a recommendation to restore every legacy stress run, and larger test volume alone is not evidence of better engineering.

## Assertions determine the actual guarantee {#assertions-determine-the-actual-guarantee}

Several changes improve the strength of small tests:
- MessageSizeTest compares received p->data against the expected pattern, correcting the old comparison against the send buffer. Seven representative strides replace an exhaustive sweep.
- CrossConnection checks the two endpoint connection counts and allows valid simultaneous acceptance outcomes; a later case repeats ping-timed connect/disconnect cycles.
- ReliableOrderedTest sends50 packets on each of32 channels and checks exact per-channel ordering plus1,600 total arrivals.
- EightPeerTest sends100 broadcasts from each of eight peers and checks all56 directed sender/receiver pairs, draining while sending to limit queue buildup.
- StatisticsHistory replaces an infinite graph with focused retrieval, aggregate, merge, resample and error tests.
- OfflineMessages adds payload/length checks, readback and GUID assertions.

Other checks are deliberately narrower than their names may suggest. The thread test requires some reception, not absence of data races. The comprehensive random-operation test mainly checks valid connection initiation and survival; no leak detector is present. ServerClient's separate all-connect case requires100 connections, but its traffic case accepts at least50 initially and more than zero remaining, without validating traffic contents or counts. MaximumConnect asserts a cap of four but does not require a minimum successful connection count or enumerate refusal notifications.

These statements describe scope, not automatic defects. They tell a downstream engineer whether a cheaper existing test already covers the contract at risk, and where a new requirement would need a focused additional assertion.

## Data transfer and performance claims {#data-transfer-and-performance-claims}

BigPacket's50KB and500KB cases compare every byte; the5MB case verifies length only. The send uses ACK_RECEIPT reliability but the receipt itself is not asserted. Download progress is counted but not checked. This preserves fragmentation/reassembly smoke coverage at a lower cost, without establishing maximum supported payload size or integrity for every byte of the largest case.

FlowControl uses an explicit three-peer relay, samples64/256/1024/4096-byte payloads and compares send/receive counts after a drain. Length checks apply in the main receiving loop but not every final-drain path. LoopbackPerformance sends roughly 500 packets per second, each 400 bytes, for 3 seconds, requiring all arrivals for reliable modes and more than half for unreliable mode. Its result contains sent/received counts, not elapsed throughput. Therefore the source supplies a delivery workload at a chosen rate, not a measured throughput improvement or benchmark of the fork.

The removed DLL test had no assertion framework but did exercise exported allocation/deallocation and classes across a DLL boundary. The removed database program required interactive PostgreSQL setup. Preserve those lost scopes as facts while respecting the explicit choice to keep CI focused; neither deletion proves those paths are broken or mandates rebuilding the old harness.

## Clock and ownership improvements, with residuals {#clock-and-ownership-improvements-with-residuals}

Commit038 replaces general test deadlines with std::chrono::steady_clock. Protocol RTT arithmetic and StatisticsHistory still use RakNet's clock where its API is part of the subject under test. That distinction prevents conflating a test timeout source with the implementation timing contract. No flakiness measurement is supplied.

ThreadTest uses atomics and joins standard threads before peer destruction instead of leaving unsynchronized global stop state. RelayPlugin teardown detaches plugins before destroying peers and then destroys plugin instances. CloudTest frees decoded query result/row allocations. These are concrete ownership improvements in the harness.

Two success paths still bypass packet cleanup: RelayPlugin's WaitForRelayResponse returns from a loop whose increment performs DeallocatePacket; CloudTest jumps to a subscribed label before that increment. Final snapshots retain both paths. This is a static cleanup observation, not a reproduced heap leak. Similarly, fixed sleeps before some connection/plugin-registration steps remain timing assumptions. None of these observations authorizes executing the project or claiming runtime failure.

## Practical use {#practical-use}

For a test modernization, retain the intended behavior and choose the smallest meaningful automated oracle. Record what a test asserts, how it terminates, which external resources it needs and which older workload it replaces. Keep stress duration, interoperability, performance and deterministic regression coverage separate. A narrowly targeted concurrency or exact-byte regression can be more valuable than a broad redundant test. Revisit an omitted scope only when the task or a real failure makes it relevant.

Sources: dossiers033–041, complete structural residuals, final tests/CMakeLists.txt, RelayPluginTest.cpp and CloudTest.cpp snapshots. Messages033–038 and040 declare Claude Opus4.6 coauthorship;039 and041 do not include that trailer. The upstream Oculus test concepts remain upstream attribution; local migrations, assertions and defaults are the target-era delta.

## Exact commit navigation {#exact-commit-navigation}

- [012 d948d871eee8: refactor: move 17 test programs from samples/ to tests/](../dossiers/012-d948d871eee8.md) · [public source](https://github.com/wu-vincent/RakNet/commit/d948d871eee8eadc63712bda8ce65e30a681a514)
- [033 119c12ae0b29: test: introduce Google Test and migrate 3 tests to gtest](../dossiers/033-119c12ae0b29.md) · [public source](https://github.com/wu-vincent/RakNet/commit/119c12ae0b299199818008fb6ff41f48e33a383e)
- [034 b2e060e32b7f: test: migrate ThreadTest and StatisticsHistoryTest to gtest](../dossiers/034-b2e060e32b7f.md) · [public source](https://github.com/wu-vincent/RakNet/commit/b2e060e32b7f0a45693117005e5f7ecf39ceab4d)
- [035 544b20633f5b: test: migrate BurstTest and ReliableOrderedTest to gtest](../dossiers/035-544b20633f5b.md) · [public source](https://github.com/wu-vincent/RakNet/commit/544b20633f5b2d6f6546d60c9d3cf0d811ad6f82)
- [036 4c4588a0453c: test: migrate DroppedConnectionTest and ComprehensiveTest, remove legacy ConvertTest files](../dossiers/036-4c4588a0453c.md) · [public source](https://github.com/wu-vincent/RakNet/commit/4c4588a0453c501af87225325122c0ea7b0058d9)
- [037 cf307cc8d07c: test: migrate BigPacketTest, ServerClientTest, and RelayPluginTest to gtest](../dossiers/037-cf307cc8d07c.md) · [public source](https://github.com/wu-vincent/RakNet/commit/cf307cc8d07ca6e39a90158e4e57e17fd493b05f)
- [038 74acca5d2641: test: replace GetTime with std::chrono and add doxygen @brief to fixtures](../dossiers/038-74acca5d2641.md) · [public source](https://github.com/wu-vincent/RakNet/commit/74acca5d264124b6f660a1c497aa3df40aeca466)
- [039 e814af9398fd: test: migrate CloudTest to gtest](../dossiers/039-e814af9398fd.md) · [public source](https://github.com/wu-vincent/RakNet/commit/e814af9398fd1100f712785c485c40009ccc0a2f)
- [040 c313ee26624b: test: migrate FlowControlTest and LoopbackPerformanceTest, remove TestDLL and RankingServerDBTest](../dossiers/040-c313ee26624b.md) · [public source](https://github.com/wu-vincent/RakNet/commit/c313ee26624b0ea15ea9172dd7026a63608dadc8)
- [041 2a89d3abb0cc: test: migrate MaximumConnectTest and EightPeerTest to gtest](../dossiers/041-2a89d3abb0cc.md) · [public source](https://github.com/wu-vincent/RakNet/commit/2a89d3abb0cc54d8098bbd59ad95d9d3436da8df)
