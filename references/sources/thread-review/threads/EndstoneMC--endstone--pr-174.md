<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:174"],"source_type":"public","date":"2025-04-16","topics":["lifetime","ffi","testing","review","networking"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-174-feature-1-21-80-support"></a>
# EndstoneMC/endstone #174: [feature] 1.21.80 support {#endstonemc-endstone-174-feature-1-21-80-support}

Source: https://github.com/EndstoneMC/endstone/pull/174

## Review scope and state {#review-scope-and-state}

- Thread author: wu-vincent; state at review: closed; merged: True.
- Evidence: Public PR and patch reviewed statically (577 additions, 315 deletions, matching recorded metadata); no code execution or tests were performed.
- Limits: Source snapshot only; no independent runtime verification.

## Engineering reading and attribution {#engineering-reading-and-attribution}

Wu's merged 55-file 1.21.80 support PR has an empty description and no substantive human discussion or review. Its one Codecov comment reports 0.00% project coverage; that report cannot establish native runtime or ABI correctness.

### Complete patch inspection {#complete-patch-inspection}

The advertised 1.21.80 port actually pins 1.21.80-preview.28 in both package metadata and the symbol table. EntityRegistry enables its explicitly preview-only viewing field. Reusing this exact declaration set against stable or later builds is therefore unsafe without another comparison. Windows/Linux addresses are updated, including the Linux Pack::createPack signature acquiring an explicit I/O provider; the obsolete Windows fabricated AppPlatformIOProvider-vtable path is removed.

Pack ownership becomes explicit: EndstoneServer clones an I/O provider from the native pack-source factory, transfers it to EndstonePackSource, and passes it through every pack creation. The repository gains command-pipeline context and reference-valued collaborators; reports reorder flags and remove a virtual reload slot. This is an adaptation of the native subsystem, not a new portable resource-pack specification.

Native networking grows NetherNet identity from a plain 64-bit value to a 24-byte discriminated P2P/Realms identity, shifting NetworkIdentifier and dependent containers. ServerNetworkHandler moves the clients map near its beginning and gains an asynchronous join task group. CommandParameterData gains custom-storage getter/is-set pointers; MinecraftCommands acquires a context provider and reorders registry/output ownership. These changes illustrate why address updates alone cannot complete a port.

Publisher declarations now distinguish single-threaded, multithreaded and strict modes and carry return-policy/subscription-body types. Container switches to the single-threaded publisher representation and adds virtual slot queries; Player replaces its opaque UI-container storage with the declared object. EventCoordinator loses the non-owner-reference base, reducing scoreboard sizes. ItemDescriptor names return by value rather than reference; ItemGroup count becomes optional. Actor motion signatures, mob death component, level virtuals, block tick slot, packet/data/flag/game-rule IDs are also adjusted. These are source layout observations with size assertions, not measured correctness. No new tests establish binary interoperability, and there is no human rationale to attribute beyond the port itself.

Exact inspected base/head: 8095d769c2927df8bf15b42bf242beefb2cc5688…459ca70abac9dcb5aa439b5e6242748fc3d61159. The complete PR diff was inspected; no upstream code or tests were executed.


## Source index {#source-index}

- https://github.com/EndstoneMC/endstone/pull/174
- https://github.com/EndstoneMC/endstone/pull/174#issuecomment-2853678481
