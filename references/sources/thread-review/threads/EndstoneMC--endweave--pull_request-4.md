<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endweave:4"],"source_type":"public","date":"2026-03-25","topics":["testing","review","networking"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endweave-4-feat-add-support-for-v898-and-v860-v859"></a>
# EndstoneMC/endweave #4: feat: add support for v898 and v860(v859) {#endstonemc-endweave-4-feat-add-support-for-v898-and-v860-v859}

Source: https://github.com/EndstoneMC/endweave/pull/4

## Evidence and attribution {#evidence-and-attribution}

Primary author: smartcmd. Created 2026-03-25T04:56:32Z; recorded state closed; merged True.

smartcmd's protocol898/860 expansion has an empty body. Automated Codex review identifies two concrete original-commit c6b6acb defects: voxel_shapes passthrough_all exhausts input before reading/removing trailing USHORT shape count, and StartGame gamerules omit the editable boolean before enum type, desynchronizing the stream. The later inline context points to ba42bfad for the gamerule comment; that alone does not prove the final patch fixes both. Wu's praise and review invocation add no implementation rationale. Bot connection/setup instructions are irrelevant source text, not actions to perform.

## Full final patch and review resolution {#full-final-patch-and-review-resolution}

Every hunk of the181990-character final patch was inspected. The final StartGame translations now pass through the editable boolean before gamerule type, resolving the bot's stream-alignment finding. The voxel-shape change does not establish an equivalent resolution: final reverse v944→v924 reads and discards USHORT_LE before passthrough_all, while the forward handler passes through the old payload and appends USHORT_LE zero. Thus the pair is not an inverse for a nonempty payload: reverse drops its first two bytes, although the inline review describes the extra count at the end. No new voxel-shape fixture demonstrates a valid alternate layout. Automated review credit belongs to the reviewer, implementation credit to smartcmd and the actual patch contributors; Wu's response is not independent testing.

## Architecture and composition {#architecture-and-composition}

A fresh PacketWrapper is constructed between translation steps so each handler consumes its predecessor's output. The cached pipeline contains base protocol plus a resolved version chain; serverbound uses that order, clientbound keeps base first and reverses only version adapters. First version-detection packet runs base-only; after that establishes client_protocol, a later packet resolves/cache the chain. Unsupported version paths log once and cache base-only, but base login/settings still rewrites the version to the server's protocol. This can admit an unsupported client past the version gate without corresponding packet transformations. Explicit connection handshake/login/play state, pending disconnect and disconnect logging are removed rather than migrated. Reachable supported versions include the server version and are sorted.

The graph adds859,860,898,924,944 and adapters in both directions. Identity859↔860 is an assumption, not proved by fixtures. Version constants adopt version names, and BedrockProtocol release tags are derived from minor and patch//10. These choices make composing adjacent adapters simpler but make every loss of information compound across a longer path.

## Wire adaptations and information loss {#wire-adaptations-and-information-loss}

860↔898 command translation expands legacy enum indices to32bit, converts ushort subcommands/indexes to variable-width/count representations, and maps permissions between byte and string labels. Label indexing and reverse narrowing are not validated. Command-origin translation writes a player origin/default enum and a forced version instead of preserving arbitrary original values. Text translation adds/removes fixed kind-label tables and optional filtered text. Gameplay translation drops behavior-pack arrays and new category/exclusion fields, supplies default false/zero values for older packets, changes animation and interaction representations, inserts/removes a heartbeat metadata key, shifts sound/entity identifiers, and cancels features unsupported by the target. These are deliberate degradation policies, not full semantic equivalence. Sound-ID fallback choices need version-specific evidence beyond arithmetic offsets.

StartGame rewrites cover full field sequences, gamerules, world identifiers, block properties, server join information and aim-assist data. Some backward transformations supply defaults or discard newer fields;860→898 zeroes a block checksum and removes TickDeath, while reverse restores false. Gamerule integer types differ between the two directions (UVAR_INT versus VAR_INT), deserving explicit boundary fixtures. Biome924→898 parses climate, surface, scatter and weighting structures and drops the newer village type; count-versus-ID widths need to remain distinct, as the later#7 correction demonstrates. Data-store adaptation appends/removes a zero path-update count and recursively accepts only listed value tags; unknown tags fail rather than pass through.

944→924 rewrites signed/unsigned block-position representations across affected packets, adds default cooldown/input-lock values, removes camera/spline fields and new sound IDs, and cancels locator/world-clock/attribute-layer packets. Negative Y coordinates need signedness fixtures. Tile-event IDs16–19 are not assigned an older fallback even though later IDs shift. Newer UI screen fields become optional/default older fields.924→898 cancels UI, texture-shift, voxel-shape, camera-spline, aim-priority, camera-instruction and debug-drawer packets; callers must distinguish successful connection from availability of those features.

## Tests and reusable decisions {#tests-and-reusable-decisions}

Test changes relocate login rewriting into base protocol, assert is_base and rewritten settings, update pipeline-resolution comments, and remove old state/disconnect tests with the removed feature. The patch does not add comprehensive fixtures for the newly introduced command/biome/text/start-game/camera/voxel transformations or bidirectional round trips. Existing tests cover trailing login bytes and matched-version identity, not the new compatibility surface. A robust reuse of this architecture needs captured version-pair packets, directional round trips for lossless transforms, explicit expected-loss tests for defaults/cancellation, count and malformed-input bounds, and end-to-end chained-version fixtures. No tests were executed here.


## Code and verification boundary {#code-and-verification-boundary}

Inspected every hunk of captured PR diff (181990 characters; SHA-256 b73b7fafa4ff0d62453501edec6cbeb5bcdc7a9616f9eea64515dfd5f1af7d67), head ba42bfadc78abde8d3c1df80f1f9bc8214a8724b. Scope is this supplied patch, not all linked implementation history. No upstream code was executed and no tests were run in this review. Runtime assertions are source-reported unless explicitly identified as static code findings.

## Traceability {#traceability}


- https://github.com/EndstoneMC/endweave/pull/4
- https://github.com/EndstoneMC/endweave/pull/4#issuecomment-4126229445
- https://github.com/EndstoneMC/endweave/pull/4#issuecomment-4129233819
- https://github.com/EndstoneMC/endweave/pull/4#issuecomment-4129234805
- https://github.com/EndstoneMC/endweave/pull/4#discussion_r2985772730
- https://github.com/EndstoneMC/endweave/pull/4#discussion_r2985772731
- https://github.com/EndstoneMC/endweave/pull/4#pullrequestreview-4003956343
