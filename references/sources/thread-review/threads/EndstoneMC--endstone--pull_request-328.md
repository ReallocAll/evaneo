<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:328"],"source_type":"public","date":"2026-02-11","topics":["lifetime","ffi","testing","api","review","refactoring"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-328-refactor-itemstack-api"></a>
# EndstoneMC/endstone #328: Refactor ItemStack API {#endstonemc-endstone-328-refactor-itemstack-api}

Source: https://github.com/EndstoneMC/endstone/pull/328

## Evidence and attribution {#evidence-and-attribution}

Primary author: wu-vincent. Created 2026-02-11T21:28:12Z; recorded state closed; merged True.

## Discussion disposition {#discussion-disposition}

ItemStack API refactor with no primary reasoning or discussion; code is the substantive source.

The acquired patch is fully inspected below; no test-success claim is independently made.

## Direct patch findings {#direct-patch-findings}

The refactor replaces a polymorphic ItemStack/public-field representation with a concrete deep-copyable value owning private Impl; EndstoneItemStack is the only impl and wraps native ItemInstance. Copy clones, moves transfer ownership, native conversion always copies the native stack and no longer falls back through public reconstruction. This preserves native state more directly and removes external subclassing. Unknown constructor type now throws rather than silently defaulting to air. Inventory returns optional values for absent slots, accepts optional to clear, and add/remove work on value copies with owned leftovers instead of mutating caller pointer inputs. Event drop/consume/cook/interact items become owned snapshots instead of borrowed references. NBT is a semantic breaking change: old toNbt/fromNbt represented the complete stack (Name/Count/Damage/Block/restrictions); new nbt property reads/writes only native user-data compound and empty compound clears it. It is not a compatible serialization replacement. Exact-head setters validate amount1..255 and mask data to15bits; createItemStack(amount) directly invokes native constructor, a separate validation path. Offhand getter still unconditionally wraps an empty native stack into an engaged optional, unlike inventory/armor nullopt checks. getContents removes the slot-pointer null check. isSimilar still compares type/user-data, not aux/data explicitly. No automated tests accompany this large ownership/API migration: needed boundaries include copy isolation, empty offhand, data variants, constructor amount versus setter, event snapshots and NBT compatibility.

## Code and verification boundary {#code-and-verification-boundary}

Inspected every hunk of captured PR diff (83709 characters; SHA-256 3430998a07387687ab07d77c56ad6feef5bfa05723de365850c14dcae6fa8668), head afec3e3d9e7f2860cf7c8416ae0d323e75d15d8f. Additional exact-head context:24 core/inventory/item_stack.cpp setters;102 endstone/metrics/_base.py, __init__.py and util/pointers.h shared ownership. Scope is this supplied patch, not all linked implementation history. No upstream code was executed and no tests were run in this review. Runtime assertions are source-reported unless explicitly identified as static code findings.

## Traceability {#traceability}


- https://github.com/EndstoneMC/endstone/pull/328
