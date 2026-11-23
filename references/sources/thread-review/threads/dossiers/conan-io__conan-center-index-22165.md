<!-- retrieval: {"source_ids":["public:thread:conan-io/conan-center-index:22165"],"source_type":"public","date":"2024-01-05","topics":["concurrency","ffi","testing","build","api","review","selection"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="conan-io-conan-center-index-22165-minhook-add-minhook-cci-20240114-recipe"></a>
# conan-io/conan-center-index#22165: minhook: add minhook/cci.20240114 recipe {#conan-io-conan-center-index-22165-minhook-add-minhook-cci-20240114-recipe}

Source: https://github.com/conan-io/conan-center-index/pull/22165

Thread state: closed; merged: True.

## Problem and constraints {#problem-and-constraints}
Package MinHook for Windows x86/x64 in Conan so consumers can use a lightweight alternative to Detours without maintaining bespoke integration. Vincent explicitly disclaims authorship of MinHook.

## Reasoning, alternatives, and revision sequence {#reasoning-alternatives-and-revision-sequence}
Initial 1.3.3 submission encountered access gating and missing final-newline hook failures, then v1/v2 CI went green. AbrilRBS asked about a fresh upstream release after the 2017 release. Vincent noted a prior unanswered request and proposed a date-based cci snapshot, citing Detours precedent; AbrilRBS agreed. valgur requested CMake 3.15 rather than 3.5 to align with Conan and avoid shared/fPIC policy trouble; Vincent accepted. Months later memsharded volunteered a future-proof versioning scheme. The final artifact is 1.3.3.cci.20240629, despite the stale PR title/body saying cci.20240114.

## Implementation and attribution {#implementation-and-attribution}
All six final files were read. conandata pins upstream commit 91cc9466e383d13a43d7cf33c7c8fdccb27095d3 and SHA256, with no final upstream patch file. Recipe requires Conan >=1.53, strips C++ ABI settings because library is C, rejects non-Windows/non-x86-family targets, supports static/shared, uses CMakeDeps/Toolchain, installs license, removes upstream lib/minhook CMake metadata, and chooses x32/x64 plus Debug suffix for library names. Consumer test resolves minhook::minhook, uses VirtualRunEnv and can_run for cross-build safety, and hooks a local DummyMessageBoxW rather than opening a real modal UI. It initializes, creates/enables, calls through trampoline with altered text, disables, calls again, and uninitializes; each API status has failure exit.

Diff evidence (patch inspected, not bundled): [pinned public three-dot comparison](https://github.com/conan-io/conan-center-index/compare/1958cf235e54905839d41b541a0e91ab2e16634f...d40b30ea894b911c5b0151dd52be2d47185ef029). Declared changed files: 6.

## Verification, outcome, and remaining limits {#verification-outcome-and-remaining-limits}
Conan v1 and v2 bots report success on the final renamed version; maintainers approved and merged. Test demonstrates package link/load and hook lifecycle but checks statuses rather than asserting printed Hooked/Not hooked text. Fixed short strings avoid the dummy formatter’s unsigned padding-size underflow for long strings; it is not a general UI renderer. Earlier review patch requiring CMake minimum increase is historical and absent from final six-file patch.

## Reusable decision and costs {#reusable-decision-and-costs}
When upstream releases stall, pin an auditable snapshot with integrity metadata and a version scheme that can later coexist with releases. Validate package boundaries with a runnable consumer; preserve maintainer contributions to version policy and reviewer contributions to build compatibility.

## Evidence coverage {#evidence-coverage}
No upstream source was executed.

Cited source links:
- [CLAassistant · 2024-01-05T02:49:59Z](https://github.com/conan-io/conan-center-index/pull/22165#issuecomment-1878051128).
- [conan-center-bot · 2024-01-05T02:52:46Z](https://github.com/conan-io/conan-center-index/pull/22165#issuecomment-1878052763).
- [conan-center-bot · 2024-01-05T02:55:38Z](https://github.com/conan-io/conan-center-index/pull/22165#issuecomment-1878054520).
- [conan-center-bot · 2024-01-05T02:57:56Z](https://github.com/conan-io/conan-center-index/pull/22165#issuecomment-1878055868).
- [conan-center-bot · 2024-01-05T09:17:52Z](https://github.com/conan-io/conan-center-index/pull/22165#issuecomment-1878357710).
- [conan-center-bot · 2024-01-05T09:49:52Z](https://github.com/conan-io/conan-center-index/pull/22165#issuecomment-1878396881).
- [conan-center-bot · 2024-01-05T10:24:45Z](https://github.com/conan-io/conan-center-index/pull/22165#issuecomment-1878444576).
- [AbrilRBS · 2024-01-05T23:54:41Z](https://github.com/conan-io/conan-center-index/pull/22165#issuecomment-1879394180).
- [wu-vincent · 2024-01-08T10:11:45Z](https://github.com/conan-io/conan-center-index/pull/22165#issuecomment-1880708267).
- [conan-center-bot · 2024-01-09T14:19:11Z](https://github.com/conan-io/conan-center-index/pull/22165#issuecomment-1883132975).
- [AbrilRBS · 2024-01-11T00:16:39Z](https://github.com/conan-io/conan-center-index/pull/22165#issuecomment-1885968508).
- [conan-center-bot · 2024-01-15T00:28:40Z](https://github.com/conan-io/conan-center-index/pull/22165#issuecomment-1891131790).
- [valgur · 2024-03-24T15:34:30Z](https://github.com/conan-io/conan-center-index/pull/22165#discussion_r1536844065) — `recipes/minhook/all/patches/cci.20240114-0001-increase-cmake-min.patch`, line 10.
- [valgur · 2024-03-24T15:34:41Z](https://github.com/conan-io/conan-center-index/pull/22165#pullrequestreview-1956585541).
- [wu-vincent · 2024-03-24T21:39:02Z](https://github.com/conan-io/conan-center-index/pull/22165#issuecomment-2016953097).
- [conan-center-bot · 2024-03-24T21:56:22Z](https://github.com/conan-io/conan-center-index/pull/22165#issuecomment-2016958033).
- [valgur · 2024-03-24T22:50:59Z](https://github.com/conan-io/conan-center-index/pull/22165#pullrequestreview-1956676725).
- [memsharded · 2024-07-29T11:06:28Z](https://github.com/conan-io/conan-center-index/pull/22165#discussion_r1695026441) — `recipes/minhook/all/conandata.yml`, line 2.
- [memsharded · 2024-07-29T11:08:44Z](https://github.com/conan-io/conan-center-index/pull/22165#pullrequestreview-2204624050).
- [AbrilRBS · 2024-07-29T17:35:30Z](https://github.com/conan-io/conan-center-index/pull/22165#pullrequestreview-2205589726).
- [conan-center-bot · 2024-07-29T20:07:13Z](https://github.com/conan-io/conan-center-index/pull/22165#issuecomment-2256801465).
- [memsharded · 2024-07-29T21:46:47Z](https://github.com/conan-io/conan-center-index/pull/22165#pullrequestreview-2206155740).
