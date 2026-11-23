<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:255"],"source_type":"public","date":"2025-08-25","topics":["concurrency","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-255-bug-message-argument-bug"></a>
# EndstoneMC/endstone #255: [bug] message argument bug {#endstonemc-endstone-255-bug-message-argument-bug}

Source: https://github.com/EndstoneMC/endstone/issues/255

## Review scope and state {#review-scope-and-state}

- Thread author: PrimeStrat; state at review: closed; merged: not applicable.
- Evidence: The public issue and code/reproduction described below were reviewed statically; no code execution or tests were performed.
- Limits: Source snapshot only; no independent runtime verification.

## Engineering reading and attribution {#engineering-reading-and-attribution}

PrimeStrat revisits 251 with version-specific custom/vanilla failures. Wu cannot reproduce and suspects a registered custom command contaminating the shared lexer. Reporter initially suspects permission attachments but isolates /warn with a message argument followed by optional duration and enum arguments, and finds reload insufficient while full restart clears the issue. Wu explains message must be the final argument or BDS parsing for other commands can break; optional trailing arguments are not exempt. The reporter acknowledges the misunderstanding. This converts vague numeric/string symptoms into a global registry invariant and motivates validation at registration (258), rather than special-casing trailing digits or blaming every affected vanilla command.


## Source index {#source-index}

- https://github.com/EndstoneMC/endstone/issues/255
- https://github.com/EndstoneMC/endstone/issues/255#issuecomment-3227637124
- https://github.com/EndstoneMC/endstone/issues/255#issuecomment-3227645172
- https://github.com/EndstoneMC/endstone/issues/255#issuecomment-3228392375
- https://github.com/EndstoneMC/endstone/issues/255#issuecomment-3228399308
- https://github.com/EndstoneMC/endstone/issues/255#issuecomment-3228401147
- https://github.com/EndstoneMC/endstone/issues/255#issuecomment-3228420684
- https://github.com/EndstoneMC/endstone/issues/255#issuecomment-3228601381
- https://github.com/EndstoneMC/endstone/issues/255#issuecomment-3228623949
- https://github.com/EndstoneMC/endstone/issues/255#issuecomment-3228635970
