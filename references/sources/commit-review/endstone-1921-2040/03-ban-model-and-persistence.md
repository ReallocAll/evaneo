<!-- retrieval: {"source_ids":["public:commit:00f3b63d88c0c620b2956317ec953f7faf729b70","public:commit:0d4eadb38039b6e092c2a7567c167f5f504c7b4e","public:commit:0f38cb7acfe22c7e062d26865ddf86c6d738c235","public:commit:17b255ee537f4c33476c4199975f3a04f8ec94e4","public:commit:1b38dfc0f0d211d7f285bee20415b651202a8f57","public:commit:20dc52da104ec6aa9af61a784af127492cf8cbcc","public:commit:27b2756de70f7399cd96940d49841dab0f102a8f","public:commit:2ac388f9265ae0dba67bafb7aad3b3098ba2b741","public:commit:2bb9b308b165bdfba84b094b3733b733e96f7b70","public:commit:5113f6bbf613cfb4641f38deb9600e9556436577","public:commit:5cd6af6c36c8f0c7435bed434fc8b1e5bb4b723f","public:commit:65159135756d228ced49f5bbe194582ee322c363","public:commit:71ddd73c8f7e70fa1f28e414388ed069c8fd4b1b","public:commit:7366a2eba1d80028168a57ef2f2b7ef3d01516cc","public:commit:738ac58be994dbbaea4c66010b401c53b3b1499d","public:commit:73ac70124e13b10dffdc04d7bd02d72c4e0c6e02","public:commit:8fafd487f3cecdfbaeeea15e9c052c4943deedb1","public:commit:983360b46ee7eaaa0c382482bbb900b3609457de","public:commit:98e0b862504fee25504f56d39b9b78ac64d49327","public:commit:9b207c498133b15508a3221abc2d86dc824bc70d","public:commit:9c660b0bbbc0d5e583a6db8ef05c878afba150d8","public:commit:9c92d4207f212dd2dd5489ce95be8ea0a737717e","public:commit:9d5180a91bee81ecae76c13b7c9efa8c4e5d7156","public:commit:a6652196d55cdd4a5c056d59191612d1f3d18b81","public:commit:aea1eea730b358f9b4dc4a80e9fa7e480de4f394","public:commit:bc0100c127d76a143d5c400a744ea04bbcfee5b0","public:commit:d81252f741d20616359caaeef2f08911fa642f9c","public:commit:edaf58611f51a53127b0b6e5f12180a0bef43853","public:commit:f97531963a9eac5770c09b3d2927ce8443d644fd"],"source_type":"public","date":"2024-11-07..2024-12-23","topics":["lifetime","ffi","testing","performance","recovery","api","review","selection","refactoring","networking"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
# Ban APIs: experiments, persistence and enforcement {#ban-apis-experiments-persistence-and-enforcement}

## Model changes are not one stable design {#model-changes-are-not-one-stable-design}

1956/1957 register command scaffolds that return without implementing bans.1960/1964 introduce generic list/entry contracts, including save/remove promises;1965/1970 experiment with PlayerProfile and inheritance.1971 removes that profile and the generic list in favor of concrete value storage.2027 later reintroduces generic BanList<T>, now sharing implemented persistence across player and IP lists, and2038 makes matching an explicit policy instead of relying on free-function lookup. These reversals support a case-specific evolution, not a universal generic-first or inheritance-first preference.

1972 initializes creation time, reason and source; setters allow empty strings.1973 implements vector storage, initially leaves existing records unchanged despite an upsert contract and mishandles optional expiration.1974 adds JSON save/load but initially reads the saved array as an object, omits reason on loading and disagrees on timestamp representation.1975/1976/1977 repair those issues through Result<void>, array iteration, reason restoration, ISO8601 formatting and second-flooring at serialization while retaining full internal clock precision.1978 removes invalid hardcoded-current-time assertions.1979 erases matching entries before insertion, making upsert replace the record and creation time.1983 guards expiration with has_value, so permanent bans no longer compare like expired optional values.

Changed tests were read in full, including fixture/error and CRUD expectations. They are source evidence of intended behavior and repair pressure. No tests, server or build were executed; the chronology alone does not establish test-driven development.

## Identity and persistence limits at2040 {#identity-and-persistence-limits-at2040}

Player matching remains case-insensitive name AND UUID AND XUID, with missing identifiers on either side treated as wildcards and empty XUID treated as unavailable. It is not a search by any independently matching identity, despite some later binding prose saying “or”. A renamed player with unchanged UUID does not match if the name differs. IP matching is exact text.2028 validates IPv4/IPv6 syntax with inet_pton but stores the original spelling; equivalent IPv6 spellings are not canonicalized by this code.

The implementation returns raw pointers/references into a vector. Erase, replacement, reallocation, expiry cleanup and load invalidate them. Upsert also resets creation and unspecified metadata to defaults. Keeping the owning list alive cannot preserve individual element addresses. The subsequent Python binding dossier follows this lifetime exposure without claiming it is solved.

Persistence uses an ofstream opened directly at the destination. It checks open failure, but ordinary streams do not throw on all failed writes without exception masks and the code does not check stream state after insertion. Mutation callers discard the Result from save. Load clears old entries before opening/parsing and appends incrementally, so a later failure can leave an empty or partial list. Invalid UUID/date parsing is tolerated; an invalid expiration string can leave the default permanent ban. getEntries does not purge expired records, whereas isBanned mutates through const_cast to remove them. The code supplies no atomic replacement, rollback or durable-write confirmation.

## Enforcement is a separate chain {#enforcement-is-a-separate-chain}

1982 implements /ban and identity capture;1984 checks the player list in both primary and subclient connection paths after native player creation and before the login event.2023 adds IP command scaffolds;2025/2026 add storage/server ownership;2028 implements commands and connection checks.2029 kicks only a name-resolved player, then2030 scans all online players matching the address, covering explicit-address bans and shared IPs. The selected player can encounter the direct kick and subsequent scan.2021 is unrelated encrypted-resource repair and receives no ban credit.

Failure reports are not coupled to persistence success: a command can report success after an in-memory mutation whose save failed. Kick goes through the existing callback/event policy, so “ban added” is not proof a connection was terminated. No operational enforcement test was run.

## Apply with limits {#apply-with-limits}

Useful review questions are: What is identity equality? Does “update” preserve creation metadata? When do returned references become stale? Is a permanent expiration represented distinctly? Does a failed write leave the old durable state intact? Do both connection entry paths and already-online users enforce the same rule? The answers here are historical source findings, not security guidance about the current Endstone release.

## Individual commit evidence {#individual-commit-evidence}

<a id="commit-1956"></a>
### Commit 1956 {#commit-1956}

5cd6af6c36c8f0c7435bed434fc8b1e5bb4b723f · 2024-11-07T11:47:46Z

[feat: add `/ban` command (to be implemented)](https://github.com/EndstoneMC/endstone/commit/5cd6af6c36c8f0c7435bed434fc8b1e5bb4b723f)


Registers permission-checked /ban command with TODO body returning true; implementation absent, despite feature title.

Static review only; no upstream execution.

<a id="commit-1957"></a>
### Commit 1957 {#commit-1957}

73ac70124e13b10dffdc04d7bd02d72c4e0c6e02 · 2024-11-07T13:10:47Z

[feat: add `/banlist` and `/pardon` command (to be implemented)](https://github.com/EndstoneMC/endstone/commit/73ac70124e13b10dffdc04d7bd02d72c4e0c6e02)


Adds /banlist and /pardon(alias unban) placeholders, operator-default ban permissions and enum autocomplete expansion. /ban accepts optional reason and localized description. Bodies remain TODO.

Static review only; no upstream execution.

<a id="commit-1960"></a>
### Commit 1960 {#commit-1960}

00f3b63d88c0c620b2956317ec953f7faf729b70 · 2024-11-10T11:56:39Z

[feat: add BanList class](https://github.com/EndstoneMC/endstone/commit/00f3b63d88c0c620b2956317ec953f7faf729b70)


Introduces generic BanList<T> interface with lookup/upsert, expires/duration overloads, entries/status/removal. References BanEntry<T> before later model completion. Documentation promise of upsert precedes implementation; preserve as scaffold.

Static review only; no upstream execution.

<a id="commit-1964"></a>
### Commit 1964 {#commit-1964}

27b2756de70f7399cd96940d49841dab0f102a8f · 2024-11-17T15:16:14Z

[feat: add BanEntry class](https://github.com/EndstoneMC/endstone/commit/27b2756de70f7399cd96940d49841dab0f102a8f)


Introduces generic BanEntry<T> getter/mutators, save/remove with doc promise stale saved entries reban; duplicate pragma and missing namespace repaired1965. Later architecture changes remove template and save/remove APIs; do not treat early promises as endpoint.

Static review only; no upstream execution.

<a id="commit-1965"></a>
### Commit 1965 {#commit-1965}

aea1eea730b358f9b4dc4a80e9fa7e480de4f394 · 2024-11-17T15:26:24Z

[feat: add PlayerProfile class](https://github.com/EndstoneMC/endstone/commit/aea1eea730b358f9b4dc4a80e9fa7e480de4f394)


Adds PlayerProfile optional UUID/name/XUID and completeness contract, fixes BanEntry namespace/duplicate pragma. Profile abstraction is removed1971 before ban implementation settles.

Static review only; no upstream execution.

<a id="commit-1970"></a>
### Commit 1970 {#commit-1970}

738ac58be994dbbaea4c66010b401c53b3b1499d · 2024-11-26T21:12:27Z

[feat(ban): implement base ban entry](https://github.com/EndstoneMC/endstone/commit/738ac58be994dbbaea4c66010b401c53b3b1499d)


Replaces templated BanEntry with abstract non-template base, adds PlayerBanEntry profile target and implementation getters/setters. Player entry still abstract and persistence unresolved. This layered inheritance experiment is removed immediately1971.

Static review only; no upstream execution.

<a id="commit-1971"></a>
### Commit 1971 {#commit-1971}

8fafd487f3cecdfbaeeea15e9c052c4943deedb1 · 2024-11-27T11:22:12Z

[refactor: remove player_profile.h](https://github.com/EndstoneMC/endstone/commit/8fafd487f3cecdfbaeeea15e9c052c4943deedb1)


Deletes PlayerProfile and generic BanList, inlines concrete BanEntry storage and direct name/UUID/XUID PlayerBanEntry fields; introduces player-specific list interface. Removes entry save/remove methods and old implicit reban contract, leaving stale @see save references. Not mere file removal: ownership/API architecture is simplified before generic reuse returns2027.

Static review only; no upstream execution.

<a id="commit-1972"></a>
### Commit 1972 {#commit-1972}

7366a2eba1d80028168a57ef2f2b7ef3d01516cc · 2024-11-27T11:37:46Z

[feat: add constructor for PlayerBanEntry](https://github.com/EndstoneMC/endstone/commit/7366a2eba1d80028168a57ef2f2b7ef3d01516cc)


Adds PlayerBanEntry identity constructor; BanEntry defaults creation=now, source=(Unknown), permanent expiration, operator reason. Setters now preserve supplied empty strings rather than substitute defaults; getters return owning strings instead of views.

Static review only; no upstream execution.

<a id="commit-1973"></a>
### Commit 1973 {#commit-1973}

edaf58611f51a53127b0b6e5f12180a0bef43853 · 2024-11-27T12:19:31Z

[feat: implement PlayerBanList](https://github.com/EndstoneMC/endstone/commit/edaf58611f51a53127b0b6e5f12180a0bef43853)


Implements vector-backed lookup/add/remove and all supplied identity constraints: name always matches plus requested UUID/XUID. Existing match is returned unchanged, contrary to upsert promise. isBanned const-casts to removeExpired; optional expiration compared directly to now wrongly treats absent expiration as older (permanent bans at risk). Exposes pointers into vector invalidated by mutation; save/load/constructor still incomplete.

Static review only; no upstream execution.

<a id="commit-1974"></a>
### Commit 1974 {#commit-1974}

65159135756d228ced49f5bbe194582ee322c363 · 2024-11-27T17:39:14Z

[feat: add save and load functionality to player ban list](https://github.com/EndstoneMC/endstone/commit/65159135756d228ced49f5bbe194582ee322c363)


Adds date dependency and JSON array save, but initial load treats parsed array as one object and omits reason; serializer and parser time formats disagree. Clears entries before parsing, uses truncating direct writes and logs errors through global server. These concrete intermediate faults are repaired in later tests commits, not endpoint guarantees.

Static review only; no upstream execution.

<a id="commit-1975"></a>
### Commit 1975 {#commit-1975}

9c660b0bbbc0d5e583a6db8ef05c878afba150d8 · 2024-11-27T18:04:13Z

[test: add test for PlayerBanList::load](https://github.com/EndstoneMC/endstone/commit/9c660b0bbbc0d5e583a6db8ef05c878afba150d8)


Changes save/load to Result<void> removing global server requirement, implements constructor, iterates JSON array and restores reason field, uses consistent date format. Adds load test checking values/permanent expiration, but raw clock tick-count expectation is platform-specific. File stream failure not checked yet, fixed1977; source tests read only.

Static review only; no upstream execution.

<a id="commit-1976"></a>
### Commit 1976 {#commit-1976}

0d4eadb38039b6e092c2a7567c167f5f504c7b4e · 2024-11-27T20:40:27Z

[fix: save date time in ISO 8601 format](https://github.com/EndstoneMC/endstone/commit/0d4eadb38039b6e092c2a7567c167f5f504c7b4e)


Standardizes ISO8601 offset format and briefly narrows Date to seconds. Test checks +02:00 input normalized to UTC text rather than platform tick count. Subsequent1977 restores clock precision and floors only at persistence boundary.

Static review only; no upstream execution.

<a id="commit-1977"></a>
### Commit 1977 {#commit-1977}

9b207c498133b15508a3221abc2d86dc824bc70d · 2024-11-27T22:08:33Z

[test: add more tests for PlayerBanList](https://github.com/EndstoneMC/endstone/commit/9b207c498133b15508a3221abc2d86dc824bc70d)


Restores full system_clock precision, centralizes DateFormat, truncates only serialized timestamps to seconds, makes duration nonoptional, checks file-open failure, returns Result errors. Adds CRUD, duration, optional identity, save/load/nonexistent/invalid-path tests. An add test incorrectly expects fixed historical now;1978 removes it. Persistence still clears live list before parse and ignores mid-write stream state; permanent-expiration bug not repaired here.

Static review only; no upstream execution.

<a id="commit-1978"></a>
### Commit 1978 {#commit-1978}

71ddd73c8f7e70fa1f28e414388ed069c8fd4b1b · 2024-11-27T22:19:08Z

[test: fix tests](https://github.com/EndstoneMC/endstone/commit/71ddd73c8f7e70fa1f28e414388ed069c8fd4b1b)


Removes impossible hardcoded creation timestamp expectation and a second optional-fields creation assertion. Tests source edited, no execution observed.

Static review only; no upstream execution.

<a id="commit-1979"></a>
### Commit 1979 {#commit-1979}

bc0100c127d76a143d5c400a744ea04bbcfee5b0 · 2024-11-28T14:39:10Z

[feat(ban): update existing entry to prevent duplicate inserts](https://github.com/EndstoneMC/endstone/commit/bc0100c127d76a143d5c400a744ea04bbcfee5b0)


Replaces all matching entries before adding updated record, closing previously ignored updates and enriching name-only ban with supplied UUID/XUID. Missing identity on either side now acts wildcard, but name remains mandatory and present conflicts fail. Adds update/const-lookup/remove-by-name tests and distinct logger-name test. Replacement resets creation and invalidates vector pointers; save Result still ignored by add/remove.

Static review only; no upstream execution.

<a id="commit-1982"></a>
### Commit 1982 {#commit-1982}

2bb9b308b165bdfba84b094b3733b733e96f7b70 · 2024-11-28T21:29:42Z

[feat: implement `/ban` command (WIP)](https://github.com/EndstoneMC/endstone/commit/2bb9b308b165bdfba84b094b3733b733e96f7b70)


Implements permission/argument/already-banned checks, online player identity enrichment, optional reason, permanent add and kick; creates banned-players.json store and calls load during server init. Load/add save Results are ignored; command success does not prove persistence. Login enforcement only arrives1984. Server virtual layout and test mocks updated.

Static review only; no upstream execution.

<a id="commit-1983"></a>
### Commit 1983 {#commit-1983}

0f38cb7acfe22c7e062d26865ddf86c6d738c235 · 2024-11-28T23:09:10Z

[feat: implement `/unban` and `/banlist`](https://github.com/EndstoneMC/endstone/commit/0f38cb7acfe22c7e062d26865ddf86c6d738c235)


Implements /pardon and player /banlist, keeps IP listing TODO; case-insensitive name match and empty XUID wildcard. Crucially guards expiration.has_value before comparing time, repairing permanent bans removed by1973 isBanned. Banning records nonempty XUID only. No direct permanent-isBanned regression test added in this patch.

Static review only; no upstream execution.

<a id="commit-1984"></a>
### Commit 1984 {#commit-1984}

20dc52da104ec6aa9af61a784af127492cf8cbcc · 2024-11-28T23:09:24Z

[feat: add player ban check during connection](https://github.com/EndstoneMC/endstone/commit/20dc52da104ec6aa9af61a784af127492cf8cbcc)


Checks player ban after connection identity initialization in both trytLoadPlayer/_createNewPlayer, kicks and returns before PlayerLoginEvent. Native player creation already happened; this is rejection integration, not preallocation authentication. Kick remains callback-mediated.

Static review only; no upstream execution.

<a id="commit-2016"></a>
### Commit 2016 {#commit-2016}

5113f6bbf613cfb4641f38deb9600e9556436577 · 2024-12-18T18:37:34Z

[feat: add an overload for `/ban` command for player name auto-completion](https://github.com/EndstoneMC/endstone/commit/5113f6bbf613cfb4641f38deb9600e9556436577)


Adds /ban player-typed overload alongside string overload for name autocomplete; execution unchanged.

Static review only; no upstream execution.

<a id="commit-2023"></a>
### Commit 2023 {#commit-2023}

1b38dfc0f0d211d7f285bee20415b651202a8f57 · 2024-12-22T19:11:44Z

[feat: add `/ban-ip` and `/unban-ip` commands](https://github.com/EndstoneMC/endstone/commit/1b38dfc0f0d211d7f285bee20415b651202a8f57)


Registers ban-ip/pardon-ip aliases, permissions and autocomplete signatures but handlers remain TODO; lexer now allows hyphens in identifiers. Do not credit functional IP enforcement until2028.

Static review only; no upstream execution.

<a id="commit-2024"></a>
### Commit 2024 {#commit-2024}

d81252f741d20616359caaeef2f08911fa642f9c · 2024-12-22T19:14:24Z

[refactor: rename `Server::getPlayerBanList` to `Server::getBanList`](https://github.com/EndstoneMC/endstone/commit/d81252f741d20616359caaeef2f08911fa642f9c)


Renames getPlayerBanList→getBanList across interface, implementation, commands, network checks and test mocks. Breaking public method rename; behavior otherwise unchanged.

Static review only; no upstream execution.

<a id="commit-2025"></a>
### Commit 2025 {#commit-2025}

17b255ee537f4c33476c4199975f3a04f8ec94e4 · 2024-12-22T19:42:17Z

[feat: add IpBanList](https://github.com/EndstoneMC/endstone/commit/17b255ee537f4c33476c4199975f3a04f8ec94e4)


Adds vector-backed IpBanList with exact textual address matching, expiration, JSONload/save, remove/upsert. Reuses player-ban persistence weaknesses: mutations ignore save Result, truncating write without post-write state check, clear-before-load can lose prior/partially restore entries, pointers invalidated by mutations, malformed date treated as no expiration.

Static review only; no upstream execution.

<a id="commit-2026"></a>
### Commit 2026 {#commit-2026}

2ac388f9265ae0dba67bafb7aad3b3098ba2b741 · 2024-12-22T19:46:33Z

[feat: add `Server::getIpBanList`](https://github.com/EndstoneMC/endstone/commit/2ac388f9265ae0dba67bafb7aad3b3098ba2b741)


Server owns banned-ips.json list and loads it at init; load Result ignored like player list. Adds public getter and mocks; no IP connection check until2028.

Static review only; no upstream execution.

<a id="commit-2027"></a>
### Commit 2027 {#commit-2027}

983360b46ee7eaaa0c382482bbb900b3609457de · 2024-12-22T21:35:32Z

[refactor: rebase IpBanList and PlayerBanList to BanList<T> class](https://github.com/EndstoneMC/endstone/commit/983360b46ee7eaaa0c382482bbb900b3609457de)


Extracts common EndstoneBanList<T> storage/persistence and ADL JSON identity serializers, leaving player extended-identity overloads. Multiple-inheritance forwarding preserved; name/UUID/XUID match still conjunction with absent identifiers treated as wildcards. Free match lookup later replaced2038. No persistence or pointer-lifetime fix added.

Static review only; no upstream execution.

<a id="commit-2028"></a>
### Commit 2028 {#commit-2028}

f97531963a9eac5770c09b3d2927ce8443d644fd · 2024-12-22T21:54:34Z

[feat: implement `/ban-ip` and `/unban-ip` commands](https://github.com/EndstoneMC/endstone/commit/f97531963a9eac5770c09b3d2927ce8443d644fd)


Implements IPv4/IPv6 parse-or-online-name ban, IP listing/unban, and checks both connection paths before login event. Stores original textual address without canonicalization, so equivalent IPv6 spellings can mismatch. Does not immediately disconnect until2029/2030; unban success translation typo repaired2031. Save failures still not surfaced to command result.

Static review only; no upstream execution.

<a id="commit-2029"></a>
### Commit 2029 {#commit-2029}

9d5180a91bee81ecae76c13b7c9efa8c4e5d7156 · 2024-12-22T22:01:38Z

[fix: kick players on IP bans](https://github.com/EndstoneMC/endstone/commit/9d5180a91bee81ecae76c13b7c9efa8c4e5d7156)


Adds socket includes and immediate kick only when ban argument resolves a player; explicit-address bans still wait for reconnect until2030.

Static review only; no upstream execution.

<a id="commit-2030"></a>
### Commit 2030 {#commit-2030}

98e0b862504fee25504f56d39b9b78ac64d49327 · 2024-12-22T22:11:26Z

[fix: ensure players with a matching IP address are immediately kicked upon an IP ban](https://github.com/EndstoneMC/endstone/commit/98e0b862504fee25504f56d39b9b78ac64d49327)


Iterates all online players and kicks exact hostname matches, covering explicit address and shared-IP peers; already-named player may receive a second kick. Moves NOMINMAX from core-private to global. No network execution.

Static review only; no upstream execution.

<a id="commit-2031"></a>
### Commit 2031 {#commit-2031}

a6652196d55cdd4a5c056d59191612d1f3d18b81 · 2024-12-22T22:12:09Z

[fix: correct message key in PardonIpCommand](https://github.com/EndstoneMC/endstone/commit/a6652196d55cdd4a5c056d59191612d1f3d18b81)


Corrects pardon IP translation key commands.ununban.success→commands.unbanip.success; ban state logic unchanged.

Static review only; no upstream execution.

<a id="commit-2038"></a>
### Commit 2038 {#commit-2038}

9c92d4207f212dd2dd5489ce95be8ea0a737717e · 2024-12-23T01:15:02Z

[refactor: use matcher for ban entry matching](https://github.com/EndstoneMC/endstone/commit/9c92d4207f212dd2dd5489ce95be8ea0a737717e)


Injects explicit Matcher policy into common ban list and both concrete classes, removing reliance on late free match lookup. All identity comparisons stay the same; stale Ip match forward declaration remains. No canonicalization or persistence repair.

Static review only; no upstream execution.
