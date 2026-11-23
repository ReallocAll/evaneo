<!-- retrieval: {"source_ids":["public:commit:2dbd28f7a9b28ab0e2d9cab6ae9e5867b1442013","public:commit:3f510866d3269534ccaff54d165b098585521e96","public:commit:4128430093dfb344aae62cbdfdf16a713e61e41b","public:commit:457caee6b0bb9d55f8be489928dc2d08cb51e2a0","public:commit:7e1149338ccebab3a2e8462b37f4f8a2d8107eff","public:commit:811837ce3df78016b0629aeb82b7a54fca15fffd","public:commit:885f2d1c45f2d1e459a8101575ba281760ef13fc","public:commit:8a28fc0fef415c5bb8034fdc5872444e46d54671","public:commit:9558dd9080eedecdad161ed316d9f279034a6455","public:commit:97adbeb1669c7b593e9935241b2ba88476e1f1fd","public:commit:ac041a05cde4e5737d8ef7a15c05aa7210fcf780","public:commit:cdcd793714aa9c0c392300ca77767a4e49a83bb2","public:commit:f97b936a67646f75b4e5111dbbb097b763d9f832"],"source_type":"public","date":"2024-06-16..2024-06-17","topics":["lifetime","ffi","testing","api","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
# Death events and preservation of client-localized messages {#death-events-and-preservation-of-client-localized-messages}

## Event interception and hierarchy evolve together {#event-interception-and-hierarchy-evolve-together}

The first death hooks only forward to the originals. Events then fire before native death handling, with ActorDeathEvent non-cancellable and PlayerDeathEvent inheriting both ActorDeathEvent and PlayerEvent. Each base ultimately derives from Event non-virtually; the player hook explicitly selects PlayerEvent for dispatch. Initial Python bindings directly repeat properties, then explicit ActorEvent/PlayerEvent bases centralize them and update exports/stubs. A subsequent guard prevents Mob::die from also dispatching ActorDeathEvent for player actors. This is a concrete duplicate-event correction. It does not prove that all actor listeners automatically receive player-death events, nor does it erase the C++ diamond by describing the Python hierarchy.

Drops, experience retention and inventory retention remain TODOs. Non-cancellable means plugin cancellation cannot stop death through this event; mutable text is a separate capability. Events hold references to the existing actor/player, not owned snapshots. No event execution, listener-order experiment or lifetime test is present in this review.

## A rendered string loses information the client needs {#a-rendered-string-loses-information-the-client-needs}

ActorDamageSource supplies a native death-message key and parameter list. The first customizable event translates this pair server-side and exposes a string. Plugins can change or empty it; nonempty output is sent to allowed permission subscribers excluding the deceased. That initial implementation carries an explicit TODO about losing client translation. The revision introduces a reusable Translatable value: an owned key plus parameters, with no client language baked in.

CommandSender now has string and Translatable overloads. Players serialize a Translate TextPacket and localization flag; console uses server I18n; native command output forwards key/parameters through its own output API; generic actors remain no-op senders. Thus the abstraction accommodates distinct destinations without pretending all destinations have clients. Player sendRawMessage is removed because sendMessage(string) now covers that path. Python mirrors the overloads and exports Translatable. Its params annotation is optional in the sense of accepting None, but the binding does not give a default, an important difference between nullable and omittable.

The final death broadcast compares the post-event string with the server-rendered original. If unchanged, it sends the original key/parameters to each permitted living recipient so their client can localize. If changed, it sends the plugin's exact raw string. Empty suppresses this custom outgoing branch. The server logs its rendered version. This is an evidence-backed design choice: preserve a richer native representation unless customization invalidates it, then honor the customized representation. It is not a general rule to infer semantic equality from text in every localization system; here equality is precisely the implemented dirty check.

The recipient mechanism also changes from general permission subscriptions to online players plus explicit logging. The deceased is skipped. The original native die method is still called afterward, so no claim is made that this hook alone suppresses every native death announcement or accounts for all gamerules. There is no live observation of duplication/suppression in this workunit.

## Causal and collaborator context {#causal-and-collaborator-context}

1184 starts from 1182 while the independent Dependabot merge 1183 lands on main. 1184–1188 build the translation branch; 1189 merges main back. Full parent diffs and a full-tree union proof show the branches touch disjoint content: dependency workflow vs translation code. This is not a hidden conflict-resolution rationale. The bot owns its version bump, Vincent owns the translation commits/integration, and no PR conversation was read here. Canonical patches preserve overlap without counting repeated imported code as new authorship.

## Tests and bounded lessons {#tests-and-bounded-lessons}

No death/localization tests change in this sequence. Assertions about correctness are limited to source control flow and representation. Useful lessons concern event timing, non-cancellability vs customization, keeping bindings/base classes aligned, duplicate hook dispatch and retaining localization keys across API layers. Tiny follow-up fixes and incomplete stages remain visible rather than being cleaned away in hindsight.

## Commit-by-commit dispositions {#commit-by-commit-dispositions}

<a id="commit-1156"></a>
### 1156: feat: add hooks for ServerPlayer::die and Mob::die {#commit-1156}

Source: [f97b936a67646f75b4e5111dbbb097b763d9f832](https://github.com/EndstoneMC/endstone/commit/f97b936a67646f75b4e5111dbbb097b763d9f832) · 2024-06-16T17:37:28Z · staging

Adds explicit-name hooks for ServerPlayer::die and Mob::die and two new manifest functions per platform, retaining all prior offsets. Both initially forward to original only. This is interception groundwork; events arrive at 1157.

<a id="commit-1157"></a>
### 1157: feat: add ActorDeathEvent and PlayerDeathEvent {#commit-1157}

Source: [885f2d1c45f2d1e459a8101575ba281760ef13fc](https://github.com/EndstoneMC/endstone/commit/885f2d1c45f2d1e459a8101575ba281760ef13fc) · 2024-06-16T17:52:18Z · substantive

Adds non-cancellable ActorDeathEvent and multiply inherited PlayerDeathEvent. Player hook dispatches through the PlayerEvent subobject before original death; Mob dispatches ActorDeathEvent. TODOs explicitly leave drops/experience/inventory policy unimplemented. Player exclusion from Mob death is missing until 1160.

<a id="commit-1158"></a>
### 1158: feat: add python bindings for ActorDeathEvent and PlayerDeathEvent {#commit-1158}

Source: [3f510866d3269534ccaff54d165b098585521e96](https://github.com/EndstoneMC/endstone/commit/3f510866d3269534ccaff54d165b098585521e96) · 2024-06-16T17:56:33Z · staging

Adds initial Python death-event classes/property accessors without all base-event classes. 1159 normalizes the inheritance/export/stub representation; this intermediate binding declaration is not treated as a settled API design.

<a id="commit-1159"></a>
### 1159: feat: add python bindings for ActorEvent and PlayerEvent {#commit-1159}

Source: [97adbeb1669c7b593e9935241b2ba88476e1f1fd](https://github.com/EndstoneMC/endstone/commit/97adbeb1669c7b593e9935241b2ba88476e1f1fd) · 2024-06-16T18:07:21Z · substantive

Exposes ActorEvent and PlayerEvent base classes, moves shared actor/player properties to them and updates all subclasses, exports and stubs. PlayerDeathEvent advertises both ActorDeathEvent and PlayerEvent bases. Also disables bugprone-unused-raii in clang-tidy, with no stated rationale. The C++ event diamond remains non-virtual and dispatch explicitly selects one base.

<a id="commit-1160"></a>
### 1160: fix: do not call ActorDeathEvent for player actors {#commit-1160}

Source: [ac041a05cde4e5737d8ef7a15c05aa7210fcf780](https://github.com/EndstoneMC/endstone/commit/ac041a05cde4e5737d8ef7a15c05aa7210fcf780) · 2024-06-16T18:13:53Z · corrective

Guards Mob::die event dispatch with !isPlayer, preserving original call for all mobs. The source and title explicitly avoid an extra ActorDeathEvent for players; no broad inheritance-based listener propagation is demonstrated by this guard.

<a id="commit-1180"></a>
### 1180: feat: add ActorDamageSource {#commit-1180}

Source: [cdcd793714aa9c0c392300ca77767a4e49a83bb2](https://github.com/EndstoneMC/endstone/commit/cdcd793714aa9c0c392300ca77767a4e49a83bb2) · 2024-06-17T13:49:38Z · substantive

Models ActorDamageSource's virtual interface including death-message key/parameters, source classifications, entity IDs/types and clone. The new death-message API later calls the host virtual; its correctness depends on ABI alignment and is not replaced with a guessed local cause table.

<a id="commit-1181"></a>
### 1181: feat: add death message to PlayerDeathEvent {#commit-1181}

Source: [9558dd9080eedecdad161ed316d9f279034a6455](https://github.com/EndstoneMC/endstone/commit/9558dd9080eedecdad161ed316d9f279034a6455) · 2024-06-17T13:51:32Z · substantive

Adds mutable death_message to PlayerDeathEvent. The hook obtains native key/parameters, translates server-side, dispatches plugins and sends nonempty text to permitted subscribers other than the dead player. Adds named admin/user broadcast constants. The TODO acknowledges lost client translation; original death still runs afterward, so this patch alone does not prove global suppression of native announcements.

<a id="commit-1182"></a>
### 1182: feat: add property `death_message` to PlayerDeathEvent's python binding {#commit-1182}

Source: [7e1149338ccebab3a2e8462b37f4f8a2d8107eff](https://github.com/EndstoneMC/endstone/commit/7e1149338ccebab3a2e8462b37f4f8a2d8107eff) · 2024-06-17T13:55:25Z · api_change

Exposes death_message get/set to Python/stubs and clarifies other mutable property descriptions. Runtime death dispatch is unchanged. Empty string suppresses this hook's outgoing branch; broader native-message behavior remains unknown.

<a id="commit-1184"></a>
### 1184: feat: add Translatable {#commit-1184}

Source: [457caee6b0bb9d55f8be489928dc2d08cb51e2a0](https://github.com/EndstoneMC/endstone/commit/457caee6b0bb9d55f8be489928dc2d08cb51e2a0) · 2024-06-17T16:33:11Z · substantive

Adds Translatable as an owned key plus string-parameter vector with read-only accessors, representing client-translatable text separately from rendered strings. This commit branches from 1182, not the chronologically preceding Dependabot merge 1183; causal order is explicitly verified.

<a id="commit-1185"></a>
### 1185: feat: add translatable message interface to CommandSender {#commit-1185}

Source: [811837ce3df78016b0629aeb82b7a54fca15fffd](https://github.com/EndstoneMC/endstone/commit/811837ce3df78016b0629aeb82b7a54fca15fffd) · 2024-06-17T17:31:27Z · api_change

Adds translatable sendMessage/sendErrorMessage overloads to the abstract CommandSender interface. This requires concrete implementers to supply new methods; implementations follow at 1186, so no standalone compatibility guarantee.

<a id="commit-1186"></a>
### 1186: feat: implement translatable message interfaces {#commit-1186}

Source: [4128430093dfb344aae62cbdfdf16a713e61e41b](https://github.com/EndstoneMC/endstone/commit/4128430093dfb344aae62cbdfdf16a713e61e41b) · 2024-06-17T17:35:29Z · substantive

Implements translatable command output via key/parameters, console output through server I18n and player output as Translate TextPacket with localize=true. Generic actor methods remain empty. Removes redundant Player::sendRawMessage in favor of sendMessage(string), initializes CommandOutputParameter count and makes Translatable implicitly constructible for brace calls. Error translation for players does not add the raw error path's red prefix.

<a id="commit-1187"></a>
### 1187: feat: add new methods to python bindings {#commit-1187}

Source: [8a28fc0fef415c5bb8034fdc5872444e46d54671](https://github.com/EndstoneMC/endstone/commit/8a28fc0fef415c5bb8034fdc5872444e46d54671) · 2024-06-17T17:35:52Z · api_change

Adds Python Translatable/export/stub and overloaded command-sender message APIs; removes send_raw_message. The optional-vector argument accepts None but is declared without a default, so Python callers still pass params explicitly at this point. No automatic conversion of arbitrary strings into translated keys is configured in Python.

<a id="commit-1188"></a>
### 1188: feat: improve logic of sending death message to players {#commit-1188}

Source: [2dbd28f7a9b28ab0e2d9cab6ae9e5867b1442013](https://github.com/EndstoneMC/endstone/commit/2dbd28f7a9b28ab0e2d9cab6ae9e5867b1442013) · 2024-06-17T17:36:33Z · substantive

Death broadcast now logs server-rendered text and iterates online players with user-broadcast permission, excluding the deceased. If plugins changed the string, sends raw replacement; otherwise preserves original translation key/parameters for each client's localization. This is a concrete preserve-native-representation-until-customized policy. It no longer uses general permission subscribers, and still invokes original death afterward.
