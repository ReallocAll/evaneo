<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:518"],"source_type":"public","date":"2026-08-28","topics":["lifetime","ffi","testing","build","api","review","networking"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-518-feat-add-support-for-bds-1-26-45"></a>
# EndstoneMC/endstone #518: feat: add support for BDS 1.26.45 {#endstonemc-endstone-518-feat-add-support-for-bds-1-26-45}

Source: https://github.com/EndstoneMC/endstone/pull/518

## Evidence and attribution {#evidence-and-attribution}

Primary author: wu-vincent. Created 2026-08-28T21:44:56Z; recorded state closed; merged True.

Wu's26.45 port combines protocol2168→2169 with IPv6 opt-out. Source claims61 symbols per platform matched, function starts checked against .pdata/eh_frame and >=0.89 body similarity across four RVA bands; an existing randomTick thunk lacks the ordinary function metadata and is explicitly treated as an exception. Vtables reportedly unchanged. Exact26.44 clients are accepted with login/settings version rewriting; only their RemoveScore wire format receives the extra prefix because26.45 removed it. Linux settings-payload layout is cross-checked against another packet, Windows payload begins+48/serial+52. IPv6 defaults off for hosts where binding fails and can be opted into. RelWithDebInfo build and306 tests are reported, but no live server test. Two functional cherry-picks are named separately from excluded style churn.

## Full patch and compatibility shims {#full-patch-and-compatibility-shims}

All35909characters were inspected, including both61-entry platform symbol-table changes. This is a protocol2168→2169 upgrade, not only a version bump. For26.40–26.44 clients, settings dispatch rewrites2168 to2169; login must instead be patched in the raw packet buffer before native decoding because mismatched version causes native LoginPacket to discard its connection request. The helper bounds-checks four bytes and writes network-order version only for exactly2168. A cached dispatcher retains a reference to the original native handler; its lifetime and concurrent initialization are assumptions, not tested here.

26.44 alone had inserted an extra true marker before scoreboard removal objective names;26.45 removes it again. The previous downgrade for26.40–43 is therefore reversed: only clients reporting exact SemVersion1.26.44 get the extra marker inserted. The shim is scheduled for removal at26.50, together with the handshake override. Compatibility relies on the asserted otherwise-identical wire schema and accurate client version; no per-version fixture, malformed payload test or join/scoreboard matrix is added.

IPv6 listening becomes opt-in through network.ipv6=false, with runtime explicitly linked to tomlplusplus. RakPeerHelper temporarily swaps its IP-support pointer to a stack object while calling original peerStartup, then restores it. The replacement reads endstone.toml on startup, defaults to IPv4-only for missing/false value and parse errors, never requests IPv6-only, and supplies zero default ports. It applies outside the gameplay-only incoming-datagram branch too. Pointer restoration is not RAII if the original throws, and stack lifetime assumes the native call does not retain the support pointer. This is a deployment behavior change for existing IPv6 users; the changelog explicitly labels it breaking. No startup/port-retention/IPv6-enabled regression tests are present.


## Code and verification boundary {#code-and-verification-boundary}

Inspected every hunk of captured PR diff (35909 characters; SHA-256 9d004a32a28effa3c21dd3ea1101f292cd14f92225af3ce9689afe3ca03a945f), head f9b2bc54cf6b5dd4b0c515578364c71658bf8fb3. No upstream code was executed and no tests were run in this review. Runtime assertions are source-reported unless explicitly identified as static code findings.

## Traceability {#traceability}


- https://github.com/EndstoneMC/endstone/pull/518
