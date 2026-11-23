<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:504"],"source_type":"public","date":"2026-08-20","topics":["ffi","testing","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-504-feat-event-add-playershearactorevent"></a>
# EndstoneMC/endstone #504: feat(event): add PlayerShearActorEvent {#endstonemc-endstone-504-feat-event-add-playershearactorevent}

Source: https://github.com/EndstoneMC/endstone/pull/504

## Evidence and attribution {#evidence-and-attribution}

Primary author: wu-vincent. Created 2026-08-20T17:53:56Z; recorded state closed; merged True.

## Native semantic boundary for shearing {#native-semantic-boundary-for-shearing}
Wu preserves the contributor's actor/item/hand cancellable event while replacing the hook mechanism. Native Player interaction reaches PlayerInteractionSystem and then InteractComponent::getInteraction once per interaction, not per tick, so no extra listener guard is needed for tick hot paths. The original must succeed and expose behavior-pack text shear or mooshear; that also covers compatible add-ons. Cancellation sets failure and suppresses the interaction before its deferred callback. Drops do not yet exist here and are intentionally excluded rather than imitating loot logic.
The symbol recipe cannot use those text literals because they live in packs, not the binary. It uses telemetry actor IDs 0x30B74/0x30B2C seven bytes apart, a +0x48 access and 0x140 stride as structural confirmation. Reported uniqueness holds on 26.44/40 both platforms but Windows26.33 has two matches, an explicit version limit. Claude assistance is disclosed.

## Direct patch findings {#direct-patch-findings}

Final hook calls the original InteractComponent::getInteraction first, exits on unsuccessful interactions, and matches behavior text shear, mooshear, plus take_sulfur_cube (the last extends beyond the body summary). It emits a cancellable event with non-null player/actor, copied current carried ItemStack, and fixed EquipmentSlot::Hand; this is not verified off-hand coverage. Cancellation suppresses interaction and returns Failure. Exports, stubs, headers, CMake and symbol configuration accompany the change. ActorInteraction Windows size is corrected to104, Linux112. Symbol-discovery recipe records the Windows26.33 ambiguity. There are no committed event tests in this patch, and no new execution was performed.

## Code and verification boundary {#code-and-verification-boundary}

Inspected every hunk of captured PR diff (16643 characters; SHA-256 b8fc117fe29e57b83f3823611a26fb94cf29b335a97e2078b9763157cb09ef97), head c324083cc380081c5655ef02c938b4344e2a3ab6. Scope is this supplied patch, not all linked implementation history. No upstream code was executed and no tests were run in this review. Runtime assertions are source-reported unless explicitly identified as static code findings.

## Traceability {#traceability}


- https://github.com/EndstoneMC/endstone/pull/504
