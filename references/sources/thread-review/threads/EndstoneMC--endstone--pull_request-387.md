<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:387"],"source_type":"public","date":"2026-04-25","topics":["testing","performance","documentation","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-387-docs-enhance-faq"></a>
# EndstoneMC/endstone #387: docs: enhance faq {#endstonemc-endstone-387-docs-enhance-faq}

Source: https://github.com/EndstoneMC/endstone/pull/387

## Evidence and attribution {#evidence-and-attribution}

Primary author: niko-at-chalupa. Created 2026-04-25T10:52:18Z; recorded state closed; merged True.

## Proposal and collaborative revision sequence {#proposal-and-collaborative-revision-sequence}

niko-at-chalupa initially added an ARM-emulation FAQ tip claiming excellent Apple M1/macOS performance. Aevarkan requested lower visual prominence (footnote), instructions rather than “users can look it up,” and either a dedicated tutorial or a link. The author chose a quick-start addition to the existing Docker section instead of a full Docker course.

Inline reviews corrected link anchors/tab activation, asked what works on Windows, split flags for beginners, moved docker run from installation to the existing start-server page, and standardized x86-64/macOS spelling. Aevarkan objected that “our testing” falsely implied maintainer testing; the final text drops that claim and says emulation can work, while official support remains x86-64 Windows/Ubuntu. The author tested macOS, explicitly lacked Windows hardware, and could not validate Windows. Aevarkan approved with platform caveats; wu-vincent accepted the change.

## Final patch and remaining defects {#final-patch-and-remaining-defects}

The 2,848-character diff adds --platform linux/amd64 for pull/run, a persistent ${PWD} volume, interactive terminal and container name, plus an official Docker beginner guide. The final emulation run command publishes -p 19132:19132 without /udp, unlike the existing Windows command shown immediately above; static inspection therefore identifies an operational protocol mismatch that styling approval missed. The FAQ link still targets the earlier tab label, while a reviewer had already observed an anchor warning; no rendered final-link check is shown.

## Reusable lesson {#reusable-lesson}

Distinguish tested platform, officially supported platform, plausible emulation and performance marketing. Attribution and novice information placement are engineering documentation concerns. Review acceptance does not replace testing copied commands or regenerated anchors. Contributor/reviewer ideas remain theirs; wu-vincent's short acceptance should not absorb the entire rationale.

## Additional source and attachment inspection {#additional-source-and-attachment-inspection}

Both design screenshots were inspected: the initial prominent ARM callout and the later footnote retain the “our testing” Apple M1/macOS Tahoe performance claim. These are intermediate review images, not the final accepted prose. They corroborate the prominence/attribution discussion rather than independent performance testing.

## Code and verification boundary {#code-and-verification-boundary}

Inspected all primary text, 33 discussion/review records including inline contexts and all 2,848 characters of final docs patch. Redacted HTML token material was respected; no hidden content reconstructed. No upstream code was executed and no tests were run in this review. Runtime assertions are source-reported unless explicitly identified as static code findings.

Source and available attachment links are listed under Traceability; the separate acquisition and inspection ledger is not included in this distribution. A screenshot corroborates only visible content, not runtime causality.

## Traceability {#traceability}


- https://github.com/EndstoneMC/endstone/pull/387
- https://github.com/EndstoneMC/endstone/pull/387#issuecomment-4319769993
- https://github.com/EndstoneMC/endstone/pull/387#issuecomment-4319901578
- https://github.com/EndstoneMC/endstone/pull/387#issuecomment-4319914176
- https://github.com/EndstoneMC/endstone/pull/387#issuecomment-4319935521
- https://github.com/EndstoneMC/endstone/pull/387#issuecomment-4319968897
- https://github.com/EndstoneMC/endstone/pull/387#issuecomment-4320014239
- https://github.com/EndstoneMC/endstone/pull/387#issuecomment-4321632150
- https://github.com/EndstoneMC/endstone/pull/387#issuecomment-4336411942
- https://github.com/EndstoneMC/endstone/pull/387#issuecomment-4336819130
- https://github.com/EndstoneMC/endstone/pull/387#discussion_r3141986888
- https://github.com/EndstoneMC/endstone/pull/387#discussion_r3142858281
- https://github.com/EndstoneMC/endstone/pull/387#discussion_r3142863131
- https://github.com/EndstoneMC/endstone/pull/387#discussion_r3142870773
- https://github.com/EndstoneMC/endstone/pull/387#discussion_r3142877802
- https://github.com/EndstoneMC/endstone/pull/387#discussion_r3142995956
- https://github.com/EndstoneMC/endstone/pull/387#discussion_r3143012426
- https://github.com/EndstoneMC/endstone/pull/387#discussion_r3143040495
- https://github.com/EndstoneMC/endstone/pull/387#discussion_r3143170029
- https://github.com/EndstoneMC/endstone/pull/387#discussion_r3143170239
- https://github.com/EndstoneMC/endstone/pull/387#discussion_r3143170703
- https://github.com/EndstoneMC/endstone/pull/387#discussion_r3143186430
- https://github.com/EndstoneMC/endstone/pull/387#discussion_r3143186849
- https://github.com/EndstoneMC/endstone/pull/387#discussion_r3143187910
- https://github.com/EndstoneMC/endstone/pull/387#discussion_r3143191759
- https://github.com/EndstoneMC/endstone/pull/387#pullrequestreview-4175585066
- https://github.com/EndstoneMC/endstone/pull/387#pullrequestreview-4176424729
- https://github.com/EndstoneMC/endstone/pull/387#pullrequestreview-4176534148
- https://github.com/EndstoneMC/endstone/pull/387#pullrequestreview-4176547014
- https://github.com/EndstoneMC/endstone/pull/387#pullrequestreview-4176572140
- https://github.com/EndstoneMC/endstone/pull/387#pullrequestreview-4176680868
- https://github.com/EndstoneMC/endstone/pull/387#pullrequestreview-4176681009
- https://github.com/EndstoneMC/endstone/pull/387#pullrequestreview-4176681334
- https://github.com/EndstoneMC/endstone/pull/387#pullrequestreview-4176693297
- https://github.com/user-attachments/assets/73b5626c-ee2b-43a9-a206-7267b65e4f6c
- https://github.com/user-attachments/assets/a4a07c96-b275-4f50-adae-0ea947041aea
