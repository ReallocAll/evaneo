<!-- retrieval: {"source_ids":["public:commit:0e8cdf79ae7ecee399a51f7095352fa3d27fc72d","public:commit:20805f067e220cdd9819e61ca6d6d1b53a681bf0","public:commit:2f2490716d205b39ba1fb1489c0458e55d5b988f","public:commit:38a7ec24b160ba9f32c5d790f05aaf0f2c623dd5","public:commit:5668c72caeaa78eec07f8544888f6c82f5c1e1ee","public:commit:6cc1b8b00bc726529db4f141f2efea4505435dc3","public:commit:75bf7f6471f24558af413f73ed4b81307d195c9d","public:commit:9fff5293143677b5fbcf74bc5c1fe549358965bf","public:commit:a65484948c1e634e780cc73d50177a1a9b2849bc","public:commit:b6d4b7e4d6f6d76e8b986a742862125ff8b6bce4","public:commit:bf6441779109ba9952a57bdf3b8db9422b0d4bcd","public:commit:f120c20a18b2cfc7d25a010b4f7d8f80481a61dd","public:commit:f394cb348f8471d5b298d1b4ecf0f68252fb7272","public:commit:fc1242f2972d3bed6cc25b55693c498d2f0450d2"],"source_type":"public","date":"2024-06-04..2024-06-16","topics":["ffi","testing","api","review","refactoring","networking"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
# Permission, server and Python boundary corrections {#permission-server-and-python-boundary-corrections}

## Decision chain and usable conclusions {#decision-chain-and-usable-conclusions}

The strongest result is a sequence of integration corrections, not a claim that the permission feature was complete when first declared. Ordinal 1081 derives per-command defaults from the native signature and registers a structured permission tree. Prior ordinal 1067 had already assigned BedrockCommand a permission name, but used the plural namespace. The mismatch remains through the 0.4.8 release work and is corrected by 1153; 1155 explicitly calls it a regression. The relevant abstraction spans constructor, registry, lookup and permission defaults. Reviewing one local function would miss the failure. Prior 1078/1080 deliberately preserve the native path when command/sender mapping is unavailable, so the changelog's broad permission wording must not erase that scope.

A second, independent correction changes permission accumulation from first insertion wins to later assignment wins (1154). The full PermissibleBase source establishes the order: clear old subscriptions/state, visit defaults, then ordered attachments, recursively calculate children with inversion. An attachment denying an already default-granted permission is the concrete counterexample to emplace. Replacement is necessary to honor that later decision. It also means callers retaining PermissionAttachmentInfo pointers across recalculation cannot assume stable objects, as before clearPermissions already destroyed them. Nothing here establishes a total ordering for conflicts between different entries in unordered child/default sets or checks recursive cycles. These are limits of the observed fix, not reasons to expand this historical review into an audit.

Python name/UUID lookup similarly crosses layers. The new native name API does a case-insensitive exact linear search and returns null when absent; Python binding order initially exposes the existing caster defect. The first response (1095) moves the string overload and disables UUID conversion. The later response (1150) fixes two concrete caster mistakes: bytes is a property, not a callable method, and a false error indicator means successful conversion. Adding noconvert to both overloads restricts coercion rather than making malformed Python C API intermediates safe. The release records the UUID crash as fixed; there is no reproduced runtime result in this unit. Static stubs still give an unconditional Player result. Use this family when reasoning about overload resolution, error-indicator conventions and keeping binding/type-stub contracts honest.

Server networking access evolves from per-player plumbing to a central GameSession-derived handle. That simplifies kick and max-player operations but relies on startup state: Minecraft can return null before a session and EndstoneServer dereferences it. NonOwnerPointer's implementation contains shared_ptr storage; adding a null constructor does not establish benign ownership for its existing reference constructor. Host-created pointer/control-block conventions were not observed. Capacity mutation combines a public bound, native max_players write, server-announcement hook and larger RakPeer connection capacity. All pieces matter. The temporary macro syntax error is repaired separately. The cap is inclusive 200, accepts zero, and invalid calls log/return rather than throw.

API evolution also includes method-to-property asynchronous and op-to-is_op renames. These are deliberately retained as compatibility effects even though the diffs are tiny. The module cleanup removing HumanActor aligns an older hierarchy removal. Test files in this family mainly update mocks/interface conformance; they are not evidence of new end-to-end permission/name lookup coverage.

## Evidence and limits {#evidence-and-limits}

Primary evidence is each actual parent-relative patch, full command_map/server/permission/caster context, and contemporaneous release text. Vincent authors these target changes; GitHub is committer for web-edited metadata where shown in the ledger. No reviewer objections or private motives are reconstructed. Before/after alternatives are the actual implementations above. No live Bedrock, Python extension, C++ build or tests were executed. See the linked prior unit for the original command-origin/fallback chain; its findings are not re-attributed to this chunk.

## Commit-by-commit dispositions {#commit-by-commit-dispositions}

<a id="commit-1081"></a>
### 1081: feat: register permissions for vanilla commands {#commit-1081}

Source: [9fff5293143677b5fbcf74bc5c1fe549358965bf](https://github.com/EndstoneMC/endstone/commit/9fff5293143677b5fbcf74bc5c1fe549358965bf) · 2024-06-04T05:57:20Z · substantive

Registers a minecraft permission root, minecraft.command parent and one child per native signature. Defaults follow native permission level: Operator above Any, otherwise True; aliases continue sharing the same command object. Recalculates the two parent nodes after registering children. The earlier BedrockCommand constructor still asks for minecraft.commands.<name>, a plural/singular mismatch repaired at 1153, so this commit alone does not establish correct enforcement.

<a id="commit-1084"></a>
### 1084: fix: remove HumanActor in actor.py {#commit-1084}

Source: [2f2490716d205b39ba1fb1489c0458e55d5b988f](https://github.com/EndstoneMC/endstone/commit/2f2490716d205b39ba1fb1489c0458e55d5b988f) · 2024-06-04T09:53:44Z · corrective

Removes obsolete HumanActor from Python actor imports and exports after its earlier C++/binding removal at 1018. This closes a stale public-module import surface; it is not a second redesign of actor inheritance.

<a id="commit-1089"></a>
### 1089: feat: add EndstoneServer::getServerNetworkHandler {#commit-1089}

Source: [bf6441779109ba9952a57bdf3b8db9422b0d4bcd](https://github.com/EndstoneMC/endstone/commit/bf6441779109ba9952a57bdf3b8db9422b0d4bcd) · 2024-06-04T10:30:34Z · substantive

Centralizes server-network-handler access through Minecraft/GameSession. Removes the per-player raw handler and login-time initialization; kick now obtains the handler from EndstoneServer. This closes the earlier temporary per-player routing TODO but the server accessor dereferences the possibly null non-owner pointer without a new lifecycle guard.

<a id="commit-1091"></a>
### 1091: feat: add Server::getPlayer by player name {#commit-1091}

Source: [f120c20a18b2cfc7d25a010b4f7d8f80481a61dd](https://github.com/EndstoneMC/endstone/commit/f120c20a18b2cfc7d25a010b4f7d8f80481a61dd) · 2024-06-04T12:30:02Z · substantive

Adds exact-name, case-insensitive Server::getPlayer alongside UUID lookup, using boost::iequals over the online-player map and nullptr when absent. Python overloads, stub and mocks are updated. Initial UUID-first overload registration interacts badly with the custom caster; 1095 and 1150 are necessary follow-ups, not independent unrelated fixes. The stub return type is not Optional despite the null result.

<a id="commit-1095"></a>
### 1095: fix: SystemError when getting player by name with Python {#commit-1095}

Source: [20805f067e220cdd9819e61ca6d6d1b53a681bf0](https://github.com/EndstoneMC/endstone/commit/20805f067e220cdd9819e61ca6d6d1b53a681bf0) · 2024-06-06T14:53:41Z · corrective

Addresses the stated get_player(name) SystemError by registering the string overload before UUID and marking UUID noconvert. This limits conversion attempts but does not fix the UUID caster implementation itself; 1150 corrects its attribute access and success return.

<a id="commit-1097"></a>
### 1097: fix: Event.asynchronous is now a property rather than a method {#commit-1097}

Source: [fc1242f2972d3bed6cc25b55693c498d2f0450d2](https://github.com/EndstoneMC/endstone/commit/fc1242f2972d3bed6cc25b55693c498d2f0450d2) · 2024-06-06T19:05:24Z · api_change

Changes Python Event.asynchronous from a method to a read-only property and aligns the stub/docstring. Event scheduling is unchanged, but callers using parentheses need migration; no compatibility alias is introduced.

<a id="commit-1099"></a>
### 1099: feat: add Server::getMaxPlayers {#commit-1099}

Source: [b6d4b7e4d6f6d76e8b986a742862125ff8b6bce4](https://github.com/EndstoneMC/endstone/commit/b6d4b7e4d6f6d76e8b986a742862125ff8b6bce4) · 2024-06-06T20:57:10Z · substantive

Adds Server::getMaxPlayers, Python max_players and test mocks, delegating to native handler state. It exposes a read-only capacity initially; the mutation and advertised-server update arrive at 1108–1109.

<a id="commit-1107"></a>
### 1107: feat: add ServerNetworkHandler::updateServerAnnouncement {#commit-1107}

Source: [6cc1b8b00bc726529db4f141f2efea4505435dc3](https://github.com/EndstoneMC/endstone/commit/6cc1b8b00bc726529db4f141f2efea4505435dc3) · 2024-06-08T18:01:17Z · substantive

Makes EndstoneServer a friend of native ServerNetworkHandler, removes the temporary public getter, adds updateServerAnnouncement hook and two platform manifest entries. Semantic TOML comparison proves all 40 prior offsets per platform unchanged despite regrouping. This prepares synchronized max-player mutation.

<a id="commit-1108"></a>
### 1108: feat: add Server::setMaxPlayers {#commit-1108}

Source: [5668c72caeaa78eec07f8544888f6c82f5c1e1ee](https://github.com/EndstoneMC/endstone/commit/5668c72caeaa78eec07f8544888f6c82f5c1e1ee) · 2024-06-08T18:06:31Z · substantive

Adds setMaxPlayers with accepted range 0..200; negative values log an error and over-limit values a warning, both leave state unchanged. Accepted values write native max_players and refresh the announcement. RakPeer startup copies connection definitions and raises capacity to 200 before calling original startup. Initial macro contains a trailing semicolon, fixed at 1109; this intermediate source is not represented as independently buildable.

<a id="commit-1109"></a>
### 1109: feat: add python bindings for Server::setMaxPlayers {#commit-1109}

Source: [75bf7f6471f24558af413f73ed4b81307d195c9d](https://github.com/EndstoneMC/endstone/commit/75bf7f6471f24558af413f73ed4b81307d195c9d) · 2024-06-08T18:10:47Z · corrective

Exposes the max_players setter to Python/stub and removes the erroneous semicolon from ENDSTONE_MAX_PLAYERS. Distinguish the syntactic repair from the intentional inclusive 200 cap; runtime capacity validation was not executed.

<a id="commit-1150"></a>
### 1150: fix: get player by uuid no longer crashes {#commit-1150}

Source: [38a7ec24b160ba9f32c5d790f05aaf0f2c623dd5](https://github.com/EndstoneMC/endstone/commit/38a7ec24b160ba9f32c5d790f05aaf0f2c623dd5) · 2024-06-15T00:16:01Z · corrective

Fixes UUID loading to read the bytes property rather than call it and returns success only when PyErr_Occurred is null. Marks the name overload noconvert too. Full caster context shows reference cleanup on normal paths, but missing null/type guards around Python C API intermediate results remain outside this fix. The release later reports UUID lookup no longer crashes; this is not an independently reproduced outcome.

<a id="commit-1153"></a>
### 1153: fix: vanilla command permissions {#commit-1153}

Source: [a65484948c1e634e780cc73d50177a1a9b2849bc](https://github.com/EndstoneMC/endstone/commit/a65484948c1e634e780cc73d50177a1a9b2849bc) · 2024-06-15T20:38:07Z · corrective

Changes BedrockCommand permissions from minecraft.commands.<name> to minecraft.command.<name>, aligning 1067's checked permission with 1081's registrations. This precisely repairs the observed namespace mismatch; it does not expand sender conversion or eliminate native fallback paths.

<a id="commit-1154"></a>
### 1154: fix: permission attachment now works as expected {#commit-1154}

Source: [f394cb348f8471d5b298d1b4ecf0f68252fb7272](https://github.com/EndstoneMC/endstone/commit/f394cb348f8471d5b298d1b4ecf0f68252fb7272) · 2024-06-15T20:57:18Z · corrective

Replaces emplace with assignment in permission recalculation and recursive children. Full context confirms defaults are visited before attachments, so later attachment values can now replace an existing default/key rather than silently losing to first insertion. Child inversion and subscription bookkeeping stay intact; this does not establish deterministic precedence among conflicting unordered sibling branches.

<a id="commit-1164"></a>
### 1164: refactor: rename Permissible's property `op` to `is_op` {#commit-1164}

Source: [0e8cdf79ae7ecee399a51f7095352fa3d27fc72d](https://github.com/EndstoneMC/endstone/commit/0e8cdf79ae7ecee399a51f7095352fa3d27fc72d) · 2024-06-16T22:56:08Z · api_change

Renames the Python Permissible property op to is_op with matching setter/stub. C++ isOp/setOp are unchanged and no alias is kept; this is a caller-facing compatibility change, not permission-engine correction.
