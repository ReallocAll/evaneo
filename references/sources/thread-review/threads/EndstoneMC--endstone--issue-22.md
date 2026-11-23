<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:22"],"source_type":"public","date":"2024-06-25","topics":["concurrency","testing","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-22-bug-unicodedecodeerror-during-server-startup"></a>
# EndstoneMC/endstone #22: [bug] UnicodeDecodeError during server startup {#endstonemc-endstone-22-bug-unicodedecodeerror-during-server-startup}

Source: https://github.com/EndstoneMC/endstone/issues/22

## Review scope and state {#review-scope-and-state}

- Thread author: marcosvkp; state at review: closed; merged: not applicable.
- Evidence: The public issue and code/reproduction described below were reviewed statically; no code execution or tests were performed.
- Limits: Source snapshot only; no independent runtime verification.

## Engineering reading and attribution {#engineering-reading-and-attribution}

marcosvkp reports Windows startup UnicodeDecodeError while reading CheckNetIsolation output. Wu hypothesizes non-UTF-8 system output and asks for sys.stdout.encoding, without a confirming reply. Linked commit f5202796895ce911faf4d27f1c82dc2da6857b47 was read in the public mirror: remove text=True/UTF-8 decoding and search the ASCII SID inside str(ret.stdout). The fix avoids decoding localized output rather than selecting a guessed codec. Suitable for finding that identifier, it is not a general text-decoding strategy. No reproduced post-fix test is shown.


## Source index {#source-index}

- https://github.com/EndstoneMC/endstone/issues/22
- https://github.com/EndstoneMC/endstone/issues/22#issuecomment-2188442567
- https://github.com/EndstoneMC/endstone/issues/22#issuecomment-2197758177
- https://github.com/EndstoneMC/endstone/commit/f5202796895ce911faf4d27f1c82dc2da6857b47
