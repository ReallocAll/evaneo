<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:411"],"source_type":"public","date":"2026-06-02","topics":["ffi","testing","recovery","api","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-411-feat-attribute-attribute-api"></a>
# EndstoneMC/endstone #411: feat(attribute): attribute API {#endstonemc-endstone-411-feat-attribute-attribute-api}

Source: https://github.com/EndstoneMC/endstone/pull/411

## Evidence and attribution {#evidence-and-attribution}

Primary author: wu-vincent. Created 2026-06-02T11:49:26Z; recorded state closed; merged True.

## Lineage and design {#lineage-and-design}

#411 rebases and finishes killcerr's #331, squash-rebasing that work into the first commit with co-author credit. The API lives on Mob because only living entities have attributes. It exposes base/min/max/effective values, modifiers, persistent versus transient insertion and removal by id.

wu-vincent states the earlier hand-written approximation miscomputed MULTIPLY_BASE and omitted redefinition/clamping. The replacement reconstructs native 1.26.x math rather than making platform-specific RVA calls. Namespaced AttributeModifierId maps deterministically to native UUID using SHA1 name generation. Persistence follows Bukkit's method split; Bedrock-only Cap and per-instance min/max preserve native information. OPERAND_CURRENT is an internal invariant, not public surface. getDefaultValue is deliberately omitted because setBaseValue overwrites Bedrock's default and no preserved original exists.

Build and stubgen success is claimed, unlike many unchecked plans. The full patch and test definitions were subsequently inspected below; the claimed runs were not independently executed. Reuse mature API vocabulary only where native semantics match, and expose unavoidable differences explicitly.

## Direct patch findings {#direct-patch-findings}

The final patch makes modifier identity a namespaced key and derives a stable SHA1-name UUID in a fixed namespace, storing the key as native name; persistent/transient insertion differs only in serializable flag and all API-created modifiers address CURRENT. Native-to-public conversion still loses original operand/serialization identity and unknown operations fall back to Add. Math resets from default/base, applies addition, base-scaled multiplication, total multiplication, cap, and native min/max/current retention rules; this corrects the earlier accumulating approximation. Mob::getAttribute wraps a possibly missing mutable attribute instead of returning nullptr, and getAttributes dereferences an unguarded AttributesComponent. Tests only prove nonempty list, health/max-health correspondence, add/remove lookup and remove-by-id; they never dereference the enumerated wrappers or test absent attributes, persistence, cap, modifier interactions or native parity. The key-removal API derives UUID rather than searching the existing native modifier UUID, which only round-trips reliably for modifiers created with this mapping. No static reading establishes claimed runtime fidelity.

### Proxy-iterator correction from exact-head linked code {#proxy-iterator-correction-from-exact-head-linked-code}

The complete attribute_map.h/.cpp and relevant associative_adapter.h iterator definitions were inspected at this PR head. The backing map is brstd::flat_map, whose dereference returns pair<const Key&, T&> (or const T& for const iteration). Therefore auto [id, instance] copies reference-bearing proxy state, not an AttributeInstance; &instance still points into the container. An earlier dangling-copy interpretation was incorrect and is withdrawn. Native container mutation and owner lifetime still govern validity, but the structured binding itself does not establish a dangling pointer. Do not diagnose proxy ranges using ordinary std::map value-copy assumptions.


## Code and verification boundary {#code-and-verification-boundary}

Inspected every hunk of captured PR diff (40621 characters; SHA-256 e48582c75cac669aee8c9b48684a8850fa7a55374ebd519af4fcf93b028aab6d), head fdd0e3d675865a6026b1fe23cd633eff7bbaa385. Scope is this supplied patch, not all linked implementation history. No upstream code was executed and no tests were run in this review. Runtime assertions are source-reported unless explicitly identified as static code findings.

## Traceability {#traceability}


- https://github.com/EndstoneMC/endstone/pull/411
