<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:538"],"source_type":"public","date":"2026-09-19","topics":["concurrency","ffi","testing","review","networking"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-538-feat-network-make-nethernet-behave-like-raknet-operationally"></a>
# EndstoneMC/endstone #538: feat(network): make NetherNet behave like RakNet operationally {#endstonemc-endstone-538-feat-network-make-nethernet-behave-like-raknet-operationally}

Source: https://github.com/EndstoneMC/endstone/pull/538

## Evidence and attribution {#evidence-and-attribution}

Primary author: wu-vincent. Created 2026-09-19T11:10:07Z; recorded state closed; merged True.

## Single-port NetherNet with explicit unfinished operational work {#single-port-nethernet-with-explicit-unfinished-operational-work}
Wu targets one forwarded UDP port across concurrent sessions. Native peer-hosted assumptions allocate per-session sockets, advertise only the first, and mishandle shared-socket STUN errors. The transport-factory hook forces global UDP sharing and pins BOTH min/max to signaling port; min0 bypasses SocketCache. A sibling Port's unsigned401 response can consume a peer's outstanding request, so SendBindingErrorResponse401 is suppressed while the owning port still answers.
STUN URI validation and configurable servers defaulting to Google's public STUN are added through SetRelayConfig after level setup; TURN deliberately removed. STUN cannot solve symmetric NAT/CGNAT. The earlier bare server-udp-ports autofill pins both bounds and limited concurrency to one, demonstrated with two clients.
A common anonymous factory implementation is located by invented symbol key/byte pattern, avoiding platform-specific constructor hooks: Linux reaches it via RTTI/vtable slot5. Static66/66 matches and exported detours are claimed. Windows26.51 two-client4-minute/zero-drop/one-port test is reported. Linux was NEVER run, STUN srflx never observed, SERVER_IP may replace rather than augment host candidates, silent signaling-bind failure and offline-mode support are unfinished, changelog omits headline change. The stated Pterodactyl two-device3-minute acceptance test is not completed; 'works on any host' is an aspiration, not established outcome.

## Direct patch findings {#direct-patch-findings}

Full patch removes the Python property-writing helper and its tests, but native transport hook explicitly sets both UDP bounds to HTTP signaling port and global_udp_port=true; reversal is therefore from per-session single-port allocation to a shared socket, not simply reopening the port window. Existing mapped ranges win; otherwise SERVER_IP(non-wildcard) and validated SERVER_PORT map one internal port to external offset. Configuration is mutated through const_cast, depending on the native caller supplying writable storage. STUN config loads at startup and applies after level initialization only for NetherNet; default is Google STUN. Validation rejects non-stun/stuns schemes, @ and ?, but is not full URI validation. A global webrtc::Port hook suppresses every401 response to prevent competing logical ports from rejecting each other's packets; its scope is broader than a session-specific unmatched-ufrag branch. No tests for NAT/shared-socket isolation or real STUN reachability are committed. TOML migration is separately fixed to recurse through tomlkit Table as well as TOMLDocument; build guidance switches project to RelWithDebInfo. Platform layouts/signature reconstruction are included, not independently validated against binaries here.

## Code and verification boundary {#code-and-verification-boundary}

Inspected every hunk of captured PR diff (32659 characters; SHA-256 cf7462a172694de98629ce0ad697fad9025aa207da76266d551c569f21d2d6c3), head e56afb7a2614f8634c4fca52f7620261e781a015. Scope is this supplied patch, not all linked implementation history. No upstream code was executed and no tests were run in this review. Runtime assertions are source-reported unless explicitly identified as static code findings.

## Traceability {#traceability}


- https://github.com/EndstoneMC/endstone/pull/538
