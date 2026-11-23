<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endweave:16"],"source_type":"public","date":"2026-04-16","topics":["testing","review","selection","networking"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->

Source: https://github.com/EndstoneMC/endweave/issues/16

Primary text and available images were inspected; the case describes attachment coverage and has no runtime reproduction.

## Evidence and attribution {#evidence-and-attribution}

Primary author: I-IKUN2004. Created 2026-04-16T02:15:50Z; recorded state closed; merged not applicable.

Image-only error report. Wu asks for0.4.3 retest plus binary packet dump so a fix can be verified. Another user reports errors persist and attaches image/log. Text contains no diagnosis or resolution; image/log evidence remains necessary.

## Attachment inspection {#attachment-inspection}

Both PNGs show CLIENTBOUND SERVER_SCRIPT_DEBUG_DRAWER328/0x148,924→898 translation failing while reading common-shape Dimension ID with VAR_INT; ValueError: Varint too long. Full8101-line log was reduced only by identical lines/timestamps to567 distinct lines, all read. It confirms Endweave0.4.3/Endstone0.11.4, detectedserver944, and291 repetitions of this same stack over~15seconds until disconnect;63other mods are present. Shutdown separately logs a PLand access violation/dependency warnings, not evidence that Endweave caused that shutdown exception. Needed packet binary is named but not attached, so log cannot establish correct wire schema or repair.

## Code and verification boundary {#code-and-verification-boundary}

No implementation fix independently verified. The referenced binary packet payload was not supplied. No upstream code was executed and no tests were run in this review. Runtime assertions are source-reported unless explicitly identified as static code findings.

Source and available attachment links are listed under Traceability; the separate acquisition and inspection ledger is not included in this distribution. A screenshot corroborates only visible content, not runtime causality. All distinct timestamp-normalized log lines read; repeated copies not reread. Referenced binary packet payload was not supplied.

## Traceability {#traceability}


- https://github.com/EndstoneMC/endweave/issues/16
- https://github.com/EndstoneMC/endweave/issues/16#issuecomment-4358807317
- https://github.com/EndstoneMC/endweave/issues/16#issuecomment-4408973471
- https://github.com/EndstoneMC/endweave/issues/16#issuecomment-4410915716
- https://github.com/user-attachments/assets/6c976a73-7911-45e1-b421-872dee5aa24d
- https://github.com/user-attachments/assets/dc1ec209-bf8f-4bf4-84f0-cf455ef25c5d
- https://github.com/user-attachments/files/27543618/2026-05-09.log
