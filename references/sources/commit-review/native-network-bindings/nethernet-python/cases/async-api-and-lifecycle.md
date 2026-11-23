<!-- retrieval: {"source_ids":["public:commit:09e4067b022dba085057e4d62af5c01bdba29a19","public:commit:26c265e417b1cc44162fe02d93afb7e3c51ea92f","public:commit:3d968dab941c2f6b45a690b456690bee2fa636ec","public:commit:449e5d19cda87a6c6eae67f0fcfcafbcfa66b6b7","public:commit:5f370a6e389ef6fb9e9611d491a5517e714720f9","public:commit:63cafaa7f81b5f96cfe56d3c7471edc6eeeb835a","public:commit:681d50261f37fcb63a8bb81064bcfd64f868a997","public:commit:8e59bb6b6d8213c58553c48ffdd31ae1ba3aaad5","public:commit:a284b8847884d537cf52789d5469f82ad7bc7a81","public:commit:ae4a4af7ffec3cfdd3719720f416a925fd089976","public:commit:d2e67f1506184edddc7f84faf936c8815ff59a1f","public:commit:dcd31c6ac47942595b45fab9ee9765c96ade08f2"],"source_type":"public","date":"2026-06-14","topics":["lifetime","ffi","testing","api","review","networking"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="nn03-an-awaitable-facade-needs-explicit-ownership-readiness-and-shutdown-contracts"></a>
# An awaitable facade needs explicit ownership, readiness and shutdown contracts {#nn03-an-awaitable-facade-needs-explicit-ownership-readiness-and-shutdown-contracts}

## From callback engine to public connections {#from-callback-engine-to-public-connections}

The early implementation has Session, SessionManager, a PeerConnection adapter and a LAN Transport facade. Session is the protocol state machine: it owns negotiation deadlines, distinguishes offer/answer phases, and becomes CONNECTED only after both data channels open. Incoming and outgoing sessions share much of the engine but differ in policy. For example, an incoming listener ignores unicast-delivery error19, while other errors close it. Treating both public connections uniformly does not erase that internal role asymmetry.

The API design in022 reports comparison with BDS connector/network-peer layering and the ergonomics of websockets. The binary/IDA observations are claims in the source document, not binary analysis reproduced by this review. The concrete Python decision is to preserve the callback-driven protocol engine and add Future/Queue-based connect, accept and receive semantics. Connection is the single public per-peer shape. DiscoveredHost carries network identity, opaque advertisement bytes and source address so a later connection can reuse a verified discovery endpoint.

Commit026 implements the facade. A readiness Future signals connection establishment. A per-connection queue carries complete application messages. Closing inserts a sticky sentinel: messages already queued drain first, later recv calls consistently raise ConnectionClosed, and clean async iteration terminates normally. Outgoing connections own their endpoint; accepted connections share their server's endpoint. That ownership distinction prevents closing one accepted client from unconditionally tearing down the entire listener.

## Timeout and close ownership evolve {#timeout-and-close-ownership-evolve}

Session.close is synchronous and idempotent at the state-machine level, but schedules underlying asynchronous WebRTC closure. Its callback therefore indicates logical closure, not necessarily completed teardown. Session.aclose is the path for waiting on the resource operation.

The first readiness implementation shields a Future and adds a callback to consume exceptions. Commit029 simplifies that contract: wait_for owns and cancels the readiness Future directly, and later notifications check done() before setting it. Endpoint shutdown also stops marking every connection closed independently; the engine's close callbacks become the single source of logical closure. This reduces duplicate transitions.

The later HTTP implementation reintroduces shielding for a different object: a shared aiortc close task. Its message identifies cancellation racing native close completion as the problem. The reusable lesson is to assign an owner to each asynchronous operation, not to prefer or prohibit shield globally. Readiness may belong to a caller timeout; shared resource teardown must remain completable when one waiter is cancelled.

## Final state is not fully symmetric {#final-state-is-not-fully-symmetric}

The final LAN Server.aclose sets its closed event, cancels accept/handler tasks, then awaits endpoint closure. It does not gather those cancelled handler tasks. The newer HttpServer.aclose stops signaling, closes sessions first so handlers can finish through ConnectionClosed, cancels stragglers and gathers them. This is a meaningful difference in teardown guarantees despite similar public API shapes. The review did not exercise cancellation or prove a leak; it preserves what each implementation waits for.

Other boundaries remain explicit:
- Pending pre-open packet buffers have a256-message cap per connection ID; live receive queues are unbounded.
- SessionManager routes existing sessions by connection ID without rechecking sender identity. No authenticated sender/session binding follows from this map.
- Unknown numeric CONNECTERROR values can survive the parser but fail public exception formatting that requires error.name.
- send raises when the session is not connected, but does not surface every false result from internal fragmentation.

These are static scope limits useful when extending the API. They are not blanket judgments about production fitness.

## Public migration and tests {#public-migration-and-tests}

Commit027 removes Transport and Session from top-level exports while keeping the advanced internal modules available. Tests explicitly assert that Transport is no longer a top-level name. Examples are rewritten from polling loops to async handlers and context managers; their import tests do not execute main(). The API tests cover local roundtrip, discovery addresses, connection failures, close behavior and a timeout regression. A task-checkbox commit in this chain shares an authored-time tie with an implementation commit, so DAG parents, not presentation order, establish causality.

## Application {#application}

For a callback-to-async wrapper, document separately: the event that establishes readiness, the owner of every shared resource, how queued data behaves at close, and whether close means “requested,” “logically closed” or “teardown completed.” Keep server task reaping separate from connection closure. Test the contract your users depend on, especially timeout/close interleavings, without multiplying redundant cases. This case supports that review checklist; it does not establish a universal preferred framework or authorize inferring broader personal preferences.

Sources: dossiers013,015–019,022–030; final api.py, errors.py and session_manager.py snapshots. Source tests and reported passing counts were read, not executed. These dossiers provide no independent runtime or cross-platform validation.

## Exact commit navigation {#exact-commit-navigation}

- [013 ae4a4af7ffec: feat(session): dialer state machine](../dossiers/013-ae4a4af7ffec.md) · [public source](https://github.com/EndstoneMC/nethernet-python/commit/ae4a4af7ffec3cfdd3719720f416a925fd089976)
- [015 dcd31c6ac479: feat(session): listener state machine](../dossiers/015-dcd31c6ac479.md) · [public source](https://github.com/EndstoneMC/nethernet-python/commit/dcd31c6ac47942595b45fab9ee9765c96ade08f2)
- [016 09e4067b022d: feat(session): SessionManager routing + full in-process handshake](../dossiers/016-09e4067b022d.md) · [public source](https://github.com/EndstoneMC/nethernet-python/commit/09e4067b022dba085057e4d62af5c01bdba29a19)
- [019 5f370a6e389e: feat(api): public Transport facade + LAN examples](../dossiers/019-5f370a6e389e.md) · [public source](https://github.com/EndstoneMC/nethernet-python/commit/5f370a6e389ef6fb9e9611d491a5517e714720f9)
- [022 8e59bb6b6d82: docs(api): public API design — connect/serve/Connection, mirrored from BDS interop](../dossiers/022-8e59bb6b6d82.md) · [public source](https://github.com/EndstoneMC/nethernet-python/commit/8e59bb6b6d8213c58553c48ffdd31ae1ba3aaad5)
- [023 a284b8847884: chore(tasks): mark Task 16 complete](../dossiers/023-a284b8847884.md) · [public source](https://github.com/EndstoneMC/nethernet-python/commit/a284b8847884d537cf52789d5469f82ad7bc7a81)
- [024 d2e67f150618: feat(api): public exception types (NetherNetError/ConnectionFailed/ConnectionClosed)](../dossiers/024-d2e67f150618.md) · [public source](https://github.com/EndstoneMC/nethernet-python/commit/d2e67f1506184edddc7f84faf936c8815ff59a1f)
- [025 449e5d19cda8: feat(api): engine hooks for the public layer (Task 17)](../dossiers/025-449e5d19cda8.md) · [public source](https://github.com/EndstoneMC/nethernet-python/commit/449e5d19cda87a6c6eae67f0fcfcafbcfa66b6b7)
- [026 63cafaa7f81b: feat(api): connect/serve/discover + Connection/Server/DiscoveredHost (Task 18)](../dossiers/026-63cafaa7f81b.md) · [public source](https://github.com/EndstoneMC/nethernet-python/commit/63cafaa7f81b5f96cfe56d3c7471edc6eeeb835a)
- [027 26c265e417b1: feat(api): export public surface; demote Transport to internal (Task 19)](../dossiers/027-26c265e417b1.md) · [public source](https://github.com/EndstoneMC/nethernet-python/commit/26c265e417b1cc44162fe02d93afb7e3c51ea92f)
- [028 681d50261f37: feat(api): client.py + server.py examples; remove host.py/join.py (Task 20)](../dossiers/028-681d50261f37.md) · [public source](https://github.com/EndstoneMC/nethernet-python/commit/681d50261f37fcb63a8bb81064bcfd64f868a997)
- [029 3d968dab941c: refactor(api): simplify Connection connect-wait and endpoint teardown](../dossiers/029-3d968dab941c.md) · [public source](https://github.com/EndstoneMC/nethernet-python/commit/3d968dab941c2f6b45a690b456690bee2fa636ec)
