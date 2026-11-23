<!-- retrieval: {"source_ids":["public:commit:108e47f98d075823307e00b022a719adf646fa51","public:commit:1dfc7176be230a6bbf2b9c54ae30d8de331de55c","public:commit:6a4a825f372d636a39f7b7ed1bb9a0d6cf45a4a7","public:commit:9d28eeab006debc63c5484097bd00c0b28bed33d","public:commit:efebe355fde2f82a1a9ba18d38dde08f5a80f9c3","public:thread:EndstoneMC/endstone:91"],"source_type":"public","date":"2024-11-15..2025-01-25","topics":["lifetime","ffi","testing","api","review","selection"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
# Damage sources and causal actor identity {#damage-sources-and-causal-actor-identity}

<a id="requirement-and-attribution"></a>
## Requirement and attribution {#requirement-and-attribution}

Issue91 was opened by umarurize asking for the actor causing ActorDeathEvent and an is_player attribute. xXLarryTFVWXx suggested Python isinstance against Player. Vincent later linked the exact194 commit as completion, documented event.damage_source.actor, and reiterated isinstance rather than adding the requested boolean. The captured primary and both comments were read; this preserves the requester's and collaborator's contribution rather than turning the outcome into a unilateral preference. Source: https://github.com/EndstoneMC/endstone/issues/91 .

## Implementation and tradeoffs {#implementation-and-tradeoffs}

169 first replaces abstract native damage-source placeholders with cause classification, mitigation rules and translated death-message selection.191 introduces a public DamageSource separating the responsible actor from the directly damaging actor, with projectile attribution as its documented example;192 makes the module discoverable.193 maps native causes to public strings and resolves actor IDs on demand from the current level.194 passes the wrapper through ActorDeathEvent/PlayerDeathEvent and implements the fall-distance accessor needed by169.

The abstraction expresses causal identity more precisely than a single killer field. It also has failure modes: actor resolution may return null; both missing actors compare equal and make isIndirect false; map.at rejects unknown future native causes; native-source subclass behavior and translation parity are untested. The initially nonnullable stubs should not be taken as proof that an actor exists.

Most importantly, ActorDeathEvent owns a unique_ptr to EndstoneDamageSource, while EndstoneDamageSource owns no native payload: it contains ActorDamageSource&. Python damage_source uses reference rather than reference_internal. Thus neither the event's unique_ptr nor the Python handle independently preserves the native event's damage object. Retaining damage_source outside the synchronous callback needs a snapshot/clone or an explicit lifetime arrangement; the reviewed implementation does not supply that guarantee. This is a concrete boundary analysis, not an observed use-after-free report.

## Apply to a new task {#apply-to-a-new-task}

Separate causal actor, direct actor and environmental damage; define unknown/missing actor semantics; retain cause and ID snapshots when callbacks can escape; decide whether a polymorphic clone preserves derived state; and test new native causes and removed actors. Use the request and completion comments as reported product intent, not as runtime validation. No tests, plugin execution or vendor binary comparison were performed here.


## Per-commit evidence {#per-commit-evidence}

<a id="commit-169"></a>
### Commit 169 {#commit-169}

1dfc7176be230a6bbf2b9c54ae30d8de331de55c · 2025-01-24T15:02:45Z

[feat: implement `ActorDamageSource`](https://github.com/EndstoneMC/endstone/commit/1dfc7176be230a6bbf2b9c54ae30d8de331de55c)

**Observed change.** Implements native ActorDamageSource base classification, cause enum, default invalid actor IDs, clone, mitigation exceptions and death translation key selection including fall-distance handling. Adds fall-distance accessor declaration.

**Causal interpretation.** Prepares a meaningful damage description instead of opaque source bytes; translation and classification are policy, not simply layout declarations.

**Limits.** Base clone copies base state; subclass semantics depend on native overrides. Actor fall-distance body arrives194. No native-parity or translation test.

<a id="commit-191"></a>
### Commit 191 {#commit-191}

6a4a825f372d636a39f7b7ed1bb9a0d6cf45a4a7 · 2025-01-25T20:47:35Z

[feat(damage): add DamageSource API](https://github.com/EndstoneMC/endstone/commit/6a4a825f372d636a39f7b7ed1bb9a0d6cf45a4a7)

**Observed change.** Adds public/Python DamageSource with damage type, responsible actor, directly damaging actor and indirect classification; cause getters/setters added natively. Public comments explain projectile owner versus projectile.

**Causal interpretation.** Separates causal attribution from immediate collision object instead of overloading one actor field, supporting the original death-source feature request.

**Limits.** Actor getters can return null but initial stubs declare Actor. Implementation comes193; bindings use borrowed reference policies.

<a id="commit-192"></a>
### Commit 192 {#commit-192}

108e47f98d075823307e00b022a719adf646fa51 · 2025-01-25T21:14:26Z

[feat(damage): add endstone.damage python module](https://github.com/EndstoneMC/endstone/commit/108e47f98d075823307e00b022a719adf646fa51)

**Observed change.** Adds endstone.damage re-export module and documentation navigation/reference entry.

**Causal interpretation.** Makes the191 API discoverable through the documented Python package, rather than only the private extension.

**Limits.** No executable usage example or generated-doc verification; concise integration disposition.

<a id="commit-193"></a>
### Commit 193 {#commit-193}

efebe355fde2f82a1a9ba18d38dde08f5a80f9c3 · 2025-01-25T23:02:47Z

[feat(damage): implement DamageSource](https://github.com/EndstoneMC/endstone/commit/efebe355fde2f82a1a9ba18d38dde08f5a80f9c3)

**Observed change.** Implements EndstoneDamageSource around borrowed ActorDamageSource&, maps cause to cached string_view, lazily resolves responsible/direct actors via current level, and defines indirect by resolved-pointer inequality. Adds string formatter/binding.

**Causal interpretation.** Keeps native classification with the event but avoids retaining actor ownership; causal IDs can resolve to null when actors are gone. A wrapper owning itself does not own the payload it references.

**Limits.** Cause map.at throws for unknown future values. If both actors fail resolution indirect becomes false. Reference lifetimes require callback discipline. Formatter has doubled comma fixed194; no tests.

<a id="commit-194"></a>
### Commit 194 {#commit-194}

9d28eeab006debc63c5484097bd00c0b28bed33d · 2025-01-25T23:20:30Z

[feat(damage): add damage source to `ActorDeathEvent` and `PlayerDeathEvent`](https://github.com/EndstoneMC/endstone/commit/9d28eeab006debc63c5484097bd00c0b28bed33d)

**Observed change.** ActorDeath/PlayerDeath now own unique_ptr<DamageSource>; handlers construct EndstoneDamageSource from native payload, expose damage_source with Python reference policy, and add FallDistanceComponent/getter needed169. Fixes formatter/stub. Complete#91 is exact link to this SHA.

**Causal interpretation.** Feature requested by umarurize; xXLarryTFVWXx suggested isinstance for player detection, which Vincent reiterated rather than adding is_player. Responsible actor access is delivered through damage_source.actor.

**Limits.** The owning unique_ptr owns only the wrapper; it still borrows native damage source. Python property reference does not keep event/native payload alive, so retention beyond callback is unsafe absent other lifetime guarantees. Author's completion statement is not runtime verification.
